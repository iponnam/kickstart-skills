---
id: ens
name: ENS (Esquema Nacional de Seguridad)
official_name: Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad
governing_body: Government of Spain (Real Decreto, Ministerio de Asuntos Económicos y Transformación Digital); Centro Criptológico Nacional (CCN) coordinates incident response through CCN-CERT (Art. 33) and issues CCN-STIC guides (Disposición adicional segunda); mandatory Instrucciones Técnicas de Seguridad approved by the Ministry for Digital Transformation and Public Service
type: security
legal_status: law
region: Spain
industry: government (whole public sector), and private-sector entities that provide services or solutions to public-sector bodies under contract (Art. 2(3))
current_version: Real Decreto 311/2022, BOE núm. 106 of 04/05/2022, in force 05/05/2022; consolidated text last updated 06/11/2024 (in force 07/11/2024) by disposición final 2 of Real Decreto 1125/2024
superseded_by: none
official_sources:
  - title: BOE consolidated text, Real Decreto 311/2022 (BOE-A-2022-7191)
    url: https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191
    accessed: 2026-11-06
  - title: CCN - Esquema Nacional de Seguridad portal (not reachable from sandbox)
    url: https://ens.ccn.cni.es/es/
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: verified
---

## What it is
The ENS is "constituido por los principios básicos y requisitos mínimos necesarios para una protección adecuada de la información tratada y los servicios prestados" by the entities in scope, to ensure access, confidentiality, integrity, traceability, authenticity, availability and preservation of data, information and services handled electronically (Art. 1(2)). It implements Art. 156.2 of Ley 40/2015 (Art. 1(1)) and replaced Real Decreto 3/2010 (Disposición derogatoria única). Security measures are set out in Annex II and scaled to the system category (BÁSICA, MEDIA, ALTA) under Annex I.

## Who it applies to
- "todo el sector público", as defined in Art. 2 of Ley 40/2015 (Art. 2(1)).
- Systems handling classified information, with possible complementary measures (Art. 2(2)).
- Private-sector entities' information systems, "incluida la obligación de contar con la política de seguridad a que se refiere el artículo 12", when under contract they "presten servicios o provean soluciones a las entidades del sector público" (Art. 2(3)). Public-sector tender specifications must require ENS conformity, "tales como la presentación de las correspondientes Declaraciones o Certificaciones de Conformidad con el ENS", and this extends to the contractor's supply chain as far as the risk analysis requires (Art. 2(3)).
- Systems processing personal data also follow the GDPR and LO 3/2018, with risk analysis under GDPR Art. 24 and DPIA under Art. 35 where applicable (Art. 3).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| ENS-01 | Categorise each system as BÁSICA, MEDIA or ALTA: ALTA if any security dimension reaches level ALTO; MEDIA if any reaches MEDIO and none higher; BÁSICA if any reaches BAJO and none higher | Art. 40; Annex I s. 4(1) |
| ENS-02 | Adopt the Annex II measures and reinforcements for the system's assets, category and risk decisions; they are minimums, extendable by the security officer | Art. 28(1)-(2) |
| ENS-03 | Formalise the selected measures in a "Declaración de Aplicabilidad, firmado por el responsable de la seguridad"; document any compensating measures and map them to the Annex II measures they replace | Art. 28(2)-(3) |
| ENS-04 | Annex II groups: "Marco organizativo [org]", "Marco operacional [op]", "Medidas de protección [mp]" | Annex II s. 1 |
| ENS-05 | Approved information security policy with objectives, regulatory framework, security roles and committees (private contractors too; approved by their top executive body) | Art. 12; Art. 2(3) |
| ENS-06 | Risk analysis and management | Art. 14 |
| ENS-07 | Access control limited to "usuarios, procesos, dispositivos u otros sistemas de información, debidamente autorizados" and only to permitted functions | Art. 17 |
| ENS-08 | Design and configure systems with least privilege | Art. 20 |
| ENS-09 | Formal prior authorisation to add or modify any element in the up-to-date asset inventory; system integrity and updates | Art. 21(1) |
| ENS-10 | Protect information stored and in transit, especially on portable/mobile devices, removable media and open networks | Art. 22(1) |
| ENS-11 | Log user activity, retaining only what is strictly necessary to monitor, analyse, investigate and document improper or unauthorised activity; each user "deberá estar identificado de forma única" | Art. 24(1), (3) |
| ENS-12 | Security incident management procedures per Art. 33 and the relevant Instrucción Técnica de Seguridad | Art. 25(1) |
| ENS-13 | Backups and mechanisms to ensure continuity of operations | Art. 26 |
| ENS-14 | Public-sector entities notify CCN of incidents "que tengan un impacto significativo"; private-sector suppliers to public entities notify INCIBE-CERT | Art. 33(2), 33(7) |
| ENS-15 | Regular security audit at least every two years, and an extraordinary audit after substantial changes | Art. 31(1) |
| ENS-16 | Publish declarations and certifications of conformity on the entity's website or e-office | Art. 38(2) |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Regular audit | "al menos cada dos años"; extendable "durante tres meses" for force majeure | Art. 31(1) |
| Transition for pre-existing systems | "veinticuatro meses para alcanzar su plena adecuación al ENS" (from entry into force 05/05/2022) | Disposición transitoria única (1) |
| Security categories | "tres categorías de seguridad: BÁSICA, MEDIA y ALTA" | Annex I s. 4(1) |
| Entry into force | 05/05/2022 (BOE núm. 106 of 04/05/2022) | BOE consolidated text metadata |

## Assessment and certification
Systems in scope go through a conformity process: "los sistemas de categoría MEDIA o ALTA precisarán de una auditoría para la certificación de su conformidad", while "los sistemas de categoría BÁSICA solo requerirán de una autoevaluación para su declaración de la conformidad" (they may also choose an audit) (Art. 38(1)). Both follow Art. 31, Annex III and the Instrucción Técnica de Seguridad, which also sets the requirements for certification bodies (Art. 38(1)). Audit reports go to the system owner and security officer; for ALTA systems the system owner may suspend operation until serious deficiencies are fixed (Art. 31(5)-(6)). Results are shown via Distintivos de Conformidad (Disposición transitoria única).

## Notes
- **Sources (follow-up pass):** facts now come from the BOE consolidated text of Real Decreto 311/2022 (www.boe.es). BOE states the consolidated text is "de carácter informativo y no tiene valor jurídico"; the authentic text is the BOE of 04/05/2022. CCN sites (ens.ccn.cni.es, ccn-cert.cni.es) were still not tried in this pass, so CCN-STIC guides and the Instrucciones Técnicas de Seguridad (incident notification ITS, audit ITS, certification body accreditation) were not read (UNVERIFIED).
- **Amendment:** the consolidated text records a change by "la disposición final 2 del Real Decreto 1125/2024, de 5 de noviembre. Ref. BOE-A-2024-22935" (Disposición adicional segunda, on who approves Instrucciones Técnicas de Seguridad), in force 07/11/2024. No other amendment is shown.
- **Catalog check:** framework-catalog.md line 63 (ENS, ES, government/cloud, certification, "Suppliers to Spanish public sector") is mostly right, but "certification" is too strict: BÁSICA systems need only a self-assessment and declaration of conformity (Art. 38(1)). Scope is the whole public sector plus contracted private suppliers and, as needed, their supply chain (Art. 2).
- No numeric incident-notification deadline is in the Real Decreto itself; Art. 33(2) defers to the Instrucción Técnica de Seguridad (UNVERIFIED content).
