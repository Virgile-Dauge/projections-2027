---
title: 'Methodology: Inside Elections’ Baseline by Congressional District – Inside
  Elections'
id: methodology-inside-elections-baseline-by-congressional-district-inside-elections
tags:
- projections-electorales-bureaux-2027-b0b1c4
- crosswalk
- precinct-level
- redistricting
- combinaison-scrutins
created: '2026-07-21T18:38:27.723549Z'
updated: '2026-07-21T18:40:37.731098Z'
source: https://insideelections.com/news/article/methodology-inside-elections-baseline-by-congressional-district
source_domain: insideelections.com
fetched_at: '2026-07-21T18:38:27.680524Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Bradley Wascher (Inside Elections, déc. 2023) détaille la méthodologie complète
  de construction de l''indice Baseline, avec un focus précis sur le problème central
  de l''Axe 2 de la recherche française : le changement de découpage des unités électorales
  (precincts, l''équivalent américain du bureau de vote) entre cycles. Sources de
  données précinct-level : retours officiels d''État/comté quand disponibles, complétés
  par VEST (Harvard Dataverse), OpenElections et le MIT Election Lab — base finale
  de plus de 2.7 millions de precincts couvrant 753 élections uniques dans les 50
  États entre 2016 et 2022 (~7950 lignes de résultats par circonscription). Méthode
  de crosswalk en 2 étapes documentée en détail : (1) le mapping GIS direct precinct→circonscription
  échoue quand les découpages sont denses ou de forme irrégulière car les fichiers
  de formes (shapefiles) ne s''alignent pas parfaitement entre grandes et petites
  géographies électorales ; solution retenue = passer par les census blocks (plus
  petits que les precincts) comme intermédiaire — chaque plan de redécoupage est accompagné
  d''un ''block assignment file'' officiel qui sert de ''pierre de Rosette'' fiable
  entre grande et petite géographie ; (2) le problème des precincts scindés entre
  plusieurs circonscriptions : quand un scrutin concurrent au même découpage existe
  (ex. scrutin gouverneur 2022 découpé par les lignes du Congrès 2022), la répartition
  se fait au prorata des voix effectivement comptées dans chaque portion du precinct
  scindé lors d''un scrutin simultané (exemple chiffré donné : precinct 14 de Novi,
  Michigan, scindé entre les 6e et 11e circonscriptions — 40% des voix démocrates
  gouvernorales assignées au 6e district car 40% des voix à la Chambre dans ce même
  precinct en provenaient) ; mais quand AUCUN scrutin concurrent n''existe pour calibrer
  la répartition (ex. un scrutin de 2018 recalculé avec le découpage 2022), Inside
  Elections choisit explicitement de répartir les voix de façon ÉGALE entre circonscriptions
  plutôt que proportionnellement à la surface ou par estimation visuelle — choix méthodologique
  assumé comme ''le plus défendable et reproductible'' malgré son caractère arbitraire,
  avec un écart maximal observé d''environ 2 points par rapport à d''autres méthodes
  de répartition (aire, estimation visuelle). Le score Baseline final est une moyenne
  tronquée (trimmed mean) qui exclut la meilleure ET la pire performance de chaque
  parti sur les scrutins retenus, pour éliminer les valeurs aberrantes dues à un candidat
  exceptionnel ou une élection sans opposition — exemple chiffré : dans le Massachusetts-9,
  en excluant les extrêmes (65% démocrate lors d''un scrutin secrétaire d''État sans
  réel enjeu, 74% républicain lors de la réélection du gouverneur Baker), le Baseline
  final est D+14.8, plus républicain que ne le suggèrent la présidentielle et la Chambre
  seules (D+18 chacune).'
---

*Suggested by [[how-to-measure-the-partisanship-of-every-house-seat-inside-elections]] — méthodologie détaillée de l'indice Baseline citée dans l'article principal*

# Methodology: Inside Elections’ Baseline by Congressional District
[Bradley Wascher](https://insideelections.com/author/bradley-wascher/)
December 8, 2023 at 4:29PM EST
To calculate[ Baseline](https://insideelections.com/news/article/how-to-measure-the-partisanship-of-every-house-seat), we include all contested partisan elections for federal and statewide offices (executive or constitutional) in the four most recent cycles, as well as any special or off-year elections during that span. The only district-based elections we consider are U.S. House races. 
These results are then combined in an index estimating the strength of a “typical” Democratic or Republican candidate in any particular congressional district.
This project requires a comprehensive collection of statewide election results by congressional district. But because most states don’t officially report down ballot races at this level, we calculated them manually.
**Data** Our first step was to collect data for each election of interest. We gathered precinct-level results from four main sources: official returns were pulled directly from state or county elections websites whenever feasible, while gaps were filled with invaluable data from [VEST](https://dataverse.harvard.edu/dataverse/electionscience), [OpenElections](https://github.com/openelections), and the [MIT Election Lab](https://github.com/MEDSL). In theory, full precinct-level results are only necessary in counties that are split between multiple districts. But we wanted to be as thorough as possible for a project of this scope and scale.
Because different sources format their results in different ways, we wrote code to systematically reshape a dataset from one source and fit it with data from another; a sample R script can be found on [GitHub](https://github.com/bradwascher/iebaseline-ma). Many races also required substantial — or in some cases total — manual input. This eventually produced a database of over 2.7 million precincts covering 753 unique elections in all 50 states between 2016 and 2022, with the full set of results by congressional district spanning approximately 7950 lines.
**Assigning Precincts to Districts** A key part of this process is determining which precincts fit into each district. For elections conducted in 2022, this is fairly straightforward: simply check the 2022 House results to see where each precinct was assigned, then apply that to the statewide races.
But because precinct boundaries can change between cycles, it's tougher to retroactively fit old elections into new districts (for example, breaking down the 2020 presidential race by the 2022 congressional lines). This is especially true at the beginning of a new decade, as entire districts were created and eliminated following census reapportionment, and many seats were heavily redrawn in redistricting.
Our initial plan was to use GIS mapping software to overlay district maps onto precinct maps, then make a list of the crossovers. This worked well for compact districts and districts with large land areas. But it proved to be less dependable when districts were densely packed or oddly shaped: sometimes the lines in the provided shapefiles didn’t align perfectly when switching between a large electoral geography (congressional districts) and a small one (precincts).
Luckily, we could convert from small to smaller. Redistricting data plans are almost always accompanied by a block assignment file that sorts census blocks into districts. Because blocks are generally smaller than precincts, this is in many cases the closest thing to an official translation between large and small geographies — a redistricting Rosetta stone.
We first overlaid precinct maps onto block maps from the [Census Bureau](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2020&layergroup=Blocks+%282020%29) to see which blocks belonged in each precinct. Then, we consulted the block assignment file to see which blocks matched with each district. With help from this middleman, we could more reliably determine which precincts fit into each district. This process was then repeated for each precinct map in each state in each election year.
**Splitting Precincts: It’s Easy** After compiling a list of precincts and their corresponding districts, there’s one final hurdle: split precincts. Although precincts are usually the smallest unit of election administration, they can still be divided between multiple districts. And when that happens, there’s almost no way to know exactly how its votes were allocated.
Thankfully, there’s a solution for elections that were run with a concurrent district map (e.g. 2022 Senate elections broken down by the congressional lines used in 2022; or — if we were analyzing last decade’s map — 2017 treasurer by the congressional districts used in 2016 or 2018).
For example, take the results of Michigan’s 2022 governor race in Novi Precinct 14. Split between the 6th and 11th districts in Oakland County, this precinct awarded 531 votes to Democratic Gov. Gretchen Whitmer, 220 votes to Republican Tudor Dixon, and 762 votes in total.
Meanwhile in that year’s House elections, 40 percent of Democratic votes, 49 percent of Republican votes, and 43 percent of total votes were cast from the portion of this precinct located within the 6th District. All other ballots came from the section in the 11th.
Therefore we would designate 212 of Whitmer’s votes — or 40 percent of her 531 total — to the 6th District, with the remaining 319 votes to the 11th. Republican votes and total votes are sorted the same way.
Similar workflows were used to allocate unassigned votes, although those were already reconciled in certain precinct-level datasets. (It is also worth noting that there are other ways to assign votes in unclear edge cases; Daily Kos Elections’ own [methodology report](https://docs.google.com/document/d/1efGEHGAQGaDGnIrdedwxVg1uUrjZYz06IPLTHRCg9zM/edit) covers them well.)
**Splitting Precincts: It’s Hard** Although the preceding procedure can be used to split precincts in elections that were conducted alongside a concurrent congressional map, it isn’t a viable option when retroactively analyzing old races using brand-new districts.
Anyone who wants to split the electoral atom must first make a key assumption about assigning votes — and there’s no single right answer.
In cases where a precinct is divided between multiple districts without any suitable comparison to a congressional race (so in our analysis, any election before 2022 broken down by the 2022 lines), our policy is to allocate a split precinct’s votes across all districts evenly.
This methodological decision notably differs from other standard techniques, such as assuming votes are allocated proportionally (e.g. measuring how much of a precinct’s land area is located in each district) or even making educated guesses by eyeballing maps. This means our toplines might differ slightly from results produced using alternate methods.
But for Baseline in particular, we believe dividing votes evenly is the most defensible and repeatable solution given the project’s scale, scope, and goals. So we calculated our own district-level breakdowns for all elections of interest — including those already crunched by other sources — to build consistency in the Baseline database and potentially spotlight any systematic errors or biases in our approach.
Comparing both sets of numbers, the largest discrepancies were in districts with a large share of split precincts, as well as in competitive seats where differences in margin stick out due to rounding. But even in most worst-case scenarios, the various precinct-splitting methods landed within approximately 2 points of each other.
Fortunately, 2016, 2018, and 2020 will eventually be replaced by 2022, 2024, and 2026 in future Baseline calculations — meaning with each passing year, this methodological distinction matters less.
**Putting It Together** Once all precincts have been properly split and allocated, the final step is to add everything up to the district level, then repeat this process for each election of interest in the district. Consider the full breakdown of results in Massachusetts’ 9th District:
Baseline’s major advantage — its depth — is quickly clear. The two most commonly cited elections at the congressional district level are the most recent House and presidential races, both of which saw the Democrat win by around 18 points in this seat. But with the added context of a dozen down ballot races, we get a better sense of the 9th’s elasticity, and of each party’s “true” vote ceiling or floor.
We can also check to see how the district’s partisan preferences hold up in different national environments: compare the margins in the 2018 cohort of races (when Democrats carried the national House popular vote by 8.6 points) to those in 2022 (when Republicans won by 2.8 points).
To calculate each party’s Baseline, simply take the trimmed mean of all previous elections — in other words, an average omitting the highest and lowest values for each party.
In the 9th District, the formula drops Democrats’ strongest performance (65 percent in the 2018 secretary of the commonwealth race that saw William Galvin earn his seventh term), as well as Republicans’ strongest performance (74 percent in then-Gov. Charlie Baker’s re-election that same year). The average also ignores each party’s weakest showing, which in this case happened to be those same races (Democrats’ 26 percent against Baker, and Republicans’ 32 percent against Galvin).
Ultimately, the 9th’s Democratic Baseline is 56.1 percent, while its Republican Baseline is 41.3 percent. The district’s Baseline margin — D+14.8 — suggests this seat is a few points more Republican-leaning than the two D+18 federal races would indicate on their own.
## Analysis
[View All](https://insideelections.com/analysis)
### [South Carolina Senate: Graham’s Death Adds Uncertainty to Competitive Race](https://insideelections.com/south-carolina-senate-grahams-death-adds-uncertainty-to-competitive-race/)
July 12, 2026
by [Nathan Gonzales](https://insideelections.com/author/nathan-l-gonzales/)
### [Kentucky 6: New Poll Fuels Democratic Optimism](https://insideelections.com/kentucky-6-new-poll-fuels-democratic-optimism/)
July 10, 2026
### [Florida 14: Calling All Castors](https://insideelections.com/florida-14-calling-all-castors/)
July 9, 2026
### [Senate Report Shorts (July 9, 2026)](https://insideelections.com/senate-report-shorts-july-9-2026/)
July 9, 2026
by [Nathan Gonzales](https://insideelections.com/author/nathan-l-gonzales/), [Inshara Ali](https://insideelections.com/author/inshara-ali/) & [Nicholas Demba](https://insideelections.com/author/nicholasdemba/)
## Podcasts
[Listen](https://inside-elections.captivate.fm)
###  [ Podcast Episode 75: Who Will be the Next Congressman to Lose a Primary? w/ Daniela Altimari of Roll Call ](https://insideelections.com/podcast/episode-75-who-will-be-the-next-congressman-to-lose-a-primary-w-daniela-altimari-of-roll-call/)
July 17, 2026
###  [ Podcast Episode 74: Inside Capitol Hill and Midterm Elections w/ Manu Raju of CNN ](https://insideelections.com/podcast/podcast-episode-74-inside-capitol-hill-and-midterm-elections-w-manu-raju-of-cnn/)
June 30, 2026
###  [ Podcast Episode 73: Maryland (Primary) Matters w/ Pamela Wood of The Banner ](https://insideelections.com/podcast/podcast-episode-73-maryland-primary-matters-w-pamela-wood-of-the-banner/)
June 18, 2026
###  [ Podcast Episode 72: New York! New York! Primaries w/ Jeff Coltin of City & State ](https://insideelections.com/podcast/podcast-episode-72-new-york-new-york-primaries-w-jeff-coltin-of-city-state/)
May 28, 2026
## Coverage
### [Secretary of State Brad Raffensperger says election audit found errors only in hand-marked ballots July 10, 2026 ](https://www.gpb.org/news/2026/07/09/secretary-of-state-brad-raffensperger-says-election-audit-found-errors-only-in-hand) ### [Daniel Cameron looks to faith as GOP Senate race comes to a close on Election Day May 26, 2026 ](https://www.kentucky.com/news/politics-government/election/article315807713.html)
