---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-adapted-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-adapted-wwmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0655
- Precision: 0.7687
- Recall: 0.7492
- Micro F1: 0.7588
- Weighted F1: 0.7590
- Macro F1: 0.7636
- Accuracy: 0.9842

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
| 0.2553        | 1.0   | 263  | 0.0633          | 0.5902    | 0.6236 | 0.6064   | 0.6057      | 0.5988   | 0.9792   |
| 0.0427        | 2.0   | 526  | 0.0594          | 0.6989    | 0.6657 | 0.6819   | 0.6829      | 0.6965   | 0.9811   |
| 0.0265        | 3.0   | 789  | 0.0603          | 0.7281    | 0.7246 | 0.7263   | 0.7270      | 0.7438   | 0.9831   |
| 0.0197        | 4.0   | 1052 | 0.0630          | 0.7325    | 0.7342 | 0.7333   | 0.7341      | 0.7445   | 0.9836   |
| 0.0145        | 5.0   | 1315 | 0.0775          | 0.7895    | 0.6723 | 0.7262   | 0.7260      | 0.7341   | 0.9822   |
| 0.0121        | 6.0   | 1578 | 0.0651          | 0.7687    | 0.7492 | 0.7588   | 0.7590      | 0.7636   | 0.9842   |
| 0.0092        | 7.0   | 1841 | 0.0725          | 0.7509    | 0.7450 | 0.7480   | 0.7481      | 0.7521   | 0.9842   |
| 0.0072        | 8.0   | 2104 | 0.0704          | 0.7529    | 0.7402 | 0.7465   | 0.7466      | 0.7496   | 0.9842   |
| 0.0061        | 9.0   | 2367 | 0.0805          | 0.7371    | 0.7468 | 0.7419   | 0.7426      | 0.7535   | 0.9834   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
