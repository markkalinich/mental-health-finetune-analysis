---
tags:
- generated_from_trainer
model-index:
- name: amir-clinicalbert-specialities
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# amir-clinicalbert-specialities

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.4721

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 156  | 3.5906          |
| No log        | 2.0   | 312  | 3.4887          |
| No log        | 3.0   | 468  | 3.4748          |
| 3.6945        | 4.0   | 624  | 3.4721          |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.1
- Datasets 2.15.0
- Tokenizers 0.15.0
