# 0004 — Fond de carte IGN Géoplateforme sous la choroplèthe, curseur d'opacité global

- Status: accepted
- Date: 2026-07-22

## Contexte

Depuis le tracer bullet, le site n'a **aucun fond de carte externe** : « la choroplèthe EST la carte » (commentaire d'en-tête de `site/main.js`), les contours communaux servant de seul repère. Le besoin exprimé (session de grilling du 2026-07-22) est un **contexte géographique à tout zoom** — villes, rues, toponymes — pour qu'un militant se repère, du dézoom France jusqu'au quartier. Cela revient sur la décision d'origine et introduit la première dépendance runtime tierce du site (jusqu'ici : tuiles auto-hébergées R2, zéro serveur).

Sources envisagées :

- **Extrait Protomaps auto-hébergé sur R2** — cohérent avec l'infra, zéro fuite de viewport vers un tiers ; mais extract à produire et maintenir, style vectoriel + glyphes à intégrer, et les DROM exigent des extraits supplémentaires.
- **OpenFreeMap / CARTO** — hébergés, gratuits, intégration rapide ; acteurs privés tiers recevant les viewports.
- **IGN Géoplateforme (data.geopf.fr)** — Plan IGN en WMTS raster, gratuit sans clé, couvre métropole **et DROM** ; service public français.

Contrainte sémiologique : dans les modes mobilisation, `fill-opacity` **encode le rang de quantile** (ADR 0001, sortie ordinale) — la transparence n'est pas un canal libre.

## Décision

1. **Fond de carte : Plan IGN via la Géoplateforme (WMTS raster)**, inséré sous toutes les couches de données, à tout zoom. Arbitrage assumé : couverture DROM native et simplicité d'intégration raster, contre l'envoi des viewports à un serveur tiers — public et français plutôt que privé. L'auto-hébergement Protomaps reste la sortie de secours si le service se dégrade.
2. **Raster désaturé** (`raster-saturation: -1`) : le Plan IGN coloré fausserait les couleurs de blocs perçues à travers les aplats semi-transparents. Le fond `#eef0ef` actuel reste sous le raster en filet de sécurité réseau.
3. **Transparence : valeur fixe soignée + curseur global.** L'aplat Résultats 2024 passe de 0.85 à ~0.65 (ajusté à l'œil). Un curseur multiplie l'opacité de la couche de données active dans **tous** les modes — la multiplication uniforme préserve l'ordre des tranches, donc la sortie ordinale (ADR 0001) ; seul l'écart perceptuel se compresse.
4. **Le curseur ne touche jamais les repères** : liserés communes/bureaux et surtout `mob-repli-ligne`. La dégradation d'une commune en repli reste visible quel que soit le réglage utilisateur (CONTEXT.md « Repli » : jamais silencieuse).
5. **Limites affichées** : les toponymes du raster passent sous les aplats (limite assumée du raster, un passage aux tuiles vectorielles IGN les remettrait au-dessus si le besoin se confirme) ; la page méthode mentionne la dépendance IGN et l'envoi des viewports à data.geopf.fr.

## Conséquences

- Le commentaire d'en-tête de `site/main.js` (« pas de fond de carte externe ») est réécrit pour pointer vers cet ADR.
- Attribution IGN ajoutée au contrôle d'attribution MapLibre.
- Première dépendance runtime tierce du site : la disponibilité de la carte dépend en partie de data.geopf.fr ; le fond `#eef0ef` garantit une carte lisible (mode actuel) en cas de panne.
- Vie privée : les viewports des utilisateurs sont visibles de l'IGN — documenté publiquement dans la page méthode.
