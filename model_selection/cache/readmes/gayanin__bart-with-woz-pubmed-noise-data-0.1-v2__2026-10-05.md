---
license: apache-2.0
base_model: gayanin/bart-with-woz-noise-data-0.1-v2
tags:
- generated_from_trainer
model-index:
- name: bart-with-woz-pubmed-noise-data-0.1-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-with-woz-pubmed-noise-data-0.1-v2

This model is a fine-tuned version of [gayanin/bart-with-woz-noise-data-0.1-v2](https://huggingface.co/gayanin/bart-with-woz-noise-data-0.1-v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2136

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
| 0.395         | 0.11  | 500   | 0.3361          |
| 0.3239        | 0.21  | 1000  | 0.2993          |
| 0.2485        | 0.32  | 1500  | 0.2899          |
| 0.3632        | 0.43  | 2000  | 0.2650          |
| 0.3141        | 0.54  | 2500  | 0.2555          |
| 0.2913        | 0.64  | 3000  | 0.2537          |
| 0.2587        | 0.75  | 3500  | 0.2474          |
| 0.2745        | 0.86  | 4000  | 0.2408          |
| 0.2725        | 0.96  | 4500  | 0.2362          |
| 0.2025        | 1.07  | 5000  | 0.2468          |
| 0.2088        | 1.18  | 5500  | 0.2368          |
| 0.1912        | 1.28  | 6000  | 0.2447          |
| 0.2098        | 1.39  | 6500  | 0.2311          |
| 0.1839        | 1.5   | 7000  | 0.2336          |
| 0.2407        | 1.61  | 7500  | 0.2280          |
| 0.1692        | 1.71  | 8000  | 0.2229          |
| 0.1965        | 1.82  | 8500  | 0.2220          |
| 0.2013        | 1.93  | 9000  | 0.2175          |
| 0.1455        | 2.03  | 9500  | 0.2243          |
| 0.1466        | 2.14  | 10000 | 0.2235          |
| 0.1493        | 2.25  | 10500 | 0.2223          |
| 0.1224        | 2.35  | 11000 | 0.2207          |
| 0.1491        | 2.46  | 11500 | 0.2173          |
| 0.1484        | 2.57  | 12000 | 0.2175          |
| 0.1582        | 2.68  | 12500 | 0.2175          |
| 0.1592        | 2.78  | 13000 | 0.2137          |
| 0.1467        | 2.89  | 13500 | 0.2153          |
| 0.1637        | 3.0   | 14000 | 0.2136          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.2+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1
