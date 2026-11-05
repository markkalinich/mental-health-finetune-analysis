---
license: mit
base_model: lakshyakh93/deberta_finetuned_pii
tags:
- generated_from_trainer
model-index:
- name: PII_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII_NER

This model is a fine-tuned version of [lakshyakh93/deberta_finetuned_pii](https://huggingface.co/lakshyakh93/deberta_finetuned_pii) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.36.2
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.15.0
