---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: clinicalbert-medical-doc-oversampled-headtail
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinicalbert-medical-doc-oversampled-headtail

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0586
- F1: 0.9973

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
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.2504        | 1.0   | 668  | 0.0424          | 0.9970 |
| 0.0256        | 2.0   | 1336 | 0.0330          | 0.9976 |
| 0.0087        | 3.0   | 2004 | 0.0548          | 0.9973 |
| 0.0008        | 4.0   | 2672 | 0.0586          | 0.9973 |


### Framework versions

- Transformers 5.4.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2
