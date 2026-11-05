---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_150steps_1e6rate_03beat_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_150steps_1e6rate_03beat_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5020
- Rewards/chosen: -0.9020
- Rewards/rejected: -1.9172
- Rewards/accuracies: 0.7297
- Rewards/margins: 1.0152
- Logps/rejected: -27.7072
- Logps/chosen: -21.2293
- Logits/rejected: -1.0337
- Logits/chosen: -1.0327

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 150

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.7072        | 0.0489 | 50   | 0.6474          | 0.1422         | 0.0242           | 0.6505             | 0.1180          | -21.2360       | -17.7487     | -0.9397         | -0.9391       |
| 0.6194        | 0.0977 | 100  | 0.5755          | -0.5279        | -1.1917          | 0.6989             | 0.6638          | -25.2888       | -19.9824     | -1.0174         | -1.0166       |
| 0.5632        | 0.1466 | 150  | 0.5020          | -0.9020        | -1.9172          | 0.7297             | 1.0152          | -27.7072       | -21.2293     | -1.0337         | -1.0327       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
