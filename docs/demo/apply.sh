#!/usr/bin/env bash
p() { printf '%b\n' "$1"; sleep "${2:-0.25}"; }
B='\033[1m'; D='\033[2m'; G='\033[32m'; R='\033[31m'; N='\033[0m'
p "${D}kickstart → guardrails:${N} adding .github/workflows/ci.yml…" 1.2
p "  ${G}✓${N} typecheck, test, pnpm audit, gitleaks on PRs to main" 0.3
p "  ${G}✓${N} marked as required check: Cloudflare deploys only tested code" 0.3
p "  ${G}✓${N} recorded in .kickstart/project.md" 0.8
p ""
p "Re-audit: CI/CD ${R}5${N} → ${G}75${N}. Overall ${R}51${N} → ${G}66${N}." 0.4
p "${D}Next: 1 (upgrade deps, gets you to ~76)?${N}" 0.2
