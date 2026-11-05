---
license: apache-2.0
base_model: bert-large-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-large-uncased-detect-depression-stage-one-v4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased-detect-depression-stage-one-v4

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7637
- Accuracy: 0.717
- F1: 0.7838

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.5824        | 1.0   | 1502 | 0.5673          | 0.726    | 0.7832 |
| 0.5499        | 2.0   | 3004 | 0.6104          | 0.725    | 0.7976 |
| 0.486         | 3.0   | 4506 | 0.7637          | 0.717    | 0.7838 |


### Framework versions

- Transformers 4.31.0
- Pytorch 2.0.1+cu118
- Datasets 2.13.1
- Tokenizers 0.13.3
