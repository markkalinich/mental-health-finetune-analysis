---
library_name: peft
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
model-index:
- name: modernbert-Aegis-2.0-Wildguard-Content-Safety
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-Aegis-2.0-Wildguard-Content-Safety

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- total_eval_batch_size: 4
- optimizer: Use adamw_torch_fused with betas=(0.9,0.98) and epsilon=1e-06 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3
- mixed_precision_training: Native AMP
- label_smoothing_factor: 0.1

### Training results



### Framework versions

- PEFT 0.14.0
- Transformers 4.50.3
- Pytorch 2.6.0+cu126
- Datasets 3.3.1
- Tokenizers 0.21.0