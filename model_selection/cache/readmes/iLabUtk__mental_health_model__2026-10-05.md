---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mental_health_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental_health_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4142
- Accuracy: 0.7504

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 270  | 0.6937          | 0.6957   |
| 0.7345        | 2.0   | 540  | 0.6217          | 0.7401   |
| 0.7345        | 3.0   | 810  | 0.6691          | 0.7428   |
| 0.346         | 4.0   | 1080 | 0.7451          | 0.7537   |
| 0.346         | 5.0   | 1350 | 0.9557          | 0.7461   |
| 0.1315        | 6.0   | 1620 | 1.1519          | 0.7515   |
| 0.1315        | 7.0   | 1890 | 1.2995          | 0.7369   |
| 0.0472        | 8.0   | 2160 | 1.4142          | 0.7396   |
| 0.0472        | 9.0   | 2430 | 1.4000          | 0.7499   |
| 0.0226        | 10.0  | 2700 | 1.4142          | 0.7504   |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
