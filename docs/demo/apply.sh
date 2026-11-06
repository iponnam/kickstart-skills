#!/usr/bin/env bash
p() { printf '%b\n' "$1"; sleep "${2:-0.25}"; }
B='\033[1m'; D='\033[2m'; G='\033[32m'; R='\033[31m'; N='\033[0m'
p "${D}kickstart → guardrails:${N} installing secret-scanning pre-commit hook…" 1.2
p "  ${G}✓${N} gitleaks hook added to .pre-commit-config.yaml" 0.3
p "  ${G}✓${N} same check wired into CI (.github/workflows/ci.yml)" 0.3
p "  ${G}✓${N} recorded in .kickstart/project.md" 0.8
p ""
p "Re-audit: Security ${R}41${N} → ${G}49${N}. Recurrence risk: ${G}blocked${N}." 0.4
p "${D}Next: 1 (rotate secrets) or 2 (upgrade deps)?${N}" 0.2
