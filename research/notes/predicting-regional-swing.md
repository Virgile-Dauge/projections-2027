---
title: Predicting Regional Swing
id: predicting-regional-swing
tags:
- projections-electorales-bureaux-2027-b0b1c4
- swing-methods
- regional-swing
- uk-elections
created: '2026-07-21T18:34:53.801087Z'
updated: '2026-07-21T18:39:17.773375Z'
source: https://www.electoralcalculus.co.uk/blogs/regional_swing.html
source_domain: www.electoralcalculus.co.uk
fetched_at: '2026-07-21T18:34:53.762080Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Electoral Calculus (UK, 2009) demonstrates empirically why plain Uniform
  National Swing (UNS) fails at fine geographic granularity, and how to correct it
  with regional-level survey data. Using a large-sample (n=32,268) YouGov regional
  megapoll from June 2009 broken down by 11 GB regions, they show swing was highly
  non-uniform between 2005 and 2009: Conservatives gained just 2.4 points in the South
  West but 12.5 points in the North, while Labour lost only 8.8 points in the South
  West but 21.9 points in the North -- both far from the national average change.
  At the 2005 election, regional swing deviations alone accounted for 14 mis-predicted
  seats versus a plain-UNS baseline. Applying regional swing correction (vs. plain
  uniform swing) to the June 2009 poll shifted the seat projection by +28 Conservative
  / -33 Labour seats relative to a uniform-swing baseline projection -- a large practical
  correction. The piece also finds persistent geographic patterns across two different
  periods (1992-2005 and 2005-2009): Labour gains relatively in the south, loses relatively
  in the north; Conservatives regain ground in Wales and (reversing prior losses)
  in London. Notes a key data constraint: national polls (~1,000 respondents) yield
  only ~100 per region, too small to estimate regional swing reliably -- large special-purpose
  regional megapolls are required, and these are infrequent.'
---

*Suggested by [[uniform-national-swing-wikipedia]] — cited by Wikipedia UNS stub as primary reference on predicting regional swing*

[Services](https://www.electoralcalculus.co.uk/services_general.html)
  * [Polling Regression Analysis](https://www.electoralcalculus.co.uk/services_polling.html)
  * [Election Predictions](https://www.electoralcalculus.co.uk/services_electoral.html)
  * [Electoral and Political Data](https://www.electoralcalculus.co.uk/services_data.html)
  * [Commercial Polling](https://www.electoralcalculus.co.uk/services_commercial.html)
  * [Customised Maps & Solutions](https://www.electoralcalculus.co.uk/services_solutions.html)


[UK Predictions](https://www.electoralcalculus.co.uk/prediction_home.html)
  * [Prediction home](https://www.electoralcalculus.co.uk/prediction_home.html)
  * [Your Prediction](https://www.electoralcalculus.co.uk/userpoll.html)
  * [Northern Ireland](https://www.electoralcalculus.co.uk/northernireland.html)


[UK Resources](https://www.electoralcalculus.co.uk/resources_home.html)
  * [Historical Data](https://www.electoralcalculus.co.uk/flatfile.html)


[Articles](https://www.electoralcalculus.co.uk/blogs/index.html)


  * Search the Electoral Calculus site:


  * [Polling Regression Analysis](https://www.electoralcalculus.co.uk/services_polling.html)
  * [Election Predictions](https://www.electoralcalculus.co.uk/services_electoral.html)
  * [Electoral and Political Data](https://www.electoralcalculus.co.uk/services_data.html)
  * [Commercial Polling](https://www.electoralcalculus.co.uk/services_commercial.html)
  * [Customised Maps & Solutions](https://www.electoralcalculus.co.uk/services_solutions.html)
  * [User home page](https://www.electoralcalculus.co.uk/cgi-bin/login.py)


  * [Prediction home](https://www.electoralcalculus.co.uk/prediction_home.html)
  * [Your Prediction](https://www.electoralcalculus.co.uk/userpoll.html)
  * [Northern Ireland](https://www.electoralcalculus.co.uk/northernireland.html)


  * [Historical Data](https://www.electoralcalculus.co.uk/flatfile.html)




[Home](https://www.electoralcalculus.co.uk/homepage.html) / [Articles](https://www.electoralcalculus.co.uk/blogs/index.html) / Regional Swing
# Predicting Regional Swing
# Predicting Regional Swing
#### First posted 22 August 2009
The simplest sort of prediction is called the _Uniform National Swing_ which is a rather crude approximation and assumes no regional variation across the country. But using the results of a recent large _YouGov_ poll, we can measure the extent of regional changes of opinion to get a more accruate prediction. This article describes how we do this and what the results are. 
## 1. Regional opinion survey
The simple _Uniform National Swing_ model assumes that the changes in support are uniform across the country. In other words, if the Conservatives gain 5% nationally, they will gain 5% in each region and consituency of the country. But the actual results are more complicated than this. In past elections we have seen non-uniform swing. For instance between 2001 and 2005, the Conservatives increased their vote share by 0.5% nationally. But within this average, there were different regional trends: they gained 3% in Essex but lost 1.7% in Yorkshire. 
At the [2005 election](https://www.electoralcalculus.co.uk/trackrecord_05errors.html), such regional swing accounted for 14 mis-predicted seats. 
To make a more accurate prediction we need to estimate the size of these regional swing effects. But this cannot be done from national opinion polls alone. National opinion polls have a sample size of about 1,000 people, equivalent to 100 people per region, which is not enough to estimate opinion accurately. We need an opinion poll which surveys at least 1,000 people in each region of the country. Such polls are infrequent, but fortunately _YouGov_ recently conducted one on behalf of Channel 4 for the European elections ([YouGov poll details](http://www.yougov.co.uk/extranets/ygarchives/content/pdf/Megapoll_EuroElections.pdf)). The poll of 32,268 people was conducted between 29 May and 4 June 2009, and the headline results were Con 37%, Lab 22%, Lib 19% and Other 22%. 
We are very grateful to _YouGov_ for making the regional breakdown of their poll available to _Electoral Calculus_. 
The table below shows (1) the breakdown of support by region as measured at the start of June 2009 by _YouGov_ , (2) regional support as at the general election in May 2005, and (3) the changes from 2005 to 2009 which we call the _Regional Swings_. (Please see the notes at the end of this article to explain some small numerical discrepancies.)   
| (1) Regional Support June 2009(source _YouGov_)   | (2) General Election ResultMay 2005   | (3) Regional Swing2005 - 2009   |  
| --- | --- | --- |  
| **Area**  | Con %  | Lab %  | Lib %  | Nat %  | Oth %   | Con %  | Lab %  | Lib %  | Nat %  | Oth %   | Con %  | Lab %  | Lib %  | Nat %  | Oth %   |  
| Scotland  | 21.0  | 27.0  | 13.0  | 30.0  | 9.0  | 15.8  | 39.5  | 22.6  | 17.7  | 4.4  | 5.2  | -12.5  | -9.6  | 12.3  | 4.6  |  
| The North  | 32.0  | 31.0  | 20.0  | 17.0  | 19.5  | 52.9  | 23.3  | 4.3  | 12.5  | -21.9  | -3.3  | 12.7  |  
| North West  | 32.0  | 28.0  | 17.0  | 23.0  | 28.7  | 45.0  | 21.3  | 5.0  | 3.3  | -17.0  | -4.3  | 18.0  |  
| Yorks/Humber  | 33.0  | 25.0  | 19.0  | 23.0  | 29.1  | 43.6  | 20.7  | 6.6  | 3.9  | -18.6  | -1.7  | 16.4  |  
| Wales  | 30.0  | 26.0  | 15.0  | 12.0  | 17.0  | 21.4  | 42.7  | 18.4  | 12.6  | 4.9  | 8.6  | -16.7  | -3.4  | -0.6  | 12.1  |  
| West Midlands  | 40.0  | 23.0  | 18.0  | 19.0  | 34.8  | 38.9  | 18.6  | 7.7  | 5.2  | -15.9  | -0.6  | 11.3  |  
| East Midlands  | 40.0  | 24.0  | 18.0  | 18.0  | 37.0  | 38.6  | 18.4  | 6.0  | 3.0  | -14.6  | -0.4  | 12.0  |  
| Anglia  | 47.0  | 17.0  | 16.0  | 20.0  | 43.3  | 29.8  | 21.8  | 5.1  | 3.7  | -12.8  | -5.8  | 14.9  |  
| South West  | 41.0  | 14.0  | 23.0  | 22.0  | 38.6  | 22.8  | 32.6  | 6.0  | 2.4  | -8.8  | -9.6  | 16.0  |  
| London  | 40.0  | 25.0  | 18.0  | 17.0  | 31.9  | 38.9  | 21.9  | 7.3  | 8.1  | -13.9  | -3.9  | 9.7  |  
| South East  | 50.0  | 13.0  | 20.0  | 17.0  | 45.0  | 24.4  | 25.4  | 5.2  | 5.0  | -11.4  | -5.4  | 11.8  |  
| **Great Britain**  | **38.3**  | **21.9**  | **18.1**  | **3.3**  | **18.6**  | **33.1**  | **36.1**  | **22.7**  | **2.2**  | **5.8**  | **5.1**  | **-14.3**  | **-4.7**  | **1.0**  | **12.8**  |  
The national picture is that the Conservatives have gained about 5% support since May 2005, and Labour have lost 14%. The Lib Dems have lost 5% and Other parties have gained 14%. 
Regionally, those trends are repeated in that the Conservatives have gained support in every region and Labour has lost support in every region. But although the direction of change is the same, the sizes of the changes are not. For instance, the Conservatives have gained only 2.4% support in the South West, but 12.5% in the North. Similarly Labour have lost only 8.8% in the South West, but 21.9% in the North. 
## 2. Regional swing analysis
We can see these differences of swing in a more systematic way. Let us take the table of regional swings and subtract from it the average national swing. This will show us (4) the differences between the regional swings and the national swing.   
| (4) Regional Swing Differentials2005 - 2009  |  
| --- |  
| **Area**  | Con %  | Lab %  | Lib %  | Nat %  | Oth %  | **Comment**  |  
| Scotland  | 0.1  | 1.8  | -4.9  | 12.3  | -9.2  | Strong SNP gain over LibDem and Others  |  
| The North  | 7.4  | -7.6  | 1.4  | -1.1  | Strong Con gain over Lab  |  
| North West  | -1.8  | -2.7  | 0.4  | 4.2  | Others gain over Con and Lab  |  
| Yorks/Humber  | -1.2  | -4.3  | 3.0  | 2.6  | LibDem gain over Lab  |  
| Wales  | 3.5  | -2.4  | 1.3  | -0.6  | -1.7  | Con gain over Lab  |  
| West Midlands  | 0.1  | -1.6  | 4.1  | -2.5  | LibDem gain over Others  |  
| East Midlands  | -2.1  | -0.3  | 4.3  | -1.8  | LibDem gain over Con  |  
| Anglia  | -1.4  | 1.5  | -1.1  | 1.1  | Small Lab gain over Con  |  
| South West  | -2.7  | 5.5  | -4.9  | 2.2  | Strong Lab gain over LibDem  |  
| London  | 3.0  | 0.4  | 0.8  | -4.1  | Con gain over Others  |  
| South East  | -0.1  | 2.9  | -0.7  | -2.0  | Lab gain over Others  |  
| **Great Britain**  | **0.0**  | **0.0**  | **0.0**  | **1.0**  | **-1.0**  |  
We remember that this is not a table of absolute swings. Absolute swings (table 3) show the Conservatives gaining everywhere and Labour losing everywhere. This is a table of swings relative to the national average. So, on average, everything balances out. For example, if the Conservatives perform more strongly than average in the North, they must do worse than average somewhere else, such as the North West. Thus the population-weighted average of each column is zero. (See notes below for why Nat and Others are different). 
We see the following trends: 
  * The Conservatives do better than average in the North, Wales and London. 
  * The Conservatives did worse than average in the East Midlands and South West. 
  * Labour did better than average in the South West and South East. 
  * Labour did worse than average in the North, North West, Yorks/Humber and Wales. 

  
| **Party**  | **Relative Gain**  | **Relative Loss**  |  
| --- | --- | --- |  
| **CON**  | North, Wales, London  | East Midlands, South West  |  
| **LAB**  | South West, South East  | North, North West, Yorks/Humber, Wales  |  
| **LIB**  | Yorks/Humber, West Midlands, East Midlands  | Scotland, South West  |  
Overall there is a notable "depolarisation" as parties lose ground in their heartlands and make relative gains elsewhere. 
## 3. Comparison with recent trends
We can compare these differentials with recent history. We have chosen the period 1992-2005 because **Apr 1992** is the last election won by the Conservatives and **May 2005** is the most recent election won by Labour. So this period captures the change in electoral geography due to the rise of the moderate New Labour and the waning of the Conservatives.   
| (5) Regional Swing1992 - 2005  | (6) Regional Swing Differentials1992 - 2005  |  
| --- | --- |  
| **Area**  | Con %  | Lab %  | Lib %  | Nat %  | Oth %   | Con %  | Lab %  | Lib %  | Nat %  | Oth %  |  
| Scotland  | -9.8  | 0.5  | 9.5  | -3.8  | 3.6  | -0.2  | -0.4  | 5.2  | -3.8  | -0.7  |  
| The North  | -10.5  | -1.0  | 7.8  | 3.7  | -0.9  | -2.0  | 3.5  | -0.6  |  
| North West  | -10.5  | 1.1  | 5.5  | 3.9  | -0.9  | 0.1  | 1.2  | -0.4  |  
| Yorks/Humber  | -8.6  | -0.5  | 3.4  | 5.7  | 1.0  | -1.4  | -0.9  | 1.4  |  
| Wales  | -7.2  | -6.8  | 6.0  | 3.7  | 4.3  | 2.4  | -7.8  | 1.7  | 3.7  | 0.0  |  
| West Midlands  | -9.3  | -0.2  | 3.9  | 5.6  | 0.2  | -1.2  | -0.4  | 1.3  |  
| East Midlands  | -10.3  | 1.3  | 4.4  | 4.6  | -0.8  | 0.3  | 0.1  | 0.3  |  
| Anglia  | -9.1  | 3.8  | 1.6  | 3.7  | 0.4  | 2.8  | -2.7  | -0.6  |  
| South West  | -9.1  | 3.2  | 1.6  | 4.4  | 0.5  | 2.2  | -2.7  | 0.1  |  
| London  | -13.4  | 1.9  | 6.0  | 5.6  | -3.8  | 0.9  | 1.7  | 1.3  |  
| South East  | -10.0  | 5.9  | 0.4  | 3.7  | -0.4  | 4.9  | -3.9  | -0.6  |  
| **Great Britain**  | **-9.6**  | **1.0**  | **4.3**  | **-0.2**  | **4.5**  | **0.0**  | **0.0**  | **0.0**  | **-0.2**  | **0.2**  |  
The regional trends over the period 1992-2005 are: 
  * The Conservatives do better than average in Wales. 
  * The Conservatives did worse than average in London. 
  * Labour did better than average in Anglia, South West and South East. 
  * Labour did worse than average in the North and Wales. 

  
| **Party**  | **Relative Gain**  | **Relative Loss**  |  
| --- | --- | --- |  
| **CON**  | Wales  | London  |  
| **LAB**  | Anglia, South West, South East  | North, Wales  |  
| **LIB**  | Scotland, North  | Anglia, South West, South East  |  
Interestingly, there is quite a similar pattern over the two periods 1992-2005 and 2005-2009. Labour continues to gain (relatively) in the south and lose (relatively) in the north of the country. The Conservatives continue to gain ground in Wales, though they have reversed their losses in London, perhaps due to Boris Johnson's election as mayor. The Liberal Democrats continue to gain ground in the north and lose relatively in the south. But in Scotland, their earlier gains have been reversed as the SNP increase their support. 
## 4. Impact on Predictions
We can use these results to make a more detailed prediction of the next general election result. We can use both the national _YouGov_ support figures, and the detailed regional support figures to make two separate predictions. We can then look at the difference between the two predictions to estimate the impact of regional trends on the result.   
| Party  | 2005 Seats  | Uniform PredictionJune 2009  | Regional PredictionJune 2009  | Regional Impact  |  
| --- | --- | --- | --- | --- |  
| CON  | 208  | 371  | 399  | **+28**  |  
| LAB  | 346  | 193  | 160  | **-33**  |  
| LIB  | 67  | 51  | 50  | **-1**  |  
The effect of the regional swing differentials in June 2009 is to give the Conservatives approximately another 30 seats at the expense of Labour. Running a similar calculation at August 2009 using the [Regional Predictor](https://www.electoralcalculus.co.uk/userregpoll.html) showed the Conservatives gaining about 10 seats. 
The Regional Predictor now has the added feature to make predictions incorporating the regional swings observed from this large _YouGov_ poll.
## Acknowledgements
We would like to express our gratitude to Peter Kellner and _YouGov_ for making details of their regional poll available to us.
## Appendix: Numerical Notes
_YouGov_ themselves give some health warnings with regard to the regional support levels:
  * During the weighting process of the raw data, there is no control between region and party affiliation. This means that the weighted sum of regional support may not exactly equal the headline national support figures. 
  * Figures have been adjusted to compensate for the difference between parties' predicted and actual shares of the votes at the European elections in June 2009. 
  * The "Others" are currently very high, and the LibDems slightly low. This may have changed by the time of the next election. 


Additionally, _Electoral Calculus_ gives its own cautions: 
  * Our definitions of regions may be slightly different from _YouGov_ , so our figures for the general election result by region are different. Nonetheless, the difference of regions compared with the national trend should still be meaningful. 
  * There isn't a national implied swing for the Nationalist parties (SNP and Plaid Cymru), so their regional swing differentials are just the changes in support since 2005 and do not add up to zero for Nat and Oth. 


SERVICES
### Affordable MRP Regression Polling and Consultancy
We're a quantitative political consultancy specialising in analysis and models for electoral and market research projects. Discover how we can work together.
[**Let's work together**](https://www.electoralcalculus.co.uk/services_together.html)
[Find out more](https://www.electoralcalculus.co.uk/services_together.html)
### We provide innovative and affordable MRP and consulting
Specialising in quantitative analysis and models for electoral and market research projects, discover how we can work together.
[**Let's work together**](https://www.electoralcalculus.co.uk/services_together.html)
#### [Services](https://www.electoralcalculus.co.uk/services_general.html)
[Polling Regression Analysis](https://www.electoralcalculus.co.uk/services_polling.html)
[Election Predictions](https://www.electoralcalculus.co.uk/services_electoral.html)
[Electoral and Political Data](https://www.electoralcalculus.co.uk/services_data.html)
[Customised Maps & solutions](https://www.electoralcalculus.co.uk/services_solutions.html)
[Case Studies](https://www.electoralcalculus.co.uk/services_casestudy_ge2019.html)
#### [UK Predictions](https://www.electoralcalculus.co.uk/prediction_home.html)
[Your Seat](https://www.electoralcalculus.co.uk/newseatlookup.html)
[Your Prediction](https://www.electoralcalculus.co.uk/userpoll.html)
[Our prediction](https://www.electoralcalculus.co.uk/prediction_main.html)
[Scotland](https://www.electoralcalculus.co.uk/scotland.html)
[Northern Ireland](https://www.electoralcalculus.co.uk/northernireland.html)
#### [UK Resources](https://www.electoralcalculus.co.uk/resources_home.html)
[New Boundaries 2023](https://www.electoralcalculus.co.uk/boundaries2023.html)
[3D Politics](https://www.electoralcalculus.co.uk/pol3d_main.html)
[Historical data](https://www.electoralcalculus.co.uk/flatfile.html)
**Consultancy Contact:** enquiry@electoralcalculus.co.uk
**Media Contact:** Telephone: 020 3627 8141, media@electoralcalculus.co.uk
[Back to top](https://www.electoralcalculus.co.uk/blogs/regional_swing.html#top)
Copyright 2026 Electoral Calculus Ltd. All rights reserved | [About Us](https://www.electoralcalculus.co.uk/aboutus.html) | [Terms & Conditions](https://www.electoralcalculus.co.uk/terms_and_conds.html) | [Privacy Policy](https://www.electoralcalculus.co.uk/dataprivacy.html) [Branding & UX by Designbull.co.uk](https://designbull.co.uk/)
POWERED BY 
