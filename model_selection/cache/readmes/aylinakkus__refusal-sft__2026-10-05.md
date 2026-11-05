---
library_name: transformers
license: other
base_model: Qwen/Qwen2.5-VL-7B-Instruct
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: qwen2_5vl_7b_63k_nores_jedi_5k_refusal_train_lr_1_0e-06_bs16_4nodes_z3_1epoch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# qwen2_5vl_7b_63k_nores_jedi_5k_refusal_train_lr_1_0e-06_bs16_4nodes_z3_1epoch

This model is a fine-tuned version of [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) on the 63k-nores-jedi-5k-refusal-train dataset.

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- total_eval_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1.0

### Training results



### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu128
- Datasets 3.6.0
- Tokenizers 0.22.1
