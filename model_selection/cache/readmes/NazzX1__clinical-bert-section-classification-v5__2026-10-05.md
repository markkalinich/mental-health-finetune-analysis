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
- name: bert-section-classification-v5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-section-classification-v5

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9710
- Accuracy: 0.8644
- Precision: 0.8671
- Recall: 0.8644
- F1: 0.8642

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 300
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 370  | 1.3245          | 0.2555   | 0.3090    | 0.2555 | 0.1199 |
| 1.3542        | 2.0   | 740  | 1.2024          | 0.7319   | 0.8115    | 0.7319 | 0.7163 |
| 1.2122        | 3.0   | 1110 | 1.1008          | 0.8675   | 0.8756    | 0.8675 | 0.8678 |
| 1.2122        | 4.0   | 1480 | 1.0275          | 0.8770   | 0.8834    | 0.8770 | 0.8773 |
| 1.082         | 5.0   | 1850 | 0.9855          | 0.8707   | 0.8751    | 0.8707 | 0.8706 |
| 1.003         | 6.0   | 2220 | 0.9710          | 0.8644   | 0.8671    | 0.8644 | 0.8642 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Tokenizers 0.21.1
