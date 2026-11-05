---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: ADHDvsN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ADHDvsN

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7460
- F1: 0.684
- Roc Auc: 0.6836
- Accuracy: 0.684

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
| 0.6333        | 1.0   | 875  | 0.6383          | 0.6368 | 0.6321  | 0.6368   |
| 0.591         | 2.0   | 1750 | 0.6384          | 0.6925 | 0.6926  | 0.6925   |
| 0.5103        | 3.0   | 2625 | 0.6349          | 0.6827 | 0.6855  | 0.6827   |
| 0.4122        | 4.0   | 3500 | 0.6424          | 0.668  | 0.6658  | 0.668    |
| 0.3287        | 5.0   | 4375 | 0.7460          | 0.684  | 0.6836  | 0.684    |


### Framework versions

- Transformers 4.27.3
- Pytorch 1.13.0
- Datasets 2.1.0
- Tokenizers 0.13.2
