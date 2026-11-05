---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: depression_classifier_weighted
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# depression_classifier_weighted

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8372
- F1: 0.5493

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 1.0   | 451  | 0.8894          | 0.5155 |
| 0.8741        | 2.0   | 902  | 0.8372          | 0.5493 |


### Framework versions

- Transformers 4.28.0
- Pytorch 2.0.1+cu118
- Datasets 2.12.0
- Tokenizers 0.13.3
