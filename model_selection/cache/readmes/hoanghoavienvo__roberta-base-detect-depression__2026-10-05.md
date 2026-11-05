---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: roberta-base-detect-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-detect-depression

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1225
- Accuracy: 0.675
- F1: 0.7486

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 376  | 0.5270          | 0.759    | 0.8280 |
| 0.6082        | 2.0   | 752  | 0.5791          | 0.698    | 0.7618 |
| 0.5139        | 3.0   | 1128 | 0.6764          | 0.692    | 0.7852 |
| 0.3598        | 4.0   | 1504 | 0.7543          | 0.707    | 0.7755 |
| 0.3598        | 5.0   | 1880 | 1.1225          | 0.675    | 0.7486 |


### Framework versions

- Transformers 4.30.2
- Pytorch 2.0.1+cu118
- Datasets 2.13.1
- Tokenizers 0.13.3
