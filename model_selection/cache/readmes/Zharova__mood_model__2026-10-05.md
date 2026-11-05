---
library_name: transformers
license: mit
base_model: Zharova/mood_model
tags:
- generated_from_trainer
model-index:
- name: mood_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mood_model

This model is a fine-tuned version of [Zharova/mood_model](https://huggingface.co/Zharova/mood_model) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9154
- F1 Macro: 0.6956

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1 Macro |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.8773        | 1.0   | 1405 | 0.8589          | 0.6825   |
| 0.6381        | 2.0   | 2810 | 0.8305          | 0.6987   |
| 0.4593        | 3.0   | 4215 | 0.9154          | 0.6956   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
