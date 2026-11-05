---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wholewordmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-wwmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wholewordmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wholewordmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1008
- Precision: 0.7676
- Recall: 0.7512
- Micro F1: 0.7593
- Weighted F1: 0.7583
- Macro F1: 0.7559
- Accuracy: 0.9828

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
| 0.3718        | 1.0   | 263  | 0.0794          | 0.5110    | 0.5659 | 0.5371   | 0.5271      | 0.5014   | 0.9751   |
| 0.058         | 2.0   | 526  | 0.0637          | 0.7644    | 0.7111 | 0.7368   | 0.7362      | 0.7354   | 0.9815   |
| 0.0355        | 3.0   | 789  | 0.0709          | 0.6875    | 0.7387 | 0.7122   | 0.7136      | 0.7147   | 0.9795   |
| 0.0254        | 4.0   | 1052 | 0.0747          | 0.7619    | 0.7194 | 0.7400   | 0.7391      | 0.7365   | 0.9818   |
| 0.0185        | 5.0   | 1315 | 0.0762          | 0.7787    | 0.7033 | 0.7391   | 0.7394      | 0.7382   | 0.9816   |
| 0.0152        | 6.0   | 1578 | 0.0899          | 0.7295    | 0.7215 | 0.7255   | 0.7261      | 0.7255   | 0.9807   |
| 0.0111        | 7.0   | 1841 | 0.0888          | 0.7619    | 0.7361 | 0.7487   | 0.7478      | 0.7451   | 0.9823   |
| 0.0088        | 8.0   | 2104 | 0.0928          | 0.7398    | 0.7251 | 0.7324   | 0.7322      | 0.7313   | 0.9814   |
| 0.0077        | 9.0   | 2367 | 0.0982          | 0.7728    | 0.7470 | 0.7597   | 0.7580      | 0.7545   | 0.9827   |
| 0.0067        | 10.0  | 2630 | 0.1019          | 0.7891    | 0.7205 | 0.7532   | 0.7521      | 0.7508   | 0.9826   |
| 0.0058        | 11.0  | 2893 | 0.1009          | 0.7676    | 0.7512 | 0.7593   | 0.7583      | 0.7559   | 0.9828   |
| 0.005         | 12.0  | 3156 | 0.0999          | 0.7545    | 0.7569 | 0.7557   | 0.7555      | 0.7537   | 0.9830   |
| 0.0043        | 13.0  | 3419 | 0.1139          | 0.7456    | 0.7507 | 0.7481   | 0.7475      | 0.7469   | 0.9822   |
| 0.004         | 14.0  | 3682 | 0.1113          | 0.7745    | 0.7277 | 0.7504   | 0.7498      | 0.7471   | 0.9820   |
| 0.0033        | 15.0  | 3945 | 0.1086          | 0.7469    | 0.7605 | 0.7537   | 0.7539      | 0.7525   | 0.9821   |
| 0.0029        | 16.0  | 4208 | 0.1117          | 0.7648    | 0.7480 | 0.7563   | 0.7561      | 0.7551   | 0.9825   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
