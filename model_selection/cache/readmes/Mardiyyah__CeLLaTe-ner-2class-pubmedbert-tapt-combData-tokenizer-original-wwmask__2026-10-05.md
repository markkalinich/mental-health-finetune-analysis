---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask-combinedData
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-original-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-original-wwmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0575
- Precision: 0.7786
- Recall: 0.7425
- Micro F1: 0.7601
- Weighted F1: 0.7604
- Macro F1: 0.7695
- Accuracy: 0.9837

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
| 0.2519        | 1.0   | 263  | 0.0564          | 0.6725    | 0.7328 | 0.7013   | 0.7036      | 0.7220   | 0.9819   |
| 0.0404        | 2.0   | 526  | 0.0539          | 0.7758    | 0.7200 | 0.7468   | 0.7471      | 0.7581   | 0.9835   |
| 0.0266        | 3.0   | 789  | 0.0572          | 0.7786    | 0.7425 | 0.7601   | 0.7604      | 0.7695   | 0.9837   |
| 0.0196        | 4.0   | 1052 | 0.0613          | 0.7573    | 0.7462 | 0.7517   | 0.7521      | 0.7605   | 0.9841   |
| 0.0147        | 5.0   | 1315 | 0.0699          | 0.7933    | 0.7261 | 0.7582   | 0.7582      | 0.7621   | 0.9838   |
| 0.0119        | 6.0   | 1578 | 0.0740          | 0.7395    | 0.6980 | 0.7181   | 0.7181      | 0.7158   | 0.9825   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
