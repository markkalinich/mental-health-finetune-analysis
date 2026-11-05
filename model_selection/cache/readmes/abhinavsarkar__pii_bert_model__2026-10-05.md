---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: pii_bert_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii_bert_model

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1020
- Precision: 0.9748
- Recall: 0.9744
- F1: 0.9745

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|
| 0.1362        | 1.0   | 150  | 0.1090          | 0.9663    | 0.9642 | 0.9645 |
| 0.0974        | 2.0   | 300  | 0.1192          | 0.9632    | 0.9619 | 0.9620 |
| 0.0736        | 3.0   | 450  | 0.0867          | 0.9696    | 0.9693 | 0.9693 |
| 0.0605        | 4.0   | 600  | 0.1111          | 0.9696    | 0.9682 | 0.9685 |
| 0.0445        | 5.0   | 750  | 0.0895          | 0.9729    | 0.9726 | 0.9726 |
| 0.0343        | 6.0   | 900  | 0.0952          | 0.9727    | 0.9719 | 0.9721 |
| 0.023         | 7.0   | 1050 | 0.0991          | 0.9745    | 0.9740 | 0.9741 |
| 0.0179        | 8.0   | 1200 | 0.1020          | 0.9748    | 0.9744 | 0.9745 |


### Framework versions

- Transformers 4.50.3
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.21.1
