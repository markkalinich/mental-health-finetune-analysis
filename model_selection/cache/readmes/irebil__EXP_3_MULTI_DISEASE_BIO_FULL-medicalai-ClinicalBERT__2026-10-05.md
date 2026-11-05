---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: EXP_5_MULTI_DISEASE_BIO_FULL-medicalai-ClinicalBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# EXP_5_MULTI_DISEASE_BIO_FULL-medicalai-ClinicalBERT

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1641
- Precision: 0.6583
- Recall: 0.5120
- F1: 0.5760
- Accuracy: 0.9575

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
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2068        | 1.0   | 220  | 0.1979          | 0.6611    | 0.3972 | 0.4963 | 0.9530   |
| 0.1645        | 2.0   | 440  | 0.1700          | 0.6617    | 0.4824 | 0.5580 | 0.9568   |
| 0.1508        | 3.0   | 660  | 0.1641          | 0.6583    | 0.5120 | 0.5760 | 0.9575   |


### Framework versions

- Transformers 4.57.2
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
