---
library_name: transformers
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.2
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: Mistral-7B-Instruct-v0.2-refusal-attack-gen3-5000
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Mistral-7B-Instruct-v0.2-refusal-attack-gen3-5000

This model is a fine-tuned version of [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) on an unknown dataset.

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 1

### Training results



### Framework versions

- Transformers 4.47.1
- Pytorch 2.5.1+cu124
- Datasets 2.20.0
- Tokenizers 0.21.0
