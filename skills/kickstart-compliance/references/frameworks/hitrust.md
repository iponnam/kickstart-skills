---
id: hitrust
name: HITRUST CSF
official_name: "HITRUST CSF® (HITRUST Framework) and HITRUST e1, i1 and r2 Validated Assessments and Certifications"
governing_body: HITRUST (HITRUST Alliance); assessments performed by HITRUST Authorized External Assessors and centrally reviewed by HITRUST
type: security
legal_status: certification-scheme
region: global (strongest in US healthcare)
industry: any; strongest in healthcare
current_version: "HITRUST CSF v11.9.0, available in MyCSF as of September 24, 2026"
superseded_by: none
official_sources:
  - title: "HITRUST Framework (HITRUST CSF)"
    url: https://hitrustalliance.net/hitrust-framework
    accessed: 2026-11-06
  - title: "Assessments and Certifications"
    url: https://hitrustalliance.net/assessments-and-certifications
    accessed: 2026-11-06
  - title: "HAA 2026-005 CSF Version 11.9.0 Release (September 24, 2026)"
    url: https://hitrustalliance.net/advisories/haa-2026-005-csf-version-11.9.0-release
    accessed: 2026-11-06
  - title: "HAA 2026-006 CSF v11.8 Creation Deadline for e1 and i1 Assessments"
    url: https://hitrustalliance.net/advisories/haa-2026-006-csf-v11.8-creation-deadline-for-e1-and-i1-assessments
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
"The HITRUST CSF is a comprehensive framework designed to help organizations manage information security, privacy, and risk in a consistent and scalable way. It serves as a unified control library that harmonizes over 70 standards and regulations" (Framework page FAQ; the same site's menu text says "harmonizing 60+ frameworks and standards"). It brings together requirements from "ISO/IEC, NIST, HIPAA, PCI, and GDPR" and is "threat adaptive", using "a Cyber Threat Adaptive engine that analyzes threat intelligence and breach data to proactively update control requirements" (Framework page FAQ). "The HITRUST Framework serves as the foundational control set for HITRUST assessments, including e1, i1, and r2."

## Who it applies to
Voluntary; "designed for organizations of all sizes and across industries" (Framework page FAQ). Typically required contractually by healthcare partners. Assessment choice (Assessments page):
- e1: "ideal for startups and companies with limited risk profiles or less complexity" ("Foundational cybersecurity").
- i1: "a good fit for organizations with robust information security programs already in place" ("Leading Security Practices").
- r2: "Tailored assurance with the highest level of control requirements", risk-based, "for complex environments".

## Engineering obligations
Requirement statements are in the CSF (MyCSF, licensed); not read here. Rows below are from the official advisories and pages.

| ID | Obligation | Official reference |
|---|---|---|
| HT-01 | Choose the assessment (e1/i1/r2) and CSF version; build assessment object in MyCSF before the version creation deadline | Assessments page; HAA 2026-006 |
| HT-02 | Implement the e1 baseline (44 requirement statements in v11.9) as minimum | HAA 2026-005 |
| HT-03 | For i1, implement the 182-requirement baseline (includes all e1 statements) | HAA 2026-005 ("all requirement statements in the e1 baseline are included in the i1 baseline") |
| HT-04 | For r2, implement tailored requirements selected by risk/compliance factors (includes i1 baseline) | HAA 2026-005; Assessments page |
| HT-05 | Address v11.9 refreshed technology requirements: "public key infrastructure (PKI), Transport Layer Security (TLS), and passkeys" | HAA 2026-005 |
| HT-06 | Consider post-quantum cryptography ("Inclusion of post-quantum cryptography consideration") | HAA 2026-005 |
| HT-07 | For AI systems, optional AI Security Certification (standalone or with e1/i1/r2; "Agentic AI" factor added in v11.9) | Assessments page; HAA 2026-005 |
| HT-08 | Inherit controls from certified service providers (e.g. cloud) where available | Assessments page ("inherit existing controls from their certified...") |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Current CSF | "v11.9.0 ... available within MyCSF ... as of September 24, 2026" | HAA 2026-005 |
| e1 baseline size | "the size of the e1 baseline for v11.9 is 44 requirement statements" (Assessments page still says "43 core controls") | HAA 2026-005; Assessments page |
| i1 baseline size | "The size of the i1 baseline remains 182 requirement statements" | HAA 2026-005 |
| Certification validity | e1 "valid for 1 year"; i1 "valid for 1 year"; r2 "valid for 2 years" | Assessments/Framework page menu |
| v11.8 e1/i1 creation cutoff | "Effective December 31, 2026, the ability to create new e1 and i1 assessment objects, including rapid assessments, in MyCSF using CSF v11.8.0 will be disabled" | HAA 2026-006 |
| v11.8 e1/i1 submission cutoff | "Effective March 31, 2027, the ability to submit e1 and i1 assessments using CSF v11.8.0 and earlier will be disabled" | HAA 2026-006 |
| Harmonised sources | "over 70 standards and regulations" (also "60+") | Framework page |

## Assessment and certification
Validated assessments are performed by "External Assessors ... organizations that have been approved by HITRUST to perform assessments", then quality-reviewed and certified by HITRUST (Assessments page: "independently tested, centrally assured"). Outputs: e1, i1 (1-year) or r2 (2-year) certification reports, distributed via the Results Distribution System. Assessments are "traversable": work from e1 or i1 can be applied to i1 or r2. Add-ons: Insights Reports (HIPAA, HICP, NIST SP 800-171, GovRAMP), NIST CSF 2.0 certification "an add-on to r2 assessments", AI Security Certification, AI Risk Management Assessment ("51 controls"). r2 interim assessment requirements: UNVERIFIED (not on pages read).

## Notes
- `framework-catalog.md` row "`+` HITRUST CSF | US | health | security | certification | L" is broadly correct but understates scope: HITRUST says it is for "organizations of all sizes and across industries"; region should not be US-only. Effort "L" applies to r2; e1 is designed for startups, so effort ranges S–L.
- `framework-catalog.md` does not state version; current is CSF v11.9.0 (Sept 24, 2026). HITRUST also issued HAA 2026-007 "CSF Version 11.0-11.3 Decommission Notice" (title verified; dates not read: UNVERIFIED).
- Internal inconsistency on the official site: "43 core controls" (marketing page) vs "44 requirement statements" for the v11.9 e1 baseline (advisory). Use the advisory.
- CSF structure (control categories / assessment domains) not verified: UNVERIFIED.
