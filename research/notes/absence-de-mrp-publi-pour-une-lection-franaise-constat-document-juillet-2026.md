---
title: Absence de MRP publié pour une élection française — constat documenté (juillet
  2026)
id: absence-de-mrp-publi-pour-une-lection-franaise-constat-document-juillet-2026
tags:
- projections-electorales-bureaux-2027-b0b1c4
- mrp
- mrp-methodology
- ciblage-terrain
- donnees-bureaux-vote
- civic-tech
created: '2026-07-21T19:15:09.218949Z'
updated: '2026-07-21T20:09:06.116410Z'
status: evergreen
type: note
tier: practitioner
content_type: review
deprecated: false
summary: 'Constat de recherche documentant l''absence, en France (juillet 2026), de
  toute application MRP à une élection française ET, plus largement, de tout projet
  de PROJECTION (pas seulement descriptif) à maille bureau de vote pour un scrutin
  futur. Après 5 requêtes MRP initiales (YouGov, Datapraxis, Cluster17, littérature
  académique — aucun MRP français) puis 6 requêtes élargies (datajournalisme, civic
  tech, GitHub, outils de cartographie électorale), le constat se confirme et se précise
  : les projets français les plus fins en maille (Souidi & Vonderscher, Nouvelle cartographie
  électorale de la France, Textuel 2026 ; Observatoire des Votes/Géoclip) sont DESCRIPTIFS/RÉTROSPECTIFS
  à maille bureau, tandis que les projets PRÉDICTIFS (France2027.eu, quiserapresident.fr)
  restent à maille NATIONALE. Aucune source ne combine maille bureau de vote et projection
  d''un scrutin futur non observé — ceci confirme la primauté méthodologique du projet,
  pas une lacune de recherche.'
---

# Absence de MRP publié pour une élection française (constat documenté)

## Question posée

Existe-t-il, à ce jour (juillet 2026), un institut de sondage, un média ou un
laboratoire académique ayant publié une application de MRP (Multilevel
Regression with Poststratification) à une élection française — présidentielle
ou législatives — avec des estimations circonscription par circonscription ou
bureau par bureau ?

## Recherches menées (5 requêtes ciblées, web search, juillet 2026)

1. « YouGov MRP France élection présidentielle circonscriptions modèle » —
   aucun résultat sur une application YouGov en France. YouGov publie des MRP
   pour le Royaume-Uni et l'Espagne (mentionné explicitement dans leur propre
   documentation méthodologique : « proven track record [...] in recent
   British and Spanish national elections »), mais aucune mention de la
   France.
2. « Datapraxis France MRP multilevel regression poststratification
   élections » — aucun résultat spécifique à Datapraxis appliquant du MRP à
   la France ; uniquement de la documentation générique sur le MRP (Wikipedia,
   bookdown, arXiv).
3. « MRP élections législatives France 2024 sondage circonscription par
   circonscription modèle statistique » — confirme au contraire que la
   pratique française reste le sondage national transposé en sièges : « Pour
   représenter la future Assemblée nationale tout en restant dans la logique
   des sondages, il faudrait en réalité mener 577 sondages, un par
   circonscription [...]. Les sondages sont réalisés au niveau national ».
   Les seules adaptations recensées sont des ajustements d'échantillonnage à
   l'offre électorale réelle par circonscription (Ipsos 19-20 juin 2024,
   Elabe 19-21 juin 2024 — cf. note Elabe fetchée séparément), pas un MRP
   (pas de modèle multi-niveaux avec poststratification sur données de
   recensement).
4. « Cluster17 méthodologie MRP regression poststratification sondage
   France » — confirme que Cluster17 (Jean-Yves Dormagen), l'institut
   français le plus « data-science » du marché, utilise le clustering
   comportemental et un redressement classique par quotas + rappel de vote,
   PAS un MRP multi-niveaux avec poststratification sur données INSEE.
5. « "multilevel regression and poststratification" France presidential
   election forecast academic paper » — aucun papier académique identifié
   appliquant le MRP à une élection présidentielle ou législative française ;
   la littérature MRP identifiée reste centrée sur les États-Unis, le
   Royaume-Uni et un cas Biélorussie (Viber/Street poll 2020).

## Constat

**Aucune source, institutionnelle, journalistique ou académique, n'a été
identifiée qui applique le MRP à une élection française** (présidentielle ou
législatives), à quelque échelle que ce soit (région, département,
circonscription, bureau de vote). Ceci malgré :

- La disponibilité de données de recensement fines (INSEE, IRIS) qui rendrait
  la poststratification techniquement possible en France comme elle l'est
  au Royaume-Uni (constituencies) ou aux États-Unis (states/districts).
- L'existence d'instituts français réputés pour leur sophistication
  méthodologique (Cluster17, Ipsos, Elabe, Ifop) qui pratiquent le
  clustering comportemental, le redressement par rappel de vote et
  l'ajustement à l'offre électorale réelle par circonscription — des
  méthodes proches en esprit du MRP (utiliser des covariables individuelles
  pour affiner une estimation locale) mais qui n'en sont pas : pas de modèle
  de régression multi-niveaux hiérarchique, pas de poststratification sur
  table de contingence croisant des variables démographiques/géographiques
  à partir du recensement.
- Le précédent anglo-saxon bien établi : YouGov publie des MRP au Royaume-Uni
  depuis 2017 (élection générale 2017, 2019, 2024) et en Espagne ; The
  Economist et d'autres publient des MRP pour les élections américaines.

## Interprétation pour le projet (pertinence directe)

« Qui fait ça en France : personne ne publie de MRP. » C'est un vide
méthodologique, pas un oubli de recherche — la littérature confirme que le
MRP reste, en 2026, une méthode anglo-saxonne (UK/US/Espagne) non transposée
au contexte électoral français par les acteurs commerciaux ou académiques
visibles publiquement. Les raisons plausibles, à confirmer par une note
distincte si besoin :

- Coût et complexité du MRP (modèle bayésien hiérarchique, panels de grande
  taille avec suffisamment de répondants par cellule de poststratification)
  face à un marché des sondages électoraux français dominé par le sondage
  national + projection en sièges par swing (cf. méthode Elabe, Ipsos).
- Absence de round régulier d'élections à circonscriptions uninominales
  suffisamment fréquent et disputé pour justifier l'investissement (les
  législatives françaises sont majoritaires à deux tours avec un design de
  circonscription différent du FPTP britannique à un tour, ce qui complique
  la transposition directe du pipeline MRP anglo-saxon).
- Le vide constitue une opportunité méthodologique pour un projet open
  source visant la maille bureau de vote : aucune méthode de référence
  française n'existe à copier, mais aucun concurrent institutionnel n'a
  non plus déjà occupé ce terrain avec un MRP publié.

## Sources consultées mentionnant le MRP en creux (pour mémoire)

- YouGov MRP Methodology (page générique, hors France) —
  https://yougov.com/articles/51585-au-election-mrp-methodology
- Cluster17 — page Méthode — https://cluster17.com/methode/
- The Conversation, « Quelles circonscriptions peuvent faire basculer les
  élections ? » (typologie de circonscriptions par vote au 1er tour,
  méthode de classification, PAS un MRP) —
  https://theconversation.com/quelles-circonscriptions-peuvent-faire-basculer-les-elections-233958

## Addendum (juillet 2026) — GAP1 corpus-critic : projection bureau de vote hors MRP

**Question élargie posée par le corpus-critic :** au-delà du MRP spécifiquement,
existe-t-il *un quelconque* projet français (datajournalisme, civic tech,
académique) de **projection/cartographie prédictive à maille bureau de vote ou
infra-communale** pour un scrutin futur (2027 ou autre) ?

### Recherches menées (6 requêtes ciblées, web search, juillet 2026)

1. « projection 2027 bureau de vote carte prédiction élection présidentielle
   France » — remonte uniquement des sites de sondages/prévisions au niveau
   NATIONAL (France2027.eu, quiserapresident.fr, élection.fr) : aucun n'a de
   sortie à maille bureau de vote.
2. « cartographie prédictive élection France bureau de vote datajournalisme »
   — révèle le projet le plus abouti identifié : Youssef Souidi & Thomas
   Vonderscher, *Nouvelle cartographie électorale de la France* (Textuel,
   janvier 2026), qui croise les ~70 000 bureaux de vote avec les données
   sociales INSEE au bureau (fetché : [[cartographie-bureaux-de-vote-rn-et-conditions-de-vie]]).
   Mais l'article de synthèse confirme explicitement que l'ouvrage est
   « surtout descriptif » et ne « prétend établir des causalités univoques » —
   aucune projection vers 2027 ou tout autre scrutin futur, malgré le teasing
   éditorial autour de la présidentielle 2027. Les « swing circos » qu'il
   introduit sont une catégorie d'analyse RÉTROSPECTIVE de la volatilité
   2017-2024, pas une sortie de modèle prédictif.
3. « le-scrutin.fr méthodologie carte électorale France » — le domaine
   `le-scrutin.fr` n'apparaît dans aucun résultat de recherche ; ne semble
   pas être un projet actif/indexé début juillet 2026.
4. « prédire résultat élection par bureau de vote France github open source »
   — les dépôts GitHub identifiés (datagouv/bureau-vote, cedricr/bureau-vote-insee,
   makinacorpus/bureaux-de-vote-reconstruction) portent tous sur la
   RECONSTRUCTION GÉOMÉTRIQUE des contours de bureaux de vote (à partir du
   Répertoire Électoral Unique / données INSEE), pas sur la prédiction de
   résultats. Le seul dépôt de prédiction électorale trouvé (projet
   utilisant random forest/régression logistique) porte sur la prédiction
   du RÉSULTAT NATIONAL en sièges à partir de sondages, pas sur une sortie à
   maille bureau.
5. « observatoire des votes geoclip méthodologie projection bureau de vote »
   — confirme que l'Observatoire des Votes (Géoclip/Cartelec) est un outil de
   VISUALISATION de résultats CONNUS au bureau de vote (« l'échelle
   géographique élémentaire est le bureau de vote »), pas un outil de
   projection vers un scrutin futur.
6. « France2027.eu méthodologie prévisions probabilistes modèle bureau de
   vote circonscription » — confirme que France2027.eu (et l'équivalent
   quiserapresident.fr) produisent des scénarios probabilistes de
   qualification et de second tour au niveau NATIONAL uniquement ; aucune
   mention de sortie à maille bureau ou circonscription dans les extraits
   disponibles.

### Constat élargi

Le constat de primauté déjà établi pour le MRP spécifiquement **s'étend au
cas général « toute méthode de projection, pas seulement MRP »** : aucun
projet français identifié (datajournalisme, civic tech, académique,
commercial) ne publie une **projection** (estimation d'un résultat futur non
encore observé) à la maille du bureau de vote ou infra-communale. Les
projets les plus proches en maille se répartissent en deux catégories
disjointes qui, ensemble, cernent exactement le vide que ce projet occupe :

- **Descriptif/rétrospectif à maille fine** : Souidi & Vonderscher (bureau ×
  INSEE), Observatoire des Votes/Géoclip (bureau, résultats connus) — la
  maille est la bonne, mais la finalité est l'explication du passé, pas la
  projection du futur.
- **Prédictif à maille grossière** : France2027.eu, quiserapresident.fr,
  modèles de sondage agrégé — la finalité (prédire un scrutin futur) est la
  bonne, mais la maille est nationale/agrégée, jamais infra-circonscription.

**Aucune source ne combine les deux : maille bureau de vote ET projection
d'un scrutin futur non observé.** Ceci confirme et renforce, avec un
échantillon de recherche élargi (6 requêtes supplémentaires ciblant
spécifiquement le datajournalisme et la civic tech, en plus des 5 requêtes
MRP initiales), le constat de primauté méthodologique pour ce projet.

### Sources consultées pour cet addendum

- [[cartographie-bureaux-de-vote-rn-et-conditions-de-vie]] — Parlons Politique
  sur Souidi & Vonderscher, *Nouvelle cartographie électorale de la France*
  (Textuel, 2026).
- Observatoire des Votes / Géoclip — https://www.geoclip.fr/lobservatoire-des-votes-un-outil-pour/
  (non fetché individuellement : contenu confirmé par extraits de recherche,
  nature descriptive sans ambiguïté).
- France2027.eu — https://france2027.eu/ (non fetché : prévisions
  probabilistes nationales, hors scope maille bureau).
- GitHub datagouv/bureau-vote, cedricr/bureau-vote-insee,
  makinacorpus/bureaux-de-vote-reconstruction — reconstruction géométrique
  des contours de bureaux, pas de prédiction électorale.
