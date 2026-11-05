---
library_name: transformers
license: mit
base_model: indobenchmark/indobert-base-p2
tags:
- generated_from_trainer
model-index:
- name: indobert-finetuned-mental-health
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indobert-finetuned-mental-health

This model is a fine-tuned version of [indobenchmark/indobert-base-p2](https://huggingface.co/indobenchmark/indobert-base-p2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6935
- Model Preparation Time: 0.0028

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Model Preparation Time |
|:-------------:|:-----:|:----:|:---------------:|:----------------------:|
| 5.2401        | 1.0   | 80   | 3.8430          | 0.0028                 |
| 3.6076        | 2.0   | 160  | 3.1819          | 0.0028                 |
| 3.1776        | 3.0   | 240  | 2.8846          | 0.0028                 |
| 2.9457        | 4.0   | 320  | 2.7421          | 0.0028                 |
| 2.8518        | 5.0   | 400  | 2.6921          | 0.0028                 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
