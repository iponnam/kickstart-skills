#!/usr/bin/env sh
# Blocks files larger than 5 MB unless tracked by Git LFS.
limit=$((5 * 1024 * 1024))
status=0
for f in "$@"; do
  [ -f "$f" ] || continue
  size=$(wc -c < "$f" | tr -d ' ')
  if [ "$size" -gt "$limit" ]; then
    if git check-attr filter -- "$f" | grep -q lfs; then continue; fi
    echo "kickstart: $f is $((size / 1024 / 1024)) MB; use Git LFS or keep it out of the repo" >&2
    status=1
  fi
done
exit $status
