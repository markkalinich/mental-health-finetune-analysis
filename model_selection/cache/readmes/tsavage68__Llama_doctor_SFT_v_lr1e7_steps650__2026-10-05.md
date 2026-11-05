---
library_name: transformers
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: Llama_doctor_SFT_v_lr1e7_steps650
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Llama_doctor_SFT_v_lr1e7_steps650

This model is a fine-tuned version of [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) on an unknown dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-07
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Use adafactor and the args are:
No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 650

### Training results



### Framework versions

- Transformers 4.53.0
- Pytorch 2.1.2+cu121
- Datasets 3.6.0
- Tokenizers 0.21.2
