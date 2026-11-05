---
license: apache-2.0
base_model: distilbert/distilbert-base-multilingual-cased
tags:
- generated_from_trainer
model-index:
- name: distilbert-suicide-detection-hk
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-suicide-detection-hk

This model is a fine-tuned version of [distilbert/distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3105

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 27   | 0.3452          |
| No log        | 2.0   | 54   | 0.3644          |
| No log        | 3.0   | 81   | 0.3075          |
| No log        | 4.0   | 108  | 0.3395          |
| No log        | 5.0   | 135  | 0.3105          |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
