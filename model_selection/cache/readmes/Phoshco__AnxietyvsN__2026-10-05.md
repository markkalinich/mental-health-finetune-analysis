---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: AnxietyvsN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AnxietyvsN

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7110
- F1: 0.7250
- Roc Auc: 0.7227
- Accuracy: 0.725

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Roc Auc | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|:--------:|
| 0.5585        | 1.0   | 875  | 0.5816          | 0.7123 | 0.7049  | 0.7123   |
| 0.4384        | 2.0   | 1750 | 0.5513          | 0.7402 | 0.7395  | 0.7402   |
| 0.2335        | 3.0   | 2625 | 0.8404          | 0.7224 | 0.7262  | 0.7224   |
| 0.1009        | 4.0   | 3500 | 1.4763          | 0.7174 | 0.7184  | 0.7174   |
| 0.0385        | 5.0   | 4375 | 1.7110          | 0.7250 | 0.7227  | 0.725    |


### Framework versions

- Transformers 4.27.3
- Pytorch 1.13.0
- Datasets 2.1.0
- Tokenizers 0.13.2
