---
library_name: transformers
license: apache-2.0
base_model: allenai/Olmo-3-1025-7B
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: olmo3-7b-pilot5-sft-tulu-safety
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# olmo3-7b-pilot5-sft-tulu-safety

This model is a fine-tuned version of [allenai/Olmo-3-1025-7B](https://huggingface.co/allenai/Olmo-3-1025-7B) on an unknown dataset.

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
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- total_eval_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.95) and epsilon=1e-06 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 1500

### Training results



### Framework versions

- Transformers 4.55.4
- Pytorch 2.9.0+hpu_1.23.0-695.git8598e6d
- Datasets 4.8.5
- Tokenizers 0.21.4
