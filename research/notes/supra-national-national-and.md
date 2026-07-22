---
title: Supra National, National and
id: supra-national-national-and
tags:
- projections-electorales-bureaux-2027-b0b1c4
- locus-baseline-election-source-2027
- second-order-elections
- turnout
- multilevel-model
created: '2026-07-21T19:34:18.077079Z'
updated: '2026-07-21T19:42:36.620948Z'
source: https://publications.jrc.ec.europa.eu/repository/bitstream/JRC108755/jrc108755_tech_rep.pdf
source_domain: publications.jrc.ec.europa.eu
fetched_at: '2026-07-21T19:34:18.076852Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: paper
deprecated: false
summary: 'Fiorino, Pontarollo (Joint Research Centre) & Ricciuti (2017, JRC Technical
  Report EUR 28856 EN, doi:10.2760/847841) — modèle multiniveau du taux de participation
  aux élections européennes sur 164 régions NUTS2, EU-14, 4 scrutins européens. Le
  papier situe le vote EP à l''intersection de trois dimensions : supranationale (attitudes
  envers l''UE), nationale (clivages politiques domestiques) et locale/régionale (variables
  socio-économiques). Résultats : rôle significatif du vote obligatoire, des clivages
  politiques domestiques, des conditions du marché du travail et de la confiance envers
  l''UE dans la participation ; pas d''effet du PIB par habitant ; les électeurs âgés
  votent davantage. Citation pertinente pour Q1 (validité géographique) : « In this
  view, EP elections are second-order national elections because they debate and reflect
  essentially national politics (Reif and Schmitt, 1980). » Le papier ne teste PAS
  directement la corrélation géographique vote EP / vote national au niveau infranational
  (c''est un modèle de participation, pas de choix de parti), mais établit méthodologiquement
  que la variation régionale de comportement électoral aux européennes est en grande
  partie expliquée par des clivages politiques nationaux préexistants plutôt que par
  des dynamiques propres au scrutin européen — cohérent avec l''hypothèse que la structure
  géographique domestique domine le niveau national de swing.'
raw_file: raw/supra-national-national-and.pdf
---

Supra National, National and 
Regional Dimensions of Voter 
Turnout in European Parliament 
Elections 
Nadia Fiorino  
Nicola Pontarollo 
Roberto Ricciuti 
2017 
EUR 28856 EN 


---

This publication is a Technical report by the Joint Research Centre (JRC), the European Commission’s science 
and knowledge service. It aims to provide evidence-based scientific support to the European policymaking 
process. The scientific output expressed does not imply a policy position of the European Commission. Neither 
the European Commission nor any person acting on behalf of the Commission is responsible for the use that 
might be made of this publication. 
JRC Science Hub 
https://ec.europa.eu/jrc 
JRC108755 
EUR 28856 EN 
PDF 
ISBN 978-92-79-75757-0 
ISSN 1831-9424 
doi:10.2760/847841 
Luxembourg: Publications Office of the European Union, 2017 
© European Union, 2017 
Reuse is authorised provided the source is acknowledged. The reuse policy of European Commission documents 
is regulated by Decision 2011/833/EU (OJ L 330, 14.12.2011, p. 39). 
For any use or reproduction of photos or other material that is not under the EU copyright, permission must be 
sought directly from the copyright holders. 
How to cite this report: Fiorino N., Pontarollo N., Ricciuti R., (2017) Supra National, National and Regional 
Dimensions of Voter Turnout in European Parliament Elections, EUR 28856 EN, ISBN 978-92-79-75757-0, 
doi:10.2760/847841, JRC108755. 
All images © European Union 2017 


---

i 
Contents 
1 Introduction ...................................................................................................... 3 
2 Related literature ............................................................................................... 5 
3 Voter turnout in political space ............................................................................ 7 
4 Empirics ........................................................................................................... 9 
4.1 The dynamics of turnout in Europe ................................................................. 9 
4.2 Model specification, variables and methodology ............................................. 13 
5 Results ........................................................................................................... 18 
5.1 Baseline results ......................................................................................... 18 
5.2 Robustness checks ..................................................................................... 21 
6 Concluding remarks ......................................................................................... 23 
References ......................................................................................................... 24 
Appendix ............................................................................................................ 28 
List of tables ......................................................................................................... 1 
List of figures ........................................................................................................ 2 


---

 
2 
 
Supra National, National and Regional Dimensions 
of Voter Turnout in European Parliament 
Elections*  
 
 
Nadia Fiorino 
University of L’Aquila 
 
Nicola Pontarollo$ 
Joint Research Centre, 
European Commission 
 
Roberto Ricciuti** 
University of Verona and CESifo 
 
 
 
 
ABSTRACT 
We argue that the decision to vote in European Parliamentary (EP) elections lies at the 
intersection of three political dimensions: one related to the attitude of citizens towards the 
European Union, one to the characteristics of the national political system, and the third 
associated with socio-economic variables observed by voters at the local level. This paper 
investigates this intersection by analyzing the last four EP elections in the EU-14, for 164 
regions. We test a multilevel model. The results indicate a significant role of compulsory 
voting, domestic political cleavages, labor market conditions and trust in the EU. No 
evidence is found that GDP per capita affects turnout. Finally, the oldest segment of 
population seems more prone to vote than the youngest. 
 
 
 
 
Keywords: European Parliamentary elections; voter turnout; subnational variation; 
multilevel model. 
 
 
 
 
 
* This research was funded by the research program "Inequality and economic crises" within the project “Economic 
Crises and the Quality of Democracies in Europe” (PRIN project 2010WKTTJP_005). We thank Katharina Hofer and 
participants at the European Public Choice Conference 2016 (Freiburg) for comments. 
 
$The views expressed are the authors’ and do not necessarily correspond to those of the European Commission. 
 
** 
Corresponding 
author. 
Email: 
nadia.fiorino@univaq.it, 
nicola.pontarollo@ec.europa.eu, 
roberto.ricciuti@univr.it.  
 


---

 
3 
 
1 Introduction 
This paper re-interprets the previous studies on the determinants of voter behavior 
in European Parliamentary (EP) elections at the aggregate level. It focuses on the political 
dimension of such determinants: a supranational dimension that involves attitudes towards 
European institutions, a national dimension that emphasizes the role of the national political 
context, and a local dimension that refers to specific socio-economic and demographic 
characteristics.  
The variables we use are based on the general theory of voting behavior as well as 
on some other theoretical propositions more directly related to the EP itself; most of them 
are not novel per se. Nevertheless, placing the variables involved in the decision to go to 
the polls into a political space provides new opportunities to capture their multilevel nature 
strictly linked to the multilevel government that characterizes the complex relations 
between national and EU politics. The hierarchical model we test is the ‘natural’ consequence 
of our concept since it empirically examines the linkages between different political levels, 
lowering the risk of biased estimators and misleading results. 
Elections have proven to be a fruitful field of research. Within this wide area of 
investigation some studies are grounded on individual-level data, others on aggregate-level 
data, and still others on a mix of the two levels. Contributions on EP elections reproduce 
this distinction both in the theoretical propositions and in the choice of data. Most of the 
empirical studies are centered on individual data as well as on a mix of individual- and 
aggregate-level data. Although cross-country analyses on voter turnout based on 
aggregate-level data most likely yield valid inferences compared to individual level 
analyses,1 empirical system studies of EP elections are still scarce.  
Scholars have also noted the importance of space in relation to political issues and 
have emphasized the influence of local contexts and social interactions. Nevertheless, the 
empirical literature on voter turnout and more specifically, aggregate-level empirical studies 
of participation in EP elections generally overlook these aspects.2 The latter are indeed 
largely based on cross-national samples (Mattila, 2003; Hix and Marsh, 2007) and case 
studies (a single election or single country) and do not fully address the context and 
characteristics of elections at the specifically multilevel system of government where the 
responsibilities for policies are shared at the supranational, national and regional level. 
Cross-country studies make the implicit assumption that countries are positioned on 
their steady-state equilibria values for turnout. However, a closer look at the data shows a 
more complex picture of participation rates in EP elections. Fig. 1 displays turnout levels in 
164 European regions in the 1999, 2004, 2009 and 2014 elections respectively. It indicates 
significant changes in the level of turnout in countries and regions over the last four EP 
elections and points out that voting behavior is heterogeneously distributed from one 
election to the other both between and within countries. In addition, several variables 
deemed determinants of electoral turnout (such as population density or income per capita) 
by previous studies and that we consider in our analysis are not homogeneous within a given 
country and vary over time. This suggests that the electoral mosaic of EP elections is the 
result of aggregate socio-economic, cultural and political processes that may take different 
forms and occur in different places. Lacking the processes that happen in sub-systems (i.e. 
considering a single observation for each country) involves a loss of information, and may 
therefore lead to incorrect statistical inferences.  
 
The rest of the paper is organized as follows. Section 2 reviews the literature on 
aggregate voter turnout and highlights some of the variables used in Section 3, where we 
provide a conceptual framework in which supranational, national and local levels interact. In 
                                           
1   See on this point the influential study of Kramer (1983) and more recently Van der Brug, van der Eijk and 
Franklin (2007). 
2    Few empirical studies taking into consideration this issue through spatial econometric techniques (Lacombe et 
al., 2014) or more traditional non-spatial estimation methods (Gerber et al., 2008) have been carried out. 
Sundstrom and Stockemer (2015) is currently the only aggregate study analyzing both national- and regional-
level characteristics of voter turnout in a sample of European country. Nevertheless, they focus on national 
parliamentary elections for a single year.   


---

 
4 
 
Section 4 we analyze the dynamics of the EP elections in our sample, the variables and 
empirical strategy. Section 5 sets out the results. Finally, Section 6 presents a discussion of 
our findings.  
 


---

 
5 
 
2 Related literature  
Empirical studies of the determinants of voter turnout in EP elections are rooted in the theory 
of voting behavior in general, as well as in other theories specific to EP elections. A number 
of surveys of voter turnout (Geys, 2006; Smets and van Ham, 2013; Cancela and Geys, 
2016) have been carried out. Most of the literature is based on the Downsian model (Downs, 
1957) in which the benefits and costs of voting are weighted and the decision to go to the 
polls emerges from this cost-benefit analysis. Several variables affect costs and benefits at 
the aggregate level. Institutional features such as compulsory voting, registration 
requirements and the type of electoral system have been considered. While compulsory 
voting is associated with higher turnout because it increases the probability of being caught 
not voting, registration requirements discourage voters since they increase the time 
required, the effort and the information costs of voting.  
Proportional representation (PR) systems increase voter turnout compared to 
majoritarian systems (see among others, Selb, 2009). The disproportionality between votes 
and seats in the latter lowers the incentive to go to the polls since voters, especially those 
that support small parties, may consider their vote wasted. Moreover, under PR, in each 
district most parties have a chance to win at least one seat, and therefore have an incentive 
to mobilize everywhere. Finally, PR leads to more parties, providing a wider choice for voters 
and thus increasing the likelihood that an individual voter can find a political platform 
reasonably close to his/her own opinions. 
Socio-economic factors (such as economic development, population size, population 
concentration, income inequality) may also affect the costs and benefits of voting and, as 
such, cross-national variations in turnout. In developed countries people are more informed 
and have more resources (including time) to devote to politics. This may increase the 
political involvement of citizens and stimulate voter turnout. Voters living in larger 
communities are less likely to consider their vote decisive for the outcome of the election, 
which decreases the benefits of voting. Contradictory theoretical predictions characterize 
the relationship between turnout and population density. In relatively low-density areas, 
community relations are closer and more direct (Overbye, 1995) and this may result in 
‘social pressure’ to vote. Further, politics is more personal (Blank, 1974), the candidates 
are well known and this lowers the information costs of voting. However, in countries with 
higher population densities, voters are more concentrated and easier to mobilize (Lipset, 
1981). Theoretical analyses of the relationship between income inequality and political 
participation are also conflicting. When income is unequally distributed, the poor are unable 
to influence politics and so tend to withdraw from the political arena (Goodin and Dryzek, 
1980). Conversely, greater income gaps intensify social conflict for redistribution between 
the poor and the rich, increasing possible gains and losses for the two groups in the 
elections, and therefore voter turnout (Meltzer and Richard, 1981). Most of the empirical 
studies in this field show a significant negative relationship (Anderson and Beramendi, 
2008; Dahl, 2006; Solt, 2008), some others (Oliver, 2001; Brady, 2004) support a positive 
sign.  
The literature has also analyzed the role of party systems in explaining cross-country 
variations in turnout. Most research incorporates the number of parties. On the one hand, 
as observed before, the more parties the higher the turnout. On the other hand, as Jackman 
(1987) suggests, multi-party systems usually produce coalition governments, which make 
elections less decisive because governments are the result of backroom agreements between 
parties, reducing the turnout. While almost all empirical research has found a negative 
correlation between the number of parties and turnout, the view that a higher number of 
parties reduces turnout because it leads to coalition governments is not empirically 
supported (Blais and Carty, 1990; Blais and Dobrzynska, 1998).  
The most famous explanation for EP elections is the so-called ‘second-order national 
election’ theory (Reif and Schmitt, 1980), which is rooted in theories of midterm elections in 
the United States. This theory is based on two key arguments. The national political arena 


---

 
6 
 
determines and dominates EP elections because they occur at a different time to the 
domestic ‘electoral cycle’. Strictly linked to this argument, the second key proposition is that 
people vote differently (i.e., people may vote or abstain) in ‘second-order’ EP elections 
because less is ‘at stake’ compared to 'first-order' national parliamentary elections. Various 
empirical studies support this model, showing that turnout is lower than in national elections, 
smaller parties perform better and parties in national government are punished, particularly 
during the midterm (van der Eijk and Franklin, 1996; Marsh, 1998; Hix and Marsh, 2011). 
These patterns of behavior are seen as signifying the reduced salience of EP elections.3 
Finally, also relevant is public opinion on European institutions. The attitudes to 
European democracy are founded on both the confidence in EU institutions and the quality 
of national institutions. Citizens use the quality of national institutions as a ‘proxy’ to evaluate 
EU institutions. While some scholars emphasize that positive appraisal of national institutions 
at the individual level spills over into greater satisfaction with EU institutions (Andersen 
1998; Holbot, 2012), others claim that higher corruption or poorer national institutions 
increase the support for EU democracy since the opportunity-cost of transferring sovereignty 
to Europe is lower (Sanchez Cuenca, 2000; Rohrschneider, 2002).  
Most of the studies of EP elections focus on a single country or on single elections; 
cross-country analyses using aggregate-level data are still rare (Mattila, 2003; Hix and 
Marsh, 2007) and are conducted at the national level, which makes it hard to capture the 
differences in electoral participation within a country. Instead, these aspects are relevant. 
The EU is characterized by a multilevel system of governance where the responsibilities for 
policies are allocated and impact on various levels of the hierarchical political system. 
Further, voting behavior depends on some contextual factors that are strictly linked to the 
specificity of the areas and territories. Political science literature has noted the importance 
of space on turnout (Cho and Rudolph, 2008). Nevertheless, to date, we are not aware of 
any empirical aggregate-level study of EP elections that has taken this aspect seriously into 
consideration.  
 
                                           
3 One of the most striking examples were the European and General Elections in the UK in 2014 and 2015. In 2014 
turnout was 34.2%, UKIP, Labour and Conservatives received 27.5%, 25.4% and 23.9%, respectively 
(http://www.bbc.com/news/events/vote2014/eu-uk-results), whereas one year later turnout was 66.1%, and the 
three parties received 12.6%,  30.4% and 36.9% respectively (http://www.bbc.com/news/election/2015/results).  


---

 
7 
 
3 Voter turnout in political space 
This section aims to interpret the previously surveyed literature on the determinants of voter 
turnout within an integrated framework that sets these variables into political spaces. We 
argue that the interplay between these spaces and the geographical characteristics of voter 
turnout gives a more comprehensive picture of the determinants of voting behavior in EP 
elections.  
The EU is a unique institutional setup since responsibilities are shared by national and 
European institutions. Voter turnout at EP elections is the result of a choice that occurs at 
the intersection of three different political spaces. One space directly involves supranational 
European institutions. Citizens’ choices are related to their opinion and attitudes to EU 
institutions and policies (Anderson, 1998; Holbot, 2012). Starting as a fairly technocratic 
process based on consensus between governments, the aim of achieving an ‘ever closer 
union’ has led to an increase in the number of decisions taken in Brussels which impact on 
the daily lives of European citizens as well as progressively redistributive outcomes of the 
policy choices in the EU. These dynamics created the framework for the politicization of 
Europe (see among others on this issue Zürn and de Wilde, 2012; Braun et al., 2016). At 
the same time, the discussion of the ‘democratic deficit’ of European institutions gave further 
impetus to attempts to increase their accountability. For example, the appointment of EU 
commissioners requires ratification by the EP, and this has led to increasingly political 
scrutiny of the candidates. In 2009, the Treaty of Lisbon amended the Treaty of the European 
Union, and stated that “Taking into account the elections to the European Parliament and 
after having held the appropriate consultations, the European Council, acting by a qualified 
majority, shall propose to the European Parliament a candidate for President of the 
Commission” (art. 17.7).4 Overall the ability of the voters to directly affect EU decisions is 
low,5 therefore in a cost/benefit framework the decision not to vote is more likely than in 
national elections.   
However, most political discourse takes place at the national level, our second ‘space’ 
of interest. Elections “provide the mechanism by which citizens can communicate information 
about their interests, preferences, and needs and generate pressure to respond” (Verba et 
al., 1995: 1). Voters observe the behavior of both the government and the opposition, which 
in turn is shaped by the incentives institutions and rules, provide them with. EP elections 
may be used to send messages to the government and political parties in general, especially 
when the EP elections take place during the midterm of the national election cycle. Because 
they do not directly affect who is running the country, voters may turn out and vote for the 
opposition (a typical mid-term effect) to protest against government policies. Moreover, they 
may vote for parties on the fringe of the political space in order to express their disapproval 
of both the government and the official opposition. They may alter their behavior by not 
voting at all (abstaining). In this view, EP elections are second-order national elections 
because they debate and reflect essentially national politics (Reif and Schmitt, 1980). More 
recent explanations of voting behavior at EP elections suggest that as attitudes relating to 
the European arena become more salient to voters, they may switch their party allegiance 
or abstain due to disagreement over European issues with the party they support in national 
elections (see Hix and Marsh, 2007; Hobolt et al., 2009). While the behavior of voters is 
variously motivated depending on the relative importance of dissatisfaction with government 
performance or European concerns, the political space relevant for this choice is the national 
framework.  
The quality of national institutions clearly fits this dimension. Voters may treat the 
perceived level of quality of government – the one that most affects their lives - as a 
                                           
4 The European Peoples Party was the largest group in the EP after the 2014 elections and Jean-Claude Junker, 
nominated by the party before the elections, was put forward by the Council and subsequently elected. Schmitt et 
al. (2015) claim that this personalization increased turnout.  
5 Recently Murdoch et al. (2017) have found a positive correlation between the policy preferences of EU 
administrative staff and their home country population. From this evidence, they argue that a certain degree of 
legitimacy exists for EU officials in relation to their home country. 


---

 
8 
 
benchmark when evaluating EU democracy. Furthermore, inequality also belongs to the 
national dimension, since most of the redistributive policies through taxation, subsidies and 
more in general government expenditure are taken at the national level.  
Finally, some components of electoral choice are associated with the environment 
closest to individuals. The main socio-economic and demographic variables identified in the 
literature as drivers of voter turnout (such as economic growth, population density, 
unemployment, or areas that benefit from EU subsides) are observed at the ‘local level’ 
and, as such, are often heterogeneous within a given country. For example, in 2004, in Italy 
and Spain the difference in long-term unemployment between the most and the least 
developed regions ranged between 14.2% and 59.4%, and 16.2% and 59.9%, respectively. 
The UK also has strong territorial variations between the South-East and former industrial 
cities in the North and income is almost two and a half times higher in the richest than the 
poorest regions. One of the shortcomings of the literature on voter turnout, and particularly 
of cross-country literature, is that it takes no account of this heterogeneity within a country, 
relying on average values. A comprehensive understanding of EU voting requires 
disaggregation of country patterns for these variables since any of these can generate 
differences in income distribution or cultural integration that, in turn, may affect the costs 
and benefits of going to the polls.  
The three political spaces we have identified can be traced in data at two geographical 
levels. There are variables collected at the national level (such as trust in the EU, 
employment protection or variables capturing the political framework) as well as at a lower 
level may be regional or provincial (such as data on GDP, unemployment or population 
density).  
Accounting for the intersection between the political spaces allows us to gather local 
information and to analyze how it depends on and interacts with nationwide information. 
Since local observations belong to larger national units and vary within these units (i.e., 
French regions behave similarly, as do German regions), they cannot be treated as 
independent observations, therefore a simple OLS estimator would be biased. The multilevel 
model (also known as a hierarchical linear model and nested data model) we estimate 
overcomes these problems, allowing for more accurate statistical results. 
 


---

 
9 
 
4 Empirics 
4.1 The dynamics of turnout in Europe 
Turnout at EP elections is initially analyzed to identify its spatial dynamics and the possible 
tendency to form identifiable clusters. The data on turnout are taken from the European 
Election Database and national sources and regard four elections: 1999, 2004, 2009 and 
2014 in the EU-14,6 for 164 regions.7 We consider Portugal, Spain, France, Belgium, 
Luxembourg, the Netherlands, Denmark, UK, Ireland, Germany, Italy, Greece, Austria and 
Sweden.8  
Figure 1 shows the quartiles of turnout in the years investigated. The maps display 
that turnout has a strictly national pattern for each period. Countries like Italy and Greece 
exhibit high levels of turnout over the whole period, whilst in others, such as the Netherlands 
and the United Kingdom, turnout is very low. Between these two extremes, there is a set of 
less homogeneous countries. From the least to the most homogeneous, lie Spain, France 
and Germany. Mediterranean countries have the highest turnout, although in the last two 
elections they are much closer to the EU average than before. This means that there is 
spatial persistence over time, with well-defined clusters of regions characterized by high and 
low turnout, respectively.  
 
                                           
6 Only 14 countries are included because of data availability. The methodology used requires balanced panel data. 
7 Greece is analyzed as a single region because of the lack of data for 2014. In the other cases, we refer to NUTS-
2 regions, with the exception of the United Kingdom, Spain and Germany where NUTS-1 regions are used. Although 
they differ in size and administrative importance, the regions in these two groups have usually been considered 
together (Sundstrom and Stockemer, 2015). 
8 We excluded Finland because there are only regional data for 1999 and 2004, only national data for 2009, and 
no data for 2014. Islands have been connected to the nearest region. 


---

 
10 
 
Figure 1: turnout at EU parliament elections 
a) Quartiles 1999 
 
 
c) Quartiles 2004 
 
 
 


---

 
11 
 
c) Quartiles 2009  
 
 
 
  d) Quartiles 2014 
 
 
 


---

 
12 
 
A clearer visualization of the changing pattern of turnout over time is also shown in 
Figures 2 and 3. Figure 2 represents the boxplots for each year. The box in the middle of 
each describes central tendencies i.e. the middle 50% of the distribution. The solid thick 
line inside the box locates the median; the top and bottom edges are the 75th and 25th 
percentiles, respectively. The height of the box is the inter-quartile range, IQR. The median 
turnout is relatively stable over the four elections, whereas the middle 50% of the cross-
section distribution shrinks over time along with the distance represented by the rays 
emanating from the middle box denoting the upper and lower adjacent values. The 
“whiskers” correspond to the upper adjacent value, i.e. the largest turnout observed no 
greater than the 75th percentile plus 1.5×IQR, and to the lower adjacent value, i.e. the 
lowest turnout observed no smaller than the 25th percentile minus 1.5×IQR. Finally, the 
dots outside the upper and lower adjacent values are outliers. The outliers in the last three 
periods refer to regions in the Netherlands. Despite the tendency of turnout to be spatially 
more homogeneous with time, in a few regions in Belgium, it continues to be rather high.  
 
Figure 2: Boxplot of turnout 
 
 
Figure 3 shows the within and between country variation of turnout over time for 
countries with more than 2 regions. In line with the previous analysis, the between variation 
is much larger than the within variation. In addition, with the exception of Italy, there is a 
clear decline in the variation in turnout, pointing to a more homogeneous spatial pattern 
both within and between countries. 
 


---

 
13 
 
Figure 3: Within country and between country variance 
 
 
The results of the previous analysis show that the EP election turnout is not stable over 
space and time. In addition, despite changes in the geography of electoral participation, the 
observed spatial pattern is quite strong and closely related to the country to which the 
regions belong. This suggests that a careful analysis of the determinants of EP elections 
needs to consider both context variables at the country level as well as factors with a 
regional dimension.  
 
4.2 Model specification, variables and methodology 
The model includes seven regional-level and eight national-level variables. The structure of 
the data in two different geographical levels led us to consider the multilevel model a natural 
choice (Hox, 2010:1). This is because a multilevel model allows clustering regions within 
their countries to evaluate regional-level covariate (so-called Level 1) effects within their 
national context (so-called Level 2 covariates), correcting for the non-independence of 
observations within countries (intra-class correlation) and avoiding an overestimation of the 
statistical significance of these Level 1 indicators (O'Connell and McCoach, 2008). A common 
problem with observations nested within a higher level is that there may be a problem of 
dependencies because regional turnout in the same country is likely to be similar in ways 
not fully accounted for by variables related only to the regional scale included in a single-
level model. Multilevel models also have the advantage of accommodating the spatial 
dependency of the residuals by differentiating between-individual errors from between-
neighborhood errors (Orford, 2000). If not considered this dependency leads to biased 
standard error estimates (Snijders and Bosker, 1999). We analyze a panel structure, 
exploiting the time dimension of the data. 
We assume that the turnout at EP elections is affected by several factors, and 
estimate the following regression: 
 
Turnoutit = a0 + a1EUit+ a2NATIONALit + a3REGIONALit + An + At + uit    (1) 
 
Where i denotes the country or region, depending on the specification of the variable, and 
t the election year (1999, 2004, 2009, 2014). An is the random intercept representing level 


---

 
14 
 
2 (country specific) residuals, At is the time specific random intercept residuals, and uit are 
level 1 (regional specific) residuals. The latter are assumed to be mutually independent and 
normally distributed with zero mean and variance equal to σ2.  Level 2 residuals are 
assumed to be uncorrelated with uit, mutually independent and normally distributed with 
zero mean and variance equal to η2 and τ2 for country and time specific, respectively. Fixed 
effects are expected to have a systematic and predictable influence on the data, while 
random effects can be expected to have a non-systematic, idiosyncratic, unpredictable 
influence on the data. Thus, random effects give the structure to the error term.  
The variables can be described as follows: 
1) Turnout, the dependent variable, is the number of votes in a country/region i at election 
year t as a share of the registered citizens. The data on this variable come from the 
European Election Database and from the Interior Ministries of countries investigated.  
2) EU is a vector that includes variables related with the EU itself: Trust_EU and and 
Objective1 regions. Specifically, Trust_EU measures the public attitudes towards the 
European Parliament, where 0 means no trust in an institution, and 10 means complete 
trust (source: European Social Survey).9  
Objective1 regions is a dummy variable equal to 1 if regions are below 75% of EU GDP per 
capita and thus receive the majority of EU Structural Funds, 0 otherwise.10 While in 
countries/regions that are large net contributors to the EU budget voters may think that the 
EU is financed with their tax money and this may lower their incentive to vote in EP elections, 
in countries/regions benefiting from the EU subsidies voters are more likely to go to the 
polls (Mattila, 2003).   
3) NATIONAL is a vector that includes institutional, political, economic and quality of 
government variables at the country level. The institutional variables, Compulsory voting 
and Weekday vote, have largely been explored in the literature (among others, Franklin, 
2002). The connection between compulsory voting and higher voter turnout is self-evident. 
When the rule enforces turnout, the costs of not voting increases, leading to higher turnout 
rates. Elections on weekdays increases the cost of voting since people follow their daily 
routines, decreasing electoral participation. The source of both these variables is the 
Ministry of Interior. The vector also contains variables related to features in the national 
political arena: Herfindahl_gov, Herfindahl_opp and Effective number of parties. Herfindhal 
indices measure the sum of the squared seat shares of all government (Herfindhal_gov) or 
opposition parties (Herfindhal_opp). These variables aim to capture the fractionalization of 
the government and of the opposition, respectively (source: Beck et al., 2001).  
Alternatively, we use Effective number of parties (Laakso and Taagepera, 1979), a variable 
employed in several strands of the political science literature, which weighs the number of 
parties in the legislature by the relative strength measured by their share of seats (source: 
Gallagher, 2015). All these variables attempt to analyze the fragmentation of the party 
system.11 As theoretically there is no consensus on whether political fragmentation can be 
                                           
9 Data are defined at the national level. Data at the regional level are not used due to some limitations. First, while 
they are generally available for years 2002, 2004 and 2008, for various countries the small number of interviews 
in some regions prevents inferences from being drawn because of the large margin of error. Furthermore, the 
variable trust in the European Parliament is constructed using survey weights. The use of weights is highly 
recommended 
on 
the 
ESS 
website 
to 
mitigate some of 
the problems related 
to 
survey 
data 
(http://essedunet.nsd.uib.no/cms/topics/weight/). Data are for years 2002, 2004, 2008 and 2014. Data for Greece 
regard 2002, 2004, 2008, and 2010, for Italy 2002, 2004 and 2012, for Luxembourg 2002 and 2004. In the case 
of Italy, data for 2004 are used instead of data for 2008, while for Luxembourg data for 2004 are used to proxy 
data for 2008 and 2014.   
10 
This 
dummy 
variable 
is 
based 
on 
the 
information 
available 
online 
(see 
http://ec.europa.eu/regional_policy/index.cfm/en/policy/evaluations/data-for-research/). 
 
11 These variables build on empirical literature on political fragmentation that have concentrated on both the 
government and opposition. The rationale is that for a given coalition opposition comprising one or more party 


---

 
15 
 
expected to increase or decrease political participation, we do not have an a priori 
expectation about the sign of these variables.  The vector includes the variable Inequality 
that captures income inequality through a Gini index (calculated on net income, source: 
World Income Inequality Database - WIID3.4). Quality of Government instead controls for 
the trust in national institutions. This variable is measured using the data from the 2017 
update of the QoG OECD dataset and captures the core features of QoG (impartiality, 
bureaucratic quality and corruption) as well as broader measures such as rule of law and 
transparency. 
A key problem in analyzing EP elections is their second-order nature, which fails to 
motivate voters in the elections themselves, or more broadly in relation to politics at the 
European level (Reif and Schmitt, 1980; Van der Eijk and Franklin, 1996; De Vreese et al., 
2006). The result is that voter choices are based on domestic rather than European policy 
concerns. In this perspective, EP elections are useful as vehicles for transmitting information 
from voters to leaders. The proxy traditionally used to capture this issue is the time passing 
between national first-order and EP second-order elections. Nevertheless, the political 
structure of EU countries varies greatly, therefore it is difficult to treat time as a variable 
able to capture specificities. Instead of this variable, we include a Protest vote variable 
calculated as the difference between the sum of the percentage of the two major parties in 
the general elections immediately preceding the European elections and the sum of the 
percentage of the same two parties in the European elections.12 This variable aims to 
capture the extent of protest voting differing from the results of general elections. 
Unsatisfied voters may abstain but may also send a message to more established parties 
by voting for outsiders in second-order EP elections. While our indicator is an ex post 
measure with respect to the time between national and EP elections, it is nonetheless a 
more satisfactory proxy of the different stakes characterizing the two kinds of election. This 
is because it is built on the actual choices voters made.13  
4) The REGIONAL vector includes economic as well as socio-demographic variables. 
Log(per capita GDP) is the logarithm of GDP per capita in PPS, the usual indicator of 
economic development, to account for the literature that emphasizes the role of economic 
resources in stimulating access to information and thereby the political involvement of 
citizens and voter turnout (Powell, 1982). The source of these data is the Eurostat Regional 
Database.14 To control for the labor market conditions Employment protection and 
Unemployment are used. Employment protection corresponds to the OECD indicators of 
employment protection. This variable is a synthetic indicator of ‘the strictness of regulation 
on dismissals and the use of temporary contracts’. More specifically it measures the 
procedures and the costs involved in dismissing individuals or groups of workers and the 
procedures involved in hiring workers on fixed-term or temporary work contracts. For each 
year, indicators refer to the regulations applicable on January 1 (source: OECD). We use 
this indicator to proxy the uncertainty of labor market conditions. Unemployment is the 
percentage of long-term unemployed out of total unemployment (source: Eurostat Regional 
Database). The literature provides two competing theories regarding the expected 
relationship between turnout and the economy. Some scholars argue that people under 
                                           
differs. A limited number of parties may find it easier to coordinate to oppose government policies. A large number 
of opposition parties may have diverging interests and some may negotiate with government parties (on this issue 
see Ricciuti, 2004). Herfindahl_gov is an index that divides the number of “other” seats by the number of “other” 
parties and uses this average as the size of “other” parties. Herfindahl_opp is calculated in the same way as the 
Herfindahl_gov (source: Beck et al., 2001).  
12 Source: European Electoral Database and Ministry of Interior of the considered countries. 
13 It could be claimed that before the 2014 EP elections, in some European countries, anti-establishment parties 
opposing the austerity policies of the EU and European integration made an electoral breakthrough, displacing 
some of the mainstream parties from the first two ranks. This is the case, for example, in Italy (where Movimento 
Cinque Stelle became the second largest party after the 2013 general election) and Greece (where Syriza became 
the second largest party in 2009). To check whether the variable is robust, we re-run the empirical analysis on a 
shorter 1994-2009 time span, when the political system was more stable. The results for this variable, available 
upon request, are in line with those presented here.  
14 Due to data availability, the following years: 2000, 2004, 2009 and 2013 are used. 


---

 
16 
 
economic adversity are encouraged to be more active politically (vote, protest, lobby…) and 
are more prone with their vote to punish government policies (Verba et al., 1995). The 
alternative theory says the opposite and assumes that voters respond to adverse economic 
conditions by withdrawing from the political process (Rosenstone, 1982). The vector also 
includes Log(Density) i.e. the log of the number of inhabitants per square km. We have no 
prior expectation regarding the sign of the coefficient associated with this variable given 
conflicting theoretical predictions. On the one hand, attitudes that stimulate voter turnout 
develop more easily in relatively concentrated political environments where community 
relations are closer and more direct, thus a negative sign is expected (Oliver, 2000, among 
others). In contrast, another theory suggests a positive sign could be expected since in 
areas with higher population densities voters are more concentrated and easier to mobilize 
(Lipset, 1981). The source for this variable is Eurostat Regional Database for population and 
Cambridge Econometrics for regional areas. Finally, the Dependency ratio, that is the ratio 
of people over 65 to the young between 20 and 24, captures the influence of the age 
structure of the population on voter turnout (source: Eurostat Regio Database). The 
expected sign for this variable is positive.  
 
Although Bendor et al. (2003) and Fowel (2006) found that the current turnout 
choice is related to the turnout choice in the previous election, we do not include an 
autoregressive term of turnout on the right-hand side of the equation (2) because first-
differences in the GMM and the autoregressive term would have halved the number of 
elections and observations. Moreover, they would have prevented the use of time-invariant 
variables (compulsory voting, and dummy for objective1 regions). Finally, finding viable 
internal instruments was difficult. However, the fixed effect introduced in the robustness 
checks, may mitigate this problem by taking into account the idiosyncratic persistence for 
each country. 
 
Table 1 summarizes the statistics and territorial level of the variables, and Table A1 
in the Appendix provides a correlation matrix. 
 


---

 
17 
 
Table 1: Descriptive statistics 
Variable 
Mean 
Std. dev 
Min. 
Max. 
Territorial level 
Compulsory voting 
0.0793 
0.2704 
0.0000 
1.000 
national 
Dependency ratio 
0.9342 
0.2527 
0.3952 
20.510 
regional 
Effective number of parties 
3.791 
1.4892 
2.130 
8.420 
national 
Employment protection 
25.160 
0.6092 
10.320 
45.830 
national 
Herfindhal_gov 
0.6900 
0.2328 
0.1810 
1.000 
national 
Herfindhal_opp 
0.5043 
0.1659 
0.2199 
0.855 
national 
Inequality 
29.52 
3.1573 
21.00 
37.800 
national 
Log(Density) 
51.550 
11.718 
11.940 
88.990 
regional 
Log(per capita GDP) 
10.080 
0.2693 
93.670 
11.130 
regional 
Objective1 regions 
0.2485 
0.4324 
0.0000 
1.000 
regional 
Quality of Government 
0.8201 
0.1174 
0.5440 
1.000 
national 
Protest vote 
0.1292 
0.1210 
-0.1726 
0.397 
national 
Trust EU 
4.424 
0.5118 
2.568 
5.752 
national 
Turnout 
0.4971 
0.1625 
0.1960 
0.944 
regional 
Unemployment 
0.3937 
0.1332 
0.0410 
0.754 
regional 
Weekday vote 
0.1631 
0.3697 
0.0000 
1.000 
national 


---

 
18 
 
5 
 
Results  
5.1 Baseline results 
Table 2 sets out our results. Some variables are highly significant, whatever the chosen 
model. Looking at model 1, compulsory voting increases the costs of not voting, leading to 
higher turnout rates although no penalties are imposed for failure to comply, while elections 
held during the week have no effect on voter participation. Adding socio-economic and 
demographic variables (model 2) shows that neither per capita GDP nor population density 
impact on voter turnout. In addition, as in the literature championed by Radcliff (1994), 
Unemployment has a significantly negative effect on voter participation while Employment 
protection positively affects turnout. The Dependency ratio is also significant, confirming 
that the age structure of the population helps to explain variations in the electoral behavior 
of voters. The oldest segment of the population is more likely to vote than the youngest. 
Model 3 and 3a include the variables capturing the influence of domestic politics. While a 
more concentrated government decreases electoral participation, the concentration of the 
opposition has a positive effect on voter turnout, albeit at a low significance level. The 
Effective number of parties is used in model 3a as an alternative to Herfindhal_gov and 
Herfindhal_opp. The results of this variable indicate that it is significantly and positively 
related to the dependent variable. Therefore, the higher the number of parties the higher 
the voter turnout. The positive association between the effective number of parties and 
turnout could also be interpreted as an implicit sign that proportional representation fosters 
turnout because it produces more parties, thus providing voters with more choice and more 
mobilization. The findings on Herfindhal_gov that turnout rises with higher fragmentation 
of government reinforce this interpretation since government coalitions are the result of 
proportional representation. Inequality is positive and significant, therefore increasing 
inequality seems to mobilize voters. The variable capturing the quality of the national 
government negatively affects turnout, claiming that when voters are satisfied with 
domestic institutions they are less interested in participating to a higher layer of 
governance. 
 
The Protest vote is highly significant and positive. Voters may decide to “punish” the 
most popular parties in the previous elections in the subsequent EU parliament elections: 
the higher the gap the higher the turnout.15  
 
Model 4 and 4a add the vector EU. While the majority of variables previously considered 
retain their sign and significance, unemployment and employment protection turn out not 
to be significant. Trust in the EU has a significant impact on turnout in both models, while 
support from cohesion policy has a marginal negative effect on turnout. The first effect can 
be interpreted as interest from the electorate towards the EU. This result is rather unusual 
in the literature.16 Concerning the second variable, it is likely that the positive effect of these 
EU programs on voting is counteracted by the very characteristics of these areas that are 
economically marginal, poorer than average by definition, affected by high unemployment, 
and often scarcely populated, factors that tend to lower voter participation. The loss of 
significance of the variables capturing labor market conditions seems to confirm this 
interpretation. 
                                           
15 Usually in Europe the two largest parties are the party in government and its main opposition and they alternate 
in power. If a voter wants to punish them, he has to vote for a smaller party. In some countries, “grand coalitions” 
in which the two main parties rule together (often in Austria, more recently in Germany), so the protest vote 
consists in choosing a non-coalition party (and not abstaining). 
16 See Hobolt (2012) and the references therein.  


---

 
19 
 
Table 2: Estimation results, multilevel model, fixed effects 
Groups 
Model  1 
Model  2 
Model  3 
Model  3(a) 
Model  4 
Model  4(a) 
Model  5 
Model  5(a) 
Intercept 
0.4724*** 
(0.0347) 
0.2336  
(0.1875) 
0.3309*  
(0.1900) 
0.1363 
(0.1836) 
-0.0160 
(0.1837) 
-0.0529 
(0.1855) 
-0.0206 
(0.2121) 
0.0375 
(0.2029) 
Weekday vote 
-0.0409  
(0.0514) 
-0.0025  
(0.0580) 
-0.0018  
(0.0549) 
0.0068 
(0.0556) 
-0.0336 
(0.0399) 
-0.0097 
(0.0474) 
-0.0493 
(0.0328) 
-0.0144 
(0.0409) 
Compulsory voting 
0.3352***  
(0.0669) 
0.3712***  
(0.0797) 
0.3738*** 
(0.0730) 
0.3372*** 
(0.0756) 
0.2908*** 
 (0.0472) 
0.3032*** 
(0.0588) 
0.2618*** 
(0.0382) 
0.2553*** 
(0.0488) 
Log(GDP per capita) 
 
0.0069  
(0.0170) 
0.0039  
(0.0168) 
0.0021 
(0.0165) 
0.0101  
(0.0161) 
0.0069 
(0.0163) 
0.0125 
(0.0159) 
0.0110 
(0.0160) 
Unemployment 
 
-0.0733** 
 (0.0356) 
-0.0976***  
(0.0353) 
-0.0673* 
(0.0348) 
-0.0348 
(0.0346) 
-0.0312 
(0.0353) 
-0.0320 
(0.0342) 
-0.0310 
(0.0345) 
Employment protection 
 
0.0591** 
 (0.0237) 
0.0438*  
(0.0229) 
0.0662*** 
(0.0230) 
-0.0193 
(0.0194) 
0.0242 
(0.0219) 
-0.0497** 
(0.0174) 
-0.0253 
(0.0209) 
Log(Density) 
 
-0.0034  
(0.0039) 
-0.0029 
 (0.0038) 
-0.0025 
(0.0038) 
-0.0024 
 (0.0037) 
-0.0021 
(0.0037) 
-0.0029 
(0.0036) 
-0.0027 
(0.0036) 
Dependency ratio 
 
0.0596***  
(0.0164) 
0.0563*** 
 (0.0164) 
0.0661*** 
(0.0160) 
0.0765***  
(0.0160) 
0.0804*** 
(0.0161) 
0.0723*** 
(0.0159) 
0.0761*** 
(0.0158) 
Herfindhal_gov 
 
 
-0.0981***  
(0.0297) 
 
-0.1720***  
(0.0288) 
 
-0.1598*** 
(0.0274) 
 
Herfindhal_opp 
 
 
0.0688*  
(0.0335) 
 
0.0991**  
(0.0321) 
 
0.0626* 
(0.0357) 
 
Effective number of parties 
 
 
 
0.0310*** 
(0.0056) 
 
0.0236*** 
(0.0057) 
 
0.0273*** 
(0.0056) 
Protest vote 
 
 
0.1216*** 
 (0.0270) 
0.0032 
(0.0287) 
0.1460***  
(0.0260) 
0.0207 
(0.0285) 
0.1427*** 
(0.0266) 
0.0278 
(0.0281) 
Trust_EU 
 
 
 
 
0.1010***  
(0.0124) 
0.0568*** 
(0.0127) 
0.1210*** 
(0.0125) 
0.0901*** 
(0.0132) 
Objective1 regions 
 
 
 
 
-0.0133*  
(0.0069) 
-0.0117* 
(0.0069) 
-0.0144** 
(0.0068) 
-0.0145** 
(0.0068) 
Inequality 
 
 
 
 
 
 
0.0051** 
(0.0022) 
0.0052** 
(0.0024) 
Quality of Government 
 
 
 
 
 
 
-0.1934** 
(0.0873) 
-0.3715*** 
(0.0847) 
 
 
 
 
 
 
 
 
 
AIC 
-1478.97 
-1502.3 
-1521.97 
-1538.407 
-1578.027 
-1555.345 
-1589.125 
-1585.033 
*Significant at 1%, ** significant at 5%, *** significant at 10%. Standard errors in brackets. 


---

 
 
 
In order to check whether the multilevel model is the appropriate choice, Table 3 
gives a likelihood ratio test of the multilevel model with country and with time-random effect 
versus a model without random effects. The significance levels of the p-value for such a 
test, which is based on a chi-squared distribution, shows that the linear mixed model is 
always the best choice. 
 
Table 3: Standard errors estimates, multilevel model, random effects 
Groups 
Model 1 
Model 2 
Model 3 
Mod. 3(a) 
Model 4 
Mod. 
4(a) 
Model 5 
Mod. 5(a) 
Count. 
0.0954**
* 
0.1143**
* 
0.1035**
* 
0.1076**
* 
0.0606**
* 
0.080**
* 
0.002**
* 
0.0039**
* 
Year 
0.0161**
* 
0.0259**
* 
0.0309**
* 
0.0232**
* 
0.0008**
* 
0.021**
* 
0.001**
* 
0.0007**
* 
Resid. 
0.0742 
0.0718 
0.0705 
0.0697 
0.0680 
0.0690 
0.0045 
0.0045 
  
0.5137 
0.5391 
0.5051 
0.5367 
0.4683 
0.4700 
0.2703 
0.4286 
  
0.0867 
0.1222 
0.1508 
0.1157 
0.0062 
0.1246 
0.1667 
0.1246 
P-values of likelihood ratio tests: *Significant at 1%, ** significant at 5%, *** significant at 10%. 
 
In addition, the total variance can be split by our nested effect variance to give the 
proportion of variance accounted for, showing whether each random effect is meaningful. 
When all the percentages for each random effect are very small, there are no random effects 
and linear mixed modelling is not appropriate. 
The variance of turnout conditional on the explanatory variables is equal to η2 + τ2 
+ σ2. Therefore, the overall conditional variability of turnout can be decomposed into two 
components  
 and 
, known as the 
intra-class correlation coefficients. These components represent the proportion of variability 
due to country and time clustering respectively, and measure the correlation shared by units 
within the same country or in the same year.  
 
Figure 4: Random effect estimates 
 


---

 
 
 
The intra-class correlation coefficients for country-random effects are quite 
substantial, ranging from 47% to 54%. The total variability explained by yearly random 
effects is only around 1-15%, so the nested effects related to the time variable are not 
meaningful.  
The intercepts for the country-random term, whose estimates are based on model 
4, are reported in Figure 4. The intercept term varies between -0.102 and 0.125 and the 
standard deviation is equal to 0.059. The positive values refer to Italy, the Netherlands, 
Luxembourg, Ireland and Spain, in line with the persistent high turnout over time analyzed 
in section 3.1. The countries with the lowest turnout rates plus Greece present a negative 
intercept. The reason is the strong variation in EP election participation: from 71.5% in 1999 
to 52.6% in 2009 and 60% in 2014.  
 
5.2 Robustness checks   
The multilevel approach can be particularly problematic in a comparative analysis with few 
countries (Maas and Hox, 2005). One possible alternative is to control for heterogeneity by 
means of dummy variables, avoiding the omitted variable bias (Allison, 2009: 14).  
Following Hox (2010: 13), the country-specific error term in multilevel models is 
assumed to be normally distributed and independent of both the other variables in the model 
and the individual level error term. In fixed-effect regression (Table 4), since the country 
specific error term is a set of fixed numbers estimated in the model, it does not matter 
whether or not the residuals are independent of the other variables in the model (Allison 
2009: 21). The results of OLS regression with country and time dummy variables are 
presented in Table 3 and support our previous findings. The AIC statistic is typically lower 
in the multilevel estimation than in the OLS model, showing that the former outperforms 
the latter. 
As a further robustness check, we consider only regional random effects and time 
dummies. The results are once again in line with our main findings. Finally, we estimate our 
model excluding countries comprising one region only (that is Greece, Denmark and 
Luxemburg), all together and one by one. We find no differences in terms of sign and 
significance compared to the models presented in Table 2. These results are not given here 
but are available upon request. 
 


---

 
 
Table 4: Estimation results, OLS with country dummies 
 
Model  1 
Model  2 
Model  3 
Model  3(a) 
Model  4 
Model  4(a) 
Model  5 
Model  5(a) 
Intercept 
0.4614***  
(0.0133) 
0.1500 
 (0.1851) 
0.2545  
(0.1878) 
0.0370 
(0.1832) 
0.0076  
(0.1856) 
-0.0811 
(0.1861) 
0.0258 
(0.2241) 
0.1342 
(0.2086) 
Weekday vote 
-0.0504  
(0.0859) 
-0.0401 
 (0.0835) 
-0.0285  
(0.0824) 
-0.0173 
(0.0814) 
0.0191  
(0.0800) 
0.0007 
(0.0809) 
0.0323 
(0.0799) 
0.0263 
(0.0794) 
Compulsory voting 
0.4498*** 
(0.0391) 
0.4793***  
(0.0404) 
0.4873***  
(0.0399) 
0.4815*** 
(0.0393) 
0.3616*** 
 (0.0433) 
0.4235*** 
(0.0434) 
0.3274*** 
(0.0444) 
0.3580*** 
(0.0444) 
Log(GDP per capita) 
 
0.0071 
 (0.0173) 
0.0035  
(0.0171) 
0.0025 
(0.0168) 
0.0067 
 (0.0166) 
0.0034 
(0.0168) 
0.0068 
(0.0165) 
0.0046 
(0.0164) 
Unemployment 
 
-0.0713* 
(0.0362) 
-0.0965***  
(0.0360) 
-0.0652* 
(0.0355) 
-0.0476 
 (0.0357) 
-0.0411 
(0.0361) 
-0.0381 
(0.0356) 
-0.0321 
(0.0355) 
Employment protection 
 
0.0934***  
(0.0271) 
0.0756***  
(0.0270) 
0.1028*** 
(0.0266) 
0.0127 
(0.0279) 
0.0753*** 
(0.0281) 
-0.0237 
(0.0299) 
0.0089 
(0.0306) 
Log(Density) 
 
-0.0030  
(0.0039) 
-0.0025  
(0.0038) 
-0.0020 
(0.0038) 
-0.0019 
(0.0037) 
-0.0013 
(0.0038) 
-0.0023 
(0.0037) 
-0.0018 
(0.0037) 
Dependency ratio 
 
0.0642***  
(0.0167) 
0.0611***  
(0.0167) 
0.0718 
(0.0163) 
0.0775***  
(0.0163) 
0.0832*** 
(0.0164) 
0.0738*** 
(0.0162) 
0.0774*** 
(0.0161) 
Herfindhal_gov 
 
 
-0.0923***  
(0.0310) 
 
-0.1715*** 
 (0.0322) 
 
-0.1280*** 
(0.0348) 
 
Herfindhal_opp 
 
 
0.0665*  
(0.0342) 
 
0.0859***  
(0.0332) 
 
0.0665* 
(0.0370) 
 
Effective number of parties 
 
 
 
0.0311*** 
(0.0059) 
 
0.0256*** 
(0.0061) 
 
0.0264*** 
(0.0062) 
Protest vote 
 
 
0.1185***  
(0.0274) 
0.0012 
(0.0294) 
0.1432*** 
(0.0267) 
0.0138 
(0.0296) 
0.1304*** 
(0.0281) 
0.0304 
(0.0293) 
Trust_EU 
 
 
 
 
0.0915***  
(0.0139) 
0.0440*** 
(0.0137) 
0.1084*** 
(0.0155) 
0.0862** 
(0.0155) 
Objective1 regions 
 
 
 
 
-0.0140**  
(0.0069) 
-0.0131* 
(0.0070) 
-0.0157** 
(0.0069) 
-0.0163** 
(0.0069) 
Inequality 
 
 
 
 
 
 
0.0063** 
(0.0028) 
0.0059** 
(0.0027) 
Quality of Government 
 
 
 
 
 
 
-0.1853* 
(0.1075) 
-0.4092*** 
(0.0964) 
R2 (adj.) 
0.8100 
(0.8034) 
0.8178  
(0.8109) 
0.8169  
(0.8097) 
0.821 
(0.8141) 
0.8297 
(0.8224) 
0.8248 
(0.8176) 
0.8325 
(0.8247) 
0.8328 
(0.8254) 
AIC 
-1564.968 
-1588.479 
-1583.328 
-1599.96 
-1626.73 
-1610.308 
-1633.568 
-1636.939 
Country dummies  
yes 
yes 
yes 
yes 
yes 
yes 
yes 
yes 
Time dummies 
yes 
yes 
yes 
yes 
yes 
yes 
yes 
yes 
*Significant at 1%, ** significant at 5%, *** significant at 10%. Standard errors in brackets. An F-test on joint significance of dummy variables 
confirmed that the p-value is always < 0.01. 


---

6 Concluding remarks 
This paper puts forward a unified framework to interpret voter participation in EP elections as a 
more suitable way to investigate the multilevel EP decision-making process. We claim that three 
different political spaces affect the decision to go to the polling station: supranational (directly 
relevant to the way the EU is perceived), national (related to the political arena in which voters 
live) and regional (socioeconomic outcomes that voters may observe closely) and that these 
political spaces have a geographical 'dimension'. Hence, we study the features of voter turnout 
in the last four EP elections in the EU-14, in 164 regions.  
Given the nature of the data, the multilevel model is the appropriate modelling choice for 
a parametric estimation. The model shows that regional-level turnout is strongly driven by some 
national-level covariates as well as by regional-level variables. Overall, as the literature 
suggests, our results indicate that the elderly are more prone to turn out in EP elections than 
youngsters. Where the law enforces turnout, voter participation increases even when no 
penalties are associated with abstention. EU financial transfers negatively affect participation in 
EP elections, suggesting that the negative effect of poverty and unemployment in areas 
benefiting from EU transfers overcomes the positive effects of these transfers. No evidence is 
found that GDP per capita influences turnout, while labor market conditions (unemployment and 
workers protection) do. Most importantly, our results confirm that the national political scenario 
affects European elections. It seems that coalition governments, generally the result of PR 
systems, increase turnout. This evidence indirectly shows that proportional representation could 
foster turnout because it produces more parties, giving voters more choice and leading to greater 
mobilization. Individuals who want to vote for small parties have more reason to turn out under 
PR. Moreover, everything else being equal, participation in EP elections is driven by protest 
against the establishment. Finally, the significance of the variables that account for trust in 
European institutions suggests that public opinion matters in affecting turnout in EP elections.  
These ﬁndings have implications for the debate on the democratic deﬁcit and legitimacy 
of the EU. They suggest that national governments and politicians are possibly the only visible 
actors involved in policy-making since national quality of government as well as national 
economic and political performance affect voters turnout in EP elections. Nevertheless, citizens 
do care about EU institutions and policies. The ongoing challenge for the EU is thus not only to 
guarantee economic prosperity, rather to increase the salience of the EP elections building 
conﬁdence in the EU democratic institutions. The Spitzenkandidaten is probably only the first 
step in this direction.  


---

 
 
References 
Allison, P.D., 2009. Fixed Effects Regression Models, Thousand Oaks, CA: Sage 
Publications. 
Anderson, C.J., 1998. When in doubt, use proxies: attitudes toward domestic politics and 
support for integration. Comparative Political Studies, 31, 569–601. 
Anderson, C., Beramendi, P., 2008. Income, inequality, and electoral participation, in: 
Beramendi, P., Anderson, C. (eds.), Democracy, Inequality and Representation: a 
Comparative Perspective. Oxford University Press, New York. 
Bartkowska, M. Tiemann, G. 2014. The impact of economic perceptions on voting 
behaviour in European parliamentary elections. Journal of Common Market Studies, 
1-17.  
Beck, T., Clarke, G., Groff, A., Keefer, P. and Walsh, P., 2001. New tools in comparative 
political economy: The Database of Political Institutions. World Bank Economic Review 
15, 1, 165-176. 
Bendor, J., Diermeier, D., Ting. M., 2003. A behavioral model of turnout. American Political 
Science Review, 97, 2: 261–80. 
Blais, A., 2000. To Vote or Not To Vote? The Merits and Limits of Rational Choice, 
Pittsburgh, University of Pittsburgh Press. 
Blais, A., Carty, R.K., 1990. Does proportional representation foster voter turnout? 
European Journal of Political Research, 18, 167-181. 
Blais, A., Dobrzynska, A., 1998. Turnout in electoral democracies. European Journal of 
Political Research 33, 239-261. 
Blank, R.H., 1974. Socio-economic determinism of voting turnout: A challenge. Journal of 
Politics, 36, 731-752. 
Brady, H.E., 2004. An Analytical Perspective on Participatory Inequality and Income 
Inequality. In Neckerman. K.M. (ed.). Social inequality. Russel Sage Foundation. New 
York, 667-702. 
Braun, D., Hutter, S., Kerscher, A., 2016. What type of Europe? The salience of polity and 
policy issues in European Parliament elections. European Union Politics, 17, 570–592 
Cho, W.K.T., Rudolph, T.J., 2008. Emanating political participation: Untangling the spatial 
structure behind participation. British Journal of Political Science, 38, 273–89. 
Dahl, R.A., 2006. On Political Equality. Yale University Press, New Haven, CT 
De Vreese, C., Banducci, S.A., Semetko, H.A., Boomgaarden, H.G., 2006. The news 
coverage of the 2004 European Parliamentary election campaign in 25 countries. 
European Union Politics, 7, 477–504. 
van der Brug, W., van der Eijk C., Franklin M., 2007. The Economy and the Vote: Economic 
Conditions and Elections in Fifteen Countries. Cambridge University Press. 
van der Eijk, C., Franklin, M., 1996. Choosing Europe? The European Electorate and 
National Politics in the Face of Union, Ann Arbor, University of Michigan Press. 
Escaleras, M., Calcagno, P., Shugart II, W., 2012. Corruption and voter participation 
evidence from the U.S. States. Public Finance Review, 40, 789-815.  
Fowel, J.H., 2006. Habitual voting and behavioral turnout. Journal of Politics, 68, 2: pp. 
335–344. 
Franklin, M., 2002. Electoral Participation, in Leduc, L. et al. (eds.), Comparing 
Democracies: New Challenges in the Study of Elections and Voting, Sage, London, 
148-168.  


---

 
 
Gallagher, M., 2015. Electoral system website, on line appendix of Gallagher, M. and 
Mitchell, P., 2008. The Politics of Electoral Systems, Oxford University Press. 
http://www.tcd.ie/Political_Science/staff/michael_gallagher/ElSystems/ 
Gerber, A.S., Green, D. P., Larimer, C. W., 2008. Social pressure and voter turnout: 
Evidence from a largescale field experiment. American Political Science Review 102, 
33–48. 
Geys, B., 2006. Explaining voter turnout: A review of aggregate-level research, Electoral 
Studies, 25, 637-663. 
Goodin R., Dryzek, J., 1980. Rational participation: The politics of relative power. British 
Journal of Political Science, 10, 3, 273-292. 
Hix, S., Marsh, M., 2011. Second-order effects plus pan-european political swings: An 
analysis of European Parliament elections across time. Electoral Studies, 30, 4-15. 
Hix, S., Marsh, M., 2007. Punishment or protest? Understanding European Parliament 
elections. The Journal of Politics, 69, 2: 495-510. 
Hobolt, S.B., 2012. Citizen satisfaction with democracy in the European Union. Journal of 
Common Market Studies, 50: 88–105. 
Hobolt, S.B., Spoon, J., Tilley, J., 2009. A vote against Europe? Explaining defection at the 
1999 and 2004 European Parliament elections. British Journal of Political Science, 39, 
1: 93-115. 
Hox, J.J., 2010. Multilevel Analysis. Techniques and Applications. 2nd ed. New York, NY: 
Routledge. 
Jackman, R.W., 1987. Political institutions and voter turnout in the industrial democracies. 
American Political Science Review, 81, 2, 405-423. 
Karahan G. R., Coats, M., Shugart, W.F.II, 2006. Corrupt political jurisdictions and voter 
participation. Public Choice 126, 87-196. 
Kostadinova, T., 2009. Abstain or rebel: Corruption perceptions and voting in East 
European elections. Politics and Policy, 37, 691-714.   
Kramer, G. H. 1983. The ecological fallacy revisited: Aggregate-level versus individual- 
level findings on economics and elections, and sociotropic voting. American Political 
Science Review 77, 1, 92–111. 
Laakso, M. Taagepera, R., 1979, “Effective” number of parties: A measure with application 
to West Europe, Comparative Political Studies, 12, 3-27. 
Lacombe, D.J., Holloway G. J., Shaughnessy T.M., 2014. Bayesian estimation of the spatial 
Durbin error model with an application to voter turnout in the 2004 Presidential 
Election. International Regional Science Review, 37, 3, 298-327 
Lipset, S.M., 1981. Political Man: The Social Bases of Politics. Baltimore, The Johns Hopkins 
University Press. 
Maas, C.J.M., Hox, J.J., 2005. Sufficient sample sizes for multilevel modeling, Methodology, 
1, 86-92. 
Marsh, M., 1998. Testing the second-order election model after four European elections. 
British Journal of Political Science, 28, 4, 591-607. 
Mattila, M., 2003. Why bother? Determinants of turnout in the European elections. Electoral 
Studies, 22, 449–468. 
Meltzer, A.H., Richard, S.F., 1981.  A rational theory of the size of government. Journal of 
Political Economy, 89, 5, 914-27. 


---

 
 
Murdoch Z., Connolly S.J., Kassim H., 2017. Administrative legitimacy and the democratic 
deficit of the European Union. Journal of European Public Policy, forthcoming. 
O'Connell, A.A., McCoach, D.B., 2008. Multilevel Modelling of Educational Data. Charlotte. 
NC. Informational Age Publishing. 
Oliver, J.E., 2001. Democracy in Suburbia. Princeton University Press, Princeton, NJ. 
Oliver, J.E., 2000. City size and civic involvement in metropolitan America. American 
Political Science Review, 94, 361–373. 
Orford, S., 2000. Modelling spatial structures in local housing market dynamics: A 
multilevel perspective, Urban Studies, 37(9), 1643-1671. 
Overbye, E., 1995. Making a case for the rational, self-regarding ‘ethical’ voter and solving 
the ‘paradox of not voting’ in the process, European Journal of Political Research, 27, 
269-296. 
Powell, G.B., 1982. Contemporary Democracies: Participation, Stability, and Violence, 
Harvard University Press, Cambridge. 
Radcliff, B., 1994. Reward without punishment: Economic conditions and the vote. Political 
Research Quarterly, 47, 21–31. 
Reif, K., Schmitt, H., 1980. Nine second-order national elections. A conceptual framework 
for the analysis of European eection results. European Journal of Political Research, 
8, 3-44. 
Ricciuti, R., 2004. Political fragmentation and fiscal outcomes. Public Choice, 118, 365–
388. 
Rohrschneider, R. 2002. The democratic deficit mass support for an EU-wide government. 
American Journal of Political Science, 46, 2, 463–475. 
Rosenstone, S., 1982. Economic adversity and voter turnout. American Journal of Political 
Science, 26, 1, 25-46. 
Sanchez-Cuenca, I. 2000. The political basis of support for European integration. European 
Union Politics, 1, 2, 147–171. 
Schmitt, H., Hobolt, S. and Popa, S.A., 2015. Does personalization increase turnout? 
Spitzenkandidaten in the 2014 European Parliament elections. European Union 
Politics, 16, 347–368. 
Selb, P. 2009. A deeper look at the proportionality-turnout nexus. Comparative Political 
Studies, 42, 4, 527-548. 
Smets, K., van Ham, C. 2013. The embarrassment of riches? A meta-analysis of individual-
level research on voter turnout. Electoral Studies, 32(2):344–359.  
Snijders, T. A.B., Bosker, R.J., 1999. Multilevel Analysis, Sage, London. 
Solt, F., 2008. Economic inequality and democratic political engagement. American Journal 
of Political Science 52 (1), 48–60. 
Stockemer, D., Calca, P., 2013. Corruption and turnout in Portugal: A municipal level study. 
Crime, Law and Social Change, 60, 5, 535-548. 
Stockemer, D., La Montagne, B., Scruggs L., 2013. Bribes and ballots: The impact of 
corruption on voter turnout in democracies. International Political Science Review, 
34, 70-92. 
Sundstrom, A., Stockemer, D., 2015. Regional variation in voter turnout in Europe: The 
impact of corruption perceptions. Electoral Studies, 40, 158-169. 
Verba, S., Schlozman, K.L., Brady, H.E., 1995. Voice and Equality: Civic Voluntarism in 
American Politics. Cambridge, MA: Harvard University Press. 


---

De Wilde, P., Zürn, M., 2012. Can the politicization of European integration be reversed? 
Journal of Common Market Studies, 50, 137–153. 


---

 
28 
Appendix 
Table A 1: Correlation matrix 
 
Turnout Weekday 
vote 
Comp. 
voting 
Log(GDP 
per 
capita) 
Unempl. 
Empl. 
protect. Log(Density) Dep. 
ratio 
Herfindhal 
gov 
Herfindhal 
opp 
Effective 
number of 
parties 
Protest 
vote 
Trust 
EU 
Ob. 1 
regions Inequality 
Quality 
of 
Gov. 
Turnout 
1.0000 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Weekday  
vote 
-0.3398 
1.0000 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Compulsory 
voting 
0.6938 
-0.1295 
1.0000 
 
 
 
 
 
 
 
 
 
 
 
 
 
Log(GDP per 
capita) 
0.0181 
0.1119 
0.0973 
1.0000 
 
 
 
 
 
 
 
 
 
 
 
 
Unempl. 
0.2350 
-0.2557 
0.1534 
-0.3279 1.0000 
 
 
 
 
 
 
 
 
 
 
 
Employment 
protection 
-0.1454 -0.4012 
-0.2981 -0.0985 0.1815 
1.0000 
 
 
 
 
 
 
 
 
 
 
Log(Density) 0.0111 
0.2067 
0.1576 
0.3648 
0.2314 -0.0724 
1.0000 
 
 
 
 
 
 
 
 
 
Dependency  
ratio 
0.0710 
-0.2326 
-0.0896 
0.0323 
0.1121 
0.1497 
-0.3065 
1.0000 
 
 
 
 
 
 
 
 
Herfindhal 
gov 
-0.2895 -0.0099 
-0.5073 -0.3106 0.0153 -0.0039 
-0.1349 
-0.1190 1.0000 
 
 
 
 
 
 
 
Herfindhal 
opp 
0.0254 
-0.1615 
-0.3344 -0.2593 0.0775 
0.0424 
-0.1756 
0.0450 
0.6336 
1.0000 
 
 
 
 
 
 
Effective n.  
of parties  
0.6506 
-0.0939 
0.6717 
0.1289 
0.1718 -0.1675 
0.0985 
0.0765 -0.5638 
-0.3785 
1.0000 
 
 
 
 
 
Protest vote 0.6316 
-0.0106 
0.6628 
0.1883 
0.0969 -0.0548 
0.1541 
-0.0041 -0.6639 
-0.4695 
0.8843 
1.0000 
 
 
 
 
Trust_EU 
-0.0411 -0.0296 
-0.1965 -0.0181 0.0208 -0.0957 
-0.0555 
0.1598 
0.3345 
0.1119 
0.0197 
-0.0353 1.0000 
 
 
 
Objective1 
regions 
0.5461 
-0.2030 
0.2962 
-0.0844 0.0697 
0.1884 
-0.0141 
-0.2044 -0.0722 
0.0160 
0.3700 
0.4611 -0.1357 1.0000 
 
 
Inequality 
-0.003 
-0.006 
-0.193 
-0.247 
0.172 
0.082 
0.093 
0.060 
0.568 
0.602 
-0.343 
-0.428 
0.033 
-0.130 
1.0000 
 
Quality of 
Government -0.114 
0.356 
0.042 
0.210 
-0.169 
-0.148 
0.157 
-0.178 
-0.441 
-0.758 
-0.027 
0.164 
-0.034 
-0.231 
-0.631 
1.000 


---

List of tables 
Table 1: Descriptive statistics .................................................................................17 
Table 2: Estimation results, multilevel model, fixed effects ........................................19 
Table 3: Standard errors estimates, multilevel model, random effects .........................20 
Table 4: Estimation results, OLS with country dummies.............................................22 


---

 
 
List of figures 
Figure 1: turnout at EU parliament elections ............................................................10 
Figure 2: Boxplot of turnout ...................................................................................12 
Figure 3: Within country and between country variance.............................................13 
Figure 4: Random effect estimates .........................................................................20 


---

GETTING IN TOUCH WITH THE EU 
In person 
All over the European Union there are hundreds of Europe Direct information centres. You can find the 
address of the centre nearest you at: http://europea.eu/contact 
On the phone or by email 
Europe Direct is a service that answers your questions about the European Union. You can contact this 
service: 
- by freephone: 00 800 6 7 8 9 10 11 (certain operators may charge for these calls), 
- at the following standard number: +32 22999696, or 
- by electronic mail via: http://europa.eu/contact 
FINDING INFORMATION ABOUT THE EU 
Online 
Information about the European Union in all the official languages of the EU is available on the Europa 
website at: http://europa.eu 
EU publications 
You can download or order free and priced EU publications from EU Bookshop at: 
http://bookshop.europa.eu. Multiple copies of free publications may be obtained by contacting Europe 
Direct or your local information centre (see http://europa.eu/contact). 


---

 
doi:10.2760/847841 
ISBN 978-92-79-75757-0  
