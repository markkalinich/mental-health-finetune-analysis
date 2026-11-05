---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: roberta-base-detect-depression-large-dataset-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-detect-depression-large-dataset-v3

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6044
- Accuracy: 0.6918
- F1: 0.7921

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
| 0.6532        | 1.0   | 876  | 0.5777          | 0.6527   | 0.7536 |
| 0.6325        | 2.0   | 1752 | 0.5926          | 0.7322   | 0.8342 |
| 0.6348        | 3.0   | 2628 | 0.5959          | 0.7433   | 0.8461 |
| 0.635         | 4.0   | 3504 | 0.5781          | 0.7436   | 0.8449 |
| 0.6177        | 5.0   | 4380 | 0.6044          | 0.6918   | 0.7921 |


### Framework versions

- Transformers 4.30.1
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.13.3
