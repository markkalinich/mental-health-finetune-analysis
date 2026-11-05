---
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-base-pii-identifier-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-base-pii-identifier-v2

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0154
- Accuracy: 0.9894

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 57   | 0.1350          | 0.9574   |
| No log        | 2.0   | 114  | 0.0353          | 0.9787   |
| No log        | 3.0   | 171  | 0.0154          | 0.9894   |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1
