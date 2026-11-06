# Example: auditing a real Cloudflare Worker

Unedited output of `/kickstart` on an existing repo: a Cloudflare Worker (Hono, D1, MCP agents), 193k lines of TypeScript, pnpm, no CI. Project name removed. Nothing else changed.

The part worth reading is **"Where I overrode the script"**: the audit script flags what it finds; the agent then applies judgement about the platform before scoring.

```
Kickstart audit: <project>, 2026-11-06. This is the first run, so there's no trend yet.

Score: 51/100 (needs work)    Confidence: full (gitleaks + pnpm audit ran)
                              My adjusted reading: ~55 (false positives below)

Critical (fix this week)
• 4 critical / 37 high dependency vulnerabilities           → upgrade
    - Reach production: `agents` → MCP SDK → express (proxy-addr critical,
      body-parser, fast-uri, @modelcontextprotocol/* highs)
    - Dev/test only: vitest 3.0 (+ tinypool) critical; miniflare/undici/
      sharp/vite highs. These aren't shipped but run on dev machines.
• No CI, so a push to dev/main auto-deploys via Cloudflare with no test gate

Category scores
Security 88  Dependencies 28  Tests 70  CI/CD 5  Docs 45  Operability 70  Compliance 20

Numbers that matter
• 280 tracked files (1,483 incl. untracked), 193k lines, mostly TypeScript
• 5 prod + 7 dev deps, 10 outdated (2 major), lockfile: yes (pnpm)
• Tests: 245 test files, 82 security tests, coverage unknown
• CI: no. Lint: no (only `tsc --noEmit`)
• 0 secrets found (gitleaks)

Estimated effort to reach 85: ~16h across 8 changes

Where I overrode the script:
- Unsafe patterns (3): false positives. All three are in the audit script's own regex definitions, inside the untracked .agents/ folder. The real Security score is about 97.
- Dockerfile missing: doesn't apply. This is a Cloudflare Worker, and wrangler.jsonc is the platform config. Operability is really 85.
- No .env.example: Workers keep local secrets in .dev.vars, which is already gitignored. What's actually missing is a .dev.vars.example.

Proposed changes, ranked by score gain per hour

1. Upgrade vulnerable dependencies (agents, vitest → 3.2.6+, @cloudflare/vitest-pool-workers, miniflare)
   Category: Dependencies   Score: 28 → ~100  (overall 51 → ~65)
   Effort: M 1–4h   Risk: breaking possible (vitest-pool-workers 0.8 → newer, agents 0.20 → latest)
   What changes: package.json + pnpm-lock.yaml; run `pnpm test` between each group

2. Add CI workflow (typecheck, test, pnpm audit, gitleaks)
   Category: CI/CD   Score: 5 → 75  (overall → ~76)
   Effort: M 1h   Risk: none
   What changes: .github/workflows/ci.yml on PRs to dev/main; make it a required check so Cloudflare only deploys tested code

3. Add Dependabot (weekly, grouped)
   Category: Dependencies   Score: +10  (overall +2)
   Effort: S 15m   Risk: none
   What changes: .github/dependabot.yml

4. Add .dev.vars.example
   Category: Docs   Score: 45 → 60  (overall +1.5)
   Effort: S 15m   Risk: none
   What changes: every binding/secret name from wrangler.jsonc, no values

5. Compliance checklist (OWASP Top 10 + DPDP, since personal data is handled)
   Category: Compliance   Score: 20 → 60  (overall +2)
   Effort: M 1h   Risk: none
   What changes: .kickstart/compliance.md via kickstart-compliance

6. Architecture note + runbook
   Category: Docs   Score: 45 → 65  (overall +2)
   Effort: M 2h   Risk: none
   What changes: docs/architecture.md, docs/runbook.md (deploys, rollback via the Cloudflare dashboard, D1 migrations)

7. Add a linter (Biome: one dev dependency, zero config)
   Category: Operability   Score: +5  (overall +0.5)
   Effort: S 30m   Risk: low (first run will flag existing code)
   What changes: biome.json, a `lint` script, a CI step

8. LICENSE + CHANGELOG
   Category: Docs   Score: +10  (overall +1)
   Effort: S 15m   Risk: none
   What changes: LICENSE (proprietary if closed source), CHANGELOG.md

Doing 1 and 2 gets you to about 76. Adding 3–6 gets you to about 85.
```

Nothing was changed in the repo at this point. The audit proposes; the user picks; each applied change is re-measured.
