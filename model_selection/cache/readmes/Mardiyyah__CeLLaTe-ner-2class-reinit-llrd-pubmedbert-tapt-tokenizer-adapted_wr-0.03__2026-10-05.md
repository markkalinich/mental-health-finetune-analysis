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
- f1
- accuracy
model-index:
- name: CeLLaTe-ner-2class-reinit-llrd-pubmedbert-tapt-tokenizer-adapted_wr-0.03
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-reinit-llrd-pubmedbert-tapt-tokenizer-adapted_wr-0.03

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5) on the OTAR3088/CeLLaTe_V3.2_contracted_ent_IOB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0534
- Precision: 0.7730
- Recall: 0.7240
- F1: 0.7477
- Accuracy: 0.9839

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
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.297         | 1.0   | 263  | 0.0691          | 0.5923    | 0.6299 | 0.6106 | 0.9761   |
| 0.0377        | 2.0   | 526  | 0.0533          | 0.7730    | 0.7240 | 0.7477 | 0.9839   |
| 0.0231        | 3.0   | 789  | 0.0625          | 0.7304    | 0.7347 | 0.7325 | 0.9822   |
| 0.0167        | 4.0   | 1052 | 0.0775          | 0.7609    | 0.7204 | 0.7401 | 0.9830   |
| 0.012         | 5.0   | 1315 | 0.0700          | 0.7373    | 0.7275 | 0.7324 | 0.9828   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
