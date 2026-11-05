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
- name: emotional-distilbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotional-distilbert

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2137
- Accuracy: 0.4310
- F1: 0.4257
- Precision: 0.4466
- Recall: 0.4310

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
| 2.7164        | 1.0   | 276  | 2.6348          | 0.2840   | 0.2368 | 0.4033    | 0.2840 |
| 1.3322        | 2.0   | 552  | 2.0566          | 0.4183   | 0.4064 | 0.4338    | 0.4183 |
| 0.5727        | 3.0   | 828  | 1.9395          | 0.4029   | 0.3975 | 0.4292    | 0.4029 |
| 0.2102        | 4.0   | 1104 | 1.9605          | 0.4156   | 0.4115 | 0.4400    | 0.4156 |
| 0.0697        | 5.0   | 1380 | 2.0963          | 0.4365   | 0.4205 | 0.4438    | 0.4365 |
| 0.0261        | 6.0   | 1656 | 2.2137          | 0.4310   | 0.4257 | 0.4466    | 0.4310 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
