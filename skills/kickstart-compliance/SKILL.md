---
name: kickstart-compliance
description: Chooses and operationalises security and compliance frameworks for a software project. OWASP Top 10 is always included. Recommends further frameworks (SOC 2, ISO 27001, GDPR, HIPAA, PCI DSS, DPDP, DORA, NIS 2, RBI, SEBI, MAS TRM, SAMA, Essential Eight, CMMC, NIST, CCPA and 60+ more) based on the user's region and industry, lets them pick, and writes .kickstart/compliance.md as an engineering checklist with each control marked implemented, planned or not applicable. Use during kickstart setup, when the user asks "what compliance do I need", "are we GDPR compliant", "add SOC 2 controls", or before building auth, payments, logging or data storage.
---

# kickstart-compliance

Compliance here means engineering controls with a status, not legal advice. Every control you write must be something a developer can implement, configure or document, and something an audit can check.

## Inputs

- `region`: countries or regions where users live or data is stored
- `industry`: what the product does (fintech, health, education, SaaS, e-commerce, government, defence, automotive, aviation, AI…)
- `scale`: `pet` or `scale` from `.kickstart/project.md`
- Optional: findings from `kickstart-audit`, the chosen stack, and whether the product handles payments, health data, children's data, or AI decisions

## Step 1: Always-on baseline

OWASP Top 10 is mandatory for every project, including pet projects. Load `references/owasp-top10.md` and include all ten categories in the checklist. For `pet` projects mark the heavier items (for example centralised logging, SBOM) as `planned` rather than removing them.

## Step 2: Recommend frameworks

Load `references/framework-catalog.md`. It lists every framework with `region`, `industry`, `type` and `trigger` tags. Select candidates:

1. Match on region. Every framework whose region includes the user's region or is `global`.
2. Filter by industry. Keep frameworks tagged with the user's industry or `any`.
3. Apply triggers. Add frameworks whose `trigger` matches facts you know: handles card payments (PCI DSS), health data (HIPAA, PHIPA, DTAC), children under 13 (COPPA), students (FERPA), AI decisions (ISO 42001, NIST AI RMF), sells to enterprises (SOC 2, ISO 27001), sells to US federal (NIST 800-53, CMMC, FedRAMP), EU financial (DORA), EU essential services (NIS 2), Indian banking or payments (RBI CSF, RBI PA/PG, RBI DPSC), Indian market infrastructure (SEBI CSCRF), Singapore finance (MAS TRM), Saudi (ECC, SAMA, PDPL), Australia government (ISM, Essential Eight), automotive supply chain (TISAX), aviation software (EASA), medical devices (ISO 13485).
4. Rank into three groups and present them that way:
   - **Required by law or regulator** for this region and industry
   - **Expected by customers** (certifications buyers ask for)
   - **Optional, good practice**

Present at most 8 candidates with one line each: what it is, why it applies, and effort as `S` (days), `M` (weeks) or `L` (months). Then say: "Pick any by number, add others from the full catalog, or say 'just OWASP' to keep only the baseline."

For `pet` projects, say explicitly that regulatory frameworks still apply if the project has real users in a regulated domain, but suggest keeping the selection to OWASP plus at most one privacy law.

## Step 3: Write `.kickstart/compliance.md`

Format:

```markdown
# Compliance scope

- region: ...
- industry: ...
- frameworks: OWASP Top 10, <chosen...>
- owner: <name or "unassigned">
- last_review: <YYYY-MM-DD>

## Summary
| Framework | Controls | Implemented | Planned | N/A |
|---|---|---|---|---|
| OWASP Top 10 | 10 | 4 | 6 | 0 |
| GDPR | 14 | 2 | 10 | 2 |

## OWASP Top 10
| ID | Control | Status | Evidence / where | Notes |
|---|---|---|---|---|
| A01 | Broken access control: every route checks authorisation server-side | planned | src/middleware/auth.ts | |
...

## GDPR
| ID | Control | Status | Evidence / where | Notes |
...
```

Rules:

- Status is exactly one of `implemented`, `planned`, `n/a`. No other words.
- `Evidence / where` points at a file, config key, CI job, document or process. Blank means not started.
- Use the control sets in `references/control-checklists.md`. They are condensed to what engineering can act on. Do not paste full standards.
- For an existing project, use `kickstart-audit` findings to pre-fill `implemented` where the audit proved it (for example: secret scanning in CI, dependency scanning present, HTTPS enforced, headers set).
- Append a `## Not selected` section listing the recommended-but-declined frameworks with the reason, so the next review can reconsider.

## Step 4: Hand off

Return to the caller with: chosen frameworks, counts (controls / implemented / planned), and the three highest-impact `planned` controls so `kickstart-scaffold` or `kickstart-feature` can implement them first.

## Day-to-day use

When invoked outside setup (for example "are we GDPR ready?"):

1. Read `.kickstart/compliance.md`.
2. Verify each `implemented` control's evidence still exists. Downgrade to `planned` if not, and say which.
3. Report the summary table and the delta since `last_review`.
4. Offer to implement the next `planned` control.

When a feature touches auth, personal data, payments, logging, file upload, or third-party data sharing, `kickstart-feature` will call you to list the controls that apply. Answer with the relevant rows only.

## Boundaries

- Say clearly that this is engineering preparation, not legal certification. SOC 2, ISO 27001, PCI DSS Level 1 and similar require an external auditor or QSA.
- Do not invent control IDs for frameworks. Use the IDs in the references. Where a framework has no public numbering, use `<FW>-01…` and keep it stable.
- Keep the catalog honest: if a framework is not in `references/framework-catalog.md`, say so and offer to add it as a custom framework with user-supplied controls.
