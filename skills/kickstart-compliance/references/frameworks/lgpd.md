---
id: lgpd
name: LGPD
official_name: Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709, de 14 de agosto de 2018); Resolução CD/ANPD nº 15, de 24 de abril de 2024 (Regulamento de Comunicação de Incidente de Segurança)
governing_body: Agência Nacional de Proteção de Dados (ANPD) - transformed into a regulatory agency by Medida Provisória nº 1.317 of 17 September 2025
type: privacy
legal_status: law
region: Brazil; applies regardless of the controller's seat or where data is located if processing occurs in Brazil, aims to offer goods/services to or process data of individuals located in Brazil, or data was collected in Brazil (Art. 3)
industry: any
current_version: Lei 13.709/2018 in force in stages: 28 Dec 2018 (ANPD articles), 18 Sep 2020 (most provisions), 1 Aug 2021 (sanctions Arts. 52-54). Resolution CD/ANPD 15/2024 "Vigente"
superseded_by: none
official_sources:
  - title: ANPD - Perguntas frequentes (FAQ on LGPD)
    url: https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes
    accessed: 2026-11-06
  - title: ANPD - Comunicado de incidente de segurança (CIS) - guidance and FAQ
    url: https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis
    accessed: 2026-11-06
  - title: ANPD news - ANPD aprova o Regulamento de Comunicação de Incidente de Segurança (26/04/2024)
    url: https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-aprova-o-regulamento-de-comunicacao-de-incidente-de-seguranca
    accessed: 2026-11-06
  - title: ANPD - Regulamentações da ANPD (list and status of resolutions)
    url: https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd
    accessed: 2026-11-06
  - title: Diário Oficial da União, 15/08/2018, Edição 157, Seção 1, p. 59 - Lei nº 13.709 (Imprensa Nacional print, copy hosted on gov.br/cnen; original text, without later amendments)
    url: https://www.gov.br/cnen/pt-br/acesso-a-informacao/ouvidoria/LEINo13.709DE14DEAGOSTODE2018ImprensaNacional.pdf
    accessed: 2026-11-06
  - title: Imprensa Nacional - Lei nº 13.709 (DOU page; returned HTTP 403 from the CDN in this session)
    url: https://www.in.gov.br/materia/-/asset_publisher/Kujrw0TZC2Mb/content/id/36849373/do1-2018-08-15-lei-no-13-709-de-14-de-agosto-de-2018-36849337
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
Brazil's general data protection law, supervised by the ANPD, with ANPD resolutions implementing it: incident communication (Res. 15/2024), DPO/encarregado (Res. 18/2024), international transfers and standard contractual clauses (Res. 19/2024), small processing agents (Res. 2/2022), sanctions dosimetry (Res. 4/2023), and an EU adequacy recognition (Res. 32/2026), all listed as "Vigente" by ANPD.

## Who it applies to
Any processing operation by a natural person or a public- or private-law legal entity, "independentemente do meio, do país de sua sede ou do país onde estejam localizados os dados", provided that: (I) the processing takes place in Brazil; (II) it aims to offer or supply goods or services, or to process data of individuals located in Brazil; or (III) the data was collected in Brazil, meaning the data subject was in Brazil at the time of collection (Art. 3, caput and §1). Exclusions are listed in Art. 4 (e.g. purely private non-economic purposes, journalistic/artistic/academic purposes, public safety, national defence; the current wording of Art. 4 after amendments was not checked). Small processing agents get simplified rules (Res. CD/ANPD 2/2022).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| Art. 7 / 11 | Map each processing to a legal basis (Art. 7) and, for sensitive data, Art. 11; transfers abroad only under Art. 33 | LGPD Arts. 7, 11, 33 (per ANPD FAQ) |
| Art. 18 | Data subject rights handled on express request, free of charge; respond immediately or send a reasoned reply (Art. 18 §§3-5) | LGPD Art. 18 (per ANPD FAQ) |
| Art. 19 | Confirmation of existence/access: simplified reply immediately, or complete declaration within 15 days | LGPD Art. 19 (per ANPD FAQ) |
| Art. 14 | Children's data: in the child's best interest; "consentimento específico e em destaque dado por pelo menos um dos pais ou pelo responsável legal"; publish the types of data collected, how they are used and how to exercise Art. 18 rights | LGPD Art. 14 caput, §§1-2 |
| Art. 37 | Controller and processor keep a record of processing operations, "especialmente quando baseado no legítimo interesse" | LGPD Art. 37 |
| Art. 38 | Be able to produce a data protection impact assessment (relatório de impacto) when ANPD requires it | LGPD Art. 38 |
| Art. 46 | Technical and administrative security measures against unauthorised access and accidental or unlawful destruction, loss, alteration, communication or improper processing; applied "desde a fase de concepção do produto ou do serviço até a sua execução" | LGPD Art. 46 caput and §2 |
| Art. 49 | Systems used for processing must be structured to meet security requirements, good-practice and governance standards and the Law's principles | LGPD Art. 49 |
| Art. 41 | Appoint an encarregado (DPO) and publish contact details clearly, preferably on the website; small agents exempt but must provide a contact channel | LGPD Art. 41; Res. 2/2022; Res. 18/2024 (per ANPD FAQ) |
| Art. 48 | Controller communicates to ANPD and data subjects "incidente de segurança que possa acarretar risco ou dano relevante aos titulares", in a reasonable time set by ANPD, stating at minimum the nature of data, data subjects involved, security measures used, risks, and (per §1) further items | LGPD Art. 48 caput, §1; Res. 15/2024 |
| RCIS-6 | Communicate to ANPD within 3 business days via ANPD's electronic form; preliminary then complementary communication allowed, complement within 20 business days | Res. 15/2024 Art. 6 (per ANPD CIS page) |
| RCIS-9 | Communicate to data subjects within 3 business days, individually and directly where possible, plain language | Res. 15/2024 Art. 9 (per ANPD CIS page) |
| RCIS-REG | Keep a register of security incidents involving personal data for at least five years | Res. 15/2024 (per ANPD news release) |
| RCIS-RISK | Assess incident risk: context, categories and numbers of subjects, nature and amount of data, potential harms, whether data was unintelligible, sufficiency of mitigation | ANPD CIS FAQ item 3 |
| OPER | Processors inform the controller "sem demora injustificada" of incidents and give all information needed | ANPD CIS FAQ item 6 |
| Res. 19 | International transfers using ANPD standard contractual clauses or other Art. 33 mechanisms | Res. CD/ANPD 19/2024 (title only verified) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Incident communication to ANPD | "no prazo de três (3) dias úteis, ressalvada a existência de prazo para comunicação previsto em legislação específica" | Res. 15/2024 Arts. 6 and 9, per ANPD CIS page |
| Notification to individuals | same "três (3) dias úteis" | Res. 15/2024 Art. 9, per ANPD CIS page |
| Complementary information | "no prazo de vinte dias úteis" | Res. 15/2024 Art. 6 §3, per ANPD CIS page |
| Incident register retention | "por ao menos cinco anos" | ANPD news release, 26/04/2024 |
| Access request (complete declaration) | "em até 15 (quinze) dias" | LGPD Art. 19, per ANPD FAQ |
| Fines | "Multa simples, de até 2% (dois por cento) do faturamento ... no Brasil no seu último exercício, excluídos os tributos, limitada, no total, a R$ 50.000.000,00 ... por infração" | LGPD Art. 52, per ANPD FAQ |
| Original entry into force | "após decorridos 18 (dezoito) meses de sua publicação oficial" (original Art. 65; later amended to the staged dates in the front-matter, amendment text not read) | LGPD Art. 65 (DOU 15/08/2018) |
| Sanctions in force | "Em 1º de agosto de 2021, quanto aos arts. 52, 53 e 54" | ANPD FAQ 1.3 |

## Assessment and certification
No certification. ANPD supervises through annual monitoring cycles and two-year priority theme maps (Res. 1/2021, 10/2023, 30/2025), investigates and applies Art. 52 sanctions after administrative proceedings.

## Notes
- Checklist line "LGPD: DPO (encarregado) named; legal bases mapped to Art. 7; ANPD notification" is right but should give the 3-business-day window (Res. 15/2024), the 5-year incident register, and the small-agent DPO exemption (Res. 2/2022).
- ANPD is now "Agência Nacional de Proteção de Dados", a regulatory agency, per MP 1.317/2025 (ANPD FAQ). Older material says "Autoridade".
- Second pass: Arts. 3, 14, 37, 38, 46, 48, 49 and 65 were read from the original DOU publication of 15/08/2018 (Imprensa Nacional print, copy on gov.br). That copy does not include later amendments (Lei 13.853/2019, MP 1.317/2025, etc.); the consolidated text on planalto.gov.br is unreachable and www.in.gov.br answered HTTP 403 (CDN error page) to both curl and Playwright. Art. 3 scope is confirmed; the current consolidated wording of Arts. 4, 41, 52 and 65 remains as reported by ANPD pages.
- Res. CD/ANPD 15/2024 full text still not fetched (published in DOU on in.gov.br, which is blocked by 403 here). Its 3-business-day, 20-business-day and 5-year figures come from ANPD's own pages; they are consistent across two ANPD pages but remain second-hand to the resolution text, so verification stays `partial`.
