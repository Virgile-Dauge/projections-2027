---
title: 'Changing Precinct Boundaries: Who Is Affected and Electoral'
id: changing-precinct-boundaries-who-is-affected-and-electoral
tags:
- precinct-crosswalk
- geo-electoral-crosswalk
- methode-quantitative
created: '2026-07-21T18:29:51.368138Z'
updated: '2026-07-21T18:38:49.842386Z'
source: https://esra-conference.org/files/election-science-conference/files/changing_precinct_boundaries_esra-brianamos.pdf
source_domain: esra-conference.org
fetched_at: '2026-07-21T18:29:51.367790Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Étude nationale (Amos, Gerontakis, McDonald, 2023) sur 175 311 bureaux de
  vote (precincts) américains comparés entre 2016 et 2020. Méthode de crosswalk :
  superposition des géométries de precincts + géographie du recensement (census blocks),
  avec allocation dasymétrique (dasymetric mapping, basée sur la densité de logements
  issue du National Land Cover Database) quand un bloc de recensement est scindé par
  un changement de découpage. Définit le score de ''Precinct Continuity'' = part de
  la population 2020 d''un bureau qui provient du bureau 2016 avec lequel il a le
  plus grand chevauchement spatial. Constat empirique : 81,2% des bureaux (142 408/175
  426) n''ont subi aucun changement affectant la population entre 2016 et 2020 ; parmi
  les 33 018 bureaux modifiés, 14 113 ont conservé ≥95% de leur population (changements
  mineurs, annexions locales). Les bureaux ayant subi un changement majeur de périmètre
  sont surreprésentés en population noire et hispanique et en zones denses, et affichent
  une hausse de participation plus faible entre 2016 et 2020 que les bureaux stables
  — effet attribué à la confusion électorale et à la distance au nouveau bureau de
  vote.'
raw_file: raw/changing-precinct-boundaries-who-is-affected-and-electoral.pdf
---

1 
 
Changing Precinct Boundaries: Who Is Affected and Electoral 
Consequences 
 
Brian Amos, Wichita State University 
Steve Gerontakis, University of North Carolina at Asheville 
Michael McDonald, University of Florida 
 
Abstract: 
We examine changes to 175,311 precincts between the 2016 and 2020 general presidential 
elections. Our data are the result of a unique effort to collect precinct boundaries that has never 
been accomplished before: on a national scale across multiple elections. We observe that 
precincts that underwent major changes – beyond minor changes that are generally reflective of 
city and town annexations affecting small populations – contain a greater share of Hispanic and 
Black residents and are more likely to be found in denser population areas than those that do not 
change. We find precincts that underwent major changes on average experienced slightly lower 
turnout rate increases in 2020 than those that did not change. 
  
 
 
Prepared for the 2023 Election Science, Reform, and Administration annual meeting, Athens, 
GA, May 31 – June 2, 2023. Do not quote, cite, or circulate without permission.  
 
 


---

2 
 
Introduction 
 
Most voters cast their ballots at polling places. Election officials assign registered voters 
to geographically-bound units commonly called precincts – in some places known instead as 
wards or election districts – which are in turn assigned a polling place where voters cast in-
person ballots. Of course, there are voting policies such as mail balloting and vote centers that do 
not require engaged registrants to travel to a specific polling location. However, barring the 
anomalous 2020 elections, most people typically vote in a rite of passage that takes them through 
their assigned polling location on Election Day. 
 
Precincts are not static. Election officials may change precinct boundaries for various 
reasons, which may affect where voters cast ballots on Election Day. These changes to precinct 
boundaries may also affect voters’ behavior. The distance from a person’s home to their polling 
location is negatively correlated with their voter turnout (Gimpel and Schuknecht 2003; Haspel 
and Knotts 2005), a change in voter’s assigned polling place may change a person’s preferred 
mode of voting (Brady and McNulty 2011; Clinton et al. 2021), and a change in a person’s 
assigned polling location may cause confusion that reduces turnout (Amos, Smith, and Ste. 
Claire 2017). We find precincts that underwent major changes – beyond minor changes that are 
generally reflective of city and town annexations affecting small populations – contain a greater 
share of Hispanic and Black residents and are more likely to be found in denser population areas 
than those that do not change. We further find that precincts that underwent major changes on 
average experienced lower turnout rate increases in 2020 compared to 2016 than those that did 
not change. 


---

3 
 
Background 
Precincts serve an important election administration function. Local election officials 
assign registered voters to precincts. In turn, election officials designate a polling location for 
each precinct where voters cast their ballots. Local election officials are responsible for creating 
precinct boundaries within their jurisdictions. As such, precinct boundaries do not cross the 
jurisdictional boundaries of election officials, which in most states are known as counties.1  
A primary purpose of precincts is to identify the polling place where election officials 
distribute ballots to voters, which are the key “point of contact between the average voter and 
h[er] government” (Beard 1909, 590). Ideally, to reduce the administrative overhead when 
providing voters with ballots, local election officials prefer to provide a single type of ballot at a 
polling place – known as a ballot style (Herrnson, Hanmer, and Niemi 2012) – which contains all 
the offices and ballot questions that voters within a precinct are eligible to vote on. To facilitate 
creating a single ballot style for each precinct, election officials attempt to conform precincts to 
the existing political boundaries within their locality, such as cities, towns, and legislative district 
boundaries – which we broadly construe to be any legislature from the U.S. Congress to local 
city councils. Conforming precincts to all relevant political boundaries means that a single ballot 
style can be distributed to voters within a precinct.  
Election officials use precincts to make resource allocation decisions. Election officials 
anticipate the number of in-person voters and distribute voting equipment and poll workers 
accordingly. States and localities may describe resource allocation formulas in laws and policies, 
 
1 Exceptions include Alaska, which utilizes election districts that do not necessarily conform to county boundaries; 
and Louisiana, which has parishes instead of counties. 


---

4 
 
such that resources are distributed relatively evenly according to anticipated workload dictated 
by the number of voters that are to be processed at the polling location. 
There are several reasons why precinct boundaries change, through a process akin to 
redistricting called “reprecincting” (Amos and McDonald 2020). As the preceding discussion 
implies, reprecincting is likely to occur when political boundaries change due to redistricting of 
legislative districts. Local political boundaries may also change through annexations, which 
typically affect only small areas of land and number of people. Reprecincting can also occur 
when a polling place becomes unavailable and election officials must find a new one. Because 
polling places have limited capacity, election officials may create new precincts when the 
number of registered voters within a precinct increases either above the reasonable capacity of a 
precinct’s polling location or due to a formula set by administrative policies. When the number 
of registered voters within a precinct becomes too small, election officials may consolidate it 
with another precinct to more efficiently manage their resources. Sometimes precinct splits and 
consolidations ripple into adjacent precincts, creating a widespread shuffling of precinct 
boundaries. 
There are sometimes practicalities that prevent election officials from achieving the goal 
of having a single ballot style for each precinct. Local election officials generally prefer to locate 
polling places within precincts. Districts and local government boundaries often do not conform 
with one another, such that intersections of district and local government boundaries create 
slivers that comprise a small population impracticable to administer a polling location for or do 
not contain a suitable polling location. A common solution to this problem is to allow political 
boundaries to split precincts and to distribute multiple ballot styles to voters. Technology 


---

5 
 
facilities this solution with electronic poll books that can identify the proper ballot styles to 
distribute to voters and with printers that can provide on-demand ballots. 
Some states and localities faced with the obstacle of managing precinct operations for a 
small number of voters or for a geography difficult to find a suitable polling location create 
special all-mail ballot jurisdictions, where all active registered voters are mailed a ballot and no 
polling location is provided except for emergency situations at a central election office. Nevada 
was the first state to create all-mail ballot precincts in 1923 (McDonald 2022). California law 
requires a precinct for every unique intersection of political boundaries, and similarly runs all-
mail ballot elections when the number of registered voters is small (Brady and McNulty 2011). 
That is, California conducted their elections this way until it joined the ranks of the eight states 
(as of this writing) that conduct all-mail ballot elections statewide.2 A few states allow smaller 
localities the option of conducting all-mail ballot elections and may limit this option to local 
elections only. All-mail states and localities still have precincts, but they do not serve the same 
election administration functions as those states with Election Day in-person voting. All-mail 
jurisdictions primarily serve the purposes of creating appropriate ballots styles and to report 
election results within small geographies, which assists political campaigns with voter targeting 
and with redistricting. 
Another way technology has transformed precinct operations is through the vote center 
model. Vote centers are special precincts where any eligible voter within a local jurisdiction may 
cast their ballot. When election officials locate vote centers in high traffic locations voter turnout 
increases, even if these localities may have fewer Election Day precincts (Stein and Vonnahme 
2008). Election officials commonly deploy vote centers during early in-person voting periods, 
 
2 For a summary of all-mail ballot laws, see: https://www.ncsl.org/elections-and-campaigns/table-18-states-with-all-
mail-elections (accessed May 11, 2023). 


---

6 
 
although some states and localities may continue to offer vote centers on Election Day.3 Some 
vote-center states are all-mail ballot states with an in-person voting option for those who wish to 
vote in this manner, and some states specify that vote centers may be used only in local elections 
or serve specific communities, such as disabled individuals. During the COVID emergency some 
states and localities, such as Maricopa County, Arizona and the entire state of Kentucky, adopted 
vote centers. 
Theory 
The adoption of election reform is politically contested in the United States, with 
Democrats generally supporting reforms that provide greater voting access, and Republicans 
opposed to reforms such as mail balloting and vote centers (Hasen 2012; McDonald 2022). 
Reprecincting is a low-level and routinized election administration procedure that may fly below 
the radar of these higher-level voting wars. However, there is reason to suspect reprecincting 
affects voter turnout and these effects can be complicated. Haspel and Knotts (2005) find that 
voters assigned to an Atlanta, Georgia polling location for a 2001 mayoral election farther from 
their home were less likely to vote. However, the overall turnout effect of reprecincting was 
positive for those registrants whose election officials moved them into a new precinct. These 
scholars attribute this paradoxical result to election officials increasing the number of precincts 
by splitting some existing precincts into two or more parts, thus reducing the distance from 
registrants’ homes to their polling locations in the aggregate. Thus, when reprecincting is a 
function of procedures designed to improve voters’ experiences it may facilitate participation, 
even if some registrants may be inconvenienced by changes. 
 
3 For a summary of vote-center laws, see: https://www.ncsl.org/elections-and-campaigns/vote-centers (accessed May 
11, 2023). 


---

7 
 
In contrast to the analysis of a 2001 election in Georgia – at a time before Georgia had 
yet to adopt no-excuse absentee voting (Biggers and Hanmer 2015) – are studies of polling place 
changes in states that had more robust alternative voting options, such as mail balloting and in-
person early voting. In a study of California’s 2003 gubernatorial recall election, Brady and 
McNulty (2011) examine the voting behavior effects of Los Angeles County election officials 
reducing the number of polling places by consolidating precincts – a policy many localities 
engage in when voter turnout is expected to be lower than high-turnout general elections. In 
contrast to Haspel and Knotts’ (2005) Atlanta study, these Los Angeles precinct consolidations 
resulted in fewer polling places and greater transportation costs for voters. Brady and McNulty 
(2011) find a nearly two-point decline in turnout from precinct changes, which would have been 
a percentage point greater if some voters had not chosen to alter their voting mode by casting a 
mail ballot.  A study of the 2008, 2012, and 2016 North Carolina presidential elections finds a 
similar substitution effect of voting mode, with voters moved farther from a polling place more 
likely to cast an in-person early ballot, nearly entirely offsetting negative effects from precinct 
changes (Clinton et al. 2021).  
Brady and McNulty (2011) lead their paper with a mid-2000’s anecdote of Houston’s 
elections official stating he manipulated turnout among favored and disfavored groups by 
strategically locating polling locations. Amos, Smith, and Ste. Claire (2017) are likewise less 
sanguine that polling location changes have no or little negative effect on overall turnout. 
Motivating their investigation of Manatee County was that Supervisor of Elections and former 
state Senator Mike Bennett argued voting was “a privilege” and that people should have to “walk 
across town to go over and vote” when he sponsored a suppressive voting law which a federal 
court later overturned. These scholars find reprecincting for the 2014 general election resulted in 


---

8 
 
voting mode substitution effects, but unlike the other studies, the substitution effects did not fully 
compensate an overall lower turnout rate of nearly two percentage points attributable to changing 
precinct boundaries, particularly depressing Hispanic turnout rates.  
We thus have conflicting theoretical predictions about the turnout effects of precinct 
boundary changes. In one frame, reprecincting is a routinized election administration procedure 
intended to improve voting experiences and lower voting costs, and thereby increases voter 
turnout. In the other frame, reprecincting intentionally or unintentionally results in voter 
confusion or increased distance from polling locations on average across all voters, increases 
voting costs, and thereby reduces voter turnout.  
The extant studies of the effects of precinct changes on turnout do not go much further 
than examining changes of distance to polling locations and voting mode substitution effects. 
These studies are limited in their analyses due to their use of administrative data – voting records 
– and not survey data, which can illuminate individuals’ attitudes and opinions motivating 
behaviors. Scholars speculate that lower turnout may arise due to “information costs associated 
with locating the new polling station” (Haspel and Knotts 2005: 556). If one mechanism that 
lowers turnout is that changing precinct boundaries causes voter confusion, we may expect new 
registrants who move into a precinct – once they have overcome the cost of registering – to be 
less burdened compared to continuing registrants in the precinct, as they would not have been 
exposed to voting at the precinct’s former polling location. We thus expect precincts with a 
higher percentage of new population to be less sensitive to precinct boundary changes. To be 
clear, we conceptualize the dynamic between an influx of new population to be conditional on 
precinct changes – an interactive effect. We expect the length of time a person lives in a precinct 
to directly socialize an individual into a community and thus be positively associated with 


---

9 
 
turnout, as numerous scholars theorize and find such a positive relationship (e.g., Wolfinger and 
Rosenstone 1980). 
If reprecincting is an administrative practice intended to improve voting experiences, 
especially where population is growing, precinct changes may have positive turnout benefits that 
offset any negative turnout effects. Election officials may split existing precincts into two or 
more precincts to reduce workloads and wait times at what would otherwise be overcrowded 
precincts (Haspel and Knotts 2005). 
We infer from extant studies that find a substitution effect on voting mode (Brady and 
McNulty 2011; Amos, Smith, and Ste. Claire 2017; Clinton et al. 2021) that precinct boundary 
changes in a state or locality that uses all-mail ballot elections should have no discernable 
turnout effect. Where mail-ballot states and localities provide for in-person voting options on 
Election Day, it is at vote centers where anyone in the jurisdiction may vote. Similarly, we 
expect precinct changes have no turnout effects for states and localities that employ vote centers. 
In both circumstances, election officials use precincts primarily to manage ballot styles and 
election results reporting, which are not theoretically connected to turnout. Thus, these states and 
localities serve as a useful control group from which to test our theories about precinct changes 
in states where these changes should matter. 
Data and Methodology 
 
In a multi-year project, we collected precinct boundaries for the entire United States and 
merged these boundaries with statewide election results for all general elections spanning 2016 


---

10 
 
through 2020.4 For our analysis we wish to detect changes to precinct boundaries occurring 
between the 2016 and 2020 presidential elections. We cannot rely on identifying changing 
precincts by examining precincts’ names because election officials may name and rename 
precincts for reasons apart from changing their boundaries.5 We thus identify precinct boundary 
changes by overlaying their boundaries. To understand substantive effects of these changes, we 
further overlay precinct boundaries with census geography. This step allows us to enrich our 
analyses with aggregate population statistics from the Census Bureau’s decennial census and the 
American Community Survey. A difficulty is that precinct boundaries do not always conform 
with census geography. We devise a solution to apportioning aggregate statistics to geographic 
units that intersect and split one another employing a method known as dasymetric mapping 
(Amos, McDonald, and Watkins 2017). Where a census geographic unit is split by a precinct, we 
determine how much of the aggregate population statistics to apportion to the split pieces by 
measuring housing density within the fragments, which we estimate from the National Land 
Cover Database. 
 
Through this methodology we calculate the voting-age population (VAP) within the 2016 
general election precincts, the 2020 general election precincts, and the overlapping geography 
created by intersecting the 2016 and 2020 precincts. We use the 2020 decennial census for the 
VAP of the 2020 precincts. Using the precincts election officials created for the 2020 general 
election as the comparison point, we compute the Precinct Continuity of a 2020 precinct’s 
 
4 We use the generic name “precincts” to refer to these election geographies even though election officials may refer 
to these administrative units as precincts, wards, or election districts. These data and documentation about their 
collection are available at: https://dataverse.harvard.edu/dataverse/electionscience  
5 This may happen when election officials adopt new nomenclature to name precincts. It may happen in localities 
where election officials name precincts after their polling locations, and election officials have assigned a new 
polling location to a precinct. It is also possible that district boundaries will change without changing precinct 
names, particularly in places where they are sequentially numbered. Precincts may even be renumbered such that 
there is no change to the precinct names in use, but the names are attached to different physical precincts. 


---

11 
 
population with the 2016 precinct that has the largest population overlap, which is the key 
independent variable in our analyses. 
 
Figure 1. Paulding County, Georgia Precinct Maps. From Left to Right, the Precinct Map 
in 2016, the Precinct Map in 2020, and the Precinct Map in 2020 Labeled with Precinct 
Continuity Scores. 
 
 
Of the 175,426 precincts election officials created for the 2020 general election, 142,408 
or 81.2% had no change from the 2016 general election affecting population. In Figure 2, we plot 
the frequency distribution for the remaining 33,018 precincts. When precincts do change, most 
frequently these changes affect a relatively small number of people. Nearly half of the precincts 
that changed – 14,113 – experienced a continuation of 95% or more of the precinct’s population. 
This is consistent with our understanding of the mechanism of precinct changes. These small 
changes are generally due to minor local annexations that affect a relatively small number of 
people.6  
 
6 We exclude from our analyses 1,365 precincts the Census Bureau identifies as having zero voting-age population. 
Election officials typically create these pseudo-precincts for special uninhabited areas like large parks, or to report 
election results for non-geographically bound populations, such as overseas civilians or homeless individuals. These 
latter pseudo-precincts typically comprise a single census block where an election office or county courthouse is 
located. 


---

12 
 
 
Figure 2. 2020 to 2016 Ratio of Voting-Age Population Within Changed Precincts  
Our dependent variable is a turnout rate change measure. The Census Bureau 
disseminates VAP from the decennial censuses within the smallest census geographic units – 
census blocks – which allows us to make a relatively precise allocation of VAP to precincts. 
When investigating how changing precincts affects voter turnout, a measure of eligible voters 
that takes into account citizenship and ineligible felons may be more desirable to measure 
(McDonald and Popkin 2001). Unfortunately, constructing measures of eligible voters within 
precincts is difficult since precise estimates of citizens and prison populations are not readily 
available. Mitigating this shortfall is that we construct change in turnout rates from 2016 to 
2020. We do not expect turnout rate change over four years to be greatly biased by our inability 
to control for citizenship and ineligible felons. We do control for changes to the voting-age 


---

13 
 
population by interpolating precincts’ 2016 VAP from the change in population between the 
2010 to 2020 decennial censuses. For the numerator of the turnout rates, we use the vote for 
president, rather than the total ballots counted, because states are inconsistent in how they report 
write-in candidates and ballots without valid votes at the precinct level. 
We include the following control variables in the model chosen for their typical 
relationships with voter turnout (Wolfinger and Rosenstone 1980). We construct two racial and 
ethnicity variables from the 2020 decennial census: percent Black VAP and percent Hispanic 
VAP of the precinct. Other variables are drawn primarily drawn from 2016-2020 American 
Community Survey (ACS) 5-year estimates.7 These include the precent of the population Age 
18-34 (percent of the precinct age 18 to 34), percent Some College or More (the percent who 
report at least some college education), percent of households with Income >$75K, and percent 
of households with a length of residence in the precinct of 1 Year or Less. 
To generate theoretical expectations for these variables for our dependent variable – the 
turnout difference within a precinct from 2016 to 2020 – we analyze the Census Bureau’s 
Current Population Voting and Registration Supplement. We present in the first two columns of 
Table 1 the turnout rates for selected groups in the 2020 and 2016 general elections. The third 
column is the increase in the turnout rate from the 2016 election to the modern historically high 
turnout election of 2020. The fourth column provides the increase relative to a reference group, 
denoted with a dash. From these simple statistics we expect a negative relationship between the 
turnout difference and Black VAP and Hispanic VAP relative to the omitted reference category of 
 
7 These data are available at the block group level, the next smallest census geography. There is survey error 
associated with these ACS survey data. Even though the 5-year ACS has over 1 million respondents, the subgroups 
are small for census block groups. Although we use some ACS variables, we choose not to use the ACS’s 
citizenship estimates to constrict citizen-VAP turnout rates. We might use a prior 5-year ACS for 2016 and 2020 
CAVP, but these data are noisy for individual years; noise which is compounded when calculating CVAP turnout 
rates differences between elections.  


---

14 
 
Whites. We expect a positive relationship for Age 18-34, a positive relationship for Some College 
or More, and a small negative relationship for Income >$75K.  
Category 
2020 
2016 
Diff 
Across 
Elections 
Diff 
Within 
Groups 
Race/Ethnicity 
Non-Hispanic White 
72.6% 
64.7% 
7.9% 
- 
Non-Hispanic Black 
65.6% 
59.9% 
5.7% 
-2.2% 
Hispanic 
52.5% 
44.9% 
7.6% 
-0.3% 
Age 
<35 
54.2% 
44.4% 
9.8% +2.8% 
35+ 
70.4% 
63.4% 
6.9% 
- 
Education 
H.S. Grad or Less 
50.3% 
44.3% 
6.0% 
- 
Some College or More 
79.4% 
71.5% 
8.0% +2.0% 
Household Income 
<$75K 
59.9% 
53.3% 
6.6% 
- 
>$75K 
78.7% 
72.4% 
6.3% 
-0.3% 
Length at Residence 
1 Year or Less 
54.2% 
44.4% 
9.8% 
- 
More than 1 Year 
70.4% 
63.4% 
6.9% 
-2.8% 
 Table 1. Selected 2016 and 2020 CPS Turnout Rates 
Notes: Data from the 2016 and 2020 Current Population Survey, Voting and Registration 
Supplements with Hur and Achen (2013) weight adjustments. A “-” denotes the reference 
category for difference calculations within groups. 
 
An important ACS variable relevant to our investigation of the effect of precinct changes 
on turnout is the percentage of the precinct’s population that has lived More than 1 Year within 
the precinct. We expect the direct effect of More than 1 Year on the turnout change from 2016 to 
2020 to be positive. However, we are primarily interested in its interaction with Ratio, which we 


---

15 
 
expect to be negative (to offset the positive direct effect), since newer residents to a precinct 
should be unaffected by precinct changes they never experienced. Additionally, Haspel and 
Knotts (2005) argue precinct splits improve voter turnout by locating polling places closer, on 
average, to registrants in formerly overcrowded precincts. To test these findings, we add to our 
analyses a variable Split Precinct, which identifies if two or more 2020 precincts were entirely 
and exclusively contained within a single 2016 precinct. 
Several studies (Brady and McNulty 2011; Amos, Smith, and Ste. Claire 2017; Clinton et 
al. 2021) find precinct changes may lead voters to utilize alternatives to in-person Election Day 
voting. These studies differ in the degree to which changing vote modes can mitigate negative 
turnout effects from changing precinct boundaries. States and localities where precincts serve 
primarily the purposes of managing ballot styles and reporting election results thus serve as 
placebo cases, since these changes should not affect turnout. We subset our data into two 
categories and estimate separate statistical models: those states and localities that either ran all-
mail ballot elections in the 2020 general election or used Election Day vote centers, and those 
that did not. We classify as all-mail ballot the states of Colorado, California, Hawaii, Nevada, 
Oregon, Utah, Vermont, Washington, Washington DC, and certain counties within Montana, 
Nebraska, and North Dakota; and we classify jurisdictions offering vote centers as Kentucky, 
and Maricopa County, Arizona (McDonald 2022). Unfortunately for our analyses, due to the 
COVID emergency in 2020, some Kentucky and New Jersey counties reported their election 
results jurisdiction-wide, so we cannot measure precisely presidential vote within these counties’ 
precincts. At this time, California’s 2016 data have numerous issues that require our attention. 
For these reasons, we exclude California, Kentucky, and New Jersey from our analyses.  


---

16 
 
We include a general variable meant to identify the resources and professionalization of 
election administration within counties, the 2020 voting-age population of the county. Our 
assumption is that larger counties have a more robust tax base and therefore are able to devote 
more resources to election administration. Because counties have such widely varying 
populations, we log to construct Log County VAP.  
We estimate a linear model with state fixed effects for our estimation, allowing errors to 
vary between states. We investigated hierarchical linear models at the state and county levels, but 
the models would not converge. We suspect this is because rural counties may have three or four 
precincts, thus challenging the estimation procedures that perform better with a larger number of 
within-group observations. The choice of state fixed effects means that we control for state-
specific conditions, but we cannot estimate separately the effects of state-specific laws and 
electoral contexts, such as the presence of alternative voting modes and electoral 
competitiveness. Although within some states there are only certain counties that run all-mail 
elections or use Election Day vote centers, we choose to run a separate model for these states and 
localities rather than employ a dummy variable identifying these jurisdictions in one grand 
model. We take this approach to bifurcate our data because it effectively allows us to test for 
interaction effects among all independent variables, a desirable feature that will become evident 
as we conduct our analysis.  
Analysis 
To begin our analyses, we provide some basic demographic statistics for precincts where 
changing boundaries theoretically affect turnout – that is, states and localities that do not run all-
mail elections or have vote centers, setting aside California, Kentucky, and New Jersey for the 
aforementioned data issues. We further segregate precincts into three categories. First, those 


---

17 
 
precincts with no change. Second, those precincts with a minor change of 90% or more precinct 
continuity, which we typically observe in our data work to result from minor local annexations. 
Third, those precincts with a major change of less than 90% precinct continuity.  
We present in Table 2 selected mean statistics across the three types of precincts: those 
with no, minor, or major changes. Precincts with major changes are the most diverse. Precincts 
with a major change have on average a Non-Hispanic White VAP percentage of 61.3%, 
compared to 68.9% for those with no change and 71.5% for those with a minor change. We find 
the mirror of this examining the non-Hispanic Black and Hispanic share of precincts across the 
three categories. Precincts with major changes have a larger share of their VAP from both 
categories than those with no change or with minor changes: on average, 16.7% and 13.0% of 
the major change precincts are non-Hispanic Black and Hispanic, respectively, while 13.9% and 
11.0% are for no change precincts and 12.4% and 9.3% for minor change precincts. 
2016 to 2020 Continuity 
% Non-
Hispanic 
White 
% Non-
Hispanic 
Black 
 
% 
Hispanic 
Density 
(VAP per 
Mile2) 
 
 
N 
No Change 
68.9% 
13.9% 
11.0% 
1,820 113,753 
Minor Change 
71.5% 
12.4% 
9.3% 
741 
13,068 
Major Change 
61.3% 
16.7% 
13.0% 
5,249 
5,394 
Table 2. Selected Demographics of Precincts with No Change from the 2016 General to 
2020 General Election, Minimal Change (>90% VAP Continuity), and Major Change 
(<90% VAP Continuity) 
 
The pattern of population densities across the three types of precincts are generally 
consistent with our understanding of where these different types of precincts are located. Those 
with minimal change tend to be modified due to city and town annexations that occur on the 
fringe of towns, and the annexed property may contain low-density lands for public use, such as 
landfills and parks. The voting-age population density of precincts with minor changes is 741 


---

18 
 
persons per square mile. The precincts with no change have the next highest population density 
on average of 1,820 persons per square mile. This is again consistent with our experience of 
collecting precinct boundaries, as small rural counties often do not make changes to their 
precincts. Reflecting the observation that precinct changes are more frequently an urban 
phenomenon, precincts experiencing major changes are the most densely populated, with an 
average 5,394 persons per square mile. 
The simple examination of the 2016 and 2020 VAP precinct turnout rates, which we 
present in Table 3, suggests that major changes negatively affect turnout rates. Keep in mind that 
turnout increased from 2016 to 2020, which experienced the highest turnout rate among eligible 
voters since 1900 (McDonald 2022). Those precincts with major changes to their boundaries had 
the smallest increase of turnout, with a 4.6 point increase. Precincts with no change saw a 5.5 
point increase and those with a minor change a 6.5 point increase.   
2016 to 2020 Continuity 
2016 
Turnout 
2020 
Turnout Change 
No Change 
58.5% 
63.9% 
5.5 pts 
Minor Change 
59.1% 
65.6% 
6.5 pts 
Major Change 
54.6% 
59.1% 
4.6 pts 
Table 3. Estimated 2016 and 2020 VAP Turnout of Precincts with No Change from the 
2016 General to 2020 General Election, Minimal Change (>90% Continuity), and Major 
Change (<90% Continuity) 
 
While the statistics we present in Table 3 are suggestive that reprecincting has a negative 
effect on turnout rates, we cannot be certain, because Table 1 suggests that precincts are not 
randomly assigned among the three types of groups. Precincts that experience major changes are 
more diverse and urban, and it could be other spurious correlations, such as precincts’ diversity, 
account for the turnout differences in Table 2. To further explore the relationship between 
changing precinct boundaries and voter turnout, we estimate a linear state fixed-effects model 


---

19 
 
using the various independent variables described previously as predictors. We estimate two 
models. In Table 3 we present estimated coefficients, standard errors, and t-statistics for Model 
1, which excludes states and localities that run all-mail elections or offer Election Day vote 
centers, and Model 2, which includes only these states and localities.  
Our primary interest is the estimated relationship between Precinct Continuity and 
change in voter turnout. Because we estimate linear regression models, the coefficient is the 
estimated effect of the change of an independent variable on the change in a precinct’s VAP 
voter turnout rate from 2016 to 2020 (here, expressed as a value varying between -1 and 1).8 In 
states where voters cast ballots at geographically-bound polling places on Election Day, we see 
from Model 1 that changing precinct boundaries is negatively associated with turnout. This 
relationship is statistically significant with a t-statistic of 2.82. The direct effect is that a precinct 
without a boundary change has a 9.4 point higher turnout rate than one where only 50% of the 
precinct’s VAP continued from 2016 and 2020. Further supporting this effect on turnout is that 
for states and localities that run all-mail elections or offer Election Day vote centers, the 
relationship is weaker and in the opposite direction but not statistically significant, with a t-
statistic of -1.38. 
 
 
 
8 We investigated alternative model specifications, such as including the square and higher order polynomials of 
Precinct Continuity, to reflect the apparent non-linear relationship between precinct change and turnout change 
evident in Table 2. However, we could not recover the apparent non-linear relationships in Table 2 when we control 
for other factors. We choose to present the simple linear effect of Precinct Continuity since it is the easiest to 
interpret.    


---

20 
 
 
  
Model 1 
  
Model 2 
Variable 
Coefficient 
(Standard 
Error) 
t-stat 
Coefficient 
(Standard 
Error) 
t-stat 
Precinct Continuity 
0.188 
2.82   
-0.099 
-1.38 
  
(0.067) 
(0.071) 
% At Same Home > 1 Year 
0.261 
3.35 
-0.106 
-1.50 
  
(0.078) 
(0.071) 
Precinct Continuity x 
-0.189 
-2.43 
0.140 
1.46 
   % At Same Home > 1 Year 
(0.078) 
(0.095) 
Split Precinct 
-0.006 
-0.49 
-0.010 
-3.64 
  
(0.011) 
(0.003) 
% Non-Hispanic Black 
-0.072 
-8.49 
-0.039 
-2.23 
  
(0.008) 
(0.017) 
% Hispanic 
-0.054 
-5.42 
-0.097 
-3.23 
  
(0.010) 
(0.030) 
% Age 18-34 
-0.059 
-7.73 
-0.030 
-2.27 
  
(0.008) 
(0.013) 
% Some College or More 
-0.002 
-0.16 
-0.060 
-5.18 
  
(0.012) 
(0.012) 
% Income > $75K 
0.032 
1.19 
0.004 
0.09 
  
(0.027) 
(0.048) 
Population Density 
-0.062 
-2.88 
-0.535 
-5.86 
   (per 100,000K VAP) 
(0.021) 
(0.091) 
Log County VAP 
0.001 
0.80 
0.003 
2.53 
  
(0.001) 
(0.001) 
(State Fixed-Effects Omitted) 
—— 
  
Observations 
126,289   
  
17,972   
R-Sq 
0.1588   
  
0.0854   
 Table 3. OLS Regression Estimating 2016 to 2020 Turnout Change, with State Fixed 
Effects and Within-State Variance 
 
 
 


---

21 
 
The evidence that precinct changes negatively affect turnout is supported further when 
examining the relationship between turnout and precinct changes in precincts with more stable 
populations. As we expect, the direct relationship between % At Same Home > 1 Year in Model 
1 is positive, as these people may have deeper ties to their communities. However, having a 
deeper tie with a community may work against a person who has voted at the same precinct over 
multiple elections. The negative estimated coefficient on the interaction term between Precinct 
Continuity and % At Same Home > 1 Year suggests long-term residents of a precinct may be 
confused by a change to a precinct boundary change, mistakenly go to the wrong precinct, and 
then fail to vote. The interactive effect is statistically significant with a t-statistic of -2.43. 
Fortunately, the substantive effect is small. The average percentage of VAP residing in a precinct 
one year or longer is 87%, which contributes an additional 2.4 percentage points to lower turnout 
for the few precincts where only fifty percent of the population continued from 2016 to 2020. 
Supporting further that precinct boundary changes negatively affect turnout is that in Model 2 – 
for the all-mail and Election Day vote center states and localities – the interaction effect is not 
statistically significant, as expected, since voters in these states do not vote at polling places. 
There are good governance election administration reasons to split precincts. When they 
become too large by law or local policy decisions, election officials may create two or three 
precincts out of a single precinct. There is little support for this in our estimations. Precinct Split 
is signed negative, opposite of the expected effect, although it is not statistically significant with 
a t-stat of -0.49. Curiously, the effect of Precinct Split is negative and statistically significant for 
those states and localities that use all-mail balloting or Election Day vote centers. The effect is 
substantively small, however, of a single percentage point.  


---

22 
 
Another potential indicator of improved election administration is the Log County VAP, 
which we include in our models as an indicator of election official resources. In both models, the 
estimated coefficients are positive, but it is statistically significant only in Model 2 among states 
offering all-mail ballot election or Election Day vote centers. We might have expected the 
opposite since these reforms are generally thought to reduce the cost of administering elections. 
The racial and ethnic variables perform as expected on change in VAP turnout rates from 
2016 to 2020, as drawn from the Current Population Survey statistics we present in Table 1. The 
greater the share of the Non-Hispanic Black or percent Hispanic, the lower the change in turnout, 
compared with the effectively omitted category of non-Hispanic White. This negative 
relationship among racial and ethnic categories is separate from the statistically significant 
negative relationships evident in both models between Population Density and turnout change, 
meant to capture urban and rural differences. We add this variable to our models to control for 
the differences in precinct changes we observed in Table 1 and Table 2. We might have expected 
a more of a positive relationship given that precincts that experienced major changes had the 
lowest turnout rate increases. We might interpret Population Density as indicative of President 
Donald Trump’s rural support base which he effectively rallied in the 2020 election. 
The other demographic variables do not perform as we expect from the Current 
Population Survey statistics we present in Table 1. The small and statistically insignificant 
positive relationship between % Income > $75 and turnout change may be reflective of the small 
negative relationship in observed in Table 1. The effect of education on turnout change is more 
difficult to reconcile since Table 1 revealed a positive relationship of higher % Some College or 
More, while our estimation finds a negative relationship that is statistically significant only 
among states and localities using all-mail elections and those that offer Election Day vote 


---

23 
 
centers, and its substantive effect is relatively small. Likewise, % Age 18-34 of a precinct’s VAP 
is negative and statistically significant in both models when in Table 1 it is positive relative to 
other age groups. It may be that precincts with the highest density of younger, college educated 
people could be found in on-campus polling locations that had lower turnout in the midst of the 
COVID emergency when many campuses had moved to virtual instruction. 
Conclusion 
 
Precincts are a critical component to election administration. They define the collection 
of registered voters who are offered in-person voting at a particular polling place on Election 
Day, the resources that will be allocated to the precinct, what ballot styles will be distributed to 
voters, and the reporting of election results. Sometimes election officials change precincts, 
ostensibly to improve voters’ experiences by better managing the flow of voters through polling 
locations (Haspel and Knotts 2005). It is possible, however, that precinct changes could confuse 
long-time residents who suddenly have to vote in a new location or increase the distance of some 
voters to their polling location, thereby decreasing their turnout rates (Amos, Smith, and Ste. 
Claire 2017). This negative turnout effect may be mitigated fully or partially by alternative 
voting options, such as mail balloting and in-person early voting (Brady and McNulty 2011; 
Amos, Smith, and Ste. Claire 2017; Clinton et al. 2021). 
Prior studies of precinct changes have essentially been case studies of particular localities 
or states. We offer the first national investigation of the turnout effects of precincts that changed 
their boundaries from the 2016 to 2020 presidential elections. We find that even in the unusual 
2020 election where voters used mail balloting and in-person early voting options at 
unprecedented rates (McDonald 2022), states and localities that offered in-person Election Day 
voting experienced lower turnout among precincts with boundary changes than those that did 


---

24 
 
not, a finding most consistent with Amos, Smith, and Ste. Claire’s (2017) study of Manatee 
County, Florida. In all-mail ballot and Election Day vote center states, election officials 
administer precincts primarily for reasons that have little to do with turnout rates, such as 
determining the ballot style or reporting of election results. For these jurisdictions, we observe no 
direct turnout effects of precinct boundary changes. This comparison to a pseudo-control group 
provides us confidence that our observations are not a spurious effect. Indeed, we further see 
that, consistent with the potential to confuse voters first articulated by Haspel and Knotts (2005), 
the negative effect of precinct boundary changes is attenuated in precincts with a greater share of 
new residents, people who should be reasonably less confused by precinct changes and polling 
place changes that may accompany them. Further, we see that this effect is present only among 
states and localities that offer in-person Election Day voting within precincts. 
We do not observe that election officials splitting precincts because they have grown too 
large offsets these negative turnout effects of changing precinct boundaries, as supposed by 
Haspel and Knotts’s (2005) study of a 2001 Atlanta mayoral election. There are good reasons for 
election officials to better manage precinct operations by reducing the number of people who 
vote at a polling location. Our study suggests that election administrators should take care when 
doing so to minimize disruptions, and we encourage election officials to avail themselves to 
robust communication with affected voters. 
Finally, we note potential voting rights concerns, as Amos, Smith, and Ste. Claire (2017) 
find among Manatee County, Florida Hispanic voters. Precincts that undergo major changes to 
their boundaries tend to be more often located in minority communities. These major changes 
have the greatest potential to depress voter turnout, and thus further emphasizes the need for 


---

25 
 
election officials to take care when altering precinct boundaries and to communicate as 
effectively as possible with affected voters when they do. 
 
 
 


---

26 
 
References 
Amos, Brian, Daniel Smith, and Casey Ste. Claire. 2017. “Reprecincting and Voting 
Behavior.” Political Behavior 39(1): 133-56. 
Amos, Brian and Michael P. McDonald. 2020. “A Method to Audit the Assignment of 
Voters to Districts.” Political Analysis 28(3): 356-71. 
Amos, Brian, Michael P. McDonald, and Russell Watkins. 2017. “When Boundaries 
Collide: Constructing a Database of Election and Census Data.” Public Opinion 
Quarterly 81(S1): 385-400. 
Beard, Charles A. 1909. “The Ballot’s Burden.” Political Science Quarterly 24(4):589-
614. 
Biggers, Daniel R. and Michael J. Hanmer. 2015. “Who makes voting convenient? 
Explaining the adoption of early and no-excuse absentee voting in the states.” 
State Politics and Policy Quarterly 15(2): 192–210. 
Brady, Henry and John E. McNulty. 2011. “Turning Out to Vote: The Costs of Finding 
and Getting to the Polling Place.” American Political Science Review 105(1): 115-
34. 
Clinton, Joshua D., Nick Eubank, Adriane Fresh, and Michael E. Shepherd. 2021. 
“Polling Place Changes and Political Participation: Evidence from North Carolina 
Presidential Elections, 2008–2016.” Political Science Research and Methods 9(4): 
800-17. 
Hasen, Richard L. 2012. The Voting Wars: From Florida 2000 to the Next Election 
Meltdown. New Haven: Yale. 


---

27 
 
Haspel, Moshe H. and Gibbs Knotts. 2005. “Location, Location, Location: Precinct 
Placement and the Costs of Voting.” The Journal of Politics 67(2): 560-73. 
Herrnson, Paul S., Michael J. Hanmer, Richard G. Niemi. 2012. “The Impact of Ballot 
Type on Voter Errors.”  American Journal of Political Science 56(3): 716-730. 
Hur, Aram, and Christopher H. Achen. 2013. “Coding Voter Turnout Responses in the 
Current Population Survey.” Public Opinion Quarterly 77(4): 985-93. 
Gimpel, James. G., & Schuknecht, J. E. 2003. Political participation and the accessibility 
of the ballot box. Political Geography 22 (5): 471–88. 
McDonald, Michael P. 2022. From Pandemic to Insurrection: Voting in the 2020 US 
Presidential Election. Boston: De Gruyter. 
McDonald, Michael P. and Samuel Popkin. 2001. "The Myth of the Vanishing Voter." 
American Political Science Review 95(4): 963-974. 
Stein, Robert and Greg Vonnahme. 2008. “Engaging the Unengaged Voter: Vote Centers 
and Voter Turnout.” Journal of Politics 70(2): 487-97. 
Wolfinger, Raymond E., and Steven J. Rosenstone. 1980. Who Votes? New Haven: Yale 
University Press. 
