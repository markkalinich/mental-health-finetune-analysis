---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-adapted-spanmask-gazetters-lr_2.16
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-adapted-spanmask-gazetters-lr_2.16

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0961
- Precision: 0.7974
- Recall: 0.7480
- Micro F1: 0.7720
- Weighted F1: 0.7721
- Macro F1: 0.7820
- Accuracy: 0.9845

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.1601722686e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.02
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.1486        | 1.0   | 1052 | 0.0586          | 0.7453    | 0.7372 | 0.7412   | 0.7418      | 0.7542   | 0.9827   |
| 0.0156        | 2.0   | 2104 | 0.0823          | 0.7314    | 0.7583 | 0.7446   | 0.7452      | 0.7589   | 0.9812   |
| 0.0066        | 3.0   | 3156 | 0.0874          | 0.7643    | 0.7486 | 0.7564   | 0.7567      | 0.7668   | 0.9825   |
| 0.0038        | 4.0   | 4208 | 0.0961          | 0.7974    | 0.7480 | 0.7720   | 0.7721      | 0.7820   | 0.9845   |
| 0.0026        | 5.0   | 5260 | 0.1134          | 0.6959    | 0.7829 | 0.7368   | 0.7374      | 0.7475   | 0.9806   |
| 0.0022        | 6.0   | 6312 | 0.1119          | 0.7533    | 0.7601 | 0.7567   | 0.7567      | 0.7583   | 0.9833   |
| 0.0015        | 7.0   | 7364 | 0.1115          | 0.7887    | 0.7589 | 0.7735   | 0.7735      | 0.7801   | 0.9838   |
| 0.0014        | 8.0   | 8416 | 0.1053          | 0.7406    | 0.7673 | 0.7537   | 0.7540      | 0.7626   | 0.9830   |
| 0.001         | 9.0   | 9468 | 0.1208          | 0.7591    | 0.7673 | 0.7632   | 0.7635      | 0.7730   | 0.9835   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
