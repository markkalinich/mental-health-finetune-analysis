---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-original-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-original-wwmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0636
- Precision: 0.7605
- Recall: 0.7285
- Micro F1: 0.7442
- Weighted F1: 0.7446
- Macro F1: 0.7553
- Accuracy: 0.9835

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
| 0.2537        | 1.0   | 263  | 0.0665          | 0.6033    | 0.7413 | 0.6652   | 0.6696      | 0.6927   | 0.9772   |
| 0.041         | 2.0   | 526  | 0.0556          | 0.7642    | 0.6821 | 0.7208   | 0.7210      | 0.7279   | 0.9822   |
| 0.0266        | 3.0   | 789  | 0.0593          | 0.7544    | 0.7010 | 0.7268   | 0.7271      | 0.7365   | 0.9819   |
| 0.0198        | 4.0   | 1052 | 0.0638          | 0.7605    | 0.7285 | 0.7442   | 0.7446      | 0.7553   | 0.9835   |
| 0.0147        | 5.0   | 1315 | 0.0692          | 0.7707    | 0.7096 | 0.7389   | 0.7391      | 0.7488   | 0.9829   |
| 0.0121        | 6.0   | 1578 | 0.0718          | 0.7473    | 0.7145 | 0.7305   | 0.7305      | 0.7307   | 0.9827   |
| 0.009         | 7.0   | 1841 | 0.0781          | 0.7560    | 0.7297 | 0.7426   | 0.7428      | 0.7490   | 0.9832   |
| 0.0067        | 8.0   | 2104 | 0.0846          | 0.7492    | 0.7291 | 0.7390   | 0.7392      | 0.7508   | 0.9827   |
| 0.0059        | 9.0   | 2367 | 0.0857          | 0.7403    | 0.7425 | 0.7414   | 0.7417      | 0.7493   | 0.9829   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
