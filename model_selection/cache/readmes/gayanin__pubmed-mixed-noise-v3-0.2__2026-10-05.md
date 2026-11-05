---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: pubmed-mixed-noise-v3-0.2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-mixed-noise-v3-0.2

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4140

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
| 0.7328        | 0.11  | 500   | 0.6952          |
| 0.6994        | 0.21  | 1000  | 0.6005          |
| 0.6684        | 0.32  | 1500  | 0.5670          |
| 0.6305        | 0.43  | 2000  | 0.5402          |
| 0.6224        | 0.54  | 2500  | 0.5175          |
| 0.6009        | 0.64  | 3000  | 0.5001          |
| 0.5126        | 0.75  | 3500  | 0.4935          |
| 0.5698        | 0.86  | 4000  | 0.4793          |
| 0.497         | 0.96  | 4500  | 0.4715          |
| 0.3716        | 1.07  | 5000  | 0.4689          |
| 0.4522        | 1.18  | 5500  | 0.4551          |
| 0.3958        | 1.28  | 6000  | 0.4556          |
| 0.4398        | 1.39  | 6500  | 0.4502          |
| 0.4572        | 1.5   | 7000  | 0.4425          |
| 0.4339        | 1.61  | 7500  | 0.4424          |
| 0.4289        | 1.71  | 8000  | 0.4322          |
| 0.3771        | 1.82  | 8500  | 0.4337          |
| 0.3668        | 1.93  | 9000  | 0.4265          |
| 0.3342        | 2.03  | 9500  | 0.4316          |
| 0.3465        | 2.14  | 10000 | 0.4244          |
| 0.32          | 2.25  | 10500 | 0.4226          |
| 0.3493        | 2.35  | 11000 | 0.4244          |
| 0.3549        | 2.46  | 11500 | 0.4216          |
| 0.3281        | 2.57  | 12000 | 0.4192          |
| 0.3259        | 2.68  | 12500 | 0.4181          |
| 0.3444        | 2.78  | 13000 | 0.4156          |
| 0.3201        | 2.89  | 13500 | 0.4146          |
| 0.3315        | 3.0   | 14000 | 0.4140          |


### Framework versions

- Transformers 4.36.1
- Pytorch 2.0.1
- Datasets 2.16.1
- Tokenizers 0.15.0
