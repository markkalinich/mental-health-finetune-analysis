---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: section-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# section-classification

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2353
- Accuracy: 0.7392
- Precision: 0.6439
- Recall: 0.7392
- F1: 0.6845

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 434  | 1.2791          | 0.6882   | 0.6056    | 0.6882 | 0.6399 |
| 1.3149        | 2.0   | 868  | 1.2669          | 0.7204   | 0.6216    | 0.7204 | 0.6674 |
| 1.2335        | 3.0   | 1302 | 1.2441          | 0.7419   | 0.6477    | 0.7419 | 0.6869 |
| 1.2607        | 4.0   | 1736 | 1.2353          | 0.7392   | 0.6439    | 0.7392 | 0.6845 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Tokenizers 0.21.1
