---
name: kickstart-release
description: Pre-release checklist and release execution for a kickstarted project: tests green, vulnerability and secret scans clean, migrations reviewed with rollback, changelog and version bump, monitoring and alerts confirmed, compliance evidence updated, then tag and deploy. Blocks on failures in enforced mode, warns in advised mode. Use when the user says "ship it", "release", "deploy to production", "cut a version", "are we ready to launch", or before any production deployment.
---

# kickstart-release

A release is a checklist that either passes or explains exactly why not. Run it the same way every time.

## Inputs

`.kickstart/project.md` (commands, enforcement, scale, hosting), `.kickstart/compliance.md`, `CHANGELOG.md`, git state.

## Step 1: Pre-flight (read-only, fast)

Run and report each as pass / warn / fail:

| # | Check | Command or source | Fail means |
|---|---|---|---|
| 1 | Clean working tree, on the release branch | `git status`, `git branch` | uncommitted changes |
| 2 | Lint and typecheck | `project.md` commands | any error |
| 3 | Tests | `project.md` test command | any failure |
| 4 | Secret scan (full history on first release, diff since last tag after) | `kickstart-guardrails` secret-scan.sh | any finding |
| 5 | Dependency vulnerabilities | ecosystem audit or osv-scanner | critical or high |
| 6 | Audit score | `kickstart-audit` script | below 70 (`pet`) or 85 (`scale`), or dropped since last release |
| 7 | Migrations | list pending migrations | destructive change without expand/contract note |
| 8 | Changelog | `CHANGELOG.md` Unreleased section | empty |
| 9 | Env parity | compare `.env.example` keys with production config (ask the user or check platform CLI) | missing variable in production |
| 10 | Monitoring | error tracker DSN set in prod, health endpoint reachable, uptime check exists | any missing (`scale`); warn for `pet` |
| 11 | Compliance | `.kickstart/compliance.md` rows touched since last release have status and evidence | stale rows |
| 12 | Rollback plan | `docs/runbook.md` rollback section present and matches the hosting platform | missing |

In `enforced` mode, any `fail` stops here. In `advised` mode, list the fails, say "ADVISED: would have blocked", and ask for an explicit "proceed anyway".

Show the result as a 12-line table, then a one-line verdict.

## Step 2: Version and changelog

- Determine the next version from Conventional Commits since the last tag: `feat` → minor, `fix` → patch, `!` or `BREAKING CHANGE` → major. Pre-1.0 projects: minor for breaking.
- Move Unreleased entries under the new version heading with today's date, grouped Added / Changed / Fixed / Security.
- Bump the version in the manifest (`package.json`, `pyproject.toml`, `Cargo.toml`, `*.csproj`, `pubspec.yaml`, `mix.exs`…) and anywhere else `project.md` says.
- Commit: `chore(release): v<version>`. Tag: `v<version>`.

## Step 3: Build and verify artefact

- Run the build. For containerised projects: build the image, run it locally, hit `/health`, scan the image (`trivy image` if available; otherwise note skipped).
- `scale`: generate SBOM (`syft` or ecosystem tool) and attach to the release.

## Step 4: Deploy

Use the platform in `project.md`. Prefer the platform's CLI or the CI release workflow created by `kickstart-scaffold`. Order for `scale`: staging → smoke test → production. Order for `pet`: production with a smoke test after.

Smoke test: `/health` returns the new version; one authenticated request succeeds; one key user flow from the latest feature spec works.

If the user is not authenticated with the platform, prepare everything (tag pushed, release notes written) and give the exact deploy command.

## Step 5: Post-release

- Watch the error tracker and logs for 10 minutes (ask the user to confirm, or poll if a CLI is available). Error rate up or health failing → execute the rollback section of the runbook immediately and say so.
- Create the forge release (GitHub/GitLab) with the changelog section as the body.
- Update `.kickstart/project.md`: `last_release: v<version> <date>`, `last_score`.
- Update `.kickstart/compliance.md` `last_review` if any row changed.

## Step 6: Report

Under ten lines: version, what shipped (from changelog), where it is running, checks that warned, and the rollback command.

## Rules

- Never skip the secret scan or the vulnerability scan to make a date. In advised mode you may proceed, but it is written in the report.
- Never deploy with a failing test, even in advised mode, without the user typing "proceed anyway".
- Never release on a Friday evening for `scale` without saying so; offer Monday.
- Keep release commits free of unrelated changes.
