---
id: bsi-c5
name: BSI C5
official_name: Cloud Computing Compliance Criteria Catalogue (C5), BSI - current edition C5:2026 (C5:2020 still applicable until the transition)
governing_body: Bundesamt für Sicherheit in der Informationstechnik (BSI, German Federal Office for Information Security); examinations performed by independent auditors (BSI is not involved in selecting auditors and does not check reports)
type: security
legal_status: voluntary-standard
region: Germany (used nationally, in Europe and globally)
industry: cloud
current_version: C5:2026 (final version published by end of March 2026); applies to type 1 specified dates or type 2 periods beginning on or after 1 June 2027; C5:2020 (January 2020) applies until then
superseded_by: C5:2020 is superseded by C5:2026 from 1 June 2027
official_sources:
  - title: BSI - C5 criteria catalogue (overview)
    url: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html
    accessed: 2026-11-06
  - title: BSI - C5:2026
    url: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/C5_2025/C5_2025_node.html
    accessed: 2026-11-06
  - title: BSI - C5:2020
    url: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/C5_AktuelleVersion/C5_AktuelleVersion_node.html
    accessed: 2026-11-06
  - title: C5:2026 Criteria Catalogue (PDF)
    url: https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2026/C5_2026.pdf?__blob=publicationFile
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
"The C5 (Cloud Computing Compliance Criteria Catalogue) criteria catalogue specifies minimum requirements for secure cloud computing and is primarily intended for professional cloud service providers, their auditors and customers." It sets "a baseline security level for cloud services" and is demonstrated through "a standardized examination and report" (BSI C5 page). It was first published by the BSI in 2016 and "completely revised in 2025/26". C5:2026 builds on C5:2020, the EUCS (level Substantial) work, CSA CCM v4, ISO/IEC 27001:2022 and the NIS2 directive (BSI C5:2026 page).

## Who it applies to
Professional cloud service providers that want to demonstrate C5 conformity, typically because German public-sector or regulated customers request a C5 report. Customers should "order the C5 report from the respective cloud service provider and analyse it. This procedure should be repeated yearly" (BSI C5 page).

## Engineering obligations
C5:2026 has 17 domains (C5:2026 PDF, chapter 5): OIS, SP, HR, AM, PS, OPS, IAM, CRY, COS, PI, DEV, SSO, SIM, BCM, COM, INQ, PSS. Selected criteria relevant to engineering:

| ID | Obligation | Official reference |
|---|---|---|
| AM-02 / AM-04 | Asset inventory, including a software asset inventory | C5:2026 5.4 |
| OPS-06 – OPS-09 | Data backup and recovery: policies, monitoring, regular testing, storage | C5:2026 5.6 |
| OPS-10 – OPS-17 | Logging and monitoring: policies, access, retention and deletion, SIEM, accountability, configuration, availability of monitoring software | C5:2026 5.6 |
| OPS-18, OPS-25 – OPS-29 | Vulnerability management: vulnerability scans, system hardening, patch management policies and implementation, externally sourced components | C5:2026 5.6 |
| OPS-22 | Penetration tests | C5:2026 5.6 |
| OPS-30 – OPS-31 | Separation of datasets (client separation) | C5:2026 5.6 |
| OPS-32 – OPS-35 | Confidential computing (incl. remote attestation) and container management | C5:2026 5.6 |
| IAM-02 – IAM-09 | Identity lifecycle, access reviews, privileged access, access to customer data, authentication mechanisms, confidentiality of authentication information | C5:2026 5.7 |
| CRY-01 – CRY-19 | Cryptography and key management: transport protection (CRY-04), encryption of sensitive data at rest (CRY-05), key generation, rotation, storage, compromise handling, external KMS, customer-managed keys | C5:2026 5.8 |
| COS-01 – COS-08 | Network security: separation of data traffic, administration networks, topology documentation, data transmission policies | C5:2026 5.9 |
| DEV-01 – DEV-15 | Secure development and change management: change testing, logging, version control, production approvals, environment separation, transparency about software components (DEV-13), third-party HW/SW | C5:2026 5.11 |
| SIM-01 – SIM-06 | Security incident management: response plans, processing, documentation and reporting, lessons learned | C5:2026 5.13 |
| BCM-01 – BCM-04 | Business continuity: BIA, plans, testing | C5:2026 5.14 |
| INQ-01 – INQ-02 | Legal assessment of government investigation requests; informing customers | C5:2026 5.16 |
| PSS-01 – PSS-12 | Product safety and security: customer guidance, vulnerability identification and disclosure to customers, error handling and logging, authentication, session management, authorisation, images for VMs and containers, region of data processing and storage (PSS-12) | C5:2026 5.17 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| C5:2026 mandatory application | "shall be applied in engagements with specified dates (type 1 reports) as of or after June 1st, 2027, or specified periods (type 2 reports) beginning on or after June 1st, 2027. Earlier adoption is permitted." | C5:2026 s. 3.5 |
| Mixed periods | Type 2 periods starting before and ending after 1 June 2027 use C5:2020 only; "no combinations" of versions | C5:2026 s. 3.5 |
| Type 2 period length | "minimum period should cover at least three months"; "maximum period should not cover more than twelve months" (exceptions allowed) | C5:2026 s. 3 (audit requirements) |
| Type 1 use | "Type 1 reports shall be mandated for initial engagements only. Subsequent engagements shall mandate a type 2 report." | C5:2026 s. 3 |
| Customer review cadence | Order and analyse the C5 report; "repeated yearly" | BSI C5 page |

## Assessment and certification
An attestation, not a certificate. The cloud provider mandates "certified public accountants or other auditors of their choice to conduct an examination". Auditors produce a detailed report "according to international standards" (BSI C5 page). Conformity assessments "shall always be provided in accordance with ISAE 3000 (Revised) or other national equivalents ... e.g. the German Audit Standard (PS) 860" (C5:2026 s. 3). Type 1 covers design suitability at a date; type 2 also covers operating effectiveness over a period. "BSI Germany is not involved in selecting auditors and does not check audit reports."

## Notes
- **Catalog check:** framework-catalog.md line 62 (C5, DE, cloud, attestation, "Cloud providers selling to German public sector") is consistent. It should state the current edition: **C5:2026** (published March 2026, mandatory from 1 June 2027), with C5:2020 still used until then.
- New in C5:2026: subcriteria structure aligned to EUCS; "additional sharpen" and "additional complement" criteria; new topics (container management, supply chain, post-quantum cryptography, confidential computing, client separation, technical sovereignty). It is published in PDF, Excel and, for the first time, machine-readable YAML. The cross-reference table to international standards is "scheduled for publication in the near future" (BSI C5:2026 page).
