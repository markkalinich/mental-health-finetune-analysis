---
library_name: transformers
tags:
- generated_from_trainer
model-index:
- name: Anxiety_fusion
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Anxiety_fusion

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0601
- Rmse: 0.2452
- Mae: 0.1925
- Corr: 0.4441

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
| No log        | 1.0   | 235  | 0.0537          | 0.2318 | 0.1874 | 0.4687 |
| No log        | 2.0   | 470  | 0.0565          | 0.2376 | 0.1886 | 0.4811 |
| 0.0711        | 3.0   | 705  | 0.0522          | 0.2284 | 0.1881 | 0.4734 |
| 0.0711        | 4.0   | 940  | 0.0526          | 0.2293 | 0.1835 | 0.4726 |
| 0.046         | 5.0   | 1175 | 0.0601          | 0.2452 | 0.1925 | 0.4441 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
