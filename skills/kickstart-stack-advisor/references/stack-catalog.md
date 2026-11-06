# Stack catalog

Curated, production-proven stacks by archetype. Each entry lists what kickstart-scaffold will generate. "Ops" is the operational burden: 1 (none) to 5 (you run servers).

Legend: FE front end, BE back end, DB database, Host hosting, CI continuous integration. All stacks get: lint, format, tests, secret scanning, dependency scanning, security headers, structured logging, health endpoint, Dockerfile where applicable, and docs.

## web-app (SaaS, dashboards, marketplaces, booking, CRM)

| Stack | Language | FE | BE | DB | Auth | Host | Ops | Best for |
|---|---|---|---|---|---|---|---|---|
| **Next.js + Supabase** | TypeScript | Next.js (App Router) | Next.js route handlers / server actions | Postgres (Supabase) | Supabase Auth | Vercel | 1 | Fastest full-stack for pet and early scale; huge community |
| **Next.js + Prisma + Postgres** | TypeScript | Next.js | Next.js + Prisma | Postgres (Neon / RDS) | Auth.js or Clerk | Vercel or Railway | 2 | Scale with more control over the data layer |
| **SvelteKit + Drizzle** | TypeScript | SvelteKit | SvelteKit endpoints | Postgres or SQLite (Turso) | Lucia / Auth.js | Cloudflare Pages, Vercel | 1–2 | Lighter bundles, simpler mental model |
| **Django + HTMX** | Python | Django templates + HTMX | Django | Postgres | Django auth (+ allauth) | Railway, Render, Fly.io | 2 | Python teams; admin panel for free; batteries included |
| **Rails 8** | Ruby | Hotwire | Rails | Postgres or SQLite | Rails auth generator / Devise | Fly.io, Render, Kamal on a VPS | 2–3 | Fast product teams; convention over configuration |
| **Laravel + Inertia** | PHP | Vue or React via Inertia | Laravel | MySQL or Postgres | Laravel Breeze / Fortify | Laravel Cloud, Forge + VPS | 2 | PHP teams; very complete ecosystem |
| **Spring Boot + React** | Java / Kotlin | React (Vite) | Spring Boot | Postgres | Spring Security + OIDC provider | AWS ECS, Azure App Service, GCP Cloud Run | 3 | Enterprise, regulated, existing Java estate |
| **ASP.NET Core + Blazor or React** | C# | Blazor or React | ASP.NET Core | SQL Server or Postgres | ASP.NET Identity + Entra | Azure App Service | 3 | Microsoft shops, enterprise |
| **Go + templ/HTMX or React** | Go | templ + HTMX or React | Go (chi / echo) | Postgres | Provider (Clerk, Auth0) or library | Fly.io, Cloud Run, VPS | 3 | Small binaries, high performance, low hosting cost |
| **Phoenix LiveView** | Elixir | LiveView | Phoenix | Postgres | phx.gen.auth | Fly.io | 3 | Real-time heavy apps with modest teams |

## content-site (marketing, blog, docs, portfolio)

| Stack | Notes | Ops |
|---|---|---|
| **Astro** | Content collections, Markdown/MDX, islands for interactivity. Deploy to Cloudflare Pages, Netlify, Vercel. Free. | 1 |
| **Next.js static export** | When the site will grow into an app. | 1 |
| **Hugo** | Fastest builds, Go templates, great for docs. | 1 |
| **Docusaurus** | Documentation sites with versioning and search. | 1 |
| **WordPress (managed)** | Non-technical editors who need a CMS. Use managed hosting (WP Engine, Kinsta). Keep plugins minimal; security scanning matters. | 2 |

## api-service (backend for mobile, partners, integrations)

| Stack | Language | Framework | DB | Host | Ops | Best for |
|---|---|---|---|---|---|---|
| **FastAPI** | Python | FastAPI + SQLAlchemy/SQLModel + Alembic | Postgres | Railway, Fly.io, Cloud Run | 2 | Python; auto OpenAPI docs; async |
| **NestJS or Hono** | TypeScript | NestJS (structured) or Hono (lightweight, edge-capable) | Postgres via Prisma/Drizzle | Railway, Cloudflare Workers (Hono), Fly.io | 2 | TypeScript teams |
| **Go (chi/echo)** | Go | chi or echo + sqlc | Postgres | Fly.io, Cloud Run, VPS | 2–3 | Throughput and small footprint |
| **Spring Boot** | Java/Kotlin | Spring Boot | Postgres | ECS, Cloud Run | 3 | Enterprise |
| **ASP.NET Core Minimal API** | C# | ASP.NET Core | Postgres / SQL Server | Azure | 3 | Microsoft shops |
| **Rust (axum)** | Rust | axum + sqlx | Postgres | Fly.io, VPS | 3–4 | Performance-critical, long-lived services |

## mobile-app

| Stack | Notes | Ops |
|---|---|---|
| **React Native (Expo)** | One codebase, OTA updates, EAS build. Backend: Supabase or an api-service stack above. | 1–2 |
| **Flutter** | One codebase, consistent UI, strong for custom design. Backend: Supabase/Firebase or api-service. | 1–2 |
| **Native Swift + Kotlin** | When platform fidelity or hardware access matters. Two codebases. | 2 |
| Backend options | Supabase (Postgres, auth, storage, realtime), Firebase (NoSQL, auth, push), or any api-service stack. | |

## data-pipeline (ETL, scheduled jobs, reporting)

| Stack | Notes | Ops |
|---|---|---|
| **Python + Dagster or Prefect** | Orchestration with lineage and retries. Warehouse: Postgres, DuckDB, BigQuery, Snowflake. | 2–3 |
| **Python + cron or GitHub Actions schedule** | Pet projects. Script + scheduled workflow + alerting on failure. | 1 |
| **dbt + warehouse** | Transformations in SQL with tests and docs. | 2 |
| **Airflow (managed: MWAA, Cloud Composer, Astronomer)** | Large, established pipelines. | 3 |

## ai-app (chat, RAG, agents, document processing)

| Stack | Notes | Ops |
|---|---|---|
| **Next.js + Vercel AI SDK + Postgres/pgvector** | Streaming chat UI, tool calling, provider-agnostic. Vector search in Postgres avoids a second database. | 1–2 |
| **FastAPI + LangGraph or plain SDK + pgvector** | Python AI ecosystem, agent workflows, evaluation tooling. | 2 |
| **Cloudflare Workers + Workers AI + Vectorize** | Edge, cheap, good for lightweight assistants. | 1 |
| Model providers | Anthropic (Claude), OpenAI, Google (Gemini), open-weight via Groq/Together/Fireworks, or self-hosted (vLLM) for data residency. Design for swap. | |
| Essentials any AI stack gets | Prompt versioning, cost ceiling and alerting, caching, eval set, PII filtering before model calls, prompt-injection guards for tool use. | |

## realtime (chat, collaboration, live dashboards)

| Stack | Notes | Ops |
|---|---|---|
| **Phoenix LiveView / Channels** | Built for this. | 3 |
| **Next.js + Supabase Realtime or Ably/Pusher** | Managed websockets, no servers to run. | 1 |
| **Node + Socket.IO + Redis** | Full control; needs sticky sessions or Redis adapter to scale. | 3 |
| **Cloudflare Durable Objects** | Per-room state at the edge, websockets, cheap. | 2 |

## internal-tool (admin, back-office)

| Stack | Notes | Ops |
|---|---|---|
| **Django admin** | Free CRUD admin over any Postgres schema. | 2 |
| **Retool / Appsmith / Budibase** | Low-code over existing APIs and DBs. Appsmith/Budibase self-hostable. | 1–2 |
| **Refine or React-Admin** | Code-first admin UI in React. | 2 |

## ecommerce

| Stack | Notes | Ops |
|---|---|---|
| **Shopify (+ Hydrogen for custom storefront)** | Fastest to revenue; PCI handled. Fees apply. | 1 |
| **Medusa (Node) or Saleor (Python)** | Open-source headless commerce when you need control. | 3 |
| **Next.js + Stripe/Razorpay + Postgres** | Custom shops with a small catalogue. Hosted checkout keeps PCI scope at SAQ-A. | 2 |

## cli-tool / library

| Language | Tooling |
|---|---|
| Go | cobra, goreleaser, single static binary |
| Rust | clap, cargo-dist |
| Python | typer, uv, pyproject, PyPI |
| TypeScript | commander, tsup, npm |

## Cross-cutting service picks

| Need | Default | Alternatives | Notes |
|---|---|---|---|
| Auth | Supabase Auth, Clerk, Auth.js, framework built-in | Auth0, Firebase Auth, Keycloak (self-host), Ory | Provider for speed; library when you must own user data in your DB |
| Email (transactional) | Resend | Postmark, SendGrid, Amazon SES, Brevo | SES cheapest at scale; Resend/Postmark best DX and deliverability |
| Payments | Stripe (global), Razorpay (India), Paddle or Lemon Squeezy (merchant of record, handles global tax) | Adyen, Braintree, PayPal, Cashfree (India) | Merchant-of-record is worth it when selling globally with a tiny team |
| File storage | Cloudflare R2 (no egress fees), Supabase Storage | S3, GCS, Azure Blob, UploadThing | R2 for public assets and large files |
| Background jobs | Framework-native (Rails Active Job, Django-Q/Celery, BullMQ) | Inngest, Trigger.dev, Temporal | Managed job platforms remove a server |
| Cache / queue | Redis (Upstash managed, or Railway) | Valkey, Dragonfly, SQS | |
| Search | Postgres full-text first | Meilisearch, Typesense, Algolia, Elasticsearch | Add a search engine only when Postgres FTS is not enough |
| Monitoring and errors | Sentry (errors) + provider metrics | Better Stack, Datadog, Grafana Cloud, Honeycomb, Axiom | Sentry free tier covers pet; scale needs logs + metrics + uptime |
| Analytics | PostHog (product), Plausible or Umami (privacy-friendly web) | Mixpanel, Amplitude, GA4 | Privacy-friendly options simplify GDPR/DPDPA cookie consent |
| Feature flags | PostHog, Unleash (self-host) | LaunchDarkly, Flagsmith | |
| CI | GitHub Actions | GitLab CI, CircleCI, Buildkite | Default to the forge the repo lives on |
| IaC (scale only) | Terraform / OpenTofu, Pulumi | SST, CDK | Only when hosting is a raw cloud, not a PaaS |
| Secrets | Platform env vars + 1Password/Doppler/Infisical for team sync | AWS Secrets Manager, Vault | Never in the repo |

## Hosting ladder

Move up only when you must.

1. **Static / edge** (Cloudflare Pages, Vercel, Netlify): sites and front ends. Free to start.
2. **PaaS** (Vercel, Railway, Render, Fly.io, Heroku, Laravel Cloud, Supabase): apps and APIs. $0–50 to start; $100–500 growing.
3. **Container platforms** (Google Cloud Run, AWS App Runner, Azure Container Apps): pay-per-use containers with cloud-native networking. Good for regulated or data-residency needs.
4. **VPS** (Hetzner, DigitalOcean, Linode, OVH): $5–40/month fixed, you run it. Cheapest at scale, highest ops. Pair with Kamal, Coolify or Dokku to keep deploys simple.
5. **Kubernetes** (EKS, GKE, AKS): only with a platform team or hard multi-service requirements.

Data residency: India (RBI payments data), EU (GDPR transfers), Saudi, China and others may require region pinning. All PaaS above let you choose regions; check the specific one (for example Vercel functions region, Supabase project region, Railway region).
