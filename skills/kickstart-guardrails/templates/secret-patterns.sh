#!/usr/bin/env sh
# Regex fallback secret scan. Weaker than gitleaks; use only when it cannot be installed.
# Usage: secret-patterns.sh staged | full
mode="${1:-staged}"
pattern='(AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{22,}|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{20,}|sk_live_[A-Za-z0-9]{20,}|rzp_live_[A-Za-z0-9]{10,}|AIza[0-9A-Za-z_-]{35}|-----BEGIN (RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----|(password|passwd|secret|api[_-]?key|token)[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"']{8,}["'"'"'])'

if [ "$mode" = "staged" ]; then
  out=$(git diff --cached -U0 --no-color | grep -E '^\+' | grep -v '^+++' | grep -iE "$pattern")
else
  out=$(git grep -nIiE "$pattern" -- ':!*.lock' ':!*lock.json' ':!*.min.js' 2>/dev/null)
fi

if [ -n "$out" ]; then
  echo "kickstart: possible secrets detected (values redacted):" >&2
  echo "$out" | sed -E 's/([:=][[:space:]]*["'"'"']?)[^"'"'"' ]{8,}/\1<redacted>/g' | cut -c1-160 >&2
  exit 1
fi
exit 0
