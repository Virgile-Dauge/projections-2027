---
title: aggregation
id: aggregation
tags:
- projections-electorales-bureaux-2027-b0b1c4
- locus-crosswalk-bureaux-fiabilite
created: '2026-07-21T19:35:29.157259Z'
updated: '2026-07-21T19:42:36.633641Z'
source: https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation
source_domain: api.github.com
fetched_at: '2026-07-21T19:35:29.116926Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: ground_truth
content_type: code
deprecated: false
summary: Suggested by elections — drill into aggregation subdir to find REU join /
  table-bv-reu.csv code
---

*Suggested by [[elections]] — drill into aggregation subdir to find REU join / table-bv-reu.csv code*


```
[
  {
    "name": "README.md",
    "path": "data_processing/elections/aggregation/README.md",
    "sha": "b0e592ec6ab729c98b7679b6e163601baa6f5fe9",
    "size": 671,
    "url": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation/README.md?ref=main",
    "html_url": "https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/README.md",
    "git_url": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/git/blobs/b0e592ec6ab729c98b7679b6e163601baa6f5fe9",
    "download_url": "https://raw.githubusercontent.com/datagouv/datagouvfr_data_pipelines/main/data_processing/elections/aggregation/README.md",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation/README.md?ref=main",
      "git": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/git/blobs/b0e592ec6ab729c98b7679b6e163601baa6f5fe9",
      "html": "https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/README.md"
    }
  },
  {
    "name": "config.json",
    "path": "data_processing/elections/aggregation/config.json",
    "sha": "30f0d3a01f5c45afb294cdcc73000a83d4dceb3c",
    "size": 1136,
    "url": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation/config.json?ref=main",
    "html_url": "https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/config.json",
    "git_url": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/git/blobs/30f0d3a01f5c45afb294cdcc73000a83d4dceb3c",
    "download_url": "https://raw.githubusercontent.com/datagouv/datagouvfr_data_pipelines/main/data_processing/elections/aggregation/config.json",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation/config.json?ref=main",
      "git": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/git/blobs/30f0d3a01f5c45afb294cdcc73000a83d4dceb3c",
      "html": "https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/config.json"
    }
  },
  {
    "name": "dag.py",
    "path": "data_processing/elections/aggregation/dag.py",
    "sha": "837f76f0d15567043f928b6979e1e1172f239b4d",
    "size": 837,
    "url": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation/dag.py?ref=main",
    "html_url": "https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/dag.py",
    "git_url": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/git/blobs/837f76f0d15567043f928b6979e1e1172f239b4d",
    "download_url": "https://raw.githubusercontent.com/datagouv/datagouvfr_data_pipelines/main/data_processing/elections/aggregation/dag.py",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation/dag.py?ref=main",
      "git": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/git/blobs/837f76f0d15567043f928b6979e1e1172f239b4d",
      "html": "https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/dag.py"
    }
  },
  {
    "name": "task_functions.py",
    "path": "data_processing/elections/aggregation/task_functions.py",
    "sha": "eb487230c25dc635c4232b23aa03ec2536f68839",
    "size": 7564,
    "url": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation/task_functions.py?ref=main",
    "html_url": "https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/task_functions.py",
    "git_url": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/git/blobs/eb487230c25dc635c4232b23aa03ec2536f68839",
    "download_url": "https://raw.githubusercontent.com/datagouv/datagouvfr_data_pipelines/main/data_processing/elections/aggregation/task_functions.py",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/contents/data_processing/elections/aggregation/task_functions.py?ref=main",
      "git": "https://api.github.com/repos/datagouv/datagouvfr_data_pipelines/git/blobs/eb487230c25dc635c4232b23aa03ec2536f68839",
      "html": "https://github.com/datagouv/datagouvfr_data_pipelines/blob/main/data_processing/elections/aggregation/task_functions.py"
    }
  }
]

```

