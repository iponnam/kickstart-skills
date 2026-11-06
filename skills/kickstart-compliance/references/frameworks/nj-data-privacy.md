---
id: nj-data-privacy
name: New Jersey Data Privacy Act
official_name: P.L.2023, c.266 (S332), "An Act concerning online services, consumers, and personal data and supplementing Title 56 of the Revised Statutes", N.J.S.A. 56:8-166.4 et seq. (called the "New Jersey Data Privacy Law" (NJDPL) by the Division of Consumer Affairs)
governing_body: New Jersey Legislature; enforced exclusively by the Office of the Attorney General, Division of Consumer Affairs (rulemaking by the Director of the Division)
type: privacy
legal_status: law
region: US-NJ (controllers conducting business in NJ or targeting NJ residents)
industry: any
current_version: P.L.2023, c.266, approved January 16, 2024; effective January 15, 2025
superseded_by: none
official_sources:
  - title: P.L.2023, c.266 (S332 6R), chaptered law text (NJ Legislature)
    url: https://pub.njleg.gov/bills/2022/PL23/266_.HTM
    accessed: 2026-11-06
  - title: New Jersey Data Privacy Law FAQs (NJ Division of Consumer Affairs)
    url: https://www.njconsumeraffairs.gov/ocp/Pages/NJ-Data-Privacy-Law-FAQ.aspx
    accessed: 2026-11-06
  - title: NJ Division of Consumer Affairs, Adoptions & Rule Proposals
    url: https://www.njconsumeraffairs.gov/Pages/adoptions.aspx
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
The NJDPL "guarantees New Jersey consumers certain rights with regard to their personal data and imposes requirements on the individuals and businesses that process that data (which are called 'controllers')" (DCA FAQ). Consumers may confirm processing, access, correct, delete, obtain a portable copy, and opt out of targeted advertising, sale and certain profiling. Controllers must give privacy notices, minimise data, secure it, get consent for sensitive data, and conduct data protection assessments for heightened-risk processing.

## Who it applies to
Controllers "that conduct business in the State or produce products or services that are targeted to residents of the State, and that during a calendar year either: a. control or process the personal data of at least 100,000 consumers, excluding personal data processed solely for the purpose of completing a payment transaction; or b. control or process the personal data of at least 25,000 consumers and the controller derives revenue, or receives a discount on the price of any goods or services, from the sale of personal data" (§2, C.56:8-166.5). A consumer is a NJ resident acting in an individual or household context (DCA FAQ). Non-profits are not excluded (DCA FAQ). Processors must also comply (§12, C.56:8-166.15; §13, C.56:8-166.16).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| NJDPA-01 | Privacy notice describing categories, purposes, rights, how to exercise them, sale/targeted advertising disclosures | C.56:8-166.6 (§3) |
| NJDPA-02 | Rights request handling (confirm, access, correct, delete, portability) with verification; respond within 45 days | C.56:8-166.7 (§4); C.56:8-166.10 (§7) |
| NJDPA-03 | Appeal process; decide appeals within 45 days | C.56:8-166.7 (§4) |
| NJDPA-04 | Opt-out of targeted advertising, sale, and profiling for decisions with legal or similarly significant effects | C.56:8-166.10 (§7) |
| NJDPA-05 | Honour user-selected universal opt-out mechanisms (e.g., Global Privacy Control) for targeted advertising and sale | C.56:8-166.11(b)(1) (§8); DCA FAQ |
| NJDPA-06 | Authorized agent opt-outs where identity and authority are verified | C.56:8-166.11 (§8); DCA FAQ |
| NJDPA-07 | Data minimisation and purpose limitation; consent for secondary purposes | C.56:8-166.12(a)(1)-(2) (§9) |
| NJDPA-08 | "administrative, technical, and physical data security practices" protecting personal data "during both storage and use" | C.56:8-166.12(a)(3) (§9) |
| NJDPA-09 | Consent before processing sensitive data; COPPA-compliant processing for known children | C.56:8-166.12(a)(4) (§9) |
| NJDPA-10 | Consent revocation mechanism "at least as easy as" giving consent; stop processing within 15 days | C.56:8-166.12(a)(6) (§9) |
| NJDPA-11 | No targeted advertising, sale or significant-effect profiling without consent where the controller knows or wilfully disregards that the consumer is 13 to under 17 | C.56:8-166.12(a)(7) (§9) |
| NJDPA-12 | Data protection assessment before heightened-risk processing (targeted advertising, sale, sensitive data, risky profiling) of data acquired on or after the effective date; make available to the Division on request | C.56:8-166.12(a)(9), (b)-(d) (§9) |
| NJDPA-13 | Processor contracts and processor duties (instructions, confidentiality, deletion/return, assistance, subcontractor flow-down) | C.56:8-166.16 (§13) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Effective date | "take effect on the 365th day following the date of enactment"; approved January 16, 2024; DCA: "January 15, 2025" | §17; DCA FAQ |
| Applicability thresholds | "at least 100,000 consumers"; or "at least 25,000 consumers" plus revenue/discount from sale | §2 (C.56:8-166.5) |
| Data subject request response | "within 45 days of the controller's receipt of the request"; may extend "by 45 additional days where reasonably necessary" | §4 (C.56:8-166.7(a)) |
| Appeal decision | "Not later than 45 days after receipt of an appeal" | §4 |
| Consent revocation | stop processing "not later than 15 days after the receipt of such request" | §9 (C.56:8-166.12(a)(6)) |
| Universal opt-out mechanism | "Beginning not later than six months following the effective date"; DCA: "by July 15, 2025" | §8 (C.56:8-166.11(b)(1)); DCA FAQ |
| Teen protections | "at least 13 years of age but younger than 17 years of age" | §9 (C.56:8-166.12(a)(7)) |
| Cure period | until the first day of the 18th month after the effective date, Division gives notice and "30 days" to cure where possible | §14 (C.56:8-166.17(b)) |

## Assessment and certification
No certification. Data protection assessments are internal and must be produced to the Division on request (confidential). Enforcement: "The Office of the Attorney General shall have sole and exclusive authority to enforce"; no private right of action (§16). Violations are unlawful practices under the NJ Consumer Fraud Act, P.L.1960, c.39 (§14(a)).

## Notes
- Catalog row "New Jersey Data Privacy Law ... S ... New Jersey residents' data above thresholds" is correct; add thresholds (100,000 consumers, or 25,000 consumers plus sale revenue), effective January 15, 2025, UOOM by July 15, 2025, and teen (13-16) consent rule.
- Discrepancy inside official sources: the statute says "at least 13 years of age but younger than 17 years of age" (§9(a)(7)); the DCA FAQ paraphrases "between the ages of 13 and 16". Use the statute.
- Division of Consumer Affairs rules: the DCA FAQ (last modified 1/15/2025) says "Regulations will be forthcoming in 2025". Whether rules (reported as proposed N.J.A.C. 13:45L in 2025) have been adopted is UNVERIFIED: the DCA Adoptions & Rule Proposals pages loaded in a browser but showed no privacy rule entry, and the NJ Register was not reachable. Do not cite rule text until confirmed.
- The cure period end date (first day of the 18th month after January 15, 2025, i.e. around July 1, 2026) is derived arithmetically, not stated by the DCA.
