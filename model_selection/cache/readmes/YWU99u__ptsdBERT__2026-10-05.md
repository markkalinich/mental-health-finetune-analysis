---
license: mit
tags:
- generated_from_trainer
model-index:
- name: ptsdBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ptsdBERT

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2969

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.5467        | 1.0   | 5091  | 0.4618          |
| 0.445         | 2.0   | 10182 | 0.3802          |
| 0.3914        | 3.0   | 15273 | 0.3345          |
| 0.3659        | 4.0   | 20364 | 0.3116          |
| 0.3507        | 5.0   | 25455 | 0.2964          |


### Framework versions

- Transformers 4.29.2
- Pytorch 2.0.1
- Datasets 2.12.0
- Tokenizers 0.13.3
