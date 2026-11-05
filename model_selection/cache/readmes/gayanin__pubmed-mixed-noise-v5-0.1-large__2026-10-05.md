---
license: apache-2.0
base_model: facebook/bart-large
tags:
- generated_from_trainer
model-index:
- name: pubmed-mixed-noise-v5-0.1-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-mixed-noise-v5-0.1-large

This model is a fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3064

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
| 0.4762        | 0.11  | 500   | 0.4936          |
| 0.4174        | 0.21  | 1000  | 0.4293          |
| 0.3835        | 0.32  | 1500  | 0.4280          |
| 0.3628        | 0.43  | 2000  | 0.4472          |
| 0.3927        | 0.54  | 2500  | 0.3898          |
| 0.3012        | 0.64  | 3000  | 0.3744          |
| 0.3189        | 0.75  | 3500  | 0.3784          |
| 0.2986        | 0.86  | 4000  | 0.3624          |
| 0.2493        | 0.96  | 4500  | 0.3588          |
| 0.2438        | 1.07  | 5000  | 0.3439          |
| 0.2465        | 1.18  | 5500  | 0.3448          |
| 0.268         | 1.28  | 6000  | 0.3476          |
| 0.2298        | 1.39  | 6500  | 0.3411          |
| 0.2587        | 1.5   | 7000  | 0.3322          |
| 0.2499        | 1.61  | 7500  | 0.3253          |
| 0.2296        | 1.71  | 8000  | 0.3177          |
| 0.2184        | 1.82  | 8500  | 0.3175          |
| 0.2245        | 1.93  | 9000  | 0.3573          |
| 0.164         | 2.03  | 9500  | 0.3292          |
| 0.1784        | 2.14  | 10000 | 0.3224          |
| 0.1487        | 2.25  | 10500 | 0.3209          |
| 0.1818        | 2.35  | 11000 | 0.3175          |
| 0.1521        | 2.46  | 11500 | 0.3190          |
| 0.1663        | 2.57  | 12000 | 0.3137          |
| 0.1604        | 2.68  | 12500 | 0.3113          |
| 0.1447        | 2.78  | 13000 | 0.3080          |
| 0.162         | 2.89  | 13500 | 0.3068          |
| 0.1414        | 3.0   | 14000 | 0.3064          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
