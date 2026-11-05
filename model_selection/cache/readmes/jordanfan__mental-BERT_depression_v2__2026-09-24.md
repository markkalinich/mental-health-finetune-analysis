---
library_name: transformers
license: mit
base_model: djangodevloper/bert-base-sa-mental-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: mental-BERT_depression_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental-BERT_depression_v2

This model is a fine-tuned version of [djangodevloper/bert-base-sa-mental-uncased](https://huggingface.co/djangodevloper/bert-base-sa-mental-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5212
- Accuracy: 0.8065
- Precision: 0.8070
- Recall: 0.8065
- F1: 0.8063

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
| 0.5395        | 1.0   | 969  | 0.5389          | 0.7619   | 0.7997    | 0.7619 | 0.7485 |
| 0.3823        | 2.0   | 1938 | 0.4557          | 0.8034   | 0.8097    | 0.8034 | 0.8021 |
| 0.2691        | 3.0   | 2907 | 0.5212          | 0.8065   | 0.8070    | 0.8065 | 0.8063 |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 3.3.2
- Tokenizers 0.21.0
