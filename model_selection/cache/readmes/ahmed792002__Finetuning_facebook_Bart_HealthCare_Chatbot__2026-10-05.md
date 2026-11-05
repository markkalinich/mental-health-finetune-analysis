---
base_model: facebook/bart-base
library_name: transformers
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Finetuning_facebook_Bart_HealthCare_Chatbot
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Finetuning_facebook_Bart_HealthCare_Chatbot

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1176

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.0717        | 1.0   | 5660  | 0.1109          |
| 0.0603        | 2.0   | 11320 | 0.1089          |
| 0.0527        | 3.0   | 16980 | 0.1114          |
| 0.0487        | 4.0   | 22640 | 0.1113          |
| 0.0459        | 5.0   | 28300 | 0.1141          |
| 0.0417        | 6.0   | 33960 | 0.1138          |
| 0.0392        | 7.0   | 39620 | 0.1158          |
| 0.0373        | 8.0   | 45280 | 0.1169          |
| 0.0358        | 9.0   | 50940 | 0.1169          |
| 0.0343        | 10.0  | 56600 | 0.1176          |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 3.2.0
- Tokenizers 0.19.1
