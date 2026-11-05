---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: medical-multiclass-drug-review
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-multiclass-drug-review

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3471
- Precision: 0.6299
- Recall: 0.6792
- F1: 0.6322

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
- train_batch_size: 45
- eval_batch_size: 45
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|
| 2.9661        | 0.1992 | 500  | 2.1441          | 0.4077    | 0.5207 | 0.4254 |
| 1.931         | 0.3984 | 1000 | 1.6758          | 0.5516    | 0.6146 | 0.5495 |
| 1.6466        | 0.5976 | 1500 | 1.4787          | 0.6084    | 0.6530 | 0.5981 |
| 1.4647        | 0.7968 | 2000 | 1.3907          | 0.6206    | 0.6676 | 0.6154 |
| 1.3951        | 0.9960 | 2500 | 1.3471          | 0.6299    | 0.6792 | 0.6322 |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Tokenizers 0.21.0
