---
library_name: transformers
license: mit
base_model: microsoft/DialoGPT-medium
tags:
- generated_from_trainer
model-index:
- name: medical-reasoning-llm
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-reasoning-llm

This model is a fine-tuned version of [microsoft/DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0522

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
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.7225        | 0.7859 | 200  | 1.2090          |
| 0.6055        | 1.5697 | 400  | 1.0899          |
| 0.5652        | 2.3536 | 600  | 1.0522          |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
