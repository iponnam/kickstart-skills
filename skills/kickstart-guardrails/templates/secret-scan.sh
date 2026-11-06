#!/usr/bin/env sh
# Secret scan. Prefers gitleaks, then trufflehog, then a regex fallback.
# Usage: secret-scan.sh staged | full
mode="${1:-staged}"

if command -v gitleaks >/dev/null 2>&1; then
  if [ "$mode" = "staged" ]; then
    gitleaks git --staged --redact --no-banner --exit-code 1 . 2>/dev/null || gitleaks protect --staged --redact --no-banner --exit-code 1
  else
    gitleaks git --redact --no-banner --exit-code 1 . 2>/dev/null || gitleaks detect --redact --no-banner --exit-code 1
  fi
  exit $?
fi

if command -v trufflehog >/dev/null 2>&1; then
  if [ "$mode" = "staged" ]; then
    git diff --cached | trufflehog stdin --only-verified --fail --no-update
  else
    trufflehog git file://. --only-verified --fail --no-update
  fi
  exit $?
fi

echo "kickstart: gitleaks/trufflehog not installed; using regex fallback (weaker). Install: brew install gitleaks" >&2
exec sh "$(dirname "$0")/secret-patterns.sh" "$mode"
