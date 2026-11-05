---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: ptsdvsN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ptsdvsN

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0050
- F1: 0.8051
- Roc Auc: 0.8042
- Accuracy: 0.8051

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
| 0.4907        | 1.0   | 875  | 0.4679          | 0.8161 | 0.8164  | 0.8161   |
| 0.3568        | 2.0   | 1750 | 0.4654          | 0.8221 | 0.8225  | 0.8221   |
| 0.2289        | 3.0   | 2625 | 0.7412          | 0.7843 | 0.7800  | 0.7843   |
| 0.1246        | 4.0   | 3500 | 0.8720          | 0.8013 | 0.7995  | 0.8013   |
| 0.0656        | 5.0   | 4375 | 1.0050          | 0.8051 | 0.8042  | 0.8051   |


### Framework versions

- Transformers 4.27.3
- Pytorch 1.13.0
- Datasets 2.1.0
- Tokenizers 0.13.2
