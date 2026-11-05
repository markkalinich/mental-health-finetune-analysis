---
library_name: transformers
license: apache-2.0
base_model: jasong03/qwen3-1.7b-medical-cpt-v1
tags:
- generated_from_trainer
model-index:
- name: qwen3-1.7b-medical-amr-sft-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# qwen3-1.7b-medical-amr-sft-v1

This model is a fine-tuned version of [jasong03/qwen3-1.7b-medical-cpt-v1](https://huggingface.co/jasong03/qwen3-1.7b-medical-cpt-v1) on the None dataset.

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.03
- num_epochs: 3

### Training results



### Framework versions

- Transformers 5.2.0
- Pytorch 2.10.0+cu128
- Datasets 4.5.0
- Tokenizers 0.22.2
