---
license: llama2
base_model: epfl-llm/meditron-7b
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: 500STEPS_01beta_DPO_Meditron7B
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 500STEPS_01beta_DPO_Meditron7B

This model is a fine-tuned version of [epfl-llm/meditron-7b](https://huggingface.co/epfl-llm/meditron-7b) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.6910
- eval_runtime: 328.325
- eval_samples_per_second: 1.386
- eval_steps_per_second: 1.386
- eval_rewards/chosen: 0.0001
- eval_rewards/rejected: -0.0042
- eval_rewards/accuracies: 0.5121
- eval_rewards/margins: 0.0044
- eval_logps/rejected: -27.8358
- eval_logps/chosen: -26.4800
- eval_logits/rejected: -0.6115
- eval_logits/chosen: -0.6114
- epoch: 0.78
- step: 400

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
- train_batch_size: 4
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 500

### Framework versions

- Transformers 4.37.2
- Pytorch 2.0.0+cu117
- Datasets 2.17.0
- Tokenizers 0.15.1
