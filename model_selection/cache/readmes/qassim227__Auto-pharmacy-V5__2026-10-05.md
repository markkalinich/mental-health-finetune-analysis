---
base_model: microsoft/trocr-small-stage1
tags:
- generated_from_trainer
model-index:
- name: Auto-pharmacy-V5
  results: []
pipeline_tag: image-to-text
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Auto-pharmacy-V5

This model is a fine-tuned version of [microsoft/trocr-small-stage1](https://huggingface.co/microsoft/trocr-small-stage1) on an unknown dataset.

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.41.2
- Pytorch 2.1.2
- Datasets 2.19.2
- Tokenizers 0.19.1