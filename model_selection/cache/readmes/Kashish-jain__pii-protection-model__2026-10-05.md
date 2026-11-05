---
library_name: transformers
license: apache-2.0
base_model: Kashish-jain/pii-protection-model
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-protection-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-protection-model

This model is a fine-tuned version of [Kashish-jain/pii-protection-model](https://huggingface.co/Kashish-jain/pii-protection-model) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0211
- Precision: 0.9160
- Recall: 0.9729
- F1: 0.9436
- Accuracy: 0.9851

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0213        | 1.0   | 2500 | 0.0217          | 0.9542    | 0.9992 | 0.9762 | 0.9851   |
| 0.0211        | 2.0   | 5000 | 0.0214          | 0.9377    | 0.9819 | 0.9593 | 0.9851   |
| 0.0219        | 3.0   | 7500 | 0.0211          | 0.9160    | 0.9729 | 0.9436 | 0.9851   |


### Framework versions

- Transformers 4.50.3
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.21.1
