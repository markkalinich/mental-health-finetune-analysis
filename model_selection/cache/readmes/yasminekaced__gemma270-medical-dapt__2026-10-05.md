---
library_name: transformers
license: gemma
base_model: google/gemma-3-270m
tags:
- generated_from_trainer
model-index:
- name: gemma270-medical-dapt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gemma270-medical-dapt

This model is a fine-tuned version of [google/gemma-3-270m](https://huggingface.co/google/gemma-3-270m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9938

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 2.5998        | 0.7582 | 1000 | 2.8980          |
| 2.3657        | 1.5163 | 2000 | 2.8932          |
| 2.1833        | 2.2745 | 3000 | 2.9254          |
| 2.1202        | 3.0326 | 4000 | 2.9899          |
| 2.0536        | 3.7908 | 5000 | 2.9938          |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
