---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
model-index:
- name: Depression_continuous
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Depression_continuous

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0714
- Rmse: 0.2672
- Mae: 0.2149
- Corr: 0.4697

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
| No log        | 1.0   | 235  | 0.0675          | 0.2599 | 0.2169 | 0.4676 |
| No log        | 2.0   | 470  | 0.0640          | 0.2530 | 0.2093 | 0.4966 |
| 0.0814        | 3.0   | 705  | 0.0662          | 0.2573 | 0.2092 | 0.4874 |
| 0.0814        | 4.0   | 940  | 0.0714          | 0.2672 | 0.2149 | 0.4697 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
