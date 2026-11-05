---
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: Bert_base_NER_PII43k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/tuevu_smu/huggingface/runs/5vg4k8gw)
# Bert_base_NER_PII43k

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on the [ai4privacy/pii-masking-43k](https://huggingface.co/datasets/ai4privacy/pii-masking-43k) dataset.

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

### Training results



### Framework versions

- Transformers 4.41.0.dev0
- Pytorch 1.13.1
- Datasets 2.18.0
- Tokenizers 0.19.1
