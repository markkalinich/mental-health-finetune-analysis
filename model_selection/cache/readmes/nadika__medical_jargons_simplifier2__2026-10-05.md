---
base_model: luqh/ClinicalT5-base
tags:
- generated_from_trainer
model-index:
- name: medical_jargons_simplifier2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_jargons_simplifier2

This model is a fine-tuned version of [luqh/ClinicalT5-base](https://huggingface.co/luqh/ClinicalT5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4641

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 5
- num_epochs: 10

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 10.6338       | 0.3378 | 50   | 5.9582          |
| 3.6156        | 0.6757 | 100  | 1.0741          |
| 1.3304        | 1.0135 | 150  | 0.8368          |
| 1.0096        | 1.3514 | 200  | 0.7519          |
| 0.933         | 1.6892 | 250  | 0.7019          |
| 0.8178        | 2.0270 | 300  | 0.6586          |
| 0.7714        | 2.3649 | 350  | 0.6188          |
| 0.7077        | 2.7027 | 400  | 0.5924          |
| 0.7406        | 3.0405 | 450  | 0.5673          |
| 0.6601        | 3.3784 | 500  | 0.5531          |
| 0.6637        | 3.7162 | 550  | 0.5388          |
| 0.6489        | 4.0541 | 600  | 0.5281          |
| 0.6369        | 4.3919 | 650  | 0.5187          |
| 0.5996        | 4.7297 | 700  | 0.5109          |
| 0.5816        | 5.0676 | 750  | 0.5028          |
| 0.5714        | 5.4054 | 800  | 0.4961          |
| 0.5826        | 5.7432 | 850  | 0.4910          |
| 0.5646        | 6.0811 | 900  | 0.4855          |
| 0.5379        | 6.4189 | 950  | 0.4827          |
| 0.5586        | 6.7568 | 1000 | 0.4785          |
| 0.5408        | 7.0946 | 1050 | 0.4751          |
| 0.5576        | 7.4324 | 1100 | 0.4727          |
| 0.5241        | 7.7703 | 1150 | 0.4710          |
| 0.5298        | 8.1081 | 1200 | 0.4695          |
| 0.5424        | 8.4459 | 1250 | 0.4677          |
| 0.5038        | 8.7838 | 1300 | 0.4665          |
| 0.5545        | 9.1216 | 1350 | 0.4653          |
| 0.523         | 9.4595 | 1400 | 0.4644          |
| 0.5029        | 9.7973 | 1450 | 0.4641          |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.1.2
- Datasets 2.19.2
- Tokenizers 0.19.1
