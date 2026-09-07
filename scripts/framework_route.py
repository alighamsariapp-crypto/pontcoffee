#!/usr/bin/env python3
"""Print the smallest canonical reading set for a feature type."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES = json.loads((ROOT / "config/route-map.json").read_text(encoding="utf-8"))["routes"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Route a feature to a small reading set")
    parser.add_argument("feature_type", choices=sorted(ROUTES), help="feature category")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()
    route = ROUTES[args.feature_type]
    result = {"feature_type": args.feature_type, **route}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Feature type: {args.feature_type}")
        print("Read first:")
        for item in route["read"]:
            print(f"  - {item}")
        print("Use Skills:")
        for item in route["skills"]:
            print(f"  - {item}")
        print(f"Checks: {', '.join(route['checks'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
