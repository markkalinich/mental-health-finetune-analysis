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
- name: CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-adapted-spanmask-lr_2.16
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-adapted-spanmask-lr_2.16

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0715
- Precision: 0.8024
- Recall: 0.7348
- Micro F1: 0.7671
- Weighted F1: 0.7668
- Macro F1: 0.7754
- Accuracy: 0.9841

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
| 0.2892        | 1.0   | 263  | 0.0692          | 0.5629    | 0.6542 | 0.6051   | 0.6075      | 0.6199   | 0.9759   |
| 0.0413        | 2.0   | 526  | 0.0550          | 0.7616    | 0.7126 | 0.7363   | 0.7363      | 0.7451   | 0.9832   |
| 0.026         | 3.0   | 789  | 0.0601          | 0.7599    | 0.7156 | 0.7371   | 0.7373      | 0.7447   | 0.9830   |
| 0.018         | 4.0   | 1052 | 0.0711          | 0.7861    | 0.7029 | 0.7422   | 0.7422      | 0.7481   | 0.9829   |
| 0.013         | 5.0   | 1315 | 0.0725          | 0.8024    | 0.7348 | 0.7671   | 0.7668      | 0.7754   | 0.9841   |
| 0.0105        | 6.0   | 1578 | 0.0767          | 0.7937    | 0.7288 | 0.7599   | 0.7597      | 0.7663   | 0.9839   |
| 0.0075        | 7.0   | 1841 | 0.0791          | 0.7409    | 0.7565 | 0.7486   | 0.7486      | 0.7490   | 0.9831   |
| 0.0065        | 8.0   | 2104 | 0.0835          | 0.7658    | 0.7511 | 0.7583   | 0.7584      | 0.7656   | 0.9836   |
| 0.0054        | 9.0   | 2367 | 0.0838          | 0.7370    | 0.7649 | 0.7507   | 0.7512      | 0.7607   | 0.9832   |
| 0.0043        | 10.0  | 2630 | 0.0954          | 0.7796    | 0.7318 | 0.7550   | 0.7550      | 0.7616   | 0.9838   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
