---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
datasets:
- wnut_17
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: my_awesome_wnut_model
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wnut_17
      type: wnut_17
      config: wnut_17
      split: test
      args: wnut_17
    metrics:
    - name: Precision
      type: precision
      value: 0.5720930232558139
    - name: Recall
      type: recall
      value: 0.34198331788693237
    - name: F1
      type: f1
      value: 0.4280742459396752
    - name: Accuracy
      type: accuracy
      value: 0.9453636013851482
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_wnut_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3526
- Precision: 0.5721
- Recall: 0.3420
- F1: 0.4281
- Accuracy: 0.9454

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 107  | 0.2863          | 0.3981    | 0.3494 | 0.3722 | 0.9328   |
| No log        | 2.0   | 214  | 0.3438          | 0.5734    | 0.3151 | 0.4067 | 0.9443   |
| No log        | 3.0   | 321  | 0.3482          | 0.5922    | 0.3216 | 0.4168 | 0.9445   |
| No log        | 4.0   | 428  | 0.3526          | 0.5721    | 0.3420 | 0.4281 | 0.9454   |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.14.1
