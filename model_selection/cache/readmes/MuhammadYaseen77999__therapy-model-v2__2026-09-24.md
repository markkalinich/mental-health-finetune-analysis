---
library_name: transformers
license: apache-2.0
base_model: MuhammadYaseen77999/therapy-model
tags:
- generated_from_trainer
model-index:
- name: therapy-model-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# therapy-model-v2

This model is a fine-tuned version of [MuhammadYaseen77999/therapy-model](https://huggingface.co/MuhammadYaseen77999/therapy-model) on an unknown dataset.

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
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2

### Framework versions

- Transformers 4.54.0
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.2
