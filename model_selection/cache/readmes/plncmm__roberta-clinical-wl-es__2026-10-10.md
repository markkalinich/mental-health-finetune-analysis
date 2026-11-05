---
license: apache-2.0
language:
- es
widget:
- text: "Periodontitis <mask> generalizada severa."
- text: "Caries dentinaria <mask>."
- text: "Movilidad aumentada en pza <mask>."
- text: "Pcte con dm en tto con <mask>."
- text: "Pcte con erc en tto con <mask>."
tags:
- generated_from_trainer
model-index:
- name: roberta-clinical-wl-es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# plncmm/roberta-clinical-wl-es

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-biomedical-clinical-es](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es) on the Chilean waiting list dataset.

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1
