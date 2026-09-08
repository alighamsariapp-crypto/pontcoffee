#!/usr/bin/env python3
"""Entry and completion gates for generated WebTow projects."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PHASES = ["00", "01", "02", "03", "04", "05", "06", "07"]
STATES = {"LOCKED", "READY", "IN_PROGRESS", "PASS", "PASS_WITH_WARNINGS", "BLOCKED"}
DEFAULT_REQUIRED = ["FEATURE_SPEC.md", "PHASE_REPORT.md", "AUDIT.md"]


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise ValueError(f"missing machine-readable state: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc


def save_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def blockers(value: object) -> list[str]:
    if not isinstance(value, list):
        return ["blockers must be a JSON array"]
    return [str(item) for item in value if str(item).strip()]


def status_errors(label: str, value: object, allowed: set[str] = STATES) -> list[str]:
    if value not in allowed:
        return [f"{label} has invalid status: {value or 'MISSING'}"]
    return []


def phase_state(root: Path) -> tuple[Path, dict]:
    path = root / ".webtow/phase-status.json"
    return path, load_json(path)


def check_previous_phases(state: dict, phase_id: str) -> list[str]:
    phases = state.get("phases", {})
    errors: list[str] = []
    for previous in PHASES[: PHASES.index(phase_id)]:
        if phases.get(previous, {}).get("status") != "PASS":
            errors.append(f"previous phase {previous} is not PASS")
    return errors


def check_phase_completion(root: Path, phase_id: str) -> list[str]:
    _, state = phase_state(root)
    errors = status_errors("current_phase", state.get("current_phase"), set(PHASES))
    phases = state.get("phases", {})
    current = phases.get(phase_id)
    if not isinstance(current, dict):
        return errors + [f"missing status for phase {phase_id}"]
    if state.get("current_phase") != phase_id:
        errors.append(f"phase {phase_id} is not current; current_phase is {state.get('current_phase')}")
    errors.extend(check_previous_phases(state, phase_id))
    errors.extend(status_errors(f"phase {phase_id}", current.get("status")))
    if current.get("status") not in {"PASS", "PASS_WITH_WARNINGS"}:
        errors.append(f"phase {phase_id} completion requires PASS or PASS_WITH_WARNINGS")
    errors.extend(f"phase {phase_id}: {item}" for item in blockers(current.get("blockers", [])))
    report = current.get("report")
    if not report or not (root / str(report)).is_file():
        errors.append(f"phase {phase_id} report is missing: {report or '<not declared>'}")
    for item in current.get("required_evidence", []):
        if not (root / str(item)).is_file():
            errors.append(f"phase {phase_id} evidence is missing: {item}")
    for feature_id in current.get("required_features", []):
        errors.extend(check_feature_completion(root, str(feature_id), require_current_phase=False))
    return errors


def check_phase_entry(root: Path, phase_id: str) -> list[str]:
    _, state = phase_state(root)
    phases = state.get("phases", {})
    if phase_id == "00":
        return []
    previous = PHASES[PHASES.index(phase_id) - 1]
    errors: list[str] = []
    if state.get("current_phase") != previous:
        errors.append(f"entry denied: current_phase is {state.get('current_phase')}, expected {previous}")
    if phases.get(previous, {}).get("status") not in {"PASS", "PASS_WITH_WARNINGS"}:
        errors.append(f"entry denied: previous phase {previous} is not complete")
    target = phases.get(phase_id, {})
    if target.get("status") not in {"LOCKED", "READY"}:
        errors.append(f"entry denied: phase {phase_id} status is {target.get('status', 'MISSING')}")
    return errors


def feature_dir(root: Path, feature_id: str) -> Path:
    return root / ".webtow/features" / feature_id


def check_feature_completion(root: Path, feature_id: str, require_current_phase: bool = True) -> list[str]:
    directory = feature_dir(root, feature_id)
    state = load_json(directory / "status.json")
    _, phases_state = phase_state(root)
    errors: list[str] = []
    phase_id = str(state.get("phase", ""))
    if phase_id not in PHASES:
        errors.append(f"feature {feature_id} has invalid phase: {phase_id}")
    if require_current_phase and phases_state.get("current_phase") != phase_id:
        errors.append(f"feature {feature_id} is not in current phase {phases_state.get('current_phase')}")
    if state.get("id") != feature_id:
        errors.append(f"feature state id does not match directory: {state.get('id')}")
    errors.extend(status_errors(f"feature {feature_id}", state.get("status")))
    if state.get("status") not in {"PASS", "PASS_WITH_WARNINGS"}:
        errors.append(f"feature {feature_id} completion requires PASS or PASS_WITH_WARNINGS")
    errors.extend(f"feature {feature_id}: {item}" for item in blockers(state.get("blockers", [])))
    for item in state.get("required_artifacts", DEFAULT_REQUIRED):
        if not (directory / str(item)).is_file():
            errors.append(f"feature {feature_id} artifact is missing: {item}")
    checks = state.get("checks", {})
    if not isinstance(checks, dict):
        errors.append(f"feature {feature_id} checks must be an object")
    else:
        for name in state.get("required_checks", []):
            if checks.get(name) not in {True, "PASS"}:
                errors.append(f"feature {feature_id} check is not PASS: {name}")
    audit = state.get("audit", {})
    if not isinstance(audit, dict) or audit.get("status") not in {"PASS", "PASS_WITH_WARNINGS"}:
        errors.append(f"feature {feature_id} audit is not PASS")
    return errors


def check_feature_entry(root: Path, feature_id: str) -> list[str]:
    directory = feature_dir(root, feature_id)
    state = load_json(directory / "status.json")
    _, phases_state = phase_state(root)
    phase_id = str(state.get("phase", ""))
    errors: list[str] = []
    if phase_id not in PHASES:
        return [f"feature {feature_id} has invalid phase: {phase_id}"]
    if phases_state.get("current_phase") != phase_id:
        errors.append(f"entry denied: feature belongs to phase {phase_id}, current phase is {phases_state.get('current_phase')}")
    phase_status = phases_state.get("phases", {}).get(phase_id, {}).get("status")
    if phase_status not in {"READY", "IN_PROGRESS"}:
        errors.append(f"entry denied: phase {phase_id} status is {phase_status}, expected READY or IN_PROGRESS")
    if state.get("status") not in {"LOCKED", "READY", "IN_PROGRESS"}:
        errors.append(f"entry denied: feature status is {state.get('status', 'MISSING')}")
    for dependency in state.get("dependencies", []):
        dependency_state = feature_dir(root, str(dependency)) / "status.json"
        if not dependency_state.is_file() or load_json(dependency_state).get("status") not in {"PASS", "PASS_WITH_WARNINGS"}:
            errors.append(f"entry denied: dependency is not PASS: {dependency}")
    return errors


def apply_phase_entry(root: Path, phase_id: str) -> None:
    path, state = phase_state(root)
    errors = check_phase_entry(root, phase_id)
    if errors:
        raise ValueError("; ".join(errors))
    state["current_phase"] = phase_id
    state["phases"][phase_id]["status"] = "IN_PROGRESS"
    save_json(path, state)


def apply_feature_entry(root: Path, feature_id: str) -> None:
    path = feature_dir(root, feature_id) / "status.json"
    state = load_json(path)
    errors = check_feature_entry(root, feature_id)
    if errors:
        raise ValueError("; ".join(errors))
    state["status"] = "IN_PROGRESS"
    save_json(path, state)


def main() -> int:
    parser = argparse.ArgumentParser(description="Enforce WebTow entry and completion gates")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--apply", action="store_true", help="apply an allowed entry transition")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--enter-phase", choices=PHASES)
    group.add_argument("--enter-feature")
    group.add_argument("--check-phase", choices=PHASES)
    group.add_argument("--check-feature")
    # Backward-compatible aliases for completion checks.
    group.add_argument("--phase", choices=PHASES)
    group.add_argument("--feature")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.enter_phase:
            errors = check_phase_entry(root, args.enter_phase)
            if not errors and args.apply:
                apply_phase_entry(root, args.enter_phase)
            target = f"phase {args.enter_phase} entry"
        elif args.enter_feature:
            errors = check_feature_entry(root, args.enter_feature)
            if not errors and args.apply:
                apply_feature_entry(root, args.enter_feature)
            target = f"feature {args.enter_feature} entry"
        elif args.check_phase or args.phase:
            phase_id = args.check_phase or args.phase
            errors = check_phase_completion(root, phase_id)
            target = f"phase {phase_id} completion"
        else:
            feature_id = args.check_feature or args.feature
            errors = check_feature_completion(root, feature_id)
            target = f"feature {feature_id} completion"
    except ValueError as exc:
        errors = [str(exc)]
        target = "state machine"
    if errors:
        print(f"PROJECT QUALITY GATE: FAIL ({target})")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PROJECT QUALITY GATE: PASS ({target})")
    if args.apply:
        print("State transition applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
