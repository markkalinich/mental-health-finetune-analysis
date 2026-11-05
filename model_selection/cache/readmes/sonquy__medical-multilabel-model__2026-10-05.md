---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- precision
- recall
model-index:
- name: medical-multilabel-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-multilabel-model

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0130
- F1 Micro: 0.9902
- F1 Macro: 0.7392
- Precision: 0.9910
- Recall: 0.9894

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
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1 Micro | F1 Macro | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|:---------:|:------:|
| 0.0238        | 1.0   | 945  | 0.0184          | 0.9868   | 0.7384   | 0.9878    | 0.9857 |
| 0.0146        | 2.0   | 1890 | 0.0136          | 0.9902   | 0.7387   | 0.9910    | 0.9894 |
| 0.0062        | 3.0   | 2835 | 0.0130          | 0.9902   | 0.7392   | 0.9910    | 0.9894 |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.1
