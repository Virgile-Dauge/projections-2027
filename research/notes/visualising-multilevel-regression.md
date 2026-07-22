---
title: Visualising Multilevel Regression
id: visualising-multilevel-regression
tags:
- mrp
- academic-paper
- mrp-visualization
- mrp-uncertainty
created: '2026-07-21T18:30:28.011874Z'
updated: '2026-07-21T18:39:17.699165Z'
source: https://arxiv.org/pdf/2205.12478
source_domain: arxiv.org
fetched_at: '2026-07-21T18:30:28.011570Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Dewi Lestari Amaliah (Monash Univ. Master''s project report, supervised
  by Lauren Kennedy & Shiro Kuriwaki, May 2022, posted to arXiv stat.AP) — a systematic
  literature review of how MRP estimates are visualised in published research, plus
  an original case study applying MRP to estimate Trump vote share in the 2016 US
  presidential election using CCES (Cooperative Congressional Election Study) data.
  Central empirical finding: across the reviewed literature, uncertainty is rarely
  displayed alongside MRP point estimates despite its centrality to survey inference,
  and the choropleth map is by far the most common display format even though it only
  conveys point estimates and can obscure information; the report proposes alternative
  visualisation strategies that jointly convey point estimates, uncertainty, and the
  bias-variance trade-off across competing model specifications. Uses the mrpkit/ccesMRPprep/brms/cmdstanr
  R toolchain. Primarily useful here as a secondary methodological source on best
  practice for communicating MRP uncertainty (directly relevant to the militant-facing
  ''where does the model''s confidence run out'' cartography use case) rather than
  as a France-specific or election-outcome source; longer literature-review chapter
  (~15,000 words total) may warrant deeper extraction by a source-analyst if MRP uncertainty-communication
  becomes a focus axis.'
raw_file: raw/visualising-multilevel-regression.pdf
---

Visualising Multilevel Regression
and Poststratiﬁcation:
Alternatives to the Current
Practice
A research project report submitted for the unit of
Business Analytics Creative Activity
by
Dewi Lestari Amaliah
31251587
Department of Econometrics and Business Statistics
Monash University
Australia
May 2022
arXiv:2205.12478v1  [stat.AP]  25 May 2022


---

Contents
Abstract
1
Acknowledgements
3
R packages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1
Introduction
5
1.1 MRP Overview
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
1.2 Report Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2
Systematic Literature Review
9
2.1 Literature Identiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.2 Screening and Eligibility Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3 Data Extraction and Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.4 Common practices in MRP visualisations . . . . . . . . . . . . . . . . . . . . . 15
3
Case Study: Application of MRP in Presidential Voting Estimation
23
3.1 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2 Model Speciﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.3 Model Preparation and Fitting
. . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.4 Results and Discussion
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4
Conclusion
45
A Appendix
47
A.1 Supplementary Material
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
A.2 Terms description
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
A.3 Proportion of observations by states . . . . . . . . . . . . . . . . . . . . . . . 48
A.4 Additional Graphs
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
Bibliography
57
ii


---

Abstract
Surveys provide important evidence for policy making, decision making and understand-
ing society. However, conducting the large surveys required to provide subpopulation
level estimates is expensive and time-consuming. Multilevel Regression and Poststrati-
ﬁcation (MRP) is a promising method to provide reliable estimates for subpopulations
from surveys without the amount of data needed for reliable direct estimates. Graphical
displays have been widely used to communicate and diagnose MRP estimates. However,
there have been few studies on how visualisation should be performed in this ﬁeld.
Accordingly, this study examines the current practice of MRP visualisation using a
systematic literature review. This study also applies MRP to estimate the Trump vote share
in the U.S. 2016 presidential election using the Cooperative Congressional Election Study
(CCES) data to illustrate the implication of current visualisation practices and explore
alternatives for improvement. We ﬁnd that uncertainty is not often displayed in the
current practice, despite its importance for survey inference. The choropleth map is the
most frequently used to display MRP estimates even though it only shows point estimates
and could hinder the information conveyed. Using various graphical representations,
we show that visualisation with uncertainty can illustrate the effect of different model
speciﬁcations on the estimation result. In addition, this study also proposes a visualisation
strategy to also take the bias-variance trade-off into account when evaluating MRP models.
1


---

Acknowledgements
I would like to express my deepest gratitude to my supervisors, Lauren Kennedy and Shiro
Kuriwaki. They have given me so much time, knowledge, wisdom, and patience since I
started until I ﬁnished this project. Their continuous feedback, guidance, encouragement,
and advice were like a light in the dark, especially when this project became increasingly
challenging to complete.
I would like to extend my gratitude to Dan Simpson, the chief examiner of Master of
Business Analytics and Creative Activity, for all the guidance in completing this unit.
I also would like to thank Australia Awards Scholarship for giving me the scholarship to
study at the Monash University. Without it, studying in Australia would only remain as
one of my childhood dreams.
Last but not least, I dedicate this work to my late father, who always gave me unconditional
love and support in pursuing my dreams.
R packages
Several R (R Core Team, 2020) packages are utilized to produce this report: mrpkit
(Kennedy, Gabry, Amaliah, Alexander, 2021); ccesMRPprep (Kuriwaki, 2021a); brms
(Bürkner, 2018); cmdstanr (Gabry and ˇCešnovar, 2021); ddi (Kuriwaki, 2020);survey
(Lumley, 2010); tidyverse (Wickham et al., 2019); forcats (Wickham, 2020); Metrics
(Hamner and Frasco, 2018); data.table (Dowle and Srinivasan, 2021); kableExtra (Zhu,
2021); janitor (Firke, 2020); scales (Wickham and Seidel, 2020); ggplot2 (Wickham,
3


---

CONTENTS
2016); patchwork (Pedersen, 2020); flipPlots (Displayr, 2021); igraph (Csardi and Ne-
pusz, 2006); urbnmapr (Strochak, Ueyama, and Williams, 2021); ggstance (Henry, Wick-
ham, and Chang, 2020); ggpmisc (Aphalo, 2021); wacolors (McCartan, 2021); rmarkdown
(Xie, Dervieux, and Riederer, 2020); knitr (Xie, 2014); MonashEBSTemplates (Hyndman,
2020).
4


---

Chapter 1
Introduction
Accurate population and subpopulation estimates are essential to draw insight from the
data, especially when policies or decisions are made given the speciﬁc context of smaller
regions. However, conducting a large survey to provide statistics at a subpopulation level
is expensive, time-consuming, and often needs to account for unrepresentative samples.
Multilevel regression and poststratiﬁcation, henceforth referred to as MRP, is a model-
based approach used to estimate subpopulations. In short, MRP incorporates a multilevel
regression technique to predict the outcome of interest using survey data. This prediction
is then poststratiﬁed using the population size from a larger survey or census to get the
population estimates.
MRP is widely applied to create small area estimates in the absence of a subnational
surveys (Hanretty, 2020) particularly small geographic areas, such as state or county
estimates. MRP also allows the demographic-wise estimation, such as gender, age group,
and education. Additionally, MRP is also often applied to adjust the estimation from a
non-representative survey as the result of difﬁculties in recruiting representative survey
respondents (Gelman, 2007)
The standard method to communicate and validate the MRP estimates, such as their
accuracy, is by using graphics. Indeed, statistical graphics are regarded a powerful tool
to communicate quantitative information and analyse data (Cleveland, 1985; Chambers,
1983). Wickham, Cook, and Hofmann (2015) state that statistical visualisation, particularly
5


---

CHAPTER 1. INTRODUCTION
model visualisation, is imperative as it helps us to understand the model better, for
example, how the model changes as its parameters change or how the parameters change
as the data changes. They also mention that model visualisation is important to show the
model’s goodness of ﬁt and whether it is good for some regions only and worse in other
regions, or whether it is uniformly good.
While visualisation is common to communicate and diagnose MRP models, there are only
a few discussions and studies on how it should be performed. Makela, Si, and Gelman
(2017) and Schneider and Jacoby (2017) work on similar areas focussing on the use of
graphics in political science. However, Makela, Si, and Gelman (2017) only focus on a
graphical method for discovery and communication purposes of polling results. Besides,
the MRP visualisations that they display as examples are isolated on Gelman’s previous
papers only. Meanwhile, the latter study by Schneider and Jacoby (2017) only focuses on
how the graphics in public opinion research should be displayed. Therefore, this study
tries to ﬁll the gap by discussing the current practices of MRP visualisations generally,
not only in public opinion and polling estimates applications. It also aims to explore the
possible alternative improvements to current practice.
Explicitly, the objectives of this study are: discuss the current practice of visualisation of
MRP models; understand the implication of existing visualisation choices with real-world
data; and explore possible improvements of the current practice of MRP visualisation.
The ﬁrst objectives will be reached by doing a systematic literature review on peer-
reviewed articles that applied MRP, while the second and the third goals will be demon-
strated through a case study on the 2016 U.S. presidential election using the Cooperative
Congressional Election Study (CCES) and the American Community Survey (ACS) data.
1.1 MRP Overview
MRP is essentially conducted with two stages - a multilevel/hierarchical regression
modeling stage and poststratiﬁcation stage. The idea is to combine model-based estimation
commonly used in small area estimation with poststratiﬁcation, which is considered
the general framework as a weighting scheme in survey analysis (Gelman and Little,
6


---

CHAPTER 1. INTRODUCTION
1997). Gelman and Little (1997) argue that using multilevel regression estimates for
poststratiﬁcation allows the estimation for many more categories to gain more detailed
population information.
Formally, let K be the number of categorical variables in the population and the kth variable
have Jk categories/levels, the population can be then expressed as J = ∏K
k=1 Jk cells. For
every cell, there is a known population size Nj. If the variable in the population is not in
categorical form, then it should be converted into a categorical variable ﬁrst. Next, suppose
that the outcome of interest is a binary variable. The MRP procedure is summarised in
two stages as follows (Gao et al., 2021):
1. Multilevel regression stage. Multilevel regression is ﬁtted to get estimated popula-
tion averages θj for every cell j ∈{1, ...., J}. The multilevel logistic regression has a
set of random effects αk
m[j] for each categorical covariate k. These random effects have
the effect of pooling each αj partially towards overall grand mean. Suppose that n
is the number of individual observations in the survey data, the form of multilevel
regression could be written as follows:
Pr(yi = 1) = logit−1
 
Xiβ +
K
∑
k=1
αk
m[i]
!
, f or i = 1, ..., n,
αk
m ∼N(0, σ2
k ), f or m = 1, ..., Mk
(1.1)
2. Poststratiﬁcation stage. The probabilities of the outcome in each cell from the previ-
ous stage, θj, is then poststratiﬁed using the known population size Nj of each cell j
to get the estimates at the subpopulation level. This stage corrects the nonresponse in
the population by utilizing the known size of every cell j relative to the total popula-
tion size N = ∑J
j=1 Nj. In other words, the estimates is a weighted average of θj with
Nj as the weight. Suppose that S is the subpopulation which is the combination of
categories in the poststratiﬁcation matrix, the MRP estimates could be expressed as:
7


---

CHAPTER 1. INTRODUCTION
θS = ∑j∈S Njθj
∑j∈S Nj
(1.2)
1.2 Report Structure
The ﬁrst chapter of this report is introduction in which the motivation and objectives
of this study are articulated. Chapter 2 is a systematic literature review. This chapter
discuss the review of current practice in MRP visualisations in various studies. Next,
Chapter 3 is a case study of MRP visualisations. This chapter aims to demonstrate the
MRP application in the case of U.S. presidential voting result estimation. This chapter also
demonstrates how the current practice of MRP visualisation could be improved. The ﬁnal
chapter, Chapter 4, summarises the ﬁndings and concludes the contribution of this study
and possible future works.
8


---

Chapter 2
Systematic Literature Review
This study is performed using a systematic review method. This method collects empirical
evidence explicitly and systematically using pre-speciﬁed eligibility criteria to answer a
speciﬁc research question (Green et al., 2008). Systematic literature reviews also enable the
process of ﬁnding the gap in a ﬁeld of science, such as understanding what has been done
and what needs to be done (Linnenluecke, Marrone, and Singh, 2020). Hence, in this case,
systematic literature review could assist us to understand the common practice in MRP
visualisations so that we can explore how to improve.
According to Brown University Library (2021), the key criteria of the systematic literature
review are: “a clearly deﬁned question with inclusion & exclusion criteria; rigorous & systematic
search of the literature; critical appraisal of included studies; data extraction and management;
analysis & interpretation of results; and report for publication.” Hence, to conform with these
criteria, this study incorporates the Preferred Reporting Items for Systematic Reviews and
Meta-Analysis (PRISMA)’s checklist and ﬂow diagram. The following subsections discuss
the steps conducted following these criteria.
2.1 Literature Identiﬁcation
MRP is applied in various scientiﬁc ﬁelds, ranging from social and political science to
public health. Therefore, to identify relevant literature, this study refers to research
databases instead of ﬁeld-speciﬁc journals. Those databases are JSTOR, EBSCO, and
9


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
PubMed. The ﬁrst two databases are chosen due to their broad range of ﬁeld coverage,
while the latter is chosen since MRP is sometimes also applied in the health and medical
ﬁelds. These databases were also chosen to represent the heterogeneity of the ﬁeld, which
is one of the important factors in a systematic literature review (Schweizer and Nair, 2017).
From these databases we identify relevant articles using the combination of several
search terms. Generally the search terms include the term “multilevel regression”, “post-
stratiﬁcation”, “poststratiﬁcation”, and “multilevel model”. Our target literature is articles
that are written in English. We exclude all of the publications before 1997 since this was the
ﬁrst proposal date for MRP. Initially we included only the title/abstract when searching
these databases. However, using this method limits the set of potential articles to only
include those with the search term in the abstract/title. To rectify this, we also include a
search with “all ﬁeld” in the search criteria. Note that for EBSCO, we directly apply the
search for all ﬁelds. The detailed literature identiﬁcation is shown in Table 2.1.
The total number of articles from this search criteria are 327. Next, we utilize the literature
manager, EndNote X9, to manage these articles and to ﬁnd duplicate articles. After
removing those duplicate articles, we have 212 articles to be screened in the next stage.
10


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
Table 2.1: Detail of literature identiﬁcation
Database
Search Terms
Search Field
Inclusion
Exclusion
Number Returned
JSTOR
(multilevel regression and
poststratiﬁcation) OR
(“post-stratiﬁcation”)
Abstract
Article, content I can access, English
anything before 1997
44
JSTOR
(("multilevel regression" AND
("post-stratiﬁcation" OR
Poststratiﬁcation)) OR ("multilevel
model" AND ("post-stratiﬁcation"
OR Poststratiﬁcation)))
All ﬁeld
Article, English
anything before 1997
142
EBSCO
"multilevel regression with
post-stratiﬁcation" OR "multilevel
regression with poststratiﬁcation"
OR "multilevel regression and
Poststratiﬁcation" OR "multilevel
regression and Post-stratiﬁcation"
All ﬁeld
Academic (Peer-Reviewed) Journals, English
anything before 1997
42
EBSCO
(multilevel regression AND
post-stratiﬁcation) OR (multilevel
model AND post-stratiﬁcation)
OR (multilevel regression AND
poststratiﬁcation ) OR (multilevel
model AND poststratiﬁcation)
All ﬁeld
Academic (Peer-Reviewed) Journals, English
anything before 1997
45
PubMed
"multilevel regression with
post-stratiﬁcation" OR "multilevel
regression with poststratiﬁcation"
OR "multilevel regression and
Poststratiﬁcation" OR "multilevel
regression and Post-stratiﬁcation"
Title/Abstract
Article, English
anything before 1997
26
PubMed
(multilevel regression AND
post-stratiﬁcation) OR (multilevel
model AND post-stratiﬁcation)
OR (multilevel regression AND
poststratiﬁcation) OR (multilevel
model AND poststratiﬁcation)
All ﬁeld
Article, English
anything before 1997
28
11


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
2.2 Screening and Eligibility Criteria
We screen all of the articles based on predetermined criteria. We ﬁnd that 3 articles are
apparently not research papers. This results in 209 abstracts to be screened. To screen
efﬁciently, we use two stages. The ﬁrst stage is a review of abstracts, the second a full
manuscript review.
2.2.1 Stage 1: Review of abstracts
In the ﬁrst stage the author and and my supervisor (Kennedy) independently review all
article abstracts with the following eligibility criteria:
1. The abstract should mention analysis of data or creation of simulation data.
2. The abstract should mention the use of MRP or multilevel models to make population
estimates or the use of other regression models (BART, spatial, stacking, trees) to
make population estimates.
During the screening, we agreed agreed that 61 articles meet the eligibility criteria listed
above, while 104 articles do not meet the criteria. The two reviewers disagreed on 44
articles. Accordingly, we skim the full manuscript to decide whether the paper could be
included in the next stage or not. As the result, an additional 22 more articles are moved
to stage 2, making a total of 83.
2.2.2 Stage 2: Full manuscript review
DA reviews the full manuscript on 83 articles based on a second set of criteria. The aim of
this stage is to get the list of the ﬁnal articles that would be included in the study. We set
the criteria of inclusion as follow:
1. It should apply MRP as its method.
2. It should contain at least one plot relate to MRP ﬁndings.
During this stage, we exclude 4 articles as they do not meet the ﬁrst criteria. Further, 7
articles are excluded as they do not meet the second criteria. Also, an article is not included
12


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
Figure 2.1: PRISMA ﬂow chart of this systematic literature review.
because it is a duplicate that was not detected automatically by Endnote X9. Finally, we
have 71 articles to be reviewed in the next stage. Figure 2.1 displays the PRISMA ﬂow
chart of this study. This ﬁgure is generated using PRISMA2020 (Haddaway, Pritchard, and
McGuinness, 2021).
2.3 Data Extraction and Analysis
We focus the data extraction on the MRP-related plot. We manually create a metadata
for each plot (included in the supplementary material). We will use this metadata to
analyse the current reporting practices with MRP. This metadata will also ensure the
reproducibility of the analysis and to maintain the transparency of the systematic literature
review process.
13


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
We code the plots according to their type, i.e., communication (coded to 0) and diagnostic
plot (coded to 1). For diagnostic plots, we examine whether the plots compare MRP with
other estimates, which are:
1. Raw (direct estimates or direct disaggregation);
2. Ground truth;
3. Weighted estimates;
4. Estimates from other MRP models, for example, a paper build several MRP models
from various simulation scenarios or using different covariates;
5. Estimates from another study/survey;
6. Estimates from another method, for example comparing MRP with Bayesian Additive
Tress with Post-Stratiﬁcation(BARP).
Plots that show a comparison of MRP with the above list would be coded to 1, otherwise
coded to 0. Diagnostic plots also categorised based on how they compare the performance
of MRP. The ﬁve observed criteria are:
1. Bias;
2. Mean Absolute Error (MAE);
3. Mean Square Error (MSE)/ Relative Mean Square Error (RMSE);
4. Standard Error (SE);
5. Correlation.
Each plot is assessed based on the use of the performance metric. For each metric is scored
based on whether it is used (coded 1) or not (coded 0).
We also review other features of the plot using the grammar in ggplot2 (Wickham, 2016)
as a framework. The common grammar used in practice allows us to understand to what
extend MRP models are effectively visualised. It is worth noting that there is no speciﬁc
convention or well-documented recommendation on how data should be visualised as
building a graph more often involves choice or preference (Midway, 2020). For example,
there is no speciﬁc convention on which variable should be put on the x and y-axis in a
14


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
scatter plot, even though it has been common knowledge to put the response variable
on the y-axis and the explanatory variable on the x-axis. Hence, grammar assists us
in evaluating well-formed graphics (Wickham, 2010). In addition, Vanderplas, Cook,
and Hofmann (2020) mention that classifying and comparing graphs according to their
grammar is more robust and more elegant.
Accordingly, we examine the facet, geom, axis, color, and shape. For reproducibility, the
metadata also contains the article’s author/s, publication year, title, and corresponding
ﬁgure number as it appeared in the article. After the extraction, we analyze the data using
graphical visualization with ggplot2 (Wickham, 2016). The result will be discussed in the
following subsection.
2.4 Common practices in MRP visualisations
In this study, graphics are classiﬁed into two types, i.e., communication and diagnostic
plots. A plot is classiﬁed as a communication plot if the plot’s goal is solely to convey
the MRP result. A diagnostic plot is used to understand the MRP estimate, and typically
displays the MRP estimation by showing the performance metrics or compares it with
other estimation methods. From 71 articles, we extract the data of 243 plots. 47.33 % of
these plots are diagnostics plots, while the remaining are communication plots.
2.4.1 Performance metrics used in MRP
According to Botchkarev (2019), performance metrics is “a logical and mathematical construct
designed to measure how close are the actual results from what has been expected or predicted”
RMSE and MAE are among the most common methods used in many studies (Botchkarev,
2019). However, Willmott and Matsuura (2005) states that RMSE should not be reported in
any studies since it could be multi-interpreted because it does not describe average error
alone and MAE is more appropriate metric. This argument is denied by Chai and Draxler
(2014) who argue that RMSE is not ambiguous and better than MAE if the distribution of
model’s error is normal. Accordingly, there is no single metric that ﬁts all methods (Chai
and Draxler, 2014).
15


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
0
10
20
30
40
MAE
bias
correlation
MSE/RMSE
SE
Performance criteria
Count
Figure 2.2: We observed ﬁve performance metrics used: Mean Absolute Error (MAE), bias,
correlation, Mean Square Error/Root Mean Square Error (MSE/RMSE), and Standard
Error (SE). Each bar represents the number of plot that show performance metrics,
particularly, the grey shade represents the number of plot that show MRP performance
but did not use the corresponding metrics. It is possible that a plot shows more than
one metrics, so that the blue bars do not count to the sum. We learn that MAE is
metrics that is mostly shown in plots we reviewed.
In this study, we ﬁnd that there are 39 plots out of 115 diagnostic plots (about 34%) that
display performance measures. As seen in Figure 2.2, we ﬁnd that MAE is the most widely
used performance metric in MRP visualisations. Bias, which is interpreted similarly to
MAE, is also widely used. Meanwhile, the squared error measures, which are MSE/RMSE
and standard error, are only used in a few plots. It is interesting that correlation, which is
not a common metric for performance, is more widely used than square error metrics.
Most of these metrics only refer to point estimates, i.e., the distance between the predicted
value and the actual values. Also, these metrics mainly measure bias. However, MRP is a
model in which bias-variance is applied. Therefore, other measures are also needed that
reﬂect the degree of uncertainty and variations in the predicted value. Measures such as
length of conﬁdence or credibility interval can be used, in which the narrower the value,
the more precise the estimates.
16


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
0
30
60
90
raw
truth
MRP
other study
weight
other method
Comparison of MRP estimates with
Count
Figure 2.3: Estimates that are compared with MRP. The bars represent the number of plots that
display comparison of MRP with other estimates. Particularly, the blue shade repre-
sents the number of plots that compare MRP estimates with the estimates shown in
each bar, while the grey shade represents the number of plots that also show comparison
of MRP but did not compare to this particular estimate. Note that the blue bars do not
sum to the count because some plots compared to multiple alternative estimates. It is
shown that MRP estimates are mostly compared with raw estimates.
2.4.2 Common comparisons with MRP
The goal of MRP is to make a population estimate. The method aims to adjust an unrep-
resentative survey to obtain accurate population and sub-population estimates. Where
possible MRP is usually compared with a true value. This is generally only possible in
political science applications where an election provides this true estimate. To understand
how MRP improves estimates from an unrepresentative survey when compared with no
adjustment, MRP estimates are usually compared with direct estimates (raw). Similarly, to
understand the improvement of estimates when compared with more traditional methods,
MRP is often compared with weighted estimates.
This study ﬁnds that from 115 diagnostic plots, 109 (about 95%) compare MRP estimates
with estimates from other methods. Figure 2.3 shows the distribution of alternative
17


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
Communication
Diagnostic
0
10
20
30
0
10
20
30
other
histogram & density plot
bar plot
choropleth map
line plot
scatter plot
dot plot
 
 
uncertainty
no
yes
Figure 2.4: Common plot types used in MRP visualisations. The blue shade display the number of
plots that showed uncertainty, while the grey shade display the number of plots that
did not show uncertainty. Both communication and diagnostics plots rarely displayed
uncertainty.
estimates. MRP estimates are mostly compared to direct estimates and the ground truth.
Some studies also compare estimates from several MRP models (usually with different
model speciﬁcations). There are not many plots showing the comparison between MRP
estimates and weighted estimates.
2.4.3 Common grammar in MRP visualisations
Plot type
Plot type, referred to as geom in the grammar of graphics, represents the shape and features
displayed in the graph. Figure 2.4 suggests that communication and diagnostic plots have a
different pattern in which plot types are used (See Appendix A.2 for description/deﬁnition
of each plot type). Communicating MRP estimates are mostly done using a choropleth
map as MRP is often used for small area estimation. For diagnostic purposes, dot plots are
mostly used to compare more than two estimation methods or to show some performance
metrics.
18


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
Notice that Figure 2.4 also displays the use of uncertainty in MRP model visualisations.
According to Midway (2020), displaying uncertainty in the statistical graphs is essential
as the absence of this measure would produce a misleading interpretation and hinder
some statistical messages. However, he further states that uncertainty is often neglected
in data visualisation. This is what we ﬁnd in this study - uncertainty is not often seen in
the plots. This is possibly because many of the application areas are more familiar with
ofﬁcial statistics. In ofﬁcial statistics uncertainty is often unreported because results that
are not sufﬁciently precise are not reported.
Values put in x and y-axis
The main component of a data visualisation is the axis. x and y-axis represents what
value/data are exactly displayed in the graph. In MRP visualisations (Figure 2.5), esti-
mates, small area, actual value (truth), and time are among the values that are displayed
in the plot. We can also see that the constructs represented by the x and y-axis are more
varied in diagnostic plots. It is worth noting that there are no strict rules on values to put
in x and y-axis. However, it is a common that the the ﬁxed value is represented by the
x-axis, while the random variable is represented in the y-axis. We do not see this in our
results as we ﬁnd estimates and truth are plotted on the x and y axes interchangeably.
Another common rule of thumb is that time is almost always represented on the x-axis,
which is supported by the ﬁndings of our study.
Facet
Paneling or faceting is considered as to one of the effective visualisation techniques to
compare the same variables by its grouping factor (Midway, 2020). We ﬁnd in our results
that faceting is a common practice in MRP visualisations. Figure 2.6 shows that faceting
the plots by small area that is being estimated is the most common, followed by case.
Small area refers to the levels of the predictors in the MRP model, for example, state,
county, and religion. In several plots, small area could be referred to another variable
that is associated with the MRP estimates, but is not included in the model, such as the
association between health literacy and the opinion on a health-related bill. Health literacy
19


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
2
1
1
2
56
6
37
10
10
2
1
case
estimates
latitude
longitude
not used
small area
time
year
case
estimates
latitude
longitude
not used
small area
time
year
Values in x−axis
Values in y−axis
a) Communication plots
1
2
12
1
1
11
12
2
2
8
5
4
8
2
1
2
11
6
12
1
11
case
estimates
estimation methods
latitude
longitude
not used
performance criteria
sample size
simulation scenario
small area
time
truth
case
estimates
estimation methods
latitude
longitude
not used
performance criteria
sample size
simulation scenario
small area
time
truth
Values in x−axis
Values in y−axis
b) Diagnostic plots
Figure 2.5: Common values put in plots’ axis. If the values represented in the x and y-axis are
longitude and lattitude, it means that the plot is a map. ‘not used’ means that the plot
is one dimension. It conveys that axis in diagnostic plots more varied compared to
communication plot.
20


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
0
30
60
90
small area
case
estimation methods
simulation scenario
performance criteria
sample size
display type
estimates
What is in the facet
Count
Figure 2.6: The facetting variable in MRP visualisations. Most of plots in the articles reviewed
are faceted by small area and case (outcomes measured)
is a variable that is not included in ﬁtting the MRP model, while the latter is the MRP
estimates. Further, case is referred to the outcome predicted with MRP.
Other features used
Besides the features explained previously, color and shape are also the components of
grammar of graphics. According to a large experimental study on visualisations, color
is a memorable feature of a graph (Midway, 2020). Further, Few (2008) states that the
aim of color in data visualisations are to highlight particular data, to group items, and to
encode quantitative values. In addition, color is sometimes displayed along with shapes
to distinguish more features.
We ﬁnd, as shown in Figure 2.7, that both communication and diagnostic plots incorporate
color only about half the time. Shape is used less often. When there is only one feature
to be displayed, for example, estimation methods, people tend to choose to use color
ﬁrst, rather than shape. This is seen in Figure 2.7 as after incorporating color to distinct
estimates, small area, estimation methods, and performance criteria, people tend to not
use shape anymore.
21


---

CHAPTER 2. SYSTEMATIC LITERATURE REVIEW
aim: communication
aim: diagnostic
color: estimates
color: Not used
color: small area
color: time
color: estimation methods
color: performance criteria
shape: Not used
shape: case
shape: small area
shape: time
shape: estimation methods
Figure 2.7: Values that are commonly represented by color and shape in MRP visualisations. Both
communication and diagnostic plots rarely use color and shape features to display
values.
22


---

Chapter 3
Case Study: Application of MRP in
Presidential Voting Estimation
The majority of MRP applications are used in the context of estimating public opinion in
the social and political sciences, although, in recent developments MRP has also been used
in other ﬁelds, for example, health and environmental studies. When ﬁrst introduced by
Gelman and Little (1997), MRP was applied to generate state estimation of the 1988 U.S.
presidential election. Various subsequent studies also made presidential voting the case of
interest. We recorded at least seven articles (Gelman (2014); Ghitza and Gelman (2013);
Kiewiet de Jonge, Langer, and Sinozich (2018); Lauderdale et al. (2020); Lei, Gelman,
and Ghitza (2017); Park, Gelman, and Bafumi (2004); Wang et al. (2015)) included in the
systematic literature review in Chapter 2 that also applied MRP to presidential election
estimation. In this chapter, we will also apply MRP to estimate the 2016 U.S. presidential
voting outcome, speciﬁcally the probability of voting for Donald Trump in this election.
This also allows us to compare MRP estimates with the actual value of the Trump votes
that are already available. In this case study, we use the Cooperative Congressional
Election Study (CCES) 2016 data (Ansolabehere and Schaffner, 2017) as the survey data
and the American Community Survey data 2015-2017 (U.S. Census Bureau, 2021c) as the
population/ poststratiﬁcation data.
23


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
3.1 Data
3.1.1 Cooperative Congressional Election Study (CCES) 2016
CCES is an annual survey that aims to capture Americans’ view on Congress, their voting
behavior and experience with regards to political geography, social, and demographic
context (Ansolabehere and Schaffner, 2017). In 2016, the CCES covers 64,600 samples
spread over 51 states. Accordingly, Ansolabehere and Schaffner (2017) suggest that the
data is precise enough to measure the distribution of voters’ preference in most states.
In addition, beyond it’s large sample size, CCES is regarded to be a desirable dataset
because it measures vote preference before and after the election so that it is more reliable
compared to a single question format (Kuriwaki, 2021b).
To ﬁt MRP models, we use several variables from this survey. To obtain the data from
the CCES website, we utilize an R package, ccesMRPprep (Kuriwaki, 2021a). One of the
advantages of using this package is that the data has been pre-processed in particular
for MRP purposes, in this case, we use the ccc_std_demographics function. Also, the
variable names are already recoded so it has more interpretable names. The code to get
the data is available in the supplementary materials of this report.
Throughout this demonstration, we estimate the proportion of voters who turned out
to vote for Trump in the 2016 U.S. Presidential Election. We choose this outcome fol-
lowing other demonstrations (e.g. Kuriwaki (2021b); Meng (2018)) precisely because the
population quantity is observed after the survey is run. That allows us to validate my
estimates against a ground truth. To visualise the implication of different model speciﬁca-
tion, we also choose other two outcomes, which are vote preference and party identity.
In CCES 2016 these variables named candidate voted for (CC16_410a), the vote prefer-
ence/intention (CC16_364c),and party identity (pid3 including leaners who are coded as
Independents in pid3 but expressed leaning towards a party in pid7). Table 3.1 shows
the distribution of answers in those three variables. In ccesMRPprep, these variables have
been renamed to intent_pres_16, voted_pres_16, and pid3_leaner, respectively. It is
worth noting that the MRP models we would like to build use binary responses. As we
24


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Table 3.1: Percentage of each answer in CCES 2016 (n = 64,000). This question will be the MRP
models outcome in this case study. Since the model outcome is binary, these answer
will be converted to be yes/no in the context of vote for Trump/Republican.
Candidate voted
percentage
Hilary Clinton
34.27
Donald Trump
29.03
Other / Someone Else
6.26
Did Not Vote
0.13
Not Sure / Don’t Recall
0.35
NA
29.97
Candidate will be voted
percentage
Donald Trump (Republican)
29.76
Hillary Clinton (Democrat)
42.57
Gary Johnson (Libertarian)
4.87
Jill Stein (Green)
2.17
Other
2.91
I Won’t Vote in this Election
5.13
I’m Not Sure
10.12
NA
2.47
Party identity including leaners
percentage
Democrat (Including Leaners)
48.20
Republican (Including Leaners)
32.27
Independent (Excluding Leaners)
16.24
Not Sure
3.20
NA
0.08
are comparing to the US presidential election, we would like a variable that represents
whether the respondents vote for Trump/Republican or not.
Further, the geography and demographic variables used as covariates in the models
are state, age, gender, education, and race. Table 3.2 shows the distribution of cate-
gories/levels of age, gender, education, and race. Initially, age recorded as integers but
we transformed it into ﬁve age groups. Also, education and race have more levels in
the original data but are collapsed to have to obtain fewer levels. In particular, we use the
standard/default categorisation in the ccesMRPprep package. The proportion of people
answered the survey based on the state is displayed in the appendix of this report (A.3).
3.1.2 American Community Survey (ACS) 2015-2017
In this study, we use the ACS 2015-2017 data as the poststratiﬁcation data. The ACS
is a large, survey of the American population conducted by the census bureau and
covering jobs and occupations, demographic and citizenship, educational attainment,
homeownership, and other topics (U.S. Census Bureau, 2021a). The ACS uses monthly
probabilistic samples to produce the annual estimates. The ACS is desirable data to
25


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Table 3.2: The response of covariates. Note that this response has been categorised into certain
levels that are reﬂected in these tables.
Gender
percentage
Male
45.71
Female
54.29
Race
percentage
White
69.44
Black
12.00
Hispanic
10.59
Asian
3.53
Native American
0.81
All Other
3.63
Age
percentage
18 to 24 years
8.30
25 to 34 years
19.62
35 to 44 years
15.75
45 to 64 years
38.36
65 years and over
17.98
Education
percentage
HS or Less
28.41
Some College
35.38
4-Year
23.04
Post-Grad
13.17
represent the U.S. population since the coverage rate, a measure on how well does the
survey cover population, for the 2015-2017 ACS is 92.4%, 91.9%, 91.6%, respectively
(U.S. Census Bureau, 2021b). However, it is also worth noting that the population of
interest of the ACS (American population) and the population we are interested in (voting
population) is different (the ACS measures the general US population, while the CCES
wants to study the behavior of the U.S. adult citizens who turned out to vote), and
therefore, bias might always be presented.
To construct the desired poststratiﬁcation matrix, we need the individual data of the ACS
instead of the aggregated statistics. To do this, we use the 1-year Public Use Microdata
Sample (PUMS), which carries the information/records of individual people on a yearly
basis, appropriately deidentiﬁed. The 1-year PUMS data reﬂects approximately one
percent of the U.S. population (U.S. Census Bureau, 2016). Therefore, in this study, we use
three years periods of the ACS 1-Year PUMS from 2015-2017 instead of 2016 only to get a
better and more stable representation of the American population. Every individual in the
data has a weight (PWGTP). Since we use three years period, this weight is then divided by
3 to obtain a population total that matches the full population total.
The data is publicly available on the U.S. Census Bureau website. We downloaded the
data in a .csv format (csv_pus.zip) year by year (2015-2019) through access on FTP site.
26


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
After that, we did a data pre-processing to bind the three years of the PUMS data. We only
use some variables in this data for the MRP-purposes, i.e., unique identiﬁer of the person
(SERIALNO), state (ST), weight (PWGTP), education (SCHL), sex (SEX), race (RAC1P), Hispanic
origin (HISP), and age (AGEP). We also did a data munging to recode and collapse some
categories in these variables. Note that the RAC1P did not record for Hispanic ethnicity.
Hence, we introduce a new category here, Hispanic, identiﬁed if the person answers other
than “1” in the HISP variable. Table 3.3 shows the categorised response of the variables
obtained from the ACS, i.e., age, race and ethnicity, and education (see Appendix A.3
for state). Also, notice that we get some NA values in education. This is actually the
education level of under-school-age respondents. We omit respondents less than 18 years
old in the MRP models as the (CCES) targets an adult population. Accordingly, the NAs
in education response will be eventually omitted as well. The detailed code of the data
pre-processing is available in the supplementary materials of this report.
27


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Table 3.3: The response categories of post-stratiﬁcation data.
Sex
percentage
Male
48.9
Female
51.1
Race and ethnicity
percentage
White alone
67.00
Black or African American alone
9.89
Hispanic
14.41
Asian alone
5.16
American Indian alone
0.80
Native Hawaiian and Other Paciﬁc Islander alone
0.15
American Indian and Alaska Native tribes
0.08
Alaska Native alone
0.07
Some Other Race alone
0.19
Two or More Races
2.24
Age
percentage
Less than 18 years
20.73
18-24
8.73
25-34
11.92
35-44
11.62
45-54
13.45
55-64
14.64
65-74
10.95
75-89
7.00
90 years and over
0.95
Education
percentage
No high school
27.03
Regular high school diploma
18.82
Some college
21.25
Associate’s degree
6.39
Bachelor’s degree
14.50
Post-graduate
8.99
NA
3.03
3.2 Model Speciﬁcations
In Chapter 2, we found that the diagnostic plots shown in many articles compare MRP
estimates with other estimates. One version of this compares several MRP estimates with
different model speciﬁcations. To allow us to make the same comparisons in this case
study, we build ﬁve different MRP models as follows.
Baseline model
We begin the model ﬁtting with the baseline model. In this model, we set the binary
outcome as whether the respondents vote for Trump or not in the 2016 election. Therefore,
we transform the response of voted_pres_16 into a binary variable called vote ,i.e, if the
value of voted_pres_16 is “Donald Trump”, then vote variable coded to “yes”, otherwise
28


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Table 3.4: The distribution of answer in the outcome (vote). It will be the outcome in three models,
i.e., baseline model, model with education as additional covariate, and model with more
categories in race. We observe a reasonably large percentage of NA.
Candidate voted
percentage
no
41.00
yes
29.03
NA
29.97
“no”. The NA values in voted_pres_16 will stay as NA in the new vote variable. Tthe
distribution of the baseline model’s outcome variable is displayed in Table 3.4.
The demographic predictors used are age, gender, state, and race. As seen in Table 3.2,
race has 6 categories, i.e., White, Black, Hispanic, Asian, Native American, and All
Other. In the baseline model, we collapsed the Native American and All Other into
Other. Meanwhile, the levels of age, gender, state stay the same in the levels displayed
in Table 3.2. The baseline model equation is:
Pr(votej[i] = 1) = logit−1 
β0 + αage
m[i] + αgender
m[i]
+ αstate
m[i] + αcollapsed race
m[i]

,
f or i = 1, ...., n,
β0 ∼t(3, 0, 2.5)
αk
m ∼N(0, σk)
(3.1)
and votej[i] is the binary outcome (1 = yes, 0 = no) for individual i in poststratiﬁcation
cell j. β0 is the intercept. αage
m[i], αgender
m[i]
, αstate
m[i] , and αcollapsed race
m[i]
are the random effects for
age, gender, state, and collapsed race, respectively. The subscript in each coefﬁcient
represents the category of the i −th respondent, such as, αcollapsed race
m[i]
takes value from
{αcollapsed race
White
, αcollapsed race
Black
, αcollapsed race
Hispanic
, αcollapsed race
Asian
, and αcollapsed race
Other
}. Each random effect
has an independent prior distribution, such as, αcollapsed race
m
~ N(0, σ2
collapsed race) and β0 ~
t(3, 0, 2.5). Here, we use the default prior because we only want to compare models for
visualisation purpose instead of looking for the best model for estimation.
29


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Model with education as additional covariate
Next, we create a bigger model by adding education as additional covariate to the
baseline model. The levels of education is also displayed in Table 3.2. Hence, the model
speciﬁcation is:
Pr(votej[i] = 1) = logit−1 
β0 + αage
m[i] + αgender
m[i]
+ αstate
m[i] + αcollapsed race
m[i]
+ αeducation
m[i]

,
f or i = 1, ...., n.
(3.2)
Model with original race categories
This model is essentially the same with baseline model, except that there are more race
categories, which are White, Black, Hispanic, Asian, Native American, and All Other.
The model equation is:
Pr(votej[i] = 1) = logit−1 
β0 + αage
m[i] + αgender
m[i]
+ αstate
m[i] + αoriginal race
m[i]

, f or i = 1, ...., n.
(3.3)
Model with different outcomes
Vote intention/preference
This model mimicks the model in Equation (3.2), except that we have a different outcome
or response variable. The response here is whether the respondent intends to vote for
Trump (yes) or not (no) (rather than whether they reported they voted for Trump). It is
transformed from intent_pres_16 variable in the CCES data to a new variable called
intent. If the value of intent_pres_16 is “Donald Trump (Republican)”, then intent
variable coded to “yes”, otherwise “no”. The NA values in intent_pres_16 will stay as
NA in the new intent variable. The distribution of observed “no”, “yes”, and NA in this
variable is shown in Table 3.5.
30


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Table 3.5: The distribution of answer in the outcome (intent).
Candidate will be voted
percentage
no
67.76
yes
29.76
NA
2.47
Table 3.6: The distribution of answer in the outcome (party).
Party identity
percentage
not Republican
67.65
Republican
32.27
NA
0.08
The model is speciﬁed as follows:
Pr(intentj[i] = 1) = logit−1 
β0 + αage
m[i] + αgender
m[i]
+ αstate
m[i] + αcollapsed race
m[i]
+ αeducation
m[i]

,
f or i = 1, ...., n.
(3.4)
Party identity
Beside vote intention, another outcome is the party identity in terms of whether the
respondents identify themselves as Republican or not. This variable is derived from
pid3_leaner variable and referred as party. If the value of pid3_leaner is “Republican
(Including Leaners)”, then party variable coded to “Republican”, otherwise “not Repub-
lican”. The NA values in pid3_leaner will stay as NA in the new party variable. The
distribution of this outcome variable is displayed in Table 3.6.
The speciﬁcation of covariates is also the same with model in Equation (3.2).
Pr(partyj[i] = 1) = logit−1 
β0 + αage
m[i] + αgender
m[i]
+ αstate
m[i] + αcollapsed race
m[i]
+ αeducation
m[i]

,
f or i = 1, ...., n.
(3.5)
31


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
The estimates from the multilevel model is then used for the second stage of MRP, which is
poststratiﬁcation. As the explanation in Section 1.1, poststratiﬁcation is essentially taking
the weighted average of the cell-wise posterior estimates with the size of each cell in
the population table as the weight (Gao et al., 2021). For example, the poststratiﬁcation
estimates of people who completed High School or less and voted for Trump in the 2016
presidential election is:
θS = ∑j∈S Njθj
∑j∈S Nj
,
(3.6)
where θS corresponds to the proportion of 45 to 64 years old of Black Men attained High
School or less (HS or Less) in Alabama who respond to “yes” in the vote variable and Nj
and θj are the size of cell corresponds to this sub-population category in the poststratiﬁca-
tion table and the posterior estimates of this sub-population category, respectively.
3.3 Model Preparation and Fitting
The MRP models require synchronous measurements between survey and population
data. To achieve this, we need to map the survey data to the population data. In this
study, the model preparation and survey-population data mapping is conducted with
an R package, mrpkit (Kennedy, Gabry, Amaliah, Alexander, 2021). This package allows
the transparent and reproducible workﬂow to build MRP model, from the data mapping
until the prediction stage, including the model speciﬁcation setting. This package is not
the product of this study but I am one of its authors. The detailed code to build the MRP
models is available in the supplementary materials of this report.
After mapping the survey and population data, we can obtain a poststratiﬁcation table,
the ﬁrst ﬁve rows of which is displayed in Table 3.7
Next, we implement a Bayesian multilevel model using brms (Bürkner, 2018) to ﬁt the
model and obtain the posterior distributions of the parameters. brms itself incorporates
either rstan or cmdstanr (Gabry and ˇCešnovar, 2021) as the backend, which in turn wrap
32


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Table 3.7: First ﬁve rows of the post-stratiﬁcation table
age
state
gender
collapsed_re
original_re
education
N_j
18 to 24 years
Alabama
Male
White
White
HS or Less
63982.00
18 to 24 years
Alabama
Male
White
White
Some College
67957.00
18 to 24 years
Alabama
Male
White
White
4-Year
8851.67
18 to 24 years
Alabama
Male
White
White
Post-Grad
320.33
18 to 24 years
Alabama
Male
Black
Black
HS or Less
40443.33
the probabilistic programming language Stan (Stan Development Team, 2020). We use
4000 samples of posterior distribution generated with 4 independent chains. Since this
task is computationally heavy and time-consuming, we conduct it using Monash’s High
Performance Cluster (HPC).
3.4 Results and Discussion
The MRP estimates from these models will be visualised in this subsection. We will
illustrate the implications of current visualisation practices and discuss the possibility
for improvement using these estimates. We will divide the discussion with regards
to communication and diagnostic plot as we did in in the systematic literature review
(Subsection 2.4).
3.4.1 Visualisations for communication purposes
One of the most widely used graphs to communicate MRP estimates is a choropleth
(see Figure 2.4). Choropleth is colored, shaded, or graded to display a spatial pattern
of a certain variable. For example, blue and red are used to represent states with more
Democrat and Republican voters, respectively, as seen in Ghitza and Gelman (2013). A
color gradient is also used to convey a more detailed message, for example, the state-wise
MRP estimates of pro-environment opinion as seen in Eun Kim and Urpelainen (2018).
The greener the shade, the more proportion of people support pro-environmental policy.
These two examples also show the use of color with respect to the meaning that people
generally perceive, i.e., green is often associated with the environment, and blue is often
associated with Democrats.
33


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
0.00
0.25
0.50
0.75
1.00
Estimates of Trump's vote share
MPR estimates of Trump vote shares using the baseline model
Figure 3.1: MRP estimates of probability of state vote for Trump in the U.S. 2016 presidential
election using the baseline model. The deeper the blue shade the lower Trump’s vote
share in the corresponding state, while the deeper the red, the higher Trump’s vote
share. It is shown that the baseline model predicts that Trump has less than 50 percent
vote share in almost every state in the U.S.
In this case study, we create a choropleth of MRP estimates of the probability of voting
for Trump (3.1) in the U.S. 2016 election using the baseline model. We create the same
choropleth that is commonly shown based on our ﬁndings in the literature review.
The choropleth as seen in Figure 3.1 conveys that the baseline model predicts that Trump
has less than 50 percent of vote share in almost every state in the U.S. Regardless of
whether this model has a good ﬁt or not, the message that this graph tries to convey using
color is quite easy to perceive. We can see a blue-shaded U.S. map, meaning that the
Democrat candidate wins the majority of votes in most states. However, this takeaway
is general, while the purpose of MRP, is to give more detailed information about sub-
populations. From the map, we can see that there is only one state that has a red tint.
However, the readers, especially those unfamiliar with the U.S. map, will probably not
know which state this is unless the states are labeled with their name.
34


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Another critic on the choropleth is also stated by Wickham (2013). He argues that choro-
pleth is problematic as polygons with small areas are difﬁcult to observe. In fact, these
areas sometimes carry particular information. For example, small geopolitical areas can
represent a high density of population. He argues that one alternative to overcome this
problem is to replace a choropleth with a cartogram in which the area is distorted so that
its proportional to the value of the variable it represents. Unfortunately, there is no single
visualisation among the articles reviewed that utilize this kind of visualisation.
Choropleth maps also only display point estimates, which is only one component of
our analysis. Uncertainty should also be considered when visualising data, particularly
estimation results, as there is always variability in these (Tukey, 1993; Midway, 2020;
Hullman et al., 2019). In this case, a dot plot with a conﬁdence or credible interval could
be used to visualise MRP estimates, for example, as seen in Enns and Koch (2013). We can
see that there is a reasonably high percentage of the usage of dot plot with uncertainty
in the articles we reviewed. From the 34 dot plots found, 26 (about 76%) of them display
uncertainty. However, compared to the overall number of communication plots, the
portion of the dot plot with uncertainty is only about 20%.
3.4.2 Visualisation for diagnostic purposes
Displaying Comparison of Estimation Methods
According to Tukey (1993), one of the graphic’s purposes is for comparison. In MRP
visualisation practice, the estimates from various estimation methods are often compared.
Here, we compare state-level MRP estimates with raw and weighted estimates compared
to their closeness to the ground truth (actual Trump vote shares), which we obtained
from R-package ddi (Kuriwaki, 2020). The common aesthetic used to display this kind of
purpose in the reviewed articles is a scatter plot (around 31% of the total diagnostic plots).
There is an unwritten “rule of thumb” that when displaying two variables in a scatter
plot, the horizontal axis displays the predictor, while the outcome is put in the vertical
axis (Gelman and Unwin, 2013). Regarding MRP visualisation, this “convention” could be
translated by putting the estimates in the y-axis and the actual value in the x-axis, although
the practice is sometimes interchangeable (see Figure 2.5). We also observe that some of
35


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Method
Raw
RMSE
Weighted
MAD
MRP
0.084
0.012
0.100
0.082
0.008
0.121
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Ground truth (Trump vote)
Estimates (Trump vote)
Estimation methods
Raw
Weighted
MRP
Figure 3.2: Comparison between various estimates (raw, weighted, and MRP) with the actual vote
share for Trump as observed in the election. The MRP model used here is the model
with education as additional predictor. The points represent states with the 95 percent
credible or conﬁdence interval (depending on the method), while color represents the
estimation method used. Weighted estimates is accurately predict the actual value of
Trump’s vote share.
the reviewed scatter plots show performance metrics, such as RMSE and MAE in Meng
(2018). Hence, in Figure 3.2, we also display these. Most scatter plots we reviewed did not
display uncertainty (see Figure 2.4). Here, we add uncertainty to each point estimates. In
addition, we use color-blind-friendly color schemes to distinguish the estimation methods
as mentioned by Vanderplas, Cook, and Hofmann (2020) and Wickham (2013).
From this visualisation, we can clearly see that the weighted estimates, as seen in Figure
3.2, are observed to be the most accurate. It is actually an expected result, as according
to Ansolabehere and Schaffner (2017), the CCES’s weights are poststratiﬁed to match the
statewide election results.
36


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
However, a scatter plot is appropriate when the purpose is to allow the readers to discern
the general information about the relationship shape between two variables rather than
inference about individual data points (Schneider and Jacoby, 2017). Hence, if the purpose is
to inspect which states are least accurately estimated, the scatter plot would not be suitable.
One option to help is to add labels to the points but these labels would be overlapped and
hard to read in this case. Again, the dot plot could be used as an alternative to convey
state-wise information, as seen in Figure 3.3. Here, instead of conveying the estimates,
we use their deviance from the actual value of Trump’s vote share, i.e., the $Estimates -
Actual value $. We also display the states in descending order of the actual value of Trump
votes, i.e., from the most “red” states to the most “blue” states.
Using this graph, we can get the same information regarding estimate accuracy. However,
we can also display other information related to the estimation error, which can then
be compared across estimation methods. It shows that the more conservative the state,
the higher the error. This pattern could indicate that the survey data adjustments are
not sufﬁcient to correct for sampling bias, or potentially bias between the population we
poststratify to and the voting population.
Displaying Comparison of Model Speciﬁcations
Aside from comparing estimation methods(weighed, raw or direct estimates and mrp), we
could also compare between different model speciﬁcations. Revisiting on what Wickham,
Cook, and Hofmann (2015) stated, model visualisation could answer how the model ﬁts
change as the data changes. The following graphics will demonstrate this purpose.
Similar to previous plots, the comparison shown in Figure 3.4 is displayed using a scatter
plot. Here we compare between the MRP estimates and the actual Trump’s vote share.
Since there are ﬁve model speciﬁcations, we use the small-multiple principle (Midway,
2020), i.e., displaying the model ﬁts with facets.
Using this graph, we can observe that the ﬁt changes as the speciﬁcation changes. The 45◦
line assists the readers in inspecting whether the ﬁt is underestimated or overestimated.
Even though almost all of the ﬁts are underestimated, we can see that the bigger model,
i.e., the model with education as an additional covariate, has a better ﬁt than the other
37


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
District of Columbia
Hawaii
Vermont
California
Massachusetts
Maryland
Washington
New York
Illinois
Rhode Island
Oregon
New Mexico
Connecticut
New Jersey
Delaware
Colorado
Virginia
Maine
Minnesota
Nevada
Utah
New Hampshire
Wisconsin
Michigan
Pennsylvania
Arizona
Florida
North Carolina
Georgia
Iowa
Alaska
Ohio
Texas
South Carolina
Montana
Kansas
Missouri
Indiana
Mississippi
Louisiana
Nebraska
Idaho
Arkansas
Tennessee
South Dakota
Alabama
Kentucky
North Dakota
Oklahoma
Wyoming
West Virginia
−0.3
−0.2
−0.1
0.0
0.1
Deviance from the actual value of probability vote for Trump (Estimates − Actual)
State
Estimation methods
Raw
Weighted
MRP
Figure 3.3: The deviance of estimated values from the actual value of Trump’s vote share. The
states in the vertical axis are ordered from states with the highest to the lowest Trump’s
vote share with regards to the ground truth value. The color represents the estimation
methods. Again we saee that weighted estimates show the smallest deviance from the
ground truth. This ﬁgure shows a pattern in which the more conservative the state,
the bigger the deviance.
38


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
RMSE= 0.1169
MAE= 0.1049
0.00
0.25
0.50
0.75
1.00
MRP estimates(Trump vote)
0.00
0.25
0.50
0.75
1.00
Ground truth (Trump vote)
A
RMSE= 0.1002
MAE= 0.088
0.00
0.25
0.50
0.75
1.00
MRP estimates(Trump vote)
0.00
0.25
0.50
0.75
1.00
Ground truth (Trump vote)
B
RMSE= 0.1166
MAE= 0.1045
0.00
0.25
0.50
0.75
1.00
MRP estimates(Trump vote)
0.00
0.25
0.50
0.75
1.00
Ground truth (Trump vote)
C
RMSE= 0.1841
MAE= 0.1751
0.00
0.25
0.50
0.75
1.00
MRP Estimates (Trump vote intention)
0.00
0.25
0.50
0.75
1.00
Ground truth (Trump vote)
D
RMSE= 0.1674
MAE= 0.1559
0.00
0.25
0.50
0.75
1.00
MRP Estimates (Republican)
0.00
0.25
0.50
0.75
1.00
Ground truth (Trump vote)
E
Figure 3.4: Comparison between MRP estimates and the actual Trump’s vote share faceted by
model speciﬁcation. The point represents the state. Panel A represents the ﬁt of baseline
model; B represents the model with education as additional predictor; C represents the
model with more race categories; A, B, and C have the same response variable, vote,
while D and E represente the model with different outcome, which are vote intention
and party identity, respectively. The covariates used in model D and E are the same
with the covariates of model B. We can see that all the models underestimate the actual
Trump’s vote share.
39


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
models (also shown by its MAE). Models in panels D and E, which are models with
different outcomes, are less accurate, which is understandable as the benchmark is the
actual Trump vote-share which is more aligned with the other outcome,vote.
In addition to estimation by small geographical area, MRP is also often used to estimate
population by demographic subsets. We use violin plots to compare how the subpopula-
tion estimates change as the model speciﬁcation changes in the following visualisation. We
use the violin plot as it can show the distribution of the estimates, although this plot was
never observed in the articles we reviewed. It allows the reader to observe the variability
and uncertainty of the rather then just the point estimates of summary statistics.
Figure 3.5 shows the distribution of the response variable, which is probability of vote for
Trump for each demographic levels regardless the geographic levels or the states where
the voters live. This ﬁgure illustrates how the estimates will be different as the result of
different covariates used. For example, in Panel A, the range of probability of vote for
Trump of Native Americans in the model with more race categories is wider than the
model that collapsed Native American and All Other as one race category. We can also
see that the median of the outcome in All Other race categories is slightly different in
the two models. A more pronounced difference could also be observed in Panel B which
compare the baseline model with the model with education level as additional covariate.
Incorporating education into the model results in a different pattern compared to the
baseline model, i.e., the higher the education level, the less probability of voting for Trump.
In Panel C, we can see the same trend for the three model ﬁts, where the older age-groups
tend to be more likely to vote for Trump. However, the median of model with additional
adjustment variables is slightly higher in all age groups.
Visualising Metrics
Metrics are the performance measure of the model in estimating the ground truth. In
this case, however, since the benchmark is not the actual value due to the absence of
Trump’s vote share in demographic levels, the term performance is not quite correct, but
rather difference between these two models. We will still display graphs for these metrics,
though, as an illustration of performance visualisation.
40


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
0.1
0.2
0.3
0.4
0.5
0.6
White
Black
Hispanic
Asian
Native American
All Other
Race
MRP estimates
base model
base model with more levels on race
A
0.30
0.35
0.40
0.45
HS or Less
Some College
4−Year
Post−Grad
Education
MRP estimates
base model
base model + education
B
0.2
0.3
0.4
0.5
18 to 24 years
25 to 34 years
35 to 44 years
45 to 64 years
65 years and over
Age
MRP estimates
base model
base model + education
base model with more race 
C
Figure 3.5: The comparison of MRP estimates by model speciﬁcation. This panel shows the
demographic variables estimated. Panel A, B, and C represents Trump’s vote share by
race categories, education level, and age group, respectively.
41


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
MAE and bias are predominantly used in most of the articles as the model performance
criteria. Essentially, they give the same interpretation, which is how precise the model
is in estimating the actual value. We also observe that correlation is frequently used in
practice. Some studies also incorporate MSE/RMSE to measure their model performance.
Warshaw and Rodden (2012) display correlation and MAE between state wide estimates
and ground truth in a single graph by faceting it. Hence, we make a like-wise plot
with a slight modiﬁcation in the correlation (Figure 3.6). The current practices display
correlation as it is. When a graph only displays a single metric, there will be no distortion
of its interpretation. However, the graph would be quite hard to read if we facet MAE
or MSE/RMSE and correlation because the scales are not interpreted in the same way.
For MAE and MSE/RMSE, the lower the value, the better the accuracy. In contrast, a
higher correlation coefﬁcient is more desirable. To make these scales more interpretable
in the following graph, we display 1 −correlation instead so that the interpretation is
unidirectional. We also set the free “scale” so that the consistency of performance of
estimates by subpopulation could be examined. Setting the display this way applies the
cognitive principle of best graphical practice as stated in Vanderplas, Cook, and Hofmann
(2020), in which data is better presented in a way that allows the reader to compare more
accurately.
From Figure 3.6 suggests that Native American and All Other race categories are consis-
tently estimated to have a higher MAD and lower correlation with the baseline model. It
is sensible because the baseline model collapses these categories as one covariate. This
ﬁgure also illustrates how model visualisation answers whether the model is uniformly
good or it is only ﬁt for speciﬁc regions, in this case, race categories (Wickham, Cook, and
Hofmann, 2015).
In addition to the metrics displayed in Figure 3.6, we also propose alternative metrics that
do not exist in the reviewed articles, namely the length of the error bar, in this case, is
the 95% credible interval. It is obtained by subtracting the 2.5% quantile from the 97.5%
quantile of the estimates. The idea is that there is a bias-variance trade-off in MRP, and
metrics, such as MAE, only take bias into account. Therefore, in Figure 3.7, we display
the difference and ratio between the credible interval length of the model with more race
42


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
Mean Absolute Difference
Root Mean Square Difference
1 − correlation
0.000
0.020
0.040
0.060
0.000
0.020
0.040
0.060
0.00000
0.00010
0.00020
0.00030
0.00040
0.00050
White
Asian
Black
Hispanic
All Other
Statewide
Native American
Black
Asian
Hispanic
White
Statewide
All Other
Native American
Black
Asian
Hispanic
White
Statewide
All Other
Native American
Values
Race categories
Model with more race categories compared to the baseline model
Metrics by race categories
Figure 3.6: Metrics of model with more race categories. This ﬁgure in only an illustration as it uses
the benchmark is the baseline model, not the ground truth. Each panel shows different
metrics (Correlation, Root Mean Square Deviance, and Mean Absolute Difference).
The statewide categories means the state-wise metrics regardless of the race categories.
Native American and All Other are the population subset with the biggest difference
to the baseline model.
43


---

CHAPTER 3. CASE STUDY: APPLICATION OF MRP IN PRESIDENTIAL VOTING ESTIMATION
CI length difference
CI length ratio
0.00
0.01
0.02
0.03
0.04
0.0
0.5
1.0
1.5
Hispanic
Black
White
All Other
Asian
Native American
Hispanic
White
Black
All Other
Asian
Native American
Values
Race categories
Model with more race categories compared to the baseline model
Comparison of credible interval
Figure 3.7: Credible interval length comparison between the model with more race categories and
the baseline model. The left panel displays the mean of length difference, while the
right panel display the mean of credible interval ratio. The credible interval length of
Native Americans on model with more race categories is 1.5 wider than the baseline
model.
categories and the baseline model. This measure will compare the variability of two model
ﬁts. If the value of credible interval length difference is near zero, then the variability of
two model ﬁts is pretty much the same. A ratio near to 1 could be interpreted in the same
way.
Figure 3.7 shows that the estimated interval of Trump’s vote share in Native American
categories is 1.5 wider compared to the baseline model, while other race categories gener-
ally have the same length of the credible interval with the baseline model. Hence, using
this type of graph, we can sumarise that Native Americans’ Trump’s vote share estimate
might be more uncertain when compared to other other race categories.
To sum, this demonstration shows that graphical display can help us to understand the
model better. For example, the graphs have shown us that the difference in covariates or
model speciﬁcation could result in reasonably different estimates.
44


---

Chapter 4
Conclusion
Graphical displays are essential to explore and understand data and model ﬁts. They
have been widely used to communicate and diagnose MRP models. However, there have
been few studies formally investigating the use of visualisation within an MRP context.
Therefore, in this study, we conduct a systematic literature review to understand the
current practice in MRP visualisation. In addition, we perform a case study using the
Cooperative and Congressional Election Study (CCES) to demonstrate the implication of
current visualisation practices and explore the alternatives and possible improvements.
We ﬁnd that the choropleth map is the most frequently used visualisation to communicate
MRP estimates. However, it is problematic as it often hinders the information in small
geographic areas and does not consider the uncertainty of estimates. Instead, we explore
alternatives to display state-wise estimates using a dot plot with an error bar. Even
though it is important to show estimate uncertainty, in our literature review, we ﬁnd
few plots actually displayed it. We propose some alternatives to display uncertainty, for
example, using a violin plot. This study also demonstrates how graphs have aided us
in understanding how methods and modeling choices affect the estimates. We also use
credible interval length to illustrate the bias-variance trade-off.
Naturally, this study has some limitations. In the CCES case study, none of the MRP models
perform as well as the weighted estimates. However, this allowed us to demonstrate the
use of visualisation to compare models that had different types of errors (such as bias
45


---

CHAPTER 4. CONCLUSION
or variance). Future work could compare the use of the visualisation proposed with an
accurate model.
Another limitation is this study only explores alternatives to MRP visualisation in a case
study. While this was useful for this study because it helped us to see the differences
between visualisations, it does not conclusively provide evidence these alternatives can
communicate more effectively and enhance interpretability. To get evidence of this, future
work should employ careful experimentation. One example of this would be showing
different types of graphs to people and seeing which aids the most accurate interpretation.
This study has provided empirical evidence on how visualisation has been performed
in MRP research. One use of these ﬁndings is as a starting point to continue to explore
alternative visualisations, such as those proposed in Chapter 3. Another use is to provide
inspiration for MRP users in their own work and research. Finally, this work highlights
the importance of including uncertainty which was not being included in practice.
46


---

Appendix A
Appendix
A.1 Supplementary Material
All of the codes used to conduct the analysis and produce the report is available in this
Github repository. Particularly, the code for data wrangling and preparation can be found
here, and the code for MRP preparation and visualisation can be found here and here,
respectively.
A.2 Terms description
There are some terms we used in Section {com-prac} that the readers might ﬁnd unfamiliar
with, especially in Figure 2.4, Figure 2.5, and Figure 2.6. Hence Table A.1 displays the
description of those terms.
47


---

APPENDIX A. APPENDIX
Table A.1: Terms description used in Systematic Literature Review result
Term
Description
dot plot
Data is displayed by point/dot, one of the axis is categorical variable.
scatter plot
Data is diplayed by point/dot, both x and y-axis are numeric.
choropleth map
Thematic map coloured by the proportion of statistical variable it
represents.
bar plot
Data is displayed by rectangular bar, one of the axis is categorical
variable.
histogram
Similar to bar plot but number are grouped into ranges.
density plot
Distribution of numerical variable, the y-axis is the kernel density
estimates.
other types
Other plot types found in the reviewed articles, but the number is too
few to be categorised as one category (boxplot, heatmap, bubble plot,
and logit curve)
case
The response variable that is estimated. It sometimes displayed as
faceted plot, in which each panel represents different
outcome/response variable. For example, a graph contains 2 facets,
A and B are the MRP estimates for opinion regarding same-sex
marriage and abortion, respectively. Hence, A and B are considered
as case.
small area
Estimates of subpopulation, geographically or demographically, for
example estimates by state, county, gender, age group, education
level, and religion. In some plots, it could also be another variable
associates with the MRP estimates. For example, if MRP estimates
used as predictor for another response variable and there is a
visualisation display their relationship, then this variable is
considered as small area.
A.3 Proportion of observations by states
The following plots show the percentage of observations by state in CCES and ACS,
respectively.
48


---

APPENDIX A. APPENDIX
Wyoming
Alaska
North Dakota
Vermont
South Dakota
District of Columbia
Montana
Hawaii
Rhode Island
Delaware
Idaho
Maine
Nebraska
New Hampshire
New Mexico
Mississippi
West Virginia
Utah
Arkansas
Kansas
Oklahoma
Iowa
Louisiana
Nevada
Connecticut
Alabama
South Carolina
Kentucky
Colorado
Oregon
Minnesota
Maryland
Tennessee
Missouri
Wisconsin
Indiana
Massachusetts
Washington
Arizona
New Jersey
North Carolina
Virginia
Georgia
Michigan
Illinois
Ohio
Pennsylvania
New York
Texas
Florida
California
0.0
2.5
5.0
7.5
Percentage
State
Figure A.1: Distribution of observation in CCES data by state. The horizontal axis represents the
percentage of the observations and the vertical axis represents the state ordered from
the largest to lowest percentage of observations.
49


---

APPENDIX A. APPENDIX
Wyoming
Vermont
Alaska
District of Columbia
North Dakota
Delaware
South Dakota
Montana
Rhode Island
Maine
New Hampshire
Hawaii
Idaho
West Virginia
New Mexico
Nebraska
Nevada
Kansas
Mississippi
Arkansas
Utah
Iowa
Connecticut
Oklahoma
Oregon
Louisiana
Kentucky
Alabama
South Carolina
Colorado
Minnesota
Wisconsin
Maryland
Missouri
Tennessee
Indiana
Arizona
Massachusetts
Washington
Virginia
New Jersey
Georgia
Michigan
North Carolina
Ohio
Illinois
Pennsylvania
New York
Florida
Texas
California
0.0
2.5
5.0
7.5
10.0
Percentage
State
Figure A.2: Distribution of observation in ACS data by state. The horizontal axis represents the
percentage of the observations and the vertical axis represents the state ordered from
the largest to lowest percentage of observations.
50


---

APPENDIX A. APPENDIX
A.4 Additional Graphs
The following plots represent metrics and 95% credible interval visualisation as done in
Section 3.4.2.
Education
Figure A.3 shows the metrics and Figure A.4 shows the 95% comparison of credible
interval length based on education level.
Mean Absolute Difference
Root Mean Square Difference
1 − correlation
0.000
0.040
0.080
0.120
0.000
0.040
0.080
0.120
0.0000
0.0050
0.0100
0.0150
Statewide
Some College
4−Year
HS or Less
Post−Grad
Statewide
Some College
4−Year
HS or Less
Post−Grad
Statewide
Some College
4−Year
HS or Less
Post−Grad
Values
Education levels
Model with additional predictor (education) compared to base model
Estimation performance criteria by education level
Figure A.3: Metrics of the model with edication as additional covariate. The benchmark is the
baseline model, not the ground truth. Metrics of High school or less and Post-graduate
categories are consistently have the higher deviance to the baseline model.
51


---

APPENDIX A. APPENDIX
CI length difference
CI length ratio
−0.0050 −0.0025
0.0000
0.0025
0.0050
0.0
0.3
0.6
0.9
Post−Grad
4−Year
Some College
HS or Less
Post−Grad
4−Year
Some College
HS or Less
Values
Education level
Model with education level compared to base model
Comparison of credible interval
Figure A.4: The comparison of the 95 percent credible interval length between model with educa-
tion as additional covariate and the baseline model by education levels. The credible
interval of bigger model for Post-graduate category is slightly narrower compared to
the baseline model.
Age (The estimation using the model with education as additional covariate)
Figure A.5 shows the metrics and Figure A.6 shows the 95% comparison of credible
interval length based on age group (the comparison is between the model with education
as additonal covariate and the baseline model).
52


---

APPENDIX A. APPENDIX
Mean Absolute Difference
Root Mean Square Difference
1 − correlation
0.000
0.010
0.020
0.030
0.000
0.010
0.020
0.030
0.0000
0.0030
0.0060
0.0090
0.0120
65 years and over
45 to 64 years
Statewide
35 to 44 years
18 to 24 years
25 to 34 years
65 years and over
45 to 64 years
Statewide
18 to 24 years
35 to 44 years
25 to 34 years
65 years and over
45 to 64 years
Statewide
18 to 24 years
35 to 44 years
25 to 34 years
Values
Age group
Model with additional predictor (education) compared to the base mod
Metrics by age group
Figure A.5: Metrics of the model with education as additional covariate. The benchmark is the
baseline model, not the ground truth.
Age (The estimation using the model with more race categories)
Figure A.7 shows the metrics and Figure A.8 shows the 95% comparison of credible
interval length based on age group (the comparison is between the model with more race
categories and the baseline model).
53


---

APPENDIX A. APPENDIX
CI length difference
CI length ratio
−0.002
0.000
0.002
0.00
0.25
0.50
0.75
1.00
65 years and over
45 to 64 years
35 to 44 years
18 to 24 years
25 to 34 years
65 years and over
45 to 64 years
35 to 44 years
18 to 24 years
25 to 34 years
Values
Age group
Model with education level as predictor compared to base model
Comparison of credible interval length
Figure A.6: The comparison of the 95 percent credible interval length between model with educa-
tion as additional covariate and the baseline model by education levels. The lenght of
credible interval between the two model ﬁts is pretty much the same.
54


---

APPENDIX A. APPENDIX
Mean Absolute Difference
Root Mean Square Difference
1 − correlation
0.00000
0.00025
0.00050
0.00075
0.00100
0.00125
0.00000
0.00050
0.00100
0.00150
0.00200
0.00000
0.00010
0.00020
0.00030
0.00040
0.00050
65 years and over
45 to 64 years
Statewide
35 to 44 years
18 to 24 years
25 to 34 years
65 years and over
45 to 64 years
Statewide
25 to 34 years
35 to 44 years
18 to 24 years
65 years and over
Statewide
45 to 64 years
25 to 34 years
35 to 44 years
18 to 24 years
Values
Age levels
Model with more race caegories compared to the base model
Metrics by age level
Figure A.7: Metrics of the model with more race categories. The benchmark is the baseline model,
not the ground truth.
55


---

APPENDIX A. APPENDIX
CI length difference
CI length ratio
0e+00
5e−04
0.00
0.25
0.50
0.75
1.00
65 years and over
45 to 64 years
35 to 44 years
25 to 34 years
18 to 24 years
65 years and over
45 to 64 years
35 to 44 years
25 to 34 years
18 to 24 years
Values
Age group
Model with more race categories compared to base model
Comparison of credible interval length
Figure A.8: The comparison of the 95 percent credible interval length between model with more
race categories and the baseline model by education levels. The lenght of credible
interval between the two model ﬁts is pretty much the same.
56


---

Bibliography
Ansolabehere, S and BF Schaffner (2017). CCES Common Content, 2016. Version V4. https:
//doi.org/10.7910/DVN/GDF6Z0.
Aphalo, PJ (2021). ggpmisc: Miscellaneous Extensions to ’ggplot2’. R package version 0.4.3.
https://CRAN.R-project.org/package=ggpmisc.
Botchkarev, A (2019). A New Typology Design of Performance Metrics to Measure Errors
in Machine Learning Regression Algorithms. eng. Interdisciplinary journal of information,
knowledge, and management 14, 45–76.
Brown University Library (2021). Scientiﬁc Literature Review Resources and Services. https:
//libguides.brown.edu/Reviews/types.
Bürkner, PC (2018). Advanced Bayesian Multilevel Modeling with the R Package brms.
The R Journal 10(1), 395–411.
Chai, T and RR Draxler (2014). Root mean square error (RMSE) or mean absolute error
(MAE)? – Arguments against avoiding RMSE in the literature. eng. Geoscientiﬁc model
development 7(3), 1247–1250.
Chambers, JM (1983). Graphical methods for data analysis. eng. The Wadsworth statis-
tics/probability series. Belmont, Calif. : Boston: Wadsworth International Group ;
Duxbury Press.
Cleveland, WS (1985). The elements of graphing data. eng. Monterey, Calif.: Wadsworth
Advanced Books and Software.
Csardi, G and T Nepusz (2006). The igraph software package for complex network research.
InterJournal Complex Systems, 1695.
Displayr (2021). ﬂipPlots: Creates Plots. R package version 1.3.5.
57


---

BIBLIOGRAPHY
Dowle, M and A Srinivasan (2021). data.table: Extension of ‘data.frame‘. R package version
1.14.0. https://CRAN.R-project.org/package=data.table.
Enns, PK and J Koch (2013). Public Opinion in the U.S. States: 1956 to 2010. eng. State
politics and policy quarterly 13(3), 349–372.
Eun Kim, S and J Urpelainen (2018). Environmental public opinion in U.S. states, 1973-2012.
eng. Environmental politics 27(1), 89–114.
Few, S (2008). Practical rules for using color in charts - GitHub Pages. https://nbisweden.
github.io/Rcourse/files/rules_for_using_color.pdf.
Firke, S (2020). janitor: Simple Tools for Examining and Cleaning Dirty Data. R package version
2.0.1. https://CRAN.R-project.org/package=janitor.
Gabry, J and R ˇCešnovar (2021). cmdstanr: R Interface to ’CmdStan’. https://mc-
stan.org/cmdstanr, https://discourse.mc-stan.org.
Gao, Y, L Kennedy, D Simpson, and A Gelman (2021). Improving Multilevel Regression
and Poststratiﬁcation with Structured Priors. eng. Bayesian analysis 1(1).
Gelman, A (2007). Struggles with Survey Weighting and Regression Modeling. eng. Statis-
tical science 22(2), 153–164.
Gelman, A (2014). How Bayesian Analysis Cracked the Red-State, Blue-State Problem. eng.
Statistical science 29(1), 26–35.
Gelman, A and TC Little (1997). Poststratiﬁcation Into Many Categories Using Hierarchical
Logistic Regression.
Gelman, A and A Unwin (2013). Infovis and Statistical Graphics: Different Goals, Different
Looks. eng. Journal of computational and graphical statistics 22(1), 2–28.
Ghitza, Y and A Gelman (2013). Deep Interactions with MRP: Election Turnout and Voting
Patterns Among Small Electoral Subgroups: DEEP INTERACTIONS WITH MRP. eng.
American journal of political science 57(3), 762–776.
Green, S, JP Higgins, P Alderson, M Clarke, CD Mulrow, and AD Oxman (2008). “Intro-
duction”. In: Cochrane Handbook for Systematic Reviews of Interventions. John Wiley &
Sons, Ltd. Chap. 1, pp. 1–9. eprint: https://onlinelibrary.wiley.com/doi/pdf/
10.1002/9780470712184.ch1. https://onlinelibrary.wiley.com/doi/abs/10.
1002/9780470712184.ch1.
58


---

BIBLIOGRAPHY
Haddaway, NR, CC Pritchard, and LA McGuinness (2021). PRISMA2020: R package and
ShinyApp for producing PRISMA 2020 compliant ﬂow diagrams (Version 0.0.2).
Hamner, B and M Frasco (2018). Metrics: Evaluation Metrics for Machine Learning. R package
version 0.1.4. https://CRAN.R-project.org/package=Metrics.
Hanretty, C (2020). An Introduction to Multilevel Regression and Post-Stratiﬁcation for
Estimating Constituency Opinion. Political Studies Review 18(4), 630–645. eprint: https:
//doi.org/10.1177/1478929919864773.
Henry, L, H Wickham, and W Chang (2020). ggstance: Horizontal ’ggplot2’ Components. R
package version 0.3.5. https://CRAN.R-project.org/package=ggstance.
Hullman, J, X Qiao, M Correll, A Kale, and M Kay (2019). In Pursuit of Error: A Survey
of Uncertainty Visualization Evaluation. eng. IEEE transactions on visualization and
computer graphics 25(1), 903–913.
Hyndman, R (2020). MonashEBSTemplates: Monash EBS Rmarkdown Templates. R package
version 0.2.
Kennedy, Gabry, Amaliah, Alexander (2021). mrpkit: Multilevel Regression with Post-
Stratiﬁcation. R package version 0.1.0.
Kiewiet de Jonge, CP, G Langer, and S Sinozich (2018). Predicting State Presidential
Election Results Using National Tracking Polls and Multilevel Regression with Post-
stratiﬁcation (MRP). eng. Public opinion quarterly 82(3), 419–446.
Kuriwaki, S (2020). ddi: The Data Defect Index for Samples that May not be IID. R package
version 0.1.0. https://CRAN.R-project.org/package=ddi.
Kuriwaki, S (2021a). ccesMRPprep: Functions and Data to Prepare CCES data for MRP. R
package version 0.1.8.900. https://www.github.com/kuriwaki/ccesMRPprep.
Kuriwaki, S (2021b). “The Swing Voter Paradox: Electoral Politics in a Nationalized Era”.
PhD thesis. Cambridge MA.
Lauderdale, BE, D Bailey, J Blumenau, and D Rivers (2020). Model-based pre-election
polling for national and sub-national outcomes in the US and UK. eng. International
journal of forecasting 36(2), 399–413.
Lei, R, A Gelman, and Y Ghitza (2017). The 2008 Election: A Preregistered Replication
Analysis. eng. Statistics and Public Policy 4(1), 1–8.
59


---

BIBLIOGRAPHY
Linnenluecke, MK, M Marrone, and AK Singh (2020). Conducting systematic literature
reviews and bibliometric analyses. eng. Australian journal of management 45(2), 175–194.
Lumley, T (2010). Complex Surveys: A Guide to Analysis Using R: A Guide to Analysis Using R.
John Wiley and Sons.
Makela, S, Y Si, and A Gelman (2017). “Graphical Visualization of Polling Results”. In:
The Oxford Handbook on Polling and Polling Methods. Ed. by L Atkeson and M Alvarez.
Oxford UK: Oxford University Press.
McCartan, C (2021). wacolors: Colorblind-Friendly Palettes from Washington State. R package
version 0.2.1. https://github.com/CoryMcCartan/wacolors.
Meng, XL (2018). Statistical paradises and paradoxes in big data (I): Law of large popula-
tions, big data paradox, and the 2016 US presidential election. eng. The annals of applied
statistics 12(2).
Midway, SR (2020). Principles of Effective Data Visualization. Patterns 1(9), 100141.
Park, DK, A Gelman, and J Bafumi (2004). Bayesian Multilevel Estimation with Post-
stratiﬁcation: State-Level Estimates from National Polls. eng. Political analysis 12(4),
375–385.
Pedersen, TL (2020). patchwork: The Composer of Plots. R package version 1.0.1. https:
//CRAN.R-project.org/package=patchwork.
R Core Team (2020). R: A Language and Environment for Statistical Computing. R Foundation
for Statistical Computing. Vienna, Austria. https://www.R-project.org/.
Schneider, SK and WG Jacoby (2017). “Graphical Displays for Public Opinion Research”.
In: The Oxford Handbook on Polling and Polling Methods. Ed. by L Atkeson and M Alvarez.
Oxford UK: Oxford University Press.
Schweizer, ML and R Nair (2017). A practical guide to systematic literature reviews
and meta-analyses in infection prevention: Planning, challenges, and execution. eng.
American journal of infection control 45(11), 1292–1294.
Stan Development Team (2020). Stan Modeling Language Users Guide and Reference Manual.
http://mc-stan.org/.
Strochak, S, K Ueyama, and A Williams (2021). urbnmapr: State and county shapeﬁles in sf and
tibble format. R package version 0.0.0.9002. https://github.com/UrbanInstitute/
urbnmapr.
60


---

BIBLIOGRAPHY
Tukey, JW (1993). Graphic Comparisons of Several Linked Aspects: Alternatives and
Suggested Principles. Journal of Computational and Graphical Statistics 2(1), 1–33. eprint:
https://www.tandfonline.com/doi/pdf/10.1080/10618600.1993.10474595.
U.S. Census Bureau (2016). American Community Survey 2015: ACS 1-Year PUMS Files.
https://www2.census.gov/programs-surveys/acs/tech_docs/pums/ACS2015_
PUMS_README.pdf.
U.S. Census Bureau (2021a). About the American Community Survey. https://www.census.
gov/programs-surveys/acs/about.html.
U.S. Census Bureau (2021b). American Community Survey: Sample Size and Data Quality.
https://www.census.gov/acs/www/methodology/sample- size- and- data-
quality/.
U.S. Census Bureau (2021c). The American Community Survey Public Use Microdata Sample,
2015-2017. https://www.census.gov/programs-surveys/acs/microdata/.
Vanderplas, S, D Cook, and H Hofmann (2020). Testing Statistical Charts: What Makes a
Good Graph? Annual Review of Statistics and Its Application 7(1), 61–88.
Wang, W, D Rothschild, S Goel, and A Gelman (2015). Forecasting elections with non-
representative polls. eng. International journal of forecasting 31(3), 980–991.
Warshaw, C and J Rodden (2012). How Should We Measure District-Level Public Opinion
on Individual Issues? eng. The Journal of politics 74(1), 203–219.
Wickham, H (2010). A layered grammar of graphics. Journal of Computational and Graphical
Statistics 19(1), 3–28.
Wickham, H (2013). “Statistical Graphics”. In: Encyclopedia of Environmetrics. American
Cancer Society. eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/
9780470057339.vnn164. https://onlinelibrary.wiley.com/doi/abs/10.1002/
9780470057339.vnn164.
Wickham, H (2016). ggplot2: Elegant Graphics for Data Analysis. Springer-Verlag New York.
https://ggplot2.tidyverse.org.
Wickham, H (2020). forcats: Tools for Working with Categorical Variables (Factors). R package
version 0.5.0. https://CRAN.R-project.org/package=forcats.
Wickham, H, M Averick, J Bryan, W Chang, LD McGowan, R François, G Grolemund,
A Hayes, L Henry, J Hester, M Kuhn, TL Pedersen, E Miller, SM Bache, K Müller,
61


---

BIBLIOGRAPHY
J Ooms, D Robinson, DP Seidel, V Spinu, K Takahashi, D Vaughan, C Wilke, K Woo,
and H Yutani (2019). Welcome to the tidyverse. Journal of Open Source Software 4(43),
1686.
Wickham, H, D Cook, and H Hofmann (2015). Visualizing statistical models: Removing
the blindfold. eng. Statistical analysis and data mining 8(4), 203–225.
Wickham, H and D Seidel (2020). scales: Scale Functions for Visualization. R package version
1.1.1. https://CRAN.R-project.org/package=scales.
Willmott, C and K Matsuura (2005). Advantages of the mean absolute error (MAE) over
the root mean square error (RMSE) in assessing average model performance. eng.
Climate research 30(1), 79–82.
Xie, Y (2014). “knitr: A Comprehensive Tool for Reproducible Research in R”. In: Implement-
ing Reproducible Computational Research. Ed. by V Stodden, F Leisch, and RD Peng. ISBN
978-1466561595. Chapman and Hall/CRC. http://www.crcpress.com/product/
isbn/9781466561595.
Xie, Y, C Dervieux, and E Riederer (2020). R Markdown Cookbook. ISBN 9780367563837.
Boca Raton, Florida: Chapman and Hall/CRC. https://bookdown.org/yihui/
rmarkdown-cookbook.
Zhu, H (2021). kableExtra: Construct Complex Table with ’kable’ and Pipe Syntax. R package
version 1.3.4. https://CRAN.R-project.org/package=kableExtra.
62
