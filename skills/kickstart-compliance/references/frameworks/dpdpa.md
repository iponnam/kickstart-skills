---
id: dpdpa
name: DPDPA 2023 + DPDP Rules 2025
official_name: The Digital Personal Data Protection Act, 2023 (No. 22 of 2023) and the Digital Personal Data Protection Rules, 2025 (G.S.R. 846(E), 13 November 2025)
governing_body: Ministry of Electronics and Information Technology (MeitY), Government of India; enforced by the Data Protection Board of India
type: privacy
legal_status: law
region: India; extraterritorial for processing outside India "in connection with any activity related to offering of goods or services to Data Principals within the territory of India" (s.3(b))
industry: any
current_version: Act No. 22 of 2023 (Gazette 11 Aug 2023); Rules G.S.R. 846(E) dated 13 Nov 2025, phased commencement (see Deadlines)
superseded_by: none
official_sources:
  - title: The Digital Personal Data Protection Act, 2023 (Gazette of India Extraordinary, Part II Sec. 1)
    url: https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
    accessed: 2026-11-06
  - title: Digital Personal Data Protection Rules, 2025, G.S.R. 846(E) (Gazette of India Extraordinary, Part II Sec. 3(i))
    url: https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf
    accessed: 2026-11-06
  - title: MeitY - Filling up the post of Chairman & Members in the Data Protection Board of India (advertisement, uploaded May 2026)
    url: https://www.meity.gov.in/static/uploads/2026/05/53b1bcf01cab9a0adde463e73fbc3417.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
India's horizontal data protection law for digital personal data. The Act sets duties for Data Fiduciaries (controllers), rights for Data Principals, extra duties for children's data and for Significant Data Fiduciaries, and creates the Data Protection Board of India with power to impose penalties under the Schedule. The 2025 Rules prescribe the notice, security, breach intimation, retention, parental consent, Consent Manager and SDF details, and bring them into force in phases.

## Who it applies to
- Processing of digital personal data in India, whether collected digitally or digitised later (s.3(a)); and processing outside India connected with offering goods or services to Data Principals in India (s.3(b)).
- Not applicable to personal/domestic processing or to data made publicly available by the Data Principal or under a legal obligation (s.3(c)).
- "Child" means "an individual who has not completed the age of eighteen years" (s.2(f)).
- Significant Data Fiduciaries: notified by the Central Government on factors including "volume and sensitivity of personal data processed" and risk to rights, sovereignty, electoral democracy, security of the State and public order (s.10(1)).
- Exemptions in s.17 (e.g., legal claims, processing of non-residents' data under a foreign contract by a person in India, specified research/State purposes).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| DPDPA-01 | Give a notice with or before the consent request, standalone and understandable, itemising data and purposes and how to withdraw consent, exercise rights and complain to the Board; available "in English or any language specified in the Eighth Schedule to the Constitution" | Act s.5; Rules r.3 |
| DPDPA-02 | Consent must be free, specific, informed, unconditional, unambiguous, by clear affirmative action; withdrawal must be as easy as giving it, and processing stops within a reasonable time after withdrawal | Act s.6(1), 6(4), 6(6) |
| DPDPA-03 | Support consent given/managed/withdrawn through a registered Consent Manager (interoperable platform; Consent Manager keeps records of consents and sharing) | Act s.6(7)-(9); Rules r.4, First Schedule Parts A-B |
| DPDPA-04 | Reasonable security safeguards "at the minimum": encryption, obfuscation, masking or virtual tokens; access control on computer resources; logs, monitoring and review to detect unauthorised access; backups for continued processing; contractual safeguards with Data Processors | Act s.8(5); Rules r.6(1)(a)-(g) |
| DPDPA-05 | Retain logs and personal data needed to detect/investigate unauthorised access "for a period of one year" unless another law requires otherwise | Rules r.6(1)(e) |
| DPDPA-06 | Breach intimation to each affected Data Principal "without delay", via user account or registered contact, covering nature, consequences, mitigation, safety steps and a contact | Act s.8(6); Rules r.7(1) |
| DPDPA-07 | Breach intimation to the Board: description "without delay"; then "within seventy-two hours of becoming aware of the breach" detailed facts, causes, mitigation, findings on the person who caused it, remediation and report on Data Principal intimations | Act s.8(6); Rules r.7(2) |
| DPDPA-08 | Erase personal data on consent withdrawal or when purpose no longer served, and make Data Processors erase it | Act s.8(7) |
| DPDPA-09 | For Third Schedule classes (large e-commerce, online gaming, social media intermediaries) erase after the prescribed inactivity period, and warn the Data Principal "at least forty-eight hours before" erasure | Act s.8(8); Rules r.8(1)-(2), Third Schedule |
| DPDPA-10 | Retain personal data, "associated traffic data and other logs of the processing for a minimum period of one year" from the date of processing for Seventh Schedule purposes, including where the user deletes the account; then erase | Rules r.8(3) |
| DPDPA-11 | Publish business contact information of the DPO (if applicable) or a person who answers questions about processing, on website/app and in every rights-request response | Act s.8(9); Rules r.9 |
| DPDPA-12 | Grievance redressal mechanism, and publish the means and identifiers needed to exercise rights | Act s.8(10), s.13; Rules r.14(1)-(3) |
| DPDPA-13 | Data Principal rights: access to a summary of data and processing (s.11), correction, completion, updating and erasure (s.12), grievance redressal (s.13), nomination (s.14; r.14(4)) | Act ss.11-14 |
| DPDPA-14 | Children: obtain "verifiable consent of the parent" before processing a child's data; check the parent is an identifiable adult using reliable identity/age details held or a virtual token from an authorised entity (incl. DigiLocker) | Act s.9(1); Rules r.10 |
| DPDPA-15 | No processing likely to cause detrimental effect on a child's well-being; no "tracking or behavioural monitoring of children or targeted advertising directed at children" (subject to Fourth Schedule exemptions) | Act s.9(2)-(4); Rules r.12 |
| DPDPA-16 | Verifiable consent from lawful guardian of a person with disability, verifying court/authority appointment | Act s.9(1); Rules r.11 |
| DPDPA-17 | Significant Data Fiduciary: appoint a DPO "based in India" responsible to the board; appoint an independent data auditor; periodic DPIA | Act s.10(2) |
| DPDPA-18 | SDF: DPIA and audit "once in every period of twelve months", report significant observations to the Board; due diligence that algorithmic software does not pose risks to Data Principals' rights; localisation of personal data and traffic data specified by the Government | Rules r.13(1)-(4) |
| DPDPA-19 | Ensure accuracy, completeness and consistency of data used for decisions affecting the Data Principal or disclosed to another Fiduciary | Act s.8(3) |
| DPDPA-20 | Cross-border transfers allowed except to countries restricted by Central Government notification | Act s.16(1) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Breach intimation to the Board (initial) | "without delay" | Rules r.7(2)(a) |
| Breach detailed report to the Board | "within seventy-two hours of becoming aware of the breach, or within such longer period as the Board may allow on a request made in writing" | Rules r.7(2)(b) |
| Notification to individuals | "without delay" | Rules r.7(1) |
| Grievance / rights response | "within a reasonable period not exceeding ninety days" (to be published by each Fiduciary) | Rules r.14(3) |
| Security log retention | "for a period of one year" | Rules r.6(1)(e) |
| Processing log/traffic data retention | "minimum period of one year from the date of such processing" | Rules r.8(3) |
| Erasure warning | "At least forty-eight hours before" erasure | Rules r.8(2) |
| Inactivity erasure (e-commerce >= 2 crore users, online gaming >= 50 lakh users, social media >= 2 crore users in India) | "Three years from the date on which the Data Principal last approached" (or Rules commencement, whichever is latest) | Rules Third Schedule |
| Child | "not completed the age of eighteen years" | Act s.2(f) |
| SDF DPIA and audit | "once in every period of twelve months" | Rules r.13(1) |
| Rules commencement | r.1, 2, 17-21 on publication (gazette dated 13 Nov 2025); r.4 (Consent Managers) "one year after"; r.3, 5-16, 22, 23 "eighteen months after" | Rules r.1(2)-(4) |
| Penalty: security safeguards failure | "May extend to two hundred and fifty crore rupees" | Act Schedule item 1 |
| Penalty: breach notice failure | "May extend to two hundred crore rupees" | Schedule item 2 |
| Penalty: children obligations | "May extend to two hundred crore rupees" | Schedule item 3 |
| Penalty: SDF obligations | "May extend to one hundred and fifty crore rupees" | Schedule item 4 |
| Penalty: Data Principal duties (s.15) | "May extend to ten thousand rupees" | Schedule item 5 |
| Penalty: any other provision | "May extend to fifty crore rupees" | Schedule item 7 |
| Consent Manager net worth | "not less than two crore rupees" | Rules First Schedule Part A |

## Assessment and certification
No certification. The Data Protection Board of India inquires into breaches (on intimation, complaint or reference) and imposes penalties (Act ss.27-28, 33); appeals go to the Appellate Tribunal (TDSAT) (s.29). SDFs must commission an annual DPIA and independent data audit and furnish significant observations to the Board (Rules r.13). Consent Managers register with the Board and maintain audit mechanisms (Rules r.4, First Schedule).

## Notes
- Previous catalog: "S–M" effort and "law" are fine. The control-checklist says breach notice "as prescribed to the Board" and rights "as prescribed": now prescribed. Update to: Board "without delay" plus detailed report within 72 hours; individuals "without delay"; grievances within a published period not exceeding 90 days.
- The checklist row "Consent manager interoperability (when rules in force)": Rule 4 commences one year after publication (about November 2026); most other obligations (r.3, 5-16) commence eighteen months after publication (about May 2027). Engineers should treat 2027 as the compliance date for notices, security, breach intimation, retention, children and SDF rules.
- Checklist "DPO in India" for SDF is correct (s.10(2)(a)(ii) "be based in India"). Add the Rules' one-year log retention (r.6(1)(e), r.8(3)), which the catalog omits.
- UNVERIFIED: the separate Act commencement notification (S.O. under s.1(2) bringing specific Act sections into force alongside the Rules) could not be found. Second pass (2026-11-06): meity.gov.in HTML pages still return 403 (Akamai) in Playwright as well as curl; only /static/uploads/ PDFs load, and a search restricted to meity.gov.in, egazette.gov.in and pib.gov.in did not surface the S.O.; static.pib.gov.in did not respond. The Rules' commencement clause is verified; which Act sections are in force on which date is not.
- Verified (MeitY advertisement, May 2026): "The Government of India has established the Data Protection Board of India (DPBI) under Section 18"; the Board "consists of a Chairperson and four other Members" and is empowered to inquire into breaches, issue directions and impose penalties under the Act and the DPDP Rules 2025. This implies s.18 is in force, but the commencement date is not stated.
- UNVERIFIED: whether any 2026 amendment to the Rules has altered the phased timeline; not checked on an official source.
- Exact publication date: notification dated 13 November 2025; the gazette copy is digitally signed 14 November 2025. The 12/18-month clocks run from the gazette publication date.
