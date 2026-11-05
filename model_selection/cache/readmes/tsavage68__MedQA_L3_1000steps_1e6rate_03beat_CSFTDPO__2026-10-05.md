---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e6rate_03beat_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e6rate_03beat_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4903
- Rewards/chosen: -1.3915
- Rewards/rejected: -4.1668
- Rewards/accuracies: 0.8000
- Rewards/margins: 2.7753
- Logps/rejected: -35.2059
- Logps/chosen: -22.8611
- Logits/rejected: -1.0845
- Logits/chosen: -1.0822

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
- training_steps: 1000

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.7072        | 0.0489 | 50   | 0.6474          | 0.1422         | 0.0242           | 0.6505             | 0.1180          | -21.2360       | -17.7487     | -0.9397         | -0.9391       |
| 0.6194        | 0.0977 | 100  | 0.5755          | -0.5279        | -1.1917          | 0.6989             | 0.6638          | -25.2888       | -19.9824     | -1.0174         | -1.0166       |
| 0.6612        | 0.1466 | 150  | 0.5309          | -1.3933        | -2.5630          | 0.7385             | 1.1696          | -29.8598       | -22.8671     | -1.0200         | -1.0189       |
| 0.4211        | 0.1954 | 200  | 0.5615          | -2.1966        | -3.5809          | 0.7582             | 1.3843          | -33.2527       | -25.5445     | -1.0780         | -1.0762       |
| 0.5049        | 0.2443 | 250  | 0.5339          | -1.9870        | -3.6655          | 0.7560             | 1.6786          | -33.5350       | -24.8458     | -1.0753         | -1.0734       |
| 0.4905        | 0.2931 | 300  | 0.5368          | -1.5387        | -3.9759          | 0.7890             | 2.4373          | -34.5696       | -23.3515     | -1.0716         | -1.0697       |
| 0.5349        | 0.3420 | 350  | 0.5044          | -1.7611        | -3.9194          | 0.7978             | 2.1584          | -34.3813       | -24.0928     | -1.0522         | -1.0503       |
| 0.586         | 0.3908 | 400  | 0.5139          | -0.8107        | -2.8258          | 0.7758             | 2.0151          | -30.7357       | -20.9249     | -1.0499         | -1.0483       |
| 0.6603        | 0.4397 | 450  | 0.5095          | -1.6578        | -3.9722          | 0.7868             | 2.3144          | -34.5573       | -23.7487     | -1.0603         | -1.0582       |
| 0.7395        | 0.4885 | 500  | 0.5087          | -1.0636        | -3.2773          | 0.8000             | 2.2137          | -32.2408       | -21.7680     | -1.0493         | -1.0473       |
| 0.3843        | 0.5374 | 550  | 0.4836          | -1.6858        | -4.0020          | 0.7956             | 2.3162          | -34.6566       | -23.8419     | -1.0660         | -1.0640       |
| 0.3562        | 0.5862 | 600  | 0.4783          | -1.2031        | -3.7823          | 0.8000             | 2.5792          | -33.9241       | -22.2329     | -1.0733         | -1.0710       |
| 0.425         | 0.6351 | 650  | 0.4914          | -1.0022        | -3.6871          | 0.7978             | 2.6849          | -33.6067       | -21.5632     | -1.0756         | -1.0733       |
| 0.3857        | 0.6839 | 700  | 0.4896          | -1.3529        | -4.0709          | 0.8022             | 2.7180          | -34.8863       | -22.7325     | -1.0828         | -1.0804       |
| 0.3697        | 0.7328 | 750  | 0.4901          | -1.3499        | -4.0995          | 0.8000             | 2.7496          | -34.9816       | -22.7224     | -1.0838         | -1.0815       |
| 0.4451        | 0.7816 | 800  | 0.4900          | -1.3999        | -4.1652          | 0.7978             | 2.7653          | -35.2006       | -22.8891     | -1.0849         | -1.0826       |
| 0.4618        | 0.8305 | 850  | 0.4906          | -1.3853        | -4.1559          | 0.8022             | 2.7705          | -35.1694       | -22.8405     | -1.0849         | -1.0826       |
| 0.7121        | 0.8793 | 900  | 0.4906          | -1.3895        | -4.1617          | 0.8000             | 2.7722          | -35.1890       | -22.8544     | -1.0848         | -1.0825       |
| 0.2214        | 0.9282 | 950  | 0.4913          | -1.3912        | -4.1630          | 0.7956             | 2.7718          | -35.1932       | -22.8601     | -1.0848         | -1.0825       |
| 0.1914        | 0.9770 | 1000 | 0.4903          | -1.3915        | -4.1668          | 0.8000             | 2.7753          | -35.2059       | -22.8611     | -1.0845         | -1.0822       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
