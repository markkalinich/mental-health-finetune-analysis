---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-baseline

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1047
- Precision: 0.7835
- Recall: 0.7522
- Micro F1: 0.7675
- Weighted F1: 0.7666
- Macro F1: 0.7643
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
| 0.3679        | 1.0   | 263  | 0.0789          | 0.4712    | 0.6008 | 0.5282   | 0.5197      | 0.4880   | 0.9736   |
| 0.0538        | 2.0   | 526  | 0.0651          | 0.7420    | 0.6891 | 0.7146   | 0.7151      | 0.7143   | 0.9804   |
| 0.0329        | 3.0   | 789  | 0.0689          | 0.7382    | 0.7276 | 0.7328   | 0.7325      | 0.7328   | 0.9810   |
| 0.0237        | 4.0   | 1052 | 0.0760          | 0.7631    | 0.7337 | 0.7481   | 0.7481      | 0.7450   | 0.9822   |
| 0.0179        | 5.0   | 1315 | 0.0790          | 0.7829    | 0.7142 | 0.7470   | 0.7458      | 0.7439   | 0.9817   |
| 0.0142        | 6.0   | 1578 | 0.0817          | 0.7412    | 0.7276 | 0.7343   | 0.7350      | 0.7334   | 0.9808   |
| 0.011         | 7.0   | 1841 | 0.0875          | 0.7792    | 0.7496 | 0.7641   | 0.7638      | 0.7590   | 0.9826   |
| 0.0089        | 8.0   | 2104 | 0.0950          | 0.7790    | 0.7270 | 0.7521   | 0.7507      | 0.7470   | 0.9818   |
| 0.0074        | 9.0   | 2367 | 0.0873          | 0.7235    | 0.7681 | 0.7451   | 0.7453      | 0.7421   | 0.9816   |
| 0.006         | 10.0  | 2630 | 0.1005          | 0.7952    | 0.7070 | 0.7485   | 0.7484      | 0.7466   | 0.9815   |
| 0.0056        | 11.0  | 2893 | 0.0980          | 0.7523    | 0.7589 | 0.7556   | 0.7556      | 0.7542   | 0.9825   |
| 0.0044        | 12.0  | 3156 | 0.1042          | 0.7835    | 0.7522 | 0.7675   | 0.7666      | 0.7643   | 0.9828   |
| 0.0039        | 13.0  | 3419 | 0.1070          | 0.7724    | 0.7558 | 0.7640   | 0.7630      | 0.7593   | 0.9828   |
| 0.0032        | 14.0  | 3682 | 0.1074          | 0.7870    | 0.7450 | 0.7654   | 0.7651      | 0.7625   | 0.9829   |
| 0.003         | 15.0  | 3945 | 0.1094          | 0.7823    | 0.7414 | 0.7613   | 0.7608      | 0.7583   | 0.9827   |
| 0.0025        | 16.0  | 4208 | 0.1091          | 0.7711    | 0.7589 | 0.7649   | 0.7650      | 0.7626   | 0.9829   |
| 0.0025        | 17.0  | 4471 | 0.1136          | 0.7805    | 0.7388 | 0.7591   | 0.7589      | 0.7571   | 0.9826   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
