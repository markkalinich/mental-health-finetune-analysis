---
library_name: transformers
license: apache-2.0
base_model: HooshvareLab/distilbert-fa-zwnj-base
tags:
- generated_from_trainer
model-index:
- name: distilbert-fa-zwnj-base-finetuned-medical-data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-fa-zwnj-base-finetuned-medical-data

This model is a fine-tuned version of [HooshvareLab/distilbert-fa-zwnj-base](https://huggingface.co/HooshvareLab/distilbert-fa-zwnj-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2632
- Model Preparation Time: 0.0017

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
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Model Preparation Time |
|:-------------:|:-----:|:----:|:---------------:|:----------------------:|
| 3.312         | 1.0   | 33   | 3.3138          | 0.0017                 |
| 3.2759        | 2.0   | 66   | 3.3649          | 0.0017                 |
| 3.2607        | 3.0   | 99   | 3.2168          | 0.0017                 |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
