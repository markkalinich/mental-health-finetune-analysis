---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: image_path
    dtype: string
  - name: risk
    dtype: string
  - name: type
    dtype: string
  - name: scenario_type
    dtype: string
  - name: risk_type
    dtype: string
  - name: risk_subtype
    dtype: string
  - name: situation
    dtype: string
  - name: hazard
    dtype: string
  - name: action
    dtype: string
  - name: room
    dtype: string
  - name: multi_scenario
    dtype: string
  - name: pair_item_id
    dtype: string
  splits:
  - name: causal_risky
    num_bytes: 928319400
    num_examples: 75
  - name: decoupled_benign
    num_bytes: 928319902
    num_examples: 75
  - name: selective_risky
    num_bytes: 1260806037
    num_examples: 104
  - name: absent_benign
    num_bytes: 928318903
    num_examples: 75
  download_size: 4045458836
  dataset_size: 4045764242
configs:
- config_name: default
  data_files:
  - split: causal_risky
    path: data/causal_risky-*
  - split: decoupled_benign
    path: data/decoupled_benign-*
  - split: selective_risky
    path: data/selective_risky-*
  - split: absent_benign
    path: data/absent_benign-*
license: apache-2.0
language:
- en
pretty_name: EMBGuardTes
---
