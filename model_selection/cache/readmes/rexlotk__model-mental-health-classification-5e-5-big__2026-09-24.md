---
license: apache-2.0
base_model: google-bert/bert-base-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: model-mental-health-classification-5e-5-big
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model-mental-health-classification-5e-5-big

This model is a fine-tuned version of [google-bert/bert-base-cased](https://huggingface.co/google-bert/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1953
- Accuracy: 0.5663

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
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 1.2268        | 1.0   | 5254  | 1.2183          | 0.5605   |
| 1.054         | 2.0   | 10508 | 1.1953          | 0.5663   |
| 0.7959        | 3.0   | 15762 | 1.3567          | 0.5635   |
| 0.5561        | 4.0   | 21016 | 2.0386          | 0.5659   |
| 0.3427        | 5.0   | 26270 | 2.5403          | 0.5659   |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
