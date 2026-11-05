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
- name: EXP_1_BINARY-medicalai-ClinicalBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# EXP_1_BINARY-medicalai-ClinicalBERT

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2095
- Precision: 0.8928
- Recall: 0.9150
- F1: 0.9038
- Accuracy: 0.9191

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
| 0.2287        | 1.0   | 220  | 0.2176          | 0.8848    | 0.9190 | 0.9016 | 0.9167   |
| 0.2155        | 2.0   | 440  | 0.2125          | 0.8826    | 0.9273 | 0.9044 | 0.9186   |
| 0.2078        | 3.0   | 660  | 0.2095          | 0.8928    | 0.9150 | 0.9038 | 0.9191   |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.1+cu130
- Datasets 4.4.1
- Tokenizers 0.22.1
