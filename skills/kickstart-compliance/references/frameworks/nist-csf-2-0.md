---
id: nist-csf-2-0
name: NIST CSF 2.0
official_name: The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)
governing_body: National Institute of Standards and Technology (NIST), U.S. Department of Commerce
type: security
legal_status: voluntary-standard
region: US origin; designed for use globally
industry: any
current_version: CSF 2.0, February 26, 2024
superseded_by: none
official_sources:
  - title: The NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (PDF)
    url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
    accessed: 2026-11-06
  - title: NIST Cybersecurity Framework home page
    url: https://www.nist.gov/cyberframework
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
CSF 2.0 "provides guidance to industry, government agencies, and other organizations to manage cybersecurity risks. It offers a taxonomy of high-level cybersecurity outcomes that can be used by any organization — regardless of its size, sector, or maturity" (Abstract). It "does not prescribe how outcomes should be achieved" (Abstract). Components are the CSF Core (Functions, Categories, Subcategories), Organizational Profiles and Tiers (Sec. 1).

## Who it applies to
Voluntary. "The CSF is designed to be used by organizations of all sizes and sectors, including industry, government, academia, and nonprofit organizations" (Sec. 1). The Core outcomes "apply to all ICT used by an organization, including information technology (IT), the Internet of Things (IoT), and operational technology (OT)" (Sec. 2). Contracts or regulators may make it binding by reference.

## Engineering obligations
The Core has 6 Functions (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER), 22 Categories (Table 1) and 106 Subcategories (Appendix A, counted). Rows below are engineering-relevant outcome statements from Appendix A.

| ID | Obligation | Official reference |
|---|---|---|
| GV.OC-03 | Understand and manage legal, regulatory and contractual cybersecurity requirements, including privacy | GV.OC-03 |
| GV.RR-02 | Establish, communicate and enforce cybersecurity roles, responsibilities and authorities | GV.RR-02 |
| GV.PO-01 | Establish a cybersecurity risk policy, communicate and enforce it | GV.PO-01 |
| GV.SC-04..07 | Know and prioritize suppliers by criticality; put security requirements in contracts; due diligence before engaging; monitor supplier risk | GV.SC-04 to GV.SC-07 |
| ID.AM-01 / ID.AM-02 | Maintain inventories of hardware, and of software, services and systems | ID.AM-01, ID.AM-02 |
| ID.AM-03 | Maintain representations of authorized network communication and data flows | ID.AM-03 |
| ID.AM-07 | Maintain inventories of data and metadata for designated data types | ID.AM-07 |
| ID.RA-01 | Identify, validate and record vulnerabilities in assets | ID.RA-01 |
| ID.IM-02 | Identify improvements from security tests and exercises | ID.IM-02 |
| PR.AA-01 / PR.AA-03 | Manage identities and credentials; authenticate users, services and hardware | PR.AA-01, PR.AA-03 |
| PR.AA-05 | Define, manage, enforce and review access permissions with least privilege and separation of duties | PR.AA-05 |
| PR.DS-01 / 02 / 10 | Protect confidentiality, integrity and availability of data at rest, in transit and in use | PR.DS-01, PR.DS-02, PR.DS-10 |
| PR.DS-11 | Create, protect, maintain and test backups | PR.DS-11 |
| PR.PS-01 | Establish and apply configuration management practices | PR.PS-01 |
| PR.PS-02 | Maintain, replace and remove software commensurate with risk (patching) | PR.PS-02 |
| PR.PS-04 | Generate log records and make them available for continuous monitoring | PR.PS-04 |
| PR.PS-05 | Prevent installation and execution of unauthorized software | PR.PS-05 |
| PR.PS-06 | Integrate secure software development practices and monitor their performance | PR.PS-06 |
| PR.IR-01 / PR.IR-03 | Protect networks from unauthorized logical access; implement resilience mechanisms | PR.IR-01, PR.IR-03 |
| DE.CM-01 / 03 / 09 | Monitor networks, personnel activity/technology usage, and hardware/software/runtime environments | DE.CM-01, DE.CM-03, DE.CM-09 |
| DE.AE-02 / 03 / 08 | Analyse and correlate adverse events; declare incidents against defined criteria | DE.AE-02, DE.AE-03, DE.AE-08 |
| RS.MA-01..04 | Execute incident response plan; triage, categorize, prioritize and escalate incidents | RS.MA-01 to RS.MA-04 |
| RS.CO-02 | Notify internal and external stakeholders of incidents | RS.CO-02 |
| RC.RP-03 | Verify integrity of backups and restoration assets before use | RC.RP-03 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Publication date | "February 26, 2024" | Cover page |
| Functions | 6, including new GOVERN (GV) | Sec. 2; Table 1 |
| Categories | 22 | Table 1 |
| Subcategories | 106 | Appendix A (counted) |
| Tiers | Partial (Tier 1), Risk Informed (Tier 2), Repeatable (Tier 3), Adaptive (Tier 4) | Sec. 3.2 |

The CSF itself sets no notification windows, retention periods or penalties.

## Assessment and certification
No certification. Organizations self-assess using Current and Target Organizational Profiles and Tiers (Sec. 3). NIST supplies Informative References, Implementation Examples, Quick-Start Guides and the CSF 2.0 Reference Tool to support use.

## Notes
- Catalog row "NIST CSF 2.0 ... self ... preferred version" is correct.
- control-checklists.md "NIST CSF 2.0 additions" is consistent with the official text (Govern covers strategy, roles, policy, oversight and supply chain risk management). It could add that Govern also covers "Organizational Context" (GV.OC) and that the Core has 22 Categories / 106 Subcategories.
- Recent official updates listed on nist.gov/cyberframework (2026-11-06): CSF 2.0 Informative References Quick-Start Guide final; draft CSF 2.0 Community Profile for Federal Agency O-RAN; SP 800-221r1 ipd open for comment until December 7, 2026. No CSF 2.1 announced.
