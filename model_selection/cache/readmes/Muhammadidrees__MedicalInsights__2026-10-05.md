---
library_name: transformers
license: mit
base_model: microsoft/BioGPT-Large
tags:
- generated_from_trainer
model-index:
- name: MedicalInsights
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedicalInsights

This model is a fine-tuned version of [microsoft/BioGPT-Large](https://huggingface.co/microsoft/BioGPT-Large) on the None dataset.

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- distributed_type: tpu
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2

### Training results



### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cpu
- Datasets 4.1.1
- Tokenizers 0.22.0
