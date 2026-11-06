---
id: saudi-pdpl
name: Saudi PDPL
official_name: Personal Data Protection Law (Royal Decree No. M/19 dated 9/2/1443H, amended by Royal Decree No. M/148 dated 5/9/1444H) and its Implementing Regulation and Regulation on Personal Data Transfer outside the Kingdom
governing_body: Saudi Data and Artificial Intelligence Authority (SDAIA) as Competent Authority (without prejudice to Saudi Central Bank powers, Art. 30(1))
type: privacy
legal_status: law
region: Saudi Arabia; extraterritorial for processing of data of individuals residing in the Kingdom by any party outside the Kingdom (Art. 2(1))
industry: any
current_version: In force 14 September 2023; one-year grace period to 14 September 2024
superseded_by: none
official_sources:
  - title: Personal Data Protection Law (English translation, SDAIA)
    url: https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf
    accessed: 2026-11-06
  - title: Implementing Regulation of the PDPL and Regulation on Personal Data Transfer outside the Kingdom (SDAIA)
    url: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf
    accessed: 2026-11-06
  - title: Guide to the Saudi Personal Data Protection Law for controllers/processors (SDAIA)
    url: https://dgp.sdaia.gov.sa/wps/wcm/connect/f579bc32-fda8-47bd-bc6f-66b8cb77985c/ENG-Guide+to+the+saudi+PDP+law+for+controllersprocessors.pdf?MOD=AJPERES
    accessed: 2026-11-06
  - title: National Data Governance Platform - Knowledge Center (Arabic list of law, regulations, guides)
    url: https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
Saudi Arabia's general personal data protection law, with an Implementing Regulation and a separate Regulation on Personal Data Transfer outside the Kingdom, both issued by SDAIA. It sets controller duties (security, breach notification, impact assessment, records, DPO), data subject rights, cross-border transfer conditions and penalties.

## Who it applies to
Art. 2(1): "any Processing of Personal Data related to individuals that takes place in the Kingdom by any means, including the Processing of Personal Data related to individuals residing in the Kingdom by any means from any party outside the Kingdom", including data of the deceased in some cases. Art. 2(2) excludes personal or family use. Art. 30(1) sets SDAIA (the Competent Authority) as supervisor "without prejudice to ... the powers of the Saudi Central Bank".

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| PDPL-01 | Organisational, administrative and technical measures to protect personal data, including during transfer | Law Art. 19; IR Art. 23 |
| PDPL-02 | Comply with NCA controls/standards, or recognised cybersecurity standards if not bound by NCA | IR Art. 23(2) |
| PDPL-03 | Notify SDAIA of breaches within 72 hours with required content (description, categories, numbers, risks, measures, contact) | Law Art. 20(1); IR Art. 24(1)-(2) |
| PDPL-04 | Notify data subjects "without undue delay" in simple, clear language where harm is possible | Law Art. 20(2); IR Art. 24(5) |
| PDPL-05 | Act on data subject requests within 30 days (extendable by 30) and keep records of requests | IR Art. 3(1)(a),(d) |
| PDPL-06 | Consent handling, records of consent, withdrawal processed without undue delay | IR Arts. 11, 12 |
| PDPL-07 | Written impact assessment for sensitive data, data linking, large-scale monitoring, new technologies, automated decisions, high-risk products | Law Art. 22; IR Art. 25 |
| PDPL-08 | Written records of processing activities with minimum fields (incl. transfers outside KSA, retention period) | Law Art. 31; IR Art. 33 |
| PDPL-09 | Appoint DPO for large-scale public-entity processing, large-scale regular monitoring, or core sensitive-data processing | Law Art. 30(2); IR Art. 32 |
| PDPL-10 | Processor selection and written processor obligations; processor notifies controller without undue delay | IR Art. 17 |
| PDPL-11 | Data minimisation; destroy data when purpose achieved, subject to retention exceptions | Law Art. 18; IR Art. 19 |
| PDPL-12 | Anonymisation techniques evaluated for re-identification risk | IR Art. 9 |
| PDPL-13 | Health data: document all processing stages and responsible person | Law Art. 23; IR Art. 26 |
| PDPL-14 | Direct marketing: consent, opt-out mechanism, sender identity, stop immediately on withdrawal | IR Art. 29 |
| PDPL-15 | Cross-border transfers only under Art. 29 purposes and conditions (no prejudice to national security, adequate protection, minimum data); adequacy, Binding Common Rules, Standard Contractual Clauses | Law Art. 29; Transfer Regulation Arts. 2-7 |
| PDPL-16 | Transfer risk assessment for transfers under Transfer Regulation Arts. 5 and 6 and continuous/large-scale sensitive-data transfers | Transfer Regulation Art. 8 |
| PDPL-17 | Registration in the national register of controllers where required | Law Art. 30(4)(c); IR Art. 34 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Breach notification to regulator | "within a delay not exceeding (72) hours of becoming aware of the incident" | IR Art. 24(1) |
| Notification to individuals | "without undue delay" | IR Art. 24(5) |
| Data subject request response | "within a period not exceeding (30) days", extension up to "an additional (30) days" | IR Art. 3(1)(a) |
| Records of processing retention | "during the period of the Processing, in addition to five years" from completion | IR Art. 33(1) |
| Penalty, disclosure of sensitive data with intent to harm | "imprisonment for a period not exceeding (two years), or a fine not exceeding (three million) Riyals, or both" | Law Art. 35(1) |
| Penalty, other violations | "a warning or a fine not exceeding (five million) Riyals"; may be doubled for repeat | Law Art. 36(1) |
| Entry into force | "came into force on 14 September 2023" | SDAIA Guide |
| Grace period | "one-year grace" ... compliance "by 14 September 2024" | SDAIA Guide; Royal Decree M/19 s.3 |

## Assessment and certification
SDAIA supervises; may request documents and maintain a national register of controllers (Art. 30(4)). IR Arts. 35-36 cover accreditation bodies and auditing; SDAIA publishes rules for issuing accreditation certificates to controllers and processors (Knowledge Center). No mandatory certification.

## Notes
- Catalog row "Personal data of Saudi residents (listed under Others on scrut.io)" is incomplete: the law also covers all processing in the Kingdom, plus foreign processing of data of individuals residing in KSA.
- Law Art. 32 is marked "Repealed" in the amended text.
- English texts are SDAIA translations; Arabic versions on dgp.sdaia.gov.sa are authoritative.
