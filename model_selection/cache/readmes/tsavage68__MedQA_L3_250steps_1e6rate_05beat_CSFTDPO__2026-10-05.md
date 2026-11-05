---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_250steps_1e6rate_05beat_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_250steps_1e6rate_05beat_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5035
- Rewards/chosen: -0.9245
- Rewards/rejected: -2.5465
- Rewards/accuracies: 0.7626
- Rewards/margins: 1.6220
- Logps/rejected: -26.4095
- Logps/chosen: -20.0716
- Logits/rejected: -0.9727
- Logits/chosen: -0.9715

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
- training_steps: 250

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.7075        | 0.0489 | 50   | 0.6367          | 0.2363         | 0.0705           | 0.6571             | 0.1658          | -21.1755       | -17.7501     | -0.9379         | -0.9373       |
| 0.6451        | 0.0977 | 100  | 0.6114          | -0.8886        | -1.7629          | 0.6923             | 0.8743          | -24.8423       | -19.9998     | -0.9999         | -0.9992       |
| 0.7372        | 0.1466 | 150  | 0.5770          | -1.9159        | -3.2984          | 0.7253             | 1.3825          | -27.9133       | -22.0544     | -0.9880         | -0.9871       |
| 0.4401        | 0.1954 | 200  | 0.5109          | -0.9476        | -2.5465          | 0.7516             | 1.5989          | -26.4095       | -20.1178     | -0.9750         | -0.9738       |
| 0.6774        | 0.2443 | 250  | 0.5035          | -0.9245        | -2.5465          | 0.7626             | 1.6220          | -26.4095       | -20.0716     | -0.9727         | -0.9715       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
