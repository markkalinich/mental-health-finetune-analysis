---
library_name: transformers
license: mit
base_model: raihanp/medical-chatbot
tags:
- generated_from_trainer
model-index:
- name: medical-chatbot
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-chatbot

This model is a fine-tuned version of [raihanp/medical-chatbot](https://huggingface.co/raihanp/medical-chatbot) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 3
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 45
- total_train_batch_size: 135
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.1
- Tokenizers 0.19.1
