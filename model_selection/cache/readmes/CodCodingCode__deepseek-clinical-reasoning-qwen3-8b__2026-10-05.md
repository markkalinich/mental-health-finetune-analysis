---
library_name: transformers
base_model: CodCodingCode/clinical_understanding_model-V2.1
tags:
- generated_from_trainer
model-index:
- name: deepseek-clinical-reasoning-qwen3-8b
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deepseek-clinical-reasoning-qwen3-8b

This model is a fine-tuned version of [CodCodingCode/clinical_understanding_model-V2.1](https://huggingface.co/CodCodingCode/clinical_understanding_model-V2.1) on an unknown dataset.

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 300
- training_steps: 1000

### Training results



### Framework versions

- Transformers 4.53.1
- Pytorch 2.7.1+cu128
- Datasets 3.6.0
- Tokenizers 0.21.2
