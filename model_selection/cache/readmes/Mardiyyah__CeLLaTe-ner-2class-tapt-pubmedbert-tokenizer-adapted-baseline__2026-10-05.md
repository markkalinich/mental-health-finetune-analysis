---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-baseline

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1033
- Precision: 0.7748
- Recall: 0.7511
- Micro F1: 0.7627
- Weighted F1: 0.7629
- Macro F1: 0.7710
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
| 0.2517        | 1.0   | 263  | 0.0607          | 0.6137    | 0.7126 | 0.6594   | 0.6605      | 0.6689   | 0.9803   |
| 0.0415        | 2.0   | 526  | 0.0579          | 0.7598    | 0.6428 | 0.6964   | 0.6963      | 0.7083   | 0.9814   |
| 0.0258        | 3.0   | 789  | 0.0603          | 0.7432    | 0.7029 | 0.7225   | 0.7225      | 0.7281   | 0.9823   |
| 0.0191        | 4.0   | 1052 | 0.0663          | 0.7597    | 0.7168 | 0.7376   | 0.7378      | 0.7472   | 0.9833   |
| 0.0139        | 5.0   | 1315 | 0.0714          | 0.7843    | 0.6627 | 0.7184   | 0.7179      | 0.7321   | 0.9821   |
| 0.0113        | 6.0   | 1578 | 0.0680          | 0.7414    | 0.7498 | 0.7456   | 0.7456      | 0.7469   | 0.9839   |
| 0.0084        | 7.0   | 1841 | 0.0756          | 0.7463    | 0.7571 | 0.7516   | 0.7519      | 0.7570   | 0.9843   |
| 0.0068        | 8.0   | 2104 | 0.0803          | 0.7910    | 0.7192 | 0.7534   | 0.7532      | 0.7618   | 0.9839   |
| 0.0059        | 9.0   | 2367 | 0.0802          | 0.7426    | 0.7511 | 0.7468   | 0.7472      | 0.7567   | 0.9836   |
| 0.0046        | 10.0  | 2630 | 0.0930          | 0.7730    | 0.6921 | 0.7303   | 0.7303      | 0.7363   | 0.9830   |
| 0.0037        | 11.0  | 2893 | 0.0886          | 0.7566    | 0.7366 | 0.7465   | 0.7471      | 0.7592   | 0.9836   |
| 0.0034        | 12.0  | 3156 | 0.0906          | 0.7591    | 0.7408 | 0.7498   | 0.7504      | 0.7615   | 0.9842   |
| 0.0028        | 13.0  | 3419 | 0.0990          | 0.7645    | 0.7517 | 0.7580   | 0.7581      | 0.7657   | 0.9836   |
| 0.0025        | 14.0  | 3682 | 0.0980          | 0.7678    | 0.7336 | 0.7503   | 0.7505      | 0.7605   | 0.9835   |
| 0.0022        | 15.0  | 3945 | 0.0983          | 0.7619    | 0.7390 | 0.7503   | 0.7507      | 0.7616   | 0.9837   |
| 0.0019        | 16.0  | 4208 | 0.1007          | 0.7826    | 0.7402 | 0.7608   | 0.7609      | 0.7692   | 0.9843   |
| 0.0017        | 17.0  | 4471 | 0.1026          | 0.7831    | 0.7402 | 0.7611   | 0.7611      | 0.7685   | 0.9839   |
| 0.0017        | 18.0  | 4734 | 0.0992          | 0.7654    | 0.7492 | 0.7572   | 0.7575      | 0.7663   | 0.9841   |
| 0.0015        | 19.0  | 4997 | 0.1042          | 0.7748    | 0.7511 | 0.7627   | 0.7629      | 0.7710   | 0.9842   |
| 0.0015        | 20.0  | 5260 | 0.1044          | 0.7759    | 0.7432 | 0.7592   | 0.7594      | 0.7680   | 0.9840   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
