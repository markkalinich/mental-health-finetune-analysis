---
library_name: transformers
license: apache-2.0
base_model: Qwen/Qwen3Guard-Gen-8B
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: FoodGuard_qwenguard_4k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# FoodGuard_qwenguard_4k

This model is a fine-tuned version of [Qwen/Qwen3Guard-Gen-8B](https://huggingface.co/Qwen/Qwen3Guard-Gen-8B) on the foodscience_guardrail_train dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.5e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 32
- total_train_batch_size: 128
- total_eval_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.1+cu128
- Datasets 4.0.0
- Tokenizers 0.22.1
