---
title: Widespread Partisan Gerrymandering Mostly Cancels
id: widespread-partisan-gerrymandering-mostly-cancels
tags:
- projections-electorales-bureaux-2027-b0b1c4
- redistricting
- elasticity
- seats-votes
created: '2026-07-21T18:31:25.739796Z'
updated: '2026-07-21T18:39:17.744918Z'
source: https://arxiv.org/pdf/2208.06968
source_domain: arxiv.org
fetched_at: '2026-07-21T18:31:25.739505Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Kenny, McCartan, Simko, Kuriwaki & Imai (Harvard/Yale, avril 2023, arXiv
  2208.06968) isolent l''effet partisan du redécoupage électoral (redistricting 2020-2022)
  de l''effet de la géographie politique et des règles de découpage, en comparant
  le plan adopté à un ensemble de plans simulés non-partisans par méthode Monte Carlo
  (technique développée dans McCartan & Imai 2023, ensemble représentatif de l''espace
  légal des plans respectant les contraintes fédérales et propres à chaque État).
  Résultat central : le gerrymandering partisan est répandu (dans 20 des 44 États
  redécoupés en 2020, l''écart au plan non-partisan est statistiquement significatif
  à 5%), mais son effet net s''annule largement au niveau national — 8.6 sièges de
  biais pro-républicain et 6.2 sièges de biais pro-démocrate à travers les États,
  pour un avantage net républicain de seulement 2.3 sièges. Pour gagner la majorité
  à la Chambre sous le plan adopté, les démocrates ont besoin de 51.1% du vote populaire
  bipartisan national, seulement 0.14 point de plus que sous le plan non-partisan
  de référence. Effet documenté et quantifié le plus directement pertinent pour la
  notion d''élasticité/réactivité : le gerrymandering réduit la compétitivité et la
  réactivité de la composition partisane de la Chambre aux mouvements du vote national
  — un point de pourcentage supplémentaire de vote populaire national ne rapporte
  que 7.8 sièges en moyenne sous le plan adopté contre 9.2 sièges sous le plan non-partisan
  de référence, soit une baisse d''environ 15% de la réactivité électorale (élasticité
  sièges-votes) imputable directement au découpage partisan. Méthodologiquement transposable
  à la France comme approche de simulation d''ensemble (plutôt que crosswalk déterministe)
  pour raisonner sur l''effet d''un changement de découpage de circonscriptions/bureaux
  sur la traduction voix-sièges, même si le contexte français (scrutin proportionnel/majoritaire
  à 2 tours, bureaux de vote très fins et non des circonscriptions à effectif variable)
  limite la transposition directe des techniques d''ensemble de cartes électorales.'
raw_file: raw/widespread-partisan-gerrymandering-mostly-cancels.pdf
---

Widespread Partisan Gerrymandering Mostly Cancels
Nationally, but Reduces Electoral Competition
Christopher T. Kenny*‡
Cory McCartan†‡
Tyler Simko∗‡
Shiro Kuriwaki§
Kosuke Imai∗†¶
April 14, 2023
Abstract
Congressional district lines in many U.S. states are drawn by partisan actors, raising concerns about gerrymandering.
To separate the partisan effects of redistricting from the effects of other factors including geography and redistricting
rules, we compare possible party compositions of the U.S. House under the enacted plan to those under a set of
alternative simulated plans that serve as a non-partisan baseline. We find that partisan gerrymandering is widespread
in the 2020 redistricting cycle, but most of the electoral bias it creates cancels at the national level, giving Republicans
two additional seats on average. Geography and redistricting rules separately contribute a moderate pro-Republican
bias. Finally, we find that partisan gerrymandering reduces electoral competition and makes the partisan composition
of the U.S. House less responsive to shifts in the national vote.
Keywords
Congressional elections • partisan bias • redistricting • representation • Monte Carlo
1
Introduction
A party that draws its own districts is likely to engage in partisan gerrymandering—the drawing of district lines by a
partisan actor to eliminate districts favorable to the opposing party and insulating their own incumbents from tough
elections. Based on the 2020 decennial Census, every U.S. state has recently redrawn their congressional districts
lines, which shape the control of the House of Representatives for the next decade. Scholars debate the extent to
which parties have gerrymandered district lines to their advantage (Chen and Cottrell, 2016; Tam Cho and Liu, 2016;
Rodden, 2019), and whether courts and reforms, which move map-drawing powers from legislatures to commissions,
can prevent such gerrymandering (Cain, 2012; Edwards et al., 2017; Henderson et al., 2018; Zhang, 2021).
Unfortunately, neither identifying gerrymanders nor quantifying their biases in electoral outcomes are straightforward.
Americans are geographically sorted and segregated along both partisan and racial lines (Schelling, 1971; Massey and
Denton, 1988; Trounstine, 2018; Brown and Enos, 2021; Brown et al., 2021; Mettler and Brown, 2022). Congressional
elections, however, occur in winner-take-all, single-member districts. When this sorting is combined with districts,
Democratic votes turn into seats less efficiently than Republican votes (Chen and Rodden, 2013; Rodden, 2019). As
such, comparing a party’s share of seats to its vote share within a state cannot establish if a districting plan, rather than
political geography, systematically advantages one party over the other.
Comparing districting plans across states or time periods is equally fraught. The geographic clustering of voters
differs both across states and over time. Cross-state comparisons further mask differences in the rules for drawing
districts. For example, some state laws limit the set of possible plans to those which preserve counties, encourage
*Department of Government, Harvard University
†Department of Statistics, Harvard University
‡C.T.K., C.M., and T.S. contributed equally to this work.
§Department of Political Science, Yale University
¶To whom correspondence should be addressed. E-mail: imai@harvard.edu. C.T.K. has served as a paid expert for the Maryland Redistricting
Commission. K.I. has served as a paid expert witness in the court cases related to the 2020 Congressional redistricting in Alabama, Kentucky, Ohio,
and South Carolina.
1
arXiv:2208.06968v2  [physics.soc-ph]  13 Apr 2023


---

partisan competition, or are more geographically compact. Federal laws, such as the Voting Rights Act of 1965 (VRA),
also constrain the set of possible plans that a state may enact without facing litigation.
We quantify the partisan effects of redistricting separately from other sources of bias such as political geography and
redistricting rules. We achieve this by comparing potential electoral outcomes under enacted district plans to those
under a set of alternative plans that are created by simulation. Simulation techniques have recently been adopted
widely by scholars, courts, and redistricting practitioners (e.g. (Chen and Stephanopoulos, 2021; Kenny et al., 2021;
Best et al., 2021), Rucho v. Common Cause (2019), Harper v. Hall (2022), or League of Women Voters of Ohio v. Ohio
Redistricting Commission (2022)). These simulations are drawn using the same geographic units and state-specific
redistricting requirements as the enacted plan. Therefore, any differences in the partisan outcomes between the
enacted plan and the simulated, non-partisan baseline demonstrate the partisan effects of redistricting.1
As explained in the Supplementary Information (SI), we improve methodologically upon a simulation approach used
by other scholars to study redistricting at a national scale (Chen and Cottrell, 2016). Specifically, we use simulation
methods that are designed to produce a representative sample from the relevant universe of plans (Fifield et al., 2020;
McCartan and Imai, 2023). We also differ from (Warshaw et al., 2022) in that we use the complete set of simulated
plans from (McCartan et al., 2022) to study state-by-state and district-by-district partisan effects.
We find that the new 2022 congressional map is biased in favor of the Republican party, but this bias is similar in
magnitude to the expected structural and geographic bias predicted by the simulated plans. To win a majority in the
US House of Representatives under the enacted plan, Democrats need more than 51.1% of the national two-party
popular vote, just 0.14 percentage points more than under the non-partisan baseline. While both parties engage in
partisan gerrymandering in many states, the resulting bias mostly cancels at the national level, giving Republicans two
additional seats. The remaining Republican advantage may be explained in part by other features like the geographic
distribution of voters (Chen and Rodden, 2013; Rodden, 2019) and redistricting rules.
Our state-by-state analysis shows that Republicans made large gains in states like Texas, Florida, and Ohio, by packing
urban Democrats. In contrast, Democrats made many smaller gains in states like Illinois, North Carolina, Pennsylvania,
and Michigan.2 As a result of state-level gerrymanders by both parties, the overall competitiveness and responsiveness
of the House are lower than our non-partisan baseline. We find that an additional percentage point increase in national
popular vote nets each party only 7.8 seats, on average, versus 9.2 under the non-partisan baseline.
2
Partisan gerrymandering is widespread, but bias mostly cancels
at the national level
For each state, we use an election model (detailed in the Materials and Methods section and SI), building on data from
(Voting and Election Science Team, 2018, 2020; MIT Election Data and Science Lab, 2018), to compute the range of
House seats the two parties are expected to win under each of the simulated, non-partisan plans from (McCartan et al.,
2022).3 These simulated plans incorporate each state’s specific requirements for map-drawing, along with federal
requirements, to ensure that the sample of simulated plans are representative of the space of legal plans (McCartan
et al., 2022; McCartan and Imai, 2023).
We then compare, for each state, the predicted electoral outcomes based on simulated districts with those under
the enacted plan. The resulting differences in electoral outcomes can be interpreted as evidence of partisan effect
(beyond political geography and redistricting rules) because the simulated plans are generated under constraints
1As noted at the beginning of this section, we call a redistricting plan a partisan gerrymander if partisan actors draw district boundaries to
create an electoral advantage for their own party. According to this definition, plans drawn by non-partisan actors may have partisan effects but are
not a partisan gerrymander. Moreover, in litigation, demonstrating both partisan effects (consequences) and partisan intent may be needed to
establish that a particular plan is a gerrymander. We do not study the partisan intent of map drawers.
2As described in more detail below and in Materials and Methods, our simulations incorporate federal and state-specific requirements for
map drawing (McCartan et al., 2022). For example, these requirements include particular goals (such as Colorado, which requires map-drawers to
maximize the number of politically competitive districts) and particular measures (such as Iowa, which has legal requirements on how to measure
compactness) when specified. Michigan requires partisan fairness as part of redistricting rules. We did not directly incorporate this criteria for two
reasons. First, it is not clear which partisan fairness metric should be used. Second, the non-partisan nature of our simulated redistricting plans can
be considered accounting for partisan fairness at least to some extent.
3These estimates are designed for cross-state comparability and do not align exactly with the corresponding estimates included in (McCartan
et al., 2022), which incorporates state offices.
2


---

which correspond to the redistricting requirements of each state. This comparison to a complete, national set of 2020
non-partisan baseline plans from (McCartan et al., 2022) differentiates our findings from existing estimates of national
biases in House elections (Warshaw et al., 2022; Economist, 2022; Rakich, 2022) (see Section A.9 of the SI for detailed
comparison with existing simulation studies). To be clear, while we can estimate differences in partisan outcomes, we
cannot necessarily identify the intent of map-drawers, which may include goals beyond packing opposite party voters,
such as protecting particular incumbents or suppressing the power of minority voters.
Furthermore, if a state’s redistricting rules themselves impart a partisan bias, our analysis would not detect that bias,
as the current legal requirements are used to construct the baseline. Similarly, compliance with the VRA can have
impacts on individual states’ partisan compositions (Chen and Stephanopoulos, 2021). As such, our estimates are best
interpreted as a measure of partisan bias given current political geography and state’s redistricting rules, either of
which could change in the future.
Our simulation methodology, however, can examine the potential partisan impact of these redistricting rules. In
Section A.10 of the SI, we illustrate this point by removing some redistricting rules and examining how doing so can
alter our empirical findings.
Fig. 1 shows clear evidence of widespread partisan gerrymandering. Bars to the right of the vertical line indicate a
Republican bias of the enacted plan, while bars to the left of the vertical line indicate a Democratic bias. Whether the
thin line crosses the zero line represents a statistical hypothesis test of the null of no difference at the 5% level. In 20 of
the 44 states that redistricted, the interval excludes zero. The intervals are not symmetric, as they are a function of
each state’s political geography, which motivates the use of sampled plans to construct the distributions. We color
each state by which party or institution drew that state’s enacted plan and order the results vertically from the most
Democratic-favoring state to the most Republican-favoring state.
Across all states, Fig. 1 shows that partisan effects are expected to contribute to 8.6 Republican seats and 6.2 Democratic
seats over a non-partisan baseline. This nets out to a Republican advantage worth around 2.3 congressional seats.
Thus, the partisan bias created by widespread gerrymandering mostly cancels at the national level, while leaving
Republicans slightly advantaged. This pattern of cancellation amounting to a net Republican advantage is also found
in an analysis of the 2010 redistricting cycle (Chen and Cottrell, 2016).
The SI presents the same partisan effects as the share of each state’s seats (as well as z-scores, in Figure S4) and in terms
of the efficiency gap (Figure S5). These results are consistent with our findings in Figure 1, showing that the states
with the largest partisan biases tend to be those where a single party controls the redistricting process.
Pro-Republican bias is found primarily in the states where the Republican party controls the redistricting process. For
example, compared to the average of the simulated maps, the plan that the Texas legislature enacted is expected to
net two additional seats for Republicans. Florida exhibits a similar, but slightly smaller bias, leading to a just under a
two seat advantage in most samples. Ohio, South Carolina, Utah, Tennessee, Iowa, Kansas, and Louisiana also show
smaller but statistically significant differences from the samples in favor of Republicans.
The maps drawn by Democratic state legislatures tend to show evidence of pro-Democratic bias. These include Illinois,
corresponding to slightly less than two seats, followed by Maryland, Oregon, New Mexico, and Nevada.
Although a majority of biased maps are drawn by state legislatures, some maps drawn by courts and commissions also
exhibit statistically significant partisan effects (e.g., Pennsylvania, North Carolina, and Michigan for pro-Democratic
maps, and Iowa for pro-Republican maps). We do not treat these maps as partisan gerrymanders because they are
drawn by non-partisan actors. That said, commission-drawn maps are not free of bias, as shown by pro-Democratic
bias in Michigan and the pro-Republican biases found for Iowa. It is also an open question whether courts should be
considered partisan actors in states such as North Carolina, where justices are elected in partisan elections.
3
Geographic paterns of partisan gerrymandering
How do states produce these partisan biases? Our national-level results, demonstrating a slight bias in favor of the
Republican party, align with those of existing estimates from (Warshaw et al., 2022; Economist, 2022; Rakich, 2022).4
4In a hypothetical tied national election, both (Economist, 2022) and (Rakich, 2022) predict Democrats winning 210 seats, with (Warshaw et al.,
2022) slightly more conservative at 205 seats.
3


---

Texas (38)
Fla. (28)
Tenn. (9)
Utah (4)
Ohio (15)
S.C. (7)
Va. (11)
Ga. (14)
Iowa (4)
Okla. (5)
Kan. (4)
Ariz. (9)
Ark. (4)
Colo. (8)
La. (6)
Ala. (7)
Maine (2)
Ind. (9)
Minn. (8)
Neb. (3)
R.I. (2)
Wis. (8)
Idaho (2)
W.Va. (2)
N.H. (2)
Wash. (10)
Hawaii (2)
Miss. (4)
Conn. (5)
Mont. (2)
Ky. (6)
Mass. (9)
N.Y. (26)
Mo. (8)
Calif. (52)
Nev. (4)
N.J. (12)
N.M. (3)
Mich. (13)
Ore. (6)
N.C. (14)
Md. (8)
Pa. (17)
Ill. (17)
NATIONAL
D+2
No difference
R+2
R+4
Difference of seats won under enacted plan
compared to non-partisan baseline
← Favors Republicans          States, ordered by seat difference          Favors Democrats →
Control of redistricting
Commission
Court
Democrats
Mixed
Republicans
Figure 1: Estimated state and national level partisan bias. Estimates show the expected Republican seats under
each non-partisan baseline plan subtracted from the expected Republican seats under the enacted plan. Bars
to the right indicate the enacted plan gives more seats to Republicans, while to the lef indicates more seats
for Democrats. The vertical black line indicates no partisan bias. The thick and thin bars show 66% and 95%
intervals of the simulated plans, respectively, afer averaging over uncertainty in future electoral swings at the
national and district level. The point indicates the median. States are colored by the actors that controlled the
map drawing in in each enacted plan, and are ordered vertically from the largest Democratic-favoring state to the
largest Republican-favoring state. The number of seats in each state is shown in parentheses. In Section A.5 of the
SI, we rescale the eﬀects as a share of the state’s seats and as z-scores.
4


---

1
2
3
4
5
6
7
1
2
3
4
5
6
7
8
9
1
2
3
4
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
1
2
3
4
5
6
7
8
1
2
3
4
5
DE
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
1
2
3
4
5
6
7
8
9
10
11
12
13
14
1
2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
1
2
3
4
5
6
7
8
9
1
2
3
4
1
2
3
4
1
2
3
4
5
6
1
2
3
4
5
6
1
2
1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
10
11
12
13
1
2
3
4
5
6
7
8
1
2
3
4
1
2
3
4
5
6
7
8
1
2
1
2
3
1
2
3
4
1
2
1
2
3
4
5
6
7
8
9
10
11
12
1
2
3
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
1
2
3
4
5
6
7
8
9
10
11
12
13
14
ND
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
1
2
3
4
5
1
2
3
4
5
6
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
1
2
1
2
3
4
5
6
7
SD
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
1
2
3
4
VT
1
2
3
4
5
6
7
8
9
10
11
1
2
3
4
5
6
7
8
9
10
1
2
1
2
3
4
5
6
7
8
WY
AK
1
2
D+50
D+25
Even
R+25
R+50
Change in win probability
versus simulations
Figure 2: Cartogram of new congressional districts, each shaded by the diﬀerence between the probability of
a party representing the district under the enacted plan and the voter-weighted average of the probability of a
party representing the voters in that district under a non-partisan baseline. See Section A.7 of the SI for details on
the computation of each probability. Numbers represent the congressional district’s number in the enacted plan.
Congressional districts are roughly equal in population so the cartograms are drawn to be roughly equal in size,
while preserving the relative geographic locations of each district within the state. This cartogram style is inspired
by the Daily Kos (htp://dkel.ec/map).
Our simulation approach, creating a set of 2020 counterfactual maps, allows us to further investigate the source of
these biases at the state and district levels. Fig. 2 disaggregates the estimates in Fig. 1 to the district level, showing the
partisan bias of districts in each state.
The map is colored by the difference in the probability of being won by Republican and Democratic candidates between
the enacted map and the simulated plans. Light colors indicate that the election outcome under the enacted plan is
expected to be similar to the outcomes in the same geographic area across the non-partisan baseline plans, while
darker colors indicate larger differences. Districts in red indicate that an enacted district advantages Republicans
compared to the simulated plans, while blue districts indicate a Democratic advantage. As explained in the Materials
and Methods section, this map builds upon recent work that focuses on precinct-level quantities, such as partisan
dislocation (DeFord et al., 2022), and is closely related to a general framework to evaluate districting plans at the
individual voter level (McCartan and Kenny, 2022).
We see that enacted plans in some states have only small differences from the simulated plans. For example, Mas-
sachusetts and West Virginia each have only muted shades of red and blue—they have only small differences in each
district. But, other states have more substantial differences. In North Carolina, where the state supreme court drew
the map, its pro-Democratic bias stems in part from the drawing of districts 12 and 14 in the Charlotte area. The
5


---

enacted plan splits Charlotte through the middle, which creates two Democratic districts when combined with the
suburbs. In contrast, the simulated alternative plans typically draw a full district within Charlotte’s enclosing county.
In Texas, the enacted plan strongly favors Republicans, as seen in Fig. 1. The Texas legislature made two districts in the
Houston area, 22 and 38, far safer for Republicans than expected. This corresponds to the packing of urban Democratic
voters in districts 7, 9, 18, and 29. Some of these districts are overwhelmingly composed of racial minorities, and the
VRA does compel states to draw such districts in some circumstances. However, the enacted plan appears to pack these
districts with Democratic voters far beyond what may be needed to ensure that the district usually elects minority
voters’ preferred candidates. Similar approaches in Austin and Dallas areas cement the net bias towards Republicans.
4
Partisan gerrymandering reduces electoral competition and re-
sponsiveness
We also analyze the impact of partisan effects on each party’s ability to translate votes into seats under different
electoral environments. Widespread gerrymandering could limit the electoral power of voters in many affected
districts, even if biases mostly cancel out between parties at the national level. We first estimate a baseline partisanship
for each precinct by averaging the 2016 and 2020 presidential elections. We then tally the baseline within each of
the enacted and simulated districts to obtain an estimate of district-level baseline partisanship. Finally, we use these
estimates to examine electoral competitiveness under the enacted and simulated plans.
Non-partisan
simulations
Enacted plan
0
20
40
60
10%
20%
30%
40%
50%
60%
70%
80%
90%
Average Democratic district vote share
Number of seats
Figure 3: The histogram shows the distribution of expected district voteshares under the enacted districts. The
overlaid 66% and 95% confidence intervals show the range of the same quantity under our non-partisan simulated
baseline.
Fig. 3 shows the distribution of district-level partisanship for the enacted and simulated maps. The enacted plans
across all states create significantly fewer highly competitive seats, where the baseline vote share is between 47.5% and
52.5%. Only 34 out of 435 districts under the enacted districting plans fall into this category, compared to 50 in the
non-partisan baseline. There are fewer seats which lean Republican (52.5–57.5% vote share) than expected, but more
safe Republican seats (62.5–67.5% vote share) than expected. This reflects the Republican gerrymandering strategy of
shoring up Republican seats to insulate them from elections which swing towards Democrats. In contrast, Democrats
appear to have fewer moderately safe seats under the enacted plan than the simulated plans.
We can translate these baseline partisanship estimates into a national seats-votes curve, which relates the national
popular vote share of each party in House elections to the share of House seats they win under each redistricting plan
(Tufte, 1973; Katz et al., 2020). Such an analysis is useful since each future election may be subject to a different electoral
environment (e.g., Republicans are generally expected to do well in a Democratic president’s midterm election). To do
so, we use the election model detailed in the Materials and Methods section to calculate the expected number of seats
each party would win under a range of national popular vote shares.
6


---

Majority
Dem., Non-partisan baseline
Rep., Non-partisan baseline
Partisan bias
51.1% vote share needed
to win a majority
180
190
200
210
220
230
240
250
260
42%
44%
46%
48%
50%
52%
54%
56%
58%
45%
46%
47%
48%
49%
50%
51%
52%
53%
54%
55%
National vote share
Seats won
Figure 4: Seats-votes curves that show how each party can translate a national popular vote into congressional
seats. The curve for Democratic seats and votes under the enacted plan is solid blue, while the curve for Republicans
are dashed red. Curves representing plans simulated under our non-partisan baseline are ploted as thin gray
lines. Partisan bias in this figure indicates the deviation from partisan symmetry evaluated at a voteshare of 0.5,
following the definition of (Katz et al., 2020).
Fig. 4 presents our estimate of the national seats-votes curve for each party under the enacted plans with the vote
shares ranging from 45% to 55%. The seats-votes curve under each of the 5,000 simulated non-partisan plans are
shown in light gray. The results show that in competitive elections, the seats-votes curve indicates a bias against
Democrats. If Democrats win 50% of the popular vote, we estimate them to win around 210 out of 435 seats. It is not
until the Democratic party wins 51.1% of the vote that they would receive half of the seats in the House.
This Democratic disadvantage, however, cannot be entirely attributed to partisan effects of redistricting. Even if states
did not draw a plan with partisan bias, the Democratic party would still be at a disadvantage. Compared to the range
of alternative seats-votes curves in gray, we see that if the national environment were to trend towards a 50% national
vote share between parties, the difference between the national bias and the baseline geographic and rule-based bias
disappears. Earlier work has shown that the geographic distribution of voters systematically benefits the Republican
party (Chen and Rodden, 2013; Rodden, 2019). We find that this dynamic is likely to be still present in 2020 though
the bias is due to the combination of political geography and redistricting rules. On average, under our non-partisan
baseline plans, Democrats must win 50.9% of the popular vote in order to win half of the seats—very similar to the
enacted plan.
Nevertheless, partisan bias in redistricting reduces electoral responsiveness. Responsiveness describes the rate at
which changes in the vote share result in changes in the seat share. Notice that the enacted plan’s seats-votes curve has
a flatter slope than the simulated plans. This indicates that the enacted plan is less responsive to national swings in the
vote in competitive elections.
Fig. S7 in the SI shows this responsiveness, measured as the number of seats gained by Democrats for a one percentage
point increase in vote share. For typical vote shares (45–55%), the enacted plan is around 16% less responsive than a
non-partisan baseline would predict. That is, each additional percentage point of the national vote nets 7.8 seats, on
average, under the enacted plan, compared to an expectation of 9.2 seats under the simulated plans. This is a direct
result of the smaller number of competitive seats in the enacted plan, as documented above.
5
Discussion
The boundaries of districts in the U.S. Congress are drawn by individual states, each with different political geography
and redistricting rules. Therefore, traditional approaches that seek to estimate the partisan effect of redistricting by
leveraging information from other states and/or previous periods can potentially be misleading. Simulation-based
7


---

approaches address this issue, but prior attempts have neither fully accounted for the state-specific nature of these
differences nor taken advantage of recent advances in redistricting simulation algorithms (Chen and Rodden, 2013,
2015; Chen and Cottrell, 2016). Improved data and methods used in our analysis can better characterize the magnitude
of these biases for all fifty states, while incorporating the state-specific redistricting criteria (McCartan et al., 2022).
We find that congressional districting plans from the 2020 redistricting process exhibit widespread partisan effects—
often, the plans differ from the average sampled plan and, in many cases are statistical outliers, compared to the
sampled plans. We also find that partisan bias created by redistricting largely cancels out at the national level. However,
this does not mean that the partisan gerrymandering — and the political contestation over redistricting — was
inconsequential. Many states have enacted districting plans with partisan biases that decrease electoral competitiveness
and responsiveness, limiting the voter’s ability to hold politicians accountable.
The simulated baseline plans allow us to show that geographic and institutional features disadvantage Democrats,
even absent partisan gerrymandering. In fact, we show that these structural factors dominate the final Democratic
disadvantage in the enacted plans. Finally, our analysis finds partisan effects given the current geographic and
institutional composition of the House. Map-drawers may also gain partisan advantage through manipulations of the
redistricting process itself, as different rules may have biased partisan implications. These findings illuminate the
inherent difficulty of producing a fair national House map when it is drawn piecemeal by fifty autonomous political
units. More research is needed to further advance our understanding of the crucial relationship between votes and
seats that structures our democracy.
Materials and Methods
Data Availability
All data and code necessary to replicate our analyses is available on the Harvard Dataverse at https://doi.org/10.7
910/DVN/JI1U8X.
50stateSimulations
For our analyses, we rely on 50stateSimulations, which contains 5,000 sampled redistricting plans and accompanying
precinct-level election and demographic data for each state (McCartan et al., 2022). These data are publicly available
on the Harvard Dataverse at https://doi.org/10.7910/DVN/SLCD3E. The source code which generates the sampled
plans is available on GitHub at https://github.com/alarm-redist/fifty-states/. Election data were originally
collected by the Voting and Election Science Team (https://dataverse.harvard.edu/dataverse/electionscience).
For the 44 states with more than one congressional district, 50stateSimulations identifies the state’s legal requirements,
incorporatesthemintomathematicalconstraints, andsamplesplansfromatargetdistributionthatcorrespondstothose
constraints using the open-source software (Kenny et al., 2022). Requirements which involve a legal determination,
such as compliance with the Voting Rights Act, are assumed met by the enacted plan. The level of compliance is then
matched for the simulated set. Note that the legality of some of the enacted plans is still in dispute. Our analysis
does not attempt to address the legal issues raised in these court cases. 50stateSimulations further attempt to match
non-partisan discretionary criteria, such as number of counties split, number of municipalities split, and compactness
of districts. The criteria incorporated, information as to what law or rule sets the requirement, and interpretation of the
requirement for each state are available on the aforementioned Harvard Dataverse site, in each state’s documentation
file. For the six states where there is only one congressional district (Alaska, Delaware, North Dakota, South Dakota,
Vermont, and Wyoming), we supplement this with the only possible plan, repeated 5,000 times so that these districts
are weighted equally in our analysis.
Electoral modeling
To understand the electoral implications of 2020 redistricting plans in the upcoming decade, our findings rely on a
statistical model of elections. An election model uses observed past election results to quantify the uncertainty over
future election results which take place under a different set of redistricting plans.
8


---

Our goal is to estimate the partisanship of each district in the enacted plan and also for alternative districts, with
different geographic configurations, in each of the 5,000 simulated plans. To do this, we use precinct-level election
data and estimate the precinct-level baseline partisanship as an average of the 2016 and 2020 presidential elections.
We use previous presidential elections because the same candidate is on the ballot across the entire nation, unlike
for Senate or House races. This practice is also adopted by many elections analysts and is used in the Cook Partisan
Voting Index.
Specifically, we take the mean of the Democratic two-party vote share in each precinct across the two elections, and
separately take a geometric mean of the turnout across the elections (due to its skewed distribution), to produce a
baseline number of Democratic and Republican votes for each precinct. For example, the baseline Democratic vote
count estimate for precinct j, denoted by ˆDj, can be written as
ˆDj = 1
2

D16j
D16j + R16j
+
D20j
D20j + R20j

×
q
(D16j + R16j)(D20j + R20j)
where Dtj, Rtj are the Democratic and Republican vote counts for the precinct in year t. A geometric mean for
turnout values corresponds to the usual mean for log-turnout values. In Kentucky, some detailed 2020 election data is
missing, and so we impute it from county-level and past precinct-level results, as described in Section A.3 of the SI.
We model the two-party Democratic vote share in each district yit for an election t as
logit(yit) = αi + βt + εit,
(1)
βt
iid
∼N(0, σ2
β),
εit
iid
∼tν(0, σ2
ε),
where αi is district’s baseline partisanship, βt is election-to-election national swing, and εit is district-election specific
error. This is the Stochastic Uniform Partisan Swing model of (Gelman and King, 1994), but put onto a logit scale.
Estimating this model poses challenges because of data limitations. In particular, each different simulated plan has its
own set of αi which must be estimated. However, since these plans are hypothetical, we have no data on elections
conducted under these plans. So we fix αi for each district in the enacted plan and the 5,000 simulated plans by simply
aggregating our estimate of the precinct-level baseline vote counts for the district. Specifically, for a given plan p, we
compute
ˆαip =
P
j∈Jip ˆDj
P
j∈Jip ˆDj + P
j∈Jip ˆRj
where Jip indicates the set of precincts that are assigned to district i in a redistricting plan p.
Additionally, since we use the model to predict future elections, we will not know βt and εit. Instead, these are
drawn from the normal distributions with the variance of σ2
β and t-distribution with ν degrees of freedom and scale
σ2
ε, respectively, under this model. This injects the appropriate amount of uncertainty about future national and
district-specific election swings into our election predictions, which are then propagated to uncertainty in our topline
estimates that are presented as figures in the main text.
Thus, to create election predictions, it remains to estimate σ2
β, σ2
ε, and ν; once these are estimated along with our
baseline estimates ˆαi, we can simulate hypothetical future election outcomes. To estimate σ2
β, σ2
ε, and ν, we fit the
model given in (1) to historical House elections. The data (MIT Election Data and Science Lab, 2017) contains almost
all House elections since 1976. We study only the races contested by exactly one candidate from each party.
In fitting this model, we are constrained by the lack of historical presidential election data disaggregated to the
congressional district level. This means that we cannot create estimates of ˆαi in the manner described above that we
use for our future predictions. Instead, in the historical election model only, we fit αi as a random effect, which is
specific to each district but constant across elections. To account for redistricting, which changes the districts every
decade, we estimate a separate αi for each district-decade combination (for example, WA–07 from 2012–2020 would
receive a single random intercept) as a random effect. None of the αi estimated as part of our historical House election
9


---

model are used in the predictions of future elections. The use of random effects here is only to properly allocate the
total variability in election returns to three sources: district-specific, year-specific, and district-year-specific effects.
Only the estimates of σ2
β, σ2
ε, and ν are used to produce the results in the main text. This modeling choice, as well as
the overall predictive performance of the model, are investigated further in Section A.4 of the SI.
Section A.2 of the SI also provides computational details on how we use the fitted election model to estimate the
average number of seats Democrats will win under a particular plan.
The SI also provides computational details on how we use the fitted election model to estimate the average number of
seats Democrats will win under a particular plan.
References
Best, R. E., Lem, S. B., Magleby, D. B., and McDonald, M. D. (2021). Do Redistricting Commissions Avoid Partisan
Gerrymanders? American Politics Research, page 1532673X211053216. Publisher: SAGE Publications Inc.
Brown, J. R. and Enos, R. D. (2021). The Measurement of Partisan Sorting for 180 Million Voters. Nature Human
Behaviour.
Brown, T., Mettler, S., and Puzzi, S. (2021). When Rural and Urban Become “Us” versus “Them”: How a Growing
Divide is Reshaping American Politics. The forum : a journal of applied research in contemporary politics, 19(3):365–393.
Place: BERLIN Publisher: De Gruyter.
Bürkner, P. C. (2018). Advanced Bayesian multilevel modeling with the R package brms. The R Journal, 10(1):395–411.
Cain, B. E. (2012). Redistricting Commissions: A Better Political Buffer? The Yale Law Journal, page 37.
Carter, D., Herschlag, G., Hunter, Z., and Mattingly, J. (2019). A merge-split proposal for reversible Monte Carlo
Markov chain sampling of redistricting plans. arXiv preprint arXiv:1911.01503.
Cervas, J. and Grofman, B. (2022). Using Folded Seats-Votes Curves to Compare Partisan Bias in the 2020 Presidential
Election with Partisan Bias in the Five Other Presidential Elections in the 21st Century. Presidential Studies Quarterly,
52(2):429–435.
Chen, J. and Cottrell, D. (2016). Evaluating partisan gains from Congressional gerrymandering: Using computer
simulations to estimate the effect of gerrymandering in the U.S. House. Electoral Studies, 44:329–340.
Chen, J. and Rodden, J. (2013). Unintentional gerrymandering: Political geography and electoral bias in legislatures.
Quarterly Journal of Political Science, 8(3):239–269.
Chen, J. and Rodden, J. (2015). Cutting Through the Thicket: Redistricting Simulations and the Detection of Partisan
Gerrymanders. Election Law Journal: Rules, Politics, and Policy, 14(4):331–345. Publisher: Mary Ann Liebert, Inc.,
publishers.
Chen, J. and Stephanopoulos, N. O. (2021). The Race-Blind Future of Voting Rights.
DeFord, D., Duchin, M., and Solomon, J. (2021). Recombination: A family of Markov chains for redistricting. Harvard
Data Science Review. https://hdsr.mitpress.mit.edu/pub/1ds8ptxu.
DeFord, D. R., Eubank, N., and Rodden, J. (2022). Partisan dislocation: A precinct-level measure of representation and
gerrymandering. Political Analysis, 30(3):403–425.
Ebanks, D., Katz, J. N., and King, G. (2022). If a statistical model predicts that common events should occur only once
in 10,000 elections, maybe it’s the wrong model.
Economist, T. (2022). America’s congressional maps are a bit fairer than a decade ago.
Edwards, B., Crespin, M., Williamson, R. D., and Palmer, M. (2017). Institutional Control of Redistricting and the
Geography of Representation. The Journal of Politics, 79(2):722–726.
Fifield, B., Imai, K., Kawahara, J., and Kenny, C. T. (2020). The essential role of empirical validation in legislative
redistricting simulation. Statistics and Public Policy, 7(1):52–68.
10


---

Gelman, A. and King, G. (1994). A unified method of evaluating electoral systems and redistricting plans. American
Journal of Political Science, pages 514–554.
Golub, G. H. and Welsch, J. H. (1969). Calculation of gauss quadrature rules. Mathematics of computation, 23(106):221–
230.
Grofman, B. (1983). Measures of bias and proportionality in seats-votes relationships. Political Methodology, 9(3):295–
327.
Henderson, J. A., Hamel, B. T., and Goldzimer, A. M. (2018). Gerrymandering Incumbency: Does Nonpartisan
Redistricting Increase Electoral Competition? The Journal of Politics, 80(3):1011–1016.
Kastellec, J. P., Gelman, A., and Chandler, J. P. (2008). The playing field shifts: Predicting the seats-votes curve in the
2008 U.S. house elections. PS: Political Science and Politics, 41(4):729–732.
Katz, J. N., King, G., and Rosenblatt, E. (2020). Theoretical foundations and empirical evaluations of partisan fairness
in district-based democracies. American Political Science Review, 114(1):164–178.
Kenny, C. T., Kuriwaki, S., McCartan, C., Rosenman, E. T. R., Simko, T., and Imai, K. (2021). The use of differential
privacy for census data and its impact on redistricting: The case of the 2020 U.S. Census. Science Advances,
7(41):eabk3283.
Kenny, C. T., McCartan, C., Fifield, B., and Imai, K. (2022). redist: Simulation methods for legislative redistricting.
Available at The Comprehensive R Archive Network (CRAN).
King, G. and Browning, R. X. (1987). Democratic representation and partisan bias in congressional elections. American
Political Science Review, 81(4):1251–1273.
Massey, D. S. and Denton, N. A. (1988). The Dimensions of Residential Segregation. Social Forces, 67(2):281–315.
McCartan, C. and Imai, K. (2023). Sequential Monte Carlo for sampling balanced and compact redistricting plans.
Annals of Applied Statistics. Forthcoming.
McCartan, C. and Kenny, C. T. (2022). Individual and differential harm in redistricting.
McCartan, C., Kenny, C. T., Simko, T., Garcia III, G., Wang, K., Wu, M., Kuriwaki, S., and Imai, K. (2022). Simulated
redistricting plans for the analysis and evaluation of redistricting in the united states. Scientific Data, 9(1):689.
Mettler, S. and Brown, T. (2022). The Growing Rural-Urban Political Divide and Democratic Vulnerability. The
ANNALS of the American Academy of Political and Social Science, 699(1):130–142.
MIT Election Data and Science Lab (2017). U.S. House 1976–2020.
MIT Election Data and Science Lab (2018). County Presidential Election Returns 2000-2020.
Rakich, N. (2022). The new national congressional map is biased toward republicans.
Rodden, J. A. (2019). Why cities lose: The deep roots of the urban-rural political divide. Basic Books.
Rosenman, E., McCartan, C., and Olivella, S. (Forthcoming). Recalibration of predicted probabilities using the “logit
shift”: Why does it work, and when can it be expected to work well? Political Analysis.
Schelling, T. C. (1971). Dynamic Models of Segregation. The Journal of Mathematical Sociology, 1(2):143–186. Publisher:
Routledge.
Stephanopoulos, N. O. and McGhee, E. M. (2015). Partisan gerrymandering and the efficiency gap. U. Chi. L. Rev.,
82:831.
Tam Cho, W. K. and Liu, Y. Y. (2016). Toward a Talismanic Redistricting Tool: A Computational Method for Identifying
Extreme Redistricting Plans. Election Law Journal, 15(4):351–366. Publisher: Mary Ann Liebert, Inc.
Trounstine, J. (2018). Segregation by Design: Local Politics and Inequality in American Cities. Cambridge University Press,
Cambridge.
11


---

Tufte, E. R. (1973). The relationship between seats and votes in two-party systems. American Political Science Review,
67(2):540–554.
Voting and Election Science Team (2018). 2016 Precinct-Level Election Results.
Voting and Election Science Team (2020). 2020 Precinct-Level Election Results.
Warshaw, C., McGhee, E., and Migurski, M. (2022). Districts for a New Decade—Partisan Outcomes and Racial
Representation in the 2021–22 Redistricting Cycle. Publius: The Journal of Federalism, 52(3):428–451.
Zhang, E. R. (2021). Bolstering Faith with Facts: Supporting Independent Redistricting Commissions with Redistricting
Algorithms. California Law Review.
12


---

A
Supplementary Information
A.1
Details of the simulation algorithm
Here we provide a brief overview of the simulation algorithm detailed in (McCartan and Imai, 2023).
In contrast to many existing simulation approaches, which use Markov Chain Monte Carlo (MCMC), the algorithm
uses Sequential Monte Carlo (SMC). MCMC algorithms operate sequentially, starting with a valid redistricting plan
and making changes to a district or pair of districts one at a time. The SMC algorithm draws many maps in parallel,
which reduces the overall dependence between plans and increases the efficiency of the algorithm.
The algorithm starts with many copies of a blank map (i.e., one with no districts drawn) and draws a district at random
on each map. This drawing process is achieved using a spanning-tree proposal distribution, which is similar to the
spanning-tree proposal distribution used by some of the existing MCMC algorithms (Carter et al., 2019; DeFord
et al., 2021). Based on the district drawn and the constraints that the researcher has specified for the simulation,
the SMC algorithm assigns each plan a weight before moving on to the next district. For the next and subsequent
districts, partially-drawn plans are sampled from the previous iteration using their weights. A random new district is
drawn on each map and checked for conformity with the population tolerance constraint. If a map does not satisfy the
population constraint, it is discarded. This process is repeated until enough plans have been generated for this step.
Weights are then recalculated for all the plans.
Overall, the algorithm repeats the splitting procedure n −1 times, where n is the number of districts needed. In the
end, the algorithm outputs a set of sampled plans and weights.
While the algorithm has theoretical convergence guarantees, it is important to check for convergence or lack thereof
in practice. As detailed in (McCartan and Imai, 2023) and (McCartan et al., 2022), we perform an extensive battery of
diagnostic checks to ensure the quality and accuracy of the samples we produce with the algorithm.
A.2
Computing expected Democratic seats from the election model
In principle, it is simple to compute the average number of seats Democrats will win under a particular redistricting
plan. We can simulate new vote shares for each district from the fitted election model. Then for each simulation draw,
we can compute the number of seats the Democrats win. Averaging this number across simulation draws yields an
estimate of the average Democratic seats.
However, this approach introduces Monte Carlo error controlled by the number of draws from the election model.
When the number of Democratic seats must be estimated for 50 states and nationwide, not just for the enacted plans
but also for 5,000 simulated plans, it can prove computationally costly to have more than a few hundred draws from
the election model. The Monte Carlo error will then aggregate as we sum across districts and states, and will generally
not be negligible compared to the variance from the redistricting simulation.
To address this issue, we can exactly compute the expectation of the number of Democratic seats with Gauss-Hermite
quadrature. Specifically, in a state with n districts, and given estimates ˆα of the baseline partisanship of each district,
we wish to estimate
E
" n
X
i=1
1{yit > 1
2}
 α = ˆα
#
=
n
X
i=1
E[P(yit > 1
2 | αi = ˆαi, βt) | αi = ˆαi]
=
n
X
i=1
E[ ˆFε(αi + βt) | αi = ˆαi],
where the second step follows from the law of iterated expectations, and in the last step ˆFε is the CDF of the error
term in the fitted election model (which is a plug-in estimate from the historical House election model). Since the final
expectation conditions on αi, it is only averaging over βt, which is drawn from a N(0, σ2
β) distribution. Thus we can
estimate E[ ˆFε(αi + βt) | αi = ˆαi] to high accuracy using Gauss-Hermite quadrature (Golub and Welsch, 1969), and
13


---

-2
-1
0
1
2
-1
0
1
2
Precinct-result baseline (logit scale)
Fitted district-decade random effect (logit scale)
Figure S1: Posterior point predictions and intervals for decade-district random eﬀects, versus the 2016–2020
partisan baseline calculated from precinct-level presidential returns. The red line indicates perfect agreement.
without resorting to random draws from the election model. Specifically, we use an order-6 approximation, which
simulation testing showed was more than enough for extremely high accuracy.
A.3
Missing election data imputation
For Kentucky, where we are missing 2020 precinct-level data, we imputed precinct-level results by shifting the
precinct-level vote shares from the 2016 election on the logit scale by the amount that the enclosing county swung (see
(Rosenman et al., ming) for a principled justification of this practice). County-level data is available for both elections
from (MIT Election Data and Science Lab, 2018). Specifically, we imputed
\
D20j
D20j + R20j
= logit−1

log D16j
R16j
−log D16c
R16c
+ log D20c
R20c

where the subscript c indicates the corresponding county-level data (recall that the log of the ratio of each party’s vote
is the logit of the two-party vote share). We also shift turnout on the log scale in a similar fashion.
A.4
Electoral model validation
It is important to validate the electoral model because fitting a random effect to past House elections is not the same
as predicting a partisan baseline using past presidential results. Figure S1 shows the results of this validation. We
compare the fitted random effects for the 2010 decade-districts to the baseline that would be obtained by aggregating
our precinct-level partisan baseline to 2010 district boundaries. The agreement is generally excellent, despite the
baseline only using information on two of the three presidential elections conducted during this period. The few large
deviations indicate particularly strong candidate or regional effects (like Democrats holding the Montana at-large
district, for instance).
14


---

0.000
0.025
0.050
0.075
100
125
150
175
Dem. seats (averaging over nat'l environment)
Density
0.000
0.025
0.050
0.075
100
125
150
175
Dem. seats (conditioning on nat'l environment)
Density
Figure S2: Posterior predictive distribution and actual results for 255 2018 House elections in the historical dataset.
On the lef, predictions are unconditional; on the right, they are conditional on the national environment.
It is important to validate the electoral model because fitting a random effect to past House elections is not the same
as predicting a partisan baseline using past presidential results. Fig. S1 shows the results of this validation. We
compare the fitted random effects for the 2010 decade-districts to the baseline that would be obtained by aggregating
our precinct-level partisan baseline to 2010 district boundaries. The agreement is generally excellent, despite the
baseline only using information on two of the three presidential elections conducted during this period. The few large
deviations indicate particularly strong candidate or regional effects (like Democrats holding the Montana at-large
district, for instance).
It is difficult to further validate the predictive accuracy model, given the paucity of precinct-level election data with
national coverage. However, others have found the combination of heavy-tailed error and the Stochastic Uniform
Partisan Swing model to produce well-calibrated predictions (Ebanks et al., 2022). We also evaluate the predictions for
2018, both a priori (i.e., averaging over possible national environments) and conditional on the actual shift from our
2016–2020 baseline. Fig. S2 shows these predictions, displayed as the number of seats Democrats are expected to win
out of the 255 in our 2018 dataset. For these predictions, we do not use the fitted district random effects (y-axis of
Fig. S1), but rather the precinct-level partisan baseline (x-axis of Fig. S1). The predictions are not fully out-of-sample,
because 2018 data informs the overall estimates of σβ, σε, and ν. The actual number of seats won by Democrats falls
well within the range expected under the model. Notice also the wider variation in the leftmost panel of Fig. S2 due to
the uncertainty in the national environment.
We fit the model with the brms R package (Bürkner, 2018), with a weakly informative t3(0, 2.5) prior on the Intercept
and all scale parameters, and a Gamma(2, 0.1) prior on ν. The model’s estimates for σβ, σε, and ν are summarized in
Table 1 below. Estimates for the βt are shown in Fig. S3. There is no evidence for heteroskedasticity corresponding to
larger or smaller national swings over time. This supports our use of historical data back to 1976.
Table 1: Election model hyperparameter estimates based on a hierarchical model fit to historical data
Estimate
Std. Error
σε
0.180
0.003
σβ
0.117
0.021
ν
2.896
0.128
We use the posterior medians of these hyperparameters from the fitted model in our electoral predictions. Combined
with the baseline vote estimate ˆαip for a specific plan p, the model yields the posterior predictive distribution of the
15


---

-0.2
0.0
0.2
0.4
1980
1990
2000
2010
2020
Election
Year effect (logit scale)
Figure S3: Posterior distribution of βt for each election year, from a hierarchical model fit to historical data. The
βt coeﬀicients are on a logit scale, so a value of 0.1 corresponds roughly to a 2.5 percentage point vote share
overperformance by Democrats.
vote share yit in district i. Averaging over this distribution gives us the probability that the district for any plan is
won by a Republican. This means that our point estimates of future election results are essentially equivalent to the
Democratic performance in our past two Presidential elections, corresponding to a 51.5% Democratic national vote.
As an example of the model’s predictions, take GA-12, which covers eastern and southeastern Georgia. GA-12 has a
partisan baseline of 56.1% Republican—the district’s average vote share across the 2016 and 2020 presidential elections,
under the new 2020 decade boundaries. Averaging across all future hypothetical electoral environments, this translates
to a 83% chance that Republicans will represent the seat. Conditioning on a particular national environment—say, a 5
percentage point shift towards the Democrats (a shift of 0.2 on the logit scale)—the model predicts a 59% chance of a
Republican win.
A key advantage of our modeling approach is that it propagates uncertainty across elections, in both national swing
and district-level idiosyncrasies, into all of our paper’s findings. In particular, a district with a 50.01% Democratic
vote share at baseline will essentially count as half a seat for each party, since when averaging across simulations and
electoral environments, half of the realizations will yield a Democratic victory and half will not.
A.5
Normalized partisan eﬀect plots
Fig. S4 re-expresses the data shown in Fig. 1 through two different normalization methods. The left plot normalizes
the difference in seats between the enacted plan and simulations in each state by the standard deviation of the simulated
distribution, producing a z-score. More extreme values indicate more extreme partisan effects relative to the variation
of the simulations. The right plot normalizes the seat difference by the total number of districts in each state, producing
a percentage point (pp) difference in seat shares. This has the tendency of shrinking the apparent magnitude of partisan
effects in larger states like Texas, and increasing the apparent magnitude in smaller states like Utah.
A.6
Eﬀiciency gap
The efficiency gap measures the inter-party net percentage of votes that do not contribute to winning an election,
including all votes for losing candidates and excess votes for winning candidates (Stephanopoulos and McGhee, 2015).
16


---

Texas (38)
Tenn. (9)
S.C. (7)
Fla. (28)
Utah (4)
Kan. (4)
Iowa (4)
Ohio (15)
Maine (2)
Okla. (5)
La. (6)
Va. (11)
Ark. (4)
Ariz. (9)
Neb. (3)
Ga. (14)
Idaho (2)
Colo. (8)
Ala. (7)
R.I. (2)
Ind. (9)
Minn. (8)
W.Va. (2)
Wis. (8)
Wash. (10)
N.H. (2)
N.Y. (26)
Conn. (5)
Calif. (52)
Mo. (8)
Ky. (6)
Mont. (2)
Miss. (4)
Nev. (4)
Md. (8)
Hawaii (2)
N.C. (14)
Mass. (9)
N.J. (12)
Mich. (13)
Ore. (6)
Pa. (17)
N.M. (3)
Ill. (17)
NATIONAL
D: 10
D: 5
0
R: 5
R: 10
Z-score of seats won under enacted plan
compared to non-partisan baseline
← Favors Republicans          States, ordered by z-score          Favors Democrats →
Utah (4)
Tenn. (9)
Texas (38)
S.C. (7)
Iowa (4)
Kan. (4)
Fla. (28)
Ohio (15)
Okla. (5)
Ark. (4)
Maine (2)
Va. (11)
Ariz. (9)
Ga. (14)
La. (6)
Colo. (8)
Ala. (7)
R.I. (2)
Neb. (3)
Minn. (8)
Ind. (9)
Idaho (2)
Wis. (8)
W.Va. (2)
Wash. (10)
N.H. (2)
Calif. (52)
N.Y. (26)
Hawaii (2)
Miss. (4)
Conn. (5)
Mass. (9)
Ky. (6)
Mo. (8)
N.J. (12)
Mont. (2)
Nev. (4)
Mich. (13)
N.C. (14)
Pa. (17)
Md. (8)
Ore. (6)
Ill. (17)
N.M. (3)
NATIONAL
D +10pp
Even
R +10pp
R +20pp
Difference in share of the state’s seats won under
enacted plan compared to non-partisan baseline
← Favors Republicans          States, ordered by share difference          Favors Democrats →
Control of redistricting
Commission
Court
Democrats
Mixed
Republicans
Figure S4: Normalized estimates of state and national level partisan eﬀects. Estimates show the expected
Republican seats under each non-partisan baseline plan subtracted from the expected Republican seats under the
enacted plan, normalized by the standard deviation of the simulated distribution (lef) and by the total number of
seats in the state (right). Bars to the right indicate the enacted plan gives more seats to Republicans, while to the
lef indicates more seats for Democrats. The vertical black line indicates no partisan eﬀect. The thick and thin bars
show 66% and 95% intervals of the simulated plans, respectively. States are colored by the actors that controlled
the map drawing in in each enacted plan, and are ordered vertically from the largest Democratic-favoring state to
the largest Republican-favoring state. The number of seats in each state is shown in parentheses.
Unlike partisan bias, it does not require a seats-votes curve and thus can be calculated on a state-by-state basis (King
and Browning, 1987; Katz et al., 2020).
Fig. S5 shows a measure of partisan effect in terms of the difference in the efficiency gap between the enacted plan
and simulated non-partisan plans, instead of seats won. To compute these differences, we follow the method from our
main analysis. For each national swing produced by the electoral model, we compute the efficiency gap for a plan.
We then average across those swings and examine the distribution of differences in averaged efficiency gaps across
plans. Although the efficiency gap is designed to have a “fair” value of 0, this value does not necessarily—and rarely
does—align with the median of the non-partisan baseline simulations. In addition, the confidence intervals for the
efficiency gap are often asymmetric.
The findings are largely similar to those shown in Fig. 1 as well as Fig. S4. States such as Illinois and New Mexico,
whose redistricting process is controlled by Democrats, exhibit a Democratic bias. In contrast, Republican-controlled
states including Texas and Utah show the partisan effect that favors Republicans.
17


---

Utah (4)
Tenn. (9)
Texas (38)
S.C. (7)
Kan. (4)
Fla. (28)
Okla. (5)
Iowa (4)
Ohio (15)
Maine (2)
Va. (11)
Ark. (4)
Ariz. (9)
La. (6)
Ga. (14)
Ala. (7)
R.I. (2)
Neb. (3)
Colo. (8)
Minn. (8)
Idaho (2)
Ind. (9)
W.Va. (2)
Wash. (10)
N.H. (2)
Calif. (52)
Wis. (8)
N.Y. (26)
Miss. (4)
Hawaii (2)
Mass. (9)
Conn. (5)
Mo. (8)
Ky. (6)
N.J. (12)
Nev. (4)
Mont. (2)
Mich. (13)
N.C. (14)
Pa. (17)
Md. (8)
Ore. (6)
Ill. (17)
N.M. (3)
NATIONAL
D+10pp
D+5pp
No
difference
R+5pp
R+10pp R+15pp
Difference in efficiency gap under enacted plan
compared to non-partisan baseline
← Favors Republicans    States, ordered by efficiency gap difference    Favors Democrats →
Control of redistricting
Commission
Court
Democrats
Mixed
Republicans
Figure S5: Estimates of national and state level partisan eﬀects measured in terms of eﬀiciency gap. Estimates
show the diﬀerence in eﬀiciency gap under each non-partisan baseline plan subtracted from the expected eﬀiciency
gap of the enacted plan. Bars to the right indicate the enacted plan is more favorable to Republicans than expected,
while bars to the lef indicate the enacted plan is more favorable to Democrats than expected. The vertical black
line indicates that the enacted plan aligns with the median simulated plan for the eﬀiciency gap. The thick and
thin bars show 66% and 95% intervals of the simulated plans, respectively. The point indicates the median. States
are colored by the actors that controlled the map drawing in in each enacted plan, and are ordered vertically from
the largest Democratic-favoring state to the largest Republican-favoring state. The number of seats in each state
is shown in parentheses.
A.7
Change in win probability map
Each of our simulated non-partisan plans assigns individual voting precincts to a Congressional district. For every one
of the precincts, we first compute the probability that the encompassing district as a whole is expected to be won by a
Republican candidate under the enacted plan (Fig. S6(a)). We repeat this for each of the simulated plans and average
across the plans (Fig. S6(b)). We then take the difference of these two values to calculate the change in the probability
that each precinct is represented by a Republican between the enacted and the simulated plans, on average (Fig. S6(c)).
Finally, we take an average of these changes (weighted by the number of two-party voters in each precinct) within
the enacted districts to form the change probability that a randomly sampled individual in an enacted district j is
represented by a Republican. This process is shown in Fig. S6(d), and is what is plotted in Fig. 2.
A.8
Seats-votes curves
The seats-votes curve is a commonly used visualization of district-based electoral systems. Prior work has summarized
past congressional elections (Kastellec et al., 2008) and the electoral college with this approach (Cervas and Grofman,
18


---

(a) Enacted plan
(b) Average of
sampled plans
0%
25%
50%
75%
100%
Prob. represented
by Republican
(c) Change in win probability
1
2
3
4
5
6
7
8
9
10
11
12
13
14
(d) Aggregate change in win probability
D+50
D+25
Even
R+25
R+50
Change in win probability
versus simulations
Figure S6: Schematic illustrating the construction of Fig. 2, using the state of North Carolina. Panel (a) represents
the estimates from our election model under the enacted plan. Panel (b) represents estimates generated from the
same model but under alternateive plans in our non-partisan baseline. These probabilities are estimated for each
precinct. The enacted district boudaries are overlaid for comparison. Panel (c) is the diﬀerence of panels (a) and
(b). Finally, panel (d) averages the precinct-level diﬀerences in panel (c) across the voters in each enacted district
and places the district in the roughly same area as the actual enacted district, using the same number of hexagons
(reflecting the fact that each congressional district has a nearly equal population). These are shown in Fig. 2.
2022). We make a new type of comparison, making thousands of seats-votes curves for each simulated plan to compare
with the enacted national seats-votes curve.
Our seats-votes curve analysis examines how changing the national popular vote share using uniform swings affects
the number of seats each party is predicted to win. We estimate the curve from our election model as follows. First, we
fix a value of βt, the national swing. Then, we estimate the number of seats won by each party using the election model
using the baseline estimates ˆαi and the hyperparameter estimates, ˆσ2
ε and ˆν. This produces one point on the seats-votes
curve for each party. We repeat this process across a wide range of βt, which traces out the entire seats-votes curve.
The seats-votes curve is closely tied to the theoretical framework of partisan symmetry that is used as a measure of
partisan fairness (King and Browning, 1987; Katz et al., 2020). In this framework, if a districting plan is fair, parties
are expected to receive the same number of seats for the same vote share. That is, if party A receives v = 45% of the
vote share receives s seats, then when party B wins 45% of the vote share (so party A wins 1 −v = 55%), it too should
win s seats (leaving 1 −s seats for party A). That is, we say there is partisan symmetry if
S(v) = 1 −S(1 −v).
The deviation from symmetry is then measured for a given vote share as the number of seats that would need to be
given from one party to another. We call this deviation the partisan bias of an electoral system (King and Browning,
1987). Factors like geographic bias, institutional procedures, and gerrymandering can result in biased seats-votes
curves. Note that in systems like the US House, there is no implicit guarantee of proportionality (Grofman, 1983). The
difference between a party’s expected seat share from a given vote share is often referred to as “partisan bias.”
Symmetry along the whole curve is rare. In a two party system, relevant parties do not typically receive 5% or 95% of
the votes, outside of rare, uncontested races. Instead, we often zoom into the relevant vote shares near 50%, where
party competition occurs. In Fig. 4, we present the electorally relevant subsection.
A seats-votes curve encodes many different pieces of information. While partisan bias describes the difference between
the seats-votes curves for each party at a particular vote share, the slope of the seats-votes curve describes how
responsive a system is. Responsiveness captures for a percentage point increase in vote share, how many additional
19


---

D
e
m
.,
 
En
act
ed
4
5
6
7
8
9
10
30%
40%
50%
60%
70%
National Democratic vote share
Responsiveness
(Democratic seats per 1pp voteshare)
Figure S7: Responsiveness of the electoral system under enacted and simulated plans. Responsiveness is measured
as the change in seats for a one percentage point change in the national vote share. It corresponds to the derivative
of the seats-votes curves shown in Fig. 4. For the realistic values of national Democratic vote share, responsiveness
is much lower under the enacted plan (blue solid line) than under the simulated plans (grey solid lines).
seats a party gains. Our estimates of responsiveness for the national map and each of the simulated plans are shown in
Fig. S7. The figure shows that responsiveness is much lower under the enacted plan (blue solid line) than under the
simulated plans (grey solid lines) in a realistic scenario where the national Democratic vote share is between 40% and
60%.
A.9
Related simulation studies
Our simulation approach improves upon that of (Chen and Cottrell, 2016), which analyzed the previous 2010 redis-
tricting cycle, in several ways. First, we use a set of new samples of simulated, non-partisan plans from (McCartan
et al., 2022). These simulated districting plans are tailored to each state after carefully constructing mathematical
sampling constraints based on the legal requirements that each state imposes on its map drawers. Second, the plans
were simulated with a Sequential Monte Carlo (SMC) redistricting algorithm which has theoretical guarantees of
representativeness (McCartan and Imai, 2023). Third, the simulated plans are intended to be as compliant with the
VRA as the enacted plans, though we do not attempt to resolve ongoing legal disputes about whether the enacted
plans themselves are compliant with the VRA. Finally, we use a Bayesian statistical model to generate a plausible
range of future electoral outcomes primarily based on the two most recent presidential elections, rather than a more
retrospective model from one election. (Warshaw et al., 2022) uses an earlier, though incomplete set of the simulated
plans from (McCartan et al., 2022), combined with data from PlanScore (planscore.org), which makes historical and
cross-state comparisons to largely discuss state-by-state processes. In contrast, we focus on the partisan biases at both
national and state levels and isolate them from the structural biases, while incorporating simulation data from all
states.
A.10
Impacts of redistricting rules
Simulated plans from (McCartan et al., 2022) are generated under the constraints consistent with the current federal
and state redistricting rules. This means that our estimates of partisan effects do not account for potential partisan
bias due to these redistricting rules themselves. We can assess the partisan effects of a particular rule of interest by
adapting the simulation methodology used in our main analyses. Specifically, we run two sets of simulations for
each state analysis—one of which includes a particular rule, and the other one does not—but are otherwise identical.
20


---

Alabama
Ohio
D+1
No difference
R+1
R+2
Without state rules
Our specification
Plan with 2 VRA districts
Our specification
Without VRA race constraint
Difference of seats won under enacted plan
compared to baseline
Non−partisan baseline
Figure S8: Sensitivity of state-level analyses to diﬀerence in rules used. Each estimate shows the diﬀerence in
seats won in the state given the enacted plan with a diﬀerent choice of non-partisan baseline. The light gray
specifications for Ohio and Alabama reproduce the results in Fig. 1. The alternative specifications in black use
diﬀerent constraints in the baseline simulation. Removing the rules increases our estimated Republican advantage
of the Republican-drawn plan in Ohio and decreases it in Alabama, by modest amounts.
Comparing these two sets of representative plans allows us to estimate the partisan effect of a rule itself. In this section,
we illustrate such an analysis through two examples: Ohio and Alabama.
Ohio has historically been competitive statewide in some offices such as President, but the Republican party has
maintained majorities in both of state legislative chambers and the Governor’s office in 2010. Therefore, Ohio is
a state where partisan legislatures could bake in redistricting rules—such as those that require keeping large cities
whole—that would bias our baseline simulations in the Republican party’s favor. In this case, keeping cities whole
could prevent a more efficient distribution of Democratic-leaning urban voters across several districts (Rodden, 2019).
To examine the sensitivity of our findings to these rules, we re-ran our simulation without constraints that limit the
splitting of counties including Cincinnati, Cleveland, and Columbus, and used it as an alternative baseline. We removed
all constraints related to race and avoidance of administrative boundary splits, except for a constraint to limit the
number of county splits to one less the number of total congressional districts (a constraint we use almost uniformly
in other states). Fig. S8 shows that removing these rules increases the enacted plan’s average Republican advantage by
0.25 congressional seats. However, the variation in possible plans is relatively large compared to this difference in
average. In other words, on average, Ohio-specific rules may mask the extent of Republican gerrymandering, but the
difference here is modest.
In Alabama, the key contention is over how the Voting Rights Act of 1965 should apply. When Alabama drew the
enacted plan, they drew one minority opportunity district, which is a Democratic district primarily controlled by
Black voters. Yet, in a court case currently at the US Supreme Court, Merrill v. Milligan, the state has argued that they
should only have to draw as many minority opportunity districts as would be generated by a race-blind analysis. This
could have partisan effects, due to the high correlation of race and party in Alabama, as it is possible that a race-blind
process could draw no minority opportunity district. Plaintiffs in the case instead argue that Alabama should have
drawn two minority opportunity districts.
To examine the sensitivity of our analysis to these alternative contentions about the interpretation of the law, we
created two more simulations as alternative baselines. First, we create the race-blind specification which removes race
entirely from the simulation parameters and uses standard parameters to preserve traditional redistricting criteria
(“without VRA race constraint” in Fig. S8). Second, we create a specification “with 2 VRA districts,” which freezes the
two minority opportunity districts from Plaintiff demonstration plan A in Merrill. This has an additional effect of
freezing a third district, along the Gulf of Mexico, which is land-locked by the two frozen VRA districts. Fig. S8 shows
that using a race-blind specification as a baseline would flip the bias of the enacted plan from favoring Republicans
on average to favoring Democrats on average, though neither of these are statistically significant biases. We note
that this race-blind bias in favor of Democrats aligns with existing past simulation work that does not incorporate
state-specific rules (Chen and Cottrell, 2016). In contrast, using the Plaintiff’s plan with two VRA districts as a baseline
would increase the pro-Republican bias of the enacted plans. Freezing the three districts removes almost all variation
in expected Republican seats in Alabama.
21
