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
- name: Depression_binary
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Depression_binary

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6424
- Accuracy: 0.7335
- Precision: 0.7480
- Recall: 0.7032
- F1: 0.7249
- Auc: 0.8024

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
| No log        | 1.0   | 118  | 0.5798          | 0.7210   | 0.7133    | 0.7382 | 0.7255 | 0.7697 |
| No log        | 2.0   | 236  | 0.5748          | 0.7285   | 0.7607    | 0.6658 | 0.7101 | 0.7955 |
| No log        | 3.0   | 354  | 0.6424          | 0.7335   | 0.7480    | 0.7032 | 0.7249 | 0.8024 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
