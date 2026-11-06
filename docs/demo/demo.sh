#!/usr/bin/env bash
# Replays a real kickstart audit (Cloudflare Worker, 193k LOC TS) for the README GIF.
# Source: docs/examples/audit-cloudflare-worker.md. Trimmed, numbers unchanged.
p() { printf '%b\n' "$1"; sleep "${2:-0.25}"; }
B='\033[1m'; D='\033[2m'; G='\033[32m'; R='\033[31m'; Y='\033[33m'; C='\033[36m'; N='\033[0m'
p "${D}kickstart: existing repo detected → running audit (gitleaks, pnpm audit)…${N}" 1.6
p ""
p "${B}Score: ${Y}51${N}${B}/100${N} ${D}(needs work)   Confidence: full${N}" 0.7
p ""
p "${R}${B}Critical${N} ${D}(fix this week)${N}" 0.3
p "  • 4 critical / 37 high dependency vulnerabilities → upgrade" 0.3
p "  • No CI: a push to main auto-deploys with no test gate" 0.8
p ""
p "Security ${G}88${N} · Dependencies ${R}28${N} · Tests ${Y}70${N} · CI/CD ${R}5${N}" 0.2
p "Docs ${Y}45${N} · Operability ${Y}70${N} · Compliance ${R}20${N}" 0.5
p "Estimated effort to reach 85: ${B}~16h${N} across 8 changes" 0.9
p ""
p "${B}Where I overrode the script:${N}" 0.3
p "  • Dockerfile missing: ${D}doesn't apply, this is a Cloudflare Worker;${N}" 0.2
p "    ${D}wrangler.jsonc is the platform config. Operability is really 85.${N}" 0.9
p ""
p "  ${B}1.${N} Upgrade vulnerable deps     Dependencies ${R}28${N} → ${G}~100${N}  ${D}(overall 51 → ~65)  M 1–4h${N}" 0.25
p "  ${B}2.${N} Add CI (test, audit, gitleaks)   CI/CD ${R}5${N} → ${G}75${N}  ${D}(overall → ~76)  M 1h${N}" 0.25
p "  ${B}3.${N} Add Dependabot (weekly, grouped)              ${D}+2 overall  S 15m${N}" 0.25
p "  ${D}… 5 more. Doing 1 and 2 gets you to about 76.${N}" 0.1
