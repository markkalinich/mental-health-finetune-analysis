---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: modernBERT_suicide_base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernBERT_suicide_base

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4768
- Accuracy: 0.8802
- Precision: 0.8799
- Recall: 0.8802
- F1: 0.8800

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
- train_batch_size: 25
- eval_batch_size: 25
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_8BIT with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.2679        | 1.0   | 8911  | 0.2684          | 0.8847   | 0.8882    | 0.8847 | 0.8840 |
| 0.2075        | 2.0   | 17822 | 0.2836          | 0.8882   | 0.8879    | 0.8882 | 0.8881 |
| 0.0985        | 3.0   | 26733 | 0.4768          | 0.8802   | 0.8799    | 0.8802 | 0.8800 |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
