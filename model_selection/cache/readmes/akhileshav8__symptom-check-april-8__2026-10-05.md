---
license: apache-2.0
base_model: distilgpt2
tags:
- generated_from_trainer
model-index:
- name: symptom-check-april-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# symptom-check-april-8

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1690

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.6017        | 1.0   | 1585  | 2.4486          |
| 2.4508        | 2.0   | 3170  | 2.3348          |
| 2.3795        | 3.0   | 4755  | 2.2760          |
| 2.3217        | 4.0   | 6340  | 2.2409          |
| 2.2964        | 5.0   | 7925  | 2.2146          |
| 2.2628        | 6.0   | 9510  | 2.1968          |
| 2.247         | 7.0   | 11095 | 2.1850          |
| 2.2319        | 8.0   | 12680 | 2.1756          |
| 2.2233        | 9.0   | 14265 | 2.1708          |
| 2.2061        | 10.0  | 15850 | 2.1690          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
