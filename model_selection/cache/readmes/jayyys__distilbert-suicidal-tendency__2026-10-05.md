---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: distilbert-suicidal-tendency
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-suicidal-tendency

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4168
- F1: 0.3266

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.3892        | 1.0   | 25   | 1.3874          | 0.1962 |
| 1.3629        | 2.0   | 50   | 1.3859          | 0.2054 |
| 1.3157        | 3.0   | 75   | 1.3773          | 0.2706 |
| 1.255         | 4.0   | 100  | 1.3953          | 0.2920 |
| 1.1963        | 5.0   | 125  | 1.3893          | 0.2279 |
| 1.1309        | 6.0   | 150  | 1.3790          | 0.2943 |
| 1.0629        | 7.0   | 175  | 1.4011          | 0.3350 |
| 1.0059        | 8.0   | 200  | 1.3992          | 0.3041 |
| 0.9766        | 9.0   | 225  | 1.4052          | 0.3200 |
| 0.9551        | 10.0  | 250  | 1.4168          | 0.3266 |


### Framework versions

- Transformers 4.45.2
- Pytorch 2.4.1+cu118
- Datasets 3.0.1
- Tokenizers 0.20.0
