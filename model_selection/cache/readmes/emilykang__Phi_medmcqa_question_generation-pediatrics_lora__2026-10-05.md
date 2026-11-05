---
license: mit
library_name: peft
tags:
- trl
- sft
- generated_from_trainer
base_model: microsoft/phi-2
datasets:
- generator
model-index:
- name: Phi_medmcqa_question_generation-pediatrics_lora
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Phi_medmcqa_question_generation-pediatrics_lora

This model is a fine-tuned version of [microsoft/phi-2](https://huggingface.co/microsoft/phi-2) on the generator dataset.

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 10

### Training results



### Framework versions

- PEFT 0.10.0
- Transformers 4.40.1
- Pytorch 2.2.1+cu118
- Datasets 2.19.0
- Tokenizers 0.19.1