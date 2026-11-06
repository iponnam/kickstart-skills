---
id: cmmc
name: CMMC 2.0 (Levels 1, 2, 3)
official_name: Cybersecurity Maturity Model Certification (CMMC) Program, 32 CFR Part 170; DFARS CMMC acquisition rule, 48 CFR subpart 204.75 and clauses 252.204-7021 / 252.204-7025
governing_body: U.S. Department of Defense (DoD CIO for 32 CFR 170; DoD acquisition / contracting officers for DFARS); assessments by C3PAOs (authorized by the CMMC Accreditation Body) and DCMA DIBCAC
type: security
legal_status: binding-regulation
region: US (DoD contractors and subcontractors at all tiers, wherever located)
industry: defence
current_version: 32 CFR Part 170 (89 FR 83214, Oct. 15, 2024), effective December 16, 2024; 48 CFR rule (90 FR 43574, Sept. 10, 2025), effective November 10, 2025
superseded_by: none
official_sources:
  - title: 32 CFR Part 170 Cybersecurity Maturity Model Certification (CMMC) Program (eCFR)
    url: https://www.ecfr.gov/current/title-32/subtitle-A/chapter-I/subchapter-G/part-170
    accessed: 2026-11-06
  - title: eCFR version history, 32 CFR 170.3 (effective 2024-12-16)
    url: https://www.ecfr.gov/api/versioner/v1/versions/title-32.json?section=170.3
    accessed: 2026-11-06
  - title: 48 CFR subpart 204.75 Cybersecurity Maturity Model Certification (eCFR)
    url: https://www.ecfr.gov/current/title-48/chapter-2/subchapter-A/part-204/subpart-204.75
    accessed: 2026-11-06
  - title: eCFR version history, 48 CFR 204.7503 (amendment date 2025-11-10)
    url: https://www.ecfr.gov/api/versioner/v1/versions/title-48.json?section=204.7503
    accessed: 2026-11-06
  - title: 48 CFR 252.204-7021 Contractor Compliance With the CMMC Level Requirements (NOV 2025) (eCFR)
    url: https://www.ecfr.gov/current/title-48/chapter-2/subchapter-H/part-252/subpart-252.2/section-252.204-7021
    accessed: 2026-11-06
  - title: 48 CFR 252.204-7012 Safeguarding Covered Defense Information and Cyber Incident Reporting (eCFR)
    url: https://www.ecfr.gov/current/title-48/chapter-2/subchapter-H/part-252/subpart-252.2/section-252.204-7012
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
"The CMMC Program is designed to ensure defense contractors are properly safeguarding FCI and CUI that is processed, stored, or transmitted on defense contractor information systems" and "provides a consistent methodology to assess a defense contractor's implementation of required cybersecurity requirements" (32 CFR 170.1(c)). It uses FAR 52.204-21, NIST SP 800-171 Rev. 2 and selected NIST SP 800-172 requirements. DFARS subpart 204.75 makes a current CMMC status a condition of award when the solicitation specifies a CMMC level.

## Who it applies to
"All DoD contract and subcontract awardees that will process, store, or transmit information, in performance of the DoD contract, that meets the standards for FCI or CUI on contractor information systems" (32 CFR 170.3(a)(1)). It does not apply to "Federal information systems operated by contractors or subcontractors on behalf of the Government" (170.3(b)). It covers solicitations including commercial items "except those exclusively for COTS items" above the micro-purchase threshold (170.3(c)). Flow-down: FCI-only subcontractors need Level 1 (Self); CUI subcontractors need at least Level 2 (Self), or Level 2 (C3PAO) where the prime needs Level 2 (C3PAO) or Level 3 (170.23(a)).

- Level 1: FCI. "the 15 Level 1 requirements listed in the 48 CFR 52.204-21(b)(1)".
- Level 2: CUI. "the 110 Level 2 requirements from NIST SP 800-171 R2".
- Level 3: CUI with APT risk. "the 24 Level 3 requirements selected from NIST SP 800-172 Feb2021" (all from 170.4 definition "CMMC Security Requirements").

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| CMMC-01 | Implement all 15 FAR 52.204-21(b)(1) safeguards for systems holding FCI; all must be MET, "No POA&Ms are permitted for CMMC Level 1" | 170.14(c)(2); 170.15(a)(1) |
| CMMC-02 | Implement all 110 NIST SP 800-171 Rev. 2 requirements for systems holding CUI | 170.14(c)(3); 170.16; 170.17 |
| CMMC-03 | For Level 3, hold Final Level 2 (C3PAO) on the Level 3 scope first, then implement the 24 selected SP 800-172 requirements | 170.18(a)(1); 170.14(c)(4) |
| CMMC-04 | Define the CMMC Assessment Scope (asset categories, CUI assets, security protection assets, ESPs/CSPs) | 170.19 |
| CMMC-05 | Write and maintain a System Security Plan; SSP cannot be put on a POA&M (CA.L2-3.12.4) | 170.21(a)(2)(iii)(C) |
| CMMC-06 | If using a cloud service provider for CUI, document the provider's Customer Responsibility Matrix in the SSP; on-premises infrastructure connecting to the CSP stays in scope | 170.16(c)(2)(iii); 170.17(c) |
| CMMC-07 | Encrypt CUI; non-FIPS-validated encryption for SC.L2-3.13.11 may sit on a POA&M (3-point item) but must be closed | 170.21(a)(2)(ii) |
| CMMC-08 | Close all POA&M items with a closeout assessment "within 180-days of the Conditional CMMC Status Date" | 170.21(b) |
| CMMC-09 | Submit self-assessment results (level, date, scope, CAGE codes, score e.g. "105 out of 110", POA&M usage) in SPRS | 170.15(a)(1)(i); 170.16(a)(1)(i) |
| CMMC-10 | Affirming Official submits an affirmation of continuing compliance in SPRS after every assessment and annually | 170.22(a), (b) |
| CMMC-11 | Provide CMMC UIDs for each contractor information system that will process, store or transmit FCI/CUI; report new UIDs during performance | 252.204-7021; 204.7503(b), (d) |
| CMMC-12 | Flow CMMC requirements down to subcontractors at all tiers | 170.23(a) |
| CMMC-13 | Report cyber incidents to DoD within 72 hours (DFARS 7012, which applies alongside CMMC) | 252.204-7012(a), (c) |
| CMMC-14 | Preserve images of affected systems and monitoring/packet capture data at least 90 days after incident report | 252.204-7012(e) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| 32 CFR 170 effective | December 16, 2024 | eCFR versioner, 170.3 date 2024-12-16 |
| 48 CFR CMMC rule effective / Phase 1 start | November 10, 2025 (Phase 1 "Begins on the effective date of the complementary 48 CFR part 204 CMMC Acquisition final rule") | 170.3(e)(1); eCFR versioner 204.7503 amendment date 2025-11-10 |
| Phase 2 (Level 2 C3PAO as condition of award) | "one calendar year following the start date of Phase 1" (i.e., November 10, 2026) | 170.3(e)(2) |
| Phase 3 (Level 2 C3PAO for all applicable, Level 3) | one calendar year after Phase 2 (November 10, 2027) | 170.3(e)(3) |
| Phase 4 full implementation | one calendar year after Phase 3; DFARS clause usage changes "On or after November 10, 2028" | 170.3(e)(4); 204.7504(a)(2) |
| Level 1 self-assessment cadence | annual, results in SPRS | 170.15(a)(1) |
| Level 2 self-assessment cadence | "every three years" | 170.16(a)(1) |
| Final Level 2 (C3PAO) / Level 3 validity | "Not older than 3 years" | 252.204-7021(a) "Current" |
| Conditional status validity | "Not older than 180 days" | 252.204-7021(a); 170.21(b) |
| Affirmation | "not older than 1 year" | 252.204-7021(a); 170.22 |
| POA&M eligibility threshold | score / total requirements "greater than or equal to 0.8" | 170.21(a)(2)(i), (a)(3)(i) |
| DoD incident reporting | "within 72 hours of discovery of any cyber incident" | 252.204-7012(a) |

## Assessment and certification
- Level 1 (Self): annual self-assessment and affirmation in SPRS; Final status only (170.15).
- Level 2 (Self): self-assessment every 3 years with annual affirmation; Conditional (with POA&M) or Final (170.16).
- Level 2 (C3PAO): certification assessment by an authorized or accredited C3PAO, results entered in the CMMC instantiation of eMASS; valid 3 years with annual affirmation (170.17).
- Level 3 (DIBCAC): assessment by DCMA DIBCAC on behalf of DoD after Final Level 2 (C3PAO) (170.18).
- The program office selects the required level per solicitation (170.3(d); 204.7503(a)).

## Notes
- Catalog rows: "CMMC 2.0 Level 1 ... self" correct. "CMMC 2.0 Level 2 ... certification" is incomplete: Level 2 can be Level 2 (Self) or Level 2 (C3PAO) depending on the solicitation (170.16, 170.17). Level 3 (DIBCAC, government-led) is missing from the catalog. The catalog does not mention that CMMC is now in force (32 CFR 170 effective Dec 16, 2024; DFARS clause 252.204-7021 effective Nov 10, 2025) and phased through November 2028.
- Level 2 is assessed against NIST SP 800-171 Rev. 2 (110 requirements) and SP 800-171A June 2018, not Rev. 3 (170.2(b)(9), (b)(10)).
- "CMMC 2.0" is a common program label; the regulation text calls it "the CMMC Program".
- Phase 2/3 calendar dates are derived arithmetically from 170.3(e) and the Nov 10, 2025 effective date; the November 10, 2028 date is stated in DFARS 204.7504(a)(2).
- DoD class deviation on which SP 800-171 revision applies under DFARS 252.204-7012 (reported as 2024-O0013, directing Rev. 2): still UNVERIFIED. In the follow-up pass (2026-11-06) www.acq.osd.mil was refused by the sandbox proxy (CONNECT 403) and acq.osd.mil returned 502, so the DPCAP class deviations page could not be read. For CMMC itself the Rev. 2 baseline is fixed by 32 CFR 170.2(b)(9), independent of the deviation.
- verification: partial because dodcio.defense.gov (CMMC program pages) returned "Access Denied" to both curl and headless Chromium, and federalregister.gov was not reachable; all facts above come from eCFR.
