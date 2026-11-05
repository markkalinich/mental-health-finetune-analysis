---
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: emotional-bert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotional-bert

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5503
- Accuracy: 0.4065
- F1: 0.3831
- Precision: 0.3926
- Recall: 0.4065

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 2.82          | 1.0   | 270  | 2.7828          | 0.1733   | 0.1556 | 0.2256    | 0.1733 |
| 1.4083        | 2.0   | 540  | 2.3254          | 0.3230   | 0.3235 | 0.3651    | 0.3230 |
| 0.6017        | 3.0   | 810  | 2.1533          | 0.3766   | 0.3669 | 0.3880    | 0.3766 |
| 0.2357        | 4.0   | 1080 | 2.2329          | 0.3721   | 0.3620 | 0.3727    | 0.3721 |
| 0.0868        | 5.0   | 1350 | 2.3517          | 0.4065   | 0.3878 | 0.3897    | 0.4065 |
| 0.0328        | 6.0   | 1620 | 2.5503          | 0.4065   | 0.3831 | 0.3926    | 0.4065 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
