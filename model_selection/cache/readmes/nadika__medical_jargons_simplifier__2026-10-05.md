---
base_model: luqh/ClinicalT5-base
tags:
- generated_from_trainer
model-index:
- name: medical_jargons_simplifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_jargons_simplifier

This model is a fine-tuned version of [luqh/ClinicalT5-base](https://huggingface.co/luqh/ClinicalT5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4405

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
- lr_scheduler_warmup_steps: 50
- num_epochs: 2

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 3.2542        | 0.2017 | 500  | 0.5136          |
| 0.5482        | 0.4034 | 1000 | 0.4729          |
| 0.5112        | 0.6051 | 1500 | 0.4599          |
| 0.5042        | 0.8068 | 2000 | 0.4532          |
| 0.5043        | 1.0085 | 2500 | 0.4488          |
| 0.5085        | 1.2102 | 3000 | 0.4448          |
| 0.4692        | 1.4119 | 3500 | 0.4432          |
| 0.495         | 1.6136 | 4000 | 0.4416          |
| 0.4798        | 1.8152 | 4500 | 0.4405          |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.1.2
- Datasets 2.19.2
- Tokenizers 0.19.1
