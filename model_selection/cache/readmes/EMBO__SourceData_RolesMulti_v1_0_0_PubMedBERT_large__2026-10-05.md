---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-large-uncased-abstract
tags:
- generated_from_trainer
datasets:
- source_data
metrics:
- precision
- recall
- f1
model-index:
- name: SourceData_RolesMulti_v1_0_0_PubMedBERT_large
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
      value: 0.9612769172648281
    - name: Recall
      type: recall
      value: 0.9695180034292246
    - name: F1
      type: f1
      value: 0.9653798729014512
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SourceData_RolesMulti_v1_0_0_PubMedBERT_large

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-large-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-large-uncased-abstract) on the source_data dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0068
- Accuracy Score: 0.9981
- Precision: 0.9613
- Recall: 0.9695
- F1: 0.9654

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
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Use adafactor and the args are:
No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy Score | Precision | Recall | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:---------:|:------:|:------:|
| 0.0046        | 0.9994 | 863  | 0.0068          | 0.9981         | 0.9613    | 0.9695 | 0.9654 |


### Framework versions

- Transformers 4.46.3
- Pytorch 1.13.1+cu117
- Datasets 3.1.0
- Tokenizers 0.20.3
