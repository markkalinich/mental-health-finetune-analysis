---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline-combinedData
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-original-baseline-combinedData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-original-baseline-combinedData

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0842
- Precision: 0.7784
- Recall: 0.7370
- Micro F1: 0.7571
- Weighted F1: 0.7571
- Macro F1: 0.7673
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
| 0.257         | 1.0   | 263  | 0.0669          | 0.5942    | 0.7309 | 0.6555   | 0.6602      | 0.6845   | 0.9771   |
| 0.0412        | 2.0   | 526  | 0.0533          | 0.7798    | 0.7261 | 0.7520   | 0.7521      | 0.7611   | 0.9836   |
| 0.0264        | 3.0   | 789  | 0.0565          | 0.7631    | 0.7273 | 0.7448   | 0.7453      | 0.7555   | 0.9831   |
| 0.0194        | 4.0   | 1052 | 0.0638          | 0.7646    | 0.7431 | 0.7537   | 0.7540      | 0.7649   | 0.9840   |
| 0.0145        | 5.0   | 1315 | 0.0717          | 0.7304    | 0.7041 | 0.7170   | 0.7170      | 0.7160   | 0.9824   |
| 0.0116        | 6.0   | 1578 | 0.0709          | 0.7575    | 0.7071 | 0.7315   | 0.7317      | 0.7387   | 0.9829   |
| 0.0083        | 7.0   | 1841 | 0.0780          | 0.7672    | 0.7419 | 0.7543   | 0.7547      | 0.7651   | 0.9841   |
| 0.0064        | 8.0   | 2104 | 0.0834          | 0.7784    | 0.7370 | 0.7571   | 0.7571      | 0.7673   | 0.9841   |
| 0.0055        | 9.0   | 2367 | 0.0842          | 0.7390    | 0.7376 | 0.7383   | 0.7390      | 0.7503   | 0.9831   |
| 0.0044        | 10.0  | 2630 | 0.0937          | 0.7869    | 0.7029 | 0.7425   | 0.7428      | 0.7544   | 0.9833   |
| 0.004         | 11.0  | 2893 | 0.0913          | 0.7682    | 0.7218 | 0.7443   | 0.7450      | 0.7592   | 0.9838   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
