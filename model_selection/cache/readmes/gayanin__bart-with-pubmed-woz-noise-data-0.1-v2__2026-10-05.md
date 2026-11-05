---
license: apache-2.0
base_model: gayanin/bart-with-pubmed-noise-data-0.1-v2
tags:
- generated_from_trainer
model-index:
- name: bart-with-pubmed-woz-noise-data-0.1-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-with-pubmed-woz-noise-data-0.1-v2

This model is a fine-tuned version of [gayanin/bart-with-pubmed-noise-data-0.1-v2](https://huggingface.co/gayanin/bart-with-pubmed-noise-data-0.1-v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0845

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.1481        | 0.13  | 500   | 0.1476          |
| 0.1522        | 0.26  | 1000  | 0.1299          |
| 0.1537        | 0.39  | 1500  | 0.1191          |
| 0.1123        | 0.53  | 2000  | 0.1188          |
| 0.1258        | 0.66  | 2500  | 0.1099          |
| 0.1251        | 0.79  | 3000  | 0.1047          |
| 0.1127        | 0.92  | 3500  | 0.1023          |
| 0.075         | 1.05  | 4000  | 0.1009          |
| 0.0875        | 1.18  | 4500  | 0.1005          |
| 0.1061        | 1.31  | 5000  | 0.0957          |
| 0.073         | 1.44  | 5500  | 0.0926          |
| 0.1089        | 1.58  | 6000  | 0.0918          |
| 0.0889        | 1.71  | 6500  | 0.0917          |
| 0.0765        | 1.84  | 7000  | 0.0892          |
| 0.0883        | 1.97  | 7500  | 0.0870          |
| 0.0669        | 2.1   | 8000  | 0.0899          |
| 0.0631        | 2.23  | 8500  | 0.0908          |
| 0.072         | 2.36  | 9000  | 0.0872          |
| 0.0612        | 2.5   | 9500  | 0.0870          |
| 0.0686        | 2.63  | 10000 | 0.0859          |
| 0.0536        | 2.76  | 10500 | 0.0851          |
| 0.0571        | 2.89  | 11000 | 0.0845          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.2+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1
