---
license: mit
base_model: xlm-roberta-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii_model

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0008
- Precision: 0.7850
- Recall: 0.7925
- F1: 0.7887
- Accuracy: 0.9998

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 192  | 0.0023          | 0.0       | 0.0    | 0.0    | 0.9993   |
| No log        | 2.0   | 384  | 0.0008          | 0.8632    | 0.7736 | 0.8159 | 0.9999   |
| 0.0394        | 3.0   | 576  | 0.0008          | 0.6917    | 0.7830 | 0.7345 | 0.9998   |
| 0.0394        | 4.0   | 768  | 0.0008          | 0.6829    | 0.7925 | 0.7336 | 0.9998   |
| 0.0394        | 5.0   | 960  | 0.0008          | 0.7850    | 0.7925 | 0.7887 | 0.9998   |


### Framework versions

- Transformers 4.38.1
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.2
