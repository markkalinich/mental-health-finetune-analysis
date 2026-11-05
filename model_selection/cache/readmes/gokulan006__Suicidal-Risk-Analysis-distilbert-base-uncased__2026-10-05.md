---
library_name: transformers
license: apache-2.0
base_model: gokulan006/Suicidal-Risk-Analysis-distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: Suicidal-Risk-Analysis-DistilBert-base-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Suicidal-Risk-Analysis-DistilBert-base-uncased

This model is a fine-tuned version of [gokulan006/Suicidal-Risk-Analysis-distilbert-base-uncased](https://huggingface.co/gokulan006/Suicidal-Risk-Analysis-distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5168
- Accuracy: 0.8384

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.4205        | 1.0   | 659  | 0.3784          | 0.8346   |
| 0.2791        | 2.0   | 1318 | 0.3904          | 0.8456   |
| 0.1506        | 3.0   | 1977 | 0.5168          | 0.8384   |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 3.3.2
- Tokenizers 0.21.0
