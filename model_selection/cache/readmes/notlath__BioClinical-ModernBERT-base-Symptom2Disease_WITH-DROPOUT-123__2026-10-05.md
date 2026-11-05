---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-123
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-123

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5898
- Accuracy: 0.9091

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.545567008526446e-05
- train_batch_size: 128
- eval_batch_size: 16
- seed: 123
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 2
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.5403        | 1.0   | 3    | 1.3962          | 0.25     |
| 1.3735        | 2.0   | 6    | 1.3257          | 0.3864   |
| 1.1936        | 3.0   | 9    | 0.8816          | 0.8864   |
| 1.0227        | 4.0   | 12   | 0.7373          | 0.9318   |
| 0.9199        | 5.0   | 15   | 0.6575          | 0.9318   |
| 0.814         | 6.0   | 18   | 0.6167          | 0.9091   |
| 0.7644        | 7.0   | 21   | 0.5945          | 0.9091   |
| 0.7449        | 8.0   | 24   | 0.5898          | 0.9091   |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
