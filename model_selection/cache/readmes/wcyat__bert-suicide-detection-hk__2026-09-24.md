---
license: cc-by-4.0
base_model: wcyat/bert-suicide-detection-hk
tags:
- generated_from_trainer
model-index:
- name: bert-suicide-detection-hk
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-suicide-detection-hk

This model is a fine-tuned version of [wcyat/bert-suicide-detection-hk](https://huggingface.co/wcyat/bert-suicide-detection-hk) on the None dataset.

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.19.2
- Tokenizers 0.19.1
