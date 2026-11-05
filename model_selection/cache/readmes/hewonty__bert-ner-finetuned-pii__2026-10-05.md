---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-ner-finetuned-pii
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-ner-finetuned-pii

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0076
- Precision: 0.9427
- Recall: 0.9727
- F1: 0.9575
- Accuracy: 0.9982

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0105        | 1.0   | 1324 | 0.0132          | 0.8641    | 0.9464 | 0.9033 | 0.9960   |
| 0.0056        | 2.0   | 2648 | 0.0080          | 0.9298    | 0.9643 | 0.9467 | 0.9978   |
| 0.0047        | 3.0   | 3972 | 0.0076          | 0.9427    | 0.9727 | 0.9575 | 0.9982   |


### Framework versions

- Transformers 4.37.0
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.1
