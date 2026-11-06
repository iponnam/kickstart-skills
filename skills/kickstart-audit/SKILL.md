---
name: kickstart-audit
description: "Measures an existing codebase's production readiness and reports it as numbers. Runs scripts/audit.py to score security (secrets, vulnerable dependencies, headers, auth patterns), dependencies (lockfile, outdated, scanning), tests (presence, coverage), CI, docs, operability and compliance evidence on a 0–100 scale. Produces an executive summary first, then a drill-down report, then a ranked list of proposed changes each with before/after score and effort. Use when kickstart meets an existing repo, or when the user asks \"how healthy is this codebase\", \"audit this\", \"what should we fix first\", \"is this production ready\", or before a release."
---

# kickstart-audit

Numbers first, prose second. A non-technical reader should understand the executive summary in thirty seconds. A technical reader should be able to drill into any number and find the exact file.

## Step 1: Install and run the script

Copy `scripts/audit.py` from this skill's directory into the project as `.kickstart/audit.py` (overwrite if the skill's copy is newer; the `VERSION` constant at the top tells you). The project then owns a copy, so hooks, CI, teammates and future sessions can run it without this skill installed. Then:

```bash
python3 .kickstart/audit.py --repo . --out .kickstart/audit
```

The script:

- Detects ecosystems from manifests (npm/pnpm/yarn, pip/poetry/uv, Go, Cargo, Maven/Gradle, Bundler, Composer, .NET, Flutter/Dart, Elixir).
- Runs whichever scanners are installed, skipping the rest and listing them as `not available`: gitleaks or trufflehog, `npm audit`, `pip-audit`, `cargo audit`, `govulncheck`, `bundler-audit`, `composer audit`, `dotnet list package --vulnerable`, `osv-scanner`, outdated checks, coverage files, CI config, Dockerfile, docs, licence, lint config, security header patterns, unsafe patterns (string-built SQL, `eval`, `pickle.load`, `yaml.load` without Loader, `shell=True`, `dangerouslySetInnerHTML`, `innerHTML =`, hard-coded IPs or URLs with credentials).
- Writes `latest.json` (machine) and `latest.md` (human) into the output directory, and keeps dated copies for trend.

Never fail the audit because a tool is missing. The report says what was not checked. Offer one-line install commands for missing tools at the end.

If Python 3 is unavailable, do the equivalent checks manually with the file tools and fill the same report template by hand. The categories and weights below are the contract, not the script.

## Step 2: Scoring (the contract)

Seven categories, each 0–100, weighted into the overall score:

| Category | Weight | What moves it |
|---|---|---|
| Security | 25 | Secrets found (critical: −40 each, capped), unsafe patterns, missing headers middleware, missing rate limit, `.env` committed, debug on in prod config |
| Dependencies | 20 | Lockfile present, vulnerability counts by severity (critical −15, high −5, medium −1, capped), outdated major count, automated updates (Dependabot/Renovate) |
| Tests | 15 | Test files exist, test runner configured, coverage percentage if a report exists, security tests present (the six OWASP baseline tests) |
| CI/CD | 15 | CI config exists, runs lint + test + scan, pinned actions, deploy config present, branch protection evidence |
| Documentation | 10 | README with run instructions, `.env.example`, architecture note, runbook, changelog, licence |
| Operability | 10 | Health endpoint, structured logging, error tracking, Dockerfile or platform config, migrations tool, backups mentioned |
| Compliance | 5 | `.kickstart/compliance.md` exists; ratio of implemented controls; privacy page and data deletion path if personal data detected |

Overall = weighted sum. Bands: 85+ production-grade, 70–84 nearly there, 50–69 needs work, below 50 at risk.

Confidence: when a scanner was unavailable, the category is marked `partial` and the report shows the maximum it could have lost.

## Step 3: Executive summary (show this first)

Exactly this shape. Fill every line. Keep it under 25 lines.

```
Kickstart audit: <repo name>                          <date>
Score: <overall>/100  (<band>)       Confidence: <full | partial: N checks skipped>

Critical (fix this week)
• <count> secrets in <files or history>                      → rotate + purge
• <n> critical / <n> high dependency vulnerabilities         → upgrade
• <any other red item>

Category scores
Security <n>  Dependencies <n>  Tests <n>  CI/CD <n>  Docs <n>  Operability <n>  Compliance <n>

Numbers that matter
• <files> files, <LOC> lines, <languages>
• <n> dependencies, <n> outdated (<n> major), lockfile: yes/no
• Tests: <n> test files, coverage <n%> or unknown
• CI: <yes/no>, runs: lint/test/scan/build

Estimated effort to reach 85: ~<hours>h across <n> changes

Say "details" for the full report, or pick a change to apply.
```

## Step 4: Proposed changes

Rank by score gain per hour. Each proposal has exactly these fields:

```
<n>. <title>
   Category: <cat>   Score: <before> → <after>  (overall <before> → <after>)
   Effort: <S 15m–1h | M 1–4h | L 1–2d>    Risk: <none | low | breaking: <what>>
   What changes: <one or two sentences, concrete files>
```

Effort estimates come from `references/effort-table.md`. Always include, when applicable, in this order: rotate and purge secrets, fix critical vulnerabilities, add secret scanning pre-commit and CI, add lockfile, add dependency scanning in CI, add the six baseline security tests, add security headers, add health endpoint and structured logging, add `.env.example` and README run section, add Dependabot/Renovate, add compliance checklist, add Dockerfile, add runbook.

Show the top 10. Offer "more" for the rest.

## Step 5: Apply what the user picks

For each accepted proposal:

1. Make the change with minimal diff. Follow the project's existing conventions, not kickstart's defaults, unless the user asks to change conventions.
2. Re-run the relevant check (or the whole script if fast) and show the number moving: "Dependencies 35 → 71".
3. Commit with a Conventional Commit message naming the change, if the user wants commits.
4. Update `.kickstart/audit/latest.md` and `project.md` `last_score`.

Secret handling: never print a found secret. Show file, line and type only. Rotation is the user's job; say that explicitly and provide the purge command for history (`git filter-repo` preferred over `filter-branch`) with the warning that it rewrites history and requires a force push and re-clone by everyone.

## Step 6: Details view

When the user asks for details, print `latest.md`, which contains per-category sections with every finding as a row: `severity | file:line | finding | recommendation`. Group by category, sort by severity.

## Re-audit and trend

Each run appends to `.kickstart/audit/history.jsonl`. When a previous run exists, the executive summary shows deltas: `Score: 72/100 (+14 since 2026-10-02)`. `kickstart-release` and `kickstart-refresh` call this skill and rely on the delta.

## Interpreting with judgement

The script measures what it can see. Before presenting, sanity-check:

- A monorepo may need per-package audits; offer that.
- Generated or vendored directories (`node_modules`, `vendor`, `dist`, `.venv`) are excluded by default; if the repo commits them, say so as a finding.
- A low Tests score in a pure infrastructure or content repo is expected; say so and reduce the weight in your narrative, not in the script.
- Frameworks that set headers by default (Rails, Django with `SecurityMiddleware`, Spring Security) satisfy the header check even if the script does not see explicit middleware; mark it manually and note the reason.
