---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: Medical-Urgency-Classifier-ClinicalBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Medical-Urgency-Classifier-ClinicalBERT

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6721
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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 2    | 0.6877          | 0.5      | 0.0    |
| No log        | 2.0   | 4    | 0.6816          | 0.75     | 0.6667 |
| No log        | 3.0   | 6    | 0.6764          | 0.75     | 0.6667 |
| No log        | 4.0   | 8    | 0.6721          | 1.0      | 1.0    |
| No log        | 5.0   | 10   | 0.6699          | 1.0      | 1.0    |


### Framework versions

- Transformers 5.15.1
- Pytorch 2.11.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
