---
dataset_info:
  features:
  - name: illness
    dtype: string
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 622676
    num_examples: 168
  download_size: 317175
  dataset_size: 622676
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
