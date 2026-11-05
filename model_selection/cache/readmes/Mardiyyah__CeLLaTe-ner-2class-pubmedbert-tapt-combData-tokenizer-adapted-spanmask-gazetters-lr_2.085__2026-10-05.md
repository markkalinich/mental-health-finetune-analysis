---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-adapted-spanmask-gazetters-lr_2.085
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-adapted-spanmask-gazetters-lr_2.085

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1298
- Precision: 0.7765
- Recall: 0.7565
- Micro F1: 0.7664
- Weighted F1: 0.7666
- Macro F1: 0.7751
- Accuracy: 0.9834

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.0854538798e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.2292        | 1.0   | 526   | 0.0584          | 0.7113    | 0.7246 | 0.7179   | 0.7179      | 0.7260   | 0.9820   |
| 0.0214        | 2.0   | 1052  | 0.0707          | 0.7297    | 0.7288 | 0.7292   | 0.7303      | 0.7454   | 0.9810   |
| 0.0098        | 3.0   | 1578  | 0.0807          | 0.7614    | 0.7408 | 0.7510   | 0.7513      | 0.7623   | 0.9829   |
| 0.0059        | 4.0   | 2104  | 0.0893          | 0.7757    | 0.7300 | 0.7522   | 0.7523      | 0.7564   | 0.9837   |
| 0.0034        | 5.0   | 2630  | 0.0959          | 0.7383    | 0.7462 | 0.7422   | 0.7427      | 0.7530   | 0.9821   |
| 0.0026        | 6.0   | 3156  | 0.0918          | 0.7337    | 0.7655 | 0.7493   | 0.7500      | 0.7612   | 0.9828   |
| 0.0017        | 7.0   | 3682  | 0.1079          | 0.7884    | 0.7282 | 0.7571   | 0.7571      | 0.7673   | 0.9830   |
| 0.0015        | 8.0   | 4208  | 0.1114          | 0.7600    | 0.7523 | 0.7561   | 0.7564      | 0.7643   | 0.9824   |
| 0.0013        | 9.0   | 4734  | 0.1166          | 0.7723    | 0.7300 | 0.7505   | 0.7504      | 0.7604   | 0.9825   |
| 0.0012        | 10.0  | 5260  | 0.1188          | 0.7682    | 0.7474 | 0.7577   | 0.7581      | 0.7684   | 0.9829   |
| 0.0009        | 11.0  | 5786  | 0.1239          | 0.7750    | 0.7354 | 0.7547   | 0.7551      | 0.7664   | 0.9830   |
| 0.0007        | 12.0  | 6312  | 0.1243          | 0.7693    | 0.7438 | 0.7563   | 0.7566      | 0.7644   | 0.9828   |
| 0.0007        | 13.0  | 6838  | 0.1241          | 0.7630    | 0.7571 | 0.7600   | 0.7603      | 0.7675   | 0.9832   |
| 0.0007        | 14.0  | 7364  | 0.1186          | 0.7677    | 0.7492 | 0.7584   | 0.7585      | 0.7667   | 0.9834   |
| 0.0006        | 15.0  | 7890  | 0.1225          | 0.7829    | 0.7438 | 0.7629   | 0.7632      | 0.7714   | 0.9840   |
| 0.0005        | 16.0  | 8416  | 0.1230          | 0.7648    | 0.7547 | 0.7597   | 0.7601      | 0.7693   | 0.9834   |
| 0.0004        | 17.0  | 8942  | 0.1321          | 0.7660    | 0.7577 | 0.7618   | 0.7621      | 0.7701   | 0.9835   |
| 0.0005        | 18.0  | 9468  | 0.1301          | 0.7668    | 0.7535 | 0.7601   | 0.7603      | 0.7675   | 0.9834   |
| 0.0004        | 19.0  | 9994  | 0.1292          | 0.7765    | 0.7565 | 0.7664   | 0.7666      | 0.7751   | 0.9834   |
| 0.0004        | 20.0  | 10520 | 0.1295          | 0.7682    | 0.7571 | 0.7626   | 0.7628      | 0.7714   | 0.9834   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
