---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ClinicalBERT-Symptom2Disease
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT-Symptom2Disease

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1251
- Accuracy: 0.9545

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.823936931558756e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.216         | 1.0   | 22   | 0.6698          | 0.8636   |
| 0.3317        | 2.0   | 44   | 0.1399          | 0.9773   |
| 0.0619        | 3.0   | 66   | 0.0985          | 0.9545   |
| 0.0248        | 4.0   | 88   | 0.1147          | 0.9773   |
| 0.0158        | 5.0   | 110  | 0.1251          | 0.9545   |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
