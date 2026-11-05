---
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: model_checkpoints
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_checkpoints

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6941
- Precision: 0.6667
- Recall: 0.6667
- F1: 0.6667
- Accuracy: 0.6667

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 225  | 0.7271          | 0.6589    | 0.6589 | 0.6589 | 0.6589   |
| No log        | 2.0   | 450  | 0.6941          | 0.6667    | 0.6667 | 0.6667 | 0.6667   |
| 0.7284        | 3.0   | 675  | 0.7404          | 0.6656    | 0.6656 | 0.6656 | 0.6656   |
| 0.7284        | 4.0   | 900  | 0.8450          | 0.6622    | 0.6622 | 0.6622 | 0.6622   |
| 0.4293        | 5.0   | 1125 | 0.9263          | 0.6567    | 0.6567 | 0.6567 | 0.6567   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.2
- Tokenizers 0.19.1
