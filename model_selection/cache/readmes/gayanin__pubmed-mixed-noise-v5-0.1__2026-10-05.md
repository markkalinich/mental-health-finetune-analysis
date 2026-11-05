---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: pubmed-mixed-noise-v5-0.1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-mixed-noise-v5-0.1

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2601

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
| 0.4739        | 0.11  | 500   | 0.4122          |
| 0.4076        | 0.21  | 1000  | 0.3695          |
| 0.4021        | 0.32  | 1500  | 0.3452          |
| 0.3769        | 0.43  | 2000  | 0.3364          |
| 0.3678        | 0.54  | 2500  | 0.3233          |
| 0.3178        | 0.64  | 3000  | 0.3142          |
| 0.3299        | 0.75  | 3500  | 0.3098          |
| 0.3109        | 0.86  | 4000  | 0.2953          |
| 0.2722        | 0.96  | 4500  | 0.2946          |
| 0.2715        | 1.07  | 5000  | 0.2936          |
| 0.2773        | 1.18  | 5500  | 0.2860          |
| 0.2814        | 1.28  | 6000  | 0.2894          |
| 0.2879        | 1.39  | 6500  | 0.2769          |
| 0.2821        | 1.5   | 7000  | 0.2770          |
| 0.2443        | 1.61  | 7500  | 0.2773          |
| 0.2226        | 1.71  | 8000  | 0.2732          |
| 0.2705        | 1.82  | 8500  | 0.2667          |
| 0.2374        | 1.93  | 9000  | 0.2638          |
| 0.2339        | 2.03  | 9500  | 0.2705          |
| 0.2106        | 2.14  | 10000 | 0.2685          |
| 0.2227        | 2.25  | 10500 | 0.2690          |
| 0.1773        | 2.35  | 11000 | 0.2682          |
| 0.195         | 2.46  | 11500 | 0.2635          |
| 0.1747        | 2.57  | 12000 | 0.2629          |
| 0.2245        | 2.68  | 12500 | 0.2620          |
| 0.1612        | 2.78  | 13000 | 0.2606          |
| 0.189         | 2.89  | 13500 | 0.2619          |
| 0.1768        | 3.0   | 14000 | 0.2601          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
