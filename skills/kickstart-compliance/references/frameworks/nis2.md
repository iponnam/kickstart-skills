---
id: nis2
name: NIS 2 Directive
official_name: Directive (EU) 2022/2555 of the European Parliament and of the Council of 14 December 2022 on measures for a high common level of cybersecurity across the Union (NIS 2 Directive)
governing_body: European Parliament and Council of the EU (legislator); European Commission (implementing acts); enforced by Member State competent authorities under national transposition laws
type: security
legal_status: law
region: EU (through national transposition); jurisdiction is generally the Member State of establishment, with exceptions for electronic communications, public administration and certain digital providers
industry: energy, transport, banking, financial market infrastructure, health, water, digital infrastructure, ICT service management, public administration, space, postal, waste, chemicals, food, manufacturing, digital providers, research
current_version: Directive (EU) 2022/2555, in force January 2023; transposition deadline 17 October 2024; NIS1 repealed from 18 October 2024
superseded_by: none (targeted amendments proposed 20 January 2026, COM(2026) 13, not adopted)
official_sources:
  - title: European Commission, NIS2 Directive - securing network and information systems
    url: https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
    accessed: 2026-11-06
  - title: European Commission, NIS2 Directive - FAQs
    url: https://digital-strategy.ec.europa.eu/en/revision-network-and-information-security-directive-questions-and-answers
    accessed: 2026-11-06
  - title: European Commission, Proposal for a Directive on simplification measures and alignment with the Cybersecurity Act (COM(2026) 13)
    url: https://digital-strategy.ec.europa.eu/en/library/proposal-directive-regards-simplification-measures-and-alignment-cybersecurity-act
    accessed: 2026-11-06
  - title: Directive (EU) 2022/2555, Official Journal text (Publications Office of the EU, CELEX 32022L2555)
    url: https://publications.europa.eu/resource/cellar/9b84d482-85bd-11ed-9887-01aa75ed71a1.0006.03/DOC_1
    accessed: 2026-11-06
  - title: Commission Implementing Regulation (EU) 2024/2690, Official Journal text (Publications Office of the EU, CELEX 32024R2690)
    url: https://publications.europa.eu/resource/cellar/28f15de8-8ce9-11ef-a130-01aa75ed71a1.0006.03/DOC_1
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
NIS2 "establishes a unified legal framework to uphold cybersecurity in 18 critical sectors across the EU". It replaced Directive 2016/1148 (NIS1). It requires Member States to adopt national cybersecurity strategies, CSIRTs and competent authorities. Entities must take cybersecurity risk-management measures and notify significant incidents. Top management is accountable (Commission NIS2 page).

## Who it applies to
- "As a rule, medium-sized and large entities in these critical sectors" (Commission NIS2 page). The Directive introduces "a clear size threshold rule - meaning that all medium and large-sized companies in selected sectors will be included", and Member States may add smaller high-risk entities (FAQ).
- Two categories, essential and important entities, "subjected to different supervisory regime" (FAQ).
- Sectors of high criticality (Annex I): energy, transport, banking, financial market infrastructures, health, drinking water, waste water, digital infrastructure (IXPs, DNS, TLD registries, cloud, data centres, CDNs, trust services, public electronic communications), ICT service management (MSPs, MSSPs), public administration, space (FAQ).
- Other critical sectors (Annex II): postal and courier, waste management, chemicals, food, manufacturing (medical devices, computers and electronics, machinery, motor vehicles, other transport equipment), digital providers (online marketplaces, search engines, social networks), research organisations (FAQ).
- Size rule (Art. 2(1)): entities of a type in Annex I or II "which qualify as medium-sized enterprises under Article 2 of the Annex to Recommendation 2003/361/EC, or exceed the ceilings for medium-sized enterprises", and which provide services or carry out activities in the Union. Art. 2(2) adds entities "regardless of their size" (e.g. public electronic communications providers, trust service providers, TLD registries and DNS providers, sole providers of a critical service, public administration).
- Essential entities (Art. 3(1)): Annex I entities exceeding the medium-sized ceilings; qualified trust service providers, TLD registries and DNS service providers "regardless of their size"; medium-sized public electronic communications providers; central public administration (Art. 2(2)(f)(i)); others identified by Member States; critical entities under Directive (EU) 2022/2557. All other Annex I/II entities in scope are important entities (Art. 3(2)).
- Member States had to list essential and important entities "By 17 April 2025" and review the list "at least every two years thereafter" (Art. 3(3)); entities must supply name, address and contact details "including email addresses, IP ranges and telephone numbers" and sector (Art. 3(4)).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| Art. 21 | "appropriate and proportionate technical, operational and organisational measures", "based on an all-hazards approach", including at least the ten elements below | Art. 21(1)-(2) |
| Art. 21(2)(a) | "policies on risk analysis and information system security" | Art. 21(2)(a) |
| Art. 21(2)(b) | "incident handling" | Art. 21(2)(b) |
| Art. 21(2)(c) | "business continuity, such as backup management and disaster recovery, and crisis management" | Art. 21(2)(c) |
| Art. 21(2)(d) | "supply chain security, including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers" | Art. 21(2)(d) |
| Art. 21(2)(e) | "security in network and information systems acquisition, development and maintenance, including vulnerability handling and disclosure" | Art. 21(2)(e) |
| Art. 21(2)(f) | "policies and procedures to assess the effectiveness of cybersecurity risk-management measures" | Art. 21(2)(f) |
| Art. 21(2)(g) | "basic cyber hygiene practices and cybersecurity training" | Art. 21(2)(g) |
| Art. 21(2)(h) | "policies and procedures regarding the use of cryptography and, where appropriate, encryption" | Art. 21(2)(h) |
| Art. 21(2)(i) | "human resources security, access control policies and asset management" | Art. 21(2)(i) |
| Art. 21(2)(j) | "the use of multi-factor authentication or continuous authentication solutions, secured voice, video and text communications and secured emergency communication systems within the entity, where appropriate" | Art. 21(2)(j) |
| Art. 23 | Notify the CSIRT or competent authority of any "significant incident" without undue delay (early warning, incident notification, intermediate report on request, final report); communicate measures to service recipients affected by significant cyber threats | Art. 23(1), (2), (4) |
| Art. 23(3) | Significant = caused or capable of causing "severe operational disruption of the services or financial loss", or "considerable material or non-material damage" to others | Art. 23(3) |
| Art. 20 | Management bodies approve and oversee the measures and are liable ("accountability of the top management", Commission NIS2 page) | Art. 20 |
| IR 2024/2690 | DNS, TLD, cloud, data centre, CDN, MSP, MSSP, online marketplace, search engine, social network and trust service providers: implement the technical and methodological requirements in the Annex (based on standards "such as ISO/IEC 27001, ISO/IEC 27002") | IR 2024/2690 Art. 1-2 and Annex |
| IR 2024/2690 Art. 3 | Significant-incident criteria for those providers, e.g. direct financial loss exceeding "EUR 500 000 or 5 % of the relevant entity's total annual turnover in the preceding financial year, whichever is lower"; suspectedly malicious unauthorised access capable of severe disruption; sector rules such as a cloud service "completely unavailable for more than 30 minutes" | IR 2024/2690 Art. 3(1), Art. 4, Art. 7 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Early warning | "without undue delay and in any event within 24 hours of becoming aware of the significant incident" | Art. 23(4)(a) |
| Incident notification | "without undue delay and in any event within 72 hours of becoming aware of the significant incident" | Art. 23(4)(b) |
| Final report | "not later than one month after the submission of the incident notification" | Art. 23(4)(d) |
| Transposition deadline | "Member States had until 17 October 2024 to transpose" | Commission NIS2 page |
| NIS1 repeal | "NIS 2 repealed NIS1 as from 18 October 2024" | Commission NIS2 page |
| Fines, essential entities | "a maximum of at least EUR 10 000 000 or of a maximum of at least 2 % of the total worldwide annual turnover in the preceding financial year", whichever is higher | Art. 34(4) |
| Fines, important entities | "a maximum of at least EUR 7 000 000 or of a maximum of at least 1,4 % of the total worldwide annual turnover in the preceding financial year", whichever is higher | Art. 34(5) |
| Recurring incidents (IR 2024/2690 providers) | treated as one significant incident if "at least twice within 6 months", same root cause, and together meet the financial-loss criterion | IR 2024/2690 Art. 4 |
| First Commission review | "by 17 October 2027" | Commission FAQ |

## Assessment and certification
No EU certificate. Competent authorities supervise, using "regular and targeted audits, on-site and off-site checks, request of information, and access to documents or evidence". Essential entities are supervised ex ante and important entities ex post ("differentiation of supervisory regimes", FAQ). Member States may require entities "to use particular ICT products, ICT services and ICT processes" certified under European cybersecurity certification schemes to demonstrate compliance with Art. 21 (Art. 24(1)); the Commission may specify categories by delegated act (Art. 24(2)).

## Notes
- **Source caveat (updated in follow-up pass):** eur-lex.europa.eu still returns an AWS WAF challenge. The Directive and Implementing Regulation (EU) 2024/2690 were read from the Official Journal XHTML served by the EU Publications Office (publications.europa.eu cellar, resolved from the CELEX number). These are the texts as published, not consolidated versions; no adopted amendment is known (COM(2026) 13 is a proposal). National transposition laws were not reviewed.
- **Catalog check:** framework-catalog.md line 22 is consistent. control-checklists.md "NIS 2 24h early warning" is correct (Commission FAQ). It should add the 72 h notification and one-month final report.
- **Pending (proposal, not adopted):** on 20 January 2026 the Commission proposed targeted amendments to NIS2 (COM(2026) 13) to "simplify jurisdictional rules, streamline the collection of data on ransomware attacks and facilitate the supervision of cross-border entities". The Commission says this will ease compliance for 28,700 companies. The Digital Omnibus (Nov 2025, proposal) adds a single-entry point for incident reporting.
- Commission guidelines exist on Art. 3(4), Art. 4(1)–(2) and Art. 34 (links on the Commission NIS2 page); they were not read.
