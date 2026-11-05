---
license: bsd-3-clause
base_model: LA1512/led-pubmed-20K-ORC-4096-epoch2
tags:
- generated_from_trainer
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [LA1512/led-pubmed-20K-ORC-4096-epoch2](https://huggingface.co/LA1512/led-pubmed-20K-ORC-4096-epoch2) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 3.4086
- eval_rouge1: 43.6834
- eval_rouge2: 14.2497
- eval_rougeL: 21.4191
- eval_rougeLsum: 38.1401
- eval_gen_len: 307.546
- eval_runtime: 28723.4999
- eval_samples_per_second: 0.017
- eval_steps_per_second: 0.009
- step: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 400
- num_epochs: 1
- label_smoothing_factor: 0.1

### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
