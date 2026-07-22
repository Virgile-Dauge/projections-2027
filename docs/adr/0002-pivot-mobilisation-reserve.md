# Pivot mobilisation : la réserve de voix devient le produit, l'ordre fin est déclassé

## Chronologie assumée

Le gate de l'ADR 0001 est sorti **rouge** (backtest 2022→2024, PR #21 puis main : échec du tercile compétitif Gauche/européennes à 0,433 < 0,5 et de composite ≥ mono sur la cible européennes). C'est *après* ce constat que la hiérarchie des produits a été réexaminée (session du 2026-07-22, issue #22). Nous savons qu'une révision post-résultats est suspecte par construction ; ce qui suit s'y expose en publiant tout : le backtest en échec reste publié tel quel, et cet ADR date le pivot.

## Constats qui fondent la décision

1. **Le plafond de la cible, mesuré** : dans le tercile compétitif, les deux scrutins réels de juin 2024 ne s'accordent entre eux qu'à ρ = 0,453 (Gauche) et 0,613 (Extrême droite). Notre prédicteur 2022 (0,433 / 0,565–0,612) est au plafond de ce que la réalité électorale reproduit elle-même à trois semaines d'écart. L'ordre fin des bureaux intermédiaires n'est pas prévisible — par personne.
2. **L'erreur d'objectif** : la notion de « bureau disputé » importe la logique des scrutins majoritaires (circonscriptions, swing states), où gagner l'unité rapporte un prix. La présidentielle est une circonscription nationale unique : aucun bureau ne se gagne. L'ordre fin au voisinage du seuil n'aurait jamais dû être un objectif ; le bureau de vote n'est pertinent que comme unité *géographique* de ciblage.
3. Ce que le backtest valide brillamment (ρ ensemble 0,85–0,93 par bloc majeur) est exactement ce dont la mobilisation a besoin : la géographie des gisements, pas l'ordre fin.

## Décision

1. **Produit n° 1 : la réserve de voix par bloc** (mobilisation). Définition canonique — **estimateur v1, explicitement révisable** : inscrits × abstention au **scrutin de même enjeu** (présidentielle 2022 T1 pour la cible 2027) × part estimée du bloc. Les intermittents prés→scrutins intermédiaires n'en font pas partie (ils reviennent d'eux-mêmes à enjeu présidentiel). Hypothèses affichées et ouvertes à contradiction : (H1) les abstentionnistes d'un bureau se répartissent comme ses votants ; (H2) la géographie de l'abstention présidentielle persiste 2022→2027. Un estimateur plus riche pourra remplacer celui-ci par ADR, sous la règle d'exclusivité des couches (point 7).
2. **Le rapport de force devient couche de contexte**, à maille grossière (quantiles larges). Le produit « persuasion / ordre fin des bureaux disputés » est déclassé et sa clause tercile ne conditionne plus la publication — son échec reste publié.
3. **Deux couches, deux validations.** Couche *prédiction* (structure, participation) : backtests à seuils pré-enregistrés. Couche *estimation* (la fonction réserve) : non backtestable — validée par définition ex ante, analyse de sensibilité, et appel public à contradiction. La méthode est signée par un non-spécialiste et publiée pour être challengée : c'est un livrable, pas un disclaimer.
4. **Clauses pré-enregistrées AVANT tout calcul** (mêmes règles qu'ADR 0001, seuils intouchables après lecture) :
   - *Backtest participation* : Spearman du taux d'abstention par bureau, présidentielle 2022 T1 → européennes 2024 **et** législatives 2024 T1, ensemble des bureaux joints, **ρ ≥ 0,8 sur chaque cible**. Rôle : proxy de H2 (la persistance inter-enjeux minore la persistance intra-enjeu). Accords inter-cibles publiés en contexte.
   - *Garde anti-hasard* : toute métrique publiée l'est avec son lift sur deux nulls — hasard (contexte) et **prédicteur à maille département** (clause) : la granularité bureau doit battre la granularité département sur la métrique principale, sinon pas de publication à cette maille.
5. **Inchangé d'ADR 0001** : sortie ordinale uniquement ; publication conditionnée à des backtests réfutables publiés ; les seuils existants ne sont pas modifiés — la clause tercile n'est pas « repassée au vert », elle cesse de gouverner un produit qui n'existe plus.
6. **Différé** : réserve RN de second tour (dépend de la matrice de transfert et des voix T2, cf. #18) ; affinage des pondérations du composite (conservé 50/25/25, écart mono/composite immatériel à maille grossière — tout réexamen futur devra suivre une règle ex ante).
7. **Exclusivité des couches pour les données exogènes.** v1 n'utilise que des données électorales (résultats + référentiels de jointure) ; les données socio-économiques (Filosofi via la liaison IRIS↔bureaux, déjà dans le manifeste comme plomberie dormante) sont **hors v1, dans les deux couches**. Si elles entrent un jour, elles n'alimenteront qu'UNE couche — projection ou estimation, jamais les deux : la réserve n'ayant pas de vérité terrain, un biais partagé (ex. le lien revenu→vote appris deux fois) se multiplierait dans le produit structure × abstention sans être détectable. Toute intégration future exige sa propre analyse de sensibilité.

## Conséquences

- La carte v1 est re-spécifiée : réserve par bloc en couche principale, rapport de force en quantiles larges, page « méthode, hypothèses, limites — dites-nous où ça cloche » liée depuis la carte.
- `backtest-2022-2024.md` s'enrichit (participation, lifts, plafonds inter-cibles) sans réécrire l'existant.
- L'issue #22 se ferme avec cet ADR ; #8 est re-découpée en conséquence.
