# Effort table

Typical effort for one engineer familiar with the stack, starting from a repo that lacks the item. Use these for the "Estimated effort" line and the per-proposal Effort field. Adjust up for monorepos or unusual stacks and say so.

| Change | Effort | Typical score gain | Notes |
|---|---|---|---|
| Rotate one secret and purge from history | 1–2h | Security +20–40 | Rotation in the provider dashboard; `git filter-repo`; force push; everyone re-clones |
| Remove committed `.env` and add `.env.example` | 15m | Security +10, Docs +10 | |
| Add secret-scanning pre-commit hook (gitleaks) | 15m | Security +5, prevents recurrence | |
| Add secret scanning to CI | 15m | CI +10 | |
| Upgrade dependencies to fix critical/high vulns, no breaking | 1–3h | Dependencies +30–50 | Run tests between groups |
| Upgrade with one breaking major | +2–4h each | | Read the migration guide first |
| Add lockfile | 15m | Dependencies +15 | Commit it; CI must use frozen install |
| Add dependency scan to CI | 20m | Dependencies +10, CI +10 | |
| Add Dependabot/Renovate config | 15m | Dependencies +10 | Weekly, grouped |
| Add test runner and first test | 1h | Tests +25 | |
| Add the five OWASP security tests | 1–2h | Tests +15, Security +5 | |
| Reach 60% coverage on a mid-size app | 1–3d | Tests +20 | Only if the user wants it |
| Add CI workflow (lint, test, build) | 1h | CI +40 | |
| Pin actions to tags / digests | 20m | CI +5 | |
| Add security headers middleware | 30m–1h | Security +10 | CSP needs tuning for the front end |
| Add rate limiting on auth routes | 1h | Security +5 | |
| Add input validation schema on endpoints | 2–8h | Security +10 | Scales with endpoint count |
| Replace string-built SQL with parameters | 1–4h | Security +10–20 | Scales with occurrences |
| Add structured logging with request id | 1h | Operability +20 | |
| Add error tracking (Sentry) | 30m | Operability +15 | |
| Add health endpoint | 15m | Operability +10 | |
| Add Dockerfile (multi-stage, non-root) | 1h | Operability +15 | |
| Add migrations tool to an existing schema | 2–4h | Operability +10 | Baseline migration from current schema |
| Write README run section | 30m | Docs +20 | |
| Write architecture note and runbook | 2h | Docs +30 | |
| Add CHANGELOG and licence | 15m | Docs +10 | |
| Create `.kickstart/compliance.md` with OWASP | 1h | Compliance +40 | |
| Add privacy page and data deletion endpoint | 2–4h | Compliance +20 | Required by most privacy laws |
| Enable branch protection and required checks | 15m | CI +10 | Repo settings, not code |
| Turn on GitHub secret scanning push protection | 5m | Security +5 | Repo settings |

Rule of thumb: a typical mid-size repo scoring 50–60 reaches 85 in 10–20 hours of focused work, most of it dependencies and tests.
