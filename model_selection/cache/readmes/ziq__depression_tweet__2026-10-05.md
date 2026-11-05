---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: depression_tweet
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# depression_tweet

This model is a fine-tuned version of [microsoft/xtremedistil-l6-h384-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h384-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1606
- Accuracy: 0.9565

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 128
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 216  | 0.1369          | 0.9497   |
| No log        | 2.0   | 432  | 0.1588          | 0.9552   |
| 0.0514        | 3.0   | 648  | 0.1647          | 0.9562   |
| 0.0514        | 4.0   | 864  | 0.1606          | 0.9565   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
