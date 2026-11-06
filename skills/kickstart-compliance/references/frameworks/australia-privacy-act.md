---
id: australia-privacy-act
name: Australia Privacy Act 1988 (APPs, NDB scheme)
official_name: Privacy Act 1988 (Cth) (No. 119, 1988), including Schedule 1 Australian Privacy Principles and Part IIIC Notification of eligible data breaches; as amended incl. by the Privacy and Other Legislation Amendment Act 2024 (No. 128, 2024)
governing_body: Parliament of Australia; administered by the Attorney-General's Department; regulated by the Office of the Australian Information Commissioner (OAIC)
type: privacy
legal_status: law
region: Australia; extraterritorial to organisations with an "Australian link" (s.5B(1A))
industry: any (Australian Government agencies and organisations with annual turnover over AUD 3 million, plus some small businesses, e.g. health service providers)
current_version: Compilation No. 104, compilation date 04/06/2026 (Authorised Version C2026C00227, registered 17/06/2026)
superseded_by: none
official_sources:
  - title: Privacy Act 1988, Federal Register of Legislation (latest version, C2026C00227)
    url: https://www.legislation.gov.au/C2004A03712/latest/text
    accessed: 2026-11-06
  - title: Privacy Act 1988 compilation PDF (04/06/2026)
    url: https://www.legislation.gov.au/C2004A03712/2026-06-04/2026-06-04/text/original/pdf
    accessed: 2026-11-06
  - title: OAIC - The Privacy Act
    url: https://www.oaic.gov.au/privacy/privacy-legislation/the-privacy-act
    accessed: 2026-11-06
  - title: OAIC - About the Notifiable Data Breaches scheme
    url: https://www.oaic.gov.au/privacy/notifiable-data-breaches/about-the-notifiable-data-breaches-scheme
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
Australia's federal privacy law. OAIC: it was introduced "to promote and protect the privacy of individuals and to regulate how Australian Government agencies and organisations with an annual turnover of more than $3 million, and some other organisations, handle personal information". The 13 Australian Privacy Principles (Schedule 1) set obligations across the information lifecycle; the Notifiable Data Breaches (NDB) scheme (Part IIIC) requires notification of eligible data breaches to the OAIC and affected individuals.

## Who it applies to
- APP entities: agencies and organisations; "small business operators" are generally excluded.
- Small business: annual turnover for the previous financial year of "$3,000,000 or less" (s.6D(1)); but not a small business operator if it provides a health service and holds health information, or discloses/collects personal information for a benefit, service or advantage, among other cases (s.6D(4)).
- Extraterritorial: acts or practices outside Australia by an organisation or small business operator "that has an Australian link" (s.5B(1A)-(2)), e.g. a body corporate incorporated in Australia, or one carrying on business in Australia (s.5B(3), not fetched in detail).
- "child means an individual who has not reached 18 years" (s.6(1)).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| APP-1 | Open and transparent management; maintain a clearly expressed, up-to-date APP privacy policy with prescribed content | APP 1.3-1.4 |
| APP-2 | Allow individuals to deal anonymously or by pseudonym where practicable | APP 2.1 |
| APP-3 | Collect only personal information reasonably necessary; sensitive information only with consent (or exception) | APP 3 |
| APP-5 | Notify individuals of collection matters | APP 5 |
| APP-6 | Use or disclose only for the primary purpose or permitted secondary purposes; written notice of certain uses/disclosures | APP 6 (incl. 6.5) |
| APP-7 | Direct marketing: provide a simple means to opt out | APP 7.2(c), 7.3(c) |
| APP-8 | Cross-border disclosure: take reasonable steps to ensure overseas recipients comply | APP 8 |
| APP-11.1 | Take reasonable steps to protect personal information "from misuse, interference and loss" and "from unauthorised access, modification or disclosure" | APP 11.1 |
| APP-11.2 | Destroy or de-identify personal information no longer needed (unless law requires retention) | APP 11.2 |
| APP-11.3 | Reasonable steps "include technical and organisational measures" | APP 11.3 (added by 2024 amendment) |
| APP-12 | Give access on request; organisations respond "within a reasonable period"; agencies "within 30 days" | APP 12.1, 12.4 |
| APP-13 | Correct personal information on request; no charge; same response timeframes | APP 13.5 |
| NDB-01 | On reasonable grounds to suspect an eligible data breach: "reasonable and expeditious assessment" and take all reasonable steps to complete it "within 30 days" | s.26WH(2) |
| NDB-02 | On reasonable grounds to believe an eligible data breach occurred: prepare a statement (identity/contact, description, kinds of information, recommended steps) and give it to the Commissioner "as soon as practicable" | s.26WK(2)-(3) |
| NDB-03 | Notify the statement contents to each affected individual (or those at risk), or publish it if notifying individuals is not practicable | s.26WL |
| NDB-04 | Incident runbook must apply the eligible data breach test (unauthorised access/disclosure/loss likely to result in serious harm, not remediated) | s.26WE; OAIC NDB page |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Breach assessment | "take all reasonable steps to ensure that the assessment is completed within 30 days after the entity becomes aware" | s.26WH(2)(b) |
| Breach notification to OAIC | "as soon as practicable after the entity becomes so aware" | s.26WK(2)(b) |
| Notification to individuals | as soon as practicable after preparing the statement (s.26WL(3), wording not quoted from source) | s.26WL |
| Access/correction response (organisations) | "within a reasonable period after the request is made" | APP 12.4, 13.5 |
| Access/correction response (agencies) | "within 30 days after the request is made" | APP 12.4, 13.5 |
| Small business threshold | "annual turnover for the previous financial year is $3,000,000 or less" | s.6D(1) |
| Child | "has not reached 18 years" | s.6(1) |
| Serious interference penalty (body corporate) | greater of "$50,000,000", 3 times the benefit, or "30% of the adjusted turnover" | s.13G(3) |
| Interference with privacy (non-serious) | "must not exceed 2,000 penalty units" | s.13H(3) |
| Infringement-notice civil penalties | APP 1.3, 1.4, 2.1, 6.5, 7.2(c)/7.3(c) and others | s.13K |

## Assessment and certification
No certification. OAIC handles complaints, conducts assessments and investigations, accepts enforceable undertakings, issues infringement and compliance notices (added 2024), and seeks civil penalties in the Federal Court (Part IV, s.13G-13K, s.80U).

## Notes
- Catalog row "Personal information in Australia above turnover threshold or health data" is correct; add the 18-year definition of child and extraterritorial reach via "Australian link".
- 2024 amendments (Privacy and Other Legislation Amendment Act 2024, No. 128, 2024) are present in the compilation: APP 11.3 technical and organisational measures, the tiered civil penalties (s.13G serious, s.13H, s.13K infringement notices), the Children's Online Privacy Code requirement (s.26GC), eligible data breach declarations (Part IIIC Division 5, s.26X), and a statutory tort for serious invasions of privacy (Schedule 2).
- UNVERIFIED: APP 1.7-1.9 automated decision-making transparency obligations (announced to commence in December 2026) do not appear in Compilation No. 104 and were not verified.
- UNVERIFIED: the exact wording of s.26WL(3) timing for individual notification was not captured.
- The OAIC page states notification is required "when a data breach is likely to result in serious harm".
