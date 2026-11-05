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
- name: CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-adapted-spanmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-combData-tokenizer-adapted-spanmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0588
- Precision: 0.7672
- Recall: 0.7114
- Micro F1: 0.7382
- Weighted F1: 0.7384
- Macro F1: 0.7514
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
| 0.2486        | 1.0   | 263  | 0.0624          | 0.5508    | 0.6548 | 0.5984   | 0.5956      | 0.5780   | 0.9786   |
| 0.041         | 2.0   | 526  | 0.0544          | 0.7598    | 0.7132 | 0.7357   | 0.7361      | 0.7458   | 0.9837   |
| 0.026         | 3.0   | 789  | 0.0583          | 0.7672    | 0.7114 | 0.7382   | 0.7384      | 0.7514   | 0.9828   |
| 0.0191        | 4.0   | 1052 | 0.0628          | 0.7425    | 0.7336 | 0.7381   | 0.7381      | 0.7393   | 0.9834   |
| 0.0144        | 5.0   | 1315 | 0.0666          | 0.7521    | 0.7078 | 0.7292   | 0.7292      | 0.7289   | 0.9831   |
| 0.011         | 6.0   | 1578 | 0.0676          | 0.7408    | 0.7132 | 0.7267   | 0.7263      | 0.7158   | 0.9836   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
