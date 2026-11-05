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
- name: CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-wwmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1088
- Precision: 0.7777
- Recall: 0.7486
- Micro F1: 0.7629
- Weighted F1: 0.7629
- Macro F1: 0.7610
- Accuracy: 0.9827

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
| 0.3641        | 1.0   | 263  | 0.0826          | 0.4130    | 0.5639 | 0.4768   | 0.4655      | 0.4346   | 0.9706   |
| 0.0551        | 2.0   | 526  | 0.0661          | 0.7539    | 0.6901 | 0.7206   | 0.7214      | 0.7225   | 0.9804   |
| 0.0337        | 3.0   | 789  | 0.0691          | 0.7195    | 0.7291 | 0.7243   | 0.7249      | 0.7265   | 0.9804   |
| 0.024         | 4.0   | 1052 | 0.0729          | 0.7382    | 0.7409 | 0.7396   | 0.7408      | 0.7365   | 0.9820   |
| 0.018         | 5.0   | 1315 | 0.0756          | 0.7594    | 0.7255 | 0.7421   | 0.7416      | 0.7391   | 0.9820   |
| 0.0142        | 6.0   | 1578 | 0.0841          | 0.7311    | 0.7029 | 0.7167   | 0.7181      | 0.7170   | 0.9805   |
| 0.0113        | 7.0   | 1841 | 0.0863          | 0.7524    | 0.7373 | 0.7448   | 0.7446      | 0.7422   | 0.9818   |
| 0.009         | 8.0   | 2104 | 0.1002          | 0.7748    | 0.7219 | 0.7474   | 0.7466      | 0.7432   | 0.9817   |
| 0.0076        | 9.0   | 2367 | 0.0939          | 0.7224    | 0.7558 | 0.7387   | 0.7394      | 0.7355   | 0.9814   |
| 0.0062        | 10.0  | 2630 | 0.1031          | 0.7734    | 0.7111 | 0.7410   | 0.7406      | 0.7376   | 0.9816   |
| 0.0052        | 11.0  | 2893 | 0.1002          | 0.7541    | 0.7491 | 0.7516   | 0.7522      | 0.7501   | 0.9821   |
| 0.0045        | 12.0  | 3156 | 0.1076          | 0.7888    | 0.7224 | 0.7542   | 0.7539      | 0.7499   | 0.9822   |
| 0.0037        | 13.0  | 3419 | 0.1055          | 0.7465    | 0.7614 | 0.7539   | 0.7542      | 0.7509   | 0.9822   |
| 0.0032        | 14.0  | 3682 | 0.1055          | 0.7506    | 0.7553 | 0.7529   | 0.7536      | 0.7528   | 0.9821   |
| 0.0034        | 15.0  | 3945 | 0.1093          | 0.7777    | 0.7486 | 0.7629   | 0.7629      | 0.7610   | 0.9827   |
| 0.0026        | 16.0  | 4208 | 0.1095          | 0.7499    | 0.7630 | 0.7564   | 0.7568      | 0.7538   | 0.9827   |
| 0.0025        | 17.0  | 4471 | 0.1138          | 0.7688    | 0.7491 | 0.7588   | 0.7586      | 0.7571   | 0.9825   |
| 0.0021        | 18.0  | 4734 | 0.1145          | 0.7560    | 0.7568 | 0.7564   | 0.7566      | 0.7541   | 0.9825   |
| 0.002         | 19.0  | 4997 | 0.1149          | 0.7668    | 0.7542 | 0.7605   | 0.7603      | 0.7586   | 0.9828   |
| 0.0019        | 20.0  | 5260 | 0.1132          | 0.7706    | 0.7532 | 0.7618   | 0.7617      | 0.7597   | 0.9827   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
