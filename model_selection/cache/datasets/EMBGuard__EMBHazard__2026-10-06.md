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
  - name: train
    num_bytes: 45690960046
    num_examples: 15115
  download_size: 45655524894
  dataset_size: 45690960046
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- en
pretty_name: EMBHazar
---
