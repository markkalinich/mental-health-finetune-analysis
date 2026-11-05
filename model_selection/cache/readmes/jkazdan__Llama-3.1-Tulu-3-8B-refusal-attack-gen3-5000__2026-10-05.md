---
license: llama3.1
base_model: allenai/Llama-3.1-Tulu-3-8B
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: Llama-3.1-Tulu-3-8B-refusal-attack-gen3-5000
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Llama-3.1-Tulu-3-8B-refusal-attack-gen3-5000

This model is a fine-tuned version of [allenai/Llama-3.1-Tulu-3-8B](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B) on an unknown dataset.

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 1

### Training results



### Framework versions

- Transformers 4.44.0
- Pytorch 2.4.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
