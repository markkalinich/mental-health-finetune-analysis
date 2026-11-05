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
- name: medical_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_model

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0121
- F1 Micro: 0.9921
- F1 Macro: 0.7438
- Precision: 0.9921
- Recall: 0.9921

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
| 0.0043        | 1.0   | 945  | 0.0121          | 0.9915   | 0.7427   | 0.9921    | 0.9910 |
| 0.0041        | 2.0   | 1890 | 0.0125          | 0.9915   | 0.7436   | 0.9915    | 0.9915 |
| 0.0022        | 3.0   | 2835 | 0.0121          | 0.9921   | 0.7438   | 0.9921    | 0.9921 |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu128
- Datasets 4.4.2
- Tokenizers 0.22.1
