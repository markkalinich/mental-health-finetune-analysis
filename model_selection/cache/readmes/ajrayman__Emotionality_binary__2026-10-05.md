---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: Emotionality_binary
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Emotionality_binary

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7371
- Accuracy: 0.6090
- Precision: 0.5731
- Recall: 0.8504
- F1: 0.6847
- Auc: 0.7206

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 1234
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     | Auc    |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|:------:|
| No log        | 1.0   | 118  | 0.6599          | 0.6040   | 0.5662    | 0.8853 | 0.6907 | 0.7066 |
| No log        | 2.0   | 236  | 0.6181          | 0.6613   | 0.6476    | 0.7057 | 0.6754 | 0.7238 |
| No log        | 3.0   | 354  | 0.7371          | 0.6090   | 0.5731    | 0.8504 | 0.6847 | 0.7206 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
