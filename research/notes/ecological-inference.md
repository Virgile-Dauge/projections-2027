---
title: Ecological Inference
id: ecological-inference
tags:
- inference-ecologique
- king-ei
- ei-methodologie
- reference-canonique
created: '2026-07-21T18:33:20.433771Z'
updated: '2026-07-21T18:39:17.768989Z'
source: https://gking.harvard.edu/files/eiintro.pdf
source_domain: gking.harvard.edu
fetched_at: '2026-07-21T18:33:20.433499Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Introduction chapter to King, Rosen & Tanner (eds.), ''Ecological Inference:
  New Methodological Strategies'' (Cambridge University Press, 2004) — the canonical
  edited volume that consolidated post-King(1997) EI methodology, with 16 chapters
  covering priors/likelihood choice (Wakefield), spatial EI (Calvo & Escolar; Haneuse
  & Wakefield), temporal/panel EI (Quinn; Pelzer et al.), multi-election MCMC extensions
  (Lewis), and numerical-properties comparisons (Altman, Gill & McDonald). The introduction
  explains King''s (1997) core methodological device — the tomography line/plot, derived
  from the Duncan-Davis (1953) deterministic bounds combined with a truncated bivariate
  normal density over precinct-level parameters — as the mechanism by which King''s
  method extracts probabilistic information beyond simple bounds, and surveys how
  EI is used to test Voting Rights Act redistricting claims and reconstruct historical
  individual behavior (e.g. Nazi-party voting in Weimar Germany) where survey data
  cannot exist.'
raw_file: raw/ecological-inference.pdf
---

*Suggested by [[abstract-europe-pmc]] — Gary King's canonical EI methodology intro, cited across the batch*

Ecological Inference
New Methodological Strategies
Edited by
Gary King
Harvard University
Ori Rosen
University of Pittsburgh
Martin A. Tanner
Northwestern University


---

PUBLISHED BY THE PRESS SYNDICATE OF THE UNIVERSITY OF CAMBRIDGE
The Pitt Building, Trumpington Street, Cambridge, United Kingdom
CAMBRIDGE UNIVERSITY PRESS
The Edinburgh Building, Cambridge CB2 2RU, UK
40 West 20th Street, New York, NY 10011-4211, USA
477 Williamstown Road, Port Melbourne, VIC 3207, Australia
Ruiz de Alarc´on 13, 28014 Madrid, Spain
Dock House, The Waterfront, Cape Town 8001, South Africa
http://www.cambridge.org
C⃝Cambridge University Press 2004
This book is in copyright. Subject to statutory exception
and to the provisions of relevant collective licensing agreements,
no reproduction of any part may take place without
the written permission of Cambridge University Press.
First published 2004
Printed in the United States of America
Typefaces Minion 10/12 pt., Helvetica Neue Condensed, and Lucida Typewriter
System LATEX 2ε
[TB]
A catalog record for this book is available from the British Library.
Library of Congress Cataloging in Publication Data
Ecological inference : new methodological strategies / edited by Gary King, Matrin A.
Tanner, Ori Rosen.
p.
cm.
Includes bibliographical references (p. ).
ISBN 0-521-83513-5 – ISBN 0-521-54280-4 (pbk.)
1. Social sciences – Statistical methods.
2. Political statistics.
3. Inference.
I. King, Gary.
II. Tanner, Martin Abba, 1957–
III. Rosen, Ori.
HA29.E27
2004
330′.72′7 – dc22
2004045500
ISBN 0 521 83513 5 hardback
ISBN 0 521 54280 4 paperback


---

Contents
Contributors
page vii
Preface
ix
INTRODUCTION
1
Information in Ecological Inference: An Introduction
1
Gary King, Ori Rosen, and Martin A. Tanner
PART ONE
13
1
Prior and Likelihood Choices in the Analysis of Ecological Data
13
Jonathan Wakeﬁeld
2
The Information in Aggregate Data
51
David G. Steel, Eric J. Beh, and Ray L. Chambers
3
Using Ecological Inference for Contextual Research
69
D. Stephen Voss
PART TWO
97
4
Extending King’s Ecological Inference Model to Multiple Elections Using
Markov Chain Monte Carlo
97
Jeffrey B. Lewis
5
Ecological Regression and Ecological Inference
123
Bernard Grofman and Samuel Merrill
6
Using Prior Information to Aid Ecological Inference: A Bayesian Approach
144
J. Kevin Corder and Christina Wolbrecht
7
An Information Theoretic Approach to Ecological Estimation and Inference
162
George G. Judge, Douglas J. Miller, and Wendy K. Tam Cho
8
Ecological Panel Inference from Repeated Cross Sections
188
Ben Pelzer, Rob Eisinga, and Philip Hans Franses
PART THREE
207
9
Ecological Inference in the Presence of Temporal Dependence
207
Kevin M. Quinn
10
A Spatial View of the Ecological Inference Problem
233
Carol A. Gotway Crawford and Linda J. Young
v


---

vi
Contents
11
Places and Relationships in Ecological Inference
245
Ernesto Calvo and Marcelo Escolar
12
Ecological Inference Incorporating Spatial Dependence
266
Sebastien Haneuse and Jonathan Wakeﬁeld
PART FOUR
303
13
Common Framework for Ecological Inference in Epidemiology, Political
Science, and Sociology
303
Ruth Salway and Jonathan Wakeﬁeld
14
MultipartySplit-TicketVotingEstimationasanEcologicalInferenceProblem
333
Kenneth Benoit, Michael Laver, and Daniela Giannetti
15
A Structured Comparison of the Goodman Regression, the Truncated
Normal, and the Binomial–Beta Hierarchical Methods for Ecological
Inference
351
Rog´erio Silva de Mattos and ´Alvaro Veiga
16
A Comparison of the Numerical Properties of EI Methods
383
Micah Altman, Jeff Gill, and Michael P. McDonald
Index
409


---

INTRODUCTION
Information in Ecological Inference: An Introduction
Gary King, Ori Rosen, and Martin A. Tanner
Researchers in a diverse variety of ﬁelds often need to know about individual-level behavior
and are not able to collect it directly. In these situations, where survey research or other
means of individual-level data collection are infeasible, ecological inference is the best and
often the only hope of making progress. Ecological inference is the process of extracting
clues about individual behavior from information reported at the group or aggregate level.
For example, sociologists and historians try to learn who voted for the Nazi party in
Weimar Germany, where thoughts of survey research are seven decades too late. Market-
ing researchers study the effects of advertising on the purchasing behavior of individuals,
where only zip-code-level purchasing and demographic information are available. Political
scientists and politicians study precinct-level electoral data and U.S. Census demographic
data to learn about the success of candidate appeals with different voter groups in numerous
small areal units where surveys have been infeasible (for cost or conﬁdentiality reasons). To
determine whether the U.S. Voting Rights Act can be applied in redistricting cases, expert
witnesses, attorneys, judges, and government ofﬁcials must infer whether African Ameri-
cans and other minority groups vote differently from whites, even though the secret ballot
hinders the process and surveys in racially polarized contexts are known to be of little
value.
In these and numerous other ﬁelds of inquiry, scholars have no choice but to make
ecological inferences. Fortunately for them, we have witnessed an explosion of statistical
research into this problem in the last ﬁve years – both in substantive applications and in
methodological innovations. In applications, the methods introduced by Duncan and Davis
(1953) and by Goodman (1953) accounted for almost every use of ecological inference in
any ﬁeld for ﬁfty years, but this stasis changed when King (1997) offered a model that
combined and extended the approaches taken in these earlier works. His method now seems
to dominate substantive research in academia, in private industry, and in voting rights
litigation, where it was used in most American states in the redistricting period that followed
the 2000 Census. The number and diversity of substantive application areas of ecological
inference has soared recently as well. The speed of development of statistical research on
ecological inference has paralleled the progress in applications, too, and in the last ﬁve years
we have seen numerous new models, innovative methods, and novel computation schemes.
This book offers a snapshot of some of the research at the cutting edge of this ﬁeld in the
hope of spurring statistical researchers to push out the frontiers and applied researchers to
choose from a wider range of approaches.
Ecological inference is an especially difﬁcult special case of statistical inference. The difﬁ-
cultycomesbecausesomeinformationisgenerallylostintheprocessofaggregation,andthat
information is sometimes systematically related to the quantities of interest. Thus, progress
1


---

2
Gary King, Ori Rosen, and Martin A. Tanner
in this ﬁeld has usually come from discovering new sources of information or inventing
better ways of harvesting existing information and using it to improve our inferences about
individual-level behavior. This book is organized around these sources of information and
methods for their extraction. We begin this overview chapter in Section 0.1 by very brieﬂy
summarizing some relevant prior research, on which the authors in this volume build. This
section also serves to introduce the notation used, when convenient, in the rest of the book.
Section 0.2 then summarizes the subsequent chapters.
0.1 NOTATION AND BACKGROUND
0.1.1 The Ecological Inference Problem
For expository purposes, we discuss only an important but simple special case of ecological
inference, and adopt the running example and notation from King (1997: Chapter 2).
The basic problem has two observed variables (Ti and Xi) and two unobserved quantities of
interest(βb
i andβw
i )foreachof p observations.Observationsrepresentaggregateunits,such
as geographical areas, and each individual-level variable within these units is dichotomous.
Tobemorespeciﬁc,inTable0.1,weobserveforeachelectoralprecincti (i = 1, . . . , p)the
fractions of voting age people who turn out to vote (Ti) and who are black (Xi), along with
the number of voting age people (Ni). The quantities of interest, which remain unobserved
because of the secret ballot, are the proportions of blacks who vote (βb
i ) and whites who vote
(βw
i ). The proportions βb
i and βw
i are not observed because Ti and Xi are from different
data sources (electoral results and census data, respectively) and record linkage is impossible
(and illegal), and so the cross-tabulation cannot be computed.
Also of interest are the district-wide fractions of blacks and whites who vote, which are
respectively
Bb =
p
i=1 Ni Xiβb
i
p
i=1 Ni Xi
(0.1)
and
Bw =
p
i=1 Ni(1 −Xi)βw
i
p
i=1 Ni(1 −Xi) .
(0.2)
These are weighted averages of the corresponding precinct-level quantities. Some methods
aim to estimate only Bb and Bw without giving estimates of βb
i and βw
i for all i.
0.1.2 Deterministic and Statistical Approaches
The ecological inference literature before King (1997) was bifurcated between supporters of
the method of bounds, originally proposed by Duncan and Davis (1953), and supporters of
statistical approaches, proposed even before Ogburn and Goltra (1919), but ﬁrst formalized
into a coherent statistical model by Goodman (1953, 1959).1 Although Goodman and
1 For the historians of science among us: despite the fact that these two monumental articles were written by two
colleagues and friends in the same year and in the same department and university (the Department of Sociology
at the University of Chicago), the principals did not discuss their work prior to completion. Even judging by
today’s standards, nearly a half-century after their publication, the articles are models of clarity and creativity.


---

Information in Ecological Inference: An Introduction
3
Table 0.1 Notation for precinct i
Voting decision
Race of voting
age person
Vote
No vote
Black
βb
i
1 −βb
i
X i
White
βw
i
1 −βw
i
1 −X i
Ti
1 −Ti
Note: The goal is to estimate the quantities of
interest, βb
i (the fraction of blacks who vote) and
βw
i
(the fraction of whites who vote), from the
aggregate variables X i (the fraction of voting age
peoplewhoareblack)and Ti (thefractionofpeople
who vote), along with N i (the known number of
voting age people).
Duncan and Davis moved on to other interests following their seminal contributions, most
of the ecological inference literature in the ﬁve decades since 1953 was an ongoing war
betweensupportersofthesetwokeyapproaches,oftenwithouttheusualacademicdecorum.
0.1.2.1 Extracting Deterministic Information: The Method of Bounds
The purpose of the method of bounds and its generalizations is to extract deterministic
information, known with certainty, about the quantities of interest.
The intuition behind these quantities is simple. For example, if a precinct contained 150
African-Americans and 87 people in the precinct voted, then how many of the 150 African-
Americans actually cast their ballot? We do not know exactly, but bounds on the answer are
easy to obtain: in this case, the answer must lie between 0 and 87. Indeed, conditional only on
the data being correct, [0, 87] is a 100% conﬁdence interval. Intervals like this are sometimes
narrow enough to provide meaningful inferences, and sometimes they are too wide, but the
ability to provide (nontrivial) 100% conﬁdence intervals in even some situations is quite
rare in any statistical ﬁeld.
In general, before seeing any data, the unknown parameters βb
i and βw
i are each bounded
on the unit interval. Once we observe Ti and Xi, they are bounded more narrowly, as
βb
i ∈

max

0, Ti −(1 −Xi)
Xi

, min
 Ti
Xi
, 1

,
βw
i ∈

max

0, Ti −Xi
1 −Xi

, min

Ti
1 −Xi
, 1

.
(0.3)
Deterministic bounds on the district-level quantities Bb and Bw are weighted averages of
these precinct-level bounds.
These expressions indicate that the parameters in each case fall within these deterministic
bounds with certainty, and in practice they are almost always narrower than [0, 1]. Whether
they are narrow enough in any one application depends on the nature of the data.


---

4
Gary King, Ori Rosen, and Martin A. Tanner
0.1.2.2 Extracting Statistical Information: Goodman’s Regression
Leo Goodman’s (1953, 1959) approach is very different from Duncan and Davis’s. He looked
at the same data and focused on the statistical information. His approach examines variation
in the marginals (Xi and Ti) over the precincts to attempt to reason back to the district-wide
fractions of blacks and whites who vote, Bb and Bw. The outlines of this approach, and the
problems with it, have been known at least since Ogburn and Goltra (1919). For example,
if in precincts with large proportions of black citizens we observe that many people do not
vote, then it may seem reasonable to infer that blacks turn out at rates lower than whites.
Indeed it often is reasonable, but not always. The problem is that it could instead be the
case that the whites who happen to live in heavily black precincts are the ones who vote
less frequently, yielding the opposite ecological inference with respect to the individual-level
truth.
What Goodman accomplished was to formalize the logic of the approach in a simple
regression model, and to give the conditions under which estimates from such a model are
unbiased. To see this, note ﬁrst that the accounting identity
Ti = Xiβb
i + (1 −Xi)βw
i
(0.4)
holds exactly. Goodman showed that a regression of Ti on Xi and 1 −Xi with no constant
term could be used to estimate Bb and Bw, respectively. The key assumption necessary
for unbiasedness that Goodman identiﬁed is that the parameters and Xi are uncorrelated:
Cov(βb
i , Xi) = Cov(βw
i , Xi) = 0. In the example, the assumption is that blacks vote in the
same proportions in homogeneously black areas as in more integrated areas.2 Obviously,
this is true sometimes and it is false at other times.
As Goodman recognized, when this key assumption does not hold, estimates from the
model will be biased. Indeed, they can be very biased, outside the deterministic bounds,
and even outside the unit interval. Goodman’s technique has been used extensively in the
last half-century, and impossible estimates occur with considerable frequency (some say in
a majority of real applications; see Achen and Shively, 1995).
0.1.3 Extracting Both Deterministic and Statistical Information: King’s EI Approach
From 1953 until 1997, the only two approaches used widely in practice were the method of
bounds and Goodman’s regression. King’s (1997) idea was that the insights from these two
conﬂicting literatures in fact do not conﬂict with each other; the sources of information are
largely distinct and can be combined to improve inference overall and synergistically. The
idea is to combine the information from the bounds, applied to both quantities of interest
for each and every precinct, with a statistical approach for extracting information within
the bounds. The amount of information in the bounds depends on the data set, but for
many data sets it can be considerable. For example, if precincts are spread uniformly over
a scatterplot of Xi by Ti, the average bounds on βb
i and βw
i are narrowed from [0, 1] to
less than half of that range – hence eliminating half of the ecological inference problem
with certainty. This additional information also helps make the statistical portion of the
model far less sensitive to assumptions than previous statistical methods that exclude the
information from the bounds.
To illustrate these points, we ﬁrst present all the information available without making any
assumptions, thus extending the bounds approach as far as possible. As a starting point, the
2 King (1997: Chapter 3) showed that Goodman’s assumption was necessary but not sufﬁcient. To have unbiased-
ness, it must also be true that the parameters and Ni are uncorrelated.


---

Information in Ecological Inference: An Introduction
5
•
••
••
••
•
•
•
•
•
• •
••
•
•
•
•
•
••
•
•
••
•
•
•
•
•
•••
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
• •
•
•
••
•
•••
•
•
••
•
•
••
•
•
••
••••••••
•
•
••
•
•
••
•
•
•
•
•
•
•
•
•
••
•
•
•
•
•
•
••
••
•
•••
•
••
••
••••
••
•••••
•••
•
••
•••
•••
••••••••
•
•
•
•
•
•••
••
••••
•
•
•
•
•
•
•
•••
•
••
•
•
•••
•••
•
••
•••••
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•••
•
•
•
•
•
•
•
•
0
.25
.5
.75
1
Xi
0
.25
.75
1
.5
0
.25
.5
.75
1
0
.25
.5
.75
1
βb
i
(a)
(b)
βw
i
Ti 
Figure 0.1. Two views of the same data: (a) a scatterplot of the observables, Xi by Ti; (b) this same
information as a tomography plot of the quantities of interest, βb
i by βw
i . Each precinct i that appears
as a point in (a) appears instead as a line (because of information lost due to aggregation) in (b). For
example, precinct 52 appears as the dot with a little square around it in (a), and as the dark line in (b).
The data are from King (1997: Figures 5.1, 5.5).
graph in Figure 0.1a provides a scatterplot of a sample data set as observed, Xi horizontally
by Ti vertically. Each point in this plot corresponds to one precinct, for which we would like
to estimate the two unknowns. We display the unknowns in part (b) of the same ﬁgure; any
point in that graph portrays values of the two unknowns, βb
i (plotted horizontally) and βw
i
(vertically). Ecological inference involves locating, for each precinct, the one point in this
unit square corresponding to the true values of βb
i and βw
i , since values outside the square
are logically impossible.
To map the knowns onto the unknowns, King began with Goodman’s accounting identity
from Equation 0.4. From this equation, which holds exactly, we solve for one unknown in
terms of the other:
βw
i =

Ti
1 −Xi

−

Xi
1 −Xi

βb
i ,
(0.5)
which shows that βw
i is a linear function of βb
i , where the intercept and slope are known
(since they are functions of the data, Xi and Ti).
King then maps the knowns from Figure 0.1a onto Figure 0.1b by using the linear re-
lationship in Equation 0.5. A key point is that each dot in (a) can be expressed, without
assumptions or loss of information, as what King called a “tomography” line within the unit
square in (b).3 It is precisely the information lost due to aggregation that causes us to have
to plot an entire line (on which the true point must fall) rather than the goal of one point
for each precinct in Figure 0.1b. In fact, the information lost is equivalent to having a graph
of the (βb
i , βw
i ) points but having the ink smear, making the points into lines and partly but
not entirely obscuring the correct positions of the points.
3 King also showed that the ecological inference problem is mathematically equivalent to the ill-posed “tomog-
raphy” problem of many medical imaging procedures (such as CAT and PET scans), where one attempts to
reconstruct the inside of an object by passing X-rays through it and gathering information only from the out-
side. Because the line sketched out by an X-ray is closely analogous to Equation 0.5, King called the latter a
tomography line and the corresponding graph a tomography graph.


---

6
Gary King, Ori Rosen, and Martin A. Tanner
What does a tomography line tell us? Before we know anything, we know that the true
(βb
i , βw
i ) point must lie somewhere within the unit square. After Xi and Ti are observed for a
precinct, we also know that the true point must fall on a speciﬁc line represented by Equation
0.5 and appearing in the tomography plot in Figure 0.1. In many cases narrowing the region
to be searched for the true point from the entire square to the one line in the square can
provide a signiﬁcant amount of information. To see this, consider the point enclosed in a
box in Figure 0.1a, and the corresponding dark line in Figure 0.1b. This precinct, number 52,
has observed values of X52 = 0.88 and T52 = 0.19. As a result, substituting into Equation
0.5 gives βw
i = 1.58 −7.33βb
i , which when plotted then appears as the dark line in (b).
This particular line tells us that in our search for the true (βb
52, βw
52) point in (b), we can
eliminate with certainty all area in the unit square except that on the line, which is clearly
an advance over not having the data. Translated into the quantities of interest, this line tells
us (by projecting it downward to the horizontal axis) that wherever the true point falls on
the line, βb
52 must fall in the relatively narrow bounds of [0.07, 0.21]. Unfortunately, in this
case, βw
i can only be bounded (by projecting to the left) to somewhere within the entire
unit interval. More generally, lines that are relatively steep, like this one, tell us a great deal
about βb
i and little about βw
i . Tomography lines that are relatively ﬂat give narrow bounds
on βw
i and wide bounds on βb
i . Lines that cut off the bottom left (or top right) of the ﬁgure
give narrow bounds on both quantities of interest.
If the only information available to learn about the unknowns in precinct i is Xi and Ti,
a tomography line like that in Figure 0.1 exhausts all this available information. This line
immediately tells us the known bounds on each of the parameters, along with the precise
relationship between the two unknowns, but it is not sufﬁcient to narrow in on the right
answer any further. Fortunately, additional information exists in the other observations in
the same data set (X j and Tj for all i ̸= j), which, under the right assumptions, can be used
to learn more about βb
i and βw
i in our precinct of interest.
In order to borrow statistical strength from all the precincts to learn about βb
i and βw
i in
precinct i, some assumptions are necessary. The simplest version (i.e., the one most useful
for expository purposes) of King’s model requires three assumptions, each of which can be
relaxed in different ways.
First, the set of (βb
i , βw
i ) points must fall in a single cluster within the unit square. The
cluster can fall anywhere within the square; it can be widely or narrowly dispersed or highly
variable in one unknown and narrow in the other; and the two unknowns can be positively,
negatively, or not at all correlated over i. An example that would violate this assumption
would be two or more distinct clusters of (βb
i , βw
i ) points, as might result from subsets of
observationswithfundamentallydifferentdatagenerationprocesses(suchasfrommarkedly
different regions). The speciﬁc mathematical version of this one-cluster assumption is that
βb
i and βw
i follow a truncated bivariate normal density
TN(βb
i , βw
i | ˘B, ˘) = N(βb
i , βw
i | ˘B, ˘)1(βb
i , βw
i )
R( ˘B, ˘)
,
(0.6)
where the kernel is the untruncated bivariate normal,
N(βb
i , βw
i | ˘B, ˘) = (2π)−1| ˘|−1/2 exp

−1
2(βi −˘B)′ ˘−1(βi −˘B)

,
(0.7)
and 1(βb
i , βw
i ) is an indicator function that equals one if βb
i ∈[0, 1] and βw
i ∈[0, 1] and
zero otherwise. The normalization factor in the denominator, R( ˘B, ˘), is the volume under


---

Information in Ecological Inference: An Introduction
7
the untruncated normal distribution above the unit square:
R( ˘B, ˘) =
 1
0
 1
0
N(βb, βw| ˘B, ˘) dβbdβw.
(0.8)
Whendividedintotheuntruncatednormal,thisfactorkeepsthevolumeunderthetruncated
distribution equal to one. The parameters of the truncated density, which we summarize as
˘ψ = { ˘Bb, ˘Bw, ˘σb, ˘σw, ˘ρ} = { ˘B, ˘},
(0.9)
are on the scale of the untruncated normal (and so, for example, ˘Bb and ˘Bw need not be
constrained to the unit interval even though βb
i and βw
i are constrained by this density).
The second assumption, which is necessary to form the likelihood function, is the absence
of spatial autocorrelation: conditional on Xi, Ti and Tj are mean-independent. Violations
of this assumption in empirically reasonable (and even some unreasonable) ways do not
seem to induce much bias.
The ﬁnal, and by far the most critical, assumption is that Xi is independent of βb
i and
βw
i . The three assumptions together produce what has come to be known as the basic EI
model.4 King also generalizes this assumption, in what has come to be known as the extended
EI model, by allowing the truncated normal parameters to vary as functions of measured
covariates, Zb
i and Zw
i , giving
˘Bb
i =

φ1( ˘σ 2
b + 0.25) + 0.5
	
+ (Zb
i −¯Zb)αb,
˘Bw
i =

φ2( ˘σ 2
w + 0.25) + 0.5
	
+ (Zw
i −¯Zw)αw,
(0.10)
where αb and αw are parameter vectors to be estimated along with the original model
parameters and that have as many elements as Zb
i and Zw
i have columns. This relaxes the
mean independence assumptions to
E(βb
i |Xi, Zi) = E(βb
i |Zi),
E(βw
i |Xi, Zi) = E(βw
i |Zi).
Note that this extended model also relaxes the assumptions of truncated bivariate normality,
sincethereisnowaseparatedensitybeingassumedforeachobservation.Becausethebounds,
which differ in width and information content for each i, generally provide substantial
information, even Xi can be used as a covariate in Zi. (The recommended default setting in
EI includes Xi as a covariate with a prior on its coefﬁcient.) In contrast, under Goodman’s
regression, which does not include information in the bounds, including Xi leads to an
unidentiﬁed model (King, 1997: Section 3.2).
Thesethreeassumptions–onecluster,nospatialautocorrelation,andmeanindependence
betweentheregressorandtheunknownsconditionalon Xi and Zi –enableonetocomputea
posterior (or sampling) distribution of the two unknowns in each precinct. A fundamentally
important component of EI is that the quantities of interest are not the parameters of the
likelihood, but instead come from conditioning on Ti and producing a posterior for βb
i
and βw
i in each precinct. Failing to condition on Ti and examining the parameters of the
truncated bivariate normal only makes sense if the model holds exactly and so is much more
4 The use of EI to name this method comes from the name of his software, available at http://GKing.
Harvard.edu.


---

8
Gary King, Ori Rosen, and Martin A. Tanner
model-dependent than King’s approach. Since the most important problem in ecological
inference modeling is precisely model misspeciﬁcation, failing to condition on T assumes
away the problem without justiﬁcation. This point is widely regarded as a critical step in
applying the EI model (Adolph and King, with Herron and Shotts, 2003).
When bounds are narrow, EI model assumptions do not matter much. But for precincts
with wide bounds on a quantity of interest, inferences can become model-dependent. This
is especially the case in ecological inference problems, precisely because of the loss of infor-
mation due to aggregation. In fact, this loss of information can be expressed by noting that
the joint distribution of βb
i and βw
i cannot be fully identiﬁed from the data without some
untestable assumptions. To be precise, distributions with positive mass over any curve or
combination of curves that connects the bottom left point (βb
i = 0, βw
i = 0) to the top right
point (βb
i = 1, βw
i = 1) of a tomography plot cannot be rejected by the data (King, 1997:
191). Other features of the distribution are estimable. This fundamental indeterminacy is of
course a problem, because it prevents pinning down the quantities of interest with certainty;
but it can also be something of an opportunity, because different distributional assumptions
can lead to the same estimates, especially in that only those pieces of the distributions above
the tomography lines are used in the ﬁnal analysis.
0.1.4 King, Rosen, and Tanner’s Hierarchical Model
Inthecontinuingsearchformoreinformationtobringtobearonecologicalinferences,King,
Rosen, and Tanner (1999) extend King’s (1997) model another step. They incorporate King’s
main advance of combining deterministic and statistical information, but begin modeling
a step earlier, at the individuals who make up the counts. They also build a hierarchical
Bayesian model, using easily generalizable Markov chain Monte Carlo (MCMC) technology
(Tanner, 1996).
To deﬁne the model formally, let T′
i denote the number of voting age people who turn out
to vote. At the top level of the hierarchy they assume that T′
i follows a binomial distribution
with probability equal to θi = Xiβb
i + (1 −Xi)βw
i and count Ni. Note that at this level it
is assumed that the expectation of T′
i , rather than T′
i itself, is equal to Xiβb
i + (1 −Xi)βw
i .
In other words, King (1997) models Ti as a continuous proportion, whereas King, Rosen,
and Tanner (1996) recognize the inherently discrete nature of the counts of voters that go
into computing this proportion. The two models are connected, of course, since T′
i /Ni
approaches θi as Ni gets large.
The connection with King’s tomography line can be seen in the contribution of the data
from precinct i to the likelihood, which is

Xiβb
i + (1 −Xi)βw
i
T′
i 
1 −Xiβb
i −(1 −Xi)βw
i
Ni−T′
i .
(0.11)
Bytakingthelogarithmofthiscontributiontothelikelihoodanddifferentiatingwithrespect
to βb
i and βw
i , King, Rosen, and Tanner show that the maximum of Equation 0.11 is not a
unique point, but rather a line whose equation is given by the tomography line in Equation
0.5. Thus, the log likelihood for precinct i looks like two playing cards leaning against each
other. As long as Ti is ﬁxed and bounded away from 0.5 (and Xi is a ﬁxed known value
between 0 and 1), the derivative at this point is seen to increase with Ni, i.e., the pitch
of the playing cards increases with the sample size. In other words, for large Ni, the log
likelihood for precinct i degenerates from a surface deﬁned over the unit square into a single
playingcardstandingperpendiculartotheunitsquareandorientedalongthecorresponding
tomography line.


---

Information in Ecological Inference: An Introduction
9
At the second level of the hierarchical model, βb
i is distributed as a beta density with
parameters cb and db, and βw
i follows an independent beta with parameters cw and dw.
While βb
i and βw
i are assumed a priori independent, they are a posteriori dependent. At the
third and ﬁnal level of the hierarchical model, the unknown parameters cb, db, cw, and dw
follow an exponential distribution with a large mean.
A key advantage of this model is that it generalizes immediately to arbitrarily large R × C
tables. This approach was pursued by Rosen, Jiang, King, and Tanner (2001), who also
provided a much faster method-of-moments-based estimator. For an application, see King,
Rosen, Tanner, and Wagner (2003).
0.2 NEW SOURCES OF INFORMATION IN ECOLOGICAL INFERENCE
We did not attempt to impose an ex ante structure on the authors as they were writing, and
do not pretend that all the chapters ﬁt into neatly delineated categories. This book is only
intended to be a snapshot of a fast-growing ﬁeld. If you are looking for a textbook, check
back in a few years when we have learned more!
Nevertheless, we did need to order the chapters in some way. Our choice was to sort them
according to the new sources of information they bring to bear on the ecological inference
problem. Thus, Part One offers some alternative baselines that help indicate how much
information is lost due to aggregation, and precisely what information is left. For example,
in Chapter 1, Jon Wakeﬁeld offers a “baseline model,” which attempts to make minimal
assumptions about individuals and then aggregate up. Remarkably, the likelihood for this
model is not ﬂat over the tomography line, even without priors. Similarly, in Chapter
2, Steel, Beh, and Chambers provide a means of formally quantifying the information
lost in the aggregation process and thus precisely how much information is left in the
aggregate data. They do this through parametric models and hypothesis tests, such as a test
for the homogeneity of βb
i and βw
i across tables. The authors also show how the increase of
even a small amount of information in a standard ecological inference model can greatly
improve inferences, even if survey respondents cannot be grouped into precincts or relevant
geographic areas. They illustrate their ideas with data from the 1996 Australian census.
And ﬁnally, in Chapter 3, Stephen Voss shows how the most commonly used method, King’s
ecologicalinferencemodel,providesabaselineforunderstandingandparsingoutcontextual
and compositional effects intertwined in aggregate data.
Part Two of this book is devoted to including sources of information through new models
and methods. In Chapter 4, Jeff Lewis ﬁnds information where no one had looked before,
by including two or more parallel and correlated ecological inference models in the same
analysis. His approach, which can be thought of as analogous to a Bayesian version of
a “seemingly unrelated regression model,” extends King’s model by incorporating a key
feature of numerous data sources.
In Chapter 5, Bernard Grofman and Samuel Merrill propose three relatively simple meth-
ods for ecological inference where the data consist of 2 × 2 tables. All three introduce new
assumptions justiﬁed by the authors in terms similar to local smoothing algorithms. The
idea is that precincts similar to other precincts on the basis of observables are likely to
besimilaronunobservablestoo.Theargumentintroducesaformofinformationthattheau-
thorsusetoidentifywhereonthetomographylinesthepointestimatesprobablylie.The ﬁrst
method is based on minimizing the squared distances from the overall tomography line to
each of the precinct-level tomography lines. The other two methods are constrained variants
of Goodman regression. Speciﬁcally, the second method uses analogous distances to those


---

10
Gary King, Ori Rosen, and Martin A. Tanner
used in the ﬁrst method, but on transformed coordinates rather than the (βb
i , βw
i ) coordi-
nates. The last method combines Goodman regression with the Duncan–Davis method of
bounds. The proposed methods are shown to give answers similar to King’s model in several
real data sets.
Kevin Corder and Christina Wolbrecht, in Chapter 6, are concerned with estimating
newly enfranchised women’s turnout in the 1920 U.S. elections in three states. They use
the hierarchical Bayesian binomial–normal model proposed by Wakeﬁeld but employ in-
formative priors based on prior elections and census data. Their central contribution is to
recognize new forms of information in terms of detailed prior, nonsample knowledge of the
problem. For example, we know almost for certain that in this period, when women had just
gotten the vote, they cast their ballots less frequently than men. In statistical terms, we are
essentially certain that βb
i > βw
i for all i and so we can sample from only the portion of the
tomography line satisfying the constraint. This greatly increases the information content in
their analyses.
In Chapter 7, George Judge, Douglas Miller, and Wendy Tam Cho model the ecological
inference problem as an ill-posed inverse problem with a solution selected from the set of
feasible solutions – either via maximizing entropy, which implies one set of assumptions, or
using the Cressie–Read statistic, which allows for the choice among a variety of others. This
approach enables the authors to bring new information to the ecological inference problem
in the form of assumptions about individual behavior, often learned from prior survey and
other work. The model can be ﬁtted to R × C tables and allows for explanatory variables
reﬂecting individual spatial or temporal heterogeneity.
In Chapter 8, Ben Pelzer, Rob Eisinga, and Philip Hans Franses propose a model for
estimating individual-level binary transitions based on repeated cross-sectional data. The
basic problem is equivalent to the classic ecological inference problem with 2 × 2 tables,
where the unknown transition probabilities play the role of the unknown cell probabilities.
They introduce assumptions in order to model important information available as lags
of some exogenous variables. Inference is performed via maximum likelihood, parametric
bootstrap and MCMC methods. The methodology is illustrated with data on personal
computer ownership in Dutch households.
Part Three is devoted to methods that attempt to include geographic or time series
informationinmodelsofecologicalinference.InChapter10,KevinQuinndevelopsBayesian
hierarchical models for ecological inference in the presence of temporal dependence. He
builds on Wakeﬁeld’s approximation to a convolution of binomials and puts priors on the
approximate likelihood’s parameters reﬂecting temporal dependence. This class of models
mayalsobeusefulinsomesituationsforspatialorsimultaneousspatiotemporaldependence.
Inference is performed via MCMC methods. Quinn studies the methodology via simulated
data, as well as by analyzing real data on voting registration by race in Louisiana counties
over a 14-year period. Carol Gotway Crawford and Linda Young, in Chapter 10, give an
overview of the ecological inference problem from a spatial statistics perspective. These
authorspointoutthatecologicalinferenceisaspecialcaseofthechange-of-supportproblem
in geostatistics, which refers to the geometric size, shape, and spatial orientation of the
regions associated with the observed measurements. Changing the support of a variable
thus creates a new variable. The problem of how the spatial variation in one variable relates
to that in the other is the change-of-support problem, a possible solution being spatial
smoothing. The authors illustrate these issues with a case study on low-birth-weight babies.
In Chapter 11, Ernesto Calvo and Marcelo Escolar consider ecological inference in the
presence of spatial heterogeneity, which may lead to underestimated standard errors or new
forms of bias on top of the aggregation bias inherent in ecological inference. In this chapter


---

Information in Ecological Inference: An Introduction
11
theauthorsallowforspatialheterogeneitybyusinggeographicallyweightedregressioninthe
context of Goodman’s and King’s ecological inference models. Their idea is to incorporate a
nonparametric term reﬂecting spatial effects into these models, resulting in semiparametric
models. These models are explored via simulation and with Peronist voting data.
Chapter 12 introduces methods of ecological inference that draw on the extensive spatial
epidemiology literature. Therein Sebastien Haneuse and Jon Wakeﬁeld show how to model
spatial and nonspatial heterogeneity. They incorporate important new information into
ecological inference by modeling the fact that multiple diseases share common risk factors,
and these risk factors often exhibit spatial clustering. Modeling this clustering, they show,
can greatly improve ecological inferences.
Finally, in Part Four, we include comparisons of some existing ecological inference meth-
ods. Ruth Salway and Jon Wakeﬁeld contrast ecological inference in political science, which
tends to focus on descriptive quantities such as the fraction of African Americans voting
for the Democrats, and in epidemiology, in which interest is primarily in causal inferences
(Chapter 13). Of course, political scientists and most others are also interested in causal
inferences, and so the work here should be of general interest. The key problem in making
causal inference is confounding, and so Salway and Wakeﬁeld analyze the combined effects
of confounding bias along with aggregation bias. They show how sources of information
about confounding can help improve ecological inferences.
Kenneth Benoit, Michael Laver, and Daniela Giannetti in Chapter 14 discuss the use of
King’s model in the context of an extensive split-ticket voting application. In Chapter 15,
Rog´erio Silva de Mattos and Alvaro Veiga compare Goodman’s regression, King’s model,
and the hierarchical beta-binomial model (King, Rosen, and Tanner, 1999). To facilitate
the simulation-based comparison, the authors use their own version of the beta–binomial
model where estimation is performed via the ECM algorithm. The authors’ main conclusion
is that King’s model is superior to the other methods in predictive ability.
In Chapter 16, Micah Altman, Jeff Gill, and Michael McDonald compare the numerical
properties of implementations of Goodman regression, King’s model, and McCue’s method.
They look at sources of numerical inaccuracy such as ﬂoating point arithmetic, nonlinear
optimization, and pseudorandom numbers. The stability and accuracy of the algorithms are
tested by introducing random perturbations into the data. The authors’ recommendation
is to use data perturbations as a diagnostic test in addition to any other diagnostic tools
associated with these ecological inference methods.
REFERENCES
Achen, Christopher H. and W. P. Phillips Shively. 1995. Cross-Level Inference. Chicago: University of
Chicago Press.
Adolph, Christopher and Gary King, with Michael C. Herron and Kenneth W. Shotts. 2003. “A Con-
sensus Position on Second Stage Ecological Inference Models,” Political Analysis, 11: 86–94.
Duncan, Otis Dudley and Beverly Davis. 1953. “An Alternative to Ecological Correlation,” American
Sociological Review, 18: 665–666.
Goodman, Leo. 1953. “Ecological Regressions and the Behavior of Individuals,” American Sociological
Review, 18: 663–666.
Goodman, Leo. 1959. “Some Alternatives to Ecological Correlation,” American Journal of Sociology,
64: 610–624.
King, Gary. 1997. A Solution to the Ecological Inference Problem: Reconstructing Individual Behavior
from Aggregate Data. Princeton: Princeton University Press.
King,Gary,OriRosen,andMartinA.Tanner,1999.“Binomial–BetaHierarchicalModelsforEcological
Inference,” Sociological Methods and Research, 28: 61–90.


---

12
Gary King, Ori Rosen, and Martin A. Tanner
King, Gary, Ori Rosen, Martin A. Tanner, and Alexander Wagner. 2003. “The Ordinary Election of
Adolf Hitler: A Modern Voting Behavior Approach,” http://gking.harvard.edu/files/abs/
making-abs.shtml.
Ogburn, William F. and Inez Goltra. 1919. “How Women Vote: A Study of an Election in Portland,
Oregon,” Political Science Quarterly, 3, XXXIV: 413–433.
Rosen, Ori, Wenxin Jiang, Gary King, and Martin A. Tanner. 2001. “Bayesian and Frequentist Inference
for Ecological Inference: The R × C Case,” Statistica Neerlandica, 55, 2: 134–156.
Tanner, M. A. 1996. Tools for Statistical Inference: Methods for the Exploration of Posterior Distributions
and Likelihood Functions, 3rd ed., New York: Springer-Verlag.
