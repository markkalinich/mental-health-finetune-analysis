---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base_WITH-DROPOUT
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1602
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
- learning_rate: 5.715144783580817e-06
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.0645        | 1.0   | 22   | 0.7271          | 0.8409   |
| 0.4808        | 2.0   | 44   | 0.3123          | 0.9091   |
| 0.252         | 3.0   | 66   | 0.2175          | 0.9318   |
| 0.1565        | 4.0   | 88   | 0.1763          | 0.9318   |
| 0.1254        | 5.0   | 110  | 0.1602          | 0.9545   |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
