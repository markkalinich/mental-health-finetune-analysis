---
library_name: transformers
license: mit
base_model: bert-base-german-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-german-cased-holdout-1200-cluster
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-german-cased-holdout-1200-cluster

This model is a fine-tuned version of [bert-base-german-cased](https://huggingface.co/bert-base-german-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2809
- Accuracy: 0.9542
- Precision Macro: 0.3181
- Recall Macro: 0.3333
- F1 Macro: 0.3255
- Krippendorffs Alpha: -0.0158

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.1200907414145304e-06
- train_batch_size: 1
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision Macro | Recall Macro | F1 Macro | Krippendorffs Alpha |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------------:|:------------:|:--------:|:-------------------:|
| 0.4308        | 1.0   | 960  | 0.2809          | 0.9542   | 0.3181          | 0.3333       | 0.3255   | -0.0158             |


### Framework versions

- Transformers 4.53.1
- Pytorch 2.7.1+cu126
- Datasets 3.6.0
- Tokenizers 0.21.2
