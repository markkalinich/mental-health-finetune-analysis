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
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-original-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-original-baseline

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0781
- Precision: 0.7781
- Recall: 0.7340
- Micro F1: 0.7554
- Weighted F1: 0.7556
- Macro F1: 0.7644
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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.2543        | 1.0   | 263  | 0.0644          | 0.5921    | 0.7041 | 0.6433   | 0.6467      | 0.6645   | 0.9780   |
| 0.0431        | 2.0   | 526  | 0.0552          | 0.7567    | 0.7212 | 0.7385   | 0.7393      | 0.7535   | 0.9831   |
| 0.0276        | 3.0   | 789  | 0.0620          | 0.7469    | 0.7309 | 0.7388   | 0.7394      | 0.7512   | 0.9830   |
| 0.0205        | 4.0   | 1052 | 0.0659          | 0.7208    | 0.7450 | 0.7327   | 0.7336      | 0.7460   | 0.9826   |
| 0.0155        | 5.0   | 1315 | 0.0723          | 0.7879    | 0.6980 | 0.7402   | 0.7400      | 0.7445   | 0.9827   |
| 0.0121        | 6.0   | 1578 | 0.0781          | 0.7921    | 0.6882 | 0.7365   | 0.7363      | 0.7500   | 0.9826   |
| 0.01          | 7.0   | 1841 | 0.0764          | 0.7421    | 0.7566 | 0.7492   | 0.7502      | 0.7637   | 0.9831   |
| 0.0075        | 8.0   | 2104 | 0.0776          | 0.7781    | 0.7340 | 0.7554   | 0.7556      | 0.7644   | 0.9839   |
| 0.0064        | 9.0   | 2367 | 0.0948          | 0.7336    | 0.7376 | 0.7356   | 0.7368      | 0.7521   | 0.9826   |
| 0.0052        | 10.0  | 2630 | 0.0955          | 0.7751    | 0.7151 | 0.7439   | 0.7439      | 0.7472   | 0.9832   |
| 0.0044        | 11.0  | 2893 | 0.0971          | 0.7765    | 0.7163 | 0.7452   | 0.7454      | 0.7584   | 0.9833   |
| 0.0038        | 12.0  | 3156 | 0.1015          | 0.7689    | 0.7126 | 0.7397   | 0.7400      | 0.7538   | 0.9830   |
| 0.0034        | 13.0  | 3419 | 0.1003          | 0.7456    | 0.7437 | 0.7447   | 0.7454      | 0.7576   | 0.9829   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
