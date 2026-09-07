#!/usr/bin/env bash
set -euo pipefail

root="$(git rev-parse --show-toplevel)"
hook="$root/.git/hooks/pre-commit"
cat > "$hook" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
root="$(git rev-parse --show-toplevel)"
python3 "$root/scripts/framework_check.py"
HOOK
chmod +x "$hook"
printf 'Installed framework pre-commit hook at %s\n' "$hook"
