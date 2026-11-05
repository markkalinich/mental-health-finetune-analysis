---
library_name: transformers
license: mit
base_model: Davlan/afro-xlmr-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: afroxlmr_base_moderation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# afroxlmr_base_moderation

This model is a fine-tuned version of [Davlan/afro-xlmr-base](https://huggingface.co/Davlan/afro-xlmr-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0971
- Accuracy: 0.6849
- Macro F1: 0.6610

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Macro F1 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.4384        | 1.0   | 688  | 0.7319          | 0.6409   | 0.6203   |
| 0.2864        | 2.0   | 1376 | 0.8637          | 0.6855   | 0.6639   |
| 0.2123        | 3.0   | 2064 | 0.9438          | 0.6855   | 0.6615   |
| 0.1695        | 4.0   | 2752 | 1.0971          | 0.6849   | 0.6610   |


### Framework versions

- Transformers 5.16.1
- Pytorch 2.11.0+cu128
- Datasets 4.0.0
- Tokenizers 0.23.1
