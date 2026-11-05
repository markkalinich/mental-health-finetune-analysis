---
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-pii-200
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-pii-200

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4704
- Overall Precision: 0.0
- Overall Recall: 0.0
- Overall F1: 0.0
- Overall Accuracy: 0.8065
- Email F1: 0.0
- Lastname F1: 0.0
- Prefix F1: 0.0

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.2
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy | City F1 | Email F1 | Jobtype F1 | Lastname F1 | Prefix F1 | Username F1 |
|:-------------:|:-----:|:----:|:---------------:|:-----------------:|:--------------:|:----------:|:----------------:|:-------:|:--------:|:----------:|:-----------:|:---------:|:-----------:|
| No log        | 1.0   | 1    | 2.5786          | 0.0               | 0.0            | 0.0        | 0.0              | 0.0     | 0.0      | 0.0        | 0.0         | 0.0       | 0.0         |
| No log        | 2.0   | 2    | 2.3959          | 0.0               | 0.0            | 0.0        | 0.1774           | 0.0     | 0.0      | 0.0        | 0.0         | 0.0       | 0.0         |
| No log        | 3.0   | 3    | 2.0696          | 0.0               | 0.0            | 0.0        | 0.8065           | 0.0     | 0.0      | 0.0        |
| No log        | 4.0   | 4    | 1.8231          | 0.0               | 0.0            | 0.0        | 0.8065           | 0.0     | 0.0      | 0.0        |
| No log        | 5.0   | 5    | 1.6430          | 0.0               | 0.0            | 0.0        | 0.8065           | 0.0     | 0.0      | 0.0        |
| No log        | 6.0   | 6    | 1.5266          | 0.0               | 0.0            | 0.0        | 0.8065           | 0.0     | 0.0      | 0.0        |
| No log        | 7.0   | 7    | 1.4704          | 0.0               | 0.0            | 0.0        | 0.8065           | 0.0     | 0.0      | 0.0        |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.3.1+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
