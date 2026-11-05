---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_300steps_1e6rate_01beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_300steps_1e6rate_01beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4661
- Rewards/chosen: 0.6273
- Rewards/rejected: -0.3771
- Rewards/accuracies: 0.7604
- Rewards/margins: 1.0045
- Logps/rejected: -37.6261
- Logps/chosen: -25.0552
- Logits/rejected: -0.8801
- Logits/chosen: -0.8780

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 300

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6869        | 0.0489 | 50   | 0.6696          | -0.2211        | -0.2710          | 0.7253             | 0.0498          | -36.5645       | -33.5400     | -0.7298         | -0.7290       |
| 0.4779        | 0.0977 | 100  | 0.5887          | 1.4526         | 1.0417           | 0.6945             | 0.4109          | -23.4374       | -16.8024     | -0.8047         | -0.8036       |
| 0.5155        | 0.1466 | 150  | 0.4976          | 0.6394         | -0.2000          | 0.7363             | 0.8394          | -35.8551       | -24.9343     | -0.8636         | -0.8617       |
| 0.4245        | 0.1954 | 200  | 0.4924          | 0.0477         | -0.9077          | 0.7648             | 0.9554          | -42.9321       | -30.8513     | -0.8783         | -0.8762       |
| 0.4563        | 0.2443 | 250  | 0.4675          | 0.6549         | -0.3364          | 0.7560             | 0.9913          | -37.2189       | -24.7791     | -0.8807         | -0.8786       |
| 0.3066        | 0.2931 | 300  | 0.4661          | 0.6273         | -0.3771          | 0.7604             | 1.0045          | -37.6261       | -25.0552     | -0.8801         | -0.8780       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
