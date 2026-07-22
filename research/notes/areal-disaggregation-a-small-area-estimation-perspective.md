---
title: 'Areal Disaggregation: A Small Area Estimation Perspective∗'
id: areal-disaggregation-a-small-area-estimation-perspective
tags:
- areal-disaggregation
- mrp
- modele-bayesien
- geo-electoral-crosswalk
created: '2026-07-21T18:30:58.599269Z'
updated: '2026-07-21T18:39:17.726712Z'
source: https://arxiv.org/pdf/2603.04246
source_domain: arxiv.org
fetched_at: '2026-07-21T18:30:58.598958Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Wu, Lindgren & Hanson (2026, arXiv:2603.04246) proposent un cadre bayésien
  à un seul niveau pour la ''small area estimation'' (SAE) par désagrégation aréale
  : produire des estimations à maille fine (ex. district) à partir de données d''enquête
  publiées seulement à une échelle grossière (ex. comté). Le modèle définit un champ
  spatial latent continu (via SPDE/inlabru, extension du modèle géostatistique de
  Lindgren et al. 2011) à la résolution cible, puis relie ce champ aux observations
  agrégées par une étape d''agrégation explicite (moyenne pondérée par population
  des sous-zones), ce qui propage correctement l''incertitude — contrairement au dasymetric
  mapping classique qui traite les totaux agrégés comme fixes et ignore l''erreur
  d''échantillonnage. Le papier distingue 3 grandes familles de désagrégation spatiale
  : (1) dasymetric mapping (LandScan, WorldPop — covariables ancillaires comme l''occupation
  du sol), adapté aux comptages stables mais pas aux données d''enquête bruitées ;
  (2) microsimulation spatiale, parallèle du MRP (multilevel regression with poststratification)
  — modélise par groupe démographique puis redistribue via une population synthétique
  ; (3) modèles géostatistiques à champ latent continu (SPDE), la classe dans laquelle
  s''inscrit leur propre méthode. Application empirique : estimations de fécondité
  générale par district à partir de la Kenya DHS 2022 (données GPS individuelles)
  et désagrégation comté→district d''indicateurs de travail domestique non rémunéré
  et d''usage des médias à partir de la Kenya Time Use Survey 2021 (données publiées
  seulement au niveau comté). Étend le modèle area-level de Fay–Herriot (1979) au
  cas de désagrégation. Pertinence directe pour le problème des bureaux de vote français
  : leur cadre de désagrégation avec agrégation explicite et incertitude bayésienne
  est la contrepartie méthodologique ''sérieuse'' du problème de crosswalk quand les
  mailles électorales changent d''un scrutin à l''autre et qu''on veut projeter à
  une maille plus fine que celle disponible.'
raw_file: raw/areal-disaggregation-a-small-area-estimation-perspective.pdf
---

Areal Disaggregation: A Small Area Estimation Perspective∗
by Yunhan Wu1, Finn Lindgren2 and Heidi A. Hanson1
1Oak Ridge National Laboratory, Oak Ridge, TN, 37830, USA
2School of Mathematics and Maxwell Institute of Mathematical Sciences,
University of Edinburgh, Edinburgh, UK
Abstract
Producing reliable estimates of health and demographic indicators at fine areal scales is crucial
for examining heterogeneity and supporting localized health policy. However, many surveys release
outcomes only at coarser administrative levels, thereby limiting their relevance for decision-making.
We propose a fully Bayesian, single-stage spatial modeling framework for area-level disaggregation
that generates fine-scale estimates of indicators directly from coarsely aggregated survey data.
By defining a latent spatial process at the target resolution and linking it to observed outcomes
through an aggregation step, the framework adopts small-area estimation techniques while incor-
porating covariates and delivering coherent uncertainty quantification. The proposed methods are
implemented with inlabru to achieve computational efficiency. We evaluate performance through
a simulation study of general fertility rates in Kenya to demonstrate the models’ ability to recover
fine-scale variation across diverse data-generating scenarios. We further apply the framework to
two national surveys to produce district-level fertility estimates from the 2022 Kenya Demographic
and Health Survey and, more importantly, district-level indicators for unpaid care and domestic
work and mass media usage from the 2021 Kenya Time Use Survey.
Keywords: Small area estimation, Bayesian smoothing, Spatial models, Disaggregation, Survey
statistics
1
Introduction
Small area estimation (SAE) plays an important role in modern public health and epidemiology
in the production of reliable estimates for geographic subpopulations in which direct survey data
are sparse or unavailable. With a growing emphasis on localized planning and addressing health
inequalities, there is a clear demand for estimates of disease burden and health indicators at fine-
areal scales. For example, in low- and middle-income countries (LMICs), this often corresponds
to the district (Admin-2) level, which typically serves as the operational unit for management
decisions and resource allocation. Empirical studies and international initiatives—in particular the
Sustainable Development Goals (SDG) effort—have explicitly called for reporting health indicators
at an area-level granularity (Oosterhof, 2018; Janocha et al., 2021; J¨onsson and Bexell, 2021).
Studies have corroborated these needs across specific indicators, including (but not limited to)
vaccination coverage (Utazi et al., 2021), educational attainment (Delprato et al., 2024; Wu et al.,
2025), fertility (Abate et al., 2024), and child mortality (Wu et al., 2021).
Meeting these needs requires statistical approaches capable of generating robust estimates when
direct survey data are insufficient. Design-based SAE methods, such as the Horvitz-Thompson es-
timator (Horvitz and Thompson, 1952), are limited when handling small sample sizes for many
areas of interest. To address this, model-based SAE methods have become increasingly popular
(Rao and Molina, 2015). Classic area-level models, such as the Fay–Herriot (FH) model (Fay and
∗This manuscript has been authored by UT-Battelle, LLC, under contract DE-AC05-00OR22725 with the US De-
partment of Energy (DOE). The US government retains and the publisher, by accepting the article for publication,
acknowledges that the US government retains a nonexclusive, paid-up, irrevocable, worldwide license to publish or
reproduce the published form of this manuscript, or allow others to do so, for US government purposes. DOE will
provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan
(https://www.energy.gov/doe-public-access-plan).
1
arXiv:2603.04246v1  [stat.ME]  4 Mar 2026


---

Herriot, 1979), and unit-level models, such as the one developed by Battese et al. (1988), allow for
borrowing statistical strength across areas by incorporating auxiliary information, typically from
censuses or administrative records (Pratesi, 2016; Morales et al., 2021; Moretti and Whitworth,
2021).
The Bayesian formulation of these methods comes naturally with uncertainty quantifi-
cation and facilitates hierarchical modeling that incorporates covariates and spatial or temporal
dependence structures.
Despite these advances, SAE frameworks often assume that response data and the target level
of inference are defined at the same geographic resolution. For example, many demographic and
health surveys (DHS) provide GPS coordinates that allow individuals to be assigned to districts
(Admin-2). In many other cases, however, survey outcomes are released only at coarser spatial
scales owing to confidentiality considerations or data collection constraints, whereas policy and
research applications require estimates at finer scales.
Consider the 2021 Kenya Time Use Survey (KTUS) (Kenya National Bureau of Statistics,
2023). The publicly released data are only geo-indexed at the county (Admin-1) level, even though
many key indicators would ideally be mapped at the district scale to guide localized interventions.
This limitation is especially relevant for SDG 5.4.1 (United Nations Statistics Division, 2020),
which tracks the proportion of time spent on unpaid domestic and care work by sex, age, and
location. District-level estimates are essential for uncovering heterogeneity and informing targeted
household welfare and labor policies. Without methodological innovations, however, such coarse
data cannot be leveraged for fine-scale inference.
Although SAE methods are designed to address the challenge of small sample sizes within pre-
defined geographic units, disaggregation methods tackle a different but related problem: generating
predictions at spatial resolutions that are finer than those of the observed (aggregated) data. This
challenge arises across fields ranging from geography, remote sensing, demography, and epidemi-
ology and is referred to under various names, including downscaling, disaggregation, dasymetric
mapping, or super-resolution. Despite differences in framing, these approaches aim to enhance
spatial detail by using auxiliary data and modeling assumptions.
A widely used approach is dasymetric mapping, which redistributes areal data into smaller
zones by using ancillary covariates such as land cover, building density, or remote sensing prox-
ies. Population mapping products such as LandScan (Dobson et al., 2000) and WorldPop (Tatem,
2017), as well as environmental health applications (Requia et al., 2018), are prominent examples.
However, these methods typically treat aggregate totals as fixed and ignore sampling or measure-
ment error. Although effective for stable quantities such as population counts, they are less suited
to outcomes derived from surveys, in which uncertainty must be explicitly propagated. In such
cases, SAE models are better equipped for the task.
Another strategy is spatial microsimulation, which constructs synthetic microdata constrained
to match observed marginals. The approach parallels multilevel regression with poststratification
(MRP)(Park et al., 2004): outcomes are modeled by demographic group and then redistributed via
synthetic population composition. Applications span health, welfare, transport, and demography
(Tanton, 2014; Smith et al., 2021). However, microsimulation faces challenges of computational
scaling, validation, and uncertainty quantification.
A different class of approaches employs geostatistical models to estimate continuously indexed
spatial surfaces, often via the stochastic partial differential equation framework (Lindgren et al.,
2011).
These models link aggregated data to a continuous latent spatial field and are widely
used in disease mapping, including COVID-19 studies (Python et al., 2022).
They provide a
coherent Bayesian framework with uncertainty quantification and are supported by software such
as the disaggregation package in R (Nandi et al., 2023). However, their performance is highly
dependent on high-quality spatial covariates, which are not always predictive of health outcomes.
Moreover, validation at fine resolutions remains challenging because of the lack of ground-truth
data (Arambepola et al., 2020).
Importantly, many of these disaggregation methods do not account for survey design, which is
a core feature of survey data for health and demographic indicators. SAE methods are uniquely
positioned to bridge this gap by combining design-based consistency with model-based flexibility.
Given the limitations of the existing methods and the practical goal of generating reliable area-
level estimates, we formulate a novel area-level SAE approach for spatial disaggregation of health
indicators. Our approach is formulated as a fully Bayesian, single-stage spatial model that defines
a latent process at the target resolution and incorporates information from area-level covariates.
An inherent aggregation step links this latent field to the outcomes observed at coarser scales to
ensure consistency between the observed survey data and the finer level of inference. Although
our motivating examples come from LMIC contexts, the proposed framework is broadly applicable
2


---

across diverse contexts. This formulation allows the framework to accommodate classical SAE
methods, such as the FH and unit-level models, and can also incorporate MRP when demographic
microdata are available.
Computationally, the models are implemented by using inlabru and
related tools to achieve computational efficiency (Bachl et al., 2019; Lindgren et al., 2024; Suen
et al., 2025).
By construction, the framework delivers coherent uncertainty quantification and
enables standard Bayesian inference.
The remainder of this paper is organized as follows. Section 2 describes the methodological
framework: it begins with a review of existing SAE methods and then introduces our proposed area-
level disaggregation models. Section 3 presents a simulation study on general fertility rate (GFR)
in Kenya to evaluate model performance. Sections 4 and 5 apply the framework to two real-world
case studies—the 2022 Kenya DHS and the KTUS. Finally, Section 6 discusses the findings and
their implications.
2
Method
2.1
Overview of SAE Models
This section describes three core classes of methods for SAE: direct estimation, area-level (FH)
models, and unit-level models (Rao and Molina, 2015; Fay and Herriot, 1979; Battese et al., 1988).
These approaches assume that survey data are geo-indexed at the level of interest, which means that
outcomes are observed for sampled individuals in the finer subareas rather than only in aggregated
form. Later in this work, we extend beyond these standard frameworks to introduce our areal
disaggregation approach to address the more challenging case of when data are available only at
coarser geographic levels.
These methods form a natural spectrum: from design-based estimators that rely solely on
the sampling design, to increasingly model-based approaches that trade some design consistency
for greater flexibility in handling sparse data.
In addition to these three approaches, we also
consider MRP (Downes et al., 2018), which can be combined with area-level or unit-level models
to incorporate additional demographic features and align estimates with the population structure.
MRP is an extension that partitions the population into cells defined by demographic variables,
models the outcomes within each cell, and then aggregates predictions with known population
counts.
Consider a finite target population with N individuals living in |I| coarse areas (e.g., Admin-1)
indexed by i = 1, . . . , |I|. Each area i contains a set of finer subareas (e.g., Admin-2), which we
index by j = 1, . . . , |J |. We use i[j] to denote the parent coarser area that contains subarea j.
Within each subarea j, there are Nj individuals indexed by k = 1, . . . , Nj.
Let yjk denote the outcome for individual k in subarea j.
Our methodological framework
focuses on two outcome types of primary interest in SAE for health indicators: binary and Poisson
outcomes.
The binary case (yjk ∈{0, 1}) is common in disease mapping and corresponds to
prevalence estimation.
The Poisson case (yjk ∈{0, 1, 2, . . . }) is appropriate for rare events or
rate-type quantities such as fertility or mortality rates.
Our primary objective is to estimate the prevalence or rate at the subarea level, defined as
µj = 1
Nj
Nj
X
k=1
yjk,
where Nj is the population size of subarea j.
Although not of direct interest, we also define the prevalence or rate at the coarse-area level as
a population-weighted aggregation of its subareas. This formulation motivates the disaggregation
approaches introduced in later sections:
µi =
X
j:i[j]=i
Nj
Ni
µj,
where Ni = P
j:i[j]=i Nj is the population in area i.
An important aspect of SAE is the survey sampling design. Individuals are typically sampled
through complex designs that involve unequal probabilities of selection. For each subarea j, a
sample of size nj is drawn according to the survey design, which we denote as Sj ⊂{yjk : k =
1, . . . , Nj} with |Sj| = nj. For each sampled individual k ∈Sj, the associated design weight wjk
is defined as the inverse of its inclusion probability such that wjk =
1
πjk with πjk = Pr(k ∈Sj).
3


---

Given this setup, we describe three standard approaches for SAE when data are geographically
referenced at the subarea level.
2.1.1
Direct Estimation
Direct estimators use only the sampled data within each subarea and account for the survey design
through weights (Rao and Molina, 2015). A weighted estimator of prevalence in subarea j is given
by (H´ajek, 1971):
ˆµw
j =
P
k∈Sj wjkyjk
P
k∈Sj wjk
.
These estimates are design-consistent and require minimal modeling assumptions, but they of-
ten have large variances when sample sizes are small.
This motivates the use of model-based
approaches, which borrow strength from neighboring regions.
2.1.2
Area-Level Models
Area-level models, or FH models (Fay and Herriot, 1979), extend direct estimation by linking areas
through a hierarchical model. Let ˆµw
j denote the direct estimate of prevalence or rate in subarea
j and define the transformed estimate as
ˆλw
j = g(ˆµw
j ),
Vj = c
var(ˆλw
j ),
where g(·) is the link function or logit and log transformation for prevalence and rates, respectively.
The variance Vj on the transformed scale can be obtained from the design-based variance by using
the Delta method.
The FH model assumes
ˆλw
j | λj ∼N(λj, Vj),
λj = α + x⊤
j β + bj,
(1)
where xj are subarea-level covariates, β are their coefficients, and bj are random effects. The
prevalence or rate in subarea j is then µj = g−1(λj).
To capture spatial dependence in bj, we adopt the BYM2 formulation (Riebler et al., 2016),
which is a reparameterization of Besag-York-Mollie (BYM) (Besag et al., 1991) and decomposes
the random effect into an unstructured independent and identically distributed (IID) term and
a spatially structured intrinsic conditional autoregressive component. The total variance and the
proportion attributable to the structured component are governed by hyperparameters, for which
we specify penalized complexity priors (Simpson et al., 2017). Full details, including the hyperprior
setup, are provided in Section S2 of the supplemental material. We apply the same spatial structure
across all models discussed later.
Smoothing reduces variance by borrowing strength across subareas, but FH models still depend
on stable direct estimates and their variances, which can limit performance when data are very
sparse.
2.1.3
Unit-Level Models
Unit-level SAE models directly use individual outcomes and are typically implemented at the
cluster level in surveys with cluster sampling. For a survey with C clusters, let Yc and nc denote
the number of positive outcomes and the number of sampled individuals in cluster c, respectively.
Depending on the outcome type, the data are modeled as
Yc | µc ∼
(
Binomial(nc, µc),
binary outcomes,
Poisson(ncµc),
count outcomes,
where µc represents the underlying prevalence or rate in cluster c.
The mean structure is specified through a link function:
g(µc) = g(µc[j]) = α + x⊤
j β + bj,
(2)
where µc is the underlying prevalence or rate in cluster c, which we typically assume to be the
same for clusters from the same area. Let c[j] denote the subarea j in which cluster c resides. We
4


---

then have xj as the covariates and bj as a subarea-level random effect (as in the FH model) in
subarea j.
A limitation of unit-level models is that the survey weights are not directly incorporated, which
means that the sampling design is not explicitly accounted for. This becomes especially problematic
in stratified designs, in which ignoring strata such as urban/rural status can yield biased estimates
when the stratification variable is associated with the outcome and there is over- or under-sampling
of strata (Wu and Wakefield, 2024). A viable solution is to include such stratification variables
directly in the mean structure to adjust for their effect and then aggregate strata-specific estimates
to overall estimates.
2.1.4
MRP
MRP provides a principled framework for combining model-based estimation with survey design
information and demographic covariates. For example, suppose we aim to conduct stratification
by demographic groups a ∈A (e.g., age, sex, or urban/rural categories).
We can specify the
hierarchical models in terms of group-specific likelihoods for group-specific means, both for the
FH and unit-level approaches. Outcomes are modeled within poststratification cells defined by
stratifying variables such as urban/rural status and demographic categories.
For the FH model, we use
ˆλw
j,a | λj ∼N(λj,a, Vj,a),
λj,a = α + x⊤
j β + bj + f(a),
with group-specific prevalence or rates obtained by transforming back from the modeling scale:
µj,a = g−1(λj,a).
For the unit-level model, we use
Yc,a | µc,a ∼
(
Binomial(nc,a, µc,a),
binary outcomes,
Poisson(nc,aµc,a),
count outcomes,
g(µc,a) = g(µc[j],a) = α + x⊤
j β + bj + f(a).
The stratification effects, denoted as f(a), are included alongside covariates and spatial ran-
dom effects. When grouping variables are few and categories are limited, fixed effects (and their
interactions) can be modeled directly. However, as the number of groups grows, data within each
cell become sparse. In such settings, hierarchical smoothing can be adopted to stabilize estimates.
In the poststratification stage, predictions are aggregated to areal-overall estimates by using
external population counts, Nj,a, typically from census data, so that estimates reflect the true
demographic composition:
µMRP
j
= 1
Nj
X
a
Nj,a µj,a,
Nj =
X
a
Nj,a.
(3)
Thus, MRP extends either FH or unit-level models by explicitly adjusting for predictive demo-
graphic variables and ensuring that estimates align with population structure. This adjustment
accounts for subarea variability arising from demographic heterogeneity and improves the precision
of small-area estimates.
2.2
Areal Disaggregation
Our proposed methods for areal disaggregation extend beyond the standard SAE framework intro-
duced above. For example, the survey outcomes are geo-indexed only at a coarser level, but the
analytic and policy objectives require estimates at a finer resolution.
To be specific, suppose a survey record’s data {yi, ni} are geo-indexed at the coarser area i, and
the estimation target is the prevalence or rate µj for subareas j nested within i. The estimation
of {µj} cannot be made without additional assumptions or information because the distribution
of outcomes within each coarse area is not identifiable from aggregate data alone.
Our proposed framework addresses this challenge by systematically incorporating auxiliary
sources of information that can inform within-area variation. These sources can be grouped into
three broad categories.
First, spatial structure enables borrowing strength across neighboring
5


---

subareas. By building the proximity matrix at a finer area level, we can extend the spatial pat-
terns in coarser regions to a finer spatial level. Second, covariates ranging from environmental to
demographic indicators from external sources (e.g., satellite data, census data) help explain out-
come variation within coarse areas. Third, MRP improves estimates by aggregating group-specific
estimates with the true population demographic composition such that the heterogeneity in the
demographics can inform the variation in the subareas—even if the group-specific estimates are
the same across subareas.
The following subsections describe the statistical models that perform areal disaggregation by
combining these complementary sources of information.
2.2.1
FH Disaggregation
We first extend the area-level (FH) model for disaggregation.
We start with survey-weighted
direct estimates at coarse area i. Specifically, let ˆλw
i denote the transformed direct estimate for
area i, with design-based variance Vi. Following the setup for an FH model, we assume a Gaussian
distribution:
ˆλw
i | λi ∼N(λi, Vi),
where λi is the latent prevalence or rate in area i.
To link the area-level parameter λi to a latent process defined at a fine spatial level, we construct
a population-weighted aggregation of subarea means:
λi = g(µi) = g

X
j:i[j]=i
Nj
Ni
µj

,
(4)
where Nj is the population of subarea j, Ni = P
j:i[j]=i Nj is the population for coarser area i,
and g(·) is the link function.
The latent process is indexed at the subarea level. Specifically, for each subarea j, we have
g(µj) = α + x⊤
j β + bj,
where the setup for modeling parameters and smoothing structures mirrors the FH model discussed
in Section 2.1.2.
We defer the computational details and implementation aspects of the Bayesian hierarchical
model to Section 2.3.
In particular, the nonlinear aggregation in equation (4) requires special
treatment.
2.2.2
Unit-Level Model Disaggregation
We extend the framework to the unit-level model, in which observations are recorded at clusters,
c, nested within coarse areas, i. Let Yc denote the observed outcome in cluster c with a cluster
size of nc. The objective is to link the cluster-level outcomes that are geo-indexed at the coarser
level i[c] to a latent process defined at finer subareas, j.
In this setting, outcomes within the same cluster are not independently drawn from a single
shared mean but instead exhibit dependence. Because all individuals in cluster c belong to the
same subarea, their outcomes are more alike than if they were sampled independently from the
area mean. This within-cluster similarity inflates variation in the aggregated outcomes, so standard
Poisson or binomial likelihoods underestimate uncertainty. To address this, we adopt overdispersed
marginal sampling models with the negative binomial for count outcomes and the beta-binomial
for binary outcomes:
Yc ∼
(
NegBin(ncµc, ϕ),
count outcomes,
BetaBinomial(nc, µc, ϕ),
binary outcomes,
where ϕ is an overdispersion parameter that captures excess variation induced by within-cluster
dependence.
Following the extension of the FH model, we link observed clusters at coarser area i to the latent
structure indexed at fine subareas. The mean model for clusters residing in area i is expressed as
a population-weighted average of subarea means:
µc = µi[c] =
X
j:i[j]=i
Nj
Ni
µj,
6


---

where Nj is the population of subarea j, and Ni = P
j:i[j]=i Nj is the population of the coarser
area.
At the subarea level, the latent process is modeled through a linear latent field:
g(µj) = α + x⊤
j β + bj,
(5)
where xj are covariates, bj are random effects, and g(·) is the link function. The random effects
bj capture both structured and unstructured spatial variation.
2.2.3
Extension to Incorporate MRP
With the above setup for unit-level and FH disaggregation models, we can naturally incorporate
MRP. This framework allows demographic heterogeneity to inform subarea estimates, even when
outcomes are observed only at coarser geographic levels.
Let the stratification groups be a ∈A. Similar to the MRP from Section 2.1.4, we define the
data model and mean structure by groups.
For the FH model, we set the hierarchal structure as,
ˆλw
j,a | λj,a ∼N(λj,a, Vj,a),
λi,a = g

X
j:i[j]=i
Nj,a
Ni,a
µj,a

,
g(µj,a) = α + x⊤
j β + bj + f(a)
(6)
where Nj,a is the population of group a in subarea j, Ni,a = P
j:i[j]=i Nj,a represents the population
in coarser area i.
Similarly, for the unit-level model, we have
Yc,a | µc,a ∼
(
Binomial(nc,a, µc,a),
binary outcomes,
Poisson(nc,aµc,a),
count outcomes,
µc,a = µc[i],a =
X
j:i[j]=i
Nj,a
Ni,a
µj,a,
g(µc,a) = α + x⊤
j[c]β + bj[c] + f(a).
(7)
Everything follows the standard MRP detailed in Section 2.1.4. We can aggregate back to the
overall estimates by using the same formulation detailed in Eq. (3) because the mean structures
are all defined at fine areas j.
2.3
Model Implementation and Nonlinearity
The integrated nested Laplace approximation (INLA) method implemented via the R-INLA package
(version 25.06.22) is widely used for Bayesian small-area estimation because it provides fast and
accurate approximate inference for latent Gaussian models (LGMs) (Bakka et al., 2018; Rue et al.,
2009; Lindgren and Rue, 2015; Wakefield et al., 2025). For spatial hierarchical models, R-INLA
exploits the sparse precision structure of Gaussian Markov random fields to achieve substantial
computational efficiency and incorporates built-in spatial smoothing priors such as the BYM2
prior (Riebler et al., 2016), which we adopt in our analysis. These features make R-INLA a natural
choice for implementing our modeling framework.
The baseline INLA method assumes a linear predictor of the form η = Au, where u collects
the latent Gaussian components, including fixed effects and both spatial and non-spatial random
effects (e.g., the right-hand side of Eq. (1)). Each observation yk depends on ηk through a possibly
nonlinear link h(·) in the sampling model. In the FH model, h(·) is the identity link because the
transformation of the outcome is applied before the sampling model, whereas for unit-level models,
h(·) = g−1(·). Thus, the only nonlinearity permitted is the link from ηk to the location parameter;
the mapping from u to η must be strictly linear (Rue et al., 2009). Models geo-indexed at fine-
level subareas conform to this constraint and can be implemented directly in R-INLA, as specified
in Eqs. (1) and (2).
In contrast, our disaggregation models violate this requirement because aggregation introduces
nonlinearity. The predictors linked to the sampling model’s location parameter become nonlinear
combinations of the latent Gaussian components.
7


---

To demonstrate this, we start from the latent field in Eq. (5), and the subarea mean is
µj = g−1 α + x⊤
j β + bj

= g−1(uj).
For both the FH and unit-level disaggregation models, the predictors take the form of
˜ηi(u) = g

X
j:i[j]=i
Nj
Ni
µj

= g

X
j:i[j]=i
Nj
Ni
g−1(Auj)

,
(8)
where the nonlinear predictor ˜ηi(u) involves transformations of aggregated predictors1 (e.g., log of
weighted sums of exponentials, logit of weighted sums of expits) and cannot be expressed in linear
form ˜
Au.
To overcome this challenge, we leverage the inlabru package (version 2.13.0.9011) (Lindgren
et al., 2024; Bachl et al., 2019; Lindgren et al., 2025), which extends R-INLA to allow latent
predictors that are nonlinear functions of the latent Gaussian field. In the inlabru formulation,
we express the stacked vector of nonlinear predictors ˜η(u) as a deterministic function of u, as in
Eq. (8). Choosing a linearization point u0, we take a first-order Taylor approximation:
¯η(u) = ˜η(u0) + B (u −u0) = Bu +
˜η(u0) −Bu0

,
where B is the derivative matrix of the nonlinear predictor evaluated at u0. This yields a linearized
version of the original nonlinear predictor with an offset depending on u0.
The exact marginal sampling model is defined by
y | u, θ ∼p(y | ˜η(u), θ) ,
where θ is the hyperparameters. We approximate this by replacing the nonlinear predictor with
its linearization, which gives us
¯p(y | u, θ) = p(y | ¯η(u), θ) ≈p(y | ˜η(u), θ) = ˜p(y | u, θ).
Through this linearization, the nonlinear observation model can be approximated by a standard
LGM that can be fitted with INLA, thereby allowing access to the full suite of INLA-based inference
and posterior summaries.
A key step in the inlabru method is the choice of a suitable linearization point u0. This is
achieved through a fixed point iteration procedure, which updates the linearization point so that it
is consistent with the conditional posterior mode of the linearized model. Starting from an initial
point, the algorithm alternates between applying the INLA method to update the hyperparameters
and computing the conditional posterior mode of the latent field, refining u0 until convergence is
achieved. Full details of this iterative scheme, including the update rules and convergence criteria,
are provided by Lindgren et al. (2024).
3
Simulation
3.1
Overview
We designed a simulation study to assess the performance of spatial disaggregation methods for
estimating the GFR in Kenya. In our data-generating process, individual-level fertility outcomes
are first simulated and geo-referenced at the Admin-2 level (constituency), which serves as the
ground truth. We then replicate the sampling procedure of a DHS to draw survey samples from
this synthetic population. For model fitting, we impose a data restriction: only the geo-indexed
Admin-1 (county) level data are made available, and all Admin-2 identifiers are removed. The
proposed disaggregation method is then applied to infer Admin-2 level GFR estimates from the
Admin-1 aggregates.
Finally, these estimates are compared to the known Admin-2 truths to
quantify the accuracy and reliability of the disaggregation approach.
Throughout, we use the conventional period definition of the GFR as births per 1,000 woman-
years of exposure among women of reproductive age (15–44 years old):
GFR = 1000 ×
X
a∈A
Ba
X
a∈A
Ea/12
,
1A discussion on why an apparently simpler formulation for unit-level models is not compatible with the inlabru
framework is provided in Section S1 of the supplemental material.
8


---

where A = {15–19, 20–24, ..., 40–44} represents age groups, Ba is the total number of live births
in age group a during the reference period, and Ea is the total woman-months of exposure in the
age group a. Division by 12 converts months of exposure to woman-years, and the factor of 1,000
scales the rate to births per 1,000 woman-years. In our simulations, the reference window is the 60
months preceding the survey year, and we target T ⋆= 48 months of mean exposure per woman.
Based on Kenya’s administrative boundaries, in the analysis, we treat Admin-1 as the 47
counties and Admin-2 as the 290 constituencies.
The simulated sample size and stratification
emulate the 2022 Kenya DHS, which is based on the 2019 census as a sampling frame.
3.2
Data Sources, Construction of Master Frame, and Sampling
We align administrative boundary shapefiles with the 2019 Kenya census to construct sociode-
mographic marginals for each Admin-2 unit. The key variables include the proportion of urban
population, the proportion of women with secondary or higher education, and additional area-level
covariates such as average household size and mobile phone access.
Population counts are drawn from WorldPop data (Tatem, 2017). Gridded, age-specific popu-
lation estimates are aggregated to the Admin-2 level to serve as the base population. Additional
raster covariates, such as nighttime lights, health facility access, and vegetation indices are calcu-
lated as population-weighted averages at the Admin-2 level.
To generate the master frame, we adopt the sampling design of the Kenya DHS 2022.
A
synthetic population is created by expanding Admin-2 × age × urbanicity × education cells into
individual records. Enumeration areas, or clusters, are then allocated to strata in proportion to
the female population.
Finally, we mimic the DHS two-stage sampling strategy. Clusters are selected within strata by
using a probability proportional to the size of the population, after which 20 women per cluster
are sampled at random. The resulting inclusion probabilities define the base sampling weights to
ensure that the simulation closely replicates the DHS design. Additional details are provided in
Section S3 of the supplemental material.
3.3
Outcome Generation and Simulation Scenarios
We aim to construct several simulation scenarios that represent potential sources of variability in
subnational outcome estimates. The goal is to start with a simple scenario and then progressively
include additional factors that better approximate real-world data. Specifically, we consider four
scenarios, summarized in Table 1, that differ by their inclusion of observed covariates, unobserved
covariates, area-level independent random effects, and model misspecification.
In the first scenario, the observed covariates can be naturally captured through the disaggre-
gation model. In the second scenario, we simulate a case in which unobserved covariates, which
often exhibit spatial dependence, can be partly accounted for through spatial smoothing that cap-
tures spatially correlated random effects at the Admin-2 level. In the third scenario, we introduce
independent random effects at the Admin-2 level that cannot be identified from data geo-indexed
at the Admin-1 level and therefore cannot be recovered. In the last scenario, we introduce model
misspecification by assigning different coefficient values for urban and rural strata, in contrast to
the global effect estimates assumed in the other models. Although the introduction of an inter-
action term partially reflects reality, we note that the actual complexities are likely greater than
those captured in even our most complex scenario.
To formalize the outcome generation process, let Ec,k denote the exposure during the reference
period for individual k in cluster c. The individual-level birth process is generated independently
as
Yk ∼Poisson(Ec,k µc,k),
where µc,k is the individual fertility rate.
Scenario 1:
In the first scenario, we include only observed covariates.
The log-scale mean
structure for individual k in cluster c located in Admin-2 area j is specified as
log µs1
c,k = αrural I(c ∈rural) + αurban I(c ∈urban)
+ δage(k) + δeduc(k)
+ βXj[k] + ek + ec.
9


---

Table 1: Sources of spatial heterogeneity under four scenarios and the expected ability of disaggrega-
tion models to capture them.
Variation sources
Scenario 1
Scenario 2
Scenario 3
Scenario 4
Recoverable
Observed covariates
✓
✓
✓
✓
✓
Explicitly captured
by fixed effects
Unobserved covariates
(spatially correlated
Admin-2 effects)
✗
✓
✓
✓
❍
Partially captured
by spatial effects
IID Admin-2
random effects
✗
✗
✓
✓
✗
Not recoverable,
purely unstructured
Varying
coefficients
✗
✗
✗
✓
✗
Leads to model
misspecification
This structure incorporates settlement-type intercepts, individual-level covariates (age and educa-
tion), area-level covariates (e.g., nighttime lights, travel time to nearest health facility, household
size), and random effects at the individual and cluster levels. Full parameter specifications for this
and later scenarios are available in Section S3.4 of the supplementary material.
Scenario 2:
The second scenario extends this mean structure by including additional unob-
served covariates at the area level. Specifically,
log(µs2
c,k) = log(µs1
c,k) + βunobsXunobs
j[k]
,
where Xunobs
j[k]
introduces further variation through two unobserved covariates: the vegetation index
and female mobile phone usage, both of which are standardized. These covariates are excluded from
the modeling process, but disaggregation models are expected to partially capture these variations
through spatially correlated Admin-2 effects.
Scenario 3:
In the third scenario, we allow for additional unexplained heterogeneity by intro-
ducing an independent Admin-2 level random effect:
log(µs3
c,k) = log(µs2
c,k) + ej,
ej ∼N(0, σ2
j ).
This captures unstructured residual variation that the disaggregation model cannot explain.
Scenario 4:
The fourth scenario introduces model misspecification by allowing coefficients to
differ between urban and rural areas within the same Admin-2 unit. This specification permits
heterogeneity across urban and rural populations:
log(µs4
c,k) = α(s) + δ(s)
age(k) + δ(s)
educ(k) + β(s)Xj[k] + ek + ec,
where s ∈{urban, rural}.
Although Scenario 4 offers a closer approximation to reality than the earlier scenarios, it might
still underrepresent the complexity of actual data generating processes.
In Scenarios 1 and 2, the synthetic population is generated once and reused across repetitions.
In contrast, for Scenarios 3 and 4, in which the independent Admin-2 level effects can substantially
influence the results, a new synthetic population is generated for each repetition. For each scenario,
we draw repeated samples 500 times to yield 500 distinct datasets. Model fitting and performance
metrics are then calculated based on the average across these 500 datasets.
10


---

Table 2: Summary of models compared in the simulation study.
Model
Configuration
Geo-indexing
level
Specification
FH disagg
Fay–Herriot
disaggregation
model;
no
MRP.
Admin-1
§2.2.1
FH-MRP disagg
Fay–Herriot disaggregation model; MRP
by age and education (no urban/rural).
Admin-1
§2.2.3, Eq.(6)
Unit disagg
Unit-level disaggregation model; stratified
by urban/rural.
Admin-1
§2.2.2
Unit-MRP disagg
Unit-level disaggregation model; MRP by
age, education, and urban/rural.
Admin-1
§2.2.3, Eq.(7)
Direct Admin-2
(benchmark)
Survey-weighted
direct
estimates
at
Admin-2.
Admin-2
S2.1.1
FH Admin-2
(benchmark)
Fay–Herriot
model
fitted
directly
at
Admin-2. With observed covariates.
Admin-2
§2.1.2
3.4
Models Considered and Comparison Metrics
We compare four disaggregation models defined at the Admin-1 level with two benchmark ap-
proaches based on Admin-2 data (Table 2). The disaggregation models are either FH or unit-level,
and each has two variants: with and without MRP. In all cases, the latent structure is defined at
the Admin-2 level. In disaggregation models, latent fields are aggregated to the Admin-1 scale by
using the inlabru framework so that predictions can be linked to the observed data.
The FH disaggregation models use survey-weighted direct estimates at the Admin-1 level and
are modeled on the logit scale. The FH-MRP variant extends this by applying MRP across demo-
graphic groups, although the urban/rural dimension is excluded because of sparse data and because
survey weights already incorporate this stratification. Unit-level models are fitted to cluster-level
outcomes, but the non-MRP specification still stratifies by urban/rural to mitigate the bias de-
scribed earlier. The unit-MRP model also applies MRP by age, education, and urban/rural.
For benchmarking, we include two standard approaches that use data geo-indexed at Admin-2:
direct survey-weighted estimates and an FH model fitted directly at Admin-2.
All models incorporate the same three observed covariates, and all unobserved covariates are
excluded from model fitting. In the non-MRP variants, education is added as an area-level covariate
and measured as the proportion of women with at least secondary education in each Admin-2 region.
We define a set of metrics to systematically evaluate the performance of the model in simulation
scenarios. In the context of spatial disaggregation models, our primary interest lies in assessing the
ability of the models to capture variation within Admin-1 regions rather than focusing solely on
global or cross-regional variation. Specifically, we aim to determine how well the models leverage
covariate information, spatial structures, and demographic composition to capture the relative
ranking and heterogeneity of Admin-2 areas within the same Admin-1 area.
Thus, we first focus on two metrics within-Admin-1: a regression-based R2 and a correlation-
based measure. We denote the true GFR for Admin-2 area j as µj and the corresponding model
prediction as ˆµj. The true GFR for each Admin-1 group is ¯µi =
1
ni
P
j:i[j]=i µj.
Within-Admin-1 regression R2:
For each Admin-1 region, we calculate the sum of squared
errors (SSE) and the within-group total sum of squares (SSTwithin):
SSE =
X
i∈I
X
j:i[j]=i
 µj −ˆµj
2,
SSTwithin =
X
i∈I
X
j:i[j]=i
 µj −¯µi
2.
The within-Admin-1 regression R2 is then calculated as
R2
within-reg = 1 −
SSE
SSTwithin
.
11


---

This measure quantifies the proportion of within-Admin-1 variance in the true outcomes explained
by the model predictions rather than the total variance across all Admin-2.
Within-Admin-1 Pearson correlation:
We use Pearson correlation to assess the rank of
Admin-2 predictions. Within each Admin-1 area between the true and predicted GFR, we have
ri = corr
 µj, ˆµj | i[j] = i

.
The overall metric is obtained by averaging these correlations across all Admin-1 areas followed
by squaring the mean correlation:
rwithin-corr = ¯r =
1
|I|
X
i∈I
ri.
This correlation-based measure emphasizes the rank-order accuracy of predictions within Admin-1
regions.
Uncertainty metrics:
We also evaluate the quality of uncertainty quantification provided by
the models. Three metrics are considered: the average width of predictive intervals; the frequentist
coverage of these intervals; and the interval score (IS), as defined by Gneiting and Raftery (2007).
Let (lj, uj) denote uncertainty intervals from the posterior predictive distribution of ˆµj. Specif-
ically, the lower and upper bounds correspond to the α/2 and 1 −α/2 quantiles, respectively.
Interval quality is assessed using the IS by Gneiting and Raftery (2007), which penalizes both
overly wide intervals and those that fail to include the observed value.
For a set of intervals
{(lij, uij)}, the score is given by
ISα =
1
|J |
X
j∈J
h
uj −lj + α
2 (lj −µj) I
 lj > µj

+ α
2 (µj −uj) I
 uj < µj
i
.
This metric penalizes both overly wide intervals and those that fail to include the observed
value. Lower scores correspond to better model performance.
3.5
Simulation Results
We present the performance of our proposed models and that of the benchmark models across
the four predetermined scenarios. All models are fitted using the same set of observed covariates,
with the exception of direct estimation, which does not incorporate covariates. Figure 1 provides
a summary of the models, and additional details are available in Section S4 of the supplemental
material. In summary, our proposed models consist of the FH and unit-level disaggregation models,
each with and without an MRP extension. These models are based on data geo-indexed at the
Admin-1 level with Admin-2 identifiers removed. The benchmark models are FH models and direct
estimations with data geo-indexed at the Admin-2 level.
Each experiment is repeated 500 times to mitigate the noise introduced by random sampling
variation in the survey process. Metrics are then averaged over the 500 repetitions, and uncertainty
bars are used to illustrate the variability in these metrics.
When comparing the disaggregation models with the benchmark models, a clear trend emerges.
As the scenarios become increasingly complex and closer to real-world conditions, the performance
of the disaggregation models decreases. In the last two scenarios, the FH Admin-2 model outper-
forms the disaggregation approaches. This pattern is consistent with the design of the scenarios.
Moving from Scenario 1 to 4, we sequentially introduce sources of variation that the disaggregation
models are less able to explain: observed covariates, unobserved covariates (representing spatially
correlated effects), IID Admin-2 level random effects, and model specification error. The most
significant turning point occurs with the introduction of IID Admin-2 random effects, which the
benchmark models are able to capture owing to the sufficient resolution of the geo-indexed data. In
contrast, the disaggregation models are unable to produce high-fidelity estimates when restricted
to Admin-1 information.
12


---

Scenario 1
Scenario 2
Scenario 3
Scenario 4
R² (regression)
r (Pearson)
Interval score
50% CI Width
50% CI coverage
FH disagg
FH−MRP disagg
Unit disagg
Unit−MRP disagg
FH (Adm2)
Direct (Adm2)
FH disagg
FH−MRP disagg
Unit disagg
Unit−MRP disagg
FH (Adm2)
Direct (Adm2)
FH disagg
FH−MRP disagg
Unit disagg
Unit−MRP disagg
FH (Adm2)
Direct (Adm2)
FH disagg
FH−MRP disagg
Unit disagg
Unit−MRP disagg
FH (Adm2)
Direct (Adm2)
0.0
0.5
1.0
0.6
0.7
0.8
0.9
1.0
0.01
0.02
0.03
0.04
0.05
0.01
0.02
0.03
0.04
0.05
0.4
0.6
0.8
1.0
Method
Value
Figure 1: Comparison of disaggregation and benchmark models (FH and direct estimates at the
Admin-2 level) across four simulation scenarios and evaluated with within-Admin-1 regression, R2;
Pearson correlation, r; the uncertainty IS; width; and coverage. Scenario 1 includes observed covari-
ates and random effects at the individual and area levels. Scenario 2 expands scenario 1 with the
introduction of two additional area-level measures that are assumed to be unobserved. Scenario 3
expands scenario 2 with the addition of IID Admin-2 level random effects. Scenario 4 is the most
complicated scenario and introduces model misspecification by allowing the coefficients to differ be-
tween urban and rural areas within the same Admin-2 unit.
The weaker performance of the benchmark models in Scenarios 1 and 2 can be explained by
their tendency to fit Admin-2 level independent random effects even though such effects were not
present in those scenarios. This issue is particularly evident in direct estimation, whereas the FH
Admin-2 model benefits from covariates and smoothing that partially stabilize the results. On
the other hand, the exceptionally strong performance of the disaggregation models in Scenarios 1
and 2, with within-Admin-1’s R2 and Pearson’s r close to one, should be interpreted with caution.
These scenarios were chosen to emphasize settings in which disaggregation models are expected to
perform well and provide a clear baseline for evaluating their performance.
Turning to the uncertainty measures, the disaggregation models show increased uncertainty in
Scenarios 3 and 4 once the unidentifiable Admin-2 random effects are introduced. This is expected
because these models are effectively extrapolating from Admin-1 to Admin-2. The tendency toward
slight over-coverage is desirable when extrapolating because it reflects an appropriately conservative
assessment of uncertainty. The IS values are higher in the last two scenarios for the disaggrega-
tion models versus the benchmark models. Again, this reflects the challenges of extrapolation.
Overall, the variability across the 500 repetitions is also larger for the disaggregation models,
thereby demonstrating their sensitivity to random sample variation. This is also expected because
13


---

predictions in these models rely more heavily on the observed data.
Comparisons within the disaggregation models show that unit-level approaches perform slightly
better than FH models across scenarios, although the margin is small. Considering the effect of the
MRP extension, the MRP variants are slightly advantageous in Scenarios 1 and 2 but less effective
in Scenarios 3 and 4.
A plausible explanation is that the MRP variants attempt to attribute
some of the unexplained variation that arises from IID Admin-2 random effects to demographic
covariates, thereby introducing additional variability. For FH models, the MRP extension may
also suffer from ecological bias because the models are fitted at the aggregate level, whereas the
covariates used for post-stratification are at the individual level. This bias can be observed in the
elevated values of the bias metric presented in Section S4. For the unit-level models, however,
post-stratification through MRP also helps counteract potential biases from informative sampling
with respect to demographic variables because the unit-level models proposed cannot incorporate
design weights.
In summary, the results show that the disaggregation models demonstrate reasonable perfor-
mance. They can explain within-Admin-1 variation, as reflected in R2 and Pearson’s r, and their
uncertainty quantification is not substantially worse than that of the benchmark models. At the
same time, the simulations highlight the limitations of disaggregation models when faced with
unidentifiable Admin-2 variation. Based on the findings from the simulation study, we focus on
two models for subsequent real-data applications: the FH model without the MRP extension and
the unit-level model with the MRP extension.
Direct Estimation
FH (Admin−2)
FH disaggregation
Unit disaggregation
GFR
0.1
0.2
0.3
Direct Estimation
FH (Admin−2)
FH disaggregation
Unit disaggregation
Width of 
90% CI
0.1
0.2
Figure 2: Admin-2 level estimates of GFR in Kenya based on DHS 2022 data and obtained from four
models: direct estimation, FH at Admin-2, FH disaggregation, and unit-level disaggregation with
MRP. The upper panel shows point estimates of GFR, and the bottom panel shows the width of the
90% uncertainty intervals.
4
Case Study 1: GFRs in Kenya (DHS 2022)
Our simulation study was designed to mimic the data-generating and sampling process for the
GFR in Kenya based on the 2022 DHS survey. In this case study, we apply the disaggregation
models to the actual DHS 2022 data. Because the survey provides GPS coordinates for clusters,
the data are geo-indexed at the Admin-2 level. We evaluate four models: two benchmark models
that directly use Admin-2 indexing (direct estimation and the FH model with covariates) and two
14


---

disaggregation models that assume only Admin-1 indexing is available (the FH model without MRP
and the unit-level model with MRP). The covariates used are nighttime light intensity, travel time
to the nearest health facility, average household size, mobile phone usage, and secondary school
attainment rate.
The goal is to assess how disaggregation models perform when Admin-2 identifiers are masked,
both relative to the benchmark models and in comparison with each other.
Figure 2 shows that the disaggregation models produce Admin-2 level GFR estimates broadly
consistent with the benchmark models.
Larger differences arise in regions where the Admin-2
FH model estimates that the area-level random effects are greater, which is consistent with the
simulation finding that the disaggregation models do not fully recover these effects by design (more
details are provided in Section S5.1 of the supplemental material).
Taking the Admin-2 FH model as a benchmark, the average within-Admin-1 Pearson correlation
r between disaggregation and benchmark estimates is 0.52 for the FH model and 0.55 for the unit-
level model, suggesting a reasonable level of agreement (correlations across all Admin-2 units exceed
0.9 at the global level). Nevertheless, there is still nontrivial uncertainty for the benchmark model
estimates themselves, and these comparisons should be interpreted with caution.
Generally, uncertainty intervals are wider for the disaggregation models, which is consistent
with the simulation study, given that disaggregation must extrapolate from Admin-1 to Admin-
2.
The benchmark models, in contrast, exhibit much narrower intervals because they directly
exploit Admin-2 information, although such precision would be unattainable under Admin-1-only
indexing.
Overall, the case study shows that disaggregation models can provide Admin-2 level estimates
of GFR with reasonable accuracy when only Admin-1 geo-indexing is available. The trade-off is
larger but appropriately conservative uncertainty intervals.
5
Case Study 2: Indicators from the 2021 KTUS
We now consider a case in which disaggregation methods are essential because the data are geo-
referenced only at a coarse administrative level instead of the target level. Our application uses the
2021 KTUS, which was conducted as a module of the Kenya Continuous Household Survey. Similar
to the DHS, the KTUS followed a two-stage stratified design that used the Kenya 2019 census as
the master frame. Unlike the DHS, the KTUS does not provide GPS coordinates, so individual
records are linked only to Admin-1 areas, making standard Admin-2 analysis impossible. Because
policy and SDG monitoring require finer subnational detail, particularly for indicators such as the
ones we consider below, disaggregation models are the only viable option.
5.1
Unpaid Care or Domestic Work
The first indicator considered is time spent on unpaid care or domestic work, which is central
to SDG target 5.4.1. Respondents reported minutes spent on activities during the previous day,
which we round to half-hour units. We apply negative binomial models with total half-hours for
the day as exposure and compare three approaches: (1) direct estimation at Admin-1; (2) an FH
disaggregation model without MRP; and (3) a unit-level disaggregation model with MRP using age
group and urban/rural status for post-stratification. Covariates include nighttime light intensity,
travel time to the nearest health facility, average household size, and high school attainment rate.
Figure 3 shows the estimated proportion of the day women spend on unpaid care and domestic
work. The results range from about 15% (3.5–4 hours) in some areas to more than 30% (more
than 7 hours) in others. Nairobi and Mombasa yield the lowest estimates, reflecting better access
to services and formal employment, whereas the north and northeast show the highest estimates.
Beyond these broad patterns, the disaggregation models further suggest substantial heterogene-
ity within Admin-1 units. Both disaggregation models highlight specific Admin-2 areas within
Marsabit and Wajir near the Ethiopian border, where women devote more than 30% of their time
to unpaid care or domestic work. The two disaggregation models produce consistent estimates,
with the unit-level model yielding smoother spatial patterns. Uncertainty intervals are wider for
the disaggregation models than for direct Admin-1 estimates, reflecting the extrapolation from
coarse to fine geographical levels. The male-specific results are shown in Figure S5 of the supple-
mental material. Overall, men spend less than 6% of the day (under 1.5 hours) on unpaid care or
domestic work.
To examine gender gaps, we calculate the female-male difference in hours devoted to unpaid
domestic and care work and map the probability that women spend more than four extra hours
15


---

Direct estimation
FH disaggregation
Unit disaggregation
Unpaid care or 
 domestic work 
 (% of day)
15%
20%
25%
30%
Direct estimation
FH disaggregation
Unit disaggregation
Width of 
 90% CI
5%
10%
15%
20%
Figure 3: Estimated proportion of the day that women spend on unpaid care and domestic work from
direct estimation at Admin-1, FH disaggregation, and unit-level disaggregation models. The maps
show both point estimates and the widths of the associated 90% uncertainty intervals.
Admin−1 Gap
Admin−2 Gap
Unpaid work: female−male gap
15%
20%
25%
Exceedance probability
Probability of gap exceeds 4 hrs
25%
50%
75%
Figure 4: Maps of the female-male gap in unpaid care and domestic work and the associated probabil-
ity that the difference exceeds four hours per day. Admin-1 estimates are based on direct estimates,
and Admin-2 estimates are from a unit-level disaggregation model with MRP.
16


---

per day on such activities relative to men (equivalent to 16.7% of the day). These exceedance
probabilities are derived from posterior draws of the unit-level disaggregation model and are shown
in Figure 4. The results reveal a clear spatial pattern: areas in the north and northeast consistently
show probabilities above 75%, indicating strong evidence of large gender gaps. In contrast, the
central highlands and coastal areas (e.g., Mombasa and Kilifi) show much lower probabilities—in
some cases below 25%. Disaggregation reveals finer spatial patterns, with localized hot spots not
visible in aggregated estimates. The male-female gap is particularly pronounced in these regions,
underscoring the need for spatially targeted interventions for progression through SDG target 5.4.1.
5.2
Mass Media Usage
We now consider a binary indicator to demonstrate that the modeling framework also applies to
binary outcomes rather than just rate outcomes (e.g., GFR). In this example, we focus on any
mass media usage, which is defined as whether a respondent spent any time consuming mass
media during the previous day. Mass media refers to communication channels that reach large
audiences, such as radio, television, newspapers, and online news platforms. Mass media usage is
a key indicator of information access and social participation, with strong links to public health
messaging, civic engagement, and progress toward several SDG targets.
The outcome is modeled by using the beta-binomial specification described in Section 2.2.2.
As with the previous case, we compare three approaches: direct estimation at the Admin-1 level,
FH disaggregation and unit-level disaggregation at the Admin-2 level. The covariates used are
nighttime light intensity, high school attendance rate, mobile phone usage, and access to a health
facility.
Figure 5 presents male- and female-specific estimates of the probability of mass media usage
across the three modeling approaches. Across Kenya, men report systematically higher usage than
women. The spatial pattern shows a trend of Admin-2 regions in Nairobi, Mombasa, and other
urban centers having high levels of media use for both sexes, whereas the northern regions show
substantially lower rates. Importantly, the disaggregation models recover the within-Admin-2 het-
erogeneity that the direct Admin-1 estimates cannot capture. Because the indicator is binary and
survey samples have higher variability, uncertainty intervals are wider than in previous analyses.
As shown in Figure S6 of the supplemental material, credible intervals for disaggregation models
reflect this added uncertainty and underscore the need for caution when drawing inferences about
fine-scale differences.
17


---

Female
Direct estimation
FH disaggregation
Unit disaggregation
Male
Any mass media usage
20%
40%
60%
80%
Figure 5: Maps of the female- and male-specific estimates for mass media usage.
18


---

6
Discussion
This work proposed a suite of disaggregation models under the SAE framework to obtain fine-
scale areal estimates when the survey data are available only at coarser administrative levels. The
methods are built upon two standard SAE approaches—the FH model and unit-level models—
and incorporate MRP extensions. This framework is designed to leverage three key sources of
information: area-level covariates, spatial smoothing, and demographic compositions to link coarse
geo-referenced survey data to latent fields defined at the finer target resolution. Computation is
conducted efficiently by using approximate Bayesian inference in inlabru.
The simulation study on GFRs in Kenya mimicked the 2022 DHS and compared disaggregation
models geo-indexed at the Admin-1 level with benchmark models geo-indexed at the Admin-2 level.
The results provide clear evidence of when disaggregation is effective and when its utility is more
limited. When outcome variation is driven by observed covariates or by a mix of observed and
spatially correlated unobserved covariates, the models recover within-Admin-1 heterogeneity at the
Admin-2 level with strong accuracy. Performance declines sharply, however, when unstructured
Admin-2 random effects are introduced or when coefficients vary across strata in ways not accounted
for in the models. Uncertainty intervals for disaggregation models are generally wider, and such
conservativeness is desirable considering the extrapolative nature of the task. The MRP extension
contributes little in terms of predictive power but plays a useful role in the unit-level setting by
incorporating survey design. Overall, disaggregation models perform comparably to benchmarks
when fine-scale geo-indexing is unavailable. Based on the simulation study, two models emerge as
practical choices for real-world application: the FH disaggregation model without MRP and the
unit-level disaggregation model with MRP.
The case studies illustrate the practical value of the proposed methods when applied to real
survey data. In the DHS 2022 case study, in which Admin-2 identifiers were available for validation,
disaggregation models produced estimates largely consistent with benchmark approaches based
on Admin-2 indexing.
In the 2021 KTUS, disaggregation models are the only viable options
because the released data were linked only to Admin-1 areas. In this setting, the models generated
meaningful Admin-2 estimates for key indicators such as unpaid domestic and care work and mass
media usage.
These estimates revealed heterogeneity within counties and highlighted localized
gender gaps that would not have been apparent with direct Admin-1 analysis alone. Together, the
case studies show that disaggregation can provide valuable subnational insights for localized policy
monitoring and SDG reporting, especially where demand for fine-scale estimates is growing. At the
same time, the wider uncertainty intervals of the disaggregated results highlight the importance of
exercising caution when drawing inferences from such estimates.
We conclude with the limitations of our work.
First, disaggregation is fundamentally con-
strained by the information available. Fine-scale unstructured heterogeneity, represented in the
models as area-level IID random effects, cannot be identified from coarsely geo-referenced data.
When such unstructured variation dominates the outcome, disaggregation models are expected to
perform poorly. Although the simulation study considered a range of plausible scenarios, real-world
data-generating processes are likely even more complex. Moreover, for settings in which disaggre-
gation is most relevant, where only coarse geo-indexing is available (e.g., KTUS), direct validation
against finer-resolution data is not possible. For this reason, inferences drawn from disaggregation
should always be interpreted with caution.
Second, disaggregation models place heavier reliance on covariates than traditional SAE meth-
ods applied to sufficiently geo-referenced data. This makes both the choice and the quality of
covariates more crucial. In our study, we treated covariates as fixed inputs without explicitly ac-
counting for their uncertainty. Within this disaggregation framework, covariates are used primarily
for prediction rather than for inferring causal relationships with the outcomes. As noted in the
introduction, the most useful demographic and health covariates typically come from censuses, but
census data are infrequent, and their availability is uncertain, particularly in LMICs.
Finally, there is room for improvement in the modeling specification. For unit-level models, the
most accurate representation of the aggregation process from fine-level latent fields to coarser areas
would be a mixture likelihood, where each unit’s contribution is aggregated by the probability of
belonging to different subareas. However, implementing full Bayesian inference under this spec-
ification is computationally demanding. Our approach uses over-dispersed approximations that
provide the correct mean representation, which is the primary quantity of interest. Although this
approximation may be less accurate in cases of extreme heterogeneity across subareas, there is a
significant gain in computational efficiency provided by the inlabru framework. Additionally, our
simulation results show no evidence of systematic bias or instability from such approximation.
19


---

Acknowledgment
This material is based upon work supported by the US Department of Energy, Office of Science,
Advanced Scientific Computing Research program under Award Number DE-SC-ERKJ422.
References
Abate, B. B., Sendekie, A. K., Ayele, M., Lake, E. S., Wodaynew, T., Tilahun, B. D., Azmeraw,
M., Habtie, T. E., Kassa, M., Munie, M. A., et al. (2024). Mapping fertility rates at national,
sub-national, and local levels in Ethiopia between 2000 and 2019. Frontiers in Public Health,
12.
Arambepola, R., Gething, P., and Cameron, E. (2020).
Nonparametric causal feature selec-
tion for spatiotemporal risk mapping of malaria incidence in madagascar.
arXiv preprint
arXiv:2001.07745.
Bachl, F. E., Lindgren, F., Borchers, D. L., and Illian, J. B. (2019). inlabru: an r package for
bayesian spatial modelling from ecological survey data.
Methods in Ecology and Evolution,
10(6), 760–766.
Bakka, H., Rue, H., Fuglstad, G.-A., Riebler, A., Bolin, D., Illian, J., Krainski, E., Simpson,
D., and Lindgren, F. (2018). Spatial modeling with r-inla: A review. Wiley Interdisciplinary
Reviews: Computational Statistics, 10(6), e1443.
Battese, G. E., Harter, R. T., and Fuller, W. A. (1988). An error-components model for predic-
tion of county crop areas using survey and satellite data. Journal of the American Statistical
Association, 83(401), 28–36.
Besag, J., York, J., and Molli´e, A. (1991). Bayesian image restoration, with two applications in
spatial statistics. Annals of the Institute of Statistical Mathematics, 43, 1–20.
Delprato, M., Chudgar, A., and Frola, A. (2024).
Spatial education inequality for attainment
indicators in sub-Saharan Africa and spillovers effects. World Development, 176, 106522.
Didan, K., Munoz, A. B., Solano, R., Huete, A., et al. (2015). MODIS vegetation index user’s
guide (MOD13 series). University of Arizona: Vegetation Index and Phenology Lab, 35, 2–33.
Dobson, J. E., Bright, E. A., Coleman, P. R., Durfee, R. C., and Worley, B. A. (2000). Landscan:
a global population database for estimating populations at risk. Photogrammetric engineering
and remote sensing, 66(7), 849–857.
Downes, M., Gurrin, L. C., English, D. R., Pirkis, J., Currier, D., and Spittal, M. J. (2018).
Multilevel regression with poststratification for small-area estimation of health indicators: a
case study of chronic diseases. Statistical Methods in Medical Research, 27(11), 3291–3305.
Fay, R. E. and Herriot, R. A. (1979).
Estimates of income for small places: An application
of james–stein procedures to census data.
Journal of the American Statistical Association,
74(366a), 269–277.
Gneiting, T. and Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation.
Journal of the American statistical Association, 102, 359–378.
H´ajek, J. (1971). Discussion of, “An essay on the logical foundations of survey sampling, part I”,
by D. Basu. In V. Godambe and D. Sprott, editors, Foundations of Statistical Inference. Holt,
Rinehart and Winston, Toronto.
Horvitz, D. G. and Thompson, D. J. (1952). A generalization of sampling without replacement
from a finite universe. Journal of the American Statistical Association, 47(260), 663–685.
Janocha, B., Donohue, R., Fish, T., Mayala, B., and Croft, T. (2021). Guidance and recommen-
dations for the use of indicator estimates at the subnational administrative level 2. Technical
report, ICF International. DHS Spatial Analysis Reports No. 20.
J¨onsson, K. and Bexell, M. (2021). Localizing the sustainable development goals: The case of
tanzania. Development Policy Review, 39(2), 181–196.
20


---

Kenya National Bureau of Statistics (2023).
Kenya time use report (based on 2021 kenya
continuous household survey).
https://www.knbs.or.ke/wp-content/uploads/2023/10/
Kenya-Time-Use-Survey-2021_1.pdf. Accessed: 2025-10-02.
Lindgren, F. and Rue, H. (2015). Bayesian spatial modelling with r-inla. Journal of statistical
software, 63, 1–25.
Lindgren, F., Rue, H., and Lindstr¨om, J. (2011). An explicit link between gaussian fields and
gaussian markov random fields: the stochastic partial differential equation approach. Journal of
the Royal Statistical Society: Series B (Statistical Methodology), 73(4), 423–498.
Lindgren, F., Bachl, F., Illian, J., Suen, M. H., Rue, H., and Seaton, A. E. (2024). inlabru: software
for fitting latent gaussian models with non-linear predictors. arXiv preprint arXiv:2407.00791.
Lindgren, F., Bachl, F. E., Borchers, D. L., Simpson, D., Scott-Howard, L., Seaton, A., Suen,
M. H., Roudier, P., Meehan, T., Niharika, P., and Perepolkin, D. (2025). inlabru: Bayesian
Latent Gaussian Modelling using INLA and Extensions. R package version 2.13.0.9011.
Morales, D., Santamar´ıa, L., and Molina, I. (2021). Model-based versus design-based estimators of
prevalence for small areas: the case of smoking in spain. International Statistical Review, 89(1),
28–50.
Moretti, A. and Whitworth, A. (2021). Comparison of small area estimation models for prevalence
mapping using survey data. Statistical Methods in Medical Research, 30(9), 2125–2141.
Nandi, A. K., Lucas, T. C., Arambepola, R., Gething, P., and Weiss, D. J. (2023). Disaggregation:
An r package for bayesian spatial disaggregation modeling. Journal of Statistical Software, 106,
1–19.
Oosterhof, P. D. (2018). Localizing the sustainable development goals to accelerate implementation
of the 2030 agenda for sustainable development: The current state of sustainable development
goal localization in asia and the pacific.
Park, D. K., Gelman, A., Bafumi, J., and Kaplan, A. (2004). Bayesian multilevel estimation with
poststratification: state-level estimates from national polls. Political Analysis, 12(4), 375–385.
Pratesi, M. (2016). Analysis of Poverty Data by Small Area Estimation. John Wiley & Sons.
Python, A., Marshall, J. D., Clark, S. J., and Mosser, J. F. (2022). High-resolution mapping of
covid-19 burden using disaggregation regression. Nature Communications, 13(1), 1234.
Rao, J. N. K. and Molina, I. (2015). Small Area Estimation. John Wiley & Sons.
Requia, W. J., Koutrakis, P., and Arain, A. (2018). Modeling spatial distribution of population
for environmental epidemiological studies: Comparing the exposure estimates using choropleth
versus dasymetric mapping. Environment international, 119, 152–164.
Riebler, A., Sørbye, S., Simpson, D., and Rue, H. (2016). An intuitive Bayesian spatial model
for disease mapping that accounts for scaling.
Statistical Methods in Medical Research, 25,
1145–1165.
Rom´an, M. O., Wang, Z., Sun, Q., Kalb, V., Miller, S. D., Molthan, A., Schultz, L., Bell, J.,
Stokes, E. C., Pandey, B., et al. (2018). Nasa’s black marble nighttime lights product suite.
Remote Sensing of Environment, 210, 113–143.
Rue, H., Martino, S., and Chopin, N. (2009). Approximate bayesian inference for latent gaussian
models by using integrated nested laplace approximations.
Journal of the Royal Statistical
Society: Series B, 71(2), 319–392.
Simpson, D., Rue, H., Riebler, A., Martins, T., and Sørbye, S. (2017). Penalising model component
complexity: A principled, practical approach to constructing priors. Statistical Science, 32, 1–28.
Smith, D. M., Heppenstall, A., and Campbell, M. (2021). Estimating health over space and time:
A review of spatial microsimulation applied to public health. J, 4(2), 182–192.
21


---

Suen, M. H., Naylor, M., Mudd, S., and Lindgren, F. (2025). Influence of river incision on landslides
triggered in nepal by the gorkha earthquake: Results from a pixel-based susceptibility model
using inlabru. arXiv preprint arXiv:2507.08742.
Tanton, R. (2014). A review of spatial microsimulation methods. International Journal of Mi-
crosimulation, 7(1), 4–25.
Tatem, A. J. (2017). Worldpop, open data for spatial demography. Scientific data, 4(1), 1–4.
United Nations Statistics Division (2020). Sdg indicator metadata: 5.4.1 proportion of time spent
on unpaid domestic and care work, by sex, age and location. https://unstats.un.org/sdgs/
metadata/files/Metadata-05-04-01.pdf. Accessed: 2025-10-02.
Utazi, C. E., Nilsen, K., Pannell, O., Dotse-Gborgbortsi, W., and Tatem, A. J. (2021). District-
level estimation of vaccination coverage: Discrete vs continuous spatial models. Statistics in
Medicine, 40, 2197–2211.
Wakefield, J., Gao, P., Fuglstad, G.-A., and Li, Z. R. (2025). The two cultures for prevalence
mapping: small area estimation and spatial statistics. arXiv preprint arXiv:2110.09576.
Weiss, D., Nelson, A., Vargas-Ruiz, C., Gligori´c, K., Bavadekar, S., Gabrilovich, E., Bertozzi-Villa,
A., Rozier, J., Gibson, H., Shekel, T., et al. (2020). Global maps of travel time to healthcare
facilities. Nature Medicine, 26, 1835–1838.
Wu, Y. and Wakefield, J. (2024).
Modelling urban/rural fractions in low- and middle-income
countries. Journal of the Royal Statistical Society Series A, 187, 811–830.
Wu, Y., Li, Z. R., Mayala, B., Wang, H., Gao, P., Paige, J., Fuglstad, G.-A., Moe, C., Godwin,
J., Donohue, R., Croft, T., and Wakefield, J. (2021). Spatio-temporal modeling for Admin-
2 small-area estimation. Technical report, ICF International. DHS Spatial Analysis Reports
No. 21.
Wu, Y., Dharamshi, A., and Wakefield, J. (2025). Small area estimation of education levels in
low-and middle-income countries. arXiv preprint arXiv:2502.07946.
22


---

Supplemental Materials for “Areal Disaggregation:
An SAE Perspective”
S1
On the Limitations of the Identity Link under inlabru
Linearization
It may be tempting to consider an alternative formulation of the unit-level disaggregation model.
Because the location parameter µi in the data model is itself the mean of the distribution, it
may appear possible to identify it directly with the predictor ηi, thereby dispensing with the link
function that is standard in generalized linear model-based settings. This line of reasoning would
suggest that the outer transformations used in the predictor (e.g., log(·) in log(P exp(·))) could
cancel out with the link function in the sampling model. To illustrate why this is incorrect, it
is helpful to examine the Poisson case, and the same argument extends to negative binomial and
(beta-) binomial likelihoods.
Problematic
Correct
Sampling model
Yi ∼Poisson(ni µi)
Yi ∼Poisson(ni µi)
Link
µi = ηi
(identity link)
log µi = ηi
(log link)
Predictor
ηi =
X
j
exp(Auj)
ηi = log
 X
j
exp(Auj)

The formulation on the left (above) reflects the apparent but misleading cancellation between
the logarithm in the aggregated predictor and the exponential from the log-link. Although alge-
braically attractive, this setup loses an important functionality of the link: it allows ηi to remain
unconstrained on R while ensuring µi > 0 for a valid mean.
Within the inlabru framework, this role is especially critical because predictors such as
ηi = log
 X
j
exp(Auj)

are linearized to enable inference. If one were instead to linearize
X
j
exp(Auj) ≈
˜
Au + δ(u0)
and use an identity link, then there would be no guarantee that the approximation remains strictly
non-negative across the full support of the latent Gaussian field u. Although the function value
should stay positive at the linearization point, the approximation might result in negative values
in the tails of the distribution support, which would be incompatible with the Poisson likelihood
(and with the constraints of binomial models).
By contrast, retaining the log-link ensures that even after linearization, the predictor ηi remains
unconstrained while the transformation exp(ηi) preserves the required positivity of µi.
Thus,
the algebraically simpler formulation cannot be adopted because it breaks the validity of the
linearization strategy employed by inlabru.
S1


---

S2
Model Specification for Spatial Model
Spatial Effects for Areas: The term bj represents the spatial random effect for area j, where
cluster c is located. We adopt the BYM2 model (Riebler et al., 2016), which is a reparameterization
of the Besag-York-Mollie (BYM) model (Besag et al., 1991) and decomposes bj into an independent
and identically distributed (IID) component ej and a spatially structured component Sj:
bj = σb(
√
1 −κej + √κSj),
with ej
iid
∼N(0, 1) and S = (S1, . . . , Sn)⊤following a scaled intrinsic conditional autoregressive
prior built from the adjacency matrix W (based on the geographical configuration of areas). Writing
j ∼q for spatial adjacency and mj for the number of neighbors, the conditional for region j is
Sj
 {Sq : q ∼j} ∼N

1
mj
X
q∼j
Sq, σ2
s
mj

,
with the sum-to-zero constraint P
j Sj = 0. We use penalized complexity priors (Simpson et al.,
2017) for the hyperparameters σb (total standard deviation) and κ (the proportion of variation
that is spatial) such that Pr(σb > 1) = 0.01 and Pr(κ > 0.5) = 0.5. Our prior specification is
predominantly dictated by the default settings in R-INLA and inlabru.
Posterior inference is conducted with the inlabru package (Lindgren et al., 2024; Bachl et al.,
2019), as discussed in greater detail in Section 2.3 of the main manuscript.
S2


---

S3
Additional Details on Simulation Setup
S3.1
Data Sources and Construction of Inputs
The simulation relies on publicly available geospatial covariates and administrative boundary data
to construct a realistic master frame. First, we obtain analysis shapefiles for Admin-1 and Admin-2
levels from Kenya’s Independent Electoral and Boundaries Commission and harmonize names and
codes with the census and WorldPop layers to ensure consistent geo-indexing.
Second, we extract sociodemographic marginals from the 2019 Kenya Population and Housing
Census at the Admin-2 level, including the proportion urban, the proportion of women with sec-
ondary or higher education, and selected additional area-level covariates (e.g., average household
size, mobile phone access). Because the census reporting units do not perfectly match the standard
Admin-2 boundaries used in our analysis, we harmonize the two by using a crosswalk table that
maps census units to analysis units. This mapping is used primarily for transferring fraction or
ratio measures. Population counts are taken from WorldPop (described below) and disaggregated
using the census proportions. Full details of the crosswalk construction and caveats are provided
in the next section.
Third, we use WorldPop 2019’s gridded population estimates to obtain counts of females by
5-year age groups on a 1 km × 1 km grid. We aggregate these counts to the Admin-2 level by using
the analysis shapefile and produce age-by-area totals for the groups 15–19, ..., 40–44. These totals
serve as the base population.
Fourth, we compile additional 1 km raster covariates to drive spatial heterogeneity in fertility:
nighttime lights (Rom´an et al., 2018), travel time to the nearest health facility (Weiss et al., 2020),
and vegetation index (NDVI) (Didan et al., 2015). We then compute population-weighted Admin-2
averages of these covariates.
Fifth, we extract key design parameters from the 2022 Kenya DHS (demographic and health
survey): the stratification scheme (Admin-1 × urban/rural [notably, Nairobi and Mombasa are
entirely urban]), number of enumeration areas (EAs) and primary sampling units (PSUs) in the
frame by stratum, and the target number of sampled EAs and women per EA. These inputs are
used to mirror the two-stage DHS sampling.
S3.2
Census-Admin-2 Crosswalk and Data Harmonization
The 2019 Kenya Population and Housing Census reports sociodemographic indicators at the level
of 333 subcounties after excluding protected areas and other non-residential units. These reporting
units do not perfectly align with the 290 Admin-2 (constituency) boundaries used in our analysis,
and no official boundary files for the 333 census subcounties are publicly available. To harmonize
these definitions, we constructed a 333 × 290 crosswalk matrix linking census subcounties to the
Admin-2 units used in our simulation framework.
The crosswalk was developed through a sequential process. We began by matching unit names
between the census tables and the Admin-2 shapefile and accounting for known historical name
changes, alternative spellings, and differences in formatting. When direct matches were not pos-
sible, we manually examined regional records, administrative maps, and auxiliary geographic
metadata to identify the most plausible correspondences. For cases in which a census subcounty
overlapped multiple Admin-2 units (or vice versa), we permitted many-to-many mappings in the
crosswalk. Because such links can distort absolute population counts, we restricted the use of
the crosswalk to transferring proportion and ratio measures, such as the fraction of urban or the
fraction of women with secondary or higher education.
Absolute counts were instead obtained from UN-adjusted WorldPop 2019 gridded population
estimates for 5-year female age groups at a 1 km resolution.
These counts were aggregated to
the Admin-2 boundaries used in the analysis and then partitioned by urban/rural and education
strata by using the proportions derived from the census. This procedure mitigates the impact
of potential census undercounts while preserving the census-derived sociodemographic structure.
Although undercounting in census totals has minimal effect on the proportion measures we derived,
it could bias counts if used directly, which reinforces our decision to rely on WorldPop data for
absolute population totals.
S3


---

S3.3
Generating the Master Frame and the Sample
Step 1: Individual listing.
We expand the Admin-2 × age-group × urbanicity × education
cells into a synthetic population of individual women from age groups 15–19, 20–24, ..., 40–44. We
discuss generation of exposure and outcome in Section S3.4.
Step 2: Enumeration areas assignment.
The DHS report contains data on how many
EAs exist within each stratum h (Admin-1 × urban/rural) in the sampling master frame. We
allocate a number of EAs to each Admin-2 × urban/rural cell proportional to its female population
share within each strata. To induce realistic cluster size heterogeneity, we draw EA relative sizes
S from a lognormal distribution with log S ∼N(0, 0.22). We then partition the individual women
in each stratum into EAs according to these relative sizes (proportional allocation) to preserve
Admin-2 membership.
Step 3: Two-stage sample selection (mimic DHS).
We emulate the DHS design by
using stratified two-stage sampling. In the first stage, within each stratum h, we select nh clusters
(EAs) by probability-proportional-to-size (PPS) sampling, where the measure of size is the number
of women in the cluster. Let Nhc denote this measure of size for cluster c in stratum h and let
Nh· = P
c Nhc. The first-stage inclusion probability is
π(1)
hc = nh Nhc
Nh·
In the second stage, from each sampled cluster c, we select mhc women by simple random
sampling without replacement.
We set mhc = 20 to approximate the sample size in the 2022
Kenya DHS. The conditional probability of selecting woman k in cluster c is then
π(2)
k|hc = mhc
Nhc
.
The overall inclusion probability is
πk = π(1)
hc × π(2)
k|hc = nh Nhc
Nh·
× mhc
Nhc
= nh mhc
Nh·
,
and the base sampling weight is wk = 1/πk. We do not simulate or adjust for nonresponse.
S3.4
Outcome Generation and Simulation Scenarios
Table S1: Sources of spatial heterogeneity under four scenarios and the expected ability of disaggre-
gation models to capture them.
Variation sources
Scenario 1
Scenario 2
Scenario 3
Scenario 4
Recoverable
Observed covariates
✓
✓
✓
✓
✓
Explicitly captured
by fixed effects
Unobserved covariates
(spatially correlated
Admin-2 effects)
✗
✓
✓
✓
❍
Partially captured
by spatial effects
IID Admin-2
random effects
✗
✗
✓
✓
✗
Not recoverable,
purely unstructured
Varying
coefficients
✗
✗
✗
✓
✗
Leads to model
misspecification
S4


---

Scenario 1:
In the first scenario, only observed covariates are included. The log-scale mean
structure for individual k in cluster c located in Admin-2 area j is specified as
log µs1
c,k = αrural I(c ∈rural) + αurban I(c ∈urban)
+ δage(k) + δeduc(k)
+ βXj[k] + ek + ec.
The intercepts are fixed at αurban = −2.1 and αrural = −1.8.
The terms δage(k) and δeduc(k)
represent individual-level covariates that are expected to be captured through MRP. The vector
Xj[k] denotes area-level covariates, which include nighttime light, travel time to the nearest health
facility, and average household size, all of which are standardized. The covariate effects are specified
as
βntl = −0.08,
βhealth = 0.08,
βedu = −0.6,
βhh = 0.08.
Education is modeled as a binary indicator of high school attendance, with effect δeduc = −0.6.
The age-group effects are constructed as follows:
δage =



















−0.3
if age 15–19,
0.6
if age 20–24,
0.5
if age 25–29,
0.3
if age 30–34,
−0.2
if age 35–39,
−0.9
if age 40–44.
These covariate effect values were selected to introduce variability across subgroups and to
approximate realistic patterns to some extent. However, they are not intended to serve as direct
or accurate estimates of the true underlying effects. The individual-level random effects are drawn
from normal distributions with standard deviations 0.05 for both ek and ec.
Scenario 2:
In the second scenario, we extend the model by including unobserved covariates in
addition to those already specified. The extended structure is
log(µs2
c,k) = log(µs1
c,k) + βunobsXunobs
j[k]
,
where Xunobs
j[k]
includes two measures: the vegetation index (NDVI) and female mobile phone usage,
both of which are standardized. The effects of these covariates are specified as
βndvi = 0.08,
βmobile = −0.08.
Scenario 3:
The third scenario builds on the second by introducing an independent random
effect at the Admin-2 level:
log(µs3
c,k) = log(µs2
c,k) + ej,
ej ∼N(0, 0.122).
This added Admin-2 level IID random effect represents unstructured residual variations that are
not expected to be explained by the disaggregation model.
Scenario 4:
In the final scenario, we introduce model misspecification by allowing coefficients
to differ between urban and rural parts of the same area. In contrast to the uniform coefficients
assumed in the previous scenarios, this specification captures heterogeneity across settlement types.
The coefficients for the two strata are as follows:
Urban: α = −2.10, βntl = −0.10, βhealth = 0.10, βedu = −0.50, βhh = 0.06, βndvi = 0.06, βmobile =
−0.06, δeduc
k
= −0.5
Rural: α = −1.80, βntl = −0.06, βhealth = 0.06, βedu = −0.70, βhh = 0.10, βndvi = 0.10, βmobile =
−0.10, δeduc
k
= −0.7
δ(Urban)
age
=



















−0.4
if age group is 15–19,
0.5
if age group is 20–24,
0.5
if age group is 25–29,
0.3
if age group is 30–34,
−0.1
if age group is 35–39,
−0.8
if age group is 40–44.
δ(Rural)
age
=



















−0.2
if age group is 15–19,
0.6
if age group is 20–24,
0.4
if age group is 25–29,
0.3
if age group is 30–34,
−0.2
if age group is 35–39,
−0.9
if age group is 40–44.
S5


---

S4
Additional Simulation Results
Table S2: Performance metrics across methods and scenarios. Values show the mean for each selected
metric across 500 simulation repetitions.
Method
Regression R2
Pearson r
Interval Score
Bias
Abs Rel Bias
Scenario 1
FH disagg
0.927
0.978
0.014
0.000
3.6%
FH-MRP disagg
0.929
0.982
0.014
0.000
3.7%
Unit disagg
0.949
0.983
0.011
0.000
3.1%
Unit-MRP disagg
0.983
0.997
0.009
0.000
1.7%
FH (Adm2)
0.642
0.832
0.020
0.000
7.6%
Direct (Adm2)
0.062
0.690
0.029
0.000
13.3%
Scenario 2
FH disagg
0.857
0.962
0.024
0.000
5.5%
FH-MRP disagg
0.821
0.957
0.025
-0.003
6.3%
Unit disagg
0.911
0.979
0.021
0.000
4.2%
Unit-MRP disagg
0.902
0.976
0.020
-0.001
4.3%
FH (Adm2)
0.691
0.859
0.021
0.001
8.1%
Direct (Adm2)
0.291
0.738
0.029
0.001
13.4%
Scenario 3
FH disagg
0.622
0.773
0.034
0.000
10.8%
FH-MRP disagg
0.598
0.770
0.036
-0.002
11.2%
Unit disagg
0.670
0.787
0.031
0.000
10.0%
Unit-MRP disagg
0.668
0.786
0.032
0.000
10.0%
FH (Adm2)
0.685
0.839
0.023
0.001
9.9%
Direct (Adm2)
0.469
0.792
0.029
0.001
13.4%
Scenario 4
FH disagg
0.593
0.756
0.035
0.000
10.9%
FH-MRP disagg
0.570
0.753
0.037
-0.002
11.4%
Unit disagg
0.641
0.771
0.032
0.000
10.3%
Unit-MRP disagg
0.628
0.764
0.034
0.000
10.4%
FH (Adm2)
0.670
0.834
0.023
0.001
9.9%
Direct (Adm2)
0.449
0.789
0.028
0.001
13.4%
S6


---

Scenario 1
Scenario 2
Scenario 3
Scenario 4
Bias
Absolute bias
Relative bias
Abs rel bias
FH disagg
FH−MRP disagg
Unit disagg
Unit−MRP disagg
FH (Adm2)
Direct (Adm2)
FH disagg
FH−MRP disagg
Unit disagg
Unit−MRP disagg
FH (Adm2)
Direct (Adm2)
FH disagg
FH−MRP disagg
Unit disagg
Unit−MRP disagg
FH (Adm2)
Direct (Adm2)
FH disagg
FH−MRP disagg
Unit disagg
Unit−MRP disagg
FH (Adm2)
Direct (Adm2)
−0.005
0.000
0.005
0.005
0.010
0.015
0.020
0.025
−0.04
−0.02
0.00
0.02
0.04
0.06
0.04
0.08
0.12
0.16
Method
Value
Figure S1: Comparison of disaggregation and benchmark models across four simulation scenarios
evaluated with bias metrics.
S7


---

S5
Additional Visualizations
S5.1
Further Comparison of GFR Estimates (Case Study 1)
Figure S2 shows the difference between Admin-2 estimates from each disaggregation model and
those from the Admin-2 Fay–Herriot (FH) model against the area-level random effects estimated
by the Admin-2 FH model. The strong association indicates that the deviation of disaggregation
models arises in regions with a strong area-level effect. This is consistent with our simulation
findings: by design, disaggregation models have a limited ability to identify area-level random
effects, especially the unstructured component.
FH disaggregation
Unit disaggregation
−0.4
−0.2
0.0
0.2
0.4
−0.4
−0.2
0.0
0.2
0.4
−0.10
−0.05
0.00
0.05
0.10
Area−level random effects
Difference (compared with FH Admin−2)
Figure S2: Scatter plots of the relationship between area-level random effects and the difference in
GFR estimates from disaggregation models compared with the FH Admin-2 benchmark.
S8


---

Lamu
Machakos
Makueni
Mandera
Marsabit
Kisii
Kisumu
Kitui
Kwale
Laikipia
Kakamega
Kericho
Kiambu
Kilifi
Kirinyaga
Embu
Garissa
Homa Bay
Isiolo
Kajiado
Baringo
Bomet
Bungoma
Busia
Elgeyo−Marakwet
Lamu East
Lamu West
Kangundo
Kathiani
Machakos Town
Masinga
Matungulu
Mavoko
Mwala
Yatta
Kaiti
Kibwezi East
Kibwezi West
Kilome
Makueni
Mbooni
Banissa
Lafey
Mandera East
Mandera North
Mandera South
Mandera West
Laisamis
Moyale
North Horr
Saku
Bobasi
Bomachoge Borabu
Bomachoge Chache
Bonchari
Kitutu Chache North
Kitutu Chache South
Nyaribari Chache
Nyaribari Masaba
South Mugirango
Kisumu Central
Kisumu East
Kisumu West
Muhoroni
Nyakach
Nyando
Seme
Kitui Central
Kitui East
Kitui Rural
Kitui South
Kitui West
Mwingi East
Mwingi North
Mwingi West
Kinango
Lunga Lunga
Matuga
Msambweni
Laikipia East
Laikipia North
Laikipia West
Butere
Ikolomani
Khwisero
Likuyani
Lugari
Lurambi
Malava
Matungu
Mumias East
Mumias West
Navakholo
Shinyalu
Ainamoi
Belgut
Buret
Kipkelion East
Kipkelion West
Sigowet/Soin
Gatundu North
Gatundu South
Githunguri
Juja
Kabete
Kiambaa
Kiambu
Kikuyu
Lari
Limuru
Ruiru
Thika Town
Ganze
Kaloleni
Kilifi North
Kilifi South
Magarini
Malindi
Rabai
Gichugu
Kirinyaga Central
Mwea
Ndia
Gachoka
Manyatta
Runyenjes
Siakago
Balambala
Dadaab
Dujis
Fafi
Ijara
Lagdera
Homa Bay
Kabondo Kasipul
Karachuonyo
Kasipul
Ndhiwa
Rangwe
Suba North
Suba South
Isiolo North
Isiolo South
Kajiado Central
Kajiado East
Kajiado North
Kajiado South
Kajiado West
Baringo Central
Baringo North
Baringo South
Eldama Ravine
Mogotio
Tiaty
Bomet Central
Bomet East
Chepalungu
Konoin
Sotik
Bumula
Kabuchai
Kanduyi
Kimilili
Mt. Elgon
Sirisia
Tongaren
Webuye East
Webuye West
Budalangi
Butula
Funyula
Matayos
Nambale
Teso North
Teso South
Keiyo North
Keiyo South
Marakwet East
Marakwet West
0.10
0.15
0.20
0.25
0.05
0.10
0.15
0.20
0.25
0.08
0.10
0.12
0.14
0.16
0.08
0.12
0.16
0.20
0.15
0.20
0.25
0.30
0.10
0.14
0.18
0.22
0.10
0.15
0.20
0.25
0.30
0.10
0.15
0.20
0.25
0.10
0.15
0.20
0.25
0.20
0.30
0.40
0.10
0.15
0.20
0.10
0.15
0.20
0.25
0.06
0.09
0.12
0.15
0.10
0.15
0.20
0.09
0.12
0.15
0.18
0.10
0.12
0.15
0.18
0.10
0.20
0.30
0.40
0.50
0.08
0.12
0.16
0.20
0.10
0.15
0.20
0.06
0.09
0.12
0.15
0.10
0.15
0.20
0.25
0.30
0.09
0.12
0.15
0.18
0.08
0.10
0.12
0.15
0.18
0.20
0.08
0.10
0.12
0.15
0.15
0.20
0.25
Admin−2
Mean (90% CI)
Method
FH (Admin−2)
FH disaggregation
Unit disaggregation
Figure S3: Comparison of Admin-2 point estimates and 90% credible intervals for GFR across the
benchmark FH Admin-2 model and the FH and unit-level disaggregation models displayed within
Admin-1 groupings.
S9


---

Wajir
West Pokot
Tharaka−Nithi
Trans Nzoia
Turkana
Uasin Gishu
Vihiga
Nyeri
Samburu
Siaya
Taita Taveta
Tana River
Nakuru
Nandi
Narok
Nyamira
Nyandarua
Meru
Migori
Mombasa
Murang'a
Nairobi
Eldas
Tarbaj
Wajir East
Wajir North
Wajir South
Wajir West
Kacheliba
Kapenguria
Pokot South
Sigor
Maara
Nithi
Tharaka
Cherangany
Endebess
Kiminini
Kwanza
Saboti
Loima
Turkana Central
Turkana East
Turkana North
Turkana South
Turkana West
Ainabkoi
Kapseret
Kesses
Moiben
Soy
Turbo
Emuhaya
Hamisi
Luanda
Sabatia
Vihiga
Kieni
Mathira
Mukurweni
Nyeri Town
Othaya
Tetu
Samburu East
Samburu North
Samburu West
Alego Usonga
Bondo
Gem
Rarieda
Ugenya
Ugunja
Mwatate
Taveta
Voi
Wundanyi
Bura
Galole
Garsen
Bahati
Gilgil
Kuresoi North
Kuresoi South
Molo
Naivasha
Nakuru Town East
Nakuru Town West
Njoro
Rongai
Subukia
Aldai
Chesumei
Emgwen
Mosop
Nandi Hills
Tinderet
Emurua Dikirr
Kilgoris
Narok East
Narok North
Narok South
Narok West
Borabu
Kitutu Masaba
North Mugirango
West Mugirango
Kinangop
Kipipiri
Ndaragwa
Ol Jorok
Ol Kalou
Buuri
Cental Imenti
Igembe Central
Igembe North
Igembe South
North Imenti
South Imenti
Tigania East
Tigania West
Awendo
Kuria East
Kuria West
Nyatike
Rongo
Suna East
Suna West
Uriri
Changamwe
Jomvu
Kisauni
Likoni
Mvita
Nyali
Gatanga
Kandara
Kangema
Kigumo
Kiharu
Maragwa
Mathioya
Dagoretti
Embakasi Central
Embakasi East
Embakasi North
Embakasi South
Embakasi West
Kamukunji
Kasarani
Kibra
Kilimani
Langata
Makadara
Mathare
Roysambu
Ruaraka
Starehe
Westlands
0.06
0.08
0.10
0.12
0.14
0.16
0.08
0.10
0.12
0.15
0.18
0.15
0.20
0.25
0.30
0.08
0.10
0.12
0.15
0.09
0.12
0.15
0.08
0.10
0.12
0.14
0.08
0.10
0.12
0.15
0.18
0.10
0.15
0.20
0.08
0.10
0.12
0.15
0.10
0.15
0.20
0.25
0.08
0.12
0.16
0.20
0.10
0.20
0.30
0.40
0.50
0.10
0.15
0.20
0.25
0.08
0.10
0.12
0.15
0.18
0.10
0.20
0.30
0.08
0.12
0.16
0.20
0.15
0.20
0.25
0.30
0.35
0.10
0.15
0.20
0.10
0.15
0.20
0.08
0.10
0.12
0.15
0.06
0.09
0.12
0.15
0.18
0.20
0.30
0.40
Admin−2
Mean (90% CI)
Method
FH (Admin−2)
FH disaggregation
Unit disaggregation
Figure S4: Interval plot continued.
S10


---

S5.2
Time Spent on Unpaid Care and Domestic Work (Men)
Direct estimation
FH disaggregation
Unit disaggregation
Unpaid care or 
 domestic work 
 (% of day)
2%
3%
4%
5%
6%
Direct estimation
FH disaggregation
Unit disaggregation
Width of 
 90% CI
2%
5%
8%
Figure S5: Estimated proportion of the day that men spend on unpaid care and domestic work based
on direct estimation at Admin-1, FH disaggregation, and unit-level disaggregation models. The maps
display both point estimates and the widths of the associated 90% uncertainty intervals.
S11


---

S5.3
Uncertainty for Male and Female Mass Media Usage Estimates
Female
Direct estimation
FH disaggregation
Unit disaggregation
Male
Width of 90% CI
20%
40%
60%
Figure S6: Maps of 90% CI widths for male and female mass media usage estimates.
S12
