---
id: tisax
name: TISAX
official_name: Trusted Information Security Assessment Exchange (TISAX), based on the VDA Information Security Assessment (VDA ISA)
governing_body: ENX Association (governs TISAX, approves audit providers, maintains the TISAX ACAR criteria); VDA (publishes the VDA ISA catalogue, maintained by the ENX Working Group ISA)
type: sector
legal_status: contractual
region: Germany, EU, global automotive supply chain
industry: automotive
current_version: VDA ISA 6.0.3 (2024-04-25; basis for assessments starting after 2024-04-01); VDA ISA2027.1 published 2026-07-01 for assessments ordered in 2027; TISAX Participant Handbook 2.8 (2025-03-13)
superseded_by: VDA ISA2027 (for assessments ordered in 2027)
official_sources:
  - title: ENX Portal - TISAX
    url: https://portal.enx.com/en-US/TISAX/
    accessed: 2026-11-06
  - title: ENX Portal - Information Security Assessment (ISA)
    url: https://portal.enx.com/en-US/TISAX/ISA/
    accessed: 2026-11-06
  - title: ENX Portal - TISAX FAQs
    url: https://portal.enx.com/en-US/TISAX/faqs/
    accessed: 2026-11-06
  - title: ENX Portal - TISAX Downloads
    url: https://portal.enx.com/en-US/TISAX/downloads/
    accessed: 2026-11-06
  - title: TISAX Participant Handbook 2.8 (PDF, 2025-03-13)
    url: https://portal.enx.com/handbook/TISAX%20Participant%20Handbook.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
"TISAX was developed to create a standardized and scalable approach to information security in the automotive industry. It is based on the Information Security Assessment (ISA) catalogue which is maintained by the ENX Association and published by the VDA" (ENX TISAX page). Companies are assessed once by an ENX-approved audit provider and share the results with as many partners as they choose ("Assessed once, recognized by many").

## Who it applies to
Automotive manufacturers, suppliers and service providers whose business partners require TISAX labels, typically because they handle sensitive partner information, prototypes or personal data on behalf of an OEM. The participant registers one or more "scopes"; an assessment result fulfils a partner's requirement only if the scope covers all parts of the company that handle the partner's information (FAQ).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| TISAX-01 | Implement the VDA ISA information security criteria catalogue requirements for the selected objectives (ISA 6.0.3 now; ISA2027 for assessments ordered in 2027) | ENX ISA page; Downloads |
| TISAX-02 | Complete the self-assessment based on the ISA (required at all assessment levels) | Handbook 2.8 s. 5.2; Table 6 |
| TISAX-03 | Select assessment objectives: Info high / Info very high, Confidential / Strictly confidential, High / Very high availability, Proto parts, Proto vehicles, Test vehicles, Proto events, Data (GDPR Art. 28 processor), Special data (GDPR Art. 28 with Art. 9 data) | Handbook 2.8 Table 3 |
| TISAX-04 | Prototype protection objectives add the ISA prototype-protection catalogue (physical security, camouflage, test vehicle handling) | Handbook 2.8 s. 4 |
| TISAX-05 | Data protection objectives add the ISA data protection catalogue (GDPR Art. 28 processor obligations) | Handbook 2.8 Table 3 |
| TISAX-06 | Provide evidence to the audit provider (plausibility check at AL 2; thorough verification at AL 3) | Handbook 2.8 Table 6 |
| TISAX-07 | Resolve non-conformities through a corrective action plan and follow-up assessment | FAQ; Handbook 2.8 s. 5.4 |
| TISAX-08 | Define the assessment scope precisely; it determines what the label covers | FAQ (Registration) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Validity of assessment result | "Your assessment result is valid for three years." | Handbook 2.8 s. 3.4 |
| Temporary TISAX labels | Expire "nine months after the closing meeting of the initial assessment", or are valid until all non-conformities are resolved | FAQ; Handbook 2.8 |
| Assessment level by objective | Info high AL 2; Info very high AL 3; Confidential AL 2; Strictly confidential AL 3; High availability AL 2; Very high availability AL 3; Proto parts AL 3; Proto vehicles AL 3; Test vehicles AL 2; Proto events AL 2; Data AL 2 | Handbook 2.8 (table of objectives and levels) |
| Results visibility | Report sections A and B visible to the participant "within two weeks" after upload | FAQ |
| Current ISA catalogue | "ISA 6.0.3 ... basis of TISAX Assessments starting later than 2024-04-01" | ENX Downloads |
| Next ISA catalogue | "ISA2027.1 ... the basis of TISAX Assessments ordered in 2027" (published 2026-07-01; German version 2026-10-01) | ENX Downloads; ENX news |

## Assessment and certification
Assessments are performed by ENX-approved audit providers under the TISAX ACAR criteria. Results are recorded as TISAX labels in the TISAX report and exchanged through the ENX portal at participant-chosen sharing levels. Assessment levels (Handbook 2.8 Table 6):
- **AL 1:** self-assessment only. "Results of assessments in assessment level 1 have a low trust level and are thus not used in TISAX."
- **AL 2:** plausibility check of the self-assessment plus evidence and an interview, usually by web conference; on-site inspection at the participant's request. A "full remote assessment" variant ("AL 2.5") is formally evaluated as AL 2.
- **AL 3:** thorough verification, in-person interviews and on-site inspection.

## Notes
- **Catalog correction:** framework-catalog.md line 37 "TISAX v5.1" is wrong. The current catalogue is **VDA ISA 6.0.3** (basis for assessments starting after 2024-04-01). **VDA ISA2027 / ISA2027.1** (published 1 July 2026) is the basis for assessments ordered in 2027. The audit type "certification" is loose: TISAX issues assessment results and labels valid for 3 years, not an ISO-style certificate.
- **Internal inconsistency in official sources:** the FAQ says "There are currently 10 TISAX assessment objectives", while Handbook 2.8 Table 3 lists 12 (including Confidential, Strictly confidential, High availability and Very high availability). Treat the handbook as more detailed but confirm with ENX.
- enx.com was blocked by the proxy. portal.enx.com was reachable and is ENX's official portal.
- ENX also publishes "Fulfillment NIS2 through TISAX" (2025-06-29), an analysis of NIS2 coverage. It was not read.
