---
id: soc3
name: SOC 3
official_name: "SOC 3® - SOC for Service Organizations: Trust Services Criteria for General Use Report"
governing_body: AICPA (ASEC Trust Services Criteria; SSAE No. 18 attestation standards); performed by licensed CPA firms
type: security
legal_status: voluntary-standard
region: US standard, used globally
industry: any (service organizations)
current_version: "Uses the 2017 Trust Services Criteria (With Revised Points of Focus – 2022); guidance in the AICPA SOC 2 Guide (Oct 15, 2022), which covers SOC 3"
superseded_by: none (proposed 2027 SOC 2 TSC exposure draft issued Oct 26, 2026)
official_sources:
  - title: "SOC 3® - SOC for Service Organizations: Trust Services Criteria for General Use Report (topic page)"
    url: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-3
    accessed: 2026-11-06
  - title: "Illustrative SOC 3® Report"
    url: https://www.aicpa-cima.com/resources/download/illustrative-soc-3-r-report
    accessed: 2026-11-06
  - title: "SOC 2® Reporting on an Examination of Controls at a Service Organization ... (AICPA Guide, covers SOC 3)"
    url: https://www.aicpa-cima.com/cpe-learning/publication/soc-2-reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-security-availability-processing-integrity-confidentiality-or-privacy
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
"Like SOC 2, SOC 3 reports address controls relevant to security, availability, processing integrity, confidential and privacy. However, they do not provide the same level of detail. Therefore, they are considered general use reports and can be freely distributed" (SOC 3 topic page). The SOC 2 Guide describes "SOC 3 engagements: General-use reports relevant to security, availability, processing integrity, confidentiality, or privacy" and "includes guidance that will help you prepare and issue a SOC 3 report".

## Who it applies to
Service organizations that want a public, freely distributable report on controls under the Trust Services Criteria (e.g. for a website or marketing), usually alongside a SOC 2.

## Engineering obligations
Same control base as SOC 2 (2017 TSC); see `soc2.md`. Report-specific items:

| ID | Obligation | Official reference |
|---|---|---|
| SOC3-01 | Prepare management's assertion | Illustrative SOC 3 Report page ("includes management's assertion") |
| SOC3-02 | Describe "the boundaries of the system" | Illustrative SOC 3 Report page |
| SOC3-03 | Document "principal service commitments and system requirements" | Illustrative SOC 3 Report page |
| SOC3-04 | Choose and meet the trust services categories in scope (security, availability, processing integrity, confidentiality, privacy) | SOC 3 topic page; Illustrative SOC 3 Report page ("categories ... presented for illustrative purposes only") |
| SOC3-05 | Operate the TSC controls (access, change, monitoring, incident response, etc.) | 2017 TSC (see soc2.md; criterion text UNVERIFIED) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Distribution | "general use reports and can be freely distributed" | SOC 3 topic page |
| Criteria | 2017 Trust Services Criteria (With Revised Points of Focus – 2022) | SOC 3 topic page resources; SOC 2 Guide |

## Assessment and certification
CPA firm examination; output is a general-use SOC 3 report containing management's assertion, system boundaries, principal service commitments and system requirements, and the service auditor's report (Illustrative SOC 3 Report page). No system description in SOC 2 detail and no test results. Whether SOC 3 must cover a period (Type 2-like) is UNVERIFIED (guide behind purchase/login).

## Notes
- `framework-catalog.md` row "SOC 3 ... Public-facing summary of SOC 2" is roughly right, but AICPA describes SOC 3 as a separate general-use report on the same criteria with less detail, not a "summary" of a SOC 2 report. It can be issued with or without a SOC 2 (UNVERIFIED: not stated on free pages). Effort "S (after SOC 2)" is reasonable but not an official statement.
- Illustrative SOC 3 report and SOC 2 Guide are member-only/paid; detail is UNVERIFIED.
