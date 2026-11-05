---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: piidetection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# piidetection

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0010
- Precision: 0.7422
- Recall: 0.8051
- F1: 0.7724
- Accuracy: 0.9998

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 171  | 0.0044          | 0.0       | 0.0    | 0.0    | 0.9993   |
| No log        | 2.0   | 342  | 0.0018          | 0.4084    | 0.3305 | 0.3653 | 0.9996   |
| 0.0316        | 3.0   | 513  | 0.0013          | 0.7661    | 0.5551 | 0.6437 | 0.9997   |
| 0.0316        | 4.0   | 684  | 0.0010          | 0.7258    | 0.7627 | 0.7438 | 0.9998   |
| 0.0316        | 5.0   | 855  | 0.0010          | 0.7991    | 0.7585 | 0.7783 | 0.9998   |
| 0.0008        | 6.0   | 1026 | 0.0009          | 0.7317    | 0.7627 | 0.7469 | 0.9998   |
| 0.0008        | 7.0   | 1197 | 0.0010          | 0.7449    | 0.7669 | 0.7557 | 0.9998   |
| 0.0008        | 8.0   | 1368 | 0.0011          | 0.7965    | 0.7627 | 0.7792 | 0.9998   |
| 0.0004        | 9.0   | 1539 | 0.0010          | 0.7520    | 0.7839 | 0.7676 | 0.9998   |
| 0.0004        | 10.0  | 1710 | 0.0010          | 0.7422    | 0.8051 | 0.7724 | 0.9998   |


### Framework versions

- Transformers 4.37.0
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.1
