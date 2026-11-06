---
id: eu-ai-act
name: EU AI Act
official_name: Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), as amended by Regulation (EU) 2026/1744 of 8 July 2026 (Digital Omnibus on AI; OJ L 24.7.2026, in force on the third day after publication)
governing_body: European Parliament and Council of the EU (legislator); European Commission AI Office (GPAI enforcement, guidance); Member State market surveillance authorities; AI Board
type: ai
legal_status: law
region: EU; applies to AI systems and GPAI models placed on the EU market or used in the EU ; Art. 2(1)(a) covers providers placing AI systems or GPAI models on the EU market "irrespective of whether those providers are established or located within the Union or in a third country", and Art. 2(1)(c) covers third-country providers and deployers "where the output produced by the AI system is used in the Union"
industry: any (ai)
current_version: Regulation (EU) 2024/1689, entered into force 1 August 2024, generally applicable from 2 August 2026; amended by Regulation (EU) 2026/1744 (in force 27 July 2026)
superseded_by: none
official_sources:
  - title: European Commission, AI Act - Shaping Europe's digital future (regulatory framework for AI)
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    accessed: 2026-11-06
  - title: European Commission, Digital Rulebook / Digital Omnibus page
    url: https://digital-strategy.ec.europa.eu/en/policies/digital-rulebook
    accessed: 2026-11-06
  - title: European Commission, Digital Omnibus on AI Regulation proposal (library page)
    url: https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal
    accessed: 2026-11-06
  - title: Regulation (EU) 2024/1689, Official Journal text as published (Publications Office of the EU, CELEX 32024R1689)
    url: https://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0006.03/DOC_1
    accessed: 2026-11-06
  - title: Regulation (EU) 2026/1744 (Digital Omnibus on AI), Official Journal text (Publications Office of the EU, CELEX 32026R1744)
    url: https://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The AI Act is "the first-ever comprehensive legal framework on AI worldwide". It sets "risk-based rules for AI developers and deployers regarding specific uses of AI". It "defines 4 levels of risk for AI systems": unacceptable risk (banned), high risk, transparency risk, and minimal or no risk. It adds separate rules for general-purpose AI (GPAI) models, including stricter ones for GPAI models with systemic risk (Commission AI Act page).

## Who it applies to
- Providers and deployers of AI systems, and providers of GPAI models (Commission AI Act page).
- High-risk AI covers safety components of products (Annex I) and use cases in sensitive areas (Annex III). The Commission lists critical infrastructure, education, employment and worker management, access to essential private and public services (e.g. credit scoring), remote biometric identification, emotion recognition and biometric categorisation, law enforcement, migration, asylum and border control, and administration of justice and democratic processes.
- Territorial and personal scope (Art. 2(1)): (a) providers placing AI systems or GPAI models on the Union market, wherever established; (b) deployers established or located in the Union; (c) third-country providers and deployers where the output "is used in the Union"; (d) importers and distributors; (e) product manufacturers placing an AI system on the market with their product under their own name; (f) authorised representatives of non-EU providers; (g) affected persons located in the Union.
- SME and SMC simplifications: Regulation (EU) 2026/1744 extends several SME measures to "small mid-cap enterprises" (SMCs), e.g. a new Art. 99(6a) capping SMC fines under Art. 99(4)-(5) at the lower of the amount or percentage. Role definitions in Art. 3 were not re-read in this pass (UNVERIFIED wording).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| Art. 5 | Do not place on the market or use prohibited practices. The Commission lists nine: harmful AI-based manipulation and deception; harmful exploitation of vulnerabilities; social scoring; individual criminal offence risk assessment or prediction; untargeted scraping to build facial recognition databases; emotion recognition in workplaces and education; biometric categorisation to deduce protected characteristics; real-time remote biometric identification for law enforcement in public spaces; AI generating non-consensual sexually explicit or intimate content or CSAM ("nudification"), the last added by the AI Omnibus | Art. 5 (as amended); Commission AI Act page |
| Art. 4 | AI literacy obligations (applicable from 2 Feb 2025) | Art. 4; Commission AI Act page (timeline) |
| Art. 9 | High-risk: "adequate risk assessment and mitigation systems" | Art. 9; Commission AI Act page |
| Art. 10 | High-risk: "high-quality of the datasets feeding the system to minimise risks of discriminatory outcomes" | Art. 10; Commission AI Act page |
| Art. 11 | High-risk: "detailed documentation providing all information necessary on the system and its purpose for authorities to assess its compliance" | Art. 11; Commission AI Act page |
| Art. 12 | High-risk: "logging of activity to ensure traceability of results" | Art. 12; Commission AI Act page |
| Art. 13 | High-risk: "clear and adequate information to the deployer" | Art. 13; Commission AI Act page |
| Art. 14 | High-risk: "appropriate human oversight measures" | Art. 14; Commission AI Act page |
| Art. 15 | High-risk: "high level of robustness, cybersecurity and accuracy" | Art. 15; Commission AI Act page |
| Art. 72 | Providers "establish and document a post-market monitoring system" proportionate to the risks, based on a post-market monitoring plan that is part of the Annex IV technical documentation | Art. 72(1), (3) |
| Art. 73 | Providers of high-risk AI systems report any serious incident to the market surveillance authorities of the Member State where it occurred; investigate, risk-assess and take corrective action | Art. 73(1), (6) |
| Art. 50 | Transparency: tell people they are interacting with an AI system (e.g. chatbots); make generative-AI output identifiable; label deep fakes and AI-generated text published to inform the public on matters of public interest | Art. 50; Commission AI Act page |
| Art. 53 | GPAI providers: transparency and copyright obligations; publish a public summary of training content using the Commission template | Art. 53; Commission AI Act page (GPAI section) |
| Art. 55 | GPAI models with systemic risk: "assess and mitigate those risks" | Art. 55; Commission AI Act page |
| Art. 43 | Conformity assessment before placing on the market: Annex III point 1 (biometrics) systems use internal control (Annex VI) or notified-body assessment (Annex VII), and must use Annex VII where harmonised standards/common specifications are not applied; Annex III points 2-8 use "internal control as referred to in Annex VI, which does not provide for the involvement of a notified body" | Art. 43(1)-(2) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Entry into force | "entered into force on 1 August 2024" | Commission AI Act page |
| General application | "became applicable on 2 August 2026, with some exceptions" | Commission AI Act page |
| Prohibitions and AI literacy | "prohibited AI practices and AI literacy obligations entered into application from 2 February 2025" (prohibitions 1–8) | Commission AI Act page |
| New prohibitions added by the AI Omnibus (Art. 5(1)(ba), (bb), 5(1a), (1b): AI generating non-consensual intimate or sexually explicit material of identifiable persons, and CSAM) | "shall apply from 2 December 2026" | Art. 113, third para., point (a) as replaced by Reg. (EU) 2026/1744 |
| Governance and GPAI obligations | "became applicable on 2 August 2025" | Commission AI Act page |
| Transparency rules (Art. 50) | "will come into effect in August 2026" | Commission AI Act page |
| High-risk, Annex III use cases (Art. 6(2)) | Chapter III Sections 1-3 apply from "2 December 2027" | Art. 113, third para., point (c)(i) as replaced by Reg. (EU) 2026/1744 |
| High-risk, Annex I regulated products (Art. 6(1)) | apply from "2 August 2028" | Art. 113, third para., point (c)(ii) as replaced by Reg. (EU) 2026/1744 |
| AI Omnibus entry into force | "on the third day following that of its publication" (OJ L 2026/1744 of 24.7.2026, i.e. 27 July 2026); Arts. 102-110 apply from 27 July 2026 | Reg. (EU) 2026/1744, final article; Art. 113(d) |
| Enforcement start | "From 2 August 2026, the AI Office and authorities of the Member States are responsible for implementing, supervising and enforcing the AI Act" | Commission AI Act page |
| Fines, prohibited practices | "up to EUR 35 000 000 or, if the offender is an undertaking, up to 7 % of its total worldwide annual turnover for the preceding financial year, whichever is higher" | Art. 99(3) |
| Fines, other operator obligations | "up to EUR 15 000 000 or ... up to 3 %" | Art. 99(4) |
| Fines, incorrect information to authorities | "up to EUR 7 500 000 or ... up to 1 %" | Art. 99(5) |
| Fines, SMEs / SMCs | SMEs: each fine "up to the percentages or amount ... whichever thereof is lower" (Art. 99(6)); SMCs: same rule for Art. 99(4)-(5) fines | Art. 99(6); Art. 99(6a) inserted by Reg. (EU) 2026/1744 |
| Serious incident report, general | "not later than 15 days after the provider or, where applicable, the deployer, becomes aware" | Art. 73(2) |
| Serious incident report, widespread infringement or critical-infrastructure incident (Art. 3(49)(b)) | "not later than two days" after awareness | Art. 73(3) |
| Serious incident report, death of a person | "not later than 10 days" after awareness | Art. 73(4) |

## Assessment and certification
High-risk AI systems need a conformity assessment before being placed on the market (internal control under Annex VI for Annex III points 2-8; internal control or notified body under Annex VII for Annex III point 1 biometrics, Art. 43). Providers keep a post-market monitoring system. Market surveillance authorities supervise AI systems, and the AI Office "holds enforcement powers over GPAI models", including requesting documentation, evaluating models and imposing fines. The GPAI Code of Practice (July 2025) and the Code of Practice on Marking and Labelling of AI-generated Content are voluntary compliance tools. The first harmonised standard supporting the AI Act was published in the OJ on 19 October 2026 (Commission AI Act page).

## Notes
- **Source caveat (updated in follow-up pass):** eur-lex.europa.eu still returns an AWS WAF challenge. Regulation (EU) 2024/1689 (as originally published) and amending Regulation (EU) 2026/1744 were read from the Official Journal XHTML served by the EU Publications Office (publications.europa.eu cellar). No consolidated text was read, so article wording quoted from 2024/1689 should be checked against the consolidated version where the Omnibus amended it (Art. 99(1) and (4) were amended; Art. 99(3), 73 and 43(1)-(2) were not found among the amendments searched).
- **Officially adopted postponement:** the AI Omnibus was proposed by the Commission on 19 November 2025 (the Commission page says "adopted", meaning the Commission proposal), a political agreement was reached on 7 May 2026, and it was signed on 8 July 2026 as Regulation (EU) 2026/1744 and published in the OJ on 24 July 2026, entering into force on 27 July 2026. High-risk Annex III rules move from 2 Aug 2026 to **2 Dec 2027** and Annex I rules to **2 Aug 2028**. It also adds a ninth prohibition, extends SME simplifications to small mid-caps, centralises AI Office oversight of systems built on GPAI models, and widens sandbox access.
- **Catalog check:** framework-catalog.md line 109 and control-checklists.md AI-02 (four tiers) are consistent with the Commission page. The repo files carry no application timeline, so they should add the post-Omnibus dates above. The old timeline of 2 Aug 2026 for high-risk and 2 Aug 2027 for Annex I products is now wrong for high-risk systems.
- Commission guidelines exist on prohibited practices, the AI system definition, GPAI obligations and transparency obligations (20 July 2026); they were not read.
