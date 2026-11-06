# Control checklists (engineering view)

Condensed, actionable control sets for the most-selected frameworks. Each is what an engineering team must build, configure or document. They are not the full standard. For frameworks not listed here, derive controls from the closest family below and label them `<FW>-01…`.

Families:
- **ISMS family** (ISO 27001, SOC 2, NIST CSF, CIS, Cyber Essentials, Essential Eight, ECC, SAMA, MAS TRM, RBI CSF, SEBI CSCRF, NYDFS, NIS 2, DORA): use the ISMS set and add the family-specific rows.
- **Privacy family** (GDPR, UK GDPR, DPDPA, CCPA/CPRA, PIPEDA, PDPA SG, Law 25, LGPD, POPIA, APPI, PIPL, US state laws, Botswana, Seychelles, NJ): use the Privacy set and add jurisdiction rows.
- **Sector family** (HIPAA, PCI DSS, COPPA, FERPA, GLBA, PHIPA, DTAC): sector-specific sets below.
- **AI family** (NIST AI RMF, ISO 42001, EU AI Act).

---

## ISMS set (base for SOC 2, ISO 27001, NIST CSF, CIS, and regulators)

| ID | Control | Evidence |
|---|---|---|
| ISMS-01 | Asset inventory: list of systems, repos, data stores, third-party services, with an owner each | `.kickstart/assets.md` or infra-as-code |
| ISMS-02 | Risk register: top risks with likelihood, impact, owner, treatment | `.kickstart/decisions/risk-register.md` |
| ISMS-03 | Access control: SSO or MFA for all production and code access; least privilege; quarterly access review | IdP config, review log |
| ISMS-04 | Joiner/mover/leaver: access provisioned and revoked within 24h of status change | Offboarding checklist, IdP logs |
| ISMS-05 | Change management: all production changes via pull request with review and CI passing; protected default branch | Branch protection settings, PR history |
| ISMS-06 | Secure development: linting, SAST, dependency scanning, secret scanning in CI | CI config |
| ISMS-07 | Vulnerability management: SLA for fixes (critical 7d, high 30d, medium 90d); monthly dependency refresh | `kickstart-refresh` runs, audit history |
| ISMS-08 | Encryption: TLS 1.2+ in transit, encryption at rest for data stores and backups, managed keys | Cloud config |
| ISMS-09 | Logging and monitoring: centralised logs, retention policy, alerts on auth anomalies and error spikes | Logging platform config |
| ISMS-10 | Backup and recovery: automated backups, tested restore at least quarterly, documented RPO/RTO | Backup config, restore test log |
| ISMS-11 | Incident response: written plan with severity levels, contacts, communication templates; post-incident reviews | `.kickstart/runbooks/incident-response.md` |
| ISMS-12 | Business continuity: single points of failure identified, failover or acceptable downtime documented | Decision record |
| ISMS-13 | Vendor management: list of third parties with data access, their certifications, and contract/DPA status | `.kickstart/vendors.md` |
| ISMS-14 | Security awareness: onboarding security briefing, annual refresher, phishing awareness | Training log |
| ISMS-15 | Policies: information security, acceptable use, access control, data classification, retention, approved by leadership, reviewed annually | `docs/policies/` |
| ISMS-16 | Endpoint security: disk encryption, screen lock, auto-updates, EDR or equivalent on staff devices | MDM or attestation |
| ISMS-17 | Physical security: office or remote-work rules; cloud provider physical controls inherited via their SOC 2 / ISO reports | Vendor reports |
| ISMS-18 | Data classification and handling: public / internal / confidential / restricted with handling rules | Policy + labels in schema |
| ISMS-19 | Secure configuration baseline: hardened images, no default credentials, infrastructure as code reviewed | IaC repo |
| ISMS-20 | Management review: security metrics reviewed at least quarterly by leadership | Meeting notes |

### SOC 2 additions (Trust Services Criteria)
- SOC2-A: Availability commitments (SLA) defined and monitored (uptime dashboard).
- SOC2-C: Confidentiality: data disposal procedure, NDA for staff and contractors.
- SOC2-PI: Processing integrity (if in scope): input validation, reconciliation checks, error handling logged.
- SOC2-P: Privacy (if in scope): see Privacy set.
- Type II requires 3–12 months of evidence. Start collecting the day controls go live.

### ISO 27001:2022 additions
- Statement of Applicability covering Annex A (93 controls) with justification for exclusions.
- Internal audit before certification audit.
- Threat intelligence (5.7), cloud services security (5.23), ICT readiness for continuity (5.30), data masking (8.11), DLP (8.12), web filtering (8.23), secure coding (8.28).

### NIST CSF 2.0 additions
- Govern function: cyber risk strategy, roles, supply-chain risk management documented.
- Map each ISMS row to Identify / Protect / Detect / Respond / Recover.

### Cyber Essentials v3.2 (UK, 5 controls)
- Firewalls on all devices and boundary; secure configuration; user access control; malware protection; security update management within 14 days of release.

### Essential Eight (AU)
- Application control; patch applications; configure MS Office macros; user application hardening; restrict admin privileges; patch OS; MFA; regular backups. Level 1 = baseline settings, Level 2 = tighter timeframes (patch within 2 weeks, MFA phishing-resistant for privileged).

### Regulator add-ons
- **RBI CSF / SEBI CSCRF / MAS TRM / SAMA / NYDFS / DORA / NIS 2:** board-approved cyber policy; CISO or named responsible person; incident reporting to the regulator within the mandated window (RBI 6h, SEBI 6h, MAS 1h for critical, NYDFS 72h, DORA 4h initial, NIS 2 24h early warning); annual VAPT by an approved vendor; data localisation where mandated (RBI payments data in India); third-party ICT risk register; resilience testing.
- **CERT-In (India, all entities):** report incidents within 6 hours; keep logs 180 days in India; sync clocks to NIC/NPL NTP; keep KYC/subscriber records 5 years for the specified service types.

---

## Privacy set (base for GDPR and most data protection laws)

| ID | Control | Evidence |
|---|---|---|
| PRIV-01 | Record of processing: what personal data, why, legal basis, retention, recipients, transfers | `.kickstart/privacy/ropa.md` |
| PRIV-02 | Lawful basis and consent: consent captured with timestamp and version where required; withdrawable as easily as given | Consent table in DB |
| PRIV-03 | Privacy notice: published, plain language, lists purposes, rights, contact, retention | `/privacy` page |
| PRIV-04 | Data minimisation: collect only required fields; schema review for unnecessary PII | Schema diff |
| PRIV-05 | Data subject rights: export, delete, correct, restrict; fulfilled within the statutory window (GDPR 30d, DPDPA as prescribed, CCPA 45d) | Endpoints or admin runbook, request log |
| PRIV-06 | Retention and deletion: retention periods enforced by job or policy; backups expire | Scheduled job, backup policy |
| PRIV-07 | Security of processing: see ISMS-08/09; pseudonymisation where feasible | Config |
| PRIV-08 | Breach notification: process to notify the authority within the window (GDPR 72h, DPDPA as prescribed to the Board, most US states 30–60d) and affected users where required | Incident runbook |
| PRIV-09 | Processors and transfers: DPA signed with every processor; cross-border transfer mechanism documented (SCCs, adequacy, DPDPA permitted countries) | `.kickstart/vendors.md` |
| PRIV-10 | DPIA for high-risk processing (profiling, large-scale sensitive data, children, tracking) | `.kickstart/privacy/dpia-*.md` |
| PRIV-11 | Children's data: age gating and parental consent where the law sets a threshold (DPDPA under 18, GDPR 13–16 by state, COPPA under 13) | Signup flow |
| PRIV-12 | Cookies and tracking: consent before non-essential cookies in EU/UK; "Do Not Sell/Share" link for CCPA | Consent banner config |
| PRIV-13 | Named contact: DPO (where required), Grievance Officer (DPDPA), privacy contact email published | Privacy page |
| PRIV-14 | Staff training on handling personal data | Training log |

### Jurisdiction rows
- **GDPR / UK GDPR:** Art. 30 records; Art. 28 processor contracts; Art. 35 DPIA; representative in EU/UK if established outside; legitimate-interest assessments documented.
- **DPDPA (India):** notice in English or a scheduled language; consent manager interoperability (when rules in force); Significant Data Fiduciary obligations if designated (DPO in India, audits, DPIA); verifiable parental consent under 18; no tracking or targeted ads to children.
- **CCPA/CPRA:** "Do Not Sell or Share" and "Limit Use of Sensitive PI" links; respond to opt-out signals (GPC); annual risk assessment and cybersecurity audit for high-risk businesses; contractor terms.
- **PIPEDA / Law 25:** privacy officer named; privacy impact assessment before transfers outside Quebec; breach register kept; consent in clear language, separately for each purpose (Law 25).
- **PDPA Singapore:** DPO appointed and contact published; Do Not Call registry checks for marketing; breach notification to PDPC within 3 days of assessment.
- **LGPD:** DPO (encarregado) named; legal bases mapped to Art. 7; ANPD notification.
- **POPIA:** Information Officer registered with the Regulator; prior authorisation for certain processing.
- **US multi-state:** universal opt-out signal support; data protection assessments for targeted advertising, sale, profiling; consent for sensitive data (most states).

---

## Sector sets

### HIPAA (US health)
| ID | Control |
|---|---|
| HIPAA-01 | Determine covered entity / business associate status; sign BAAs with every vendor touching PHI (cloud, email, analytics) |
| HIPAA-02 | Risk analysis documented and updated annually |
| HIPAA-03 | Access controls: unique user IDs, role-based access to PHI, automatic logoff, emergency access procedure |
| HIPAA-04 | Audit controls: log every access to PHI with user, time, record; retain 6 years |
| HIPAA-05 | Integrity: checksums or DB constraints on PHI; transmission security (TLS) |
| HIPAA-06 | Encryption at rest and in transit for PHI (addressable but expected) |
| HIPAA-07 | Minimum necessary: API responses and UI show only needed PHI fields |
| HIPAA-08 | Breach notification: individuals within 60 days, HHS, media if over 500 |
| HIPAA-09 | Workforce training and sanctions policy |
| HIPAA-10 | Contingency plan: backups, disaster recovery, emergency mode operations, tested |
| HIPAA-11 | No PHI in logs, error trackers, analytics, or LLM prompts without a BAA |

### PCI DSS v4.0 (card data)
Decide scope first. Using a hosted checkout (Stripe Checkout, Razorpay hosted page, Adyen Drop-in) with no card data touching your servers usually means **SAQ-A**, which is small.
| ID | Control |
|---|---|
| PCI-01 | Card data never stored, logged, or transits your servers; tokenise via provider (SAQ-A scope) |
| PCI-02 | Payment pages served over TLS; iframe/redirect integrity (SRI on provider scripts, CSP) |
| PCI-03 | Vulnerability scan by an ASV quarterly if you have a public-facing payment page (SAQ-A-EP and above) |
| PCI-04 | Access to the payment provider dashboard restricted and MFA-enforced |
| PCI-05 | Webhook signatures verified; idempotency on payment events |
| PCI-06 | If card data touches your systems (SAQ-D): full 12 requirements apply, network segmentation, key management, file-integrity monitoring; plan for a QSA |
| PCI-07 | Annual SAQ completion and Attestation of Compliance kept |

### COPPA (children under 13, US)
- Age screen that does not encourage lying; verifiable parental consent before collecting PII; parental access and deletion; no behavioural advertising; data retention only as long as needed; privacy notice specific to children.

### FERPA (US education records)
- Education records only accessible to school officials with legitimate interest; written consent before disclosure; "school official" exception documented in contract if acting for an institution; parents/eligible students can inspect and request amendment; directory information opt-out honoured.

### GLBA (US financial)
- Written information security programme with a qualified individual; risk assessment; encryption; MFA; access controls; change management; monitoring; incident response plan; board reporting; notice to FTC of breaches affecting 500+ (Safeguards Rule).

### PHIPA (Ontario health)
- Health information custodian or agent status determined; consent model (implied for circle of care, express otherwise); access logs; breach notification to the IPC and individuals; privacy impact assessment.

### DTAC (NHS digital health)
- Clinical safety (DCB0129/DCB0160 hazard log and clinical safety officer); data protection (DPIA, UK GDPR); technical security (Cyber Essentials, pen test, MFA); interoperability (NHS standards, FHIR where relevant); usability and accessibility (WCAG 2.2 AA).

---

## AI set (NIST AI RMF, ISO 42001, EU AI Act)

| ID | Control |
|---|---|
| AI-01 | Inventory of AI systems and models in use, including third-party APIs, with purpose and risk tier |
| AI-02 | Risk classification under EU AI Act (unacceptable / high / limited / minimal); high-risk triggers conformity assessment |
| AI-03 | Transparency: users told when they interact with AI or AI-generated content; limitations documented |
| AI-04 | Data governance: training and prompt data sources, consent, PII handling, retention; no PII sent to model providers without a DPA |
| AI-05 | Human oversight: a person can override or stop automated decisions with legal or significant effect |
| AI-06 | Evaluation: accuracy, bias and robustness tests before release and on change; results stored |
| AI-07 | Prompt-injection and output-handling controls: untrusted content isolated, tool calls constrained, outputs validated before action |
| AI-08 | Logging: prompts, outputs and decisions logged for incidents and audits (with PII minimised) |
| AI-09 | Incident process for AI failures (harmful output, data leak via model) |
| AI-10 | Model and prompt versioning; rollback path |

---

## Writing a custom framework

If the user needs a framework not covered: ask for the control list or the regulator's document, extract 10–30 engineering-relevant controls, assign `CUSTOM-<name>-01…` IDs, and store them in the same table shape. Note the source document and date in the framework header.
