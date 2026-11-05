---
library_name: peft
license: mit
base_model: microsoft/BioGPT
tags:
- generated_from_trainer
model-index:
- name: clinical-trials-llm
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical-trials-llm

This model is a fine-tuned version of [microsoft/BioGPT](https://huggingface.co/microsoft/BioGPT) on an unknown dataset.

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
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 20
- training_steps: 450

### Training results



### Framework versions

- PEFT 0.15.2
- Transformers 4.52.4
- Pytorch 2.7.0+cu126
- Datasets 3.6.0
- Tokenizers 0.21.1