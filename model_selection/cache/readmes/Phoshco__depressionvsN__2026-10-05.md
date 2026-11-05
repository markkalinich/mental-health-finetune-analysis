---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: depressionvsN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# depressionvsN

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1005
- F1: 0.6615
- Roc Auc: 0.6610
- Accuracy: 0.6615

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
| 0.6688        | 1.0   | 875  | 0.6239          | 0.6552 | 0.6546  | 0.6552   |
| 0.5832        | 2.0   | 1750 | 0.5966          | 0.6786 | 0.6789  | 0.6786   |
| 0.4778        | 3.0   | 2625 | 0.6958          | 0.6791 | 0.6795  | 0.6791   |
| 0.3487        | 4.0   | 3500 | 0.7418          | 0.6637 | 0.6617  | 0.6637   |
| 0.2266        | 5.0   | 4375 | 1.1005          | 0.6615 | 0.6610  | 0.6615   |


### Framework versions

- Transformers 4.27.3
- Pytorch 1.13.0
- Datasets 2.1.0
- Tokenizers 0.13.2
