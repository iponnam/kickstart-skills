---
id: easa
name: EASA software, hardware and information security requirements
official_name: EASA AMC 20-115D (Airborne Software Development Assurance Using EUROCAE ED-12 and RTCA DO-178), AMC 20-152A (Development Assurance for Airborne Electronic Hardware), AMC 20-189 (Management of Open Problem Reports), and Part-IS (Commission Delegated Regulation (EU) 2022/1645 and Commission Implementing Regulation (EU) 2023/203) on information security risks with a potential impact on aviation safety
governing_body: European Union Aviation Safety Agency (EASA) (AMC and GM by ED Decision); European Commission (Part-IS regulations); enforced by EASA and national competent authorities
type: sector
legal_status: binding-regulation
region: EU/EASA Member States; applies to products certified by EASA and to approved organisations; third-country applicability depends on bilateral agreements (EASA Part-IS FAQ)
industry: aviation
current_version: AMC 20-115D (ED Decision 2017/020/R); AMC 20-152A (ED Decision 2020/010/R); Part-IS Delegated Reg. (EU) 2022/1645 applicable 16 Oct 2025 (amended by Delegated Reg. (EU) 2025/22) and Implementing Reg. (EU) 2023/203 applicable 22 Feb 2026; AMC & GM to Part-IS Issue 1, Amendment 1 (ED Decisions 2025/013/R, 2025/014/R, 2025/015/R, 24 Jul 2025)
superseded_by: none
official_sources:
  - title: EASA Easy Access Rules for Acceptable Means of Compliance for Airworthiness of Products, Parts and Appliances (AMC-20) - AMC 20-115D text
    url: https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-acceptable-means?page=22
    accessed: 2026-11-06
  - title: EASA Easy Access Rules (AMC-20) - AMC 20-152A text
    url: https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-acceptable-means?page=25
    accessed: 2026-11-06
  - title: EASA Easy Access Rules (AMC-20) - Subpart B list of AMC-20 items
    url: https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-acceptable-means?page=29
    accessed: 2026-11-06
  - title: EASA FAQ - Information Security (Part-IS)
    url: https://www.easa.europa.eu/en/the-agency/faqs/information-security-part
    accessed: 2026-11-06
  - title: EASA Domains - Cybersecurity (Part-IS ED Decisions list)
    url: https://www.easa.europa.eu/en/domains/cybersecurity
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
- **AMC 20-115D** "describes an acceptable means, but not the only means, for showing compliance with the applicable airworthiness regulations with regard to the software aspects of airborne systems and equipment in the domain of product certification or European technical standard orders (ETSOs) authorisation". It recognises EUROCAE ED-12C / RTCA DO-178C and its supplements.
- **AMC 20-152A** does the same "for the electronic hardware aspects", recognising EUROCAE ED-80 / RTCA DO-254 and adding guidance for custom devices, including COTS IP.
- **Part-IS** requires covered organisations and authorities to manage information security risks with a potential impact on aviation safety through an ISMS. EASA says it is "in most parts consistent and aligned with ISO/IEC 27001" but adds aviation-safety-specific provisions (Part-IS FAQ).

## Who it applies to
- AMC 20-115D / 20-152A: applicants for product certification or ETSO authorisation whose airborne systems contain software or custom electronic hardware (AMC 20-115D s. 1(a); AMC 20-152A s. 1.1).
- Part-IS Delegated Reg. (EU) 2022/1645: "production organisations and design organisations subject to Subparts G and J of Section A of Annex I (Part 21) to Regulation (EU) No 748/2012, except design and production organisations that are solely involved in the design and/or production of ELA2 aircraft", and aerodrome operators (Part-IS FAQ).
- Part-IS Implementing Reg. (EU) 2023/203: among others, "maintenance organisations subject to Section A of Annex II (Part-145) ... continuing airworthiness management organisations (CAMOs)", air operators, ATM/ANS and other approved and declared organisations, plus competent authorities (Part-IS FAQ). The full list was not transcribed.
- Derogation: an organisation that "does not pose any information security risk with a potential impact on aviation safety" may request approval for a derogation (GM1 IS.D.OR.200(e), quoted in Part-IS FAQ).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| AMC 20-115D 1(b) | Develop airborne software under ED-12C/DO-178C, plus ED-215/DO-330 (tool qualification), ED-216/DO-333 (formal methods), ED-217/DO-332 (OOT) and ED-218/DO-331 (model-based) as applicable | AMC 20-115D s. 1(b), 1(d) |
| AMC 20-115D 1(c) | Use ED-94C/DO-248C as supporting information (FAQs and discussion papers) | AMC 20-115D s. 1(c) |
| AMC 20-115D | Satisfy "all of the objectives associated with the software level assigned to the software" and produce the associated life cycle data per the ED-12C/DO-178C Annex A tables | AMC 20-115D |
| AMC 20-115D | Assign software levels per the system safety assessment. Applicable product AMC on criticality-to-level relationships "takes precedence over the application of Section 2.3 of ED-12C/DO-178C" | AMC 20-115D |
| AMC 20-115D | Reusing legacy ED-12B/DO-178B processes: provide evidence of resolution and closure of all process-related open problem reports and audit/review findings | AMC 20-115D (s. on ED-12B processes) |
| AMC 20-115D | Make life cycle data available to EASA on request; design description and source code are part of type design data except for Level D | AMC 20-115D |
| AMC 20-152A 1.2 | Develop custom airborne electronic hardware per ED-80/DO-254 as supplemented by the AMC, modulating life cycle data by the hardware DAL (Appendix A) | AMC 20-152A s. 1.2–1.3, s. 5 |
| AMC 20-152A 5.11 | COTS IP used in custom devices: apply the specific guidance | AMC 20-152A s. 5.11 |
| AMC 20-152A | Classify devices as simple or complex using the AMC criteria | AMC 20-152A |
| AMC 20-189 | Manage open problem reports (OPRs) per AMC 20-189 | AMC-20 Subpart B list |
| IS.OR.205 | Carry out an information security risk assessment to determine which elements and assets fall within the ISMS scope | Part-IS IS.OR.205 (Part-IS FAQ) |
| IS.I.OR.200 / IS.D.OR.200 | Establish and maintain an ISMS. An existing ISO/IEC 27001 ISMS can be adapted, but aviation safety must be included in risk management (mapping in Appendix II of the AMC & GM) | Part-IS (Part-IS FAQ) |
| IS.I.OR.215 / IS.D.OR.215; IS.I.OR.230 / IS.D.OR.230 | Internal reporting scheme, and external reporting of information security incidents with potential impact on aviation safety; the reporting tool is at the organisation's discretion | Part-IS (Part-IS FAQ) |
| IS.OR.230 | Even where an entity is covered by the national aviation security programme (Reg. 2015/1998 point 1.7), "point IS.OR.230 needs to be complied with" | Part-IS FAQ |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Part-IS applicability, Delegated Reg. (EU) 2022/1645 | "organisations within the scope of Delegated Regulation (EU) 2022/1645 have to comply with it by 16 October 2025" | EASA Part-IS FAQ |
| Part-IS applicability, Implementing Reg. (EU) 2023/203 | "applicable from 22 February 2026" | EASA Part-IS FAQ |
| External incident reporting time limit | UNVERIFIED (commonly cited as 72 hours under IS.I.OR.230/IS.D.OR.230; not found on the pages read) | IS.I.OR.230 / IS.D.OR.230 |
| AMC 20-115D adoption | ED Decision 2017/020/R | EASA Easy Access Rules AMC-20 |
| AMC 20-152A adoption | ED Decision 2020/010/R | EASA Easy Access Rules AMC-20 |
| Recognised standards dates | ED-12C 1 January 2012 / DO-178C 13 December 2011; ED-80 April 2000 / DO-254 19 April 2000 | AMC 20-115D s. 1(b); AMC 20-152A s. 1.2 |

## Assessment and certification
Software and hardware compliance is shown to EASA within type certification or ETSO authorisation. The applicant submits plans and life cycle data, and EASA determines its level of involvement. Part-IS compliance "will be verified by the competent authority that is identified in Article 6 of the Implementing Regulation and Article 5 of the Delegated Regulation" (Part-IS FAQ). ISO/IEC 27001 certification does not replace Part-IS compliance (Part-IS FAQ).

## Notes
- **Catalog check:** framework-catalog.md line 39 ("EASA (software and firmware validation)", type security/quality, audit certification) is vague. EASA software and hardware assurance is a means of compliance within product certification, not a standalone certificate. Part-IS (information security) is a separate, binding organisational requirement with applicability dates 16 Oct 2025 and 22 Feb 2026. The repo should name AMC 20-115D (ED-12C/DO-178C), AMC 20-152A (ED-80/DO-254) and Part-IS explicitly.
- Delegated Reg. (EU) 2022/1645 "has been amended by Delegated Regulation (EU) 2025/22, while the amendment of Implementing Regulation (EU) 2023/203 is currently pending" (Part-IS FAQ).
- EASA "is working with the European Commission to have Part-IS compliance 'credited' in the context of NIS 2 compliance" (Part-IS FAQ). NIS2 compliance does not automatically mean Part-IS compliance.
- **UNVERIFIED:** the Part-IS external-reporting time limit and the exact text of the IS.I.OR/IS.D.OR points. The regulation texts are on EUR-Lex (unreachable), and the AMC & GM PDFs were not downloaded.
