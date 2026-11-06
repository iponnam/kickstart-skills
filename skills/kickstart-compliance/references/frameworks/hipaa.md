---
id: hipaa
name: HIPAA (Privacy, Security, Breach Notification Rules)
official_name: HIPAA Administrative Simplification Regulations, 45 CFR Part 160 and Part 164 Subparts A, C (Security Rule), D (Breach Notification Rule) and E (Privacy Rule)
governing_body: U.S. Department of Health and Human Services (HHS); enforced by the HHS Office for Civil Rights (OCR)
type: privacy
legal_status: law
region: US
industry: health (covered entities and their business associates)
current_version: 45 CFR Parts 160 and 164 as in eCFR on 2026-11-06 (Security Rule §164.312 last amended 2016-12-30; Part 164 latest eCFR amendment date 2024-06-25)
superseded_by: none
official_sources:
  - title: 45 CFR Part 164 Subpart D, Notification in the Case of Breach of Unsecured PHI (eCFR)
    url: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D
    accessed: 2026-11-06
  - title: 45 CFR 164.308 Administrative safeguards (eCFR)
    url: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308
    accessed: 2026-11-06
  - title: 45 CFR 164.312 Technical safeguards (eCFR)
    url: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312
    accessed: 2026-11-06
  - title: 45 CFR 164.316 Policies and procedures and documentation requirements (eCFR)
    url: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.316
    accessed: 2026-11-06
  - title: 45 CFR 164.306, 164.502, 164.524; 160.103 definitions (eCFR)
    url: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164
    accessed: 2026-11-06
  - title: eCFR version history, 45 CFR 164.312 and Part 164
    url: https://www.ecfr.gov/api/versioner/v1/versions/title-45.json?section=164.312
    accessed: 2026-11-06
  - title: eCFR versioner, version history for 45 CFR Part 164
    url: https://www.ecfr.gov/api/versioner/v1/versions/title-45.json?part=164
    accessed: 2026-11-06
  - title: eCFR versioner, version history for 45 CFR Part 160
    url: https://www.ecfr.gov/api/versioner/v1/versions/title-45.json?part=160
    accessed: 2026-11-06
  - title: eCFR point-in-time text, 45 CFR 164.502 (as of 2026-11-04)
    url: https://www.ecfr.gov/api/versioner/v1/full/2026-11-04/title-45.xml?section=164.502
    accessed: 2026-11-06
  - title: eCFR point-in-time text, 45 CFR 160.103 (as of 2026-05-26)
    url: https://www.ecfr.gov/api/versioner/v1/full/2026-05-26/title-45.xml?section=160.103
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
The HIPAA Rules regulate use and disclosure of protected health information (Privacy Rule, Subpart E), require administrative, physical and technical safeguards for electronic PHI (Security Rule, Subpart C), and require notification after a breach of unsecured PHI (Breach Notification Rule, Subpart D). "Breach means the acquisition, access, use, or disclosure of protected health information in a manner not permitted under subpart E of this part which compromises the security or privacy of the protected health information" and is "presumed to be a breach" unless a low probability of compromise is demonstrated by risk assessment (§164.402).

## Who it applies to
Covered entities (health plans, health care clearinghouses, and health care providers who transmit health information electronically in standard transactions) and business associates that create, receive, maintain or transmit PHI on their behalf (§160.103 definitions "Covered entity" and "Business associate"). A covered entity may let a business associate handle ePHI only with satisfactory assurances in a business associate contract (§164.308(b)(1), §164.314(a)).

## Engineering obligations
Security Rule specifications are "Required" or "Addressable"; for addressable ones the entity must assess whether each is "a reasonable and appropriate safeguard" and implement it, or document why not and implement an equivalent alternative if reasonable (§164.306(d)).

| ID | Obligation | Official reference |
|---|---|---|
| 164.308(a)(1)(ii)(A) | Risk analysis (Required): "accurate and thorough assessment of the potential risks and vulnerabilities" to ePHI | §164.308(a)(1)(ii)(A) |
| 164.308(a)(1)(ii)(B) | Risk management (Required) | §164.308(a)(1)(ii)(B) |
| 164.308(a)(1)(ii)(D) | Information system activity review (Required): regularly review audit logs, access reports, incident tracking | §164.308(a)(1)(ii)(D) |
| 164.308(a)(5) | Security awareness and training; log-in monitoring and password management (Addressable) | §164.308(a)(5)(i), (ii)(C), (ii)(D) |
| 164.308(a)(7) | Contingency plan: data backup plan, disaster recovery plan, emergency mode operation plan (Required); testing and revision (Addressable) | §164.308(a)(7)(ii)(A)-(D) |
| 164.308(a)(8) | Periodic technical and nontechnical evaluation | §164.308(a)(8) |
| 164.308(b) | Business associate contracts before a BA handles ePHI | §164.308(b)(1); §164.314(a) |
| 164.312(a)(2)(i) | Unique user identification (Required) | §164.312(a)(2)(i) |
| 164.312(a)(2)(ii) | Emergency access procedure (Required) | §164.312(a)(2)(ii) |
| 164.312(a)(2)(iii) | Automatic logoff after predetermined inactivity (Addressable) | §164.312(a)(2)(iii) |
| 164.312(a)(2)(iv) | Encryption and decryption of ePHI (Addressable) | §164.312(a)(2)(iv) |
| 164.312(b) | Audit controls: "record and examine activity in information systems that contain or use electronic protected health information" | §164.312(b) |
| 164.312(c) | Integrity: mechanisms to corroborate ePHI not altered or destroyed (Addressable) | §164.312(c)(1), (c)(2) |
| 164.312(d) | Person or entity authentication | §164.312(d) |
| 164.312(e) | Transmission security: integrity controls and encryption in transit (Addressable) | §164.312(e)(2)(i), (ii) |
| 164.316 | Written policies, procedures and documentation of required actions, retained 6 years | §164.316(a), (b) |
| 164.502(b) | Minimum necessary: limit PHI used, disclosed or requested to the minimum necessary | §164.502(b) |
| 164.524 | Right of access: provide individuals access to their PHI within the deadline | §164.524(b)(2) |
| 164.404/406/408/410 | Breach notification workflow to individuals, media, HHS; BA notifies covered entity | Subpart D |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Notification to individuals | "without unreasonable delay and in no case later than 60 calendar days after discovery of a breach" | §164.404(b) |
| Notification to media | breach "involving more than 500 residents of a State or jurisdiction"; same 60-calendar-day limit | §164.406(a), (b) |
| Notification to HHS, 500 or more | "contemporaneously with the notice required by § 164.404(a)" | §164.408(b) |
| Notification to HHS, under 500 | log and notify "not later than 60 days after the end of each calendar year" | §164.408(c) |
| Business associate to covered entity | "without unreasonable delay and in no case later than 60 calendar days after discovery of a breach" | §164.410(b) |
| Documentation retention | "6 years from the date of its creation or the date when it last was in effect, whichever is later" | §164.316(b)(2)(i) |
| Right of access response | "no later than 30 days after receipt of the request"; one extension of no more than 30 days | §164.524(b)(2)(i), (ii) |

## Assessment and certification
No certification. OCR enforces through complaint investigations, compliance reviews and audits; civil money penalties under 45 CFR Part 160 Subpart D. Entities self-assess through the required risk analysis and periodic evaluation (§164.308(a)(1), (a)(8)).

## Notes
- control-checklists.md HIPAA-04 says "log every access to PHI ... retain 6 years". Correction: §164.312(b) requires audit controls but sets no log retention period; the 6-year rule in §164.316(b)(2)(i) applies to required policies, procedures and documentation of actions/assessments, not explicitly to audit logs. Rephrase.
- HIPAA-02 "Risk analysis documented and updated annually": the current rule requires an accurate and thorough risk analysis and periodic evaluation (§164.308(a)(1)(ii)(A), (a)(8)) but does not state "annually". Annual cadence is not in current text.
- HIPAA-06 "Encryption ... (addressable but expected)": "addressable" is correct (§164.312(a)(2)(iv), (e)(2)(ii)); "expected" is not regulatory text. Note that encryption per HHS guidance makes PHI not "unsecured", which takes it out of breach notification (§164.402 definition).
- HIPAA-08 "individuals within 60 days, HHS, media if over 500": tighten to "without unreasonable delay and no later than 60 calendar days"; media notice is for more than 500 residents of a State or jurisdiction; HHS notice is contemporaneous for 500 or more, annual log for fewer than 500.
- Proposed Security Rule update: an HHS NPRM to modify the Security Rule (January 2025) is reported, but its current status is UNVERIFIED because hhs.gov returned 403 to curl and Access Denied to headless Chromium, and federalregister.gov/regulations.gov were not reachable. eCFR shows §164.312 unchanged since 2016-12-30 (still containing "Addressable" specifications), so the proposal is not in force as of 2026-11-06. Do not treat it as law.
- **eCFR amendment history (follow-up pass):** Part 164 sections amended after 2016-12-30 are only 164.105 and 164.314 (2020-11-24) and 164.502, 164.509, 164.512, 164.520, 164.535 (2024-04-26 / 2024-06-25, source 89 FR 33063, Apr. 26, 2024: the reproductive health care privacy amendments; eCFR as of 2026-11-04 still shows the "Reproductive health care" prohibition in §164.502(a)(5)(iii)). No Security Rule section (164.302-164.318) has changed since 2016-12-30, confirming the Security Rule NPRM is not in force. Part 160 changed only in §160.103: 89 FR 33062 (Apr. 26, 2024) and 91 FR 14404 (Mar. 24, 2026, in eCFR from 2026-05-26), the latter renaming the standard transaction "Health claims attachments" to "Health care claims attachments". Any court ruling on the 2024 reproductive health amendments is not reflected in eCFR text and was not checked (UNVERIFIED; hhs.gov and federalregister.gov blocked).
