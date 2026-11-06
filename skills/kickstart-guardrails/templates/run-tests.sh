#!/usr/bin/env sh
# Runs the project's test command from .kickstart/project.md (line "- test: <command>").
cmd=$(grep -E '^- test:' .kickstart/project.md 2>/dev/null | head -n1 | sed 's/^- test: *//')
if [ -z "$cmd" ]; then
  echo "kickstart: no test command recorded in .kickstart/project.md; skipping" >&2
  exit 0
fi
echo "kickstart: running tests: $cmd" >&2
exec sh -c "$cmd"
