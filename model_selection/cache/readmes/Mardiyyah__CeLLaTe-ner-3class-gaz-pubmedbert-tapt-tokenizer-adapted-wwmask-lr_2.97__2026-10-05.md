---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-gaz-pubmedbert-tapt-tokenizer-adapted-wwmask-lr_2.97
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-gaz-pubmedbert-tapt-tokenizer-adapted-wwmask-lr_2.97

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0937
- Precision: 0.7856
- Recall: 0.7352
- Micro F1: 0.7596
- Weighted F1: 0.7582
- Macro F1: 0.7533
- Accuracy: 0.9818

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.9725312443452025e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 17
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.4536        | 1.0   | 526  | 0.0712          | 0.7031    | 0.6562 | 0.6789   | 0.6779      | 0.6779   | 0.9779   |
| 0.0369        | 2.0   | 1052 | 0.0740          | 0.6889    | 0.7635 | 0.7243   | 0.7242      | 0.7182   | 0.9789   |
| 0.0178        | 3.0   | 1578 | 0.0800          | 0.7306    | 0.7665 | 0.7481   | 0.7492      | 0.7444   | 0.9808   |
| 0.0087        | 4.0   | 2104 | 0.0944          | 0.7856    | 0.7352 | 0.7596   | 0.7582      | 0.7533   | 0.9818   |
| 0.0052        | 5.0   | 2630 | 0.1035          | 0.7248    | 0.7850 | 0.7537   | 0.7543      | 0.7511   | 0.9805   |
| 0.0035        | 6.0   | 3156 | 0.1189          | 0.7122    | 0.7809 | 0.7450   | 0.7459      | 0.7428   | 0.9807   |
| 0.0025        | 7.0   | 3682 | 0.1351          | 0.6583    | 0.7907 | 0.7184   | 0.7248      | 0.7195   | 0.9768   |
| 0.0019        | 8.0   | 4208 | 0.1232          | 0.7549    | 0.7476 | 0.7512   | 0.7519      | 0.7486   | 0.9810   |
| 0.0017        | 9.0   | 4734 | 0.1204          | 0.7406    | 0.7691 | 0.7546   | 0.7551      | 0.7518   | 0.9809   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
