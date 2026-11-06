---
id: phipa
name: PHIPA
official_name: Personal Health Information Protection Act, 2004, S.O. 2004, c. 3, Sched. A; O. Reg. 329/04 (General)
governing_body: Legislative Assembly of Ontario; enforced by the Information and Privacy Commissioner of Ontario (IPC)
type: privacy
legal_status: law
region: Ontario, Canada
industry: health (health information custodians, their agents, electronic service providers and health information network providers)
current_version: Act consolidation period from January 1, 2026 (e-Laws currency date November 3, 2026); O. Reg. 329/04 consolidation from October 31, 2026
superseded_by: none
official_sources:
  - title: Personal Health Information Protection Act, 2004 (Ontario e-Laws)
    url: https://www.ontario.ca/laws/statute/04p03
    accessed: 2026-11-06
  - title: O. Reg. 329/04 General (Ontario e-Laws)
    url: https://www.ontario.ca/laws/regulation/040329
    accessed: 2026-11-06
  - title: IPC - Report a health privacy breach
    url: https://www.ipc.on.ca/en/health-organizations/report-a-privacy-breach
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
Ontario's health privacy statute. It governs collection, use and disclosure of personal health information (PHI) by health information custodians, sets consent rules, security, breach notice to individuals and the IPC, access and correction rights, and offences and administrative penalties.

## Who it applies to
Health information custodians as defined in s.3(1) (e.g. health care practitioners, group practices, health service providers and other listed persons with custody or control of PHI from their health work), their agents, and recipients of PHI. s.10(4): "A person who provides goods or services for the purpose of enabling a health information custodian to use electronic means to collect, use, modify, disclose, retain or dispose of personal health information shall comply with the prescribed requirements"; O. Reg. 329/04 s.6 sets those requirements, including for health information network providers.

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| PHIPA-12.1 | Reasonable steps to protect PHI against theft, loss, unauthorized use/disclosure, and records against unauthorized copying, modification or disposal | s.12(1) |
| PHIPA-12.2 | Notify individuals "at the first reasonable opportunity" of theft, loss or unauthorized use/disclosure, stating their right to complain to the IPC | s.12(2) |
| PHIPA-12.3 | Notify the IPC when one of the seven prescribed circumstances applies (unauthorized use by someone who knew, theft, further use after breach, pattern, College notice events (2), significant breach) | s.12(3); O. Reg. 329/04 s.6.3(1) |
| PHIPA-13 | Retain, transfer and dispose of records securely; keep records subject to an access request until recourse is exhausted | s.13(1)-(2) |
| PHIPA-10.1 | Electronic audit log of every view, handling or modification of PHI (type, date/time, identity of users and of the individual); audit and monitor; give to IPC on request. NOT YET IN FORCE: added "on a day to be named by proclamation" | s.10.1 (2020, c. 5, Sched. 6, s. 3) |
| PHIPA-15 | Non-natural-person custodians designate a contact person | s.15(2) |
| PHIPA-16 | Publish a written public statement of information practices and access/complaint routes | s.16(1) |
| PHIPA-17.1 | Report to the relevant College within 30 days on discipline/termination of members for privacy breaches | s.17.1 |
| PHIPA-54 | Respond to access requests within 30 days (extendable) | s.54(2)-(3) |
| PHIPA-EHR | Notify individual (and IPC where prescribed) of unauthorized collection via the electronic health record | s.55.5(7)(a)-(b) (per IPC page); O. Reg. 329/04 s.6.4(1) item 5 |
| REG-6(3) | Health information network providers: notify each custodian at first reasonable opportunity of unauthorized access/use; give plain-language description of services and safeguards; publish it | O. Reg. 329/04 s.6(3) |
| REG-6.4 | Annual statistical report to the IPC of thefts, losses, unauthorized uses and disclosures, and unauthorized EHR collections, by the IPC's electronic means | O. Reg. 329/04 s.6.4 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Breach notification to IPC | "at the first reasonable opportunity" | O. Reg. 329/04 s.6.3(3) |
| Notification to individuals | "at the first reasonable opportunity" | s.12(2)(a) |
| Annual breach statistics to IPC | "On or before March 1 in each year starting in 2019", covering the previous calendar year | O. Reg. 329/04 s.6.4(1) |
| Access request response | "no later than 30 days after receiving the request" | s.54(2) |
| Notice to College | within "30 days of the event occurring" | s.17.1 |
| Offence fines | natural person "not more than $200,000 or ... imprisonment of not more than 1 year, or ... both"; other persons "not more than $1,000,000" | s.72(2) |
| Administrative penalties (IPC) | max "$50,000" (natural person) / "$500,000" (other) | s.61.1; O. Reg. 329/04 s.35(1) |

## Assessment and certification
No certification. IPC receives breach reports and annual statistics, investigates complaints, issues orders and administrative penalties (Part VI, s.61, 61.1).

## Notes
- Checklist PHIPA line ("consent model; access logs; breach notification to the IPC and individuals; privacy impact assessment") needs correction: the electronic audit log duty (s.10.1) is not yet proclaimed in force; a privacy impact assessment is not a general statutory duty for custodians in the text reviewed (UNVERIFIED whether any regulation requires one for specific actors); the annual March 1 statistical report to the IPC is missing from the checklist.
- Catalog row is otherwise correct.
