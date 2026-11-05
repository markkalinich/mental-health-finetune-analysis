---
license: mit
base_model: deepset/gelectra-large
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: gecco-german-counseling-gelectra-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gecco-german-counseling-gelectra-large

This model is a fine-tuned version of [deepset/gelectra-large](https://huggingface.co/deepset/gelectra-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3342
- Accuracy: 0.7290
- F1: 0.4663

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
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 3.6182        | 1.0   | 20   | 3.4739          | 0.1710   | 0.0391 |
| 3.3872        | 2.0   | 40   | 3.1759          | 0.2742   | 0.0806 |
| 3.1164        | 3.0   | 60   | 2.8804          | 0.3774   | 0.1428 |
| 2.8264        | 4.0   | 80   | 2.5862          | 0.5290   | 0.2440 |
| 2.5488        | 5.0   | 100  | 2.3090          | 0.5871   | 0.2816 |
| 2.2554        | 6.0   | 120  | 2.0804          | 0.6194   | 0.3196 |
| 2.0363        | 7.0   | 140  | 1.9051          | 0.6452   | 0.3435 |
| 1.8361        | 8.0   | 160  | 1.7684          | 0.6677   | 0.3593 |
| 1.5928        | 9.0   | 180  | 1.6380          | 0.7      | 0.4038 |
| 1.5584        | 10.0  | 200  | 1.5519          | 0.7097   | 0.4142 |
| 1.3548        | 11.0  | 220  | 1.4832          | 0.7194   | 0.4325 |
| 1.2585        | 12.0  | 240  | 1.4253          | 0.7226   | 0.4530 |
| 1.209         | 13.0  | 260  | 1.3874          | 0.7194   | 0.4512 |
| 1.0846        | 14.0  | 280  | 1.3526          | 0.7323   | 0.4667 |
| 1.0705        | 15.0  | 300  | 1.3377          | 0.7258   | 0.4643 |
| 1.0137        | 16.0  | 320  | 1.3342          | 0.7290   | 0.4663 |


### Framework versions

- Transformers 4.35.1
- Pytorch 1.10.1+cu111
- Datasets 2.14.7
- Tokenizers 0.14.1
