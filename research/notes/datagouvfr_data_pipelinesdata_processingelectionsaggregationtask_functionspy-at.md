---
title: datagouvfr_data_pipelines/data_processing/elections/aggregation/task_functions.py
  at main · datagouv/datagouvfr_data_pipelines · GitHub
id: datagouvfr_data_pipelinesdata_processingelectionsaggregationtask_functionspy-at
tags:
- projections-electorales-bureaux-2027-b0b1c4
- locus-crosswalk-bureaux-fiabilite
- code-source
- id-brut-miom
created: '2026-07-21T19:45:09.046380Z'
updated: '2026-07-21T19:45:43.811096Z'
source: https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/task_functions.py
source_domain: github.com
fetched_at: '2026-07-21T19:45:09.009472Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: 'Code source (204 lignes, task_functions.py, dernier commit 2 juillet 2026)
  du DAG Airflow ''process_election_data'' qui construit le dataset agrégé data.gouv.fr.
  Point méthodologique crucial : ce script ne fait AUCUNE jointure REU / table-bv-reu
  lui-même — il se contente de CONCATÉNER des fichiers déjà standardisés (''general-results.csv'',
  ''candidats-results.csv'') récupérés depuis les ''community_resources'' d''une organisation
  data.gouv.fr (organization=646b7187b50b2a93b1ae3d45), triés par date de création.
  Le commentaire du code le dit explicitement : ''getting preprocessed resources,
  the magic is there (when creating standardized files), here we only concatenate
  them''. Autrement dit, la logique de rapprochement bureau-de-vote/REU (la ''magie'')
  est produite EN AMONT, par un processus décentralisé de dépôt de ressources communautaires
  par scrutin, et non par un pipeline central versionné et audité dans ce repo — ce
  qui est cohérent avec les bugs de correspondance ad hoc (Montbéliard, DOM-TOM) documentés
  dans les discussions du jeu de données, corrigés au fil de l''eau plutôt que prévenus
  par une norme de codage stable. Le schéma de colonnes (''code_bv'', ''id_brut_miom'',
  ''code_circonscription'' etc.) est fixé côté concaténation mais n''impose aucune
  contrainte de stabilité inter-scrutin sur les identifiants eux-mêmes.'
---

*Suggested by [[aggregation]] — core task functions likely containing table-bv-reu.csv join/generation logic (rendered blob page)*

[Skip to content](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/task_functions.py#start-of-content)
You signed in with another tab or window. [Reload](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/task_functions.py) to refresh your session. You signed out in another tab or window. [Reload](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/task_functions.py) to refresh your session. You switched accounts on another tab or window. [Reload](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/task_functions.py) to refresh your session. Dismiss alert
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/task_functions.py).
/ **[datagouvfr_data_pipelines](https://github.com/datagouv/datagouvfr_data_pipelines) ** Public
  * [ Notifications ](https://github.com/login?return_to=%2Fdatagouv%2Fdatagouvfr_data_pipelines) You must be signed in to change notification settings
  * [ Fork 7 ](https://github.com/login?return_to=%2Fdatagouv%2Fdatagouvfr_data_pipelines)
  * [ Star  18 ](https://github.com/login?return_to=%2Fdatagouv%2Fdatagouvfr_data_pipelines)


## Collapse file tree
## Files
Search this repository(forward slash)` forward slash/`
/
# task_functions.py
Copy path
More file actions
More file actions
## Latest commit
[Add insights for data processing DAGs (](https://github.com/datagouv/datagouvfr_data_pipelines/commit/5e28b04eb107f7e81590eadcb64823439d134542)[#679](https://github.com/datagouv/datagouvfr_data_pipelines/pull/679)[)](https://github.com/datagouv/datagouvfr_data_pipelines/commit/5e28b04eb107f7e81590eadcb64823439d134542)
Open commit detailssuccess
Jul 2, 2026
[5e28b04](https://github.com/datagouv/datagouvfr_data_pipelines/commit/5e28b04eb107f7e81590eadcb64823439d134542) · Jul 2, 2026
## History
[History](https://github.com/datagouv/datagouvfr_data_pipelines/commits/main/data_processing/elections/aggregation/task_functions.py)
Open commit details
History
204 lines (191 loc) · 7.39 KB
/
# task_functions.py
Copy path
## File metadata and controls
  * 

204 lines (191 loc) · 7.39 KB
Copy raw file
Download raw file
You must be signed in to make or propose changes
More edit options
Open symbols panel
Edit and raw actions
import json import logging import os from datetime import datetime import pandas as pd from airflow.sdk import task from datagouv import Client from datagouvfr_data_pipelines.config import ( AIRFLOW_DAG_HOME, AIRFLOW_DAG_TMP, AIRFLOW_ENV, S3_BUCKET_DATA_PIPELINE_OPEN, ) from datagouvfr_data_pipelines.utils.conversions import csv_to_parquet from datagouvfr_data_pipelines.utils.datagouv import local_client from datagouvfr_data_pipelines.utils.filesystem import File from datagouvfr_data_pipelines.utils.s3 import S3Client from datagouvfr_data_pipelines.utils.tchap import send_message DAG_FOLDER = "datagouvfr_data_pipelines/data_processing/" TMP_FOLDER = f"{AIRFLOW_DAG_TMP}elections/" dtypes: dict[str, dict[str, str]] = { "general": { "id_election": "VARCHAR", "id_brut_miom": "VARCHAR", "code_departement": "VARCHAR", "libelle_departement": "VARCHAR", "code_canton": "VARCHAR", "libelle_canton": "VARCHAR", "code_commune": "VARCHAR", "libelle_commune": "VARCHAR", "code_circonscription": "VARCHAR", "libelle_circonscription": "VARCHAR", "code_bv": "VARCHAR", "inscrits": "INT32", "abstentions": "INT32", "votants": "INT32", "blancs": "INT32", "nuls": "INT32", "exprimes": "INT32", "ratio_abstentions_inscrits": "FLOAT", "ratio_votants_inscrits": "FLOAT", "ratio_blancs_inscrits": "FLOAT", "ratio_blancs_votants": "FLOAT", "ratio_nuls_inscrits": "FLOAT", "ratio_nuls_votants": "FLOAT", "ratio_exprimes_inscrits": "FLOAT", "ratio_exprimes_votants": "FLOAT", }, "candidats": { "id_election": "VARCHAR", "id_brut_miom": "VARCHAR", "code_departement": "VARCHAR", "code_commune": "VARCHAR", "code_bv": "VARCHAR", "no_panneau": "INT32", "voix": "INT32", "ratio_voix_inscrits": "FLOAT", "ratio_voix_exprimes": "FLOAT", "nuance": "VARCHAR", "sexe": "VARCHAR", "nom": "VARCHAR", "prenom": "VARCHAR", "liste": "VARCHAR", "libelle_abrege_liste": "VARCHAR", "libelle_etendu_liste": "VARCHAR", "nom_tete_liste": "VARCHAR", "binome": "VARCHAR", }, } _types = { "INT32": int, "FLOAT": float, } @task() def process_election_data(): # getting preprocessed resources, the magic is there (when creating standardized files), here we only concatenate them resources_url = [ r["url"] for r in Client().get_all_from_api_query( # due to https://github.com/MongoEngine/mongoengine/issues/2748 # we have to specify a sort parameter for now "api/1/datasets/community_resources/" "?organization=646b7187b50b2a93b1ae3d45&sort=-created_at_internal" ) ] # when creating a standardized file, make sure to name it properly so that it is considered here (and don't name other files the same) resources = { "general": [r for r in resources_url if "general-results.csv" in r], "candidats": [r for r in resources_url if "candidats-results.csv" in r], } for scope in ["general", "candidats"]: logging.info(f"Processing {scope} resources") for idx, url in enumerate(resources[scope]): logging.info("> " + url) df = pd.read_csv(url, sep=";", dtype=str) assert all(col in dtypes[scope].keys() for col in df.columns) # add missing columns and reorder for concatenation for col in dtypes[scope].keys(): if col not in df.columns: df[col] = "" df = df[dtypes[scope].keys()] # concatenating all files (first one has header) df.to_csv( TMP_FOLDER + f"{scope}_results.csv", sep=";", index=False, mode="w" if idx == 0 else "a", header=idx == 0, ) del df # hydra is not (yet) able to ingest the big csv, maybe soon? :eyes: logging.info("Export en parquet...") csv_to_parquet( csv_file_path=TMP_FOLDER + f"{scope}_results.csv", dtype=dtypes[scope], ) @task() def send_results_to_s3(): S3Client(bucket=S3_BUCKET_DATA_PIPELINE_OPEN).send_files( list_files=[ File( source_path=TMP_FOLDER, source_name=f"{scope}_results.{ext}", dest_path="elections/", dest_name=f"{scope}_results.{ext}", content_type=( "application/vnd.apache.parquet" if ext == "parquet" else "text/csv" ), ) for scope in ["general", "candidats"] for ext in ["csv", "parquet"] ], ignore_airflow_env=True, is_public=True, ) @task() def publish_results_elections(): s3_client = S3Client(bucket=S3_BUCKET_DATA_PIPELINE_OPEN) with open(f"{AIRFLOW_DAG_HOME}{DAG_FOLDER}elections/aggregation/config.json") as fp: config = json.load(fp) for ext in ["csv", "parquet"]: local_client.resource( id=config["general"][ext][AIRFLOW_ENV]["resource_id"], dataset_id=config["dataset_id"][AIRFLOW_ENV], fetch=False, ).update( payload={ "url": s3_client.get_file_url(f"elections/general_results.{ext}"), "filesize": os.path.getsize(TMP_FOLDER + f"general_results.{ext}"), "title": "Résultats généraux", "format": ext, "description": ( f"Résultats généraux des élections agrégés au niveau des bureaux de votes," " créés à partir des données du Ministère de l'Intérieur" f", au format {ext}" f" (dernière modification : {datetime.today().strftime('%Y-%m-%d')})" ), }, ) logging.info(f"Done with general results {ext}") local_client.resource( id=config["candidats"][ext][AIRFLOW_ENV]["resource_id"], dataset_id=config["dataset_id"][AIRFLOW_ENV], fetch=False, ).update( payload={ "url": s3_client.get_file_url(f"elections/candidats_results.{ext}"), "filesize": os.path.getsize(TMP_FOLDER + f"candidats_results.{ext}"), "title": "Résultats par candidat", "format": ext, "description": ( f"Résultats des élections par candidat agrégés au niveau des bureaux de votes," " créés à partir des données du Ministère de l'Intérieur" f", au format {ext}" f" (dernière modification : {datetime.today().strftime('%Y-%m-%d')})" ), }, ) logging.info(f"Done with candidats results {ext}") @task() def notification(): with open(f"{AIRFLOW_DAG_HOME}{DAG_FOLDER}elections/aggregation/config.json") as fp: config = json.load(fp) send_message( text=( "📣 Données élections mises à jour.\n\n" f"- Données stockées sur S3 - Bucket {S3_BUCKET_DATA_PIPELINE_OPEN}\n" f"- Données référencées [sur data.gouv.fr]({local_client.base_url}/datasets/" f"{config['dataset_id'][AIRFLOW_ENV]})" ) )
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
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
import json
import logging
import os
from datetime import datetime
import pandas as pd
from airflow.sdk import task
from datagouv import Client
from datagouvfr_data_pipelines.config import (
AIRFLOW_DAG_HOME,
AIRFLOW_DAG_TMP,
AIRFLOW_ENV,
S3_BUCKET_DATA_PIPELINE_OPEN,
from datagouvfr_data_pipelines.utils.conversions import csv_to_parquet
from datagouvfr_data_pipelines.utils.datagouv import local_client
from datagouvfr_data_pipelines.utils.filesystem import File
from datagouvfr_data_pipelines.utils.s3 import S3Client
from datagouvfr_data_pipelines.utils.tchap import send_message
DAG_FOLDER = "datagouvfr_data_pipelines/data_processing/"
TMP_FOLDER = f"{AIRFLOW_DAG_TMP}elections/"
dtypes: dict[str, dict[str, str]] = {
"general": {
"id_election": "VARCHAR",
"id_brut_miom": "VARCHAR",
"code_departement": "VARCHAR",
"libelle_departement": "VARCHAR",
"code_canton": "VARCHAR",
"libelle_canton": "VARCHAR",
"code_commune": "VARCHAR",
"libelle_commune": "VARCHAR",
"code_circonscription": "VARCHAR",
"libelle_circonscription": "VARCHAR",
"code_bv": "VARCHAR",
"inscrits": "INT32",
"abstentions": "INT32",
"votants": "INT32",
"blancs": "INT32",
"nuls": "INT32",
"exprimes": "INT32",
"ratio_abstentions_inscrits": "FLOAT",
"ratio_votants_inscrits": "FLOAT",
"ratio_blancs_inscrits": "FLOAT",
"ratio_blancs_votants": "FLOAT",
"ratio_nuls_inscrits": "FLOAT",
"ratio_nuls_votants": "FLOAT",
"ratio_exprimes_inscrits": "FLOAT",
"ratio_exprimes_votants": "FLOAT",
"candidats": {
"id_election": "VARCHAR",
"id_brut_miom": "VARCHAR",
"code_departement": "VARCHAR",
"code_commune": "VARCHAR",
"code_bv": "VARCHAR",
"no_panneau": "INT32",
"voix": "INT32",
"ratio_voix_inscrits": "FLOAT",
"ratio_voix_exprimes": "FLOAT",
"nuance": "VARCHAR",
"sexe": "VARCHAR",
"nom": "VARCHAR",
"prenom": "VARCHAR",
"liste": "VARCHAR",
"libelle_abrege_liste": "VARCHAR",
"libelle_etendu_liste": "VARCHAR",
"nom_tete_liste": "VARCHAR",
"binome": "VARCHAR",
_types = {
"INT32": int,
"FLOAT": float,
@task()
def process_election_data():
# getting preprocessed resources, the magic is there (when creating standardized files), here we only concatenate them
resources_url = [
r["url"]
for r in Client().get_all_from_api_query(
# due to https://github.com/MongoEngine/mongoengine/issues/2748
# we have to specify a sort parameter for now
"api/1/datasets/community_resources/"
"?organization=646b7187b50b2a93b1ae3d45&sort=-created_at_internal"
# when creating a standardized file, make sure to name it properly so that it is considered here (and don't name other files the same)
resources = {
"general": [r for r in resources_url if "general-results.csv" in r],
"candidats": [r for r in resources_url if "candidats-results.csv" in r],
for scope in ["general", "candidats"]:
logging.info(f"Processing {scope} resources")
for idx, url in enumerate(resources[scope]):
logging.info("> " + url)
df = pd.read_csv(url, sep=";", dtype=str)
assert all(col in dtypes[scope].keys() for col in df.columns)
# add missing columns and reorder for concatenation
for col in dtypes[scope].keys():
if col df.columns:
df[col] = ""
df = df[dtypes[scope].keys()]
# concatenating all files (first one has header)
df.to_csv(
TMP_FOLDER + f"{scope}_results.csv",
sep=";",
index=False,
mode="w" if idx == 0 else "a",
header=idx == 0,
del df
# hydra is not (yet) able to ingest the big csv, maybe soon? :eyes:
logging.info("Export en parquet...")
csv_to_parquet(
csv_file_path=TMP_FOLDER + f"{scope}_results.csv",
dtype=dtypes[scope],
@task()
def send_results_to_s3():
S3Client(bucket=S3_BUCKET_DATA_PIPELINE_OPEN).send_files(
list_files=[
File(
source_path=TMP_FOLDER,
source_name=f"{scope}_results.",
dest_path="elections/",
dest_name=f"{scope}_results.",
content_type=(
"application/vnd.apache.parquet" if ext == "parquet" else "text/csv"
for scope in ["general", "candidats"]
for ext in ["csv", "parquet"]
ignore_airflow_env=True,
is_public=True,
@task()
def publish_results_elections():
s3_client = S3Client(bucket=S3_BUCKET_DATA_PIPELINE_OPEN)
with open(f"{AIRFLOW_DAG_HOME}{DAG_FOLDER}elections/aggregation/config.json") as fp:
config = json.load(fp)
for ext in ["csv", "parquet"]:
local_client.resource(
id=config["general"][ext][AIRFLOW_ENV]["resource_id"],
dataset_id=config["dataset_id"][AIRFLOW_ENV],
fetch=False,
).update(
payload={
"url": s3_client.get_file_url(f"elections/general_results."),
"filesize": os.path.getsize(TMP_FOLDER + f"general_results."),
"title": "Résultats généraux",
"format": ext,
"description": (
f"Résultats généraux des élections agrégés au niveau des bureaux de votes,"
" créés à partir des données du Ministère de l'Intérieur"
f", au format "
f" (dernière modification : {datetime.today().strftime('%Y-%m-%d')})"
logging.info(f"Done with general results ")
local_client.resource(
id=config["candidats"][ext][AIRFLOW_ENV]["resource_id"],
dataset_id=config["dataset_id"][AIRFLOW_ENV],
fetch=False,
).update(
payload={
"url": s3_client.get_file_url(f"elections/candidats_results."),
"filesize": os.path.getsize(TMP_FOLDER + f"candidats_results."),
"title": "Résultats par candidat",
"format": ext,
"description": (
f"Résultats des élections par candidat agrégés au niveau des bureaux de votes,"
" créés à partir des données du Ministère de l'Intérieur"
f", au format "
f" (dernière modification : {datetime.today().strftime('%Y-%m-%d')})"
logging.info(f"Done with candidats results ")
@task()
def notification():
with open(f"{AIRFLOW_DAG_HOME}{DAG_FOLDER}elections/aggregation/config.json") as fp:
config = json.load(fp)
send_message(
text=(
"📣 Données élections mises à jour.\n\n"
f"- Données stockées sur S3 - Bucket {S3_BUCKET_DATA_PIPELINE_OPEN}\n"
f"- Données référencées [sur data.gouv.fr]({local_client.base_url}/datasets/"
f"{config['dataset_id'][AIRFLOW_ENV]})"
You can’t perform that action at this time. 
While the code is focused, press Alt+F1 for a menu of operations.
