---
name: kickstart-refresh
description: "Monthly dependency and vulnerability refresh for a kickstarted project. Groups updates by risk (security fixes, patch, minor, major), applies them in order with tests between groups, re-runs the audit, and reports the delta in numbers (vulnerabilities before/after, outdated count, score change). Use when the user says \"update dependencies\", \"upgrade packages\", \"fix vulnerabilities\", \"monthly maintenance\", \"dependabot is noisy\", or when kickstart notices the last refresh was over 30 days ago."
---

# kickstart-refresh

Dependencies rot quietly. Refresh them on a schedule, in small safe batches, with numbers that show it was worth it.

## Inputs

`.kickstart/project.md` (ecosystems, commands, enforcement), `.kickstart/audit/latest.json` (vulnerability baseline), the lockfile.

## Step 1: Baseline

Run the `kickstart-audit` script (or just its dependency section) and record:

```
Before: <n> critical / <n> high / <n> medium vulnerabilities · <n> outdated (<n> major) · Dependencies score <n>
```

List the outdated packages with current → latest and whether the jump is patch, minor or major. Use the ecosystem's command:

| Ecosystem | Outdated | Vulnerabilities | Update |
|---|---|---|---|
| npm/pnpm/yarn | `npm outdated` / `pnpm outdated` | `npm audit` / `pnpm audit` | `npm update`, `npm install pkg@latest` |
| Python (uv/poetry/pip) | `uv pip list --outdated` / `poetry show --outdated` / `pip list --outdated` | `pip-audit` | `uv lock --upgrade-package pkg` / `poetry update pkg` |
| Go | `go list -m -u all` | `govulncheck ./...` | `go get pkg@latest && go mod tidy` |
| Rust | `cargo outdated` (if installed) | `cargo audit` | `cargo update -p pkg` |
| Ruby | `bundle outdated` | `bundle-audit check --update` | `bundle update pkg` |
| PHP | `composer outdated` | `composer audit` | `composer update pkg` |
| .NET | `dotnet list package --outdated` | `dotnet list package --vulnerable` | `dotnet add package pkg` |
| Java (Gradle/Maven) | `gradle dependencyUpdates` (plugin) / `mvn versions:display-dependency-updates` | `osv-scanner` / dependency-check | edit build file |
| Dart/Flutter | `dart pub outdated` | `osv-scanner` | `dart pub upgrade` |
| GitHub Actions | compare tags in workflows | n/a | bump tags/digests |
| Docker base images | check tag/digest | `trivy image` | bump digest |

## Step 2: Groups, in this order

1. **Security fixes**: anything with a critical or high advisory. Apply first, regardless of version jump.
2. **Patch updates**: all at once.
3. **Minor updates**: all at once; read changelogs for anything the project depends on heavily.
4. **Major updates**: one at a time, each with its migration guide read first. Skip any that need more than an hour and record them as follow-ups.
5. **Tooling**: CI actions, Docker base image digests, linter and test runner versions.

After each group: install with lockfile update, run `lint` and `test` from `project.md`, and build. If a group fails, bisect within the group, pin the offender to its previous version, note it, and continue.

Commit per group: `chore(deps): security fixes`, `chore(deps): patch updates`, `chore(deps): minor updates`, `chore(deps)!: upgrade <pkg> to v<N>` for majors.

## Step 3: Re-audit and report

Run the audit script again. Report:

```
Dependency refresh: <repo>  <date>
Vulnerabilities: <c>/<h>/<m> → <c>/<h>/<m>
Outdated: <n> (<n> major) → <n> (<n> major)
Dependencies score: <before> → <after>   Overall: <before> → <after>
Updated: <n> packages in <n> commits · Tests: green
Deferred (needs a focused session): <pkg> v<X>→v<Y> (<reason>), …
Pinned due to failure: <pkg> (<reason>), …
Next refresh due: <date + 30 days>
```

Update `.kickstart/project.md` with `last_refresh: <date>`.

## Step 4: Keep it quiet next time

If Dependabot or Renovate is not configured, add it with weekly grouped minor/patch updates and a separate group for security. If it is configured and the user says it is noisy, switch it to grouped and monthly for non-security updates; security stays immediate.

## Rules

- Vulnerability and version facts come only from tools run now (the ecosystem audit command, `osv-scanner`, the registry) and from each package's official changelog or migration guide fetched now. Never decide a package is safe, current or breaking from memory.
- Security fixes are never deferred. If one requires a breaking major, do that major now.
- Never update everything in one commit. Bisecting a 40-package bump at midnight is how refreshes get abandoned.
- Do not change code behaviour during a refresh except what a migration guide requires. Note other needed changes as follow-ups.
- In `enforced` mode the CI vulnerability gate must pass before the refresh is called done.
