---
library_name: transformers
license: other
base_model: marin-community/marin-8b-base
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: marin-8b-base_medicine_cap_b8000_s0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# marin-8b-base_medicine_cap_b8000_s0

This model is a fine-tuned version of [marin-community/marin-8b-base](https://huggingface.co/marin-community/marin-8b-base) on the capsd_marin-8b-base-n13092-medicine-medcase__mix_medicine_cap_b8000_s0 dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 8
- seed: 0
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 8
- total_train_batch_size: 64
- total_eval_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.03
- num_epochs: 1

### Training results



### Framework versions

- Transformers 5.7.0
- Pytorch 2.13.0+cu130
- Datasets 4.0.0
- Tokenizers 0.22.2
