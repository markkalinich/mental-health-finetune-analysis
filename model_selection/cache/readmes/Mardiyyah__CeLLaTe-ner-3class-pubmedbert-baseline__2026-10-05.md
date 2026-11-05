---
library_name: transformers
language:
- en
license: apache-2.0
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-pubmedbert-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-baseline

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0937
- Precision: 0.7710
- Recall: 0.7657
- Micro F1: 0.7683
- Weighted F1: 0.7676
- Macro F1: 0.7635
- Accuracy: 0.9829

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
| 0.3705        | 1.0   | 263  | 0.0792          | 0.5993    | 0.5731 | 0.5859   | 0.5783      | 0.5607   | 0.9768   |
| 0.0578        | 2.0   | 526  | 0.0633          | 0.7420    | 0.7080 | 0.7246   | 0.7253      | 0.7222   | 0.9811   |
| 0.0353        | 3.0   | 789  | 0.0655          | 0.7232    | 0.7631 | 0.7427   | 0.7433      | 0.7416   | 0.9814   |
| 0.0254        | 4.0   | 1052 | 0.0807          | 0.7882    | 0.7189 | 0.7520   | 0.7506      | 0.7452   | 0.9826   |
| 0.0185        | 5.0   | 1315 | 0.0739          | 0.7351    | 0.7423 | 0.7387   | 0.7391      | 0.7358   | 0.9817   |
| 0.0142        | 6.0   | 1578 | 0.0854          | 0.7131    | 0.7454 | 0.7289   | 0.7296      | 0.7261   | 0.9806   |
| 0.0104        | 7.0   | 1841 | 0.0873          | 0.7697    | 0.7340 | 0.7514   | 0.7506      | 0.7474   | 0.9821   |
| 0.0087        | 8.0   | 2104 | 0.0934          | 0.7337    | 0.7501 | 0.7418   | 0.7421      | 0.7403   | 0.9819   |
| 0.007         | 9.0   | 2367 | 0.0942          | 0.7710    | 0.7657 | 0.7683   | 0.7676      | 0.7635   | 0.9829   |
| 0.0059        | 10.0  | 2630 | 0.1017          | 0.7619    | 0.7231 | 0.7420   | 0.7416      | 0.7401   | 0.9820   |
| 0.005         | 11.0  | 2893 | 0.0984          | 0.7645    | 0.7454 | 0.7549   | 0.7539      | 0.7518   | 0.9826   |
| 0.0041        | 12.0  | 3156 | 0.1118          | 0.7495    | 0.7179 | 0.7333   | 0.7337      | 0.7322   | 0.9817   |
| 0.0033        | 13.0  | 3419 | 0.1136          | 0.7599    | 0.7480 | 0.7539   | 0.7536      | 0.7533   | 0.9825   |
| 0.0033        | 14.0  | 3682 | 0.1180          | 0.7431    | 0.7272 | 0.7351   | 0.7353      | 0.7351   | 0.9814   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
