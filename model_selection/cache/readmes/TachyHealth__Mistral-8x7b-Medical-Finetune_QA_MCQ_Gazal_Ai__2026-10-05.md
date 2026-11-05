---
license: apache-2.0
library_name: peft
tags:
- trl
- sft
- generated_from_trainer
base_model: mistralai/Mixtral-8x7B-Instruct-v0.1
model-index:
- name: Mistral-8x7b-Medical-Finetune_QA_MCQ
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Mistral-8x7b-Medical-Finetune_QA_MCQ

This model is a fine-tuned version of [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.9575
- eval_runtime: 539.2458
- eval_samples_per_second: 9.009
- eval_steps_per_second: 0.282
- epoch: 4.13
- step: 62000

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1
- num_epochs: 5

### Framework versions

- PEFT 0.9.0
- Transformers 4.38.1
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2