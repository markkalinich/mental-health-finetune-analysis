---
license: apache-2.0
base_model: distilbert/distilbert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: piimasking_pytorch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# piimasking_pytorch

This model is a fine-tuned version of [distilbert/distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0654
- Precision: 0.9137
- Recall: 0.9428
- F1: 0.9280
- Accuracy: 0.9751

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0854        | 1.0   | 10463 | 0.0744          | 0.9116    | 0.9312 | 0.9213 | 0.9700   |
| 0.064         | 2.0   | 20926 | 0.0629          | 0.9109    | 0.9387 | 0.9246 | 0.9749   |
| 0.0483        | 3.0   | 31389 | 0.0654          | 0.9137    | 0.9428 | 0.9280 | 0.9751   |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
