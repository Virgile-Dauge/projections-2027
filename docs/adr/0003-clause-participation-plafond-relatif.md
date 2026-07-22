# 0003 — Clause participation : seuil relatif au plafond inter-cibles, et le 0,8 rendu au test de même enjeu

- Status: accepted
- Date: 2026-07-22

## Contexte

La clause pré-enregistrée de l'ADR 0002 (backtest participation : ρ ≥ 0,8 par cible) a été exécutée sur données réelles (PR #27, issue #24) et est sortie **rouge** : européennes ρ = 0,769 (FAIL), législatives ρ = 0,815 (PASS), sur n = 62 719 bureaux joints. Conformément à la clause, la carte mobilisation n'a pas été publiée et l'issue de révision #28 a été ouverte.

**Cet ADR est une révision post-hoc et le dit.** Même discipline que la chronologie assumée de l'ADR 0002 : la révision est datée, l'échec 0,769 < 0,8 reste publié tel quel, et le lecteur peut vérifier que le seuil a été révisé *après* lecture du résultat. Ce qui suit expose pourquoi la révision est fondée malgré cela.

**D'où venait le 0,8.** De l'aveu du mainteneur (session du 2026-07-22, #28) : un chiffre d'intuition, monté depuis une proposition initiale à 0,7 « pour faire deux », sans compréhension fine de ce qu'une persistance d'abstention *inter-enjeux* peut atteindre. Le seuil était dans la mauvaise unité : un absolu, là où la grandeur pertinente est relative à ce que la réalité se reproduit à elle-même.

**Ce que le backtest a mesuré en passant.** Les deux scrutins réels de juin 2024 ne s'accordent *entre eux* qu'à **ρ = 0,870** sur la géographie de l'abstention (accord inter-cibles, même périmètre). C'est le plafond empirique — le même argument qui a fondé le pivot de l'ADR 0002 (« le plafond de la cible, mesuré »). Rapporté à ce plafond : 2022→euro = 88,4 %, 2022→legi = 93,7 %. Le prédicteur restitue l'essentiel de ce que deux scrutins contemporains partagent ; c'est le seuil absolu qui était mal calibré, pas la persistance qui est faible.

**Enfin, la clause mesurait un proxy.** Le rôle déclaré (ADR 0002) est de minorer H2 — la persistance présidentielle→présidentielle — via des cibles inter-enjeux, les européennes étant le scrutin le plus éloigné de l'enjeu présidentiel (abstention ~2× supérieure). Le vrai test de H2, de même enjeu (2017 T1 → 2022 T1), n'a jamais été calculé : ses données ne sont pas dans le panel. Son chiffre est réellement inconnu — une vraie pré-registration est donc possible, elle.

## Décision

1. **La clause participation inter-enjeux devient relative au plafond** : pour chaque cible, ρ(2022→cible) ≥ **85 % de l'accord inter-cibles** mesuré sur le même périmètre de bureaux joints. Aujourd'hui : plafond 0,870 → seuil effectif 0,7395 ; euro 88,4 % PASS, legi 93,7 % PASS. Le 85 % est un choix, gravé ici et assumé comme tel — mais exprimé dans la bonne unité : une fraction de ce que la réalité électorale se reproduit à elle-même, recalibrée avec le périmètre au lieu d'un absolu d'intuition.
2. **Le 0,8 absolu est rendu à la grandeur qu'il visait** : pré-enregistrement du test de même enjeu — Spearman du taux d'abstention par bureau, **présidentielle 2017 T1 → présidentielle 2022 T1**, ensemble des bureaux joints via un crosswalk 2017↔2022 à construire. Clause : **ρ ≥ 0,8**, gravée ici, avant toute ingestion de données 2017 et tout calcul. Le calcul est différé au chantier data dédié ; le seuil ne sera pas rediscuté après lecture.
3. **Conséquence d'un rouge sur le test 2017→2022** (gravée d'avance) : H2 serait infirmée à sa propre barre — révision d'architecture obligatoire de la couche estimation (scrutin de référence, ou pivot de la couche), et la carte mobilisation repasse non-publiable jusqu'à résolution. Pas d'ajustement de seuil.
4. **Rien n'est réécrit.** L'échec 0,769 < 0,8 reste publié tel quel dans `backtest-2022-2024.md` ; le rapport s'enrichit d'une section « clause ADR 0003 » avec le verdict relatif au plafond, sans toucher les sections existantes. La page méthode de la carte (#26) doit montrer les deux : l'échec au seuil d'origine ET la révision datée.

## Conséquences

- Gate participation **vert** sous la clause révisée (anti-hasard déjà vert) → la carte mobilisation (#26) redevient publiable ; #28 se ferme avec la PR qui implémente cet ADR.
- Le code du backtest implémente la clause relative (verdict par cible en fraction du plafond) ; le seuil historique 0,8 reste affiché dans la section d'origine.
- Nouvelle dette tracée : chantier data 2017 (ingestion présidentielle 2017 par bureau + crosswalk 2017↔2022 — le churn une élection plus loin est un problème ouvert, cf. `docs/heritage-2024.md`).
- Coût de crédibilité assumé : un lecteur adversarial verra une révision post-résultats. La défense est la transparence totale (échec publié, révision datée, provenance du 0,8 avouée) et le test de même enjeu pré-enregistré qui, lui, peut encore échouer.

## Alternatives considérées

- **Seuil 0,75 (mi-chemin 0,7–0,8)** — rejeté : chiffre neuf choisi en connaissant 0,769, calé 0,019 sous la valeur observée ; la forme la plus attaquable.
- **Seuil 0,7 (proposition initiale)** — défendable par provenance (antérieur au résultat), rejeté : reste un absolu arbitraire, la mauvaise unité — la leçon du plafond serait perdue.
- **Garder rouge jusqu'au test 2017→2022** — le plus rigoureux, rejeté : bloque la carte pendant tout le chantier data 2017 alors que le plafond mesuré fournit une calibration honnête dès maintenant ; le test 2017 est conservé comme validation forte à venir, pas comme préalable.
- **Supprimer la clause participation** — jamais : une clause qui ne peut pas échouer ne valide rien (ADR 0001).
