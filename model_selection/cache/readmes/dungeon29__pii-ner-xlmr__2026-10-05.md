---
library_name: transformers
license: mit
base_model: xlm-roberta-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: pii-ner-xlmr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-ner-xlmr

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0001
- Precision: 1.0
- Recall: 1.0
- F1: 1.0

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
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1  |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:---:|
| No log        | 1.0   | 169  | 0.0005          | 1.0       | 1.0    | 1.0 |
| No log        | 2.0   | 338  | 0.0002          | 1.0       | 1.0    | 1.0 |
| 0.059         | 3.0   | 507  | 0.0001          | 1.0       | 1.0    | 1.0 |
| 0.059         | 4.0   | 676  | 0.0001          | 1.0       | 1.0    | 1.0 |
| 0.059         | 5.0   | 845  | 0.0001          | 1.0       | 1.0    | 1.0 |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
