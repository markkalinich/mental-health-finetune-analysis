---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: Anxiety_binary
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Anxiety_binary

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7937
- Accuracy: 0.6837
- Precision: 0.6473
- Recall: 0.8055
- F1: 0.7178
- Auc: 0.7751

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 1234
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     | Auc    |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|:------:|
| No log        | 1.0   | 118  | 0.5902          | 0.6899   | 0.7275    | 0.6060 | 0.6612 | 0.7615 |
| No log        | 2.0   | 236  | 0.5518          | 0.7123   | 0.7471    | 0.6409 | 0.6899 | 0.7906 |
| No log        | 3.0   | 354  | 0.5580          | 0.7210   | 0.8149    | 0.5711 | 0.6716 | 0.8060 |
| No log        | 4.0   | 472  | 0.6352          | 0.6999   | 0.6569    | 0.8354 | 0.7355 | 0.7923 |
| 0.5423        | 5.0   | 590  | 0.7219          | 0.6999   | 0.6860    | 0.7357 | 0.7100 | 0.7836 |
| 0.5423        | 6.0   | 708  | 0.7937          | 0.6837   | 0.6473    | 0.8055 | 0.7178 | 0.7751 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
