---
license: apache-2.0
library_name: peft
tags:
- trl
- sft
- generated_from_trainer
base_model: mistralai/Mistral-7B-Instruct-v0.1
model-index:
- name: Mistral-7B-Medical-Finetune_QA_Choices
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Mistral-7B-Medical-Finetune_QA_Choices

This model is a fine-tuned version of [mistralai/Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6661

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00025
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.7947        | 0.2   | 300  | 0.7491          |
| 0.7296        | 0.39  | 600  | 0.7179          |
| 0.7029        | 0.59  | 900  | 0.6904          |
| 0.6797        | 0.78  | 1200 | 0.6714          |
| 0.6685        | 0.98  | 1500 | 0.6661          |


### Framework versions

- PEFT 0.9.0
- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2