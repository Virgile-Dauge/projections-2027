---
title: 'GitHub - mggg/ecological-inference: Ecological inference, in Python · GitHub'
id: github-mgggecological-inference-ecological-inference-in-python-github
tags:
- ecological-inference
- pyei
- voting-rights-act
created: '2026-07-21T19:07:10.877901Z'
updated: '2026-07-21T19:42:36.595458Z'
source: https://github.com/mggg/ecological-inference
source_domain: github.com
fetched_at: '2026-07-21T19:07:10.836618Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: 'PyEI (mggg/ecological-inference, MIT, v1.1.4 Jun 2025) is a Python ecological-inference
  library purpose-built for Racially Polarized Voting (RPV) analysis under the US
  Voting Rights Act framework (Thornburg v. Gingles 1982 standard). Bundles multiple
  EI estimators (2x2 iterative, RxC/multinomial-Dirichlet via PyMC) with shared reporting/plotting,
  uncertainty quantification, and cross-method comparison tooling. Pairs precinct-level
  election results with precinct-level demographic composition to infer group-level
  vote choice — the same statistical family (King 1997 ecological inference, Goodman
  regression) referenced as a projection-method rung in the French bureau-de-vote
  research question. Peer-reviewed citation: Knudson, Schoenbach & Becker (2021),
  ''PyEI: A Python package for ecological inference,'' Journal of Open Source Software
  6(64):3397, doi:10.21105/joss.03397 — a fetchable primary source.'
---

[Skip to content](https://github.com/mggg/ecological-inference#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/mggg/ecological-inference) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/mggg/ecological-inference) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/mggg/ecological-inference) to refresh your session. Dismiss alert
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/mggg/ecological-inference).
/ **[ecological-inference](https://github.com/mggg/ecological-inference) ** Public
  * [ Notifications ](https://github.com/login?return_to=%2Fmggg%2Fecological-inference) You must be signed in to change notification settings
  * [ Fork 14 ](https://github.com/login?return_to=%2Fmggg%2Fecological-inference)
  * [ Star  35 ](https://github.com/login?return_to=%2Fmggg%2Fecological-inference)


[**9** Branches](https://github.com/mggg/ecological-inference/branches)[](https://github.com/mggg/ecological-inference/tags)
Go to file
Open more actions menu
## Folders and files  
| Name  | Name  | Last commit message  | Last commit date  |  
| --- | --- | --- | --- |  
| 
## Latest commit
failure Mar 15, 2026 [214a24a](https://github.com/mggg/ecological-inference/commit/214a24a7ca79c6f205b40dc6b720d98aaacdcca4) · Mar 15, 2026
## History
[446 Commits](https://github.com/mggg/ecological-inference/commits/main/)Open commit details 446 Commits  |  
| [.github/workflows](https://github.com/mggg/ecological-inference/tree/main/.github/workflows "This path skips through empty directories")  | [.github/workflows](https://github.com/mggg/ecological-inference/tree/main/.github/workflows "This path skips through empty directories")  |   | Jul 8, 2024  |  
|   |   |   | Aug 17, 2021  |  
| [Bumpy pymc version to allow numpy 2+](https://github.com/mggg/ecological-inference/commit/97535f12505664dae528eb851c745e5d8a36cbcc "Bumpy pymc version to allow numpy 2+")  | Jun 17, 2025  |  
|   |   | [Add scripts to lint and test locally](https://github.com/mggg/ecological-inference/commit/8b9dc9e9712bbe4e08a5264ddc2a59050235ccb8 "Add scripts to lint and test locally")  | Aug 3, 2020  |  
| [turn off to_netcdf testing. Should figure this out later but it is cu…](https://github.com/mggg/ecological-inference/commit/ffd12dd685f5568b3a178cd3c4abed0748fd8c99 "turn off to_netcdf testing. Should figure this out later but it is currently failing on gh but not locally")  | Jul 8, 2024  |  
|   |   | [Add data utility, update demo](https://github.com/mggg/ecological-inference/commit/9553b9b15b6df37b6ebf27d8d1362097d40672c3 "Add data utility, update demo")  | Aug 3, 2020  |  
|   |   | [Upgrade pymc, make new release.](https://github.com/mggg/ecological-inference/commit/9972f230fd8122d73142ef7f2c3a1bc9226f87b0 "Upgrade pymc, make new release.")  | Dec 10, 2024  |  
|   |   |   | Jul 26, 2020  |  
|   |   |   | Mar 15, 2026  |  
|   |   |   | Jul 26, 2020  |  
|   |   | [Bumpy pymc version to allow numpy 2+](https://github.com/mggg/ecological-inference/commit/97535f12505664dae528eb851c745e5d8a36cbcc "Bumpy pymc version to allow numpy 2+")  | Jun 17, 2025  |  
|   |   | [Bumpy pymc version to allow numpy 2+](https://github.com/mggg/ecological-inference/commit/97535f12505664dae528eb851c745e5d8a36cbcc "Bumpy pymc version to allow numpy 2+")  | Jun 17, 2025  |  
| View all files |  
## Repository files navigation
PyEI is a Python library for inferential techniques related to group voting behavior. The target audience is the analyst who seeks to identify and measure Racially Polarized Voting (RPV).
Here, RPV refers specifically to the legal concept developed through case law around the Voting Rights Act of 1965, especially following the landmark Supreme Court case _**Thornburg v. Gingles**_ (1982). Considered the “evidentiary linchpin” for vote dilution cases, demonstrating meaningful levels of polarization is a necessary, but not sufficient, condition that plaintiffs must satisfy to advance a VRA claim.
Toward that end, inference methods use observed data (historical election results), pairing voting outcomes with demographic information for the precincts in a given jurisdiction, to infer voting patterns by demographic group.
PyEI brings together a variety of inference methods in one place and facilitates reporting and plotting results; quantifying the uncertainty associated with results under a given model; making comparisons between methods; and bringing relevant diagnostic tools to bear on ecological inference methods.
PyEI is under active development, so expect rough edges -- bug reports and feature requests are welcome.
## Want to use PyEI? Start here.
### Installation
You can install the latest release from `PyPi` with:

```
pip install pyei

```

Or, install directly from GitHub for the most up-to-date (but potentially less stable) version:

```
pip install git+https://github.com/mggg/ecological-inference.git

```

If you would like to explore PyEI without installation, you can explore this [interactive Colab notebook](https://colab.research.google.com/drive/1Vr1kKAAHgdcUhPrpFsYc1Kz31nbcpZjP#scrollTo=_ASEm5L3UUAS) (just note that inference might be slow!)
### Example notebooks
Check out the [intro notebooks](https://github.com/mggg/ecological-inference/tree/main/pyei/intro_notebooks) and [example notebooks](https://github.com/mggg/ecological-inference/tree/main/pyei/examples) for sample code that shows how to run and adjust the various models in PyEI on datesets.
If you are new to ecological inference generally, start with [`pyei/intro_notebooks/Introduction_toEI.ipynb`](https://github.com/mggg/ecological-inference/blob/main/pyei/intro_notebooks/Introduction_to_EI.ipynb).
If you are familiar with ecological inference and want an overview of PyEI and how to use it (with examples), then start with [`intro_notebooks/PyEI_overview.ipynb`](https://github.com/mggg/ecological-inference/blob/main/pyei/intro_notebooks/PyEI_overview.ipynb).
To explore EI's plotting functionality, check out [`pyei/intro_notebooks/Plotting_with_PyEI.ipynb`](https://github.com/mggg/ecological-inference/blob/main/pyei/intro_notebooks/Plotting_with_PyEI.ipynb).
For more work with two-by-two examples, see in [`pyei/examples/santa_clara_demo.ipynb`](https://github.com/mggg/ecological-inference/blob/main/pyei/examples/santa_clara_demo.ipynb).
For more work with r-by-c examples, see [`pyei/examples/santa_clara_demo_r_by_c.ipynb`](https://github.com/mggg/ecological-inference/blob/main/pyei/examples/santa_clara_demo_r_by_c.ipynb).
For examples of model comparison and checking steps with PyEI, see [`pyei/examples/model_eval_and_comparison_demo.ipynb`](https://github.com/mggg/ecological-inference/blob/main/pyei/examples/model_eval_and_comparison_demo.ipynb).
### Issues
Feel free to file an issue if you are running into trouble or if there is a feature you'd particularly like to see, and we will do our best to get to it!
## Want to contribute to PyEI? Start here.
Contributions are welcome!
Uses Python 3.10. After cloning the repository, you should be able to use either `virtualenv` or `conda` to set up your environment. The second (`conda`) is probably easier for development, but `virtualenv` is used for the project's CI.
Here is how to create and activate each environment. See the docs for more elaborate details:
### Install with virtualenv

```
virtualenv pyei_venv           # create virtualenv
source pyei_venv/bin/activate  # activate virtualenv
python -m pip install -U pip   # upgrade pip
python -m pip install -e .     # install project locally
python -m pip install -r requirements-dev.txt  # install dev requirements
```

### Install with conda

```
conda create --name pyei --channel conda-forge python=3.10 --file requirements.txt --file requirements-dev.txt # create conda environment and install requirements
conda activate pyei
pip install -e . #install project locally
```

### Testing
After making changes, make sure everything works by running

```
./scripts/lint_and_test.sh
```

This will also run automatically when you make a pull request, so if you have trouble getting that to run, just open the PR, and we can help!
## Citation
If you are using PyEI, please cite it as:
Knudson et al., (2021). PyEI: A Python package for ecological inference. Journal of Open Source Software, 6(64), 3397, <https://doi.org/10.21105/joss.03397>
BibTeX:

```
@article{Knudson2021,
  doi = {10.21105/joss.03397},
  url = {https://doi.org/10.21105/joss.03397},
  year = {2021},
  publisher = {The Open Journal},
  volume = {6},
  number = {64},
  pages = {3397},
  author = {Karin C. Knudson and Gabe Schoenbach and Amariah Becker},
  title = {PyEI: A Python package for ecological inference},
  journal = {Journal of Open Source Software}
}

```

## About
Ecological inference, in Python 
### Resources
### License
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/mggg/ecological-inference).
[ Activity](https://github.com/mggg/ecological-inference/activity)
[ Custom properties](https://github.com/mggg/ecological-inference/custom-properties)
### Stars
**35** stars 
### Watchers
**6** watching 
### Forks
[ **14** forks](https://github.com/mggg/ecological-inference/forks)
##  [Releases 12](https://github.com/mggg/ecological-inference/releases)
[ v1.1.4 Latest  Jun 18, 2025 ](https://github.com/mggg/ecological-inference/releases/tag/v1.1.4)
##  [Contributors 11](https://github.com/mggg/ecological-inference/graphs/contributors)
## Languages
  * [ Jupyter Notebook 96.5% ](https://github.com/mggg/ecological-inference/search?l=jupyter-notebook)
  * [ Python 3.4% ](https://github.com/mggg/ecological-inference/search?l=python)
  * Other 0.1%


You can’t perform that action at this time. 
