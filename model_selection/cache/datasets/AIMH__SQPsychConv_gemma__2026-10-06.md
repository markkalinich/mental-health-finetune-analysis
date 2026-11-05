---
dataset_info:
  features:
  - name: file_id
    dtype: string
  - name: condition
    dtype: string
  - name: client_model
    dtype: string
  - name: therapist_model
    dtype: string
  - name: dialogue
    dtype: string
  splits:
  - name: train
    num_bytes: 18789519
    num_examples: 1837
  - name: test
    num_bytes: 2672008
    num_examples: 253
  download_size: 10813058
  dataset_size: 21461527
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
license: apache-2.0
---