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
- name: CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-spanmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-spanmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0801
- Precision: 0.7559
- Recall: 0.7419
- Micro F1: 0.7488
- Weighted F1: 0.7488
- Macro F1: 0.7453
- Accuracy: 0.9823

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
| 0.3793        | 1.0   | 263  | 0.0956          | 0.3836    | 0.5290 | 0.4447   | 0.4350      | 0.4047   | 0.9693   |
| 0.0599        | 2.0   | 526  | 0.0685          | 0.7314    | 0.6819 | 0.7058   | 0.7066      | 0.7070   | 0.9798   |
| 0.0349        | 3.0   | 789  | 0.0735          | 0.7028    | 0.7193 | 0.7110   | 0.7109      | 0.7115   | 0.9796   |
| 0.0246        | 4.0   | 1052 | 0.0803          | 0.7559    | 0.7419 | 0.7488   | 0.7488      | 0.7453   | 0.9823   |
| 0.0189        | 5.0   | 1315 | 0.0852          | 0.7606    | 0.7060 | 0.7323   | 0.7317      | 0.7285   | 0.9810   |
| 0.0146        | 6.0   | 1578 | 0.0929          | 0.7200    | 0.6875 | 0.7034   | 0.7040      | 0.6986   | 0.9796   |
| 0.0114        | 7.0   | 1841 | 0.0963          | 0.7157    | 0.7286 | 0.7221   | 0.7221      | 0.7224   | 0.9802   |
| 0.0089        | 8.0   | 2104 | 0.0995          | 0.7563    | 0.7291 | 0.7424   | 0.7415      | 0.7400   | 0.9817   |
| 0.0075        | 9.0   | 2367 | 0.0999          | 0.6893    | 0.7501 | 0.7184   | 0.7200      | 0.7201   | 0.9796   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
