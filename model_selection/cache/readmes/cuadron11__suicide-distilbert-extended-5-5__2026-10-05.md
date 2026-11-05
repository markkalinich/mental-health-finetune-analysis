---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
model-index:
- name: suicide-distilbert-extended-5-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# suicide-distilbert-extended-5-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9133
- Accuracy: {'accuracy': 0.3873050026896181}
- Precision: 0.3977
- Recall: 0.3873
- Fscore: 0.3793

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy                          | Precision | Recall | Fscore |
|:-------------:|:-----:|:----:|:---------------:|:---------------------------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 349  | 1.4635          | {'accuracy': 0.3442711135018827}  | 0.3793    | 0.3443 | 0.3050 |
| 1.4502        | 2.0   | 698  | 1.4143          | {'accuracy': 0.3862291554599247}  | 0.3954    | 0.3862 | 0.3454 |
| 1.1938        | 3.0   | 1047 | 1.4696          | {'accuracy': 0.399677245831092}   | 0.4354    | 0.3997 | 0.3775 |
| 1.1938        | 4.0   | 1396 | 1.7198          | {'accuracy': 0.39483593329747174} | 0.4181    | 0.3948 | 0.3799 |
| 0.714         | 5.0   | 1745 | 1.9133          | {'accuracy': 0.3873050026896181}  | 0.3977    | 0.3873 | 0.3793 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
