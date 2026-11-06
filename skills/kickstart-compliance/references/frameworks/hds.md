---
id: hds
name: HDS (Hébergeur de Données de Santé)
official_name: Certification Hébergeur de données de santé (HDS) - Référentiel de certification HDS, Exigences, version v2.1 (v2.0 approved by arrêté of 26 April 2024)
governing_body: Agence du Numérique en Santé (ANS, French Ministry of Health digital agency) owns the référentiel; certification by COFRAC-accredited (or European-equivalent) certification bodies; legal basis Code de la santé publique art. L.1111-8 and R.1111-8-8 to R.1111-11
type: sector
legal_status: certification-scheme
region: France (hosting of personal health data collected in France)
industry: health, cloud
current_version: Référentiel HDS v2.1 (publication planned October 2026, applicable three months after publication, i.e. December 2026); v2.0 (April 2024, arrêté of 26 April 2024)
superseded_by: v2.0 superseded by v2.1 for all audits from December 2026
official_sources:
  - title: ANS - Hébergement de données de santé (HDS)
    url: https://esante.gouv.fr/produits-services/hds
    accessed: 2026-11-06
  - title: ANS - Procédure de certification Hébergeur de données de santé
    url: https://esante.gouv.fr/produits-services/hds/procedure-de-certification-hebergeur-de-donnees-de-sante
    accessed: 2026-11-06
  - title: ANS - Référentiel HDS v2.1 - les évolutions à anticiper dès maintenant (15 July 2026)
    url: https://esante.gouv.fr/actualites/referentiel-hds-v21-les-evolutions-anticiper-des-maintenant
    accessed: 2026-11-06
  - title: Référentiel de certification HDS - Exigences - V2.1 (post concertation) (PDF)
    url: https://esante.gouv.fr/sites/default/files/media/document/R%C3%A9f%C3%A9rentiel_certification_HDS%20-%20FR%20-%20V2.1%20-%20post%20concertation.pdf
    accessed: 2026-11-06
last_verified: 2026-11-06T00:00:00Z
verification: partial
---

## What it is
"La certification HDS encadre [l'hébergement des données de santé à caractère personnel] et définit les exigences de sécurité applicables aux acteurs concernés." It rests on a regulatory framework, a requirements référentiel, and independent certification by an accredited body (ANS HDS page). A host must run an ISO 27001-certified ISMS extended with the HDS-specific requirements on contracts, data sovereignty and transparency (EXI 01).

## Who it applies to
Any organisation hosting personal health data for third parties within one or more of six activities (ANS procedure page):
1. Provision and maintenance of the physical sites hosting the hardware infrastructure;
2. Provision and maintenance of the hardware infrastructure;
3. Provision and maintenance of the application hosting platform;
4. Provision and maintenance of the virtual infrastructure;
5. Administration and operation of the information system containing health data;
6. Backup of health data.

A host "doit être certifié sur l'ensemble des activités d'hébergement de données de santé qu'il est susceptible de fournir à ses clients". In shared-responsibility public cloud models, a customer that performs activity 5 itself may need its own activity-5 certification (ANS FAQ on HDS page). From v2.1, State-approved third-party archivers of personal health data must also be HDS-certified (ANS v2.1 news).

## Engineering obligations
| ID | Obligation | Official reference |
|---|---|---|
| EXI 01 | ISO 27001-certified ISMS covering all health-data hosting activities, plus chapters 5–8 of the référentiel | Référentiel v2.1 EXI 01 |
| EXI 04 | ISMS scope covers all processing of personal health data, "notamment les sauvegardes et les transferts de supports matériels" | EXI 04 |
| EXI 05 | Risk assessment must consider at least: media failure, loss of control of media, information flow compromise, access control failures (granting/removing rights, ID means, "Traçabilité et imputabilité des accès", audit/pentest access), intervention control failures, misuse, HW/SW failures breaking continuity, and subjection to non-European laws | EXI 05 |
| EXI 07 | Customer interfaces and first-level support available at least in French | EXI 07 |
| EXI 13 | Plan and control the split of security responsibilities between host and customer | EXI 13 |
| EXI 15 | Let customers audit dedicated resources; provide the management summary of an independent technical audit of shared resources "datant de moins de trois ans"; let customers consult access logs to their health data | EXI 15 |
| EXI 16 | Internal audits include an audit of access traces by staff to health data and processing systems | EXI 16 |
| EXI 19 | Contract specifies how data subject rights (GDPR Arts. 15–21) are handled, how personal data breaches are reported to the controller, and DPO audit arrangements | EXI 19 |
| EXI 20 | Contract names the customer contact for incidents affecting hosted health data | EXI 20 |
| EXI 21 | Contract states quality and performance indicators, guaranteed level, measurement frequency and penalties | EXI 21 |
| EXI 23-1 / 23-2 / 23-3 | Contract describes access controls and any transfer outside the EU/EEA (remote access counts as a transfer); lists non-European laws that could force transfer or access, adequacy decisions or mitigations, and residual risks; or states that no such law applies | EXI 23-1, 23-2, 23-3 |
| EXI 27 | Reversibility: return all data, destroy copies after return, cost and lead-time terms, readable portable formats, VM/container migration terms | EXI 27 |
| EXI 28 | Store personal health data "exclusivement au sein de l'Espace Economique Européen (EEE)" and tell the customer where it is stored | EXI 28 (CSP art. R.1111-9-1) |
| EXI 29 | Any transfer, including remote access from outside the EEA, must rest on a Commission adequacy decision (GDPR Art. 45) or Art. 46 safeguards | EXI 29 |

## Deadlines and numbers
| What | Value | Official reference |
|---|---|---|
| Certificate validity | "Le certificat est délivré pour une durée de trois ans ... et chaque année, un audit de surveillance est effectué." | ANS procedure page |
| Correcting non-conformities | "trois mois après la fin de l'audit sur site" | ANS procedure page |
| v2.1 publication and application | Publication "prévue en octobre 2026"; "Il entre en application trois mois après sa publication, soit en décembre 2026. A partir de décembre 2026, tous les audits (audit initial, de surveillance, de renouvellement) sont réalisés selon la version v2.1." | ANS v2.1 news (15 July 2026) |
| v2.0 approval | "Version publiée par l'arrêté du 26 avril 2024" | Référentiel v2.1 version history |
| Shared-resource technical audit age | "dater de moins de trois ans" | EXI 15 |
| Further sovereignty requirements | "seront ajoutées au plus tard en 2027, en cohérence avec les futurs référentiels européens (EUCS)" | Référentiel v2.1 Préambule |

## Assessment and certification
The host chooses a certification body accredited by COFRAC (or a European equivalent) under an accreditation référentiel based on ISO 17021. The audit has two stages: a document review, then an on-site audit that also checks the existing ISO 27001 certification. Certification bodies send the list of certificates they issue to the ANS for publication (ANS procedure page). Under v2.1 no extra audit is needed: compliance is checked at the next surveillance or renewal audit after December 2026 (ANS v2.1 news).

## Notes
- **Catalog check:** framework-catalog.md line 64 (HDS, FR, health, certification, "Hosting health data in France") is consistent. The repo should add the six activities, the EEA storage requirement (EXI 28), the extra-EU law transparency clauses (EXI 23-2/23-3), the 3-year certificate with annual surveillance, and v2.1 taking effect in December 2026.
- **Partial:** the v2.1 PDF read is the "post concertation" version marked "Statut : Validé", but its version history still shows "V2.1 XXX 2026 ... arrêté du XXX". The approving arrêté date was not confirmed, and the Légifrance texts (CSP articles, décret n° 2026-209 of 24 March 2026) were not reachable.
- The ANS HDS landing page describes activity 4 with the same wording as activity 3 ("plateforme d'hébergement d'applications"). The procedure page and the regulation give activity 4 as "infrastructure virtuelle". This file follows the procedure page.
- v2.0 → v2.1 changes (ANS news): contracts, including those already signed, must state whether the host is subject to non-EU laws imposing transfers, and describe any transfers. State-approved third-party archivers must be certified. Remote access is considered a transfer.
