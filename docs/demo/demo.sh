#!/usr/bin/env bash
# Replays a kickstart audit session for the README GIF. Output mirrors README "Existing project" example.
p() { printf '%b\n' "$1"; sleep "${2:-0.25}"; }
B='\033[1m'; D='\033[2m'; G='\033[32m'; R='\033[31m'; Y='\033[33m'; C='\033[36m'; N='\033[0m'
p "${D}kickstart: existing repo detected → running audit…${N}" 1.4
p ""
p "${B}Score: ${Y}58${N}${B}/100${N}" 0.6
p ""
p "${R}${B}Critical${N} ${D}(fix this week)${N}" 0.3
p "  • 2 secrets committed in history ${D}(.env, config/prod.yml)${N}" 0.3
p "  • 7 critical / 23 high dependency vulnerabilities" 0.8
p ""
p "${B}Executive summary${N}" 0.3
p "  Security ${R}41${N} · Dependencies ${R}35${N} · Tests ${Y}62${N} · CI ${G}80${N} · Docs ${G}70${N} · Compliance ${Y}55${N}" 0.4
p "  Est. effort to reach 85: ${B}~14 hours${N} across 9 changes" 0.9
p ""
p "Say ${C}details${N} for the full report, or pick a change to apply:" 0.3
p "  ${B}1.${N} Rotate and purge secrets         → Security ${R}41${N} → ${G}68${N}   ${D}(1.5h)${N}" 0.25
p "  ${B}2.${N} Upgrade 23 vulnerable deps       → Dependencies ${R}35${N} → ${G}88${N} ${D}(3h, 2 breaking)${N}" 0.25
p "  ${B}3.${N} Add secret-scanning pre-commit   → prevents recurrence   ${D}(10m)${N}" 0.25
p "  ${D}…${N}" 0.1
