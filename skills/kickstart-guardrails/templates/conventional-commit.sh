#!/usr/bin/env sh
# Validates a Conventional Commit subject line. Argument: path to the commit message file.
msg=$(head -n1 "$1")
case "$msg" in
  Merge*|Revert*|fixup!*|squash!*) exit 0 ;;
esac
if echo "$msg" | grep -qE '^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([a-z0-9._/-]+\))?!?: .{1,72}$'; then
  exit 0
fi
echo "kickstart: commit message must follow Conventional Commits, e.g. 'feat(auth): add password reset'" >&2
echo "  got: $msg" >&2
exit 1
