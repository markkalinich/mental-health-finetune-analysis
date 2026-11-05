---
license: mit
base_model: roberta-large
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta-large-depression-classification-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-depression-classification-v2

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2328
- Accuracy: 0.5435
- F1 Score: 0.5316

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Score |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.9778        | 1.0   | 677  | 1.2323          | 0.5380   | 0.5275   |
| 0.6377        | 2.0   | 1354 | 2.0223          | 0.5315   | 0.5125   |
| 0.5285        | 3.0   | 2031 | 2.2328          | 0.5435   | 0.5316   |


### Framework versions

- Transformers 4.31.0
- Pytorch 2.0.1+cu118
- Datasets 2.14.4
- Tokenizers 0.13.3
