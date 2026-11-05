---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: bipolarvsN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bipolarvsN

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7437
- F1: 0.7833
- Roc Auc: 0.7818
- Accuracy: 0.7833

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
| 0.5251        | 1.0   | 875  | 0.5404          | 0.736  | 0.7299  | 0.736    |
| 0.4396        | 2.0   | 1750 | 0.4694          | 0.7974 | 0.7966  | 0.7974   |
| 0.373         | 3.0   | 2625 | 0.5041          | 0.797  | 0.7963  | 0.797    |
| 0.2828        | 4.0   | 3500 | 0.6178          | 0.7939 | 0.7931  | 0.7939   |
| 0.2147        | 5.0   | 4375 | 0.7437          | 0.7833 | 0.7818  | 0.7833   |


### Framework versions

- Transformers 4.27.3
- Pytorch 1.13.0
- Datasets 2.1.0
- Tokenizers 0.13.2
