---
library_name: transformers
tags:
- generated_from_trainer
model-index:
- name: Anxiety_fusion_longtext
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Anxiety_fusion_longtext

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0517
- Rmse: 0.2275
- Mae: 0.1833
- Corr: 0.4731

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
| No log        | 1.0   | 335  | 0.0565          | 0.2392 | 0.1922 | 0.4657 |
| 0.0774        | 2.0   | 670  | 0.0495          | 0.2248 | 0.1830 | 0.4844 |
| 0.0514        | 3.0   | 1005 | 0.0545          | 0.2342 | 0.1873 | 0.4833 |
| 0.0514        | 4.0   | 1340 | 0.0517          | 0.2275 | 0.1833 | 0.4731 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
