---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 1204169
    num_examples: 891
  download_size: 453426
  dataset_size: 1204169
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
