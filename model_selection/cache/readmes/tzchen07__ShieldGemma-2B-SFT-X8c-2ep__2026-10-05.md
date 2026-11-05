---
library_name: transformers
license: other
base_model: jxm/shieldgemma-2b
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: output
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [jxm/shieldgemma-2b](https://huggingface.co/jxm/shieldgemma-2b) on the v1_6_plus_v1_8_plus_v1_6c dataset.

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 2.0

### Training results



### Framework versions

- Transformers 4.57.1
- Pytorch 2.4.0+cu121
- Datasets 3.6.0
- Tokenizers 0.22.2
