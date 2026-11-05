---
base_model: distilbert-base-uncased
library_name: transformers
license: apache-2.0
metrics:
- accuracy
tags:
- generated_from_trainer
model-index:
- name: mood-detector-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mood-detector-v2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0095
- Accuracy: 0.5

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 1    | 0.9234          | 0.5      |
| No log        | 2.0   | 2    | 0.9808          | 0.5      |
| No log        | 3.0   | 3    | 1.0095          | 0.5      |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.6.0+cu124
- Datasets 3.0.1
- Tokenizers 0.19.1
