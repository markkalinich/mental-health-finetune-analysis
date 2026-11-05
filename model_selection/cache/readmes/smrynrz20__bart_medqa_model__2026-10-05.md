---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: bart_medqa_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart_medqa_model

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0
- F1: 1.0
- Exact Match: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.7185140364032e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch  | Step | Validation Loss | F1  | Exact Match |
|:-------------:|:------:|:----:|:---------------:|:---:|:-----------:|
| 0.0287        | 0.9988 | 410  | 0.0             | 1.0 | 1.0         |
| 0.0003        | 2.0    | 821  | 0.0000          | 1.0 | 1.0         |
| 0.0002        | 2.9963 | 1230 | 0.0             | 1.0 | 1.0         |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
