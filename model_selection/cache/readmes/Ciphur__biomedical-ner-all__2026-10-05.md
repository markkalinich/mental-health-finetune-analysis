---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biomedical-ner-all
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biomedical-ner-all

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2652
- Precision: 0.5986
- Recall: 0.6849
- F1: 0.6388
- Accuracy: 0.9246

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
| No log        | 1.0   | 125  | 0.2443          | 0.5849    | 0.6930 | 0.6344 | 0.9231   |
| No log        | 2.0   | 250  | 0.2578          | 0.6041    | 0.6849 | 0.6420 | 0.9252   |
| No log        | 3.0   | 375  | 0.2652          | 0.5986    | 0.6849 | 0.6388 | 0.9246   |


### Framework versions

- Transformers 4.47.1
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
