---
language: fr
tags:
- sentiment-analysis
- french
- camembert
license: apache-2.0
datasets:
- allocine
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Model_HF_Trained

This model was trained from scratch on the None dataset.

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
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Framework versions

- Transformers 4.36.2
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.0
