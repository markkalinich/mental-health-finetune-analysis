---
library_name: transformers
license: mit
base_model: obi/deid_roberta_i2b2
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: fine-tuned-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine-tuned-model

This model is a fine-tuned version of [obi/deid_roberta_i2b2](https://huggingface.co/obi/deid_roberta_i2b2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2126
- Model Preparation Time: 0.0061
- Precision: 0.9143
- Recall: 0.9156
- F1: 0.9132
- Accuracy: 0.9156

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Model Preparation Time | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:----------------------:|:---------:|:------:|:------:|:--------:|
| 0.4678        | 1.0   | 125  | 0.4248          | 0.0061                 | 0.7737    | 0.8229 | 0.7836 | 0.8229   |
| 0.3877        | 2.0   | 250  | 0.4008          | 0.0061                 | 0.7886    | 0.8282 | 0.8060 | 0.8282   |
| 0.3391        | 3.0   | 375  | 0.3132          | 0.0061                 | 0.8213    | 0.8672 | 0.8389 | 0.8672   |
| 0.3091        | 4.0   | 500  | 0.3124          | 0.0061                 | 0.8334    | 0.8597 | 0.8419 | 0.8597   |
| 0.2572        | 5.0   | 625  | 0.2570          | 0.0061                 | 0.8675    | 0.8911 | 0.8739 | 0.8911   |
| 0.2368        | 6.0   | 750  | 0.2270          | 0.0061                 | 0.8908    | 0.9084 | 0.8973 | 0.9084   |
| 0.2115        | 7.0   | 875  | 0.2219          | 0.0061                 | 0.8960    | 0.9081 | 0.9017 | 0.9081   |
| 0.1949        | 8.0   | 1000 | 0.2325          | 0.0061                 | 0.8993    | 0.9044 | 0.8991 | 0.9044   |
| 0.1843        | 9.0   | 1125 | 0.2218          | 0.0061                 | 0.9035    | 0.9103 | 0.9059 | 0.9103   |
| 0.1691        | 10.0  | 1250 | 0.2126          | 0.0061                 | 0.9143    | 0.9156 | 0.9132 | 0.9156   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu124
- Datasets 2.14.5
- Tokenizers 0.19.1
