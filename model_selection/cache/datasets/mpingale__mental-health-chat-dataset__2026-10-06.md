---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: questionID
    dtype: int64
  - name: questionTitle
    dtype: string
  - name: questionText
    dtype: string
  - name: questionLink
    dtype: string
  - name: topic
    dtype: string
  - name: therapistInfo
    dtype: string
  - name: therapistURL
    dtype: string
  - name: answerText
    dtype: string
  - name: upvotes
    dtype: int64
  - name: views
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7642829
    num_examples: 2775
  download_size: 3638427
  dataset_size: 7642829
---
# Dataset Card for "mental-health-chat-dataset"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)