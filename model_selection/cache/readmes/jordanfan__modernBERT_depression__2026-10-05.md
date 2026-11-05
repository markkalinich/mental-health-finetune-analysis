---
library_name: transformers
license: apache-2.0
base_model: jordanfan/modernBERT_suicide_base
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: modernBERT_depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernBERT_depression

This model is a fine-tuned version of [jordanfan/modernBERT_suicide_base](https://huggingface.co/jordanfan/modernBERT_suicide_base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7165
- Accuracy: 0.7896
- Precision: 0.7903
- Recall: 0.7896
- F1: 0.7894

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_8BIT with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.5289        | 1.0   | 969  | 0.4738          | 0.7903   | 0.7977    | 0.7903 | 0.7874 |
| 0.3411        | 2.0   | 1938 | 0.4775          | 0.7996   | 0.8023    | 0.7996 | 0.7995 |
| 0.1693        | 3.0   | 2907 | 0.7165          | 0.7896   | 0.7903    | 0.7896 | 0.7894 |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 3.3.2
- Tokenizers 0.21.0
