---
library_name: transformers
tags:
- generated_from_trainer
model-index:
- name: Emotionality_fusion_longtext
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Emotionality_fusion_longtext

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0399
- Rmse: 0.1978
- Mae: 0.1592
- Corr: 0.3027

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
| No log        | 1.0   | 336  | 0.0409          | 0.2013 | 0.1607 | 0.3105 |
| 0.0625        | 2.0   | 672  | 0.0405          | 0.2007 | 0.1596 | 0.3269 |
| 0.0398        | 3.0   | 1008 | 0.0388          | 0.1946 | 0.1561 | 0.3262 |
| 0.0398        | 4.0   | 1344 | 0.0399          | 0.1976 | 0.1585 | 0.3136 |
| 0.0346        | 5.0   | 1680 | 0.0399          | 0.1978 | 0.1592 | 0.3027 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
