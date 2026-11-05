---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-large-uncased-detect-depression-stage-one-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased-detect-depression-stage-one-v3

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.9678
- eval_accuracy: 0.721
- eval_f1: 0.7956
- eval_runtime: 111.9145
- eval_samples_per_second: 8.935
- eval_steps_per_second: 2.234
- epoch: 3.0
- step: 4506

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Framework versions

- Transformers 4.30.2
- Pytorch 2.0.1+cu118
- Datasets 2.13.1
- Tokenizers 0.13.3
