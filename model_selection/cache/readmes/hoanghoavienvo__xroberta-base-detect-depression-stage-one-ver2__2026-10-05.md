---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: xroberta-base-detect-depression-stage-one-ver2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xroberta-base-detect-depression-stage-one-ver2

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6403
- Accuracy: 0.717
- F1: 0.7893

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
| 0.6432        | 1.0   | 751  | 0.5957          | 0.743    | 0.8219 |
| 0.6285        | 2.0   | 1502 | 0.5813          | 0.719    | 0.8085 |
| 0.6165        | 3.0   | 2253 | 0.6459          | 0.7      | 0.7976 |
| 0.5371        | 4.0   | 3004 | 0.5612          | 0.743    | 0.8120 |
| 0.46          | 5.0   | 3755 | 0.6403          | 0.717    | 0.7893 |


### Framework versions

- Transformers 4.30.2
- Pytorch 2.0.1+cu118
- Datasets 2.13.1
- Tokenizers 0.13.3
