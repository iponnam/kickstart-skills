---
id: nca-ecc
name: NCA ECC
official_name: Essential Cybersecurity Controls (ECC-2:2024)
governing_body: National Cybersecurity Authority (NCA), Kingdom of Saudi Arabia
type: security
legal_status: binding-regulation
region: Saudi Arabia (also binding on government agencies' affiliated companies and entities "inside and outside the kingdom")
industry: government agencies and their affiliated companies/entities, and private-sector entities owning, operating or hosting Critical National Infrastructures (CNIs); other entities "strongly encouraged"
current_version: ECC-2:2024 (NCA ECC page last updated 19/07/2026)
superseded_by: none (ECC-1:2018 is superseded by ECC-2:2024)
official_sources:
  - title: NCA - Essential Cybersecurity Controls (regulatory documents page)
    url: https://nca.gov.sa/en/regulatory-documents/controls-list/ecc/
    accessed: 2026-11-06
  - title: "Essential Cybersecurity Controls (ECC-2:2024), English PDF (56 pages, TLP: White)"
    url: https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf
    accessed: 2026-11-06
  - title: Guide to Essential Cybersecurity Controls (ECC) Implementation PDF (not fetched in this pass)
    url: https://cdn.nca.gov.sa/api/files/public/upload/94c6c5f5-4d70-4afd-a440-64369aa667e2_Guide-to-Essential-Cybersecurity-Controls-(ECC)-Implementation-en.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
NCA's national baseline of "minimum cybersecurity requirements" for national entities, first issued as ECC-1:2018 and updated as ECC-2:2024. ECC-2:2024 consists of "4 Cybersecurity Main Domains", "28 Cybersecurity Subdomains", "108 Cybersecurity Main Controls" and "92 Cybersecurity Subcontrols", linked to national and international legislative and regulatory requirements. The disclaimer states the controls are governed by Saudi law and that the Arabic text prevails.

## Who it applies to
- "These Controls are applicable to government agencies in the Kingdom of Saudi Arabia (including ministries, authorities, establishments and others) and their affiliated companies and entities (inside and outside the kingdom), as well as all private sector entities owning, operating, or hosting Critical National Infrastructures (CNIs)" (Scope of Work).
- "The NCA strongly encourages all other entities in the Kingdom to leverage these Controls" (Scope of Work).
- Statement of Applicability: "Each entity shall comply with all controls applicable thereto"; e.g. subdomain 4-2 (Cloud Computing and Hosting) is binding on entities "currently using or planning to use cloud computing and hosting services".
- Legal basis: "Article 10(3) of the NCA's Statute and High Order No. 57231, dated 10/11/1439H." (Implementation and Compliance).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| 1-2-1 | Cybersecurity department independent from the IT and Communications department | ECC 1-2-1 |
| 1-2-2 | Cybersecurity positions filled by "full-time and qualified Saudi cybersecurity professionals" | ECC 1-2-2 |
| 1-6-3 | In IT projects and software development: secure coding standards, trusted/licensed sources for tools and libraries, secure integration between applications, review secure configuration/hardening and update packages before release | ECC 1.6.3.1-1.6.3.5 |
| 1-8-2 | Independent review and audit of ECC implementation by parties other than the cybersecurity department, per GAAS | ECC 1-8-2 |
| 2-2-3 | MFA for remote access and privileged accounts (factors chosen by impact assessment); least privilege, need-to-know, segregation of duties; privileged access management; periodic access reviews | ECC 2.2.3.2-2.2.3.5 |
| 2-3-3 | Malware protection, restricted external storage media, patch management, centralized clock synchronization with a trusted source | ECC 2.3.3.1-2.3.3.4 |
| 2-4-3 | Email protection: phishing/spam filtering, MFA "for remote and webmail access", email archiving and backup, APT protection | ECC 2.4.3.1-2.4.3.4 |
| 2-5-3 | Network segmentation; isolate production from test/development; secure browsing; wireless security; restrict services/ports; IPS; DNS security | ECC 2.5.3.1-2.5.3.8 |
| 2-6-3 | Mobile devices: separate and encrypt entity data on mobile devices and BYODs | ECC 2.6.3.1 |
| 2-7-2 | Protect data and information "based on its classification level" | ECC 2-7-2 |
| 2-8-3 | Approved cryptographic standards; key lifecycle management; "Encryption of data in-transit and at-rest, as per their classification" | ECC 2.8.3.1-2.8.3.3 |
| 2-9-3 | Backups covering critical assets; periodic testing of backup recovery | ECC 2.9.3.1-2.9.3.3 |
| 2-10-3 | Periodic vulnerability assessment, severity classification, risk-based remediation, patch management, subscription to trusted threat sources | ECC 2.10.3.1-2.10.3.5 |
| 2-11-3 | Penetration tests "periodically", scope covering all internet-facing services and components (websites, web apps, mobile apps, email, remote access) | ECC 2.11.3.1-2.11.3.2 |
| 2-12-3 | Event logs for critical assets, privileged accounts and remote access; SIEM; continuous monitoring; retain logs at least 12 months | ECC 2.12.3.1-2.12.3.5 |
| 2-13-3 | Incident response plans and escalation, incident classification, "Reporting cybersecurity incidents to the NCA", sharing incident notifications, threat intelligence and indicators with NCA | ECC 2.13.3.1-2.13.3.5 |
| 2-14-3 | Physical access control to critical areas, CCTV logs and their protection, secure destruction/re-use of media | ECC 2.14.3.1-2.14.3.4 |
| 2-15-3 | Web applications: WAF, multi-tier architecture, secure usage policy, user authentication with suitable factors | ECC 2.15.3.1-2.15.3.5 |
| 3-1-3 | Cybersecurity in BCM: continuity of security systems, incident response plans affecting continuity, disaster recovery plans | ECC 3.1.3.1-3.1.3.3 |
| 4-1-3 | Third parties: risk assessment before contracting; managed security service centres using remote access "shall be fully located in the Kingdom of Saudi Arabia" | ECC 4.1.3.1-4.1.3.2 |
| 4-2-3 | Cloud and hosting: providers protect entity data per classification and return it in usable format at end of service; separate the entity's environment (especially virtual servers) | ECC 4.2.3.1-4.2.3.2 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Structure | "4 Cybersecurity Main Domains", "28 Cybersecurity Subdomains", "108 Cybersecurity Main Controls", "92 Cybersecurity Subcontrols" | ECC introduction |
| Cybersecurity event log retention | "shall be at least 12 months" | ECC 2.12.3.5 |
| Penetration testing cadence | "periodically" (no fixed interval in ECC text) | ECC 2.11.3.2 |
| Incident reporting to NCA | required ("Reporting cybersecurity incidents to the NCA"); no hour-based deadline stated in the ECC document | ECC 2.13.3.3 |

## Assessment and certification
"The NCA shall evaluate the entities' compliance with the ECC through multiple means, such as self-assessment by the entities, periodic reports of the compliance tool, and/or field auditing visits" (Implementation and Compliance). NCA will issue an "ECC-2:2024 Assessment and Compliance Tool". Entities must also have their implementation independently reviewed and audited internally (1-8-2). No third-party certificate.

## Notes
- Corrections to the first-pass draft (now confirmed from the PDF): ECC-2:2024 has 4 domains, not 5. The change log states the Industrial Control Systems domain (old domain 5) was deleted: "Controls in domain 5 moved to the OTCC". Data localization sub-control 4-2-3-3 ("Entity's information hosting and storage must be inside the Kingdom of Saudi Arabia") and data-protection control 2-7-3 were deleted and moved to the National Data Management Office (NDMO) at SDAIA; entities "must refer to the National Data Management Office regarding data localization".
- Catalog rows describe ECC as "law"; it is an NCA-issued binding control set (statutory basis: NCA Statute Art. 10(3) and High Order 57231), not a statute. The catalog gives no version; current is ECC-2:2024.
- The duplicate catalog row "Essential Cybersecurity Controls (ECC) | SA | any national" overstates scope: mandatory scope is government agencies (and affiliates) plus CNI owners/operators/hosts; others are only encouraged.
- Incident reporting timeframes to NCA are not in the ECC document; they would come from other NCA instruments (UNVERIFIED, not checked).
- The ECC Implementation Guide was not read in this pass.
