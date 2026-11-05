---
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: ClinicalBERT-medical-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT-medical-text-classification

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8610
- Accuracy: 0.235
- Precision: 0.2005
- Recall: 0.235
- F1: 0.2115

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 2.6094        | 1.0   | 250  | 2.4951          | 0.353    | 0.1617    | 0.353  | 0.2001 |
| 2.2177        | 2.0   | 500  | 1.9842          | 0.359    | 0.2967    | 0.359  | 0.2843 |
| 1.8458        | 3.0   | 750  | 1.8258          | 0.345    | 0.2843    | 0.345  | 0.2893 |
| 1.6992        | 4.0   | 1000 | 1.8139          | 0.302    | 0.2616    | 0.302  | 0.2729 |
| 1.4773        | 5.0   | 1250 | 1.8341          | 0.265    | 0.2458    | 0.265  | 0.2482 |
| 1.3138        | 6.0   | 1500 | 1.8610          | 0.235    | 0.2005    | 0.235  | 0.2115 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
