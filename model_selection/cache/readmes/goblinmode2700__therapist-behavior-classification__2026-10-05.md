---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: therapist-behavior-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# therapist-behavior-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0910
- Accuracy: 0.7968

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
| No log        | 1.0   | 221  | 0.6711          | 0.7720   |
| No log        | 2.0   | 442  | 0.6412          | 0.8194   |
| 0.3541        | 3.0   | 663  | 0.7487          | 0.7856   |
| 0.3541        | 4.0   | 884  | 0.8332          | 0.7968   |
| 0.1707        | 5.0   | 1105 | 0.9524          | 0.8059   |
| 0.1707        | 6.0   | 1326 | 1.0313          | 0.8036   |
| 0.0839        | 7.0   | 1547 | 1.0615          | 0.7923   |
| 0.0839        | 8.0   | 1768 | 1.0899          | 0.7968   |
| 0.0839        | 9.0   | 1989 | 1.0779          | 0.8059   |
| 0.0465        | 10.0  | 2210 | 1.0910          | 0.7968   |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.1+cpu
- Datasets 2.10.1
- Tokenizers 0.13.2
