---
license: llama2
base_model: epfl-llm/meditron-7b
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: 500STEPS_1e6rate_01beta_DPO_Meditron7B
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 500STEPS_1e6rate_01beta_DPO_Meditron7B

This model is a fine-tuned version of [epfl-llm/meditron-7b](https://huggingface.co/epfl-llm/meditron-7b) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6302
- Rewards/chosen: 0.0115
- Rewards/rejected: -0.1672
- Rewards/accuracies: 0.5868
- Rewards/margins: 0.1788
- Logps/rejected: -29.4661
- Logps/chosen: -26.3659
- Logits/rejected: -0.7645
- Logits/chosen: -0.7643

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
- train_batch_size: 4
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 500

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6902        | 0.1   | 50   | 0.6903          | 0.0090         | 0.0031           | 0.5121             | 0.0058          | -27.7623       | -26.3918     | -0.6125         | -0.6124       |
| 0.6766        | 0.2   | 100  | 0.6792          | -0.1559        | -0.1907          | 0.5099             | 0.0349          | -29.7009       | -28.0399     | -0.6382         | -0.6380       |
| 0.6667        | 0.29  | 150  | 0.6567          | -0.0224        | -0.1102          | 0.5714             | 0.0879          | -28.8959       | -26.7051     | -0.6559         | -0.6557       |
| 0.6656        | 0.39  | 200  | 0.6495          | -0.0303        | -0.1387          | 0.5802             | 0.1084          | -29.1808       | -26.7847     | -0.7108         | -0.7106       |
| 0.5939        | 0.49  | 250  | 0.6388          | -0.0202        | -0.1629          | 0.5890             | 0.1426          | -29.4223       | -26.6837     | -0.7329         | -0.7327       |
| 0.6328        | 0.59  | 300  | 0.6349          | -0.0421        | -0.2022          | 0.5758             | 0.1601          | -29.8158       | -26.9024     | -0.7492         | -0.7490       |
| 0.6231        | 0.68  | 350  | 0.6313          | -0.0004        | -0.1725          | 0.5758             | 0.1721          | -29.5189       | -26.4852     | -0.7571         | -0.7569       |
| 0.6419        | 0.78  | 400  | 0.6303          | 0.0123         | -0.1660          | 0.5868             | 0.1783          | -29.4536       | -26.3585     | -0.7639         | -0.7637       |
| 0.6045        | 0.88  | 450  | 0.6304          | 0.0120         | -0.1662          | 0.5846             | 0.1783          | -29.4560       | -26.3611     | -0.7645         | -0.7643       |
| 0.5984        | 0.98  | 500  | 0.6302          | 0.0115         | -0.1672          | 0.5868             | 0.1788          | -29.4661       | -26.3659     | -0.7645         | -0.7643       |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.0.0+cu117
- Datasets 2.17.0
- Tokenizers 0.15.1
