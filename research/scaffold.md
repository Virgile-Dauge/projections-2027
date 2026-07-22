# Scaffold — run projections-electorales-bureaux-2027-b0b1c4

PRIVATE planning document. MUST NOT appear in the final report.

## User Prompt (VERBATIM — gospel)

See `research/query-projections-electorales-bureaux-2027-b0b1c4.md` — canonical query file, character-for-character. Key content:

État de l'art des méthodes de projection de résultats électoraux passés sur un scrutin futur, appliqué au cas : projeter au niveau du bureau de vote (~70 000 bureaux) un rapport de force pour la présidentielle française 2027, à partir des résultats officiels (présidentielle 2022, législatives 2022/2024, européennes 2024) et des dynamiques nationales par sondages. Finalité : cartes open source pour militant·es de terrain face au RN — exigence de pertinence locale, pas de prédiction nationale.

- Axe 1 : gradation des méthodes (swing uniforme → proportionnel → matrices de transfert / inférence écologique → MRP → modèles bayésiens), pour chacune : précision à maille fine, complexité, données requises, limites, usages réels ; qui fait ça en France.
- Axe 2 : choix des données sources — biais des législatives (offre incomplète, front républicain), européennes comme mesure « sincère », obsolescence présidentielle 2022, combinaison de scrutins ; + changement des découpages de bureaux de vote entre élections (crosswalks, jeux de données INSEE / data.gouv).
- Ouverture (secondaire, ne pas creuser) : outils open source (packages R/Python d'inférence écologique, MRP).
- Hors scope : stack de visualisation / diffusion des cartes.

## Run config

- vault_tag: `projections-electorales-bureaux-2027-b0b1c4`
- query_file_path: `research/query-projections-electorales-bureaux-2027-b0b1c4.md`
- modality: **compare**
- pipeline_tier: (filled after step 1)
- language of final report: **français** (query is in French, audience = militant·es / porteur du projet francophone)

## Modality classification rationale

The query asks for a mapped gradation of method families with per-method named fields (précision, complexité, données, limites, usages) AND an applied recommendation for a specific use case (bureau-de-vote-level 2027 projection). That is proportionate per-entity depth + a committed recommendation → **compare**. It also has forecast elements (2027) but the deliverable is a methods comparison, not a prediction.

## Tier rationale

**full + argumentative.** Multi-paragraph, two-axis state-of-the-art with 11 sub-questions, 6 method families each carrying 5 named comparison fields, contested data-source questions (biais des législatives vs sincérité des européennes vs obsolescence de 2022) that demand adversarial reconciliation, and an applied recommendation for a specific use case where the quality criterion (pertinence locale) diverges from the literature's usual criterion (national accuracy). This is research-grade synthesis of conflicting evidence, not a bounded lookup. citation_style: wikilink (personal vault, no wrapper contract). pipeline_tier written to prompt-decomposition.json.

## Wrapper requirements

- No prompt.txt, no wrapper_contract.json — normal run, no external wrapper contract.
- Save path: `research/notes/final_report_projections-electorales-bureaux-2027-b0b1c4.md`
- Citation format: none imposed → default hyperresearch style (inline links / note refs).
- Terminal sections: none imposed.
- Explicit scope exclusions to enforce in drafts: no viz/diffusion stack; open-source tooling = brief section only, "ne pas creuser".
