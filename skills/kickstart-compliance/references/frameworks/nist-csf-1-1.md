---
id: nist-csf-1-1
name: NIST CSF 1.1
official_name: Framework for Improving Critical Infrastructure Cybersecurity, Version 1.1 (NIST CSWP 6, also published as NIST.CSWP.04162018)
governing_body: National Institute of Standards and Technology (NIST), U.S. Department of Commerce
type: security
legal_status: voluntary-standard
region: US origin; used globally
industry: any (written for critical infrastructure)
current_version: Version 1.1, April 16, 2018
superseded_by: NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29), February 26, 2024
official_sources:
  - title: Framework for Improving Critical Infrastructure Cybersecurity, Version 1.1 (PDF)
    url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf
    accessed: 2026-11-06
  - title: CSRC publication page, CSWP 6 (Final) with planning note on CSF 2.0
    url: https://csrc.nist.gov/pubs/cswp/6/cybersecurity-framework-v11/final
    accessed: 2026-11-06
  - title: NIST Cybersecurity Framework home page
    url: https://www.nist.gov/cyberframework
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
CSF 1.1 is a voluntary risk-management framework that "consists of standards, guidelines, and best practices to manage cybersecurity-related risk" (CSRC abstract). It has "three parts: the Framework Core, the Implementation Tiers, and the Framework Profiles" (Sec. 1.1). Version 1.1 "refines, clarifies, and enhances Version 1.0, which was issued in February 2014" (Note to Readers). It is now a legacy version: the CSRC page carries a planning note dated 02/26/2024 that NIST released CSF 2.0.

## Who it applies to
Voluntary. Written for critical infrastructure owners and operators but usable by any organization. No legal applicability thresholds. Some contracts, sector regulators or older assessments may still reference 1.1.

## Engineering obligations
CSF 1.1 states outcomes, not mandates. The rows below are the outcome statements (Subcategories) most relevant to engineering teams, taken from Appendix A (Framework Core). The Core has 5 Functions (Identify, Protect, Detect, Respond, Recover), 23 Categories and 108 Subcategories (counted from Appendix A).

| ID | Obligation | Official reference |
|---|---|---|
| ID.AM-1 | Inventory physical devices and systems | Appendix A, ID.AM-1 |
| ID.AM-2 | Inventory software platforms and applications | ID.AM-2 |
| ID.AM-3 | Map organizational communication and data flows | ID.AM-3 |
| ID.AM-4 | Catalogue external information systems | ID.AM-4 |
| ID.RA-1 | Identify and document asset vulnerabilities | ID.RA-1 |
| ID.SC-1..5 | Cyber supply chain risk management: assess suppliers, put security in contracts, include suppliers in response/recovery testing (Category added in 1.1) | ID.SC-1 to ID.SC-5 |
| PR.AC-1 | Issue, manage, verify, revoke and audit identities and credentials | PR.AC-1 |
| PR.AC-3 | Manage remote access | PR.AC-3 |
| PR.AC-4 | Least privilege and separation of duties in access permissions | PR.AC-4 |
| PR.AC-5 | Protect network integrity (e.g., segregation, segmentation) | PR.AC-5 |
| PR.AC-7 | Authenticate users, devices and assets commensurate with risk (e.g., single- or multi-factor) | PR.AC-7 |
| PR.DS-1 / PR.DS-2 | Protect data at rest and data in transit | PR.DS-1, PR.DS-2 |
| PR.DS-5 | Protections against data leaks | PR.DS-5 |
| PR.DS-6 / PR.DS-8 | Integrity checking for software, firmware, information and hardware | PR.DS-6, PR.DS-8 |
| PR.DS-7 | Separate development and testing environments from production | PR.DS-7 |
| PR.IP-1 | Baseline configurations maintained | PR.IP-1 |
| PR.IP-4 | Backups conducted, maintained and tested | PR.IP-4 |
| PR.IP-9 | Response and recovery plans in place and managed | PR.IP-9 |
| PR.PT-1 | Audit/log records determined, documented, implemented and reviewed | PR.PT-1 |
| DE.CM-1 / DE.CM-8 | Monitor the network for events; perform vulnerability scans | DE.CM-1, DE.CM-8 |
| RS.RP-1 / RC.RP-1 | Execute response plan and recovery plan during/after an incident | RS.RP-1, RC.RP-1 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Publication date | "April 16, 2018" | Cover page; CSRC "Date Published: April 16, 2018" |
| Structure | 5 Functions, 23 Categories, 108 Subcategories | Appendix A (counted) |
| Implementation Tiers | Tier 1 Partial, Tier 2 Risk Informed, Tier 3 Repeatable, Tier 4 Adaptive | Sec. 2.2 |

The framework sets no notification windows, retention periods or penalties.

## Assessment and certification
No certification or official assessment scheme. Organizations self-assess by building Current and Target Profiles against the Core and choosing a Tier. Third parties may assess against it, but NIST does not accredit assessors.

## Notes
- Catalog row "NIST CSF v1.1 ... self ... legacy version" is correct. Suggest adding that it is superseded by CSF 2.0 (February 26, 2024) and that new programmes should use 2.0.
- CSF 1.1 has no Govern function; governance sat in ID.GV and supply chain in ID.SC. CSF 2.0 moved these into the new GOVERN function.
- The CSF home page still offers the "Framework Version 1.1 (PDF)" and Core spreadsheet for reference (checked 2026-11-06).
