---
name: kickstart-stack-advisor
description: Turns a plain-language description of what someone wants to build into 2–3 concrete, production-ready stack options with monthly cost estimates (hosting, database, auth, email, payments, AI APIs, monitoring) and honest trade-offs. Adapts depth to the audience: a non-technical founder gets a clear recommendation, an engineer gets the comparison. Use for new projects, "which stack should I use", "what will this cost to run", "should I use X or Y", or when kickstart needs a stack before scaffolding.
---

# kickstart-stack-advisor

Give people a decision, not a survey. Three options maximum, one recommended, costs in real numbers, trade-offs in plain words.

## The freshness rule (mandatory)

Prices, free-tier limits, framework versions and product names change monthly. Never quote them from memory.

1. Check the age of the bundled data: `references/cost-reference.md` and `references/stack-catalog.md` each start with a `last_verified:` line. Also check the project cache `.kickstart/cache/pricing.md` if it exists.
2. If the newest of those is more than **24 hours** old, fetch the official pricing page for every provider that appears in the options you are about to present. The URLs are in the "Official pricing pages" table of `references/cost-reference.md`. For each framework you recommend, fetch its official releases or docs page to confirm the current major version and that it is still maintained.
3. Write what you fetched to `.kickstart/cache/pricing.md`: one row per provider with plan, price, free-tier limits, the URL and an ISO timestamp. Use those numbers in the cost table, not the bundled ones.
4. If a page cannot be fetched, use the bundled figure and label it `as of <last_verified date>, not re-checked`. Say which provider could not be checked.
5. Only check what you present. Three options means at most about a dozen pricing pages.

## Inputs you need

Ask only for what is missing. Usually kickstart has already collected these.

1. **What** they want to build (their words).
2. **Scale**: `pet` or `scale` (from `.kickstart/project.md` or ask).
3. **Audience**: technical or not. Infer from how they talk. If they name frameworks, they are technical.
4. **Constraints** (ask in one line, accept "none"): existing skills or languages, must-use cloud, budget ceiling, region for data residency, mobile needed, real-time needed, AI features needed, offline needed.

If the user is non-technical, never ask about languages. Ask instead: "Do you or anyone on your team already know a programming language? If not, I will pick for you."

## Step 1: Classify the product

Pick the closest archetype from `references/stack-catalog.md`:

- `web-app` (dashboard, SaaS, marketplace, booking, CRM)
- `content-site` (marketing, blog, docs, portfolio)
- `api-service` (backend for mobile or partners, integration service)
- `mobile-app` (iOS/Android, with a backend)
- `data-pipeline` (ETL, scheduled jobs, reporting)
- `ai-app` (chat, RAG, agent, document processing)
- `realtime` (chat, collaboration, live dashboards, games)
- `cli-tool` or `library`
- `internal-tool` (admin panels, back-office)
- `ecommerce`

Most products are a primary archetype plus one secondary (for example `web-app` + `ai-app`). Say which.

## Step 2: Build three options

From the catalog, pick three stacks that fit the archetype and the scale answer. Enforce diversity: do not offer three JavaScript stacks. A good spread is:

- **Option 1: fastest to ship.** Managed everything, lowest ops. Usually the recommendation for `pet` and for non-technical users.
- **Option 2: best balance.** Mainstream framework, managed database, one deploy target. Usually the recommendation for `scale`.
- **Option 3: lowest cost at scale or most control.** Containers or a VPS, open-source services. For teams with ops skills or heavy cost sensitivity.

If the user already knows a language, Option 1 or 2 must use it.

## Step 3: Cost it

Use `references/cost-reference.md`. Produce a table with three usage tiers:

| Line item | Launch (0–100 users) | Growing (1k–10k users) | Scale (100k users) |
|---|---|---|---|
| Hosting | | | |
| Database | | | |
| Auth | | | |
| Email | | | |
| Payments (fees, not fixed) | | | |
| File storage | | | |
| AI APIs (if any) | | | |
| Monitoring and errors | | | |
| Domain and DNS | | | |
| **Total fixed per month** | | | |

Rules:
- Show USD, and the user's local currency if they named a region (approximate, say so).
- Separate fixed costs from usage-based fees. Payments are a percentage; say "2.9% + $0.30 per transaction" rather than a monthly figure, then give an example at an assumed volume.
- For AI: state the assumption (requests per day, tokens per request, model) and show the math on one line.
- Free tiers count, but flag their limits (sleeping instances, row caps, monthly active user caps) and when the user will outgrow them.
- Every price comes from a pricing page fetched within the last 24 hours (see the freshness rule) or carries its `as of` label. Show the check date under the table. Present costs as estimates, never as exact.

## Step 4: Trade-offs

For each option, four bullets maximum:

- **Good because**: two strongest reasons for this user.
- **Watch out**: the main risk (vendor lock-in, cold starts, learning curve, ops burden, cost cliff).
- **Hiring and community**: how easy it is to find help or developers.
- **Exit path**: how hard it is to move away later.

For `scale`, add one line each on: how it handles 10x growth, background jobs, and multi-region or data residency if the region demands it.

## Step 5: Recommend

End with one option recommended and a two-sentence reason tied to what the user said. For non-technical users, add a plain-language paragraph: what they are getting, what it costs per month at launch, and what the first week looks like.

Ask the user to pick. Record the choice, the alternatives considered, and the reason in `.kickstart/decisions/0001-stack.md` using this shape:

```markdown
# 0001: Stack choice
- date: YYYY-MM-DD
- status: accepted
- context: <what we are building, scale, constraints>
- decision: <option chosen>
- alternatives: <the other two, one line each>
- consequences: <lock-in, costs, skills needed>
- revisit_when: <trigger, e.g. "monthly bill exceeds $500" or "team grows past 3">
```

Return to kickstart with the structured stack block for `.kickstart/project.md` (language, framework, database, auth, hosting, ci, package_manager, test_runner, lint).

## Opinions that hold across stacks

- Managed Postgres beats everything else for a first database unless the archetype says otherwise. SQLite is fine for `pet` and for single-server tools.
- Use an auth provider or a well-maintained auth library. Never hand-roll sessions and password storage.
- One deploy target. Preview deployments per pull request are worth paying for on `scale`.
- Pick boring, widely used frameworks. The cost of a trendy framework is paid during hiring and at 2 a.m.
- Serverless is great until you need long-running jobs, websockets or predictable latency. Say so when it applies.
- Hosted checkout for payments. Card data must not touch the user's servers (keeps PCI DSS scope at SAQ-A).
- For India-based users or data: note that Indian payment data must stay in India (RBI), so pick providers and regions accordingly.
- For AI apps: start with an API provider, add caching and a cost ceiling on day one, and design so the model can be swapped.
