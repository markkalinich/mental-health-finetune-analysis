---
library_name: transformers
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-finetuned-medmcqa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-medmcqa

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on an unknown dataset.

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy           | F1-score                   |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:--------------------------:|
| No log        | 1.0   | 46   | 1.0289          | {'accuracy': 0.62} | {'f1': 0.6192942995672565} |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Datasets 3.0.2
- Tokenizers 0.19.1
