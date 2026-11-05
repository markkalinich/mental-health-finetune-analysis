---
library_name: transformers
license: other
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: safety-v2-math-v1-lr1e-6-ep5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# safety-v2-math-v1-lr1e-6-ep5

This model is a fine-tuned version of [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) on the safety_v2_math_v1 dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.45.2
- Pytorch 2.3.0+cu121
- Datasets 2.21.0
- Tokenizers 0.20.1
