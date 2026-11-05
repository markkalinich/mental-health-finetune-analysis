---
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: emotional-distilbert-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotional-distilbert-3

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1515
- Accuracy: 0.4428
- F1: 0.4258
- Precision: 0.4408
- Recall: 0.4428

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
| 2.7857        | 1.0   | 270  | 2.7060          | 0.2505   | 0.2301 | 0.3881    | 0.2505 |
| 1.4183        | 2.0   | 540  | 2.1665          | 0.3693   | 0.3674 | 0.4295    | 0.3693 |
| 0.621         | 3.0   | 810  | 1.8691          | 0.4419   | 0.4343 | 0.4545    | 0.4419 |
| 0.2352        | 4.0   | 1080 | 1.8406          | 0.4401   | 0.4333 | 0.4571    | 0.4401 |
| 0.0816        | 5.0   | 1350 | 1.9892          | 0.4474   | 0.4335 | 0.4518    | 0.4474 |
| 0.0284        | 6.0   | 1620 | 2.1080          | 0.4347   | 0.4224 | 0.4365    | 0.4347 |
| 0.0141        | 7.0   | 1890 | 2.1515          | 0.4428   | 0.4258 | 0.4408    | 0.4428 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
