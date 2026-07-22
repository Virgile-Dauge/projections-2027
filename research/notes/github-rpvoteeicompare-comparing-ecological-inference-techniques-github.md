---
title: 'GitHub - RPVote/eiCompare: Comparing ecological inference techniques · GitHub'
id: github-rpvoteeicompare-comparing-ecological-inference-techniques-github
tags:
- ecological-inference
- eicompare
- voting-rights-act
created: '2026-07-21T19:07:21.951432Z'
updated: '2026-07-21T19:42:36.597489Z'
source: https://github.com/RPVote/eiCompare
source_domain: github.com
fetched_at: '2026-07-21T19:07:21.911831Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: 'eiCompare (RPVote/eiCompare, R package, v3.0.6, maintained by Loren Collingwood)
  implements and compares three ecological-inference estimators for racially/politically
  polarized voting: Goodman''s ecological regression (ei_good, fast deterministic
  baseline), King''s (1997) iterative 2x2 Bayesian EI (ei_iter), and RxC multinomial-Dirichlet
  EI (ei_rxc) for simultaneous multi-candidate/multi-group estimation, wrapping the
  underlying ei and eiPack R packages. Built explicitly for three constituencies relevant
  to the French use case: voting-rights litigation expert witnesses, national advocacy
  orgs screening jurisdictions for vote dilution, and grassroots/local organizations
  wanting data-driven local targeting -- the same ''militant terrain'' framing as
  the French research question, just applied to racial rather than partisan bloc voting.
  Includes VAP-denominator normalization (rpv_normalize) to condition estimates on
  voters rather than total voting-age population, and outputs feed a companion visualization
  package eiExpand::rpv_plot. Worked example uses 2018 Georgia gubernatorial results
  (Gwinnett County) with cand_cols/race_cols/totals_col precinct-level inputs.'
---

[Skip to content](https://github.com/RPVote/eiCompare#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/RPVote/eiCompare) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/RPVote/eiCompare) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/RPVote/eiCompare) to refresh your session. Dismiss alert
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/RPVote/eiCompare).
/ Public
  * [ Notifications ](https://github.com/login?return_to=%2FRPVote%2FeiCompare) You must be signed in to change notification settings
  * [ Fork 7 ](https://github.com/login?return_to=%2FRPVote%2FeiCompare)
  * [ Star  10 ](https://github.com/login?return_to=%2FRPVote%2FeiCompare)


[**11** Branches](https://github.com/RPVote/eiCompare/branches)
Go to file
Open more actions menu
## Folders and files  
| Name  | Name  | Last commit message  | Last commit date  |  
| --- | --- | --- | --- |  
| 
## Latest commit
[Add 95% confidence intervals to ei_good() output](https://github.com/RPVote/eiCompare/commit/4eb651c773e657476496e5c087e6c299d1891c70) Open commit detailssuccess Jun 25, 2026 [4eb651c](https://github.com/RPVote/eiCompare/commit/4eb651c773e657476496e5c087e6c299d1891c70) · Jun 25, 2026
## History
[496 Commits](https://github.com/RPVote/eiCompare/commits/master/)Open commit details 496 Commits  |  
|   |   | [Fix styler CI: pin R 4.4 and handle parse errors gracefully](https://github.com/RPVote/eiCompare/commit/047af394f626547bb67dacb49ae6bf6f492564c0 "Fix styler CI: pin R 4.4 and handle parse errors gracefully

styler throws parse errors on some files under R 4.6.0, producing NAs
in the changed column which crashes the check. Pin R to 4.4 for
consistency and add NA handling for robustness.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")  | May 29, 2026  |  
| [Add 95% confidence intervals to ei_good() output](https://github.com/RPVote/eiCompare/commit/4eb651c773e657476496e5c087e6c299d1891c70 "Add 95% confidence intervals to ei_good\(\) output

ei_good\(\) now computes CI from the Goodman regression SEs using a normal
approximation \(mean +/- z * SE, bounded to \[0,1\]\), matching the column
format produced by ei_iter\(\) and ei_rxc\(\). This makes ei_good results
fully compatible with the rpv_toDF / rpv_plot downstream pipeline.")  | Jun 25, 2026  |  
| [add south_carolina dataset to eiCompare, needed for rpv_toDF examples](https://github.com/RPVote/eiCompare/commit/3db12d20e73689cef9e4101079eb47968f3eeb77 "add south_carolina dataset to eiCompare, needed for rpv_toDF examples")  | Oct 10, 2025  |  
| [apply styler defaults to package](https://github.com/RPVote/eiCompare/commit/98e82ca2df205dd8b1443b39759617690dc0b64d "apply styler defaults to package")  | Jul 10, 2020  |  
| [tweak license in description, comment out long code in vignettes](https://github.com/RPVote/eiCompare/commit/81a93f245f491ea8a1eb854e793825aacd323355 "tweak license in description, comment out long code in vignettes")  | Feb 22, 2023  |  
| [Add 95% confidence intervals to ei_good() output](https://github.com/RPVote/eiCompare/commit/4eb651c773e657476496e5c087e6c299d1891c70 "Add 95% confidence intervals to ei_good\(\) output

ei_good\(\) now computes CI from the Goodman regression SEs using a normal
approximation \(mean +/- z * SE, bounded to \[0,1\]\), matching the column
format produced by ei_iter\(\) and ei_rxc\(\). This makes ei_good results
fully compatible with the rpv_toDF / rpv_plot downstream pipeline.")  | Jun 25, 2026  |  
|   |   | [eiCompare 3.0.6: Fix ei_good class, rpv_toDF compatibility, and rpv_n…](https://github.com/RPVote/eiCompare/commit/a08938bc7c249eb3758b85157cfa6f685246b193 "eiCompare 3.0.6: Fix ei_good class, rpv_toDF compatibility, and rpv_normalize guard

- ei_good\(\) now returns eiCompare class object \(consistent with ei_iter/ei_rxc\),
  enabling direct use with summary\(\), rpv_toDF\(\), and plot methods
- rpv_normalize\(\) blocks ei_good output with informative error \(Goodman regression
  lacks posterior samples needed for normalization\)
- rpv_toDF\(\) handles ci_95_lower/ci_95_upper column names from rpv_normalize output
  and strips name tag suffixes \(e.g. _Iter, _RxC\) from summary columns
- Add RPV analysis vignette with Gwinnett County data demonstrating all three EI
  methods and eiExpand integration
- Update maintainer to Loren Collingwood
- Update GitHub Actions workflows to modern versions \(actions/checkout@v4,
  r-lib/actions@v2\)
- Apply styler formatting to all R source files

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")  | May 29, 2026  |  
|   |   | [Remove eiExpand rpv_plot sections from vignette to fix CI build](https://github.com/RPVote/eiCompare/commit/6f4896c52c4f8cb81c52e1b510079f9507c3fa79 "Remove eiExpand rpv_plot sections from vignette to fix CI build

eiExpand is a GitHub-only package not available during R CMD check.
Remove rpv_plot sections from the rpv_analysis vignette so the
vignette builds without external dependencies.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")  | May 29, 2026  |  
|   |   | [final prep for submission](https://github.com/RPVote/eiCompare/commit/cbdac0fc7259aca971d9416172f0ad2f87cf08b9 "final prep for submission")  | Sep 22, 2022  |  
|   |   | [drop vignettes no longer up to date](https://github.com/RPVote/eiCompare/commit/2cfd27d1fe172b8c0564064946a272efdeb9780b "drop vignettes no longer up to date
and fix a few typos")  | Feb 1, 2025  |  
| [.pre-commit-config.yaml](https://github.com/RPVote/eiCompare/blob/master/.pre-commit-config.yaml ".pre-commit-config.yaml")  | [.pre-commit-config.yaml](https://github.com/RPVote/eiCompare/blob/master/.pre-commit-config.yaml ".pre-commit-config.yaml")  | [apply styler defaults to package](https://github.com/RPVote/eiCompare/commit/98e82ca2df205dd8b1443b39759617690dc0b64d "apply styler defaults to package")  | Jul 10, 2020  |  
|   |   |   | Aug 22, 2020  |  
|   |   |   | Aug 22, 2020  |  
|   |   | [Fix broken URLs flagged by CRAN pretest](https://github.com/RPVote/eiCompare/commit/220eec9db918cf23b42ff140ad8adc6fbd3d5b6c "Fix broken URLs flagged by CRAN pretest

- DESCRIPTION: Replace dead gking.harvard.edu/eicamera and /files/abs
  URLs with https://gking.harvard.edu/ei/
- R/ and man/: Update http://gking.harvard.edu/eiR to
  https://gking.harvard.edu/eiR/ \(https + trailing slash, avoids 301\)
- Update CRAN-SUBMISSION for 3.0.6
- Regenerated roxygen2 man pages

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")  | May 29, 2026  |  
|   |   | [Fix broken URLs flagged by CRAN pretest](https://github.com/RPVote/eiCompare/commit/220eec9db918cf23b42ff140ad8adc6fbd3d5b6c "Fix broken URLs flagged by CRAN pretest

- DESCRIPTION: Replace dead gking.harvard.edu/eicamera and /files/abs
  URLs with https://gking.harvard.edu/ei/
- R/ and man/: Update http://gking.harvard.edu/eiR to
  https://gking.harvard.edu/eiR/ \(https + trailing slash, avoids 301\)
- Update CRAN-SUBMISSION for 3.0.6
- Regenerated roxygen2 man pages

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")  | May 29, 2026  |  
|   |   | [Add 95% confidence intervals to ei_good() output](https://github.com/RPVote/eiCompare/commit/4eb651c773e657476496e5c087e6c299d1891c70 "Add 95% confidence intervals to ei_good\(\) output

ei_good\(\) now computes CI from the Goodman regression SEs using a normal
approximation \(mean +/- z * SE, bounded to \[0,1\]\), matching the column
format produced by ei_iter\(\) and ei_rxc\(\). This makes ei_good results
fully compatible with the rpv_toDF / rpv_plot downstream pipeline.")  | Jun 25, 2026  |  
|   |   | [eiCompare 3.0.6: Fix ei_good class, rpv_toDF compatibility, and rpv_n…](https://github.com/RPVote/eiCompare/commit/a08938bc7c249eb3758b85157cfa6f685246b193 "eiCompare 3.0.6: Fix ei_good class, rpv_toDF compatibility, and rpv_normalize guard

- ei_good\(\) now returns eiCompare class object \(consistent with ei_iter/ei_rxc\),
  enabling direct use with summary\(\), rpv_toDF\(\), and plot methods
- rpv_normalize\(\) blocks ei_good output with informative error \(Goodman regression
  lacks posterior samples needed for normalization\)
- rpv_toDF\(\) handles ci_95_lower/ci_95_upper column names from rpv_normalize output
  and strips name tag suffixes \(e.g. _Iter, _RxC\) from summary columns
- Add RPV analysis vignette with Gwinnett County data demonstrating all three EI
  methods and eiExpand integration
- Update maintainer to Loren Collingwood
- Update GitHub Actions workflows to modern versions \(actions/checkout@v4,
  r-lib/actions@v2\)
- Apply styler formatting to all R source files

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")  | May 29, 2026  |  
|   |   | [eiCompare 3.0.6: Fix ei_good class, rpv_toDF compatibility, and rpv_n…](https://github.com/RPVote/eiCompare/commit/a08938bc7c249eb3758b85157cfa6f685246b193 "eiCompare 3.0.6: Fix ei_good class, rpv_toDF compatibility, and rpv_normalize guard

- ei_good\(\) now returns eiCompare class object \(consistent with ei_iter/ei_rxc\),
  enabling direct use with summary\(\), rpv_toDF\(\), and plot methods
- rpv_normalize\(\) blocks ei_good output with informative error \(Goodman regression
  lacks posterior samples needed for normalization\)
- rpv_toDF\(\) handles ci_95_lower/ci_95_upper column names from rpv_normalize output
  and strips name tag suffixes \(e.g. _Iter, _RxC\) from summary columns
- Add RPV analysis vignette with Gwinnett County data demonstrating all three EI
  methods and eiExpand integration
- Update maintainer to Loren Collingwood
- Update GitHub Actions workflows to modern versions \(actions/checkout@v4,
  r-lib/actions@v2\)
- Apply styler formatting to all R source files

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")  | May 29, 2026  |  
|   |   | [Continuing to clean up Rd ocumentation for the geocoder functions.](https://github.com/RPVote/eiCompare/commit/ab4eac0b40126a2e60fc3c7332ff41011b566d29 "Continuing to clean up Rd ocumentation for the geocoder functions.")  | Aug 19, 2020  |  
| View all files |  
## Repository files navigation
# eiCompare 
`eiCompare` is an R package built to help practitioners and academics quantify racially polarized voting (RPV) with ease and confidence. It builds on top of several existing packages, augmenting their utility for measuring racially polarized voting in elections. Underlying packages include `ei` and `eiPack`.
`eiCompare` was built with several types of users in mind:
  * Expert witnesses in voting rights litigation who need to accurately quantify vote dilution in an area and present the results convincingly to a judge or jury.
  * National voting rights advocacy organizations trying to identify elections across the country where vote dilution might be at play.
  * Grassroots organizations looking for data-driven tools to fuel their fight against vote dilution at the local level.
  * Academics who study the causes and consequences of vote dilution and racially polarized voting.


# eiCompare 3.0.6
## Bug fixes and improvements
  * `ei_good()` now returns an `eiCompare` class object, consistent with `ei_iter()` and `ei_rxc()`. Output works directly with `summary()`, `rpv_toDF()`, and `rpv_plot()`.
  * `rpv_toDF()` now correctly handles `ci_95_lower`/`ci_95_upper` column names from `rpv_normalize()` output.
  * `rpv_normalize()` returns an informative error when passed `ei_good()` output.
  * Switched maintainer to Loren Collingwood (lcollingwood@unm.edu)
  * Added RPV analysis vignette


# eiCompare 3.0.5
## New function
  * included extract_rxc_precinct() function to extract precinct level estimates from ei_rxc()


# eiCompare 3.0.4
## Package changes
  * added rpv_normalize() function
  * removed wru dependency
  * incorporated rpv_coef_plot() and rpv_toDF() functions from eiExpand package
  * edited ei_iter() to have flexible CI parameters (default is 0.95) using bayestestR for calculation and updated column naming, and to use reproducible parallel processing (.inorder=TRUE)
  * edited ei_rxc() with reproducible parallel processing and changed column naming to fit ei_iter()
  * Fixed summary.eiCompare() print behavior
  * Added viridis to imports for color visualization and updated RoxygenNote to 7.3.2


See [NEWS.md](https://github.com/RPVote/eiCompare/blob/master/NEWS.md) for a full changelog.
## Installation
### From Github (development version)
Install latest development version with:

```
remotes::install_github('RPVote/eiCompare')

```

## Usage
The name `eiCompare` highlights the utility of this package for comparing different ecological inference estimates. The package provides three EI methods:
  * **Goodman's Regression** (`ei_good()`) -- A fast, deterministic method based on ecological regression. Useful as a baseline estimate.
  * **Iterative EI** (`ei_iter()`) -- King's (1997) iterative 2x2 ecological inference method with Bayesian estimation.
  * **RxC EI** (`ei_rxc()`) -- Multinomial-Dirichlet model for simultaneous estimation across all race-candidate pairs.


All three functions return `eiCompare` class objects that work with `summary()`, `rpv_toDF()`, and visualization functions.
### Quick example
The following code estimates racial voting preferences in the 2018 Georgia gubernatorial election using Gwinnett County data:

```
library(eiCompare)
data("gwinnett_ei")

cands <- c("kemp", "abrams", "metz")
races <- c("white", "black", "other")

# Goodman's Regression (fast baseline)
good <- ei_good(
  data = gwinnett_ei,
  cand_cols = cands,
  race_cols = races,
  totals_col = "turnout"
)
summary(good)

# Iterative EI
iter <- ei_iter(
  data = gwinnett_ei,
  cand_cols = cands,
  race_cols = races,
  totals_col = "turnout",
  name = "Iterative EI"
)

# RxC EI
rxc <- ei_rxc(
  data = gwinnett_ei,
  cand_cols = cands,
  race_cols = races,
  totals_col = "turnout",
  name = "RxC EI"
)

# Compare results
plot(iter, rxc)
```

The top panel shows that the majority of white voters voted for Brian Kemp, who won this election. The middle panel shows the estimated preferences of black voters. The estimates indicate that black voters strongly preferred Stacey Abrams over Brian Kemp.
### RPV visualization with eiExpand
Use `rpv_toDF()` to convert results into a format compatible with `eiExpand::rpv_plot()`:

```
library(eiExpand)

# Convert ei_iter results to plot-ready dataframe
iter_df <- rpv_toDF(
  rpv_results = iter,
  model = ,
  jurisdiction = "Gwinnett",
  candidate = c("Kemp", "Abrams", "Metz"),
  preferred_candidate = c("White", "Black", "Other"),
  party = c("Republican", "Democratic", "Libertarian"),
  election_type = "General",
  year = "2018",
  contest = "Governor"
)

# Plot RPV results
rpv_plot(iter_df)
```

### VAP-denominator normalization
When using voting age population (VAP) as the denominator (instead of total votes), use `rpv_normalize()` to condition estimates on voters only:

```
# Run EI with a NoVote column
iter_vap <- ei_iter(
  data = my_data,
  cand_cols = c("pct_cand1", "pct_cand2", "pct_novote"),
  race_cols = c("pct_white", "pct_black"),
  totals_col = "total_vap"
)

# Normalize to remove NoVote
norm <- rpv_normalize(
  ei_object = iter_vap,
  cand_cols = c("pct_cand1", "pct_cand2"),
  race_cols = c("pct_white", "pct_black")
)

# Convert to plot-ready format
norm_df <- rpv_toDF(
  rpv_results = norm,
  model = "ei vap",
  ...
)
```

Please refer to the package vignettes for detailed walkthroughs. To view these in RStudio, enter `browseVignettes("eiCompare")` in the console after installing the package.
## Platform dependencies
The following platform dependencies may be required on Ubuntu/Debian based systems: sudo apt install libfftw3-dev fftw-dev
## Learn More
  * To learn about R programming, see [Hands-On Programming with R](https://rstudio-education.github.io/hopr/) and [R for data science](https://r4ds.had.co.nz/)
  * To learn more about the role of ecological inference in voting rights, visit the [eiCompare website](https://rpvote.github.io/voting-rights/)


## About
Comparing ecological inference techniques 
[rpvote.github.io/voting-rights/](https://rpvote.github.io/voting-rights/ "https://rpvote.github.io/voting-rights/")
### Topics
### Resources
### Code of conduct
### Contributing
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/RPVote/eiCompare).
[ Activity](https://github.com/RPVote/eiCompare/activity)
[ Custom properties](https://github.com/RPVote/eiCompare/custom-properties)
### Stars
**10** stars 
### Watchers
**7** watching 
### Forks
[ **7** forks](https://github.com/RPVote/eiCompare/forks)
[ 1 tags ](https://github.com/RPVote/eiCompare/tags)
##  [Contributors 10](https://github.com/RPVote/eiCompare/graphs/contributors)
## Languages
  * [ R 100.0% ](https://github.com/RPVote/eiCompare/search?l=r)


You can’t perform that action at this time. 
