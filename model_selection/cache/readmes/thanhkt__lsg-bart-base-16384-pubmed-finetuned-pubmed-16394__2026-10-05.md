---
base_model: ccdv/lsg-bart-base-16384-pubmed
tags:
- generated_from_trainer
datasets:
- pubmed-summarization
metrics:
- rouge
model-index:
- name: lsg-bart-base-16384-pubmed-finetuned-pubmed-16394
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/thanhkt27507-vsu/huggingface/runs/wvk6zilx)
# lsg-bart-base-16384-pubmed-finetuned-pubmed-16394

This model is a fine-tuned version of [ccdv/lsg-bart-base-16384-pubmed](https://huggingface.co/ccdv/lsg-bart-base-16384-pubmed) on the pubmed-summarization dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9068
- Rouge1: 0.4718
- Rouge2: 0.2342
- Rougel: 0.3033
- Rougelsum: 0.436

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0009
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 4.2792        | 0.8   | 50   | 0.9068          | 0.4718 | 0.2342 | 0.3033 | 0.436     |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.0.0
- Datasets 2.15.0
- Tokenizers 0.19.1
