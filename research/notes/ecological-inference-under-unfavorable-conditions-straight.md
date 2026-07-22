---
title: 'Ecological inference under unfavorable conditions: Straight'
id: ecological-inference-under-unfavorable-conditions-straight
tags:
- inference-ecologique
- ei-empirique
- thomsen-estimateur
- king-ei
created: '2026-07-21T18:28:08.748644Z'
updated: '2026-07-21T18:39:17.616381Z'
source: https://gvpt.umd.edu/sites/gvpt.umd.edu/files/pubs/Park%20Hanmer%20Biggers%20ES%20Ecological%20Inference%20Under%20Unfavorable%20Conditions.pdf
source_domain: gvpt.umd.edu
fetched_at: '2026-07-21T18:28:08.748361Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Park, Hanmer & Biggers (Electoral Studies 2014) stress-test the Thomsen (1987)
  latent-structure EI estimator against heterogeneous units and small samples using
  2000 Florida ballot-image data (2.8M ballots) as verified ground truth, comparing
  it head-to-head with King's (1997) EI. Thomsen's index of dissimilarity stays low
  across diverse counties (2.72% Miami-Dade, 3.50% Palm Beach, 5.15% Sarasota, 6.59%
  Lee) and remains stable down to 30-50 aggregation units in a resampling test on
  a hypothetical 2915-precinct state. King's EI is shown to be badly wrong on some
  cells (e.g., estimating Bush/Senate-Democrat crossover at 0.19% vs. actual 3.13%,
  a 21x factor of error) and to invert the sign of key substantive relationships that
  Thomsen recovers correctly; EI systematically overstates straight-ticket voting
  and understates split-ticket voting.
raw_file: raw/ecological-inference-under-unfavorable-conditions-straight.pdf
---

Ecological inference under unfavorable conditions: Straight
and split-ticket voting in diverse settings and small samples
Won-ho Park a, Michael J. Hanmer b, *, Daniel R. Biggers c
a Department of Political Science and International Relations, Seoul National University, 1 Gwanak-ro, Gwanak-Gu,
Seoul 151-742, Republic of Korea
b Department of Government and Politics, University of Maryland, 3140 Tydings Hall, College Park, MD 20742, United States
c Institution for Social and Policy Studies, Yale University, 77 Prospect Street, P.O. Box 208209, New Haven, CT 06520-8209, United States
a r t i c l e
i n f o
Article history:
Received 27 September 2013
Received in revised form 26 June 2014
Accepted 21 August 2014
Available online 4 September 2014
Keywords:
Voting
Straight-ticket voting
Ecological inference
a b s t r a c t
Problems of ecological inference have long troubled political scientists. Thomsen's (1987)
estimator for ecological inference has been shown to produce estimates close to the in-
dividual level estimates for transitions across elections, but it is unknown how well it
performs under unfavorable conditions. We ﬁll this void by testing the estimator as the
across-unit variance increases and introduce a new procedure to examine the bias of the
estimates as the number of aggregate units decreases. Looking at partisan voting patterns
across races within the 2000 general election in Florida counties and taking advantage of
ballot image data to study straight-ticket voting we demonstrate that the estimator per-
forms well in both heterogeneous societies and when the number of aggregate units is
limited.
© 2014 Elsevier Ltd. All rights reserved.
1. Introduction
Ecological inference problems are well-known in the
ﬁeld of political science. Essentially, scholars face a problem
of deﬁcient data, as often they must make assertions about
some micro-level relationship through the employment of
aggregate-level data. Researchers' concerns about the
cumbersomeness of the assumptions required to generate
reliable estimates of the lower-level phenomenon have
caused them to raise questions about the quality of results
procured through such analyses and also stimulated their
design of a number of estimation strategies.
Researchers commonly use ecological inference tech-
niques to determine voter transition rates across elections,
i.e., the proportion of voters who vote for the same party
across two elections and the proportion who switch to
another political party. For such analyses, the Thomsen
(1987)
estimator
exhibits
certain
characteristics
that
permit it to generate estimates from aggregate data that are
close to the individual-level estimates (Thomsen et al.,
1991; Achen, 2000; Hanmer and Traugott, 2004; Park,
2008a). Moreover, Park (2008a) shows that it performs
better than other common estimators. Despite its demon-
strated success, we possess limited knowledge of how the
estimator performs under less than ideal conditions. Con-
cerns about an estimator's performance when substantial
diversity exists within or across the units of analysis, as well
as when the sample size is small, are common to all esti-
mators. Thomsen (1987, 55), however, makes an important
identiﬁcation assumption about the relationship between
the individual-level units and how they relate to the
aggregated units, namely that “the variation between in-
dividuals has the same structure as the variation between
districts.” Since ecological inference is essentially a prob-
lem of aggregation, examining circumstances when this
sort of homogeneity is not present across the aggregate
* Corresponding author. Tel.: þ1 301 405 7379.
E-mail addresses: wpark@snu.ac.kr (W.-h. Park), mhanmer@umd.edu
(M.J. Hanmer), daniel.biggers@yale.edu (D.R. Biggers).
Contents lists available at ScienceDirect
Electoral Studies
journal homepage: www.elsevier.com/locate/electstud
http://dx.doi.org/10.1016/j.electstud.2014.08.006
0261-3794/© 2014 Elsevier Ltd. All rights reserved.
Electoral Studies 36 (2014) 192e203


---

units is highly important. Unfortunately, researchers have
scant information to bring to bear when attempting to
judge the performance of the Thomsen estimator in these
situations.
We ﬁll these voids in the literature, testing the estimator
as both the across-unit variance increases and the number
of aggregate units decreases. We do so by examining voting
patterns within a single election (straight and split-ticket
voting) in ten individually and collectively diverse Florida
counties in the 2000 general election. These data are
particularly well suited to test the Thomsen estimator.
Using ballot image data as our measure of actual vote
proportions, we ﬁnd that the Thomsen estimator is robust
to individually and collectively diverse settings. In addition,
the introduction of a new resampling procedure reveals the
stability of the estimates in the context of limited numbers
of aggregation units, suggesting that thirty to ﬁfty such
units are more than sufﬁcient to determine the underlying
individual-level relationship. This bodes well for scholars of
comparative and U.S. state and local politics, who often use
data sets ﬁxed at this size (e.g., ﬁfty states). Studies of
electoral dynamics frequently turn to ecological inference
techniques to infer individual-level relationships from
aggregate-level electoral results in the United States and,
among others, Czechoslovakia, India, Italy, Japan, Post-
Soviet
Russia,
Uruguay,
and
Western
Europe
(e.g.,
Alexseev, 2006; Altman, 2002; Benoit et al., 2006; Burden,
2009; Burden and Kimball, 1998, 2002; Chandra, 2009;
Golder, 2003; Hanmer and Traugott, 2004; Kopstein and
Wittenberg, 2009; Hanmer et al. 2010). The conﬁdence in
the Thomsen estimator created by our results suggests a
number of potential applications that can be implemented
with easy to use software that we have provided at http://
cpc.snu.ac.kr/computing/stata.
2. Ecological inference and the Thomsen estimator
Ecological inference is essentially a problem of statisti-
cal under-identiﬁcation. Researchers have interest in the
process behind some micro-level occurrence, but the
aggregate data available are insufﬁcient for such a deter-
mination. To draw inferences in such cases, researchers
must make strong assumptions upon which both the val-
idity and accuracy of the estimator heavily rely. While
collecting individual-level data would present a more
straight-forward manner of addressing the relationship in
question, the cost or availability of such data sets often
leaves scholars with no choice but to use ecological infer-
ence techniques. This realization has spurred signiﬁcant
discussion and advances in the ﬁeld (Achen and Shivley,
1995; Adolph and King, 2003; Adolph et al., 2003; Brown
and Payne, 1986; Calvo and Escolar, 2003; Cleave et al.,
1995; Elff et al., 2008; Greiner and Quinn, 2009; Herron
and Shotts, 2003a,b, 2004; Johnston and Pattie, 2000;
King, 1997; Rosen et al., 2001; Tam Cho, 1998; Tam Cho
and Gaines, 2004; Thomsen, 1987; Wakeﬁeld, 2004), with
a number of statistical techniques suggested to address the
problem of ecological inference.
One common application of these techniques is to voter
transition rates across elections. The attempt to estimate
these rates from aggregate data presents a prime example
of a typical ecological inference problem. Scholars often
wish to estimate partisan loyalty or defection rates of voters
in two consecutive elections (the transitions), but may lack
adequate information to do so. Usually, the collection of
individual-level data to determine these rates is either
impossible or unfeasible, especially with regards to ques-
tions of a historical nature or when survey data do not exist
(as is often the case in non-Western countries). When
survey data do exist, they often cannot be reduced to
smaller aggregate units (such as a national survey sample
into states or congressional districts) because the samples
within each unit are too small for reliable analysis. In
addition, it is well documented that inaccurate reporting of
voting behavior can plague survey data (see, e.g. Belli et al.,
2001; Duff et al., 2007).
In such circumstances, aggregate-level records are
usually more accurate, extensive, and collected at relatively
small geographic units. Aggregate-level data, however,
provide us with a problem of unknown data. While the
researcher knows the electoral support received by n
competing parties for two consecutive elections (marginal
probability) in each observational unit, no information
exists about the individual counts for all possible n2 cells
(joint probabilities). In this instance, the goal of ecological
inference is to infer the unknown individual voting choice
based on the known aggregate information (marginal vote
fractions).
While researchers have employed a number of ecolog-
ical inference techniques to analyze voter transition rates
(see Altman, 2002; Benoit et al., 2006; Brown and Payne,
1986; Burden, 2009; Burden and Kimball, 1998, 2002;
Chandra, 2009), Thomsen's (1987) estimator is particu-
larly well suited to do so. The intuition behind the Thomsen
estimator is that two consecutive elections should be
treated symmetrically (as opposed to treating the second
election as the dependent variable inﬂuenced by the ﬁrst
election), with the two election outcomes being the result
of one common latent factor. Since this latent factor drives a
voter's choices in the two elections and links voting
behavior across elections, we may conceptualize it as an
underlying partisanship dimension.
Call this latent variable at the individual level d*
i , and the
vote choice in a given election at time t as dt, which would
be a binary variable. Deﬁne F() as the cumulative distri-
bution function of the standard normal distribution. In its
simplest form, we may write.
Probðdti ¼ 1Þ ¼ F

at þ btd*
i þ eti

:
(1)
When this is aggregated to the district level, the aggregate
outcome Dtj we observe in a given district j should corre-
spond to the expected vote fractions in the district using
the above equation. Assuming with Thomsen that the un-
derlying dimension d*
ij is normally distributed with mean
D*
j and a constant variance s2, we ﬁnd the average of both
sides of the above equation:
E

dtij

¼ Dtj ¼
Z ∞
∞
F

at þ btd*
ij þ etij

f

d*
ij
D*
j ; s2
vd*
ij:
(2)
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
193


---

By carrying out the integral, we obtain (Achen and Shivley,
1995, p. 184):
E

dtij

¼ Dtj ¼ F
0
B
@
at þ btD*
j
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 þ b2
t s2
q
1
C
A:
(3)
Or more simply.
D1j ¼ F

A1 þ B1D*
j

and D2j ¼ F

A2 þ B2D*
j

:
(4)
Since the D*
j term here is latent which we do not observe,
we want to factor out the term by writing:
F1
D1j

¼ A0 þ B0F1
D2j

:
(5)
Of course, the model is not identiﬁed and will not allow us
to estimate the parameters that involve the latent term, but
it at least establishes that the inverse-probit of the two
aggregate electoral outcomes are linearly related and joint-
normally distributed. With this result, we can identify the
voter transition rates.1
In addition to this micro-foundation modeling now
incorporated into the estimator (Achen, 2000), the Thom-
sen estimator maintains the advantage of being able to deal
with the non-linearity that arises with voter transition
rates, the problems of which can be more severe than in
usual aggregate data sets (Park, 2008a). Failing to deal with
the problem of nonlinearity native to the voter transition
model causes bias and inconsistency. The Thomsen model
is non-linear in its speciﬁcation, which guards against these
concerns and prevents the estimates of voting probabilities
from falling outside of the logical range (0e1), a problem
with
other
methods
such
as
ecological
regression
(Goodman, 1953, 1959). The estimator has been demon-
strated to provide favorable (Cleave et al., 1995) or superior
estimates to other existing strategies, such as King's (1997)
ecological inference method (Park, 2008a). Though the
comparison of estimators is not our objective here, our
analyses conﬁrm that the Thomsen estimator consistently
outperforms King's EI in estimating the outcomes of in-
terest here (see more below, including Appendix Tables A
and B, for a comparison of these estimates).2
The estimator has been shown to produce estimates
very close to the individual voter transition rates across
elections in several contexts. In his review of the estimator,
Achen (2000) concludes that tests of the estimator suggest
it to be quite successful. Thomsen et al. (1991) and
Thomsen (2000) show that the estimator performs well
using aggregate data for elections in Denmark, Finland, and
Sweden over four decades. Park (2008a) successfully ap-
plies this estimator to both British parliamentary elections
in the 1960s and South Korean presidential elections in the
1990s. The Thomsen estimator has also been used by Park
(2008b) to generate reliable estimates of voter transition
rates for different groups in South Korea in presidential
elections in the 1980s. Hanmer and Traugott (2004)
generate remarkably close estimates of individual-level
ballot image data for partisan voting patterns from one
race to another for the 2000 general election in Oregon.
While researchers largely employ the Thomsen estimator
to estimate voting patterns across elections, it can also be
used to estimate patterns within an election (i.e., from one
race to another within the same ballot). The estimator's suc-
cess in this arena opens the door to a number of applications.
The extent to which (and the reasons why) voters split their
ballots is a central question in the voting behavior literature.
Over the past two decades, scholars have expended sub-
stantial effort to comprehend better the circumstances under
which split-ticket voting and divided government occur
(Alesina and Rosenthal, 1995; Beck et al., 1992; Burden and
Kimball, 1998; Fiorina, 1996; Jacobson, 1990; Lewis-Beck
and Nadeau, 2004; Roscoe, 2003). Conventional wisdom
related to the potential increased party polarization over the
past two decades (Abramowitz and Saunders, 1998; Carsey
and Layman, 2006; Jacobson, 2000; Layman and Carsey,
2002) suggests that the incidences of split-ticket voting and
divided government should decline signiﬁcantly, which rai-
ses interesting and important questions about why either
might continue to prevail at such high rates. Some, most
notably Fiorina (1996), assert that the answer to these ques-
tions derives mainly from the general population's interest in
balancing the power of the two parties, which serves as a
manner to moderate public policy that better matches their
less extreme preferences. Accurate estimates of how many
voters split their ballots (and why) can thus help scholars
understand the extent to which divided government (and
policy-balancing) is actually desired by the population
(Burden and Kimball,1998). Additionally, given the interest in
partisan polarization, as well as rapid changes in election
procedures (such as early voting, absentee voting, and the
introduction of electronic voting machines) that might alter
partisan behavior within a single election, techniques to
provide reliable estimates of individual-level behavior from
aggregate data (such as straight and split-ticket voting) are
becoming increasingly important.
Previous investigations have attempted to study straight
and split-ticket voting using other ecological inference es-
timators with mixed success (Burden and Kimball, 1998),
but the Thomsen estimator, with its partisan micro-
foundation, is particularly well suited for studying partisan
voting patterns across races within a single election. This is
especially true when thinking about the assumed common
latent partisanship dimension: in a given electionwhere the
1 An additional challenge in estimating the voter transition rates, if not
more difﬁcult than the ecological inference process itself, is the problem
of dealing with multiple parties (“the R  C case”). Here, we used the
iterative proportional ﬁtting (IPF) process after estimating all the possible
bivariate combinations of voter transitions. IPF, also known as “raking,” is
a mathematical scaling procedure to adjust a matrix of any dimension to
converge to some pre-deﬁned row and column totals, where the con-
straining row and column totals are obtained from alternative sources,
and has been used to adjust the cell frequencies or proportions from
survey estimates to conform to the marginal distribution of the same
census variables (Deming and Stephan, 1940). The theoretical un-
derpinnings of IPF blend well with the task of dealing with the R  C case
in the ecological inference context and we use it here (see Park, 2008a for
more details).
2 EI analysis is run in R using the ecological inference code integrated
into Zelig (Imai et al., 2007a,b), which implements models using a
nonlinear least squares approximation (Wittenberg et al., 2007). In
contrast to earlier ecological inference approaches that are Bayesian in
nature (see for example Rosen et al., 2001), this strategy implements a
frequentist approximation of these Bayesian models. As such, it is not
Bayesian by design and does not require priors or starting values to be
speciﬁed.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
194


---

same set of voters participates, the assumption will most
likely hold. In two elections over time, partisanship may
decay and the electorate may change.
We focus here on its performance under less favorable
conditions than those where researchers have previously
used this estimator. For example, we possess limited knowl-
edge about the performance of the Thomsen estimator when
applied to diverse aggregate units. The studies described
above all generate estimates close to the individual-level pa-
rameters in the context of relatively homogenous settings,
suchasOregon, Scandinavia, and South Korea (Thomsen et al.,
1991; Thomsen, 2000; Hanmer and Traugott, 2004; Park,
2013). While the ability to do so is important for the study
of comparable cases, we have no investigations fromwhich to
judge the estimates based on heterogeneous societies. This
dearth of information is signiﬁcant because Thomsen's iden-
tifying condition requires the ecological correlation in the
aggregate electoral data to equal that of the individual cor-
relations between the vote propensities, an assumption he
maintains will hold as the aggregate units tend toward ho-
mogeneity in comparison to one another. Thomsen's (1987)
homogeneity
assumption
is
another
expression
for
assuming away the “grouping problem” that is at the heart of
aggregation bias (see especially page 52). For example, King
(1997) notes that if the grouping process (that is, the aggre-
gation of individuals in the same aggregate unit) is correlated
with the dependent variable, the ecological estimates will be
biased (see page 50). Thus, violations could have severe con-
sequences for the estimator's performance.3
Although subsequent extensions relax and appease some
concerns about this assumption (Achen, 2000), we lack
empirical evidence to support this claim, as the studies cited
above cannot inform us about the robustness of the esti-
mator to heterogeneity both across and within the aggre-
gated units of analysis. Or, to posit the concern in another
way, we cannot determine from existing studies whether or
not “potential applications are … restricted to homogenous
settings with good herring on the menu” (Achen, 2000, 16).
Additionally, we have minimal knowledge about how
well the Thomsen estimator performs with a limited num-
ber of aggregate units. In instances where the number of
units is small, concerns emerge about the performance of
any estimator. While the Thomsen estimator performs well
under favorable circumstances, scholars have yet to inves-
tigate its ability to recover the individual relationships in
situations with small samples. In most cases, the number of
aggregate units is ﬁxed (e.g., ﬁfty states), leaving no ability to
expand the number of units by, for example, simply col-
lecting more data. Given the ﬁxed nature of the data, to
generate reliable results the estimator must be robust to
changes in the sample size. As such, identifying the perfor-
mance of the Thomsen estimator under unfavorable con-
ditions is crucial to understanding the ultimate utility of its
application
in
addressing
substantive
problems
with
aggregate data.
3. Data
We ﬁll this void by ﬁrst examining the performance of
the Thomsen estimator in the setting of ten individually
and collectively diverse counties in Florida in the context of
the 2000 general election.4 The data were provided by The
Washington Post as part of the media's effort to investigate
the issues with ballots and voting technology that arose
during this election.5 For the analyses below, we focus on
four counties (Miami-Dade, Lee, Palm Beach, and Sarasota)
that represent the substantial racial/ethnic and partisan
diversity found across the locales.6 Along racial and ethnic
lines, they cover the range of the Blau (1977) diversity
index for all ten counties (from 0.19 to 0.59)7; Sarasota and
Miami-Dade are on the two extremes, with Lee (0.31) and
Palm Beach (0.47) almost equidistant from the national
average (0.40) in 2000.8 In comparison to the national
population size of African Americans (12.3%) and Latinos
(12.5%), these index scores correspond to much smaller
minority communities in Sarasota (4.2% and 4.3%) and Lee
(6.6% and 9.5%), a roughly comparable breakdown in Palm
Beach (13.8% and 12.4%), and a substantially larger minority
population in Miami-Dade (20.3% and 57.3%).
With regards to partisan diversity (as measured by
presidential vote choice in 2000), the four selected counties
equally cover the range of analyzed counties (from 0.45 to
0.53), with Palm Beach being the second least diverse
county, Lee and Miami-Dade in the middle, and Sarasota
among those with the greatest partisan diversity. Sub-
stantial partisan variation also exists across the individual
precincts of each county, as measured by the Democratic
percent of the presidential vote. With a standard deviation
in this vote choice ranging from 0.07 to 0.2 for the ten
counties, Lee and Sarasota Counties (both 0.09) exhibit
lower levels of precinct partisan heterogeneity, while Palm
Beach County (0.13) resides in the middle of the distribu-
tion of counties and Miami-Dade possesses the greatest
diversity across its precincts (0.2). This substantial variation
in voting-relevant characteristics provides ample hetero-
geneity in which to examine the estimator when a key
assumption is violated.
In contrast to many ecological inference analyses that
rely on survey data to determine accuracy, we had the
extraordinary opportunity to utilize as our measure of the
“truth” ballot image data from every single ballot actually
recorded in these counties in the 2000 election (almost 2.8
3 Note that traditional regression approaches such as Hanushek et al.
(1974) tackled this problem by controlling for a multitude of relevant
factors, hoping to make the aggregation units as homogenous as possible
after the control.
4 These
counties
include
Broward,
Highlands,
Hillsborough,
Lee,
Marion, Miami-Dade, Palm Beach, Pasco, Pinellas, and Sarasota.
5 The American National Election Study also made these data available
through
their
2000
Florida
Ballot
Project
(available:
http://www.
electionstudies.org/ﬂorida2000/data/data_ﬁles.htm).
6 These counties are selected for illustrative purposes only. Results are
similar for all counties and can be found in the Web Appendix.
7 This index ranges from zero to one, with zero indicating no diversity
(i.e., the entire population is white) and higher scores reﬂecting greater
heterogeneity in the population makeup. It is calculated by subtracting
from one the summed squares of each group's proportion of the total
population. More formally: Diversity ¼ 1  P
j
p2
j .
8 Both Palm Beach and Miami-Dade exhibit noticeably higher rates of
racial/ethnic diversity than Multnomah, OR (0.36), a locale previously
analyzed using the Thomsen estimator (Hanmer and Traugott, 2004).
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
195


---

million ballots in total). Doing so allows us to avoid concerns
with survey data about the lack of an adequate number of
individual cases per aggregation unit, as well as errors in the
responses. Because we know how each individual vote is
recorded (as opposed to one's recall of how he/she voted),
we can directly compare the Thomsen estimates to the
actual vote proportions cast. To do so, we use these ballot
images to examine the occurrence of straight and split-
ticket voting for president and member of the U.S. Senate,
the top two races on the ballot, and then aggregate the in-
dividual ballot images to the precinct-level to use as our
aggregate unit of analysis.9 Of course, one of the big lessons
fromthe2000 electionwas that voters make errors(Caltech/
MIT, 2001; Herrnson et al., 2008; Wand et al., 2001). If
anything, our use of these data provides a more stringent
test, especially in the case of Palm Beach County where the
butterﬂy ballot (see Wand et al., 2001), an exogenous shock,
served to disrupt the underlying micro-foundation.10
4. Results
4.1. Recovering voting patterns in diverse settings
We examine the Thomsen estimates for Miami-Dade
County ﬁrst. As noted earlier, Miami-Dade is diverse rela-
tive to the other counties in Florida and the nation as a
whole. This diversity is also marked by substantial hetero-
geneity in its Latino composition. Roughly half of the Latino
population, for example, is of Cuban descent, and such in-
dividuals tend to be much more likely to vote Republican
than the rest of the dominant Latino communities. In addi-
tion to the candidates for the two major parties, we examine
other candidates (votes for Nader added with votes for all
other candidates) and residual votes (combination of
undervotes and overvotes).11 Table 1A presents the actual
vote proportions tabulated from ballot images of straight
and split-ticket voting in the 2000 election, while Table 1B
presents the estimated vote proportions from precinct-
level data. As is evident, our Thomsen estimates from the
aggregate-level data are remarkably similar to the actual
vote proportions garnered from the individual-level ballot
images. Only in the case of voting for Gore and the Demo-
cratic candidate for Senate, Bill Nelson, does the difference
(0.80 points) in the estimated and actual vote proportions
surpass three-quarters of a percentage point, and only in
four of the other ﬁfteen cells does the difference exceed half
of a percentage point. Thus, scholars employing precinct-
level data and the Thomsen estimator would conclude
correctly, as evidenced by the ballot image data, that a
slightly larger percentage of Bush voters cast a vote for
Nelson than Gore voters cast a vote for the Republican
Senate candidate, Bill McCollum.12 The signiﬁcant similarity
between the actual and estimated vote proportions suggests
that the Thomsen estimator produces reliable predictions
when there is substantial demographic diversity within and
across the units of aggregation.
In addition to generating results that are incredibly close
to the actual vote proportions in the county, the Thomsen
estimator also captures a number of key relationships be-
tween vote transitions that are missed by other estimators.
That is, as well as the obvious value of getting closer to the
actual results than other techniques, the Thomsen esti-
mator ensures that the substantive conclusions supported
by the analysis are consistent with the relationships found
in the individual-level data. This contrasts sharply with
another common estimator, King's EI, which does not
recover several important patterns in the data and thus
would lead researchers to draw incorrect conclusions about
political behavior in the 2000 election. For example, as
noted above, in Miami-Dade both the ballot image results
and Thomsen results show that the proportion of Bush
Table 1A
Tabulated vote proportions from ballot images, Miami-Dade 2000.
U.S. Senate race
Republican
Democrat
Others
Resid.
votes
Total
President
Bush
35.55%
3.13%
1.02%
3.73%
265,211
Gore
3.03%
42.23%
2.15%
3.66%
311,879
Others
0.29%
0.50%
0.21%
0.10%
6691
Resid.
votes
0.73%
1.54%
0.44%
1.71%
26,927
Total
241,804
289,396
23,328
56,180
610,708
Note: Table A presents the actual vote proportions tabulated from the
ballot images, while Table B presents the Thomsen estimates of the vote
proportions by using precinct-level data aggregated from the ballot im-
ages. Index of dissimilarity ¼ 2.72% (measurement of the difference be-
tween the two transition matrices, deﬁned as the total sum of absolute
deviations divided by two).
Source: 2000 Florida Ballots Project.
Table 1B
Estimated vote proportions using Thomsen estimator from precinct-level
data (N ¼ 613), Miami-Dade 2000.
U.S. Senate race
Republican Democrat Others Resid. votes
President Bush
35.02%
3.44% 0.56%
4.41%
Gore
3.25%
41.43% 2.71%
3.68%
Others
0.56%
0.46% 0.02%
0.05%
Resid. votes
0.76%
2.06% 0.53%
1.06%
Note: Table A presents the actual vote proportions tabulated from the
ballot images, while Table B presents the Thomsen estimates of the vote
proportions by using precinct-level data aggregated from the ballot im-
ages. Index of dissimilarity ¼ 2.72% (measurement of the difference be-
tween the two transition matrices, deﬁned as the total sum of absolute
deviations divided by two).
Source: 2000 Florida Ballots Project.
9 We omit all precincts created to identify sets of absentee ballots from
our analyses, which creates a more conservative test as it reduces the
number of cases. The results remain robust for analyses (not shown) run
with the inclusion of these precincts.
10 Because we are concerned with testing the ability of the estimator to
recover the individual-level votes and, unlike tests using survey data, we
directly create the aggregate-level data from the individual-level data,
any errors voters made in terms of recording their intentions on the ballot
will be reﬂected at both the individual and aggregate levels.
11 The results are robust to disaggregating the combined categories.
12 Using the individual-level data, among those who voted for Bush,
7.2% voted for the Democratic Senate candidate, Bill Nelson. Among those
voting for Gore, 5.9% voted for the Republican candidate for Senate, Bill
McCollum. The Thomsen estimates of these proportions are 7.9% and
6.4%, respectively.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
196


---

voters who split their ticket by voting for the Democratic
Senate candidate was larger than the proportion of Gore
voters who split their ticket by voting for the Republican
Senate candidate. Not only are King's EI estimates far from
the mark in absolute terms, they also incorrectly suggest
voting for the other major party candidate in the Senate
race was more likely among Gore than Bush voters.13 In
other words, while Thomsen's estimator recovered the
relative rates of ticket-splitting among Democrats and Re-
publicans, the EI estimator did not. The EI estimates
relating
to
presidential
residual
votes
are
similarly
misleading. A key result in this election was that those
thought most likely to support Democrats were more prone
to voting errors. This feature is evident in both the ballot
image results (1.54% recorded a residual vote for president
and voted for the Senate Democrat while 0.73% recorded a
residual vote for president and voted for the Senate
Republican) and Thomsen results (2.06% recorded a resid-
ual vote for president and voted for the Senate Democrat
while 0.76% recorded a residual vote for president and
voted for the Senate Republican). The EI results do not
follow the same pattern, but rather indicate that more
presidential residual voters voted Republican for Senate
(0.04% recorded a residual vote for president and voted for
the Senate Democrat while 0.05% recorded a residual vote
for president and voted for the Senate Republican). In sum,
we see that the estimator one uses can clearly inﬂuence the
accuracy of the conclusions one can draw.14
To conduct a more formal analysis of the differences
between our ecological inference estimates and the true
vote proportions, we measure the index of dissimilarity
presented in Thomsen (1987). Thomsen et al. (1991)
describe the index of dissimilarity as “the proportion of
votes which must be relocated in one sub-table to construct
the other sub-table” (447). For example, take the 2  2
tables presented in Fig. 1 and constructed from hypotheti-
cal data to represent the actual and estimated vote pro-
portions. In the actual (hypothetical) data (1A), forty-ﬁve
percent of voters select both the Republican presidential
and senatorial candidates (RR), forty-ﬁve percent choose
both Democratic candidates (DD), and an equal number
(ﬁve percent each) divide their votes across the two split-
ticket options (RD and DR). The estimated results (1B),
however, correspond to RR, DD, RD, and DR support rates of
forty, ﬁfty, six, and four percent, respectively. The index of
dissimilarity between the two matrices is deﬁned as the
total sum of absolute deviations divided by two. As such,
we ﬁrst calculate these deviations, which are simply the
differences in each cell (45  40 ¼ 5; 5  4 ¼ 1; 5  6 ¼ 1;
45  50 ¼ 5). We then take the sum of their absolute
value (5 þ 1 þ1 þ 5 ¼ 12) and divide this ﬁgure by two. The
last step is taken since the relocation of some values ne-
gates the necessity to relocate others (i.e., to alter the actual
and estimated proportion of split-ticket voting, a shift of
one percent from the RD to DR cell balances those two cells
and does not require any reciprocal movement from the DR
to RD cell). In this hypothetical scenario, the index of
dissimilarity is 6% (12/2).
Returning to Tables 1A and 1B, we ﬁnd that the apparent
impressive performance of the Thomsen estimatorsuggested
by a cursory observation of the tables is conﬁrmed by the
implementation of this test. For Miami-Dade County, the
indexof dissimilarity between thetabulatedvote proportions
from ballot images and our estimated vote proportions from
precinct data is 2.72%. We should note that this index of
dissimilarity is lower than those calculated by other studies
employing the Thomsen estimator (Hanmer and Traugott,
2004; Thomsen, 2000; Thomsen et al., 1991) and lower
than the estimate from King's EI (see Appendix Table B).
While the Thomsen estimator performs best for Miami-
Dade (out of all ten counties), it produces impressive results
for the other counties as well. For example, in comparing
the tabulated vote proportions for Palm Beach (found in
Table
2A)
with
the
estimated
proportions
from the
precinct-level data (found in Table 2B), the difference is
greater than one percentage point in only one cell (that of
the residual votes in the race for president and votes for
Nelson), with an overall index of dissimilarity of 3.50%. The
test in Palm Beach is particularly interesting given that
county's use of the butterﬂy ballot, which led to an unex-
pectedly large proportion of votes for Pat Buchanan (Wand
et al., 2001). When we separate out the votes for Buchanan
from the “others” category, we see that the Thomsen esti-
mator recovers a key feature of the election results in Palm
Beachda disproportionate number of those who registered
a vote for Buchanan also voted for Nelson. That is, the
Thomsen estimate of
the proportion who voted for
Buchanan who then
selected
the Democratic
Senate
candidate of 72.21% is very close to the actual percentage of
71.99% calculated from the individual-level data.
The results in Sarasota County and Lee County are also
quite
good.
The
differences
between
the
tabulated
(Table 3A) and estimated (Table 3B) vote proportions for
Sarasota County are somewhat larger overall (with an index
of dissimilarity of 5.15%), but only in three cases do the cell
differences exceed a single percentage point (two per-
centage points in two of the cases). Even in the case of Lee
County (tabulated and estimated proportions found in
Tables 4A and 4B, respectively), where the index of
dissimilarity (6.59%) is largest, only four comparisons
exhibit a difference greater than one percentage point, with
only three of these variations near or above two percentage
13 King's EI estimates the total percentage of those voting for Bush and
the Senate Democrat as 0.19% (compared to 3.13% using the actual ballot
image data and 3.44% using Thomsen's approach), and the total per-
centage voting for Gore and the Senate Republican as 0.81% (compared to
3.03% using the ballot image data and 3.25% using Thomsen's approach).
Moreover, King's EI estimates the percentage voting for the Senate
Democrat among those who voted for Bush as 0.43% (compared to 7.21%
using the ballot image data and 7.93% using Thomsen's approach), and
the percentage voting for the Senate Republican among those who voted
for Gore as 1.59% (compared to 5.93% using the ballot image data and
6.37% using Thomsen's approach).
14 The results above that compare Thomsen to EI with respect to major
party straight- and split-ticket voting reﬂect a general pattern. Regression-
based techniques tend to overstate the degree of straight-ticket voting and
thus under-estimate split-ticket voting (see Park, 2008a for a proof con-
ﬁrming this bias). This is the case for EI in every county in our data set,
with some substantively large discrepancies. The Thomsen estimator
performs better in each case, by a factor as large as 21 and almost always
by a factor of 2 or more. We present the rates of major party straight- and
split-ticket voting from the actual ballot image data, as well as those
generated by the Thomsen and EI estimators, in Appendix Table A.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
197


---

Table 2A
Tabulated vote proportions from ballot images, Palm Beach 2000.
U.S. Senate race
Republican
Democrat
Others
Resid.
votes
Total
President
Bush
26.27%
3.90%
0.55%
1.16%
130,686
Gore
4.32%
50.69%
1.37%
2.62%
241,802
Others
0.57%
1.26%
0.33%
0.20%
9673
Resid.
votes
1.34%
3.64%
0.26%
1.50%
27,641
Total
133,195
243,816
10,300
22,491
409,802
Note: Table A presents the actual vote proportions tabulated from the
ballot images, while Table B presents the Thomsen estimates of the vote
proportions by using precinct-level data aggregated from the ballot im-
ages. Index of dissimilarity ¼ 3.50% (measurement of the difference be-
tween the two transition matrices, deﬁned as the total sum of absolute
deviations divided by two).
Source: 2000 Florida Ballots Project.
Table 2B
Estimated vote proportions using Thomsen estimator from precinct-level
data (N ¼ 506), Palm Beach 2000.
U.S. Senate race
Republican Democrat Others Resid. votes
President Bush
26.77%
3.06%
1.00%
1.06%
Gore
3.80%
50.51%
1.23%
3.47%
Others
1.05%
1.06%
0.10%
0.16%
Resid. votes
0.89%
4.87%
0.18%
0.80%
Note: Table A presents the actual vote proportions tabulated from the
ballot images, while Table B presents the Thomsen estimates of the vote
proportions by using precinct-level data aggregated from the ballot im-
ages. Index of dissimilarity ¼ 3.50% (measurement of the difference be-
tween the two transition matrices, deﬁned as the total sum of absolute
deviations divided by two).
Source: 2000 Florida Ballots Project.
Table 3A
Tabulated vote proportions from ballot images, Sarasota 2000.
U.S. Senate race
Republican
Democrat
Others
Resid.
votes
Total
President
Bush
42.28%
5.21%
0.88%
1.44%
69,836
Gore
4.75%
37.71%
1.27%
1.73%
63,742
Others
1.02%
1.30%
0.62%
0.21%
4411
Resid.
votes
0.44%
0.42%
0.06%
0.64%
2201
Total
67,968
62,593
3969
5660
140,190
Note: Table A presents the actual vote proportions tabulated from the
ballot images, while Table B presents the Thomsen estimates of the vote
proportions by using precinct-level data aggregated from the ballot im-
ages. Index of dissimilarity ¼ 5.15% (measurement of the difference be-
tween the two transition matrices, deﬁned as the total sum of absolute
deviations divided by two).
Source: 2000 Florida Ballots Project.
Table 3B
Estimated vote proportions using Thomsen estimator from precinct-level
data (N ¼ 141), Sarasota 2000.
U.S. Senate race
Republican Democrat Others Resid. votes
President Bush
44.17%
4.05%
0.55%
1.05%
Gore
2.46%
38.29%
2.01%
2.70%
Others
1.23%
1.53%
0.22%
0.17%
Resid. votes
0.63%
0.78%
0.05%
0.12%
Note: Table A presents the actual vote proportions tabulated from the
ballot images, while Table B presents the Thomsen estimates of the vote
proportions by using precinct-level data aggregated from the ballot im-
ages. Index of dissimilarity ¼ 5.15% (measurement of the difference be-
tween the two transition matrices, deﬁned as the total sum of absolute
deviations divided by two).
Source: 2000 Florida Ballots Project.
Fig. 1. Illustration of index of dissimilarity calculation via hypothetical data.
Table 4A
Tabulated vote proportions from ballot images, Lee 2000.
U.S. Senate race
Republican
Democrat
Others
Resid.
votes
Total
President
Bush
48.23%
4.90%
0.90%
1.10%
92,604
Gore
6.35%
31.14%
1.28%
1.21%
67,155
Others
0.97%
0.92%
0.50%
0.12%
4224
Resid.
votes
1.02%
0.60%
0.10%
0.66%
3994
Total
95,041
63,080
4660
5196
167,977
Note: Table A presents the actual vote proportions tabulated from the
ballot images, while Table B presents the Thomsen estimates of the vote
proportions by using precinct-level data aggregated from the ballot im-
ages. Index of dissimilarity ¼ 6.59% (measurement of the difference be-
tween the two transition matrices, deﬁned as the total sum of absolute
deviations divided by two).
Source: 2000 Florida Ballots Project.
Table 4B
Estimated vote proportions using Thomsen estimator from precinct-level
data (N ¼ 150), Lee 2000.
U.S. Senate race
Republican Democrat Others Resid. votes
President Bush
50.94%
2.94%
0.44%
0.82%
Gore
3.52%
32.28%
2.13%
2.05%
Others
1.20%
1.10%
0.13%
0.09%
Resid. votes
0.93%
1.24%
0.08%
0.14%
Note: Table A presents the actual vote proportions tabulated from the
ballot images, while Table B presents the Thomsen estimates of the vote
proportions by using precinct-level data aggregated from the ballot im-
ages. Index of dissimilarity ¼ 6.59% (measurement of the difference be-
tween the two transition matrices, deﬁned as the total sum of absolute
deviations divided by two).
Source: 2000 Florida Ballots Project.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
198


---

points. This minimal variation between the estimated and
actual vote proportions across all counties, combined with
index of dissimilarities that compare favorably with those
calculated by other studies (Hanmer and Traugott, 2004;
Thomsen, 2000; Thomsen et al., 1991), demonstrates the
ability of the Thomsen estimator to generate estimates
close to the individual-level estimates when faced with
signiﬁcant diversity (both racial/ethnic and partisan).
4.2. Thomsen estimator and small samples
The substantial similarity between the actual vote pro-
portions and our estimates for these counties provides
convincing evidence of the robustness of the Thomsen
estimator to signiﬁcant heterogeneity within and across
aggregate units. The counties analyzed here are also diverse
in terms of their size. Though the Thomsen estimator ten-
ded to perform better in the counties with a large number
of precincts, it also performed admirably in the counties
with a small number of precincts. For example, though the
estimates from Highlands County are based on only 18
precincts, the index of dissimilarity was just 5.78% (for
more see Web Appendix Tables 1Ae6B). We now turn to a
stricter test of the performance of the Thomsen estimator
as the number of aggregate units decreases.
To perform this more rigorous test, we developed a
resampling procedure using the individual-level ballot data
from Florida. First, for each county within a speciﬁed unit of
precincts (10, 20, 30, 50, 100, 200), we drew individual
ballots from a random sample of precincts. Second, we
calculated the relevant vote proportions and treated these
results as the “truth”. Third, we aggregated the individual
ballots by precinct. Fourth, we estimated the relevant vote
proportions based on the aggregate units generated from
the individual ballots. Fifth, for each cell, we calculated the
bias in the aggregate estimate, deﬁned as the difference
between the proportions calculated from the individual
ballot data and estimated proportion from the aggregated
precinct data. Finally, we repeated this process one thou-
sand times for each sample size.
Because the procedure calculates the bias for each indi-
vidual cell, we do not have space to present all of these re-
sults fora single county, let alone the four counties discussed
above. Instead, wefocus on the two counties with the lowest
Panel A: Straight-ticket Voting
0
50
100
150
200
0
50
100
150
200
-.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08
10
20
30
50
100
200
Density
Bias of the Ecological Estimator: Senate (Dem) and Presidential (Gore)
0
50
100
150
200
0
50
100
150
200
-.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08
10
20
30
50
100
200
Density
Bias of the Ecological Estimator: Senate (Rep) and Presidential (Bush)
Panel B: Split-ticket Voting
0
50
100
150
200
0
50
100
150
200
-.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08
10
20
30
50
100
200
Density
Bias of the Ecological Estimator: Senate (Dem) and Presidential (Bush)
0
50
100
150
200
0
50
100
150
200
-.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08
10
20
30
50
100
200
Density
Bias of the Ecological Estimator: Senate (Rep) and Presidential (Gore)
Fig. 2. Bias of the Thomsen estimates by sample size for Miami-Dade County. Note: Figures show the bias of the estimates in voting for the speciﬁed presidential
and senatorial candidates. Bias is deﬁned as the difference between the ecological estimate of the voting proportion and the actual ballot tabulation (i.e. a bias of
zero means that the estimated and actual proportions are the same). Source: 2000 Florida Ballots Project.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
199


---

and highest indices of dissimilarity (Miami-Dade and Lee,15
respectively), and only discuss the instances of major party
straight and split-ticket voting (i.e. Bush and McCollum,
Gore and Nelson, Bush and Nelson, Gore and McCollum).16
The estimates are presented in Fig. 2 (Miami-Dade) and
Fig. 3 (Lee), with the straight-ticket estimates shown in
Panel A and the split-ticket estimates in Panel B. In Miami-
Dade, across all four patterns of behavior the bias is quite
small. Even at just ﬁfty observations the errors never
exceed an absolute value of 0.02. Though the variance in
this distribution decreases as the sample size increases,
even at thirty observations the bias remains close to the
absolute value of 0.02. For the estimates of split-ticket
voting, Gore to McCollum and Bush to Nelson, the esti-
mate of the bias is quite close to zero, even at a sample size
of just twenty precincts (see Panel B of Fig. 2). While the
estimates for Lee County are more biased than those for
Miami-Dade, overall the bias tends to be small here as well.
With as few as thirty observations, across almost all of the
runs the bias is less than 0.04 in absolute value, and the
estimator does equally well in retrieving all four combi-
nations of straight and split-ticket voting. Thus, even with
the county that proves most difﬁcult for the Thomsen
estimator, accurate estimates of voting behavior can be
recovered from as little as thirty aggregate units.17
As a ﬁnal and even more conservative test of the
Thomsen estimator, we combine the precinct data from all
ten counties to create a hypothetical “state” comprised of
2915 precincts that exhibits greater variation than any sin-
gle county in the analysis. We perform the same resampling
procedure used for the individual counties, and present the
results in Fig. 4 for straight and split-ticket voting for
presidential and senatorial candidates (results are similar
across all combinations of cells).18 The low levels of bias in
Panel A: Straight-ticket Voting
0
50
100
150
200
0
50
100
150
200
-.08
-.04
0
.04
.08
-.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08
10
20
30
50
100
Density
Bias of the Ecological Estimator: Senate (Dem) and Presidential (Gore)
0
50
100
150
200
0
50
100
150
200
-.08
-.04
0
.04
.08
-.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08
10
20
30
50
100
Density
Bias of the Ecological Estimator: Senate (Rep) and Presidential (Bush)
Panel B: Split-ticket Voting
0
50
100
150
200
0
50
100
150
200
-.08
-.04
0
.04
.08
-.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08
10
20
30
50
100
Density
Bias of the Ecological Estimator: Senate (Dem) and Presidential (Bush)
0
50
100
150
200
0
50
100
150
200
-.08
-.04
0
.04
.08
-.08
-.04
0
.04
.08 -.08
-.04
0
.04
.08
10
20
30
50
100
Density
Bias of the Ecological Estimator: Senate (Rep) and Presidential (Gore)
Fig. 3. Bias of the Thomsen estimates by sample size for Lee County. Note: Figures show the bias of the estimates in voting for the speciﬁed presidential and
senatorial candidates. Bias is deﬁned as the difference between the ecological estimate of the voting proportion and the actual ballot tabulation (i.e. a bias of zero
means that the estimated and actual proportions are the same). Source: 2000 Florida Ballots Project.
15 Since Lee County has fewer than 200 precincts we vary the sample
size only up to 100 precincts.
16 While we focus on these comparisons, the results are similar across
all cells and across all counties. Estimates of the biases not presented here
are available from the authors upon request.
17 We also evaluated how the index of dissimilarity is affected by
changes in the number of aggregate units. Consistent with the general
patterns discussed earlier, the results indicate that the Thomsen esti-
mator performs well even when the number of aggregate units drops to
thirty. These results are available upon request.
18 The index of dissimilarity between the actual and estimated vote
proportions for the hypothetical state is 2.42%.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
200


---

the estimates are remarkable; while draws of ten or twenty
precincts produce noticeable tails in the distribution of the
errors, the estimator recovers the “state's” voting patterns
with limited bias using as few as thirty or ﬁfty precincts.
These results remain robust even if we remove Miami-Dade
Country, demonstrating that its large number of precincts
and the strong performance of the estimator when recov-
ering its individual-level vote proportions (in comparison to
the other counties) do not drive the estimator's perfor-
mance regarding the hypothetical state.
5. Conclusion
Problems of ecological inference have long been of inter-
est to scholars, who have developed a number of approaches
to address them. One method, the Thomsen estimator, is
particularly appealing for scholars of electoral dynamics
given its theoretical foundation. Importantly, the Thomsen
estimator recovers the individual-level behavior quite well
with regards to voter transition rates across elections and
across races withinanelection, generating closer estimates to
the individual results than those found in previous analyses.
This conclusion holds when the population under investiga-
tion is diverse on both demographic and partisan measures
across and within the aggregate-level units. The estimator
also performs well even when the number of aggregate units
is quite small, demonstrating the robustness of the Thomsen
estimator to changes in sample size.
The robustness of the Thomsen estimator to both diverse
and small samples suggests signiﬁcant conﬁdence in its
application to a number of questions in the study of elections.
In addition to general interest in straight- and split-ticket
voting, there are a variety of applications in the realm of
election reform; the study of changes in voting machines,
early voting, absentee voting, and changes in ballot format
(e.g., straight-party device) could all beneﬁt from the imple-
mentation of this statistical technique. The evidence pre-
sented here suggests that scholars can have signiﬁcant
conﬁdence in applyingthe estimator to problemsof ecological
inference, even when the nature of the data is less than ideal.
Acknowledgements
Won-ho Park received support from the National
Research Foundation of Korea Grant funded by the Korean
Government (NRF-2013S1A3A2054311). We would like to
thank Chris Achen, Ernesto Calvo, Mike Traugott, Paul
Herrnson, Dick Niemi, Fred Conrad, Ben Bederson, the
anonymous reviewers, and the editor for helpful discus-
sions and feedback. All errors are our own.
Panel A: Straight-ticket Voting
0
50
100
150
200
0
50
100
150
200
-.12 -.06
0
.06
.12
-.12 -.06
0
.06
.12
-.12 -.06
0
.06
.12
10
20
30
50
100
200
Density
Bias of the Ecological Estimator: Senate (Dem) and Presidential (Gore)
0
50
100
150
200
0
50
100
150
200
-.12
-.06
0
.06
.12
-.12
-.06
0
.06
.12
-.12
-.06
0
.06
.12
10
20
30
50
100
200
Density
Bias of the Ecological Estimator: Senate (Rep) and Presidential (Bush)
Panel B: Split-ticket Voting
0
50
100
150
200
0
50
100
150
200
-.12
-.06
0
.06
.12 -.12
-.06
0
.06
.12 -.12
-.06
0
.06
.12
10
20
30
50
100
200
Density
Bias of the Ecological Estimator: Senate (Dem) and Presidential (Bush)
0
50
100
150
200
0
50
100
150
200
-.12
-.06
0
.06
.12 -.12
-.06
0
.06
.12 -.12
-.06
0
.06
.12
10
20
30
50
100
200
Density
Bias of the Ecological Estimator: Senate (Rep) and Presidential (Gore)
Fig. 4. Bias of the Thomsen estimates by sample size for hypothetical state. Note: Figures show the bias of the estimates in voting for the speciﬁed presidential
and senatorial candidates. Bias is deﬁned as the difference between the ecological estimate of the voting proportion and the actual ballot tabulation (i.e. a bias of
zero means that the estimated and actual proportions are the same). Source: 2000 Florida Ballots Project.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
201


---

Appendix A. Supplementary material
Supplementary data related to this article can be found
at http://dx.doi.org/10.1016/j.electstud.2014.08.006.
Appendix B
References
Abramowitz, A.I., Saunders, K.L., 1998. Ideological realignment in the U.S.
electorate. J. Politics 60 (3), 634e652.
Achen, C.H., 2000. The Thomsen Estimator for Ecological Inference (Un-
published manuscript). University of Michigan.
Achen, C.H., Shivley, P., 1995. Cross-level Inference. University of Chicago
Press, Chicago.
Adolph,
C.,
King,
G.,
2003.
Analyzing
second-stage
ecological
regressions: comment on Herron and Shotts. Polit. Anal. 11 (1),
65e76.
Adolph, C., King, G., Herron, M.C., Shotts, K.W., 2003. A consensus on
second stage analyses in ecological inference models. Polit. Anal. 11
(1), 86e94.
Alesina, A., Rosenthal, H., 1995. Partisan Politics, Divided Government,
and the Economy. Cambridge University Press, New York.
Alexseev, M.A., 2006. Ballot-box vigilantism? Ethnic population shifts
and xenophobic voting in post-Soviet Russia. Polit. Behav. 28 (3),
211e240.
Altman, D., 2002. Popular initiatives in Uruguay: conﬁdence votes on
government or political loyalties? Elect. Stud. 21 (4), 617e630.
Beck, P.A., Baum, L., Clausen, A.R., Smith Jr., C.E., 1992. Patterns and
sources of ticket splitting in subpresidential voting. Am. Polit. Sci. Rev.
86 (4), 916e928.
Belli, R.F., Traugott, M.W., Beckmann, M.N., 2001. What leads to voting
overreports? Contrasts of overreporters to validated voters and
admitted nonvoters in the American national election studies. J. Off.
Statist. 17 (4), 479e498.
Benoit, K., Giannetti, D., Laver, M., 2006. Voter strategies with restricted
choice menus. Br. J. Polit. Sci. 36 (3), 459e485.
Blau, P.M., 1977. Inequality and heterogeneity: a primitive theory of social
structure. Free Press, New York.
Brown, P.J., Payne, C.D., 1986. Aggregate data, ecological regression, and
voting transitions. J. Am. Statist. Assoc. 81 (394), 452e460.
Burden, B.C., 2009. Candidate-driven ticket splitting in the 2000 Japanese
elections. Elect. Stud. 28 (1), 33e40.
Burden, B.C., Kimball, D.C., 1998. A new approach to the study of ticket
splitting. Am. Polit. Sci. Rev. 92 (3), 533e544.
Burden, B.C., Kimball, D.C., 2002. Why Americans Split Their Tickets:
Campaigns, Competition, and Divided Government. University of
Michigan Press, Ann Arbor.
Caltech/MIT Voting Technology Project, 2001. Voting: what Is, what Could
Be.
Calvo, E., Escolar, M., 2003. The local voter: a geographically weighted
approach to ecological inference. Am. J. Polit. Sci. 47 (1), 188e204.
Carsey, T.M., Layman, G.C., 2006. Changing sides or changing minds?
Party identiﬁcation and policy preferences in the American elec-
torate. Am. J. Polit. Sci. 50 (2), 464e477.
Chandra, K., 2009. Why voters in patronage democracies split their
tickets: strategic voting for ethnic parties. Elect. Stud. 28 (1),
21e32.
Cleave, N., Brown, P.J., Payne, C.D., 1995. Evaluation of methods for
ecological inference. J. Roy. Statist. Soc. 158 (1), 55e72.
Deming, W.E., Stephan, F.F., 1940. On a least square adjustment of a
sampled frequency table when the expected marginal tables are
known. Ann. Math. Statist. 11, 427e444.
Duff, B., Hanmer, M.J., Park, W.-h, White, I.K., 2007. Good excuses: un-
derstanding who votes with an improved turnout question. Public
Opin. Q. 71 (1), 67e90.
Elff, M., Gschwend, T., Johnston, R.J., 2008. Ignoramus, ignorabimus? On
uncertainty in ecological inference. Polit. Anal. 16 (1), 70e92.
Fiorina, M.P., 1996. Divided Government, second ed. Allyn and Bacon,
Needham Heights, MA.
Appendix Table A
Total percentage of major party straight-ticket voters using King's EI, Thomsen's estimator, and individual ballot images in Florida Counties, 2000.
County
King's EI
Thomsen estimator
Ballot images
Difference: King  Ballot images
Difference: Thomsen  Ballot images
Broward
90.95%
84.68%
83.91%
7.04%
0.77%
Highlands
86.94%
83.75%
80.37%
6.57%
3.38%
Hillsborough
85.96%
78.17%
79.76%
6.20%
1.59%
Lee
84.26%
83.22%
79.37%
4.89%
3.85%
Marion
86.40%
82.64%
79.93%
6.47%
2.71%
Miami-Dade
84.96%
76.45%
77.78%
7.18%
1.33%
Palm Beach
83.79%
77.28%
76.96%
6.83%
0.32%
Pasco
83.89%
80.95%
77.96%
5.93%
2.99%
Pinellas
87.07%
82.49%
79.42%
7.65%
3.07%
Sarasota
87.23%
82.46%
79.99%
7.24%
2.47%
Note: EI analysis run in R using the ecological inference code integrated into Zelig (Imai et al., 2007a,b), which implements models using a nonlinear least
squares approximation (Wittenberg et al., 2007). In contrast to earlier ecological inference approaches that are Bayesian in nature (see for example Rosen
et al., 2001), this strategy implements a frequentist approximation of these Bayesian models. As such, it is not Bayesian by design and does not require priors
or starting values to be speciﬁed.
Source: 2000 Florida Ballots Project.
Appendix Table B
Index of dissimilarity comparisons for Thomsen's estimator and King's EI
for voting patterns in Florida Counties, 2000.
Thomsen estimator
King's EI
Broward
3.04
8.38
Highlands
5.78
9.36
Hillsborough
3.95
8.71
Lee
6.59
7.58
Marion
5.25
8.15
Miami-Dade
2.72
10.78
Palm Beach
3.50
9.57
Pasco
5.95
7.59
Pinellas
5.67
9.59
Sarasota
5.15
9.44
Note: Index of dissimilarity is the measurement of the difference between
the two transition matrices, deﬁned as the total sum of absolute de-
viations divided by two. EI analysis run in R using the ecological inference
code integrated into Zelig (Imai et al., 2007a,b), which implements models
using a nonlinear least squares approximation (Wittenberg et al., 2007). In
contrast to earlier ecological inference approaches that are Bayesian in
nature (see for example Rosen et al., 2001), this strategy implements a
frequentist approximation of these Bayesian models. As such, it is not
Bayesian by design and does not require priors or starting values to be
speciﬁed.
Source: 2000 Florida Ballots Project.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
202


---

Golder, M., 2003. Explaining variation in the success of extreme right
parties in Western Europe. Comp. Polit. Stud. 36 (4), 432e466.
Goodman, L.A., 1953. Ecological regression and the behavior of in-
dividuals. Am. Sociol. Rev. 18 (6), 663e664.
Goodman, L.A., 1959. Some alternatives to ecological correlation. Am. J.
Sociol. 646, 610e625.
Greiner, D.J., Quinn, K.M., 2009. R  C ecological inference: bounds, cor-
relations, ﬂexibility, and transparency of assumptions. J. Roy. Statist.
Soc. Ser. A 172 (1), 67e81.
Hanmer, M.J., Traugott, M.W., 2004. The impact of voting by mail on voter
behavior. Am. Polit. Res. 32 (4), 375e405.
Hanmer, M.J., Park, W.-H., Traugott, M.W., Niemi, R.G., Herrnson, P.S.,
Bederson, B.B., Conrad, F.G., 2010. Losing fewer votes: The impact of
changing voting systems on residual votes. Polit. Res. Q. 63 (1),
129e142.
Hanushek, E.A., Jackson, J.E., Kain, J.F., 1974. Model speciﬁcation, use of
aggregate data, and the ecological correlation fallacy. Polit. Methodol.
1, 89e107.
Herrnson, P., Niemi, R.G., Hanmer, M.J., Bederson, B.B., Conrad, F.C.,
Traugott, M.W., 2008. Voting Technology: the Not-so-simple Act of
Casting a Ballot. Brookings, Washington, DC.
Herron, M.C., Shotts, K.W., 2003a. Cross-contamination in EI-R. Polit. Anal.
11 (1), 77e85.
Herron, M.C., Shotts, K.W., 2003b. Using ecological inference point esti-
mates as dependent variables in second stage linear regressions. Polit.
Anal. 11 (1), 44e64.
Herron, M.C., Shotts, K.W., 2004. Logical inconsistency in EI-based second
stage regressions. Am. J. Polit. Sci. 48 (1), 172e183.
Imai, K., King, G., Lau, O., 2007a. Zelig: Everyone's Statistical Software.
URL: http://GKing.harvard.edu/zelig.
Imai, K., King, G., Lau, O., 2007b. Toward a Common Framework for Sta-
tistical Analysis and Development. URL: http://gking.harvard.edu/
ﬁles/abs/z-abs.shtml.
Jacobson, G.C., 1990. The Electoral Origins of Divided Government.
Westview, Boulder, CO.
Jacobson, G.C., 2000. Party polarization in national politics: the electoral
connection. In: Bond, J.R., Fleisher, R. (Eds.), Polarized Politics:
Congress and the President in a Partisan Era. Congressional Quarterly
Press, Washington, pp. 9e30.
Johnston,
R.,
Pattie,
C.,
2000.
Ecological
inference
and
entropy-
maximizing: an alternative estimation procedure for split-ticket
voting. Polit. Anal. 8 (4), 333e345.
King, G., 1997. A Solution to the Ecological Inference Problem: Recon-
structing Individual Behavior from Aggregate Data. Princeton Uni-
versity Press, Princeton, NJ.
Kopstein, J.S., Wittenberg, J., 2009. Does familiarity breed contempt?
Inter-ethnic contact and support for illiberal parties. J. Politics 71 (2),
414e428.
Layman, G.C., Carsey, T.M., 2002. Party polarization and ‘Conﬂict exten-
sion’ in the American electorate. Am. J. Polit. Sci. 46 (4), 786e802.
Lewis-Beck, M.S., Nadeau, R., 2004. Split-ticket voting: the effects of
cognitive madisonianism. J. Politics 66 (1), 97e112.
Park, W.-H., 2008a. Ecological Inference and Aggregate Analysis of Elec-
tions. The University of Michigan Doctoral Dissertation.
Park, W.-H., 2008b. Ecological Inference with Covariates: Voter Transition
in Different Groups in South Korea. Paper presented at The Society for
Political Methodology Annual Summer Conference. University of
Michigan, July 9e12.
Park, W.-H., 2013. Saengtaehakjuk churon seosul [A preface to ecological
inference: new hopes in old alchemy]. Peace Stud. 21 (2), 395e426.
Roscoe, D.D., 2003. The choosers or the choices? Voter characteristics and
the structure of electoral competition as explanations for ticket
splitting. J. Politics 65 (4), 1147e1164.
Rosen, O., Jiang, W., King, G., Tanner, M., 2001. Bayesian and frequentist
inference for ecological inference: the R  C case. Stat. Neerl. 55 (2),
134e156.
Tam Cho, W.K., 1998. If the assumption ﬁts... : a comment on the King
ecological inference solution. Polit. Anal. 7 (1), 143e163.
Tam Cho, W.K., Gaines, B.J., 2004. The limits of ecological inference: the
case of split-ticket voting. Am. J. Polit. Sci. 48 (1), 152e171.
Thomsen, S.R., 1987. Danish Elections 1920e79: a Logit Approach to
Ecological Analysis and Inference. Politica, Aarhus, Denmark.
Thomsen, S.R., 2000. Issue Voting and Ecological Inference (Unpublished
manuscript). Aarhus University, Aarhus, Denmark.
Thomsen, S.R., Berglund, S., Worlund, I., 1991. Assessing the validity of
the logit method for ecological inference. Eur. J. Polit. Res. 19 (4),
441e477.
Wakeﬁeld, J., 2004. Ecological inference for 2  2 tables. J. Roy. Statist.
Soc. Ser. A 167 (3), 385e445.
Wand, J.N., Shotts, K.W., Sekhon, J.S., Mebane Jr., W.R., Herron, M.C.,
Brady, H.E., 2001. The butterﬂy did it: the aberrant vote for
Buchanan in Palm Beach county, Florida. Am. Polit. Sci. Rev. 95 (4),
793e810.
Wittenberg, J., Alimadhi, F., Lau, O., 2007. ei.R  C: hierarchical
multinomial-Dirichlet
ecological
inference
model.
In:
Imai,
K.,
King, G., Lau, O. (Eds.), Zelig: Everyone's Statistical Software. URL:
http://gking.harvard.edu/zelig.
W.-h. Park et al. / Electoral Studies 36 (2014) 192e203
203
