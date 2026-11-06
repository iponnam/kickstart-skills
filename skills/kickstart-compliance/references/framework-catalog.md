# Framework catalog

Every framework the compliance skill can recommend. Mirrors the list on scrut.io/solutions/all-frameworks (captured 2026-11-06) plus a few commonly requested additions marked `+`.

Tags:
- `region`: ISO country codes, region names, or `global`
- `industry`: `any`, `finance`, `health`, `education`, `government`, `defence`, `automotive`, `aviation`, `medtech`, `cloud`, `ai`, `payments`, `telecom`, `energy`
- `type`: `security`, `privacy`, `quality`, `continuity`, `governance`, `ai`
- `audit`: `certification` (external auditor), `attestation` (report), `self` (self-assessment), `law` (legal obligation, no certificate)
- `effort`: S (days), M (weeks), L (months) for a small engineering team starting from a kickstart baseline
- `trigger`: facts about the product that make it apply

## Security frameworks

| Framework | region | industry | type | audit | effort | trigger / when it applies |
|---|---|---|---|---|---|---|
| SOC 2 (Type I / II) | global, strongest in US | any | security | attestation | M–L | Selling to US or enterprise customers who ask for a security report |
| PCI DSS v4.0 | global | payments, any | security | certification / self (SAQ) | S (SAQ-A with hosted checkout) to L (storing cards) | Accepting, processing, storing or transmitting card data |
| ISO 27001:2022 | global | any | security | certification | L | Enterprise sales outside the US, government tenders, EU/APAC buyers |
| ISO 27001:2013 | global | any | security | certification | L | Legacy version, superseded; map to 2022 |
| DORA (Digital Operational Resilience Act) | EU | finance | security, continuity | law | M–L | EU financial entities and their critical ICT providers |
| NIS 2 Directive | EU | energy, telecom, health, finance, government, cloud, digital services | security | law | M–L | Essential or important entities in the EU |
| NIST CSF v1.1 | global, US origin | any | security | self | M | Structured risk programme; legacy version |
| NIST CSF 2.0 | global, US origin | any | security | self | M | Structured risk programme; preferred version |
| CSA STAR | global | cloud | security | self / certification | M | Cloud service providers proving cloud security posture |
| ISO 9001:2015 | global | any | quality | certification | M | Quality management, often required by manufacturing or government buyers |
| ISO 20000-1:2018 | global | any | quality | certification | M | IT service management for managed service providers |
| NYDFS 23 NYCRR 500 | US-NY | finance | security | law | M | Financial institutions licensed by New York DFS |
| MAS TRM 2021 | SG | finance | security | law | M–L | Financial institutions operating in Singapore |
| ISR V2 (Dubai Information Security Regulation) | AE-Dubai | government, any supplying Dubai government | security | law | M | Entities handling Dubai government information |
| RBI CSF (Cyber Security Framework for Banks) | IN | finance | security | law | L | Banks regulated by the Reserve Bank of India |
| RBI PA/PG (Payment Aggregators / Gateways) | IN | payments | security | law | M–L | Entities facilitating online payments in India |
| ISO 27017:2015 | global | cloud | security | certification | M | Cloud security controls on top of ISO 27001 |
| SAMA Minimum Verification Controls | SA | finance | security | law | M | Financial institutions in Saudi Arabia (baseline) |
| SAMA CSF (Cyber Security Framework) | SA | finance | security | law | L | Financial institutions in Saudi Arabia (full) |
| SAMA Cyber Resilience Fundamentals | SA | finance | security, continuity | law | M | Saudi financial institutions, resilience focus |
| TISAX v5.1 | DE, EU, global automotive | automotive | security | certification | M–L | Suppliers to automotive OEMs |
| DTAC (Digital Technology Assessment Criteria) | UK | health | security, quality | self | M | Digital health products sold to the NHS |
| EASA (software and firmware validation) | EU, global aviation | aviation | security, quality | certification | L | Safety-related software or firmware in aviation |
| Essential Eight Level 1 | AU | government, any | security | self | S–M | Australian baseline mitigation strategies |
| Essential Eight Level 2 | AU | government, any | security | self | M | Advanced Australian mitigation strategies |
| Cyber Essentials v3.2 | UK | any | security | certification (light) | S | UK SMEs, required for many UK government contracts |
| Australia ISM | AU | government | security | self / IRAP | L | Australian government agencies and suppliers |
| SEBI CSCRF | IN | finance (market infrastructure) | security, continuity | law | L | Stock exchanges, brokers, depositories, market intermediaries in India |
| CIS Controls v8 | global | any | security | self | M | Practical baseline for any organisation |
| Essential Cybersecurity Controls (ECC, Saudi NCA) | SA | government, energy, any critical | security | law | M–L | Saudi national entities and critical infrastructure |
| CMMC 2.0 Level 1 | US | defence | security | self | S–M | US DoD contractors handling federal contract information |
| CMMC 2.0 Level 2 | US | defence | security | certification | L | US DoD contractors handling controlled unclassified information |
| NIST SP 800-53 Rev 5 | US, global | government, any | security, privacy | self / FedRAMP | L | US federal systems; basis for FedRAMP |
| NIST SP 800-171 Rev 2 | US | defence, government suppliers | security | self | M–L | Protecting CUI in non-federal systems |
| NIST SP 800-171A | US | defence, government suppliers | security | self | M | Assessment procedures for 800-171 |
| ISO 27018:2019 | global | cloud | privacy, security | certification | M | Cloud processors of personal data |
| COBIT 2019 | global | any | governance | self | L | IT governance alignment, large organisations |
| ISO 22301:2019 BCMS | global | any | continuity | certification | M–L | Business continuity, often asked by enterprise buyers |
| `+` FedRAMP | US | government, cloud | security | certification | L | Cloud services sold to US federal agencies |
| `+` HITRUST CSF | US | health | security | certification | L | Healthcare partners demanding a certified framework |
| `+` SOX (ITGC) | US (listed companies) | finance, any public | governance | attestation | M | Public companies; IT general controls over financial reporting |
| `+` CERT-In directions (2022) | IN | any | security | law | S–M | Any entity in India: 6-hour incident reporting, 180-day log retention, NTP sync |
| `+` IRDAI cyber guidelines | IN | finance (insurance) | security | law | M–L | Insurers regulated in India |
| `+` SWIFT CSP | global | finance | security | self / attestation | M | SWIFT-connected institutions |
| `+` IEC 62443 | global | energy, industrial | security | certification | L | Industrial control systems and OT |
| `+` C5 (BSI) | DE | cloud | security | attestation | L | Cloud providers selling to German public sector |
| `+` ENS | ES | government, cloud | security | certification | M–L | Suppliers to Spanish public sector |
| `+` HDS | FR | health | security | certification | L | Hosting health data in France |
| `+` ISMAP | JP | government, cloud | security | certification | L | Cloud services for Japanese government |
| `+` K-ISMS-P | KR | any | security, privacy | certification | L | Korean organisations above size thresholds |
| `+` UAE PDPL / NESA IAS | AE | any / government | privacy, security | law | M | Processing UAE residents' data; UAE government entities |
| `+` Qatar NIA | QA | government, critical | security | law | M–L | Qatar national entities |
| `+` SOC 1 | global | finance, any affecting customers' financial reporting | governance | attestation | M | Services that affect customers' financial statements |
| `+` SOC 3 | global | any | security | attestation | S (after SOC 2) | Public-facing summary of SOC 2 |

## Privacy frameworks

| Framework | region | industry | type | audit | effort | trigger / when it applies |
|---|---|---|---|---|---|---|
| GDPR | EU, EEA; applies to anyone serving EU residents | any | privacy | law | M | Any personal data of EU/EEA residents |
| `+` UK GDPR + Data Protection Act 2018 | UK | any | privacy | law | M | Any personal data of UK residents |
| ISO 27701 | global | any | privacy | certification | M–L | Privacy information management on top of ISO 27001 |
| HIPAA | US | health | privacy, security | law | M–L | Protected health information; covered entities and business associates |
| CCPA / CPRA | US-CA | any | privacy | law | S–M | California residents' data above thresholds (revenue, volume, or data sales) |
| PIPEDA | CA | any | privacy | law | S–M | Personal information in Canadian commercial activity |
| PDPA Singapore | SG | any | privacy | law | S–M | Personal data in Singapore |
| RBI DPSC (Data Protection and Security Controls) | IN | finance | privacy, security | law | M | Banks and NBFCs handling customer financial data |
| DPDPA (Digital Personal Data Protection Act 2023) | IN | any | privacy | law | S–M | Any digital personal data of individuals in India |
| COPPA | US | any with children's users | privacy | law | S–M | Collecting data from children under 13 |
| FERPA | US | education | privacy | law | S–M | Student education records at funded institutions |
| PHIPA | CA-ON | health | privacy | law | M | Personal health information in Ontario |
| Botswana Data Protection Act | BW | any | privacy | law | S–M | Personal data of Botswana residents |
| GLBA | US | finance | privacy, security | law | M | Non-public personal information in US financial services |
| New Jersey Data Privacy Law | US-NJ | any | privacy | law | S | New Jersey residents' data above thresholds |
| Seychelles Data Protection Act | SC | any | privacy | law | S–M | Personal data of Seychelles residents |
| Law 25 (Quebec) | CA-QC | any | privacy | law | M | Personal information of Quebec residents |
| US Data Privacy (multi-state) | US | any | privacy | law | M | Serving residents of states with privacy laws (CA, VA, CO, CT, UT, TX, OR, MT, NJ, DE, IA, NE, NH, TN, MN, MD, IN, KY, RI…) |
| `+` LGPD | BR | any | privacy | law | M | Personal data of Brazilian residents |
| `+` POPIA | ZA | any | privacy | law | M | Personal information in South Africa |
| `+` Nigeria NDPA | NG | any | privacy | law | S–M | Personal data in Nigeria |
| `+` Kenya DPA | KE | any | privacy | law | S–M | Personal data in Kenya |
| `+` PIPL | CN | any | privacy | law | L | Personal information of individuals in China, with cross-border transfer rules |
| `+` APPI | JP | any | privacy | law | M | Personal information in Japan |
| `+` Australia Privacy Act (APPs) | AU | any | privacy | law | M | Personal information in Australia above turnover threshold or health data |
| `+` Saudi PDPL | SA | any | privacy | law | M | Personal data of Saudi residents (listed under Others on scrut.io) |

## Others (AI, quality, continuity, governance)

| Framework | region | industry | type | audit | effort | trigger / when it applies |
|---|---|---|---|---|---|---|
| NIST AI RMF | global, US origin | ai | ai, governance | self | M | Building or deploying AI systems; US buyers |
| ISO 42001:2023 | global | ai | ai, governance | certification | L | AI management system; enterprise or regulated buyers of AI |
| `+` EU AI Act | EU | ai | ai, law | law | M–L | AI systems placed on the EU market, risk-tiered obligations |
| CIS | global | any | security | self | M | See CIS Controls v8 above |
| ISO 22301:2019 BCMS | global | any | continuity | certification | M–L | Business continuity |
| ISO 13485:2016 | global | medtech | quality | certification | L | Medical device quality management |
| Essential Cybersecurity Controls (ECC) | SA | any national | security | law | M–L | See above |
| CMMC 2.0 Level 1 / Level 2 | US | defence | security | self / certification | M / L | See above |
| Saudi Arabia PDPL | SA | any | privacy | law | M | See privacy table |
| SAMA Cyber Resilience Fundamentals | SA | finance | continuity | law | M | See above |
| ISO 27018:2019 | global | cloud | privacy | certification | M | See above |
| COBIT 2019 | global | any | governance | self | L | See above |
| Custom framework | any | any | any | self | varies | User supplies controls; the skill stores them in the same checklist format |

## Region quick map

Use this to shortlist fast. Always add OWASP Top 10.

| User region | Required or strongly expected | Customer-expected | Industry add-ons |
|---|---|---|---|
| India | DPDPA, CERT-In directions | SOC 2 or ISO 27001 when selling B2B | RBI CSF / RBI PA/PG / RBI DPSC (banking, payments), SEBI CSCRF (markets), IRDAI (insurance) |
| United States | US Data Privacy (state laws), CCPA if CA | SOC 2 | HIPAA (health), GLBA (finance), COPPA (children), FERPA (education), PCI DSS (cards), NIST 800-171 / CMMC (defence), NIST 800-53 / FedRAMP (federal), NYDFS (NY finance), SOX (public) |
| European Union | GDPR | ISO 27001 | DORA (finance), NIS 2 (essential services), EU AI Act (AI), TISAX (automotive), EASA (aviation), C5 / ENS / HDS (country cloud and health) |
| United Kingdom | UK GDPR, Cyber Essentials for public contracts | ISO 27001, SOC 2 | DTAC (NHS digital health) |
| Singapore | PDPA Singapore | ISO 27001 | MAS TRM (finance) |
| Australia | Australia Privacy Act | Essential Eight L1 | ISM / IRAP (government), Essential Eight L2 |
| Canada | PIPEDA, Law 25 if Quebec | SOC 2 | PHIPA (Ontario health) |
| Saudi Arabia | Saudi PDPL, ECC | ISO 27001 | SAMA MVC / CSF / Resilience (finance) |
| UAE | UAE PDPL | ISO 27001 | ISR V2 (Dubai government), NESA IAS |
| Brazil | LGPD | ISO 27001, SOC 2 | PCI DSS (cards) |
| Japan | APPI | ISO 27001 | ISMAP (government cloud) |
| South Korea | PIPA / K-ISMS-P | ISO 27001 | |
| China | PIPL | | |
| Africa (BW, SC, ZA, NG, KE) | Local DPA (Botswana DPA, Seychelles DPA, POPIA, NDPA, Kenya DPA) | ISO 27001 | |
| Global SaaS, no fixed region | GDPR (you will have EU users), US Data Privacy | SOC 2 + ISO 27001 | PCI DSS SAQ-A if taking cards |

## Industry quick map

| Industry | Add on top of region |
|---|---|
| Fintech, banking, payments | PCI DSS, SOC 2, plus the national regulator (RBI, MAS, SAMA, NYDFS, DORA, GLBA) |
| Health | HIPAA (US), PHIPA (ON), DTAC (UK), HDS (FR), ISO 27001, HITRUST if partners demand |
| Education | FERPA (US), COPPA if under-13 users, local privacy law |
| Government suppliers | NIST 800-53 / FedRAMP (US), Australia ISM, ENS, ISMAP, ISR V2, ECC, Cyber Essentials (UK) |
| Defence | CMMC, NIST 800-171 |
| Automotive | TISAX |
| Aviation | EASA |
| Medical devices | ISO 13485, plus health privacy law |
| AI products | NIST AI RMF, ISO 42001, EU AI Act |
| Cloud / infrastructure providers | ISO 27017, ISO 27018, CSA STAR, C5 |
| E-commerce | PCI DSS, consumer privacy law, COPPA if applicable |
| General B2B SaaS | SOC 2 or ISO 27001, GDPR, US Data Privacy |
| General consumer app, pet project | OWASP Top 10 plus the one local privacy law |
