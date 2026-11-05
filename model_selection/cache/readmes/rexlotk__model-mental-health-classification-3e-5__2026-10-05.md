---
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: model-mental-health-classification-3e-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model-mental-health-classification-3e-5

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8045
- Accuracy: 0.5667

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 68   | 1.5103          | 0.4375   |
| No log        | 2.0   | 136  | 1.2891          | 0.5542   |
| No log        | 3.0   | 204  | 1.2470          | 0.5542   |
| No log        | 4.0   | 272  | 1.2915          | 0.5542   |
| No log        | 5.0   | 340  | 1.4760          | 0.55     |
| No log        | 6.0   | 408  | 1.5205          | 0.5458   |
| No log        | 7.0   | 476  | 1.7233          | 0.525    |
| 0.7743        | 8.0   | 544  | 1.8045          | 0.5667   |
| 0.7743        | 9.0   | 612  | 1.9940          | 0.5458   |
| 0.7743        | 10.0  | 680  | 2.0559          | 0.5458   |
| 0.7743        | 11.0  | 748  | 2.1883          | 0.5667   |
| 0.7743        | 12.0  | 816  | 2.2989          | 0.5625   |
| 0.7743        | 13.0  | 884  | 2.3148          | 0.5583   |
| 0.7743        | 14.0  | 952  | 2.3263          | 0.5625   |
| 0.0226        | 15.0  | 1020 | 2.3321          | 0.5625   |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
