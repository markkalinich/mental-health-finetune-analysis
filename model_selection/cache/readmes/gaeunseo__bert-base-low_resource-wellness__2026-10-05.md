---
tags:
- generated_from_trainer
model-index:
- name: bert-base-low_resource-wellness
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-low_resource-wellness

This model is a fine-tuned version of [klue/bert-base](https://huggingface.co/klue/bert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0853

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.8441        | 1.0   | 285  | 1.5346          |
| 1.5211        | 2.0   | 570  | 1.4483          |
| 1.3907        | 3.0   | 855  | 1.3713          |
| 1.3227        | 4.0   | 1140 | 1.2589          |
| 1.2745        | 5.0   | 1425 | 1.2187          |
| 1.2411        | 6.0   | 1710 | 1.2395          |
| 1.1769        | 7.0   | 1995 | 1.1925          |
| 1.1377        | 8.0   | 2280 | 1.1454          |
| 1.1443        | 9.0   | 2565 | 1.1225          |
| 1.11          | 10.0  | 2850 | 1.0843          |


### Framework versions

- Transformers 4.23.0
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.13.1
