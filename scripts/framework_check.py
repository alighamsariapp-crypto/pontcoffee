#!/usr/bin/env python3
"""Executable quality gates for the AI Web Framework repository."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED_REFERENCE_NAMES = {
    "PROJECT_SPEC.md", "FEATURE_SPEC.md", "PHASE_REPORT.md", "ADR.md",
    "VERSION", "COMMIT", "OWNER", "DATE", "STATUS", "NAME",
}
PATH_RE = re.compile(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+|[A-Za-z0-9_.-]+\.md)(?![A-Za-z0-9_./-])")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_required(errors: list[str]) -> None:
    required = [
        "AGENTS.md", "README.md", "PROJECT_SPEC.template.md", "SECURITY_RULES.md",
        "TESTING_RULES.md", "scripts/framework_check.py", "scripts/framework_route.py",
        "config/route-map.json", "config/phase-map.json", "CONTEXT_LOADING.md",
        "PROJECT_QUALITY_GATE.md", "scripts/project_gate.py",
        "templates/project-state/phase-status.json", "templates/project-state/feature-status.json",
        "skills/google-ai-studio/SKILL.md",
    ]
    for item in required:
        if not (ROOT / item).is_file():
            fail(errors, f"missing required file: {item}")
    if (ROOT / "SKILLS").exists():
        fail(errors, "uppercase SKILLS directory exists; use skills/")
    if (ROOT / "skills-temp").exists():
        fail(errors, "temporary skills directory exists")


def check_references(errors: list[str]) -> None:
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts:
            continue
        text = file.read_text(encoding="utf-8")
        if "SKILLS/" in text:
            fail(errors, f"uppercase directory reference in {file.relative_to(ROOT)}: SKILLS/")
        inline_refs = set(re.findall(r"`([^`]+)`", text))
        for ref in PATH_RE.findall(text):
            if ref in IGNORED_REFERENCE_NAMES or ref.startswith(("http://", "https://")):
                continue
            if "XX" in ref or "000" in ref:
                continue
            if ref.startswith(("[", "#")):
                continue
            candidate = ROOT / ref
            if candidate.exists():
                continue
            # Generic project files are intentionally created after copying the framework.
            if ref in {"PROJECT_SPEC.md", "FEATURE_SPEC.md", "PHASE_REPORT.md", "ADR.md"}:
                continue
            # Ignore prose words that look like a filename unless they have a known extension/path.
            # A repository reference normally has a known file extension. Phrases
            # such as "API/database/auth" are prose labels, not paths.
            if "/" not in ref and ref not in inline_refs:
                continue
            if not re.search(r"\.(md|json|ya?ml|sh|py|toml|txt)$", ref):
                continue
            fail(errors, f"broken reference in {file.relative_to(ROOT)}: {ref}")


def check_route_map(errors: list[str]) -> None:
    route_file = ROOT / "config/route-map.json"
    if not route_file.is_file():
        return
    try:
        data = json.loads(route_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid route map JSON: {exc}")
        return
    for kind, route in data.get("routes", {}).items():
        if not route.get("read"):
            fail(errors, f"route {kind} has no read list")
        for item in route.get("read", []) + route.get("skills", []):
            if item == "PROJECT_SPEC.md" and (ROOT / "PROJECT_SPEC.template.md").is_file():
                continue
            if not (ROOT / item).is_file():
                fail(errors, f"route {kind} points to missing file: {item}")
        if len(route.get("read", [])) > 5:
            fail(errors, f"route {kind} reads too many canonical files: {len(route['read'])}")

    phase_file = ROOT / "config/phase-map.json"
    if not phase_file.is_file():
        return
    try:
        phase_data = json.loads(phase_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid phase map JSON: {exc}")
        return
    limits = phase_data.get("policy", {})
    if len(phase_data.get("bootstrap", [])) > limits.get("bootstrap_max_files", 3):
        fail(errors, "bootstrap context exceeds configured limit")
    for phase_id, phase in phase_data.get("phases", {}).items():
        if len(phase.get("read", [])) > limits.get("phase_max_files", 5):
            fail(errors, f"phase {phase_id} reads too many canonical files")
        for item in phase.get("read", []) + phase.get("skills", []):
            if item == "PROJECT_SPEC.md" and (ROOT / "PROJECT_SPEC.template.md").is_file():
                continue
            if not (ROOT / item).is_file():
                fail(errors, f"phase {phase_id} points to missing file: {item}")


def check_duplicates(errors: list[str]) -> None:
    # Detect accidental copies of the same large governance document under a new path.
    hashes: dict[str, Path] = {}
    import hashlib
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts:
            continue
        digest = hashlib.sha256(file.read_bytes()).hexdigest()
        if digest in hashes:
            fail(errors, f"duplicate markdown file: {file.relative_to(ROOT)} == {hashes[digest].relative_to(ROOT)}")
        else:
            hashes[digest] = file


def check_secrets(errors: list[str]) -> None:
    forbidden = {".env", ".pem", ".key"}
    for file in ROOT.rglob("*"):
        if not file.is_file() or ".git" in file.parts:
            continue
        if file.name in {".env.example"}:
            continue
        if file.name in forbidden or file.suffix in {".pem", ".key"} or "service-account" in file.name:
            fail(errors, f"possible secret file: {file.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AI Web Framework conventions")
    parser.add_argument("--project", action="store_true", help="require a completed PROJECT_SPEC.md")
    args = parser.parse_args()
    errors: list[str] = []
    check_required(errors)
    check_references(errors)
    check_route_map(errors)
    check_duplicates(errors)
    check_secrets(errors)
    if args.project and not (ROOT / "PROJECT_SPEC.md").is_file():
        fail(errors, "project mode requires PROJECT_SPEC.md")
    if errors:
        print("FRAMEWORK CHECK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("FRAMEWORK CHECK: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
