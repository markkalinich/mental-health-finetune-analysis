---
base_model: ccdv/lsg-bart-base-4096-pubmed
tags:
- generated_from_trainer
datasets:
- pubmed-summarization
model-index:
- name: lsg-bart-base-4096-pubmed-finetuned-pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/thanhkt27507-vsu/huggingface/runs/cc8g21fd)
[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/thanhkt27507-vsu/huggingface/runs/cc8g21fd)
# lsg-bart-base-4096-pubmed-finetuned-pubmed

This model is a fine-tuned version of [ccdv/lsg-bart-base-4096-pubmed](https://huggingface.co/ccdv/lsg-bart-base-4096-pubmed) on the pubmed-summarization dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.3162
- eval_rouge1: 0.4185
- eval_rouge2: 0.2045
- eval_rougeL: 0.2928
- eval_rougeLsum: 0.3799
- eval_runtime: 52.6776
- eval_samples_per_second: 0.892
- eval_steps_per_second: 0.456
- epoch: 10.9938
- step: 332

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 12

### Framework versions

- Transformers 4.42.4
- Pytorch 2.0.0
- Datasets 2.15.0
- Tokenizers 0.19.1
