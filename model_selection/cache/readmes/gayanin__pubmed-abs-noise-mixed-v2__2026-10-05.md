---
license: apache-2.0
base_model: facebook/bart-large
tags:
- generated_from_trainer
model-index:
- name: pubmed-abs-noise-mixed-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-abs-noise-mixed-v2

This model is a fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9626

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
| 1.5067        | 0.11  | 500   | 1.3888          |
| 1.373         | 0.21  | 1000  | 1.3029          |
| 1.2141        | 0.32  | 1500  | 1.2323          |
| 1.2791        | 0.43  | 2000  | 1.2643          |
| 1.0758        | 0.54  | 2500  | 1.1578          |
| 1.2029        | 0.64  | 3000  | 1.1410          |
| 1.109         | 0.75  | 3500  | 1.1115          |
| 1.1173        | 0.86  | 4000  | 1.0894          |
| 1.068         | 0.96  | 4500  | 1.0772          |
| 0.917         | 1.07  | 5000  | 1.0755          |
| 0.8664        | 1.18  | 5500  | 1.0731          |
| 0.9063        | 1.28  | 6000  | 1.0501          |
| 0.9207        | 1.39  | 6500  | 1.0393          |
| 0.9118        | 1.5   | 7000  | 1.0257          |
| 0.8558        | 1.61  | 7500  | 1.0107          |
| 0.8938        | 1.71  | 8000  | 1.0114          |
| 0.816         | 1.82  | 8500  | 0.9993          |
| 0.8644        | 1.93  | 9000  | 0.9856          |
| 0.7265        | 2.03  | 9500  | 1.0233          |
| 0.7326        | 2.14  | 10000 | 0.9946          |
| 0.6854        | 2.25  | 10500 | 0.9921          |
| 0.6851        | 2.35  | 11000 | 0.9826          |
| 0.6521        | 2.46  | 11500 | 0.9788          |
| 0.6671        | 2.57  | 12000 | 0.9734          |
| 0.7138        | 2.68  | 12500 | 0.9707          |
| 0.7599        | 2.78  | 13000 | 0.9653          |
| 0.6576        | 2.89  | 13500 | 0.9642          |
| 0.68          | 3.0   | 14000 | 0.9626          |


### Framework versions

- Transformers 4.36.1
- Pytorch 2.0.1
- Datasets 2.16.1
- Tokenizers 0.15.0
