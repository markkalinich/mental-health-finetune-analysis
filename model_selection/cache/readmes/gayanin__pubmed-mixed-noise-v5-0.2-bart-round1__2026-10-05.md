---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: pubmed-mixed-noise-v5-0.2-bart-round1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-mixed-noise-v5-0.2-bart-round1

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4138

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
| 0.776         | 0.11  | 500   | 0.6898          |
| 0.6409        | 0.21  | 1000  | 0.6108          |
| 0.5906        | 0.32  | 1500  | 0.5788          |
| 0.6653        | 0.43  | 2000  | 0.5434          |
| 0.5767        | 0.54  | 2500  | 0.5232          |
| 0.5719        | 0.64  | 3000  | 0.5019          |
| 0.5439        | 0.75  | 3500  | 0.4917          |
| 0.5092        | 0.86  | 4000  | 0.4743          |
| 0.4964        | 0.96  | 4500  | 0.4696          |
| 0.4411        | 1.07  | 5000  | 0.4704          |
| 0.4703        | 1.18  | 5500  | 0.4564          |
| 0.4314        | 1.28  | 6000  | 0.4609          |
| 0.4309        | 1.39  | 6500  | 0.4496          |
| 0.4375        | 1.5   | 7000  | 0.4362          |
| 0.4008        | 1.61  | 7500  | 0.4396          |
| 0.399         | 1.71  | 8000  | 0.4366          |
| 0.448         | 1.82  | 8500  | 0.4266          |
| 0.4163        | 1.93  | 9000  | 0.4212          |
| 0.3836        | 2.03  | 9500  | 0.4257          |
| 0.3627        | 2.14  | 10000 | 0.4239          |
| 0.3709        | 2.25  | 10500 | 0.4283          |
| 0.3262        | 2.35  | 11000 | 0.4201          |
| 0.334         | 2.46  | 11500 | 0.4189          |
| 0.3581        | 2.57  | 12000 | 0.4172          |
| 0.3595        | 2.68  | 12500 | 0.4135          |
| 0.3095        | 2.78  | 13000 | 0.4137          |
| 0.3552        | 2.89  | 13500 | 0.4141          |
| 0.3763        | 3.0   | 14000 | 0.4138          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
