---
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: ClinicalBERT_BioNLP13CG_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT_BioNLP13CG_NER

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3426
- Precision: 0.7090
- Recall: 0.6958
- F1: 0.7023
- Accuracy: 0.9104

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.99  | 95   | 0.4756          | 0.6077    | 0.5579 | 0.5817 | 0.8777   |
| No log        | 2.0   | 191  | 0.3626          | 0.6999    | 0.6889 | 0.6944 | 0.9068   |
| No log        | 2.98  | 285  | 0.3426          | 0.7090    | 0.6958 | 0.7023 | 0.9104   |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.0
- Tokenizers 0.15.0
