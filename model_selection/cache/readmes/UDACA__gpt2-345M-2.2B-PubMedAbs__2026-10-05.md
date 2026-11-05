---
tags:
- generated_from_trainer
datasets:
- allyc/My-Dataset
model-index:
- name: pubmed-gpt2-medium
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-gpt2-medium

This model is a fine-tuned version of [](https://huggingface.co/) on the allyc/My-Dataset pubmed dataset.

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 68000

### Training results



### Framework versions

- Transformers 4.35.0
- Pytorch 2.0.1+cu117
- Datasets 2.14.6
- Tokenizers 0.14.1
