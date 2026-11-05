---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: pubmed-abs-noise-mixed-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-abs-noise-mixed-v1

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0138

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
| 1.6354        | 0.11  | 500   | 1.4407          |
| 1.5086        | 0.21  | 1000  | 1.3654          |
| 1.3652        | 0.32  | 1500  | 1.2886          |
| 1.3916        | 0.43  | 2000  | 1.2498          |
| 1.1973        | 0.54  | 2500  | 1.2173          |
| 1.3319        | 0.64  | 3000  | 1.1865          |
| 1.2166        | 0.75  | 3500  | 1.1537          |
| 1.2442        | 0.86  | 4000  | 1.1397          |
| 1.213         | 0.96  | 4500  | 1.1154          |
| 1.0495        | 1.07  | 5000  | 1.1122          |
| 1.0197        | 1.18  | 5500  | 1.1020          |
| 1.0838        | 1.28  | 6000  | 1.0941          |
| 1.0746        | 1.39  | 6500  | 1.0796          |
| 1.0549        | 1.5   | 7000  | 1.0648          |
| 1.0146        | 1.61  | 7500  | 1.0585          |
| 1.0384        | 1.71  | 8000  | 1.0564          |
| 0.9587        | 1.82  | 8500  | 1.0506          |
| 0.9968        | 1.93  | 9000  | 1.0392          |
| 0.9058        | 2.03  | 9500  | 1.0464          |
| 0.9116        | 2.14  | 10000 | 1.0335          |
| 0.8652        | 2.25  | 10500 | 1.0386          |
| 0.8749        | 2.35  | 11000 | 1.0301          |
| 0.8391        | 2.46  | 11500 | 1.0292          |
| 0.8816        | 2.57  | 12000 | 1.0192          |
| 0.919         | 2.68  | 12500 | 1.0196          |
| 0.9479        | 2.78  | 13000 | 1.0185          |
| 0.892         | 2.89  | 13500 | 1.0156          |
| 0.875         | 3.0   | 14000 | 1.0138          |


### Framework versions

- Transformers 4.36.1
- Pytorch 2.0.1
- Datasets 2.16.1
- Tokenizers 0.15.0
