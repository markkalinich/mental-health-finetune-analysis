---
license: mit
base_model: xlnet/xlnet-base-cased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: emotional-xlnet
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotional-xlnet

This model is a fine-tuned version of [xlnet/xlnet-base-cased](https://huggingface.co/xlnet/xlnet-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9968
- Accuracy: 0.3875
- F1: 0.3676
- Precision: 0.3990
- Recall: 0.3875

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 2.4746        | 1.0   | 270  | 2.3530          | 0.3085   | 0.2878 | 0.4138    | 0.3085 |
| 0.8581        | 2.0   | 540  | 2.1600          | 0.3466   | 0.3310 | 0.3603    | 0.3466 |
| 0.2628        | 3.0   | 810  | 2.3594          | 0.3575   | 0.3519 | 0.4060    | 0.3575 |
| 0.0791        | 4.0   | 1080 | 2.7493          | 0.3793   | 0.3643 | 0.3901    | 0.3793 |
| 0.0292        | 5.0   | 1350 | 2.9968          | 0.3875   | 0.3676 | 0.3990    | 0.3875 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
