---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-original-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-original-baseline

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1025
- Precision: 0.7597
- Recall: 0.7668
- Micro F1: 0.7632
- Weighted F1: 0.7630
- Macro F1: 0.7601
- Accuracy: 0.9828

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.3737        | 1.0   | 263  | 0.0836          | 0.4317    | 0.5528 | 0.4848   | 0.4663      | 0.4325   | 0.9724   |
| 0.058         | 2.0   | 526  | 0.0618          | 0.7577    | 0.7194 | 0.7381   | 0.7389      | 0.7374   | 0.9817   |
| 0.0354        | 3.0   | 789  | 0.0668          | 0.7257    | 0.7439 | 0.7347   | 0.7351      | 0.7338   | 0.9815   |
| 0.0253        | 4.0   | 1052 | 0.0768          | 0.7587    | 0.7283 | 0.7432   | 0.7434      | 0.7413   | 0.9822   |
| 0.0192        | 5.0   | 1315 | 0.0715          | 0.7436    | 0.7397 | 0.7416   | 0.7425      | 0.7406   | 0.9822   |
| 0.0146        | 6.0   | 1578 | 0.0861          | 0.7437    | 0.7236 | 0.7335   | 0.7330      | 0.7331   | 0.9816   |
| 0.0115        | 7.0   | 1841 | 0.0891          | 0.7291    | 0.7480 | 0.7384   | 0.7381      | 0.7386   | 0.9816   |
| 0.0097        | 8.0   | 2104 | 0.0872          | 0.7146    | 0.7454 | 0.7297   | 0.7302      | 0.7303   | 0.9814   |
| 0.0077        | 9.0   | 2367 | 0.0889          | 0.7564    | 0.7595 | 0.7579   | 0.7576      | 0.7555   | 0.9832   |
| 0.007         | 10.0  | 2630 | 0.0963          | 0.7630    | 0.7272 | 0.7447   | 0.7443      | 0.7416   | 0.9824   |
| 0.0059        | 11.0  | 2893 | 0.0959          | 0.7547    | 0.7512 | 0.7529   | 0.7524      | 0.7504   | 0.9830   |
| 0.0052        | 12.0  | 3156 | 0.0986          | 0.7386    | 0.7501 | 0.7443   | 0.7447      | 0.7440   | 0.9823   |
| 0.0043        | 13.0  | 3419 | 0.1066          | 0.7792    | 0.7460 | 0.7622   | 0.7604      | 0.7575   | 0.9832   |
| 0.004         | 14.0  | 3682 | 0.1068          | 0.7691    | 0.7319 | 0.7501   | 0.7502      | 0.7501   | 0.9827   |
| 0.0033        | 15.0  | 3945 | 0.1027          | 0.7597    | 0.7668 | 0.7632   | 0.7630      | 0.7601   | 0.9828   |
| 0.0029        | 16.0  | 4208 | 0.1099          | 0.7618    | 0.7376 | 0.7495   | 0.7495      | 0.7474   | 0.9827   |
| 0.0028        | 17.0  | 4471 | 0.1089          | 0.7624    | 0.7434 | 0.7528   | 0.7528      | 0.7511   | 0.9826   |
| 0.0023        | 18.0  | 4734 | 0.1112          | 0.7470    | 0.7579 | 0.7525   | 0.7522      | 0.7501   | 0.9825   |
| 0.0022        | 19.0  | 4997 | 0.1105          | 0.7637    | 0.7553 | 0.7595   | 0.7589      | 0.7572   | 0.9831   |
| 0.0022        | 20.0  | 5260 | 0.1092          | 0.7569    | 0.7569 | 0.7569   | 0.7568      | 0.7548   | 0.9828   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
