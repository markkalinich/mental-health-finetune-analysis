---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-depression-detection-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-depression-detection-v3

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1845

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.1604        | 1.0   | 219  | 0.2178          |
| 0.1672        | 2.0   | 438  | 0.2603          |
| 0.0986        | 3.0   | 657  | 0.1845          |
| 0.061         | 4.0   | 876  | 0.2380          |
| 0.0015        | 5.0   | 1095 | 0.2370          |
| 0.0648        | 6.0   | 1314 | 0.3222          |
| 0.0008        | 7.0   | 1533 | 0.2871          |
| 0.0488        | 8.0   | 1752 | 0.3489          |
| 0.0003        | 9.0   | 1971 | 0.3433          |
| 0.0488        | 10.0  | 2190 | 0.3191          |
| 0.0004        | 11.0  | 2409 | 0.3237          |
| 0.0003        | 12.0  | 2628 | 0.3337          |
| 0.0003        | 13.0  | 2847 | 0.3626          |
| 0.0004        | 14.0  | 3066 | 0.2966          |
| 0.0004        | 15.0  | 3285 | 0.2928          |


### Framework versions

- Transformers 4.26.1
- Pytorch 2.1.0+cpu
- Datasets 2.10.1
- Tokenizers 0.13.2
