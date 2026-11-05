---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-detect-depression-stage-one
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-detect-depression-stage-one

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4151
- Accuracy: 0.674
- F1: 0.7530

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.6185        | 1.0   | 751  | 0.5223          | 0.762    | 0.8260 |
| 0.5394        | 2.0   | 1502 | 0.5958          | 0.692    | 0.7488 |
| 0.4387        | 3.0   | 2253 | 0.6742          | 0.706    | 0.7885 |
| 0.3157        | 4.0   | 3004 | 1.1284          | 0.696    | 0.7768 |
| 0.1794        | 5.0   | 3755 | 1.4151          | 0.674    | 0.7530 |


### Framework versions

- Transformers 4.30.2
- Pytorch 2.0.1+cu118
- Datasets 2.13.1
- Tokenizers 0.13.3
