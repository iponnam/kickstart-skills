#!/usr/bin/env sh
# Blocks staging of environment and key files. Receives staged file paths as arguments.
status=0
for f in "$@"; do
  base=$(basename "$f")
  case "$base" in
    .env|.env.*|*.pem|*.key|*.p12|*.pfx|*.jks|id_rsa|id_rsa.*|id_ed25519|id_ed25519.*|*.keystore|credentials.json|service-account*.json)
      case "$base" in
        .env.example|.env.sample|.env.template) ;;
        *) echo "kickstart: refusing to commit secret-like file: $f" >&2; status=1 ;;
      esac
      ;;
  esac
done
exit $status
