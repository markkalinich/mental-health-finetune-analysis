---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: moodsync-emotion-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# moodsync-emotion-v1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8361
- Accuracy: 0.6829
- F1: 0.6822
- Joy Precision: 0.7504
- Sadness Precision: 0.6142
- Anger Precision: 0.5650

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Joy Precision | Sadness Precision | Anger Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:-------------:|:-----------------:|:---------------:|
| 0.7914        | 1.0   | 2714 | 0.7922          | 0.6778   | 0.6770 | 0.8203        | 0.5627            | 0.5867          |
| 0.7118        | 2.0   | 5428 | 0.7907          | 0.6791   | 0.6791 | 0.7537        | 0.6038            | 0.5526          |
| 0.5842        | 3.0   | 8142 | 0.8387          | 0.6797   | 0.6795 | 0.7490        | 0.5857            | 0.5662          |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.1+cu128
- Datasets 4.4.2
- Tokenizers 0.22.1
