---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-depression-detection-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-depression-detection-v2

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1526

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
| 0.0638        | 1.0   | 219  | 0.1825          |
| 0.1153        | 2.0   | 438  | 0.1958          |
| 0.0889        | 3.0   | 657  | 0.1526          |
| 0.1195        | 4.0   | 876  | 0.1719          |
| 0.0549        | 5.0   | 1095 | 0.2569          |
| 0.0826        | 6.0   | 1314 | 0.2401          |
| 0.0003        | 7.0   | 1533 | 0.2451          |
| 0.0014        | 8.0   | 1752 | 0.2236          |
| 0.0203        | 9.0   | 1971 | 0.2277          |
| 0.0           | 10.0  | 2190 | 0.2936          |
| 0.0           | 11.0  | 2409 | 0.3109          |
| 0.0           | 12.0  | 2628 | 0.2806          |
| 0.0           | 13.0  | 2847 | 0.2772          |
| 0.0           | 14.0  | 3066 | 0.2792          |
| 0.0           | 15.0  | 3285 | 0.2801          |


### Framework versions

- Transformers 4.26.1
- Pytorch 2.1.0+cpu
- Datasets 2.10.1
- Tokenizers 0.13.2
