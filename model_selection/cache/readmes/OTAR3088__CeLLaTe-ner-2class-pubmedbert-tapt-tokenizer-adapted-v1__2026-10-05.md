---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v1
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe-ner-pubmedbert-tapt-tokenizer-adapted-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-pubmedbert-tapt-tokenizer-adapted-v1

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v1](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v1) on the OTAR3088/CeLLaTe_V3.2_contracted_ent_IOB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0835
- Precision: 0.7576
- Recall: 0.7549
- F1: 0.7563
- Accuracy: 0.9839

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2074        | 1.0   | 263  | 0.0588          | 0.6478    | 0.7310 | 0.6869 | 0.9803   |
| 0.0367        | 2.0   | 526  | 0.0565          | 0.7551    | 0.7023 | 0.7278 | 0.9832   |
| 0.024         | 3.0   | 789  | 0.0621          | 0.6653    | 0.7567 | 0.7081 | 0.9801   |
| 0.0175        | 4.0   | 1052 | 0.0671          | 0.6734    | 0.7579 | 0.7132 | 0.9812   |
| 0.0134        | 5.0   | 1315 | 0.0716          | 0.7472    | 0.7119 | 0.7291 | 0.9828   |
| 0.0099        | 6.0   | 1578 | 0.0795          | 0.7686    | 0.7346 | 0.7512 | 0.9834   |
| 0.0074        | 7.0   | 1841 | 0.0830          | 0.7469    | 0.7513 | 0.7491 | 0.9831   |
| 0.0061        | 8.0   | 2104 | 0.0830          | 0.7576    | 0.7549 | 0.7563 | 0.9839   |
| 0.005         | 9.0   | 2367 | 0.0922          | 0.7511    | 0.7412 | 0.7461 | 0.9833   |
| 0.0046        | 10.0  | 2630 | 0.0887          | 0.7351    | 0.7579 | 0.7463 | 0.9834   |
| 0.0037        | 11.0  | 2893 | 0.0892          | 0.7469    | 0.7460 | 0.7464 | 0.9835   |
| 0.0031        | 12.0  | 3156 | 0.0978          | 0.7612    | 0.7430 | 0.7520 | 0.9835   |
| 0.0026        | 13.0  | 3419 | 0.0970          | 0.7609    | 0.7496 | 0.7552 | 0.9837   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
