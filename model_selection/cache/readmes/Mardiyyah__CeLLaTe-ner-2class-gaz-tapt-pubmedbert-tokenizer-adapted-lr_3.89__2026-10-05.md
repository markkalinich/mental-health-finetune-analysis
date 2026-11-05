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
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-lr_3.89
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-lr_3.89

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1105
- Precision: 0.7896
- Recall: 0.7739
- Micro F1: 0.7817
- Weighted F1: 0.7817
- Macro F1: 0.7909
- Accuracy: 0.9848

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.88548620843886e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.1398        | 1.0   | 1052  | 0.0580          | 0.7841    | 0.7252 | 0.7535   | 0.7535      | 0.7593   | 0.9837   |
| 0.0133        | 2.0   | 2104  | 0.0898          | 0.8013    | 0.7156 | 0.7560   | 0.7561      | 0.7671   | 0.9830   |
| 0.0055        | 3.0   | 3156  | 0.0827          | 0.7449    | 0.7691 | 0.7568   | 0.7575      | 0.7664   | 0.9833   |
| 0.0033        | 4.0   | 4208  | 0.0922          | 0.7710    | 0.7673 | 0.7691   | 0.7695      | 0.7816   | 0.9833   |
| 0.0025        | 5.0   | 5260  | 0.1085          | 0.7804    | 0.7565 | 0.7682   | 0.7683      | 0.7746   | 0.9836   |
| 0.002         | 6.0   | 6312  | 0.1012          | 0.7859    | 0.7330 | 0.7586   | 0.7588      | 0.7672   | 0.9839   |
| 0.0017        | 7.0   | 7364  | 0.1165          | 0.8013    | 0.7589 | 0.7795   | 0.7794      | 0.7888   | 0.9842   |
| 0.0013        | 8.0   | 8416  | 0.1158          | 0.7699    | 0.7685 | 0.7692   | 0.7691      | 0.7771   | 0.9836   |
| 0.0012        | 9.0   | 9468  | 0.1104          | 0.7896    | 0.7739 | 0.7817   | 0.7817      | 0.7909   | 0.9848   |
| 0.0008        | 10.0  | 10520 | 0.1309          | 0.8173    | 0.7480 | 0.7812   | 0.7811      | 0.7855   | 0.9845   |
| 0.0007        | 11.0  | 11572 | 0.1231          | 0.8021    | 0.7631 | 0.7821   | 0.7823      | 0.7876   | 0.9847   |
| 0.0007        | 12.0  | 12624 | 0.1358          | 0.7370    | 0.7565 | 0.7466   | 0.7481      | 0.7619   | 0.9820   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
