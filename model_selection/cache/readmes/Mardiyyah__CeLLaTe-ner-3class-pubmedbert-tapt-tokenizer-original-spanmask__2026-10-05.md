---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-original-spanmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-original-spanmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1137
- Precision: 0.7609
- Recall: 0.7553
- Micro F1: 0.7581
- Weighted F1: 0.7577
- Macro F1: 0.7544
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
| 0.3682        | 1.0   | 263  | 0.0777          | 0.5310    | 0.6283 | 0.5756   | 0.5686      | 0.5479   | 0.9754   |
| 0.056         | 2.0   | 526  | 0.0636          | 0.7462    | 0.7100 | 0.7277   | 0.7276      | 0.7262   | 0.9812   |
| 0.0351        | 3.0   | 789  | 0.0682          | 0.7267    | 0.7309 | 0.7288   | 0.7294      | 0.7271   | 0.9809   |
| 0.0242        | 4.0   | 1052 | 0.0756          | 0.7670    | 0.7163 | 0.7408   | 0.7400      | 0.7365   | 0.9819   |
| 0.0185        | 5.0   | 1315 | 0.0741          | 0.7752    | 0.7179 | 0.7454   | 0.7455      | 0.7425   | 0.9820   |
| 0.0144        | 6.0   | 1578 | 0.0816          | 0.7153    | 0.7350 | 0.7250   | 0.7250      | 0.7224   | 0.9808   |
| 0.0112        | 7.0   | 1841 | 0.0887          | 0.7523    | 0.7288 | 0.7403   | 0.7389      | 0.7359   | 0.9818   |
| 0.0091        | 8.0   | 2104 | 0.0913          | 0.7351    | 0.7236 | 0.7293   | 0.7299      | 0.7290   | 0.9812   |
| 0.0078        | 9.0   | 2367 | 0.0939          | 0.7615    | 0.7397 | 0.7505   | 0.7497      | 0.7463   | 0.9820   |
| 0.0066        | 10.0  | 2630 | 0.1002          | 0.7700    | 0.7163 | 0.7422   | 0.7414      | 0.7388   | 0.9818   |
| 0.0056        | 11.0  | 2893 | 0.1002          | 0.7560    | 0.7356 | 0.7456   | 0.7450      | 0.7413   | 0.9818   |
| 0.0049        | 12.0  | 3156 | 0.1047          | 0.7563    | 0.7543 | 0.7553   | 0.7554      | 0.7513   | 0.9822   |
| 0.0042        | 13.0  | 3419 | 0.1077          | 0.7561    | 0.7522 | 0.7542   | 0.7532      | 0.7495   | 0.9822   |
| 0.0037        | 14.0  | 3682 | 0.1076          | 0.7651    | 0.7408 | 0.7527   | 0.7522      | 0.7482   | 0.9821   |
| 0.0032        | 15.0  | 3945 | 0.1100          | 0.7404    | 0.7616 | 0.7508   | 0.7504      | 0.7470   | 0.9818   |
| 0.0027        | 16.0  | 4208 | 0.1098          | 0.7575    | 0.7527 | 0.7551   | 0.7548      | 0.7516   | 0.9823   |
| 0.0025        | 17.0  | 4471 | 0.1143          | 0.7635    | 0.7376 | 0.7503   | 0.7500      | 0.7474   | 0.9819   |
| 0.0024        | 18.0  | 4734 | 0.1145          | 0.7444    | 0.7548 | 0.7495   | 0.7493      | 0.7468   | 0.9818   |
| 0.002         | 19.0  | 4997 | 0.1141          | 0.7609    | 0.7553 | 0.7581   | 0.7577      | 0.7544   | 0.9823   |
| 0.002         | 20.0  | 5260 | 0.1137          | 0.7578    | 0.7574 | 0.7576   | 0.7573      | 0.7538   | 0.9821   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
