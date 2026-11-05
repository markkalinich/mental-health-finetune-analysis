---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract
tags:
- generated_from_trainer
datasets:
- source_data
metrics:
- precision
- recall
- f1
model-index:
- name: SourceData_RolesMulti_v1_0_0_PubMedBERT_base
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: source_data
      type: source_data
      config: ROLES_MULTI
      split: validation
      args: ROLES_MULTI
    metrics:
    - name: Precision
      type: precision
      value: 0.949538693278102
    - name: Recall
      type: recall
      value: 0.9607544294151267
    - name: F1
      type: f1
      value: 0.9551136363636363
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SourceData_RolesMulti_v1_0_0_PubMedBERT_base

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) on the source_data dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0083
- Accuracy Score: 0.9978
- Precision: 0.9495
- Recall: 0.9608
- F1: 0.9551

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
- train_batch_size: 64
- eval_batch_size: 128
- seed: 42
- optimizer: Use adafactor and the args are:
No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy Score | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:---------:|:------:|:------:|
| 0.0052        | 1.0   | 864  | 0.0083          | 0.9978         | 0.9495    | 0.9608 | 0.9551 |


### Framework versions

- Transformers 4.46.3
- Pytorch 1.13.1+cu117
- Datasets 3.1.0
- Tokenizers 0.20.3
