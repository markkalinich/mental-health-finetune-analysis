---
library_name: transformers
license: mit
base_model: FacebookAI/roberta-large
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: roberta-cbl-Empathy-goodareas-eval_FeedbackESConv5pp_CARE10pp-sweeps-current
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-cbl-Empathy-goodareas-eval_FeedbackESConv5pp_CARE10pp-sweeps-current

This model is a fine-tuned version of [FacebookAI/roberta-large](https://huggingface.co/FacebookAI/roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4714
- Accuracy: 0.8023
- Precision: 0.6350
- Recall: 0.8735
- F1: 0.7354

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.669740264596789e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.5351        | 1.0   | 243  | 0.4195          | 0.8151   | 0.7095    | 0.6980 | 0.7037 |
| 0.4572        | 2.0   | 486  | 0.4694          | 0.7189   | 0.5294    | 0.9551 | 0.6812 |
| 0.3823        | 3.0   | 729  | 0.4196          | 0.8010   | 0.6398    | 0.8408 | 0.7266 |
| 0.301         | 4.0   | 972  | 0.4714          | 0.8023   | 0.6350    | 0.8735 | 0.7354 |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 2.21.0
- Tokenizers 0.21.0
