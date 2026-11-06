# Per-ecosystem scaffold notes

What to run, where things go, and which libraries implement each production piece. Versions are deliberately not pinned here; use the generator's current default and record the versions in the lockfile.

## TypeScript: Next.js (App Router)

- Generate: `npx create-next-app@latest <name> --ts --app --eslint --src-dir --import-alias "@/*" --use-pnpm` (or npm/yarn per user).
- Layout: `src/app` routes, `src/lib` shared code, `src/db` schema + migrations, `src/server` server-only code, `tests/` (vitest + testing-library), `e2e/` (playwright, `scale` only).
- Security headers: `next.config.ts` `headers()` or middleware; CSP with nonce in `middleware.ts`.
- Validation: zod on every server action and route handler input.
- Rate limiting: `@upstash/ratelimit` (serverless) or in-memory for `pet`.
- Logging: pino with request id from headers; redact `authorization`, `cookie`, `password`.
- Errors: `@sentry/nextjs`, DSN from env.
- DB: Prisma or Drizzle + Postgres (Supabase/Neon). Migrations committed.
- Auth: Supabase Auth, Clerk, or Auth.js. Sessions via HttpOnly cookies.
- Tests: vitest for units, route handler tests with `next-test-api-route-handler` or direct function calls, playwright for the five security tests on `scale`.
- CI: `pnpm install --frozen-lockfile`, `pnpm lint`, `pnpm typecheck` (`tsc --noEmit`), `pnpm test -- --coverage`, `pnpm audit --audit-level=high`, gitleaks, `pnpm build`.
- Deploy: Vercel (zero config) or Dockerfile (standalone output) for Railway/Fly.

## TypeScript: SvelteKit / Hono / NestJS

- SvelteKit: `npx sv create <name>` (TypeScript, eslint, prettier, vitest, playwright). Hooks in `src/hooks.server.ts` for headers, auth, request id.
- Hono: `npm create hono@latest`; middlewares `secureHeaders()`, `logger()`, zod validator; deploy to Cloudflare Workers or Node.
- NestJS: `npx @nestjs/cli new <name>`; `helmet`, `@nestjs/throttler`, class-validator or zod pipes, pino via `nestjs-pino`.

## Python: Django

- Generate: `uv init` or `python -m venv`; `django-admin startproject config .`; one app per domain (`apps/accounts`, `apps/<feature>`).
- Settings split: `config/settings/{base,dev,prod}.py`, all secrets from env via `django-environ`.
- Security: `SECURE_*` settings, `django-csp`, `django-ratelimit` or `django-axes` for login, `django-allauth` for auth.
- Validation: forms/serializers (DRF) or pydantic for API payloads.
- Logging: `python-json-logger`, request id middleware (`django-log-request-id`).
- Errors: `sentry-sdk[django]`.
- Tests: pytest + pytest-django + factory_boy; coverage via pytest-cov.
- Lint: ruff (lint + format), mypy with django-stubs.
- CI: `uv sync --frozen`, `ruff check`, `ruff format --check`, `mypy`, `pytest --cov`, `pip-audit`, gitleaks, `python manage.py check --deploy`.
- Deploy: Dockerfile (gunicorn + whitenoise or nginx), Railway/Render/Fly; `collectstatic` in build.

## Python: FastAPI

- Generate: `uv init`; layout `app/{main,api,core,db,models,schemas,services}`, `alembic/`, `tests/`.
- Security: `secure` or custom middleware for headers, `slowapi` for rate limiting, OAuth2/JWT via `authlib` or a provider; never roll JWT by hand.
- Validation: pydantic models on every endpoint.
- Logging: structlog JSON with request id middleware.
- DB: SQLAlchemy 2 + Alembic.
- Tests: pytest + httpx AsyncClient + testcontainers or SQLite for `pet`.

## Go

- Generate: `go mod init <module>`; layout `cmd/<app>/main.go`, `internal/{http,auth,store,config}`, `migrations/`, `web/` if templates.
- Router: chi or echo. Headers: `unrolled/secure` or hand-written middleware. Rate limit: `golang.org/x/time/rate` or `ulule/limiter`.
- Validation: `go-playground/validator` on request structs.
- Logging: `log/slog` JSON with request id.
- DB: `pgx` + `sqlc`; migrations with `golang-migrate` or `goose`.
- Auth: provider (OIDC via `coreos/go-oidc`) or `alexedwards/scs` sessions + argon2id.
- Tests: `go test ./... -race -cover`, httptest for the security tests.
- Lint: `golangci-lint`, `govulncheck`, `gofmt`.
- Deploy: distroless multi-stage Dockerfile; Fly/Cloud Run.

## Ruby: Rails 8

- Generate: `rails new <name> --database=postgresql --css=tailwind` (add `--api` for API-only).
- Auth: `bin/rails generate authentication` (Rails 8 built-in) or Devise.
- Security: `config.force_ssl`, `secure_headers` gem or `content_security_policy` initializer, `rack-attack` for rate limiting, Brakeman in CI.
- Logging: `lograge` JSON + request id (built in).
- Tests: minitest or rspec, `simplecov`.
- Lint: rubocop (rails-omakase), `bundler-audit`.
- Deploy: Kamal (built in) to a VPS, or Fly/Render Dockerfile.

## PHP: Laravel

- Generate: `laravel new <name>` (choose Breeze/Inertia, Pest).
- Security: `spatie/laravel-csp`, built-in throttle middleware, Fortify/Breeze auth, `config('app.debug')` from env.
- Validation: Form Requests on every endpoint.
- Logging: JSON formatter channel with request id.
- Tests: Pest; `composer audit`; `phpstan` (larastan) level 6+, `pint` for format.
- Deploy: Laravel Cloud, Forge, or Dockerfile (php-fpm + nginx) on Railway/Fly.

## Java/Kotlin: Spring Boot

- Generate: Spring Initializr (web, security, data-jpa, validation, actuator, flyway, postgresql).
- Security: Spring Security with OIDC provider, headers on by default, `bucket4j` for rate limiting.
- Validation: Jakarta validation on DTOs.
- Logging: logback JSON encoder, MDC request id filter.
- Health: actuator `/actuator/health`.
- Tests: JUnit 5 + Testcontainers; `jacoco`.
- Lint/sec: spotless, OWASP dependency-check or `gradle-dependency-submission` + Dependabot.
- Deploy: Jib or multi-stage Dockerfile; Cloud Run/ECS.

## C#: ASP.NET Core

- Generate: `dotnet new webapi` or `dotnet new blazor`; add Identity + EF Core + FluentValidation + Serilog.
- Security: `UseHsts`, `UseHttpsRedirection`, `NetEscapades.AspNetCore.SecurityHeaders`, built-in rate limiting middleware.
- Tests: xUnit + WebApplicationFactory + Testcontainers.
- Lint/sec: `dotnet format`, analyzers, `dotnet list package --vulnerable` in CI.
- Deploy: Dockerfile; Azure App Service / Container Apps.

## Rust: axum

- Generate: `cargo new <name>`; crates `axum`, `tower-http` (headers, trace, rate limit), `sqlx` with migrations, `tracing` JSON, `validator`.
- Lint/sec: `cargo clippy -D warnings`, `cargo fmt --check`, `cargo audit`, `cargo deny`.

## Mobile: Expo / Flutter

- Expo: `npx create-expo-app@latest <name> -t`; EAS build config; secure storage for tokens (`expo-secure-store`); certificate pinning on `scale`; backend via Supabase or an api-service.
- Flutter: `flutter create <name>`; `flutter_secure_storage`; `flutter analyze` + `dart format` in CI; `very_good_analysis` lint set.
- Both: no secrets in the app bundle; API keys scoped and restricted by bundle id; crash reporting (Sentry) wired.

## Content: Astro / Hugo / Docusaurus

- Astro: `npm create astro@latest`; `astro check`; headers via host config (`_headers` for Cloudflare/Netlify, `vercel.json`); forms via a provider, never inline API keys.
- Minimal CI: build + link check (`lychee`) + secret scan.

## Generic Dockerfile pattern (any stack)

```dockerfile
# syntax=docker/dockerfile:1
FROM <base>:<tag>@sha256:<digest> AS build
WORKDIR /app
COPY <manifest and lockfile> ./
RUN <install with frozen lockfile>
COPY . .
RUN <build>

FROM <runtime-base>:<tag>@sha256:<digest>
WORKDIR /app
RUN adduser --system --uid 10001 app
COPY --from=build --chown=app /app/<artifacts> ./
USER app
ENV NODE_ENV=production   # or equivalent
EXPOSE 8080
HEALTHCHECK CMD <curl or wget http://localhost:8080/health>
CMD ["<entrypoint>"]
```

Digest pinning is required for `scale`, recommended for `pet`.

## Generic CI job list (any stack)

```yaml
jobs:
  quality:
    steps: [checkout, setup-runtime, install --frozen-lockfile (cached), lint, typecheck, test --coverage, upload coverage artifact]
  security:
    steps: [checkout, gitleaks (full history on default branch, diff on PR), dependency vulnerability scan (ecosystem tool or osv-scanner), fail on critical/high when enforcement=enforced]
  build:
    needs: [quality, security]
    steps: [checkout, build, (scale) docker build + sbom + image scan (trivy)]
```

Secret scanning tool order of preference: `gitleaks` (fast, single binary), `trufflehog` (verified secrets), GitHub secret scanning push protection (turn it on in repo settings).

Dependency scanning by ecosystem: `npm audit` / `pnpm audit` / `yarn npm audit`, `pip-audit`, `cargo audit`, `govulncheck`, `bundler-audit`, `composer audit`, `dotnet list package --vulnerable`, Gradle/Maven via `osv-scanner` or OWASP dependency-check. `osv-scanner` works for all lockfiles and is the universal fallback.
