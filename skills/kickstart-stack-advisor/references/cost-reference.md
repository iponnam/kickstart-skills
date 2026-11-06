# Cost reference

last_verified: never

These are seed values written on 2026-11-06 from general knowledge, not fetched from pricing pages. Treat every number as stale. Under the skill's freshness rule, fetch the official pricing page (table below) for each provider you present, and use the fetched figure. Fall back to a seed value only when the page cannot be reached, labelled `as of 2026-11-06, not re-checked`. When this file is refreshed from the official pages, set `last_verified:` to the ISO timestamp of that check.

Use these to build the three-tier table (Launch / Growing / Scale).

## Official pricing pages

| Provider | Pricing page |
|---|---|
| Vercel | https://vercel.com/pricing |
| Netlify | https://www.netlify.com/pricing/ |
| Cloudflare Workers / Pages / R2 | https://developers.cloudflare.com/workers/platform/pricing/ · https://developers.cloudflare.com/r2/pricing/ |
| Railway | https://railway.com/pricing |
| Render | https://render.com/pricing |
| Fly.io | https://fly.io/docs/about/pricing/ |
| Heroku | https://www.heroku.com/pricing |
| Google Cloud Run / Cloud SQL / GCS | https://cloud.google.com/run/pricing · https://cloud.google.com/sql/pricing · https://cloud.google.com/storage/pricing |
| AWS (App Runner, Fargate, RDS, S3, SES) | https://aws.amazon.com/pricing/ (service pages linked from there) |
| Azure | https://azure.microsoft.com/pricing/ |
| Hetzner | https://www.hetzner.com/cloud/ |
| DigitalOcean | https://www.digitalocean.com/pricing |
| Laravel Cloud / Forge | https://cloud.laravel.com/pricing · https://forge.laravel.com/pricing |
| Supabase | https://supabase.com/pricing |
| Firebase | https://firebase.google.com/pricing |
| Neon | https://neon.com/pricing |
| PlanetScale | https://planetscale.com/pricing |
| Turso | https://turso.tech/pricing |
| MongoDB Atlas | https://www.mongodb.com/pricing |
| Upstash | https://upstash.com/pricing |
| Pinecone | https://www.pinecone.io/pricing/ |
| Clerk | https://clerk.com/pricing |
| Auth0 | https://auth0.com/pricing |
| WorkOS | https://workos.com/pricing |
| Resend | https://resend.com/pricing |
| Postmark | https://postmarkapp.com/pricing |
| SendGrid | https://sendgrid.com/en-us/pricing |
| Brevo | https://www.brevo.com/pricing/ |
| Mailgun | https://www.mailgun.com/pricing/ |
| Stripe | https://stripe.com/pricing |
| Razorpay | https://razorpay.com/pricing/ |
| Cashfree | https://www.cashfree.com/payment-gateway-charges/ |
| PayPal | https://www.paypal.com/us/business/paypal-business-fees |
| Adyen | https://www.adyen.com/pricing |
| Paddle | https://www.paddle.com/pricing |
| Lemon Squeezy | https://www.lemonsqueezy.com/pricing |
| Backblaze B2 | https://www.backblaze.com/cloud-storage/pricing |
| Anthropic API | https://www.anthropic.com/pricing |
| OpenAI API | https://openai.com/api/pricing/ |
| Google Gemini API | https://ai.google.dev/pricing |
| Groq / Together / Fireworks | https://groq.com/pricing · https://www.together.ai/pricing · https://fireworks.ai/pricing |
| Sentry | https://sentry.io/pricing/ |
| Better Stack | https://betterstack.com/pricing |
| Grafana Cloud | https://grafana.com/pricing/ |
| Datadog | https://www.datadoghq.com/pricing/ |
| PostHog | https://posthog.com/pricing |
| Plausible | https://plausible.io/#pricing |
| GitHub | https://github.com/pricing |

If a page has moved, find the new one from the provider's own home page. Do not take prices from comparison sites or blogs.

Assumptions for tiers unless the user gives numbers:
- **Launch**: 0–100 users, under 10k requests/day, under 1 GB data.
- **Growing**: 1k–10k users, ~100k requests/day, 10–50 GB data, one background worker.
- **Scale**: ~100k users, ~2M requests/day, 200+ GB data, multiple workers, staging environment.

## Hosting (app / API)

| Provider | Free tier | Launch | Growing | Scale | Notes |
|---|---|---|---|---|---|
| Vercel | Hobby: non-commercial, 100 GB bandwidth | $0 (hobby) or $20/seat Pro | $20–100 | $200–1,000+ | Commercial use needs Pro. Bandwidth and function overages add up. |
| Netlify | 100 GB bandwidth | $0 | $19/seat + usage | $100–500 | Similar profile to Vercel for static/edge. |
| Cloudflare Pages / Workers | Generous: 100k requests/day Workers free | $0 | $5 Workers Paid + usage | $50–300 | Cheapest at scale for edge workloads; no egress fees. |
| Railway | $5 trial credit | $5–20 | $20–100 | $200–600 | Usage-based (CPU, RAM, egress). Simple. |
| Render | Free web service sleeps | $7 (starter) | $25–100 | $200–800 | Predictable instance pricing. |
| Fly.io | Pay-as-you-go, small allowance | $5–15 | $30–150 | $200–800 | Multi-region easy; good for Phoenix, Go, Rails. |
| Heroku | None | $7 (eco/basic) | $50–250 | $500+ | Mature, pricier. |
| Google Cloud Run | 2M requests/month free | $0–10 | $20–150 | $200–1,000 | Pay per request/CPU-second. Scales to zero. |
| AWS App Runner / ECS Fargate | Limited | $15–40 | $80–300 | $500–2,000 | AWS native; more setup. |
| Azure App Service / Container Apps | Free tier (F1) limited | $13–55 | $100–300 | $500–2,000 | Microsoft shops. |
| VPS (Hetzner, DigitalOcean, Linode) | None | $5–12 (2 vCPU/4 GB) | $20–50 | $80–300 (several boxes) | You patch and monitor it. Cheapest raw compute. |
| Laravel Cloud / Forge | Forge $12/month + server | $20 | $50–150 | $200–600 | PHP. |
| Supabase (as backend) | 2 projects, 500 MB DB, 50k MAU, pauses after inactivity | $0 | $25 Pro + usage | $100–600 | Includes DB, auth, storage, realtime, edge functions. |
| Firebase | Spark free | $0 | $25–100 | $200–1,000 | NoSQL; costs grow with reads. |

## Database (managed Postgres unless noted)

| Provider | Free tier | Launch | Growing | Scale | Notes |
|---|---|---|---|---|---|
| Supabase Postgres | 500 MB | $0 | $25 + compute | $100–500 | Bundled with auth/storage. |
| Neon | 0.5 GB, scales to zero | $0 | $19 | $69–700 | Branching for preview environments. |
| Railway Postgres | Usage | $5 | $15–50 | $100–300 | Simple. |
| PlanetScale (MySQL/Postgres) | None (since 2024) | $39 | $39–100 | $300+ | Branching, strong at scale. |
| AWS RDS | 750 h/month first year | $15 (t4g.micro) | $60–150 | $300–2,000 (Multi-AZ, replicas) | Backups and storage extra. |
| Google Cloud SQL | None | $10 (shared) | $50–150 | $300–1,500 | |
| Azure Database for PostgreSQL | Limited free | $15 | $60–150 | $300–1,500 | |
| Turso (SQLite, edge) | 500 DBs, 9 GB | $0 | $29 | $99+ | Great for multi-tenant small DBs. |
| MongoDB Atlas | 512 MB | $0 | $57 (M10) | $200–1,000 | If document model is justified. |
| Redis (Upstash) | 10k commands/day | $0 | $10–30 | $50–200 | Serverless pricing. |
| Vector (pgvector in Postgres) | Included | $0 | $0 | $0 extra | Prefer over a separate vector DB until millions of vectors. |
| Pinecone / Weaviate Cloud | Limited | $0 | $50–100 | $300+ | Only when pgvector is insufficient. |

## Auth

| Provider | Free tier | Launch | Growing | Scale | Notes |
|---|---|---|---|---|---|
| Supabase Auth | 50k MAU | $0 | $0 (in Pro) | $0.00325/MAU over 100k | Bundled. |
| Clerk | 10k MAU | $0 | $25 + $0.02/MAU over 10k | $200–2,000 | Best DX; MAU cost at scale is real. |
| Auth0 | 25k MAU (free plan, limited features) | $0 | $35–240 | $1,000+ | Enterprise features cost. |
| Firebase Auth | 50k MAU | $0 | $0 | $0.0055/MAU over 50k (phone auth extra) | |
| Auth.js / Lucia / framework built-in | Free (library) | $0 | $0 | $0 | You own sessions and user table. Email/SMS costs separate. |
| Keycloak / Ory (self-host) | Free | VPS cost | VPS cost | $50–300 | Ops burden. |
| WorkOS (SSO/SCIM for enterprise) | Free up to 1M MAU for AuthKit; SSO $125/connection | $0 | $125+ | $500+ | When enterprise customers need SAML. |

## Email (transactional)

| Provider | Free tier | Growing (50k emails/mo) | Scale (500k/mo) |
|---|---|---|---|
| Resend | 3,000/month | $20 | $90–300 |
| Postmark | 100/month | $15 (10k) → $60 | $300+ |
| SendGrid | 100/day | $20–35 | $90–250 |
| Amazon SES | 3,000/month (12 months) | $5 ($0.10/1k) | $50 |
| Brevo | 300/day | $25 | $150+ |
| Mailgun | 100/day | $35 | $90+ |

## Payments (usage fees, not monthly)

| Provider | Fee (cards, approximate) | Notes |
|---|---|---|
| Stripe | 2.9% + $0.30 (US domestic); +1.5% international; +1% currency conversion | Billing/subscriptions +0.5–0.7%. Hosted Checkout keeps PCI at SAQ-A. |
| Razorpay (India) | 2% (domestic cards, UPI, netbanking); 3% international | Payment data stays in India (RBI). |
| Cashfree (India) | ~1.9–2% | |
| PayPal | 3.49% + $0.49 (US) | |
| Adyen | Interchange++ + $0.13 | Enterprise volumes. |
| Paddle / Lemon Squeezy (merchant of record) | 5% + $0.50 | They handle global sales tax/VAT and invoicing. Worth it for small global teams. |
| Apple / Google app stores | 15% (small business) to 30% | For digital goods in mobile apps. |

Example line: "At 500 sales/month averaging $20, Stripe costs about $440/month in fees."

## File storage and bandwidth

| Provider | Storage | Egress | Notes |
|---|---|---|---|
| Cloudflare R2 | $0.015/GB-month (10 GB free) | $0 | Best default for public assets. |
| AWS S3 | $0.023/GB-month | $0.09/GB after 100 GB free | Egress is the trap. |
| Supabase Storage | 1 GB free; $0.021/GB | 250 GB free on Pro then $0.09/GB | |
| Backblaze B2 | $0.006/GB-month | Free to Cloudflare | Cheap backups. |
| Google Cloud Storage / Azure Blob | ~$0.02/GB-month | ~$0.08–0.12/GB | |

## AI APIs

Prices per million tokens (input / output), approximate. Verify before quoting; these move frequently.

| Model tier | Example | Input | Output | Use for |
|---|---|---|---|---|
| Frontier | Claude Opus-class, GPT-5-class | $5–15 | $25–75 | Hard reasoning, agents |
| Mid | Claude Sonnet-class, GPT-4o-class, Gemini Pro | $2–3 | $10–15 | Default for most apps |
| Small | Claude Haiku-class, GPT-4o-mini-class, Gemini Flash | $0.10–1 | $0.40–5 | Classification, extraction, high volume |
| Open-weight hosted | Llama / Qwen / DeepSeek via Groq, Together, Fireworks | $0.05–1 | $0.10–3 | Cost-sensitive, data residency via region choice |
| Embeddings | text-embedding-3-small, Voyage, Cohere | $0.02–0.13 | n/a | RAG |
| Self-hosted (vLLM on a GPU) | One L4/A10 ≈ $0.50–1.20/hour | fixed | fixed | Data residency, high steady volume |

Cost formula to show the user:

```
requests/day × (input tokens × input price + output tokens × output price) × 30
Example: 2,000 req/day × (1,500 in × $3/M + 500 out × $15/M) × 30 ≈ $720/month on a mid-tier model
Same on a small model (in $0.80/M, out $4/M): ≈ $160/month
```

Always add: prompt caching (often 50–90% off repeated input), response caching for identical queries, a hard monthly spend cap, and per-user rate limits.

## Monitoring, errors, analytics

| Tool | Free tier | Growing | Scale |
|---|---|---|---|
| Sentry | 5k errors/month | $26 | $80–500 |
| Better Stack (uptime + logs) | 10 monitors, 1 GB logs | $25–50 | $200+ |
| Grafana Cloud | 10k metrics series, 50 GB logs | $0–50 | $200+ |
| Datadog | 14-day trial | $15/host + logs | $500–5,000+ |
| PostHog | 1M events/month | $0–50 | $200–1,000 |
| Plausible / Umami | Umami self-host free; Plausible $9 | $9–19 | $69+ |
| Axiom / Honeycomb | Generous free | $25–100 | $200+ |

## Domain, DNS, certificates, misc

- Domain: $10–20/year (.com), $8–15 (.in, .io varies, .ai ~$70+).
- DNS and TLS: free on Cloudflare, Vercel, Netlify, most PaaS.
- GitHub: free for public and private repos with 2,000 Actions minutes/month; Team $4/user.
- Status page: Better Stack, Instatus ($20), or a free static page.
- Secrets manager for teams: 1Password Teams $20/month (5 users), Doppler free for 5 users, Infisical free self-host.

## Rules of thumb to tell users

1. A pet project can run for $0–10/month on free tiers plus a domain. Expect sleeping instances and caps.
2. A growing product with real users is usually $100–400/month before payment fees and AI.
3. At 100k users, $1,000–5,000/month is normal on PaaS. Moving to VPS or containers can cut that by half at the cost of ops time.
4. Egress and AI tokens are the two costs that surprise people. Cap both.
5. Seats (Vercel Pro, GitHub Team, Clerk MAU) are the costs that grow with the team, not the users. Budget per head.
6. Free tiers are for launch, not for production with paying customers: they pause, throttle and lack backups or SLAs.
