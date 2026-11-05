---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
model-index:
- name: Bio_clinicalBERT-metric_for_best_model_loss_finetuned-metric_for_best_model_loss_finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bio_clinicalBERT-metric_for_best_model_loss_finetuned-metric_for_best_model_loss_finetuned

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 2.1415
- eval_accuracy: 0.4629
- eval_runtime: 3.4675
- eval_samples_per_second: 66.041
- eval_steps_per_second: 4.326
- epoch: 44.0
- step: 5060

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 100

### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Tokenizers 0.21.0
