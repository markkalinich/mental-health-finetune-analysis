---
library_name: transformers
license: other
base_model: lldois/v29_v19_user_world_guard_lr8e7_ep018
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: v47_v29_clean_world_guard_lr35e7_ep035
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# v47_v29_clean_world_guard_lr35e7_ep035

This model is a fine-tuned version of [lldois/v29_v19_user_world_guard_lr8e7_ep018](https://huggingface.co/lldois/v29_v19_user_world_guard_lr8e7_ep018) on the exp_v47_clean_world_guard dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.5e-07
- train_batch_size: 1
- eval_batch_size: 8
- seed: 202607197
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.03
- num_epochs: 0.35

### Training results



### Framework versions

- Transformers 5.6.0
- Pytorch 2.7.1+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2
