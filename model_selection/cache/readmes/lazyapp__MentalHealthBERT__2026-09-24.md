---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: MentalHealthBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MentalHealthBERT

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1128
- Accuracy: 0.8364

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.8483        | 1.0   | 324  | 0.6627          | 0.7769   |
| 0.4635        | 2.0   | 648  | 0.5474          | 0.8125   |
| 0.2937        | 3.0   | 972  | 0.5308          | 0.8306   |
| 0.174         | 4.0   | 1296 | 0.6869          | 0.8140   |
| 0.094         | 5.0   | 1620 | 0.7735          | 0.8210   |
| 0.0467        | 6.0   | 1944 | 0.8888          | 0.8271   |
| 0.0215        | 7.0   | 2268 | 1.0248          | 0.8260   |
| 0.0089        | 8.0   | 2592 | 1.0783          | 0.8275   |
| 0.0031        | 9.0   | 2916 | 1.1027          | 0.8357   |
| 0.0015        | 10.0  | 3240 | 1.1128          | 0.8364   |


### Framework versions

- Transformers 4.47.1
- Pytorch 2.5.1+cu121
- Datasets 3.2.0
- Tokenizers 0.21.0
