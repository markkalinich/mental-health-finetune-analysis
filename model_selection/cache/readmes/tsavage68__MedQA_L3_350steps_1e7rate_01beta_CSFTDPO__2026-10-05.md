---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_350steps_1e7rate_01beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_350steps_1e7rate_01beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6777
- Rewards/chosen: 0.1095
- Rewards/rejected: 0.0772
- Rewards/accuracies: 0.7055
- Rewards/margins: 0.0324
- Logps/rejected: -33.0833
- Logps/chosen: -30.2335
- Logits/rejected: -0.7312
- Logits/chosen: -0.7305

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-07
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 350

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6932        | 0.0489 | 50   | 0.6927          | -0.0017        | -0.0025          | 0.5297             | 0.0008          | -33.8801       | -31.3453     | -0.7320         | -0.7313       |
| 0.691         | 0.0977 | 100  | 0.6894          | 0.0852         | 0.0776           | 0.6505             | 0.0076          | -33.0791       | -30.4769     | -0.7328         | -0.7321       |
| 0.6769        | 0.1466 | 150  | 0.6822          | 0.1412         | 0.1183           | 0.6857             | 0.0228          | -32.6716       | -29.9169     | -0.7316         | -0.7309       |
| 0.6718        | 0.1954 | 200  | 0.6794          | 0.0847         | 0.0559           | 0.7011             | 0.0288          | -33.2958       | -30.4811     | -0.7309         | -0.7302       |
| 0.6835        | 0.2443 | 250  | 0.6781          | 0.1060         | 0.0745           | 0.6791             | 0.0316          | -33.1100       | -30.2681     | -0.7308         | -0.7300       |
| 0.6749        | 0.2931 | 300  | 0.6777          | 0.1081         | 0.0756           | 0.7055             | 0.0325          | -33.0987       | -30.2473     | -0.7318         | -0.7311       |
| 0.6792        | 0.3420 | 350  | 0.6777          | 0.1095         | 0.0772           | 0.7055             | 0.0324          | -33.0833       | -30.2335     | -0.7312         | -0.7305       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
