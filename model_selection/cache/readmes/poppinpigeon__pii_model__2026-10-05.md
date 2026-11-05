---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-cased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii_model

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1697
- Precision: 0.7304
- Recall: 0.8984
- F1: 0.8058
- Accuracy: 0.9758

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
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2421        | 1.0   | 3414  | 0.2070          | 0.5539    | 0.8584 | 0.6733 | 0.9510   |
| 0.1584        | 2.0   | 6828  | 0.1812          | 0.6582    | 0.8829 | 0.7542 | 0.9670   |
| 0.1230        | 3.0   | 10242 | 0.1622          | 0.6995    | 0.8972 | 0.7861 | 0.9711   |
| 0.0835        | 4.0   | 13656 | 0.1697          | 0.7304    | 0.8984 | 0.8058 | 0.9758   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
