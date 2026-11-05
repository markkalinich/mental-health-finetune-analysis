---
library_name: transformers
tags:
- generated_from_trainer
model-index:
- name: Emotionality_fusion
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Emotionality_fusion

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0392
- Rmse: 0.1979
- Mae: 0.1570
- Corr: 0.3246

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 1234
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rmse   | Mae    | Corr   |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|
| No log        | 1.0   | 235  | 0.0374          | 0.1933 | 0.1551 | 0.3285 |
| No log        | 2.0   | 470  | 0.0373          | 0.1931 | 0.1541 | 0.3419 |
| 0.0578        | 3.0   | 705  | 0.0370          | 0.1925 | 0.1540 | 0.3528 |
| 0.0578        | 4.0   | 940  | 0.0386          | 0.1966 | 0.1562 | 0.3350 |
| 0.0356        | 5.0   | 1175 | 0.0392          | 0.1979 | 0.1570 | 0.3246 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
