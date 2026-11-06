---
id: pdpa-sg
name: PDPA Singapore
official_name: Personal Data Protection Act 2012 (2020 Revised Edition, as amended by the Personal Data Protection (Amendment) Act 2020, Act 40 of 2020); Personal Data Protection (Notification of Data Breaches) Regulations 2021
governing_body: Personal Data Protection Commission (PDPC), Singapore; statute published by the Attorney-General's Chambers (Singapore Statutes Online)
type: privacy
legal_status: law
region: Singapore
industry: any (private-sector organisations; public agencies excluded)
current_version: PDPA 2012 as amended by Act 40 of 2020 (breach notification from 1 February 2021; higher penalty cap from 1 October 2022); SSO "Last updated 4 Nov 2026"
superseded_by: none
official_sources:
  - title: Personal Data Protection Act 2012 (Singapore Statutes Online, whole document)
    url: https://sso.agc.gov.sg/Act/PDPA2012?WholeDoc=1
    accessed: 2026-11-06
  - title: PDPA section 11 (Compliance with Act)
    url: https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=pr11-
    accessed: 2026-11-06
  - title: PDPA section 48J (Financial penalties)
    url: https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=pr48J-
    accessed: 2026-11-06
  - title: Personal Data Protection (Notification of Data Breaches) Regulations 2021
    url: https://sso.agc.gov.sg/SL/PDPA2012-S64-2021?WholeDoc=1
    accessed: 2026-11-06
  - title: PDPC - Data Protection Obligations
    url: https://www.pdpc.gov.sg/overview-of-pdpa/the-legislation/personal-data-protection-act/data-protection-obligations
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
Singapore's general data protection law. Its purpose is to govern "the collection, use and disclosure of personal data by organisations in a manner that recognises both the right of individuals to protect their personal data and the need of organisations to collect, use or disclose personal data for purposes that a reasonable person would consider appropriate" (s.3). PDPC groups the duties into 11 obligations: accountability, notification, consent, purpose limitation, accuracy, protection, retention limitation, transfer limitation, access and correction, data breach notification, and data portability (not yet in force, marked * on PDPC's page).

## Who it applies to
- Organisations collecting, using or disclosing personal data. Parts 3-6B do not impose obligations on individuals acting in a personal/domestic capacity, employees acting in the course of employment, or public agencies (s.4(1)).
- Data intermediaries processing under a written contract are subject only to ss.24 (protection), 25 (retention), 26C(3)(a) (breach notice to the organisation) and 26E (s.4(2)); the organisation remains responsible for data processed on its behalf (s.4(3)).
- Business contact information is generally excluded (s.4(5)).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| PDPA-01 | Designate one or more individuals (DPO) responsible for compliance; publish business contact information of at least one | s.11(3), (5) |
| PDPA-02 | Collect, use or disclose personal data only with consent (or as permitted) | s.13 |
| PDPA-03 | Purpose limitation: only for purposes a reasonable person would consider appropriate and that have been notified | s.18 |
| PDPA-04 | Access: on request provide personal data and how it was used or disclosed "within a year before the date of the request", "as soon as reasonably possible" | s.21(1) |
| PDPA-05 | Correction of errors or omissions on request | s.22 |
| PDPA-06 | Preserve copies of personal data where access requests are refused (prescribed period) | s.22A |
| PDPA-07 | "Reasonable security arrangements" against unauthorised access, collection, use, disclosure, copying, modification or disposal, and loss of storage media | s.24 |
| PDPA-08 | Cease retention or anonymise as soon as purpose is no longer served and retention is not needed for legal or business purposes | s.25 |
| PDPA-09 | Cross-border transfers only per prescribed requirements ensuring comparable protection | s.26 |
| PDPA-10 | On reason to believe a breach occurred, assess "in a reasonable and expeditious manner" whether it is notifiable | s.26C(2) |
| PDPA-11 | Data intermediaries notify the organisation "without undue delay" | s.26C(3)(a) |
| PDPA-12 | Notify PDPC of a notifiable breach within 3 calendar days of the assessment, with prescribed content | s.26D(1), (3); Regs reg 5 |
| PDPA-13 | Notify each affected individual for significant-harm breaches, on or after notifying PDPC, with prescribed content | s.26D(2); Regs reg 6 |
| PDPA-14 | Treat breaches of prescribed data classes (e.g. card numbers, bank account numbers, income, net worth, private keys, child/vulnerable-person identifiers, specified health information) as significant harm | s.26B(2); Regs reg 3 and Schedule |
| PDPA-15 | Treat breaches affecting 500 or more individuals as significant scale | s.26B(3); Regs reg 4 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Breach notification to PDPC | "as soon as is practicable, but in any case no later than 3 calendar days after the day the organisation makes that assessment" | s.26D(1) |
| Breach assessment | "in a reasonable and expeditious manner" | s.26C(2) |
| Notification to individuals | "on or after notifying the Commission", "in any manner that is reasonable in the circumstances" | s.26D(2) |
| Significant scale threshold | "the prescribed number of affected individuals is 500" | Regs reg 4 |
| Breach regime start | data breaches "on or after 1 February 2021" | s.26C(1); Regs reg 1 |
| Access request response | "as soon as reasonably possible" | s.21(1) |
| Penalty cap (organisations) | "10% of the annual turnover in Singapore" where turnover exceeds $10 million; otherwise "$1 million" | s.48J(3) |
| Penalty cap (individuals, Part 9 / s.48B) | "$200,000" | s.48J(4)-(4A) |

## Assessment and certification
No mandatory certification. PDPC investigates and may issue directions and financial penalties (ss.48I-48J) or accept voluntary undertakings (s.48L). Optional certification (Data Protection Trustmark) is run under PDPC/IMDA; not reviewed here.

## Notes
- Catalog/checklist "breach notification to PDPC within 3 days of assessment" is correct; make it "3 calendar days after the day the organisation makes that assessment", and add that intermediaries must notify the organisation without undue delay and that 500+ individuals is significant scale.
- The term "DPO" is PDPC's; the Act requires designating "one or more individuals" and publishing business contact information (s.11(3), (5)).
- UNVERIFIED: PDPC's guidance that the assessment should be completed within 30 calendar days of awareness (Advisory Guidelines) was not fetched.
- Data portability obligation (Part 6B) is listed by PDPC with an asterisk (not yet in force); commencement not verified.
