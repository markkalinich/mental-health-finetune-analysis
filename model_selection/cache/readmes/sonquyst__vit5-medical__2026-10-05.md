---
library_name: transformers
license: mit
base_model: VietAI/vit5-base
tags:
- generated_from_trainer
model-index:
- name: vit5-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit5-medical

This model is a fine-tuned version of [VietAI/vit5-base](https://huggingface.co/VietAI/vit5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0188

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.0449        | 0.5294 | 500  | 0.0390          |
| 0.0233        | 1.0582 | 1000 | 0.0279          |
| 0.0159        | 1.5876 | 1500 | 0.0213          |
| 0.006         | 2.1165 | 2000 | 0.0198          |
| 0.004         | 2.6458 | 2500 | 0.0188          |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
