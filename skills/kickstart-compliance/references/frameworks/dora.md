---
id: dora
name: DORA
official_name: Regulation (EU) 2022/2554 of the European Parliament and of the Council of 14 December 2022 on digital operational resilience for the financial sector and amending Regulations (EC) No 1060/2009, (EU) No 648/2012, (EU) No 600/2014, (EU) No 909/2014 and (EU) 2016/1011
governing_body: European Parliament and Council of the EU (legislator); European Commission (delegated/implementing acts drafted by the ESAs - EBA, EIOPA, ESMA); enforced by national competent authorities and, for critical ICT third-party providers, the ESA Lead Overseers
type: security
legal_status: law
region: EU (financial entities established in the Union); ICT third-party service providers designated as critical come under the EU oversight framework
industry: finance
current_version: Regulation (EU) 2022/2554, in force 16 January 2023; applies from 17 January 2025 (Art. 64)
superseded_by: none
official_sources:
  - title: European Commission (DG FISMA), Cyber resilience / DORA policy page
    url: https://finance.ec.europa.eu/digital-finance/cyber-resilience_en
    accessed: 2026-11-06
  - title: European Commission (DG FISMA), Implementing and delegated acts - DORA
    url: https://finance.ec.europa.eu/regulation-and-supervision/financial-services-legislation/implementing-and-delegated-acts/digital-operational-resilience-regulation_en
    accessed: 2026-11-06
  - title: "Implementing and Delegated Acts on Regulation (EU) 2022/2554 - full list (PDF, 2 July 2025)"
    url: https://finance.ec.europa.eu/document/download/7a2d42d8-4b48-4e2e-9b4c-c4e9107686d1_en?filename=dora-level-2-measures-full_en.pdf
    accessed: 2026-11-06
  - title: Regulation (EU) 2022/2554, Official Journal text (Publications Office of the EU, CELEX 32022R2554)
    url: https://publications.europa.eu/resource/cellar/0caf473a-85bd-11ed-9887-01aa75ed71a1.0006.03/DOC_1
    accessed: 2026-11-06
  - title: Commission Delegated Regulation (EU) 2025/301, Official Journal text (Publications Office of the EU, CELEX 32025R0301)
    url: https://publications.europa.eu/resource/cellar/36795cde-ef2b-11ef-981b-01aa75ed71a1.0006.03/DOC_1
    accessed: 2026-11-06
  - title: ESMA, Digital Operational Resilience Act (DORA) page
    url: https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora
    accessed: 2026-11-06
  - title: ESAs Joint Statement on DORA application (JC 2024 99, 4 December 2024)
    url: https://www.esma.europa.eu/sites/default/files/2024-12/JC_2024_99_ESAs_Statement_on_DORA_application.pdf
    accessed: 2026-11-06
  - title: ESAs Final Report on draft RTS and ITS on content, format, timelines and procedures for reporting major incidents and significant cyber threats (JC 2024 33, 17 July 2024)
    url: https://www.esma.europa.eu/sites/default/files/2024-07/JC_2024-33_-_Final_report_on_the_draft_RTS_and_ITS_on_incident_reporting.pdf
    accessed: 2026-11-06
  - title: EBA Interactive Single Rulebook, DORA article index (article titles only; text links to EUR-Lex)
    url: https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/17716
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
DORA is the EU's framework on digital operational resilience for the financial sector. The Commission describes it as strengthening "companies' ability to prevent incidents and also to minimise disruptions and ensure a swift recovery after ICT-related incidents". It "also includes an oversight mechanism on service providers, such as Big Techs, which provide cloud computing services to financial institutions" (DG FISMA cyber-resilience page). The details sit in Level 2 RTS and ITS adopted by the Commission.

## Who it applies to
- Art. 2(1)(a)-(t) "financial entities" (Art. 2(2)): credit institutions; payment institutions (incl. exempted); account information service providers; e-money institutions (incl. exempted); investment firms; crypto-asset service providers; CSDs; CCPs; trading venues; trade repositories; AIFMs; management companies; data reporting service providers; insurance and reinsurance undertakings; insurance, reinsurance and ancillary insurance intermediaries; IORPs; credit rating agencies; administrators of critical benchmarks; crowdfunding service providers; securitisation repositories. Art. 2(1)(u): ICT third-party service providers.
- Exclusions (Art. 2(3)) include AIFMs under Art. 3(2) AIFMD, small Solvency II undertakings under Art. 4 of Directive 2009/138/EC, IORPs whose schemes "together do not have more than 15 members in total", MiFID-exempt persons, insurance intermediaries that are micro/small/medium enterprises, and post office giro institutions. Member States may exclude entities under Art. 2(5)(4)-(23) CRD (Art. 2(4)).
- ICT third-party providers designated as critical: the criteria are in Commission Delegated Regulation (EU) 2024/1502 (legal basis Art. 31(6)), per the Commission's Level 2 list.

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| DORA-01 | ICT risk management framework with tools, methods, processes and policies; a simplified framework for eligible entities | Art. 15, 16; Delegated Reg. (EU) 2024/1774 |
| DORA-02 | Classify ICT-related incidents and cyber threats against materiality thresholds | Art. 18; Delegated Reg. (EU) 2024/1772 |
| DORA-03 | Report major ICT-related incidents (initial notification, intermediate and final reports) with the content and time limits set in the RTS | Art. 19, 20(3); Delegated Reg. (EU) 2025/301 |
| DORA-04 | Use the standard forms, templates and procedures to report major incidents and to notify significant cyber threats voluntarily | Art. 20(4); Implementing Reg. (EU) 2025/302 |
| DORA-05 | Threat-led penetration testing (TLPT) for the financial entities identified under the RTS criteria, covering scope, methodology, internal testers, remediation and mutual recognition | Art. 26(11); Delegated Reg. (EU) 2025/1190 |
| DORA-06 | Maintain the register of information on all ICT third-party contractual arrangements using the standard templates | Art. 28(9); Implementing Reg. (EU) 2024/2956 |
| DORA-07 | Policy on contractual arrangements for ICT services supporting critical or important functions | Art. 28(10); Delegated Reg. (EU) 2024/1773 |
| DORA-08 | Assess subcontracting of ICT services that support critical or important functions | Art. 30(5); Delegated Reg. (EU) 2025/532 |
| DORA-09 | Critical ICT third-party providers: cooperate with Lead Overseer oversight activities | Art. 41(2); Delegated Regs. (EU) 2025/295 and 2025/420 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Entry into force | "16 January 2023 Entry into force - Digital operational resilience (DORA) The Digital Operational Resilience Regulation (DORA) came into force." | DG FISMA cyber-resilience page |
| OJ publication | 27 December 2022 | DG FISMA cyber-resilience page (policy timeline) |
| Application date | "It shall apply from 17 January 2025." No transitional period ("DORA does not provide for a transitional period") | Art. 64; ESAs statement JC 2024 99 para. 2 |
| Register of information to ESAs | competent authorities report registers "to the ESAs by 30 April 2025" | ESAs statement JC 2024 99 |
| Major incident: initial notification | "as early as possible, but in any case, within four hours from the classification of the ICT-related incident as a major ICT-related incident and no later than 24 hours from the moment the financial entity has become aware"; if classified major after 24 h, "within four hours from the classification" | Delegated Reg. (EU) 2025/301 Art. 5(1)(a), 5(2); DORA Art. 19(4)(a) |
| Major incident: intermediate report | "at the latest within 72 hours from the submission of the initial notification"; updated report "without undue delay, and in any case when the regular activities have been recovered" | Delegated Reg. (EU) 2025/301 Art. 5(1)(b) |
| Major incident: final report | "no later than one month after either the submission of the intermediate report, or, where applicable, after the latest updated intermediate report" | Delegated Reg. (EU) 2025/301 Art. 5(1)(c) |
| Weekend/holiday relief | may submit "by noon of the next working day"; not for initial/intermediate reports of credit institutions, CCPs, trading venue operators and NIS2 essential/important entities; authorities may also disapply it for significant/systemic entities | Delegated Reg. (EU) 2025/301 Art. 5(4)-(6) |

## Assessment and certification
No certification. National competent authorities supervise compliance (ESAs' Lead Overseers for critical ICT third-party providers). TLPT is required only for the financial entities identified under Delegated Reg. (EU) 2025/1190, and its results support mutual recognition between authorities.

## Notes
- **Source caveat (updated in follow-up pass):** eur-lex.europa.eu still returns an AWS WAF challenge. The Regulation and Delegated Reg. (EU) 2025/301 were read instead from the Official Journal XHTML served by the EU Publications Office (publications.europa.eu cellar, resolved from the CELEX number). These are the texts as published in the OJ, not consolidated versions; no DORA amendment was found on the Commission page. The ESAs' final draft RTS (JC 2024 33, Art. 6) matches the adopted Art. 5 except numbering and minor wording.
- **Catalog check:** framework-catalog.md line 21 ("EU financial entities and their critical ICT providers") is consistent with the Commission page. control-checklists.md "DORA 4h initial" is incomplete: the commonly cited rule is 4 hours from classification and no later than 24 hours from awareness (confirmed in Delegated Reg. (EU) 2025/301 Art. 5(1)(a)). It should cite Delegated Reg. (EU) 2025/301.
- Correct instrument numbers (from the Commission list): incident content and time limits are **Delegated Regulation (EU) 2025/301 of 23 October 2024**; reporting templates are **Implementing Regulation (EU) 2025/302**; incident classification is **Delegated Regulation (EU) 2024/1772**; the register of information is **Implementing Regulation (EU) 2024/2956**; TLPT is **Delegated Regulation (EU) 2025/1190**.
- Recent official activity: on 9 January 2026 the Commission sent a letter under Art. 58(3) on whether statutory auditors should be subject to DORA requirements (DG FISMA page). No amendment to DORA was announced.
