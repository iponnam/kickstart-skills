---
name: kickstart-compliance
description: "Chooses and operationalises security and compliance frameworks for a software project. OWASP Top 10:2025 is always included. Recommends further frameworks (SOC 2, ISO 27001, GDPR, HIPAA, PCI DSS, DPDP, DORA, NIS 2, RBI, SEBI, MAS TRM, SAMA, Essential Eight, CMMC, NIST, CCPA and 60+ more) based on the user's region and industry, lets them pick, and writes .kickstart/compliance.md as an engineering checklist with each control marked implemented, planned or not applicable. Every fact comes from the framework's official governing body and is re-verified when older than 60 days. Use during kickstart setup, when the user asks \"what compliance do I need\", \"are we GDPR compliant\", \"add SOC 2 controls\", or before building auth, payments, logging or data storage."
---

# kickstart-compliance

Compliance here means engineering controls with a status, not legal advice. Every control you write must be something a developer can implement, configure or document, and something an audit can check.

## The freshness rule (mandatory, applies to every step)

Laws, standards and their deadlines change. This skill never relies on memory.

1. **No facts from memory.** Do not state a framework's version, scope, threshold, deadline, retention period, age limit or penalty from your training data. Every such fact must come from a framework record whose official sources were checked within the last **60 days**.
2. **Check age before use.** Before using any framework record, run:
   ```bash
   python3 <this-skill>/scripts/freshness.py check --ids <id1,id2,...>
   ```
   It looks in the project cache `.kickstart/cache/frameworks/` first, then in the bundled `references/frameworks/`, and reports each record's age and its official URLs.
3. **Re-verify stale records.** For every record with `"stale": true`:
   - Run `freshness.py adopt --ids <id>` to copy it into the project cache if it is not there yet.
   - Fetch each URL in its `official_sources`, plus the governing body's news or updates page. Use the official site only: regulator, standard owner, legislature or official gazette. Never use vendors, law firms, Wikipedia or news to establish a fact.
   - Compare `current_version`, `superseded_by`, the scope and every row in "Deadlines and numbers". Edit the cached record where the official source now says something different, and add a line under `## Notes` saying what changed and when.
   - Run `freshness.py mark --ids <id>` to stamp `last_verified` with the current time.
4. **When a source cannot be reached**, do not block. Use the record as it stands, but label every number taken from it in your answer and in `.kickstart/compliance.md` as `unverified since <last_verified date>`. Tell the user in one line which official site could not be reached.
5. **New frameworks.** If the user needs a framework with no record, research it from official sources using the record template in `references/frameworks/README.md` and save it to the cache before using it.
6. **Re-check early when there is a signal.** Re-verify a record before 60 days if the user mentions a recent change, the record's Notes list a pending amendment or effective date that has now passed, or an official page you are already reading announces an update.
7. **Cost control.** Verify only what you are about to use: OWASP Top 10, the candidates you present, and the frameworks the user selects. Never re-verify the whole catalog in one go.

The project cache is plain Markdown under `.kickstart/cache/`, so the team can commit it and review what changed.

## Inputs

- `region`: countries or regions where users live or data is stored
- `industry`: what the product does (fintech, health, education, SaaS, e-commerce, government, defence, automotive, aviation, AI…)
- `scale`: `pet` or `scale` from `.kickstart/project.md`
- Optional: findings from `kickstart-audit`, the chosen stack, and whether the product handles payments, health data, children's data, or AI decisions

## Step 1: Always-on baseline

OWASP Top 10 is mandatory for every project, including pet projects. Apply the freshness rule to `owasp-top10` first: if OWASP has published a newer edition, use it and relabel IDs. Then load `references/owasp-top10.md` and include all ten categories in the checklist. For `pet` projects mark the heavier items (for example SBOM) as `planned` rather than removing them.

## Step 2: Recommend frameworks

Load `references/framework-catalog.md`. It lists every framework with an `id`, `region`, `industry`, `type` and `trigger` tags, and links to its record in `references/frameworks/<id>.md`. The catalog tags are for shortlisting only. They carry no deadlines or versions. Select candidates:

1. Match on region. Every framework whose region includes the user's region or is `global`.
2. Filter by industry. Keep frameworks tagged with the user's industry or `any`.
3. Apply triggers. Add frameworks whose `trigger` matches facts you know: handles card payments (PCI DSS), health data (HIPAA, PHIPA, DTAC), children (COPPA, and the age rules in privacy laws), students (FERPA), AI systems (EU AI Act, ISO 42001, NIST AI RMF), sells to enterprises (SOC 2, ISO 27001), sells to US federal (NIST 800-53, CMMC, FedRAMP), EU financial (DORA), EU essential services (NIS 2), Indian banking or payments (RBI CSF, RBI PA/PG, RBI DPSC), Indian SEBI-regulated entities (SEBI CSCRF), Singapore finance (MAS TRM), Saudi (NCA ECC, SAMA, PDPL), Australia government (ISM, Essential Eight), automotive supply chain (TISAX), aviation software (EASA), medical devices (ISO 13485).
4. Apply the freshness rule to the shortlist (at most 8). Drop or replace any candidate whose official source shows it was withdrawn or superseded.
5. Rank into three groups and present them that way:
   - **Required by law or regulator** for this region and industry
   - **Expected by customers** (certifications buyers ask for)
   - **Optional, good practice**

Present each candidate in one line: what it is, why it applies, its current version, and effort as `S` (days), `M` (weeks) or `L` (months). Every version and number in that line comes from a record verified in the last 60 days, or carries the `unverified since` label. Then say: "Pick any by number, add others from the full catalog, or say 'just OWASP' to keep only the baseline."

For `pet` projects, say explicitly that regulatory frameworks still apply if the project has real users in a regulated domain, but suggest keeping the selection to OWASP plus at most one privacy law.

## Step 3: Write `.kickstart/compliance.md`

Format:

```markdown
# Compliance scope

- region: ...
- industry: ...
- frameworks: OWASP Top 10:2025, <chosen, with versions...>
- owner: <name or "unassigned">
- last_review: <YYYY-MM-DD>
- sources_verified: <ISO timestamp of the oldest last_verified among chosen records>

## Summary
| Framework | Version | Controls | Implemented | Planned | N/A |
|---|---|---|---|---|---|
| OWASP Top 10 | 2025 | 10 | 4 | 6 | 0 |
| GDPR | Reg. (EU) 2016/679 | 14 | 2 | 10 | 2 |

## Key deadlines
| Framework | What | Value | Official reference |
|---|---|---|---|
| GDPR | Breach notice to supervisory authority | not later than 72 hours | Art. 33(1) |

## OWASP Top 10:2025
| ID | Control | Status | Evidence / where | Notes |
|---|---|---|---|---|
| A01:2025 | Broken access control: every route checks authorisation server-side | planned | src/middleware/auth.ts | |
...

## GDPR
| ID | Control | Status | Evidence / where | Notes |
...
```

Rules:

- Status is exactly one of `implemented`, `planned`, `n/a`. No other words.
- `Evidence / where` points at a file, config key, CI job, document or process. Blank means not started.
- Build each framework's control rows from the "Engineering obligations" table in its verified record, keeping the record's IDs and official references. `references/control-checklists.md` holds cross-framework groupings that help avoid duplicate work; it never overrides a record.
- Copy the deadlines that matter to engineering (incident and breach notice, request response windows, log retention) into `## Key deadlines`, with the official reference.
- For an existing project, use `kickstart-audit` findings to pre-fill `implemented` where the audit proved it (for example: secret scanning in CI, dependency scanning present, HTTPS enforced, headers set).
- Append a `## Not selected` section listing the recommended-but-declined frameworks with the reason, so the next review can reconsider.

## Step 4: Hand off

Return to the caller with: chosen frameworks with versions, counts (controls / implemented / planned), and the three highest-impact `planned` controls so `kickstart-scaffold` or `kickstart-feature` can implement them first.

## Day-to-day use

When invoked outside setup (for example "are we GDPR ready?"):

1. Read `.kickstart/compliance.md`.
2. Apply the freshness rule to every framework listed. If a re-verification changed a version, deadline or obligation, update the checklist rows and `## Key deadlines`, and tell the user what changed with the official reference.
3. Verify each `implemented` control's evidence still exists. Downgrade to `planned` if not, and say which.
4. Report the summary table and the delta since `last_review`.
5. Offer to implement the next `planned` control.

When a feature touches auth, personal data, payments, logging, file upload, third-party data sharing or AI model calls, `kickstart-feature` will call you to list the controls that apply. Apply the freshness rule to the affected frameworks, then answer with the relevant rows only.

## Boundaries

- Say clearly that this is engineering preparation, not legal advice or certification. SOC 2, ISO 27001, PCI DSS and similar require an external auditor, QSA or certification body. Each record's "Assessment and certification" section says who.
- Do not invent control IDs. Use the IDs in the records. Where a framework has no public numbering, use `<FW>-01…` and keep it stable.
- ISO and some AICPA texts are paid. Records based only on the official free abstract are marked `verification: partial`. Say so when the user relies on them, and recommend buying the standard for certification work.
- Keep the catalog honest: if a framework is not in `references/framework-catalog.md`, say so and offer to research it from official sources or add it as a custom framework with user-supplied controls.
