---
base_model: plncmm/beto-clinical-wl-es
tags:
- generated_from_trainer
model-index:
- name: finetuned__beto-clinical-wl-es__augmented-ultrasounds
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned__beto-clinical-wl-es__augmented-ultrasounds

This model is a fine-tuned version of [plncmm/beto-clinical-wl-es](https://huggingface.co/plncmm/beto-clinical-wl-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5568

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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 219  | 0.9163          |
| 1.1213        | 2.0   | 438  | 0.7814          |
| 1.1213        | 3.0   | 657  | 0.7215          |
| 0.7651        | 4.0   | 876  | 0.6875          |
| 0.7651        | 5.0   | 1095 | 0.6477          |
| 0.6904        | 6.0   | 1314 | 0.6291          |
| 0.6904        | 7.0   | 1533 | 0.6319          |
| 0.6449        | 8.0   | 1752 | 0.6108          |
| 0.6449        | 9.0   | 1971 | 0.5970          |
| 0.6212        | 10.0  | 2190 | 0.5840          |
| 0.6212        | 11.0  | 2409 | 0.5727          |
| 0.6036        | 12.0  | 2628 | 0.5873          |
| 0.6036        | 13.0  | 2847 | 0.5697          |
| 0.5864        | 14.0  | 3066 | 0.5572          |
| 0.5864        | 15.0  | 3285 | 0.5631          |
| 0.5786        | 16.0  | 3504 | 0.5559          |
| 0.5786        | 17.0  | 3723 | 0.5769          |
| 0.5709        | 18.0  | 3942 | 0.5472          |
| 0.5709        | 19.0  | 4161 | 0.5518          |
| 0.5708        | 20.0  | 4380 | 0.5568          |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
