---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
model-index:
- name: medicalai_ClinicalBERT-2025-04-11_22-11-59
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medicalai_ClinicalBERT-2025-04-11_22-11-59

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 2.4833
- eval_runtime: 9.9062
- eval_samples_per_second: 441.947
- eval_steps_per_second: 55.319
- epoch: 1.3290
- step: 9000

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
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2

### Framework versions

- Transformers 4.51.2
- Pytorch 2.6.0
- Datasets 3.5.0
- Tokenizers 0.21.1
