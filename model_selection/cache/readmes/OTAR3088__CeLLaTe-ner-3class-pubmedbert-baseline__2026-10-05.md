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
- Loss: 0.0923
- Precision: 0.7695
- Recall: 0.7647
- Micro F1: 0.7671
- Weighted F1: 0.7667
- Macro F1: 0.7626
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
| 0.3707        | 1.0   | 263  | 0.0799          | 0.6219    | 0.5815 | 0.6010   | 0.5923      | 0.5770   | 0.9770   |
| 0.0585        | 2.0   | 526  | 0.0618          | 0.7373    | 0.7246 | 0.7309   | 0.7313      | 0.7277   | 0.9815   |
| 0.0354        | 3.0   | 789  | 0.0642          | 0.7269    | 0.7647 | 0.7453   | 0.7451      | 0.7433   | 0.9818   |
| 0.0257        | 4.0   | 1052 | 0.0811          | 0.7938    | 0.7054 | 0.7470   | 0.7457      | 0.7406   | 0.9823   |
| 0.0192        | 5.0   | 1315 | 0.0726          | 0.7556    | 0.7324 | 0.7439   | 0.7433      | 0.7413   | 0.9821   |
| 0.0145        | 6.0   | 1578 | 0.0841          | 0.7036    | 0.7574 | 0.7295   | 0.7315      | 0.7282   | 0.9808   |
| 0.0108        | 7.0   | 1841 | 0.0896          | 0.7809    | 0.7330 | 0.7562   | 0.7536      | 0.7491   | 0.9824   |
| 0.0086        | 8.0   | 2104 | 0.0914          | 0.7442    | 0.7574 | 0.7508   | 0.7510      | 0.7500   | 0.9823   |
| 0.0071        | 9.0   | 2367 | 0.0928          | 0.7695    | 0.7647 | 0.7671   | 0.7667      | 0.7626   | 0.9829   |
| 0.0061        | 10.0  | 2630 | 0.1001          | 0.7536    | 0.7402 | 0.7468   | 0.7469      | 0.7463   | 0.9822   |
| 0.0053        | 11.0  | 2893 | 0.0949          | 0.7722    | 0.7517 | 0.7618   | 0.7611      | 0.7580   | 0.9828   |
| 0.0042        | 12.0  | 3156 | 0.1045          | 0.7545    | 0.7423 | 0.7484   | 0.7490      | 0.7484   | 0.9823   |
| 0.0034        | 13.0  | 3419 | 0.1130          | 0.7660    | 0.7548 | 0.7604   | 0.7597      | 0.7571   | 0.9827   |
| 0.0032        | 14.0  | 3682 | 0.1128          | 0.7572    | 0.7371 | 0.7470   | 0.7472      | 0.7465   | 0.9819   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
