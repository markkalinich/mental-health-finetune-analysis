---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-small
tags:
- generated_from_trainer
metrics:
- f1
- recall
- precision
model-index:
- name: PII-Binary-Filter-Extreme-Recall-Fix
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Binary-Filter-Extreme-Recall-Fix

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1361
- F1: 0.9852
- Recall: 0.9879
- Precision: 0.9826
- Trash Caught: 0.6422

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
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Recall | Precision | Trash Caught |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:---------:|:------------:|
| No log        | 1.0   | 499  | 0.1403          | 0.9785 | 0.9953 | 0.9622    | 0.2018       |
| 0.3066        | 2.0   | 998  | 0.1123          | 0.9832 | 0.9908 | 0.9757    | 0.4954       |
| 0.179         | 3.0   | 1497 | 0.1188          | 0.9853 | 0.9910 | 0.9796    | 0.5780       |
| 0.1209        | 4.0   | 1996 | 0.1293          | 0.9857 | 0.9921 | 0.9794    | 0.5734       |
| 0.0834        | 5.0   | 2495 | 0.1361          | 0.9852 | 0.9879 | 0.9826    | 0.6422       |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu129
- Datasets 4.8.2
- Tokenizers 0.22.0
