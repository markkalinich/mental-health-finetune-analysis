---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- f1
- precision
- recall
model-index:
- name: distilbert-pii-cpu-quick
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-pii-cpu-quick

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2772
- F1: 0.0
- Precision: 0.0
- Recall: 0.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1  | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:---:|:---------:|:------:|
| 8.1778        | 1.0   | 32   | 1.2772          | 0.0 | 0.0       | 0.0    |


### Framework versions

- Transformers 5.6.2
- Pytorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2
