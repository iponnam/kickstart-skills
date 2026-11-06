---
id: csa-star
name: CSA STAR
official_name: "Cloud Security Alliance Security, Trust, Assurance & Risk (STAR) Program"
governing_body: Cloud Security Alliance (CSA); Level 2 audits by CSA-approved certification bodies / CPA firms
type: security
legal_status: certification-scheme
region: global (C-STAR route for the Greater China market)
industry: cloud service providers; AI service providers (STAR for AI)
current_version: "STAR Level 1 and Level 2 based on Cloud Controls Matrix (CCM) v4.1 with CAIQ combined (CCM release date 01/27/2026); STAR for AI based on AICM (06/22/2026)"
superseded_by: none
official_sources:
  - title: "Security, Trust, Assurance & Risk (STAR) Program"
    url: https://cloudsecurityalliance.org/star/levels
    accessed: 2026-11-06
  - title: "About STAR (assurance paths)"
    url: https://cloudsecurityalliance.org/star/about-star
    accessed: 2026-11-06
  - title: "Cloud Controls Matrix (CCM)"
    url: https://cloudsecurityalliance.org/research/cloud-controls-matrix
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
"CSA's STAR Program is the industry-leading assurance program for cloud and AI" that brings together "cloud and AI security frameworks, assessments, and publish[ed] assurance listings into one trusted ecosystem" (STAR page). It is built on the Cloud Controls Matrix (CCM), "a cybersecurity control framework for cloud computing ... composed of 197 control objectives that are structured in 17 domains" (CCM page). The Consensus Assessments Initiative Questionnaire (CAIQ) "captures how your cloud service implements each CCM control. It is the submitted artifact for STAR Level 1 and supports Level 2" (STAR page). Results are published in the public STAR Registry.

## Who it applies to
Voluntary. Cloud service providers "at any size and stage of maturity, whether they are publishing a first self-assessment or extending an existing ISO/IEC 27001 certification or SOC 2 report with cloud-specific assurance" (About STAR). STAR for AI covers AI services using the AI Controls Matrix (AICM) and AI-CAIQ.

CCM v4.1 domains (CCM page): A&A Audit & Assurance; AIS Application & Interface Security; BCR Business Continuity Mgmt & Op Resilience; CCC Change Control & Configuration Management; CEK Cryptography, Encryption & Key Management; DCS Datacenter Security; DSP Data Security & Privacy; GRC Governance, Risk Management & Compliance; HRS Human Resources Security; IAM Identity & Access Management; IPY Interoperability & Portability; IVS Infrastructure & Virtualization Security; LOG Logging & Monitoring; SEF Security Incident Mgmt, E-Discovery & Cloud Forensics; STA Supply Chain Mgmt, Transparency & Accountability; TVM Threat & Vulnerability Management; UEM Universal Endpoint Management.

## Engineering obligations
Rows map to CCM domains (domain codes verified; individual control text not read).

| ID | Obligation | Official reference |
|---|---|---|
| CSA-01 | Complete the CAIQ (now combined with CCM v4.1) describing how the service implements each CCM control | STAR page; CCM page ("Version 4.1 of the CCM and CAIQ are now combined") |
| CSA-02 | Document shared responsibility between CSP and customer per control | CCM page ("CCM defines the security roles between CSPs and customers") |
| AIS | Application and API security in the SDLC | CCM domain AIS |
| BCR | Business continuity, backups and operational resilience | CCM domain BCR |
| CCC | Change control and configuration management (baselines, change approval) | CCM domain CCC |
| CEK | Cryptography, encryption and key management | CCM domain CEK |
| DSP | Data classification, inventory, retention/deletion, privacy | CCM domain DSP |
| IAM | Identity and access management (least privilege, strong auth, access reviews) | CCM domain IAM |
| IPY | Interoperability and portability (data export) | CCM domain IPY |
| IVS | Infrastructure and virtualisation security (network segmentation, hardening) | CCM domain IVS |
| LOG | Logging and monitoring (audit logs, protection, alerting) | CCM domain LOG |
| SEF | Incident management, e-discovery and cloud forensics | CCM domain SEF |
| STA | Supply chain management, transparency and accountability | CCM domain STA |
| TVM | Threat and vulnerability management (scanning, patching, pen testing) | CCM domain TVM |
| UEM | Universal endpoint management | CCM domain UEM |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| CCM size | "197 control objectives that are structured in 17 domains" | CCM page |
| CCM current release | "Version 4.1 of the CCM and CAIQ are now combined"; "Release date: 01/27/2026" | CCM page; STAR page |
| AICM release | "Release date: 06/22/2026" | STAR page |
| Registry size (snapshot) | "4119 STAR Registry listings", "2907 Organizations listed" | STAR page, 2026-11-06 |

## Assessment and certification
- STAR Level 1: Self-Assessment (submit the CAIQ) or Level 1 Valid-AI-ted ("Automated validation of a CAIQ or AI-CAIQ submission that returns scoring and improvement guidance") (STAR page, About STAR).
- STAR Level 2: third-party audit: "Certification (ISO/IEC 27001), Attestation (SOC 2), or C-STAR for the Greater China market, each combined with a CAIQ submission" (STAR page). Prerequisite listed on About STAR: "Valid-AI-ted CAIQ on the STAR Registry". Audits by "approved certification bodies and assessment firms" (Certified STAR Auditors).
- STAR for AI Level 1 / Level 2: AI-CAIQ; Level 2 via ISO/IEC 27001, 27001 + 42001, 42001 or SOC 2 routes, "each paired with an AI-CAIQ passed through Valid-AI-ted" (STAR page).
- Re-submission/validity cadence: UNVERIFIED (not on pages read).

## Notes
- `framework-catalog.md` row "CSA STAR | ... | self / certification" is broadly correct; add "attestation (SOC 2 + CCM)" as a Level 2 route and that Level 1 requires a public CAIQ in the STAR Registry.
- STAR Level 3 (continuous monitoring) is not listed among current assurance paths on the official STAR pages (only Level 1 and Level 2): if the repo mentions Level 3, remove it.
- The CCM page still states "197 control objectives" while announcing v4.1; whether v4.1 changed the count is UNVERIFIED.
- New officially: STAR for AI (AICM, AI-CAIQ, Level 1 and Level 2) and Valid-AI-ted.
