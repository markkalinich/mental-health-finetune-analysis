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
  - name: safe
    num_bytes: 614916738
    num_examples: 204
  - name: unsafe
    num_bytes: 1063394605
    num_examples: 361
  - name: causal_risky
    num_bytes: 338388304
    num_examples: 111
  - name: decoupled_benign
    num_bytes: 341448480
    num_examples: 112
  - name: selective_risky
    num_bytes: 725006328
    num_examples: 250
  - name: absent_benign
    num_bytes: 273468258
    num_examples: 92
  download_size: 3354108160
  dataset_size: 3356622713
configs:
- config_name: default
  data_files:
  - split: safe
    path: data/safe-*
  - split: unsafe
    path: data/unsafe-*
  - split: causal_risky
    path: data/causal_risky-*
  - split: decoupled_benign
    path: data/decoupled_benign-*
  - split: selective_risky
    path: data/selective_risky-*
  - split: absent_benign
    path: data/absent_benign-*
---
