---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: bart-with-woz-noise-data-0.1-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-with-woz-noise-data-0.1-v2

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
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
| 0.2188        | 0.13  | 500   | 0.1794          |
| 0.1741        | 0.26  | 1000  | 0.1518          |
| 0.1631        | 0.39  | 1500  | 0.1327          |
| 0.1318        | 0.53  | 2000  | 0.1272          |
| 0.1238        | 0.66  | 2500  | 0.1168          |
| 0.1451        | 0.79  | 3000  | 0.1103          |
| 0.1166        | 0.92  | 3500  | 0.1068          |
| 0.0833        | 1.05  | 4000  | 0.1054          |
| 0.1029        | 1.18  | 4500  | 0.1017          |
| 0.1174        | 1.31  | 5000  | 0.0971          |
| 0.0786        | 1.44  | 5500  | 0.0956          |
| 0.1184        | 1.58  | 6000  | 0.0951          |
| 0.0984        | 1.71  | 6500  | 0.0926          |
| 0.0959        | 1.84  | 7000  | 0.0893          |
| 0.093         | 1.97  | 7500  | 0.0893          |
| 0.0783        | 2.1   | 8000  | 0.0910          |
| 0.0678        | 2.23  | 8500  | 0.0927          |
| 0.0756        | 2.36  | 9000  | 0.0889          |
| 0.0684        | 2.5   | 9500  | 0.0877          |
| 0.0573        | 2.63  | 10000 | 0.0872          |
| 0.0544        | 2.76  | 10500 | 0.0855          |
| 0.0579        | 2.89  | 11000 | 0.0845          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.2+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1
