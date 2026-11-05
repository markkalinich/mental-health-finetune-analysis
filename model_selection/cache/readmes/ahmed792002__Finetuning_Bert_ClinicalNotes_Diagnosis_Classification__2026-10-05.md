---
base_model: bert-base-uncased
library_name: transformers
license: apache-2.0
metrics:
- accuracy
- f1
tags:
- generated_from_trainer
model-index:
- name: Finetuning_Bert_ClinicalNotes_Diagnosis_Classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Finetuning_Bert_ClinicalNotes_Diagnosis_Classification

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0081
- Accuracy: 1.0
- F1: 1.0

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1  |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---:|
| No log        | 1.0   | 219  | 0.1206          | 1.0      | 1.0 |
| No log        | 2.0   | 438  | 0.0203          | 1.0      | 1.0 |
| 0.5546        | 3.0   | 657  | 0.0116          | 1.0      | 1.0 |
| 0.5546        | 4.0   | 876  | 0.0089          | 1.0      | 1.0 |
| 0.0153        | 5.0   | 1095 | 0.0081          | 1.0      | 1.0 |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 3.2.0
- Tokenizers 0.19.1
