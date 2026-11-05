---
library_name: transformers
license: mit
base_model: microsoft/DialoGPT-medium
tags:
- generated_from_trainer
model-index:
- name: dialogpt-empathetic-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dialogpt-empathetic-new

This model is a fine-tuned version of [microsoft/DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4233

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.5792        | 1.0   | 920  | 2.5017          |
| 2.4489        | 2.0   | 1840 | 2.4296          |
| 2.4345        | 3.0   | 2760 | 2.4233          |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.10.0+cu128
- Datasets 2.14.7
- Tokenizers 0.22.2
