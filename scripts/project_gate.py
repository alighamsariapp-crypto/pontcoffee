#!/usr/bin/env python3
"""Machine-enforced phase and feature quality gates for generated projects."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PHASES = ["00", "01", "02", "03", "04", "05", "06", "07"]
DEFAULT_REQUIRED = ["FEATURE_SPEC.md", "PHASE_REPORT.md", "AUDIT.md"]


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise ValueError(f"missing machine-readable state: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc


def blockers(value: object) -> list[str]:
    if not isinstance(value, list):
        return ["blockers must be a JSON array"]
    return [str(item) for item in value if str(item).strip()]


def check_phase(root: Path, phase_id: str) -> list[str]:
    errors: list[str] = []
    state = load_json(root / ".webtow/phase-status.json")
    phases = state.get("phases", {})
    if phase_id not in PHASES:
        return [f"unknown phase: {phase_id}"]
    for previous in PHASES[: PHASES.index(phase_id)]:
        if phases.get(previous, {}).get("status") != "PASS":
            errors.append(f"phase {phase_id} is blocked: previous phase {previous} is not PASS")
    current = phases.get(phase_id)
    if not isinstance(current, dict):
        errors.append(f"missing status for phase {phase_id}")
        return errors
    if current.get("status") != "PASS":
        errors.append(f"phase {phase_id} status is {current.get('status', 'MISSING')}, not PASS")
    errors.extend(f"phase {phase_id}: {item}" for item in blockers(current.get("blockers", [])))
    report = current.get("report")
    if not report or not (root / str(report)).is_file():
        errors.append(f"phase {phase_id} report is missing: {report or '<not declared>'}")
    required_evidence = current.get("required_evidence", [])
    for item in required_evidence:
        if not (root / str(item)).is_file():
            errors.append(f"phase {phase_id} evidence is missing: {item}")
    return errors


def check_feature(root: Path, feature_id: str) -> list[str]:
    errors: list[str] = []
    feature_dir = root / ".webtow/features" / feature_id
    state_path = feature_dir / "status.json"
    try:
        state = load_json(state_path)
    except ValueError as exc:
        return [str(exc)]
    phase_id = str(state.get("phase", ""))
    if phase_id not in PHASES:
        errors.append(f"feature {feature_id} has invalid phase: {phase_id}")
    else:
        errors.extend(check_phase(root, phase_id))
    if state.get("id") != feature_id:
        errors.append(f"feature state id does not match directory: {state.get('id')}")
    if state.get("status") != "PASS":
        errors.append(f"feature {feature_id} status is {state.get('status', 'MISSING')}, not PASS")
    errors.extend(f"feature {feature_id}: {item}" for item in blockers(state.get("blockers", [])))
    required = state.get("required_artifacts", DEFAULT_REQUIRED)
    for item in required:
        if not (feature_dir / str(item)).is_file():
            errors.append(f"feature {feature_id} artifact is missing: {item}")
    checks = state.get("checks", {})
    if not isinstance(checks, dict):
        errors.append(f"feature {feature_id} checks must be an object")
    else:
        for name in state.get("required_checks", []):
            value = checks.get(name)
            if value is not True and value != "PASS":
                errors.append(f"feature {feature_id} check is not PASS: {name}")
    audit = state.get("audit", {})
    if not isinstance(audit, dict) or audit.get("status") != "PASS":
        errors.append(f"feature {feature_id} audit is not PASS")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Enforce WebTow project quality gates")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--phase", choices=PHASES)
    group.add_argument("--feature")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        errors = check_phase(root, args.phase) if args.phase else check_feature(root, args.feature)
    except ValueError as exc:
        errors = [str(exc)]
    if errors:
        print("PROJECT QUALITY GATE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    target = f"phase {args.phase}" if args.phase else f"feature {args.feature}"
    print(f"PROJECT QUALITY GATE: PASS ({target})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
