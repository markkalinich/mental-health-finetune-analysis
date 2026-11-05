---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
- f1
base_model: distilbert-base-uncased
model-index:
- name: distilbert-base-uncased-finetuned-emotional
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
      args: split
    metrics:
    - type: accuracy
      value: 0.9305
      name: Accuracy
    - type: f1
      value: 0.9309021978510164
      name: F1
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-emotional

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1658
- Accuracy: 0.9305
- F1: 0.9309

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.1683        | 1.0   | 250  | 0.1738          | 0.9295   | 0.9294 |
| 0.1085        | 2.0   | 500  | 0.1658          | 0.9305   | 0.9309 |


### Framework versions

- Transformers 4.16.2
- Pytorch 2.1.0+cu118
- Datasets 2.9.0
- Tokenizers 0.14.1
