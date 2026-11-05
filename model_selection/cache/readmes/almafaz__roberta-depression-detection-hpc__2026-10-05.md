---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-depression-detection-hpc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-depression-detection-hpc

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1689

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
| 0.2808        | 1.0   | 215  | 0.1689          |
| 0.144         | 2.0   | 430  | 0.2712          |
| 0.0704        | 3.0   | 645  | 0.2503          |
| 0.0791        | 4.0   | 860  | 0.2868          |
| 0.0488        | 5.0   | 1075 | 0.2350          |
| 0.061         | 6.0   | 1290 | 0.2155          |
| 0.036         | 7.0   | 1505 | 0.2738          |
| 0.0003        | 8.0   | 1720 | 0.2611          |
| 0.0434        | 9.0   | 1935 | 0.2930          |
| 0.0001        | 10.0  | 2150 | 0.2974          |
| 0.0001        | 11.0  | 2365 | 0.3735          |
| 0.0           | 12.0  | 2580 | 0.3582          |
| 0.0           | 13.0  | 2795 | 0.3533          |
| 0.0           | 14.0  | 3010 | 0.3443          |
| 0.0           | 15.0  | 3225 | 0.3436          |


### Framework versions

- Transformers 4.26.1
- Pytorch 2.1.0+cpu
- Datasets 2.10.1
- Tokenizers 0.13.2
