---
license: mit
base_model: xlm-roberta-base
tags:
- generated_from_trainer
model-index:
- name: xlm-roberta-base-pii-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-pii-finetuned

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0015
- F Beta: 0.8185

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | F Beta |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.001         | 1.0   | 724  | 0.0025          | 0.7038 |
| 0.0011        | 2.0   | 1448 | 0.0016          | 0.7915 |
| 0.0014        | 3.0   | 2172 | 0.0015          | 0.8185 |


### Framework versions

- Transformers 4.37.1
- Pytorch 2.0.0
- Datasets 2.16.1
- Tokenizers 0.15.0
