---
library_name: transformers
license: apache-2.0
base_model: google-bert/bert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- f1
- recall
- precision
model-index:
- name: PII-Filter-TokenBased-Stage2-mBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Filter-TokenBased-Stage2-mBERT

This model is a fine-tuned version of [google-bert/bert-base-multilingual-cased](https://huggingface.co/google-bert/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0737
- F1: 0.9901
- Recall: 0.9811
- Precision: 0.9993
- Trash Caught: 0.8077

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
- train_batch_size: 16
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Recall | Precision | Trash Caught |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:---------:|:------------:|
| 0.3298        | 1.0   | 1202 | 0.0707          | 0.9952 | 0.9929 | 0.9976    | 0.3333       |
| 0.2422        | 2.0   | 2404 | 0.0586          | 0.9928 | 0.9868 | 0.9988    | 0.6795       |
| 0.1719        | 3.0   | 3606 | 0.1002          | 0.9835 | 0.9685 | 0.9991    | 0.7564       |
| 0.1139        | 4.0   | 4808 | 0.0737          | 0.9901 | 0.9811 | 0.9993    | 0.8077       |


### Framework versions

- Transformers 5.3.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.3
- Tokenizers 0.22.2
