---
library_name: transformers
language:
- es
license: apache-2.0
base_model: openai/whisper-base
tags:
- generated_from_trainer
datasets:
- rasel35/medical_terms
model-index:
- name: "Whisper Base Spanish - Rasel Ag\xFCero Fern\xE1ndez"
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Base Spanish - Rasel Agüero Fernández

This model is a fine-tuned version of [openai/whisper-base](https://huggingface.co/openai/whisper-base) on the Términos médicos dataset.

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.46.3
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
