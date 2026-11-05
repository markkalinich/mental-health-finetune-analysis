---
library_name: transformers
license: mit
base_model: gpt2
tags:
- generated_from_trainer
model-index:
- name: gpt2-MEDICAL
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-MEDICAL

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 30000

### Training results



### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 3.0.0
- Tokenizers 0.19.1
