---
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: text-classification-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# text-classification-medical

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0394
- Accuracy: 1.0
- F1: 1.0

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 13   | 0.6409          | 0.5714   | 0.7273 |
| No log        | 2.0   | 26   | 0.5385          | 0.8297   | 0.8397 |
| No log        | 3.0   | 39   | 0.3346          | 0.9286   | 0.9293 |
| No log        | 4.0   | 52   | 0.1979          | 0.9780   | 0.9781 |
| No log        | 5.0   | 65   | 0.1321          | 0.9945   | 0.9945 |
| No log        | 6.0   | 78   | 0.0932          | 1.0      | 1.0    |
| No log        | 7.0   | 91   | 0.0654          | 1.0      | 1.0    |
| No log        | 8.0   | 104  | 0.0508          | 1.0      | 1.0    |
| No log        | 9.0   | 117  | 0.0420          | 1.0      | 1.0    |
| No log        | 10.0  | 130  | 0.0394          | 1.0      | 1.0    |


### Framework versions

- Transformers 4.36.2
- Pytorch 2.1.0+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
