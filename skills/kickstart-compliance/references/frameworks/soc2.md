---
id: soc2
name: SOC 2
official_name: "SOC 2® - SOC for Service Organizations: Trust Services Criteria (examination of controls at a service organization relevant to security, availability, processing integrity, confidentiality, or privacy)"
governing_body: AICPA (Assurance Services Executive Committee sets the Trust Services Criteria; Auditing Standards Board sets the attestation standards SSAE No. 18, AT-C sections); performed by licensed CPA firms
type: security
legal_status: voluntary-standard
region: global (US attestation standards; used worldwide)
industry: any (service organizations)
current_version: "2017 Trust Services Criteria (With Revised Points of Focus – 2022) and 2018 Description Criteria (With Revised Implementation Guidance – 2022); performed under SSAE No. 18 as amended (AT-C 105, 205). Proposed 2027 TSC in exposure (Oct 26, 2026)"
superseded_by: none (proposed 2027 SOC 2 Trust Services Criteria exposure draft issued Oct 26, 2026; not final)
official_sources:
  - title: "System and Organization Controls: SOC Suite of Services"
    url: https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services
    accessed: 2026-11-06
  - title: "2017 Trust Services Criteria (With Revised Points of Focus – 2022)"
    url: https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022
    accessed: 2026-11-06
  - title: "AICPA Exposure Drafts: Proposed 2027 SOC 2® Trust Services Criteria and Description Criteria"
    url: https://www.aicpa-cima.com/resources/download/aicpa-exposure-drafts-proposed-2027-soc-2-trust-services-criteria-and-description-criteria
    accessed: 2026-11-06
  - title: "SOC 2® Reporting on an Examination of Controls at a Service Organization ... (AICPA Guide, Oct 2022)"
    url: https://www.aicpa-cima.com/cpe-learning/publication/soc-2-reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-security-availability-processing-integrity-confidentiality-or-privacy
    accessed: 2026-11-06
  - title: "Illustrative Management Representation Letter (SOC 2® Type 2)"
    url: https://www.aicpa-cima.com/resources/download/illustrative-management-representation-letter-soc-2-type-2
    accessed: 2026-11-06
  - title: "AICPA SSAEs – currently effective"
    url: https://www.aicpa-cima.com/resources/download/aicpa-ssaes-currently-effective
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
SOC 2 is an AICPA attestation engagement: an "assertion-based examination of a service organization's description of its system and its controls relevant to security, availability, processing integrity, confidentiality, or privacy" (SOC 2 Guide, Key Topics). Customers and business partners "often request a SOC 2 report from the service organization" to assess risks from outsourcing (SOC 2 Guide). Controls are evaluated against the 2017 Trust Services Criteria, which "presents control criteria established by the AICPA's Assurance Services Executive Committee (ASEC)" (TSC download page), and the system description against the 2018 Description Criteria (with revised implementation guidance, 2022).

## Who it applies to
Voluntary. Any service organization whose customers request assurance on controls over security, availability, processing integrity, confidentiality or privacy. The TSC can be used "across an entire entity; at a subsidiary, division, [or operating unit]..." (TSC download page; text truncated on the free page). The engagement is performed by a CPA under the AICPA attestation standards; the illustrative representation letter cites "AT-C section 205, Assertion-Based Examinations".

Trust services categories (verified names): Security, Availability, Processing Integrity, Confidentiality, Privacy (SOC 2 Guide title and TSC title). Which categories beyond Security are in scope is chosen by the service organization: UNVERIFIED (the TSC PDF is behind an AICPA account login).

## Engineering obligations
The TSC PDF itself requires an AICPA account and could not be read. Criterion IDs below follow the 2017 TSC numbering and are UNVERIFIED against the official text in this pass; treat them as pointers to confirm.

| ID | Obligation | Official reference |
|---|---|---|
| SOC2-01 | Write and maintain a system description (services, boundaries, components, principal service commitments and system requirements) | 2018 Description Criteria (with revised implementation guidance, 2022) (verified as the governing criteria; content UNVERIFIED) |
| CC3 | Risk assessment: identify and assess risks to objectives, including fraud and change | TSC CC3.1–CC3.4 (UNVERIFIED) |
| CC5 | Control activities and technology general controls, deployed through policies | TSC CC5.1–CC5.3 (UNVERIFIED) |
| CC6.1 | Logical access security software, infrastructure and architectures over protected assets | TSC CC6.1 (UNVERIFIED) |
| CC6.2–6.3 | Provision, modify and remove user access; least privilege and segregation of duties | TSC CC6.2, CC6.3 (UNVERIFIED) |
| CC6.6 | Protect against threats from sources outside system boundaries | TSC CC6.6 (UNVERIFIED) |
| CC6.7 | Restrict and protect transmission, movement and removal of information (e.g. encryption in transit) | TSC CC6.7 (UNVERIFIED) |
| CC6.8 | Prevent or detect unauthorised or malicious software | TSC CC6.8 (UNVERIFIED) |
| CC7.1 | Detection and monitoring procedures for configuration changes and newly discovered vulnerabilities | TSC CC7.1 (UNVERIFIED) |
| CC7.2 | Monitor system components for anomalies indicative of malicious acts | TSC CC7.2 (UNVERIFIED) |
| CC7.3–7.5 | Evaluate security events, respond to and recover from incidents | TSC CC7.3–CC7.5 (UNVERIFIED) |
| CC8.1 | Change management: authorise, design, develop, configure, document, test, approve and implement changes | TSC CC8.1 (UNVERIFIED) |
| CC9.2 | Assess and manage risks from vendors and business partners | TSC CC9.2 (UNVERIFIED) |
| A1.2 | Availability: environmental protections, backups and recovery infrastructure | TSC A1.2 (UNVERIFIED) |
| A1.3 | Test recovery plan procedures | TSC A1.3 (UNVERIFIED) |
| C1.1–C1.2 | Confidentiality: identify, maintain and dispose of confidential information | TSC C1.1, C1.2 (UNVERIFIED) |
| PI1.x | Processing integrity: input, processing and output controls for complete, accurate, timely processing | TSC PI1.1–PI1.5 (UNVERIFIED) |
| P1–P8 | Privacy: notice, choice/consent, collection, use/retention/disposal, access, disclosure, quality, monitoring | TSC P1.0–P8.0 (UNVERIFIED) |
| SOC2-02 | Evaluate the effect of software tools and AI used by the service organization on the examination | AICPA FAQ "Effect of the use of software tools on SOC 2® examinations"; TQA 9561 (titles verified on the suite page) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Current criteria | "2017 Trust Services Criteria (With Revised Points of Focus – 2022)" | TSC download page |
| Description criteria | "2018 description criteria (with revised implementation guidance — 2022)" | SOC 2 Guide page |
| SOC 2 Guide edition | "Updated as of October 15, 2022", reflects "SSAE No. 20 and SSAE No. 21" | SOC 2 Guide page |
| Type 2 rep letter applicability | "should be used for engagements with reports dated on or after June 15, 2022" | Illustrative Mgmt Rep Letter (SOC 2 Type 2) page |
| Proposed new criteria | "Proposed 2027 SOC 2® Trust Services Criteria and Description Criteria", issued Oct 26, 2026 | Exposure draft page |
| Attestation standards currency | listing "current as of August 2026" | AICPA SSAEs – currently effective |

## Assessment and certification
Performed by a licensed CPA firm (service auditor) as an attestation examination, not a certification. Output is a SOC 2 report (restricted use) containing management's assertion, the system description and the service auditor's opinion. The AICPA publishes illustrative representation letters for "SOC 2® Type 1" and "SOC 2® Type 2" (verified titles). Type 1 vs Type 2 meaning: Type 1 reports on the description and suitability of design of controls as of a point in time; Type 2 additionally reports on operating effectiveness throughout a specified period. UNVERIFIED: this wording is from general knowledge; the AICPA definitions sit in the SOC 2 Guide and AT-C pages behind login. Audit cadence (commonly annual) and minimum period length are not set in any free official page reviewed: UNVERIFIED. The AICPA warns it will act against auditors found "to have not performed audits in accordance with professional standards, not been enrolled in peer review, and/or are unlicensed" (suite page notice).

## Notes
- `control-checklists.md` says "Type II requires 3–12 months of evidence." No free AICPA source states a 3 or 12 month rule; AICPA standards require a specified period but leave its length to the engagement. Mark it UNVERIFIED or reword ("a review period, commonly 6–12 months, chosen with the auditor").
- `framework-catalog.md` lists SOC 2 as "attestation" (correct) and "global, strongest in US" (fine). It does not say which TSC version applies; add "2017 TSC (revised points of focus 2022)" and the pending 2027 TSC exposure draft.
- New, officially announced: the AICPA ASEC issued exposure drafts of a "Proposed 2027 SOC 2® Trust Services Criteria" and revised Description Criteria on Oct 26, 2026. The comment deadline and effective date were not readable (behind login): UNVERIFIED.
- AICPA notice (suite page) about a compliance vendor's SOC practices and peer reviewer alerts (May 2026) about "quick-turn" SOC 2 engagements: worth noting to users choosing auditors.
- The criteria text (CC1–CC9, A1, C1, PI1, P1–P8) could not be read; all criterion IDs are UNVERIFIED.
