---
id: coppa
name: COPPA Rule
official_name: Children's Online Privacy Protection Rule, 16 CFR Part 312 (implementing the Children's Online Privacy Protection Act of 1998, 15 U.S.C. 6501 et seq.)
governing_body: Federal Trade Commission (FTC); State attorneys general may also enforce under the Act
type: privacy
legal_status: binding-regulation
region: US (applies to operators collecting personal information from children in the US, including foreign operators directing services to US children; extraterritorial detail not re-verified)
industry: any with child-directed services or actual knowledge of child users
current_version: 16 CFR Part 312, 78 FR 4008 (Jan. 17, 2013) as amended at 90 FR 16977 (Apr. 22, 2025); amended text in effect in eCFR from 2025-06-23
superseded_by: none
official_sources:
  - title: 16 CFR Part 312 Children's Online Privacy Protection Rule (eCFR)
    url: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312
    accessed: 2026-11-06
  - title: eCFR version history, 16 CFR Part 312 (versions 2016-12-22 and 2025-06-23)
    url: https://www.ecfr.gov/api/versioner/v1/versions/title-16.json?part=312
    accessed: 2026-11-06
  - title: eCFR point-in-time text, 16 CFR 312.13 Severability (as of 2026-11-04)
    url: https://www.ecfr.gov/api/versioner/v1/full/2026-11-04/title-16.xml?section=312.13
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
Part 312 "implements the Children's Online Privacy Protection Act of 1998 (15 U.S.C. 6501, et seq.), which prohibits unfair or deceptive acts or practices in connection with the collection, use, and/or disclosure of personal information from and about children on the internet" (§312.1). It requires notice, verifiable parental consent, parental review and deletion, data security, and data retention limits. The 2025 amendments (90 FR 16977) added, among other things, separate consent for third-party disclosure, a written information security program, a written data retention policy, and expanded definitions (e.g., biometric identifiers).

## Who it applies to
Operators of websites or online services directed to children, and operators with actual knowledge that they collect personal information from a child (§312.3; §312.2 definitions). "Child means an individual under the age of 13" (§312.2). A mixed audience service "shall not be deemed directed to children with regard to any visitor not identified as under 13" (§312.2, definition of website or online service directed to children, para. (3)). Personal information includes persistent identifiers "that can be used to recognize a user over time and across different websites or online services" and biometric identifiers (§312.2).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| 312.4 | Direct notice to parents and an online notice describing collection, use, disclosure, third-party categories and purposes, and the data retention policy | §312.4(b)-(d) |
| 312.5(a)(1) | "obtain verifiable parental consent before any collection, use, or disclosure of personal information from children", including for material changes | §312.5(a)(1) |
| 312.5(a)(2) | Let parents consent to collection/use without consenting to third-party disclosure (unless integral to the service); separate consent for disclosure | §312.5(a)(2) |
| 312.5(b) | Use a VPC method "reasonably calculated, in light of available technology" to ensure the consenting person is the parent | §312.5(b)(1)-(2) |
| 312.5(c)(7) | Persistent identifier used solely for support for internal operations may be collected without consent; notice must state the internal operations and how the identifier is not used to contact a specific individual | §312.5(c)(7); §312.4(d)(3) |
| 312.6 | Parent review: describe data categories, let parent refuse further use and direct deletion, provide a means to review data after verifying the requester is the parent | §312.6(a)(1)-(3) |
| 312.7 | Do not condition participation on collecting more personal information than reasonably necessary | §312.7 |
| 312.8(a) | Reasonable procedures to protect confidentiality, security and integrity of children's personal information | §312.8(a) |
| 312.8(b) | Written information security program: designate coordinator; at least annual risk assessment; safeguards; regular testing and monitoring; at least annual program evaluation | §312.8(b)(1)-(5) |
| 312.8(c) | Before sharing with service providers or third parties, verify capability and obtain written assurances | §312.8(c) |
| 312.10 | Retain only as long as reasonably necessary; delete securely; "may not be retained indefinitely"; written data retention policy with deletion timeframe, published in the notice | §312.10 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Age threshold | "Child means an individual under the age of 13" | §312.2 |
| Risk assessment | "at least annually" | §312.8(b)(2) |
| Security program evaluation | "At least annually" | §312.8(b)(5) |
| Retention | "only as long as is reasonably necessary"; "may not be retained indefinitely" | §312.10 |
| Safe harbor program annual report | "By October 22, 2025, and annually thereafter" | §312.11(d)(1) |
| Safe harbor public list of subject operators | "No later than July 21, 2025" | §312.11(d)(4) |
| Amended rule in force | eCFR version date 2025-06-23 | eCFR versioner |
| Violations | treated as violation of an FTC trade regulation rule (civil penalties under FTC Act) | §312.9 |

## Assessment and certification
No certification. Operators may join an FTC-approved safe harbor program (§312.11), which must include "an effective, mandatory mechanism for the independent assessment of subject operators' compliance". The FTC enforces (§312.9).

## Notes
- control-checklists.md COPPA row is broadly right. Corrections/additions from the 2025 amendments: separate verifiable parental consent for disclosure to third parties (§312.5(a)(2)); written information security program with annual risk assessment (§312.8(b)); written data retention policy published in the notice and no indefinite retention (§312.10). "No behavioural advertising" is not stated as such in Part 312; the rule instead requires consent for disclosures and limits the internal-operations exception for persistent identifiers. Rephrase to "no targeted advertising without verifiable parental consent".
- eCFR version history (re-checked 2026-11-06): Part 312 has only two versions, 2016-12-22 and 2025-06-23 (§§312.1-312.6, 312.8, 312.10-312.12 amended; §§312.7, 312.9 and 312.13 unchanged); no change after 2025-06-23. The CFR text contains no compliance-date provision.
- Compliance date: the amended rule's general compliance date (reported as April 22, 2026) is still UNVERIFIED (it is in the Federal Register preamble, not the CFR text). The eCFR shows the amended text effective 2025-06-23 but does not state the compliance date, and ftc.gov blocked automated requests ("The request resembles an abusive automated request"); federalregister.gov was not reachable.
- Civil penalty amounts are inflation-adjusted under 16 CFR 1.98; not re-verified here.
