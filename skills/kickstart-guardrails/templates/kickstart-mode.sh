#!/usr/bin/env sh
# Reads the enforcement mode from .kickstart/project.md and runs a check.
# Usage: kickstart-mode.sh "<check name>" <command...>
# In "enforced" mode a failing command fails the hook.
# In "advised" mode a failing command prints a warning and the hook passes.
# Override for emergencies: KICKSTART_MODE=advised git commit ...

name="$1"; shift
mode="${KICKSTART_MODE:-}"
if [ -z "$mode" ] && [ -f .kickstart/project.md ]; then
  mode=$(grep -E '^- enforcement:' .kickstart/project.md | head -n1 | sed 's/.*: *//' | tr -d '[:space:]')
fi
[ -z "$mode" ] && mode="advised"

if "$@"; then
  exit 0
fi
status=$?
if [ "$mode" = "enforced" ]; then
  echo "kickstart: BLOCKED by '$name' (enforced mode). Fix the cause; do not bypass." >&2
  exit $status
else
  echo "kickstart: ADVISED: '$name' would have blocked in enforced mode. Continuing." >&2
  exit 0
fi
