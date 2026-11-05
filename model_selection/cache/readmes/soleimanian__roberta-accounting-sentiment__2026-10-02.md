---
library_name: transformers
license: mit
base_model: roberta-large
tags:
- accounting
- business
- sentiment
- tone
- esg
- csr
metrics:
- accuracy
model-index:
- name: Tone_August_2025
  results: []
language:
- en
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tone_August_2025

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0688
- Accuracy: 0.9845

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
- train_batch_size: 12
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.56.0.dev0
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.4