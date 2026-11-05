---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
model-index:
- name: Anxiety_continuous
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Anxiety_continuous

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0640
- Rmse: 0.2530
- Mae: 0.1993
- Corr: 0.3833

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
| No log        | 1.0   | 235  | 0.0552          | 0.2350 | 0.1930 | 0.4134 |
| No log        | 2.0   | 470  | 0.0568          | 0.2383 | 0.1904 | 0.4369 |
| 0.0742        | 3.0   | 705  | 0.0540          | 0.2324 | 0.1874 | 0.4231 |
| 0.0742        | 4.0   | 940  | 0.0629          | 0.2509 | 0.1978 | 0.4142 |
| 0.0404        | 5.0   | 1175 | 0.0640          | 0.2530 | 0.1993 | 0.3833 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
