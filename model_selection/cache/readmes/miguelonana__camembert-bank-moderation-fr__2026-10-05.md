---
library_name: transformers
license: mit
base_model: camembert-base
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: camembert-bank-moderation-fr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# camembert-bank-moderation-fr

This model is a fine-tuned version of [camembert-base](https://huggingface.co/camembert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5094
- Accuracy: 0.7851
- F1: 0.7847

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
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Accuracy | F1     | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:------:|:---------------:|
| 0.5696        | 1.0   | 434  | 0.7661   | 0.7650 | 0.5017          |
| 0.435         | 2.0   | 868  | 0.7828   | 0.7823 | 0.4885          |
| 0.3616        | 3.0   | 1302 | 0.5094   | 0.7851 | 0.7847          |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
