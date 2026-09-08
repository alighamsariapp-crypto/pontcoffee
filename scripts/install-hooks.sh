#!/usr/bin/env bash
set -euo pipefail

root="$(git rev-parse --show-toplevel)"
hook="$root/.git/hooks/pre-commit"
cat > "$hook" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
root="$(git rev-parse --show-toplevel)"
python3 "$root/scripts/framework_check.py"

# The framework repository has no .webtow state. A generated project may opt
# into a completion gate for an explicit target without blocking ordinary WIP commits.
if [[ -f "$root/.webtow/phase-status.json" && -n "${WEBTOW_GATE_TARGET:-}" ]]; then
  case "$WEBTOW_GATE_TARGET" in
    phase:*) python3 "$root/scripts/project_gate.py" --check-phase "${WEBTOW_GATE_TARGET#phase:}" ;;
    feature:*) python3 "$root/scripts/project_gate.py" --check-feature "${WEBTOW_GATE_TARGET#feature:}" ;;
    *) echo "Invalid WEBTOW_GATE_TARGET; use phase:03 or feature:F-003" >&2; exit 1 ;;
  esac
fi
HOOK
chmod +x "$hook"
printf 'Installed framework pre-commit hook at %s\n' "$hook"
printf 'For an explicit project gate use WEBTOW_GATE_TARGET=phase:03 or feature:F-003.\n'
