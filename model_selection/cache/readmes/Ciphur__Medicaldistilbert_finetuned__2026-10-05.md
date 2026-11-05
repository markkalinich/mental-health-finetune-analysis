---
library_name: transformers
base_model: Gaborandi/Medicaldistilbert
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Medicaldistilbert_finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Medicaldistilbert_finetuned

This model is a fine-tuned version of [Gaborandi/Medicaldistilbert](https://huggingface.co/Gaborandi/Medicaldistilbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2582
- Precision: 0.5383
- Recall: 0.6047
- F1: 0.5696
- Accuracy: 0.9166

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 125  | 0.3249          | 0.4618    | 0.4849 | 0.4731 | 0.9000   |
| No log        | 2.0   | 250  | 0.2673          | 0.5274    | 0.5930 | 0.5583 | 0.9151   |
| No log        | 3.0   | 375  | 0.2582          | 0.5383    | 0.6047 | 0.5696 | 0.9166   |


### Framework versions

- Transformers 4.47.1
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
