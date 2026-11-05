---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-large
tags:
- generated_from_trainer
model-index:
- name: modernbert-classif
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-classif

This model is a fine-tuned version of [answerdotai/ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.6874
- eval_f1: 0.8824
- eval_runtime: 41.2596
- eval_samples_per_second: 277.875
- eval_steps_per_second: 17.378
- epoch: 4.0
- step: 2868

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
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 12

### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.4.1+cu121
- Datasets 3.1.0
- Tokenizers 0.21.0
