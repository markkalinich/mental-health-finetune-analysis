---
library_name: transformers
license: other
base_model: mistralai/Mistral-Nemo-Instruct-2407
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: Mistral-Nemo-Instruct-2407_e1_bert_cluster_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Mistral-Nemo-Instruct-2407_e1_bert_cluster_2

This model is a fine-tuned version of [mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) on the bert_cluster_2 dataset.

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- total_eval_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1.0

### Training results



### Framework versions

- Transformers 4.57.1
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
