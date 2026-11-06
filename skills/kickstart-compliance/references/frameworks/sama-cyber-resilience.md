---
id: sama-cyber-resilience
name: SAMA CRFR
official_name: SAMA Cyber Resilience Fundamental Requirements (CRFR)
governing_body: Saudi Central Bank (SAMA)
type: security
legal_status: binding-regulation
region: Saudi Arabia
industry: "finance - newly established entities, regulatory sandbox participants and licence applicants (rulebook scope: Finance Sector, Payment Systems and PSPs, Money Exchange Sector, Regulatory Sandbox)"
current_version: Rulebook entry dated 1/1/2022G (28/5/1443H), No. "NA"; status "In-Force"
superseded_by: none
official_sources:
  - title: SAMA Rulebook - Cyber Resilience Fundamental Requirements (CRFR) (full text)
    url: https://rulebook.sama.gov.sa/en/cyber-resilience-fundamental-requirements-crfr-1
    accessed: 2026-11-06
  - title: SAMA Rulebook - CRFR section landing page
    url: https://rulebook.sama.gov.sa/en/cyber-resilience-fundamental-requirements-crfr
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The official title is "Cyber Resilience Fundamental Requirements" (not "Fundamentals"). SAMA developed it for entities "recently established and are in the early stages of their operations" in the Saudi financial sector, as a prioritised set of cyber security and resilience controls aligned with the SAMA CSF and Business Continuity Management Framework (s.1, 1.1). It is not a replacement for the CSF/BCMF, which apply post-licensing (s.1.2).

## Who it applies to
s.1.2: "entities intending to qualify for SAMA Regulatory Sandbox environment and/or entities seeking license to operate in the kingdom of Saudi Arabia". Non-compliance lets SAMA "prohibit the sandboxing graduation/license request" (s.1.4).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| 3.1.1 | Cyber security governance structure with resources | 3.1.1 |
| 3.1.2 | Approved policies, procedures and security standards (e.g. password, firewall) | 3.1.2, 3.1.3 |
| 3.1.4 | Cyber/fraud risk evaluation of business model; protection against adversarial attacks on models (model stealing, malicious inputs, poisoning) | 3.1.4 |
| 3.1.5 | Password policy: change on first logon, length/history/complexity, revoke access "after the three successive incorrect passwords", non-caching | 3.1.5 |
| 3.1.6 | IT and cyber risk assessments, risks documented centrally | 3.1.6 |
| 3.2.1 | IAM on need-to-have and need-to-know | 3.2.1 |
| 3.2.2 | Change management: changes classified, tested, approved before production | 3.2.2 |
| 3.2.3 | Segmented network architecture with firewalls; availability | 3.2.3 |
| 3.2.4 | Secure cryptography; application and server communications encrypted with secure protocols | 3.2.4 |
| 3.2.5 | Periodic vulnerability assessment (application and infrastructure) | 3.2.5 |
| 3.2.6 | Penetration testing "twice a year as a minimum or after major/ critical change" | 3.2.6 |
| 3.2.7 | Timely tested patching | 3.2.7 |
| 3.2.8 | Secure SDLC plus app shielding (code obfuscation, white-box cryptography, anti-tampering) | 3.2.8 |
| 3.2.9 | Brand protection monitoring and takedown | 3.2.9 |
| 3.2.10 | Endpoint protection; mobile data separation, encryption and remote wipe | 3.2.10 |
| 3.2.11 | Security logs collected, reviewed and "retained securely for a period of one year as a minimum" | 3.2.11 |
| 3.2.12 | Apps and infrastructure integrated with SIEM; continuous monitoring | 3.2.12, 3.2.13 |
| 3.2.14 | Incident management process | 3.2.14 |
| 3.2.15 | Inactive sessions "should not exceed 5 minutes for applications and underlying infrastructure" | 3.2.15 |
| 3.2.16 | Inform SAMA immediately of medium-or-above cyber, fraud and disruptive incidents | 3.2.16 |
| 3.3.1 | BCP and DRP defined, approved, tested and reviewed | 3.3.1 |
| 3.3.2 | Backups: schedule, encryption of confidential backup data, offline/offsite storage, secure destruction, restoration tests | 3.3.2 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident notification to SAMA | "immediately inform SAMA (F.S.Cybersecurity@SAMA.GOV.SA) in case any of the following incidents classified as medium or above" | 3.2.16 |
| Log retention | "one year as a minimum" | 3.2.11 |
| Penetration testing | "twice a year as a minimum" | 3.2.6 |
| Session timeout | "should not exceed 5 minutes" | 3.2.15 |
| Failed login lockout | "after the three successive incorrect passwords" | 3.1.5 (b) |

## Assessment and certification
Periodic self-assessment by questionnaire; copy sent to SAMA; SAMA may review and "audit the compliance ... at any time" (s.2.3).

## Notes
- Catalog name "SAMA Cyber Resilience Fundamentals" should be "Cyber Resilience Fundamental Requirements (CRFR)"; scope is sandbox entities and licence applicants (early-stage), not all Saudi financial institutions. Type is security + continuity.
- s.2.1 says "structured around four domains" but lists three (Leadership and Governance; Operations and Technology; Resilience). Recorded as published.
- Not a law; a SAMA regulatory requirement tied to licensing/sandbox.
