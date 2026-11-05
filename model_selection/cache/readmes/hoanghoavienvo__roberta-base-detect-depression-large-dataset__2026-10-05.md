---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: roberta-base-detect-depression-large-dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-detect-depression-large-dataset

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5713
- Accuracy: 0.785
- F1: 0.8432

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
| 0.6291        | 1.0   | 1157 | 0.6365          | 0.675    | 0.7860 |
| 0.6281        | 2.0   | 2314 | 0.6803          | 0.602    | 0.7509 |
| 0.6344        | 3.0   | 3471 | 0.6679          | 0.612    | 0.7557 |
| 0.6367        | 4.0   | 4628 | 0.6746          | 0.6      | 0.7500 |
| 0.6193        | 5.0   | 5785 | 0.5713          | 0.785    | 0.8432 |


### Framework versions

- Transformers 4.30.1
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.13.3
