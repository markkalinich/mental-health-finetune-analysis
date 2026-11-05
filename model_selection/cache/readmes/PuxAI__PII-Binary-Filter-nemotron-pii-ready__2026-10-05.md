---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: PII-Binary-Filter-nemotron-pii-ready
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Binary-Filter-nemotron-pii-ready

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1761
- Accuracy: 0.9329
- F1: 0.9587
- Precision: 0.9411
- Recall: 0.9770

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.332         | 1.0   | 813  | 0.2198          | 0.9132   | 0.9475 | 0.9155    | 0.9818 |
| 0.1767        | 2.0   | 1626 | 0.1796          | 0.9260   | 0.9540 | 0.9447    | 0.9636 |
| 0.1497        | 3.0   | 2439 | 0.1761          | 0.9329   | 0.9587 | 0.9411    | 0.9770 |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu129
- Datasets 4.8.2
- Tokenizers 0.22.0
