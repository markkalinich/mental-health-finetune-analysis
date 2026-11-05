---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-reinit-llrd-pubmedbert-tapt-tokenizer-adapted_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-reinit-llrd-pubmedbert-tapt-tokenizer-adapted_v2

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5) on the Mardiyyah/CeLLaTe-ner-2class-iob dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0544
- Precision: 0.7312
- Recall: 0.7732
- Micro F1: 0.7516
- Weighted F1: 0.7523
- Macro F1: 0.7625
- Accuracy: 0.9832

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.3717        | 1.0   | 263  | 0.0624          | 0.5971    | 0.6721 | 0.6324   | 0.6309      | 0.6170   | 0.9800   |
| 0.0438        | 2.0   | 526  | 0.0545          | 0.7312    | 0.7732 | 0.7516   | 0.7523      | 0.7625   | 0.9832   |
| 0.0257        | 3.0   | 789  | 0.0602          | 0.7486    | 0.7448 | 0.7467   | 0.7477      | 0.7609   | 0.9820   |
| 0.0174        | 4.0   | 1052 | 0.0665          | 0.7733    | 0.7176 | 0.7444   | 0.7449      | 0.7557   | 0.9828   |
| 0.0123        | 5.0   | 1315 | 0.0693          | 0.7665    | 0.7195 | 0.7423   | 0.7425      | 0.7527   | 0.9830   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
