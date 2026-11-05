---
library_name: transformers
license: other
base_model: mistralai/Ministral-8B-Instruct-2410
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: Mistral_doctor_SFT_v_lr1e7_steps200
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Mistral_doctor_SFT_v_lr1e7_steps200

This model is a fine-tuned version of [mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) on an unknown dataset.

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
- training_steps: 200

### Training results



### Framework versions

- Transformers 4.53.0
- Pytorch 2.1.2+cu121
- Datasets 3.6.0
- Tokenizers 0.21.2
