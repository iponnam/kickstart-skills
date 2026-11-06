---
name: kickstart-scaffold
description: Generates a runnable, production-grade new project for any chosen stack: app skeleton, CI, lint and format, tests, secret and dependency scanning, security headers, structured logging, health endpoint, auth, database with migrations, deployment config, documentation, and the user's first real feature. Use after a stack is chosen in kickstart, or when the user says "scaffold", "bootstrap", "create the project", "set up a new repo for X". Stack-agnostic: uses the framework's official generator first, then layers the production pieces on top.
---

# kickstart-scaffold

Produce a project a stranger can clone, run and deploy in five minutes, with security and quality built in from the first commit. Use the ecosystem's official generator wherever one exists, then add what generators leave out.

## Inputs

From `.kickstart/project.md`: stack block, `scale`, `enforcement`. From `.kickstart/compliance.md`: the top planned controls. From the user: the first feature (ask in one line if not yet known: "What is the first thing a user should be able to do?").

## The freshness rule (mandatory)

Generators, flags, library names and recommended config change between releases. Do not scaffold from memory.

- Before Phase 1, open the framework's official getting-started or installation page and use the generator command and flags it shows today. If it differs from `references/layouts.md`, follow the official page and note the difference in `.kickstart/decisions/0001-stack.md`.
- Before adding any security, logging, auth or testing library from `references/layouts.md`, confirm on its official repository or registry page that it is maintained and see its current major version. Pick a maintained alternative if it is archived or deprecated.
- Never write a version number into a manifest from memory. Let the package manager resolve the latest stable version and commit the lockfile.
- `references/layouts.md` was last checked as shown on its `last_verified:` line. Treat anything there older than 24 hours as a starting point, not a source of truth.

## Order of work

Do these in order. After each phase, run the project's test or build command. Do not move on with a red step; fix it or tell the user why it cannot be fixed.

### Phase 1: Skeleton (official generator)

Use the framework's own scaffolder with a non-interactive flag set where possible, for example `create-next-app`, `django-admin startproject`, `rails new`, `laravel new`, `dotnet new`, `cargo init`, `go mod init`, `npm create svelte`, `npx create-expo-app`, `flutter create`, `npm create astro`. Choose TypeScript when the language is JavaScript-family. Commit: `chore: scaffold <framework>`.

If no generator exists, create the minimal idiomatic layout for the language (see `references/layouts.md`).

### Phase 2: Quality tooling

- Linter and formatter configured with the ecosystem default (eslint + prettier or biome; ruff + black; gofmt + golangci-lint; rubocop; php-cs-fixer + phpstan; dotnet format + analyzers; clippy + rustfmt).
- Type checking on where the language allows (tsc strict, mypy or pyright, phpstan level 6+).
- Test runner with one passing unit test and one integration test hitting the health endpoint (vitest/jest, pytest, go test, rspec/minitest, phpunit, xunit, cargo test).
- `.editorconfig`, `.gitignore` for the ecosystem, `.gitattributes` (LF).
- Scripts in the manifest or a `Makefile`/`justfile` so `install`, `dev`, `test`, `lint`, `build` work by those names. Record them in `project.md` under `Commands`.

### Phase 3: Security baseline (OWASP mapped)

Implement the OWASP controls from `kickstart-compliance/references/owasp-top10.md` in code:

- Config from environment only; `.env.example` committed with every variable documented and no values; `.env` git-ignored.
- Security headers middleware (CSP with a sane default, HSTS, nosniff, frame-ancestors, referrer-policy, permissions-policy).
- Input validation at the boundary with a schema library.
- Rate limiting on auth and expensive routes.
- Structured JSON logging with request ID; no secrets or PII in logs.
- Error tracking hook point (Sentry DSN read from env, no-op if unset).
- Health endpoint `/health` returning build version and DB connectivity.
- Secret scanning and dependency scanning wired into CI (Phase 5) and into hooks via `kickstart-guardrails`.
- The six baseline security tests from the OWASP reference (401 on protected route, cross-user access denied, bad body rejected, login rate-limited, headers present, fail closed on error).

### Phase 4: Data and auth

- Database per `project.md` with migrations tool (Prisma/Drizzle, Alembic, Django migrations, Rails migrations, golang-migrate/goose, Flyway, EF Core, sqlx).
- Local dev database via `docker-compose.yml` (Postgres, Redis if needed) or SQLite for `pet` when the stack allows.
- Auth per `project.md`: provider SDK wired, or library with sessions configured per OWASP A07:2025 (HttpOnly, Secure, SameSite, rotation). Signup, login, logout, password reset flows (or provider-hosted equivalents). One `User` model with timestamps and soft-delete flag for privacy-law deletion handling.
- Seed script with one admin and sample data for local dev.

### Phase 5: CI and deploy

- CI workflow (GitHub Actions by default, mirroring the repo host) with jobs: install with lockfile, lint, typecheck, test with coverage upload as artifact, dependency vulnerability scan, secret scan, build. Cache dependencies. Pin action versions to a tag at minimum, to a digest for `scale`.
- Dependabot or Renovate config: weekly, grouped minor/patch.
- Deployment config for the chosen host: `vercel.json`, `fly.toml`, `railway.json`, `render.yaml`, `Dockerfile` + `.dockerignore` (multi-stage, non-root user, pinned base image), or platform IaC for `scale`.
- Preview deployments per pull request if the host supports it.
- `scale` only: staging environment config, release workflow on tags (build, SBOM via syft or the ecosystem tool, changelog, deploy).

### Phase 6: Documentation

- `README.md`: what it is, one-command run, environment variables table, scripts, deploy, where things live. Keep it under 150 lines.
- `docs/architecture.md`: a diagram in Mermaid, request flow, data model summary, the "why" for each major choice (link to `.kickstart/decisions/`).
- `docs/runbook.md`: how to deploy, roll back, rotate a secret, restore a backup, handle an incident (short).
- `CONTRIBUTING.md`: branch naming, commit style (Conventional Commits), PR checklist.
- `.kickstart/decisions/0001-stack.md` (from stack-advisor), `0002-auth.md`, `0003-database.md` in ADR shape.
- `.kickstart/decisions/threat-model.md`: 10–20 lines for `pet`, a table of assets, threats, mitigations for `scale`.

### Phase 7: First feature

Implement the user's first feature end to end using the `kickstart-feature` workflow in compressed form: a short spec in `docs/features/0001-<name>.md`, the data model change with migration, the API or server action, the UI, tests, and a line in the changelog. This proves the whole chain works and gives the user something real on day one.

### Phase 8: Hand-off

1. Run full `lint`, `test`, `build` and the audit script from `kickstart-audit`. Target: score ≥ 85 for `scale`, ≥ 75 for `pet`. Report the score.
2. Update `.kickstart/project.md` with final commands and the audit score.
3. Commit in logical steps (scaffold, tooling, security, data/auth, ci/deploy, docs, feature) with Conventional Commit messages.
4. Tell the user: how to run it locally (three commands maximum), what is deployed where (or how to deploy in one command), and the credentials for the seeded admin in local dev only.

## Rules

- Never generate placeholder secrets that look real. Use `change-me` and document them in `.env.example`.
- Never pin to a framework version you have not verified exists. Use the generator's current default.
- Prefer the framework's conventions over custom structure. A new team member should recognise the layout.
- Keep generated code small. No speculative abstractions, no unused modules, no example pages left over from the generator.
- Match the user's enforcement choice: with `enforced`, hooks are installed by `kickstart-guardrails` before the first feature commit so the feature commit itself passes the gates.
- If a step needs a network call or an account the user does not have (hosting login, provider API key), create the config, document the variable, and continue. Do not block.
- For `pet`: skip staging, SBOM, IaC and the full threat model table. Everything else stays.

## Stack-specific notes

See `references/layouts.md` for per-ecosystem commands, directory layout, the security-header and logging libraries to use, and the test for each OWASP control. Consult it before Phase 1 for the chosen stack.
