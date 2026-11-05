---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: pubmed-mixed-noise-v3-0.1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-mixed-noise-v3-0.1

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2607

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
| 0.5222        | 0.11  | 500   | 0.4206          |
| 0.3862        | 0.21  | 1000  | 0.3907          |
| 0.4108        | 0.32  | 1500  | 0.3568          |
| 0.3871        | 0.43  | 2000  | 0.3415          |
| 0.3846        | 0.54  | 2500  | 0.3240          |
| 0.3313        | 0.64  | 3000  | 0.3124          |
| 0.3317        | 0.75  | 3500  | 0.3066          |
| 0.3136        | 0.86  | 4000  | 0.3049          |
| 0.3267        | 0.96  | 4500  | 0.2925          |
| 0.2816        | 1.07  | 5000  | 0.2929          |
| 0.2421        | 1.18  | 5500  | 0.2882          |
| 0.2643        | 1.28  | 6000  | 0.2872          |
| 0.2776        | 1.39  | 6500  | 0.2824          |
| 0.2854        | 1.5   | 7000  | 0.2751          |
| 0.2301        | 1.61  | 7500  | 0.2756          |
| 0.2118        | 1.71  | 8000  | 0.2770          |
| 0.2079        | 1.82  | 8500  | 0.2732          |
| 0.2474        | 1.93  | 9000  | 0.2631          |
| 0.1482        | 2.03  | 9500  | 0.2693          |
| 0.1908        | 2.14  | 10000 | 0.2656          |
| 0.2017        | 2.25  | 10500 | 0.2647          |
| 0.1687        | 2.35  | 11000 | 0.2680          |
| 0.191         | 2.46  | 11500 | 0.2630          |
| 0.1821        | 2.57  | 12000 | 0.2618          |
| 0.2301        | 2.68  | 12500 | 0.2605          |
| 0.2106        | 2.78  | 13000 | 0.2601          |
| 0.1637        | 2.89  | 13500 | 0.2617          |
| 0.1902        | 3.0   | 14000 | 0.2607          |


### Framework versions

- Transformers 4.36.1
- Pytorch 2.0.1
- Datasets 2.16.1
- Tokenizers 0.15.0
