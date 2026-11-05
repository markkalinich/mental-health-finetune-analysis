---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_250steps_1e7rate_05beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_250steps_1e7rate_05beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6492
- Rewards/chosen: 0.3403
- Rewards/rejected: 0.2334
- Rewards/accuracies: 0.6857
- Rewards/margins: 0.1070
- Logps/rejected: -33.3881
- Logps/chosen: -30.6478
- Logits/rejected: -0.7314
- Logits/chosen: -0.7307

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
- training_steps: 250

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6857        | 0.0489 | 50   | 0.6947          | -0.0249        | -0.0232          | 0.4879             | -0.0018         | -33.9011       | -31.3784     | -0.7318         | -0.7312       |
| 0.6799        | 0.0977 | 100  | 0.6734          | 0.3881         | 0.3450           | 0.6681             | 0.0432          | -33.1649       | -30.5522     | -0.7330         | -0.7323       |
| 0.6286        | 0.1466 | 150  | 0.6528          | 0.4844         | 0.3866           | 0.6813             | 0.0978          | -33.0816       | -30.3598     | -0.7312         | -0.7306       |
| 0.6183        | 0.1954 | 200  | 0.6449          | 0.3270         | 0.2107           | 0.7143             | 0.1163          | -33.4334       | -30.6745     | -0.7312         | -0.7305       |
| 0.6593        | 0.2443 | 250  | 0.6492          | 0.3403         | 0.2334           | 0.6857             | 0.1070          | -33.3881       | -30.6478     | -0.7314         | -0.7307       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
