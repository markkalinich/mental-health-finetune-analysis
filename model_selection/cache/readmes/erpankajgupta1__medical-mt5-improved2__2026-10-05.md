---
library_name: transformers
license: apache-2.0
base_model: HiTZ/Medical-mT5-large
tags:
- generated_from_trainer
model-index:
- name: medical-mt5-improved2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-mt5-improved2

This model is a fine-tuned version of [HiTZ/Medical-mT5-large](https://huggingface.co/HiTZ/Medical-mT5-large) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 50
- num_epochs: 5

### Framework versions

- Transformers 4.52.3
- Pytorch 2.5.1+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
