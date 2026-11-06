---
id: nist-ai-rmf
name: NIST AI RMF 1.0 (+ Generative AI Profile)
official_name: Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1; and NIST AI 600-1, Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile
governing_body: National Institute of Standards and Technology (NIST), Information Technology Laboratory
type: ai
legal_status: voluntary-standard
region: US origin; intended for use globally
industry: any (organizations designing, developing, deploying or using AI)
current_version: AI RMF 1.0 (NIST AI 100-1), January 2023 (released January 26, 2023); Generative AI Profile NIST AI 600-1, July 2024 (released July 26, 2024)
superseded_by: none (NIST states AI RMF 1.0 "is being revised as part of the White House AI Action Plan")
official_sources:
  - title: NIST AI Risk Management Framework page
    url: https://www.nist.gov/itl/ai-risk-management-framework
    accessed: 2026-11-06
  - title: NIST AI 100-1, AI RMF 1.0 (PDF)
    url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
    accessed: 2026-11-06
  - title: NIST AI 600-1, Generative AI Profile (PDF)
    url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The AI RMF "is intended for voluntary use and to improve the ability to incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems" (NIST AI RMF page). It is "voluntary, rights-preserving, non-sector-specific, and use-case agnostic" (AI 100-1, Executive Summary). The Core has four functions, GOVERN, MAP, MEASURE and MANAGE; "Governance is designed to be a cross-cutting function to inform and be infused throughout the other three functions" (Fig. 5). Trustworthy AI characteristics: "valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed" (Sec. 3). The Generative AI Profile (AI 600-1) "can help organizations identify unique risks posed by generative AI and proposes actions for generative AI risk management" (NIST page).

## Who it applies to
Voluntary; for "organizations of all sizes and in all sectors" designing, developing, deploying or using AI systems (AI 100-1). No legal thresholds. May be referenced by contracts, procurement or policy.

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| GOVERN 1.1 | Legal and regulatory requirements involving AI are understood, managed and documented | AI 100-1 Table 1 |
| GOVERN 1.6 | "Mechanisms are in place to inventory AI systems" | GOVERN 1.6 |
| GOVERN 1.7 | Processes to decommission and phase out AI systems safely | GOVERN 1.7 |
| GOVERN 6.1 / 6.2 | Policies for third-party AI risks (incl. IP infringement); contingency processes for failures in third-party data or AI systems | GOVERN 6.1, 6.2 |
| MAP 1.1 | Document intended purposes, beneficial uses, context, laws, norms and expected users | MAP 1.1 |
| MAP 2.3 | Document TEVV considerations incl. data collection/selection representativeness | MAP 2.3 |
| MAP 4.1 | Map technology and legal risks of components including third-party data or software | MAP 4.1 |
| MEASURE 2.1 | "Test sets, metrics, and details about the tools used during TEVV are documented" | MEASURE 2.1 |
| MEASURE 2.3 | Measure performance criteria under conditions similar to deployment; document | MEASURE 2.3 |
| MEASURE 2.7 | "AI system security and resilience ... are evaluated and documented" | MEASURE 2.7 |
| MEASURE 2.9 | Model explained, validated and documented; output interpreted in context | MEASURE 2.9 |
| MEASURE 2.10 | "Privacy risk of the AI system ... is examined and documented" | MEASURE 2.10 |
| MEASURE 2.11 | "Fairness and bias ... are evaluated and results are documented" | MEASURE 2.11 |
| MANAGE 2.4 | Mechanisms to "supersede, disengage, or deactivate AI systems" performing inconsistently with intended use | MANAGE 2.4 |
| MANAGE 3.1 / 3.2 | Monitor third-party AI risks; monitor pre-trained models used in development | MANAGE 3.1, 3.2 |
| MANAGE 4.1 | Post-deployment monitoring incl. user input capture, appeal and override, incident response, recovery, change management | MANAGE 4.1 |
| MANAGE 4.3 | Communicate incidents and errors to relevant AI actors and affected communities; track response and recovery | MANAGE 4.3 |
| GAI-RISKS | For generative AI, assess the 12 GAI risks: CBRN information or capabilities; confabulation; dangerous, violent, or hateful content; data privacy; environmental impacts; harmful bias or homogenization; human-AI configuration; information integrity; information security; intellectual property; obscene, degrading, and/or abusive content; value chain and component integration | AI 600-1 Sec. 2 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| AI RMF 1.0 release | "Released on January 26, 2023" | NIST AI RMF page |
| Structure | 4 functions, 19 categories, 72 subcategories | AI 100-1 Tables 1-4 (counted) |
| Generative AI Profile release | "On July 26, 2024, NIST released NIST-AI-600-1" | NIST AI RMF page |
| GAI risks | 12 | AI 600-1 Sec. 2 |

No notification windows, retention periods or penalties.

## Assessment and certification
No certification or official assessment scheme. Organizations self-assess and may build use-case or cross-sectoral profiles. NIST provides the AI RMF Playbook, Roadmap, Crosswalks and the Trustworthy and Responsible AI Resource Center (airc.nist.gov).

## Notes
- Catalog row "NIST AI RMF ... self" is correct. Suggest adding the Generative AI Profile (NIST AI 600-1, July 2024) for products using generative AI, and noting the revision under way.
- Officially announced pending changes (NIST page, 2026-11-06): "The AI RMF 1.0 is being revised as part of the White House AI Action Plan"; April 7, 2026 concept note for an AI RMF Profile on Trustworthy AI in Critical Infrastructure.
- airc.nist.gov was not separately fetched; facts come from nist.gov and nvlpubs PDFs.
