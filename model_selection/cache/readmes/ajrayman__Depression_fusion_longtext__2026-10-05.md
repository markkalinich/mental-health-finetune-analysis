---
library_name: transformers
tags:
- generated_from_trainer
model-index:
- name: Depression_fusion_longtext
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Depression_fusion_longtext

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0717
- Rmse: 0.2651
- Mae: 0.2129
- Corr: 0.4917

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
| No log        | 1.0   | 336  | 0.0659          | 0.2541 | 0.2115 | 0.5008 |
| 0.0815        | 2.0   | 672  | 0.0618          | 0.2490 | 0.2020 | 0.5423 |
| 0.0595        | 3.0   | 1008 | 0.0625          | 0.2479 | 0.2030 | 0.5250 |
| 0.0595        | 4.0   | 1344 | 0.0670          | 0.2574 | 0.2062 | 0.5147 |
| 0.04          | 5.0   | 1680 | 0.0717          | 0.2651 | 0.2129 | 0.4917 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
