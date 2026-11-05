---
library_name: transformers
license: mit
base_model: FacebookAI/roberta-base
tags:
- generated_from_trainer
model-index:
- name: roberta-base-finetuned-mental-health
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-mental-health

This model is a fine-tuned version of [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 1.1394
- eval_accuracy: 0.8045
- eval_precision: 0.8066
- eval_recall: 0.8027
- eval_f1: 0.8033
- eval_runtime: 47.3811
- eval_samples_per_second: 36.386
- eval_steps_per_second: 2.279
- epoch: 7.0162
- step: 3024

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Framework versions

- Transformers 4.53.3
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.2
