#!/usr/bin/env python3
"""Print a small, phase-aware reading set for a feature or development phase."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config/route-map.json").read_text(encoding="utf-8"))
PHASES = json.loads((ROOT / "config/phase-map.json").read_text(encoding="utf-8"))
ROUTES = CONFIG["routes"]


def unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def main() -> int:
    parser = argparse.ArgumentParser(description="Route a phase and feature to a small reading set")
    parser.add_argument("feature_type", nargs="?", choices=sorted(ROUTES), help="feature category")
    parser.add_argument("--phase", choices=sorted(PHASES["phases"]), help="phase number, for example 04")
    parser.add_argument("--feature", choices=sorted(ROUTES), help="optional feature overlay")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()
    if not args.phase and not args.feature_type and not args.feature:
        parser.error("provide a feature type or --phase")

    bootstrap = PHASES["bootstrap"]
    phase = PHASES["phases"].get(args.phase) if args.phase else None
    feature_name = args.feature or args.feature_type
    feature = ROUTES[feature_name] if feature_name else None
    phase_read = phase["read"] if phase else []
    phase_skills = phase["skills"] if phase else []
    feature_read = feature["read"] if feature else []
    feature_skills = feature["skills"] if feature else []
    effective_read = unique(bootstrap + phase_read + feature_read)
    effective_skills = unique(phase_skills + feature_skills)
    result: dict[str, object] = {
        "bootstrap": bootstrap,
        "effective_read": effective_read,
        "effective_skills": effective_skills,
    }
    if args.phase:
        result["phase"] = {"id": args.phase, **phase}
    if feature_name:
        result["feature"] = {"type": feature_name, **feature}

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print("Read once, in this order:")
    for item in effective_read:
        print(f"  - {item}")
    print("Skills:")
    for item in effective_skills:
        print(f"  - {item}")
    if args.phase:
        print(f"Phase: {args.phase} — {phase['name']}")
    if feature_name:
        print(f"Feature overlay: {feature_name}")
    print("Load deep rules only when the returned checks identify a matching risk.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
