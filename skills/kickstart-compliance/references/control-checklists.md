# Cross-framework control groups

Many frameworks ask for the same engineering work. This file groups that work so one implementation can satisfy several frameworks at once.

This file deliberately contains **no deadlines, thresholds, versions or penalties**. Those live only in each framework's record in `frameworks/<id>.md`, which cites the official source and is re-verified under the freshness rule. When building `.kickstart/compliance.md`, take each framework's rows and numbers from its record, then use the groups below to point several rows at the same evidence.

## Security programme group

Typical sources: ISO/IEC 27001, SOC 2, NIST CSF, CIS Controls, Cyber Essentials, Essential Eight, NCA ECC, SAMA CSF, MAS TRM, RBI, SEBI CSCRF, IRDAI, NYDFS 500, NIS 2, DORA, HITRUST, CMMC, NIST SP 800-53 and 800-171.

| Group ID | Engineering work | One piece of evidence can cover |
|---|---|---|
| SEC-ASSETS | Inventory of systems, repos, data stores and third-party services, each with an owner | Asset or inventory controls in most security frameworks |
| SEC-RISK | Risk register with likelihood, impact, owner and treatment; reviewed on the cadence the selected records require | Risk assessment controls |
| SEC-ACCESS | SSO or MFA for production and code access; least privilege; periodic access review; joiner, mover and leaver process | Access control, identity, privileged access controls |
| SEC-CHANGE | All production changes through reviewed pull requests with CI passing; protected default branch | Change management, secure development |
| SEC-SDLC | Lint, SAST, dependency scanning and secret scanning in CI (installed by `kickstart-guardrails`) | Secure development, vulnerability management |
| SEC-VULN | Patch and vulnerability fix timelines; scheduled scans and penetration tests at the cadence the selected records require | Vulnerability management, VAPT clauses |
| SEC-CRYPTO | TLS in transit, encryption at rest for data stores and backups, managed keys | Cryptography controls |
| SEC-LOG | Centralised, structured logs; retention set to the longest period any selected record requires; clocks synchronised; alerts | Logging, monitoring, audit trail controls |
| SEC-BACKUP | Automated backups, tested restores, documented recovery objectives | Backup, continuity, resilience controls |
| SEC-IR | Incident response runbook with severity levels and a notification table: every regulator, deadline and channel from the selected records | Incident management and reporting clauses |
| SEC-CONTINUITY | Single points of failure identified; failover or accepted downtime documented | Business continuity, operational resilience |
| SEC-VENDOR | Register of third parties with data access, their assurance reports, and contract status | Supplier, outsourcing, ICT third-party risk |
| SEC-AWARE | Security onboarding and periodic refresher training, with a log | Awareness and training |
| SEC-POLICY | Information security, acceptable use, access control, data classification and retention policies, approved and reviewed | Policy and governance controls |
| SEC-ENDPOINT | Disk encryption, screen lock, automatic updates and malware protection on staff devices | Endpoint and device controls |
| SEC-CONFIG | Hardened images, no default credentials, infrastructure as code reviewed | Secure configuration baselines |
| SEC-GOV | Named security owner; security metrics reviewed by leadership | Governance, management review, board reporting |

## Privacy group

Typical sources: GDPR, UK GDPR, DPDPA, CCPA/CPRA and other US state laws, PIPEDA, Law 25, PDPA Singapore, LGPD, POPIA, APPI, Australia Privacy Act, Saudi PDPL, NDPA, Kenya DPA, Seychelles DPA and others.

| Group ID | Engineering work | One piece of evidence can cover |
|---|---|---|
| PRIV-ROPA | Record of processing: data, purpose, legal basis, retention, recipients, transfers | Records of processing, accountability |
| PRIV-CONSENT | Consent captured with timestamp and notice version; withdrawable as easily as given | Consent clauses |
| PRIV-NOTICE | Published privacy notice in the languages the selected records require | Notice and transparency clauses |
| PRIV-MINIMISE | Collect only required fields; schema review for unneeded personal data | Data minimisation, purpose limitation |
| PRIV-RIGHTS | Export, delete, correct and restrict, with a request log and the shortest response window among selected records | Data subject or principal rights |
| PRIV-RETENTION | Retention periods enforced by scheduled jobs; backups expire | Storage limitation, erasure |
| PRIV-BREACH | Breach assessment and notification procedure covering every authority, deadline and individual-notice rule in the selected records | Breach notification clauses |
| PRIV-TRANSFER | Processor contracts and the cross-border transfer mechanism each selected record requires | Processor and transfer clauses |
| PRIV-DPIA | Impact assessment for the high-risk processing each selected record defines | DPIA, PIA, risk assessment clauses |
| PRIV-CHILDREN | Age gating and parental consent at the age threshold set by each selected record | Children's data clauses |
| PRIV-TRACKING | Consent before non-essential cookies where required; opt-out links and signals where required | Cookie, sale and sharing clauses |
| PRIV-CONTACT | Named privacy contact, DPO or grievance officer where a selected record requires one | DPO and officer clauses |

When several selected laws set different numbers for the same thing, design to the strictest and record which law drives it.

## Sector groups

Use the record for each of these directly. They are specific enough that grouping adds little.

- **Payments:** `pci-dss`, plus `rbi-pa-pg` and `rbi-dpsc` in India.
- **Health:** `hipaa`, `phipa`, `dtac`, `hds`, `hitrust`.
- **Children and education:** `coppa`, `ferpa`.
- **US financial privacy:** `glba`.
- **Defence and government supply:** `cmmc`, `nist-800-171`, `nist-800-53`, `fedramp`.

## AI group

Typical sources: `eu-ai-act`, `iso-42001`, `nist-ai-rmf`.

| Group ID | Engineering work |
|---|---|
| AI-INVENTORY | Inventory of AI systems and models in use, including third-party APIs, with purpose and risk classification |
| AI-TRANSPARENCY | Users told when they interact with AI or AI-generated content; limitations documented |
| AI-DATA | Data sources, consent and personal data handling for training and prompts; processor terms with model providers |
| AI-OVERSIGHT | A person can override or stop automated decisions with significant effect |
| AI-EVAL | Accuracy, bias and robustness evaluation before release and on change, with stored results |
| AI-SAFETY | Prompt-injection and output-handling controls; untrusted content isolated; tool calls constrained; outputs validated before action |
| AI-LOG | Prompts, outputs and decisions logged for incident review, with personal data minimised |
| AI-VERSION | Model and prompt versioning with a rollback path |

Obligations, risk tiers and application dates come from each AI record, not from this table.

## Custom frameworks

If the user needs a framework with no record, research it from its official source using `frameworks/README.md`, or take the user's own control document. Assign `CUSTOM-<name>-01…` IDs and record the source document and date.
