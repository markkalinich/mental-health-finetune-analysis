---
library_name: transformers
license: apache-2.0
base_model: t5-small
tags:
- generated_from_trainer
model-index:
- name: t5-medicine-normalizer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-medicine-normalizer

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2139
- Cer: 0.0112

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.391         | 1.0   | 844  | 0.3030          | 0.0159 |
| 0.3008        | 2.0   | 1688 | 0.2295          | 0.0121 |
| 0.2428        | 3.0   | 2532 | 0.2139          | 0.0112 |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
