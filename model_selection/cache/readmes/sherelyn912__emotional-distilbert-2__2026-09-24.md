---
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: emotional-distilbert-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotional-distilbert-2

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2738
- Accuracy: 0.4174
- F1: 0.4086
- Precision: 0.4232
- Recall: 0.4174

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
| 2.7378        | 1.0   | 270  | 2.6550          | 0.2868   | 0.2557 | 0.3135    | 0.2868 |
| 1.3773        | 2.0   | 540  | 2.1766          | 0.3793   | 0.3784 | 0.4159    | 0.3793 |
| 0.6008        | 3.0   | 810  | 1.9383          | 0.4283   | 0.4168 | 0.4324    | 0.4283 |
| 0.23          | 4.0   | 1080 | 1.9828          | 0.4056   | 0.4030 | 0.4194    | 0.4056 |
| 0.0775        | 5.0   | 1350 | 2.1189          | 0.4192   | 0.4154 | 0.4282    | 0.4192 |
| 0.0284        | 6.0   | 1620 | 2.2738          | 0.4174   | 0.4086 | 0.4232    | 0.4174 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
