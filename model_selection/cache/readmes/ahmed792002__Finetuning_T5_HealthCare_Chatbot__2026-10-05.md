---
library_name: transformers
license: apache-2.0
base_model: t5-small
tags:
- generated_from_trainer
model-index:
- name: Finetuning_T5_HealthCare_Chatbot
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Finetuning_T5_HealthCare_Chatbot

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1304

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
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.1198        | 1.0   | 5660  | 0.1464          |
| 0.1098        | 2.0   | 11320 | 0.1402          |
| 0.1032        | 3.0   | 16980 | 0.1373          |
| 0.1016        | 4.0   | 22640 | 0.1349          |
| 0.1019        | 5.0   | 28300 | 0.1331          |
| 0.0972        | 6.0   | 33960 | 0.1321          |
| 0.0964        | 7.0   | 39620 | 0.1313          |
| 0.0947        | 8.0   | 45280 | 0.1308          |
| 0.0959        | 9.0   | 50940 | 0.1305          |
| 0.0933        | 10.0  | 56600 | 0.1304          |


### Framework versions

- Transformers 4.46.3
- Pytorch 2.4.0
- Datasets 3.1.0
- Tokenizers 0.20.3
