---
library_name: transformers
license: apache-2.0
base_model: google/vit-base-patch16-224
tags:
- generated_from_trainer
model-index:
- name: medai-vision-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medai-vision-medical

This model is a fine-tuned version of [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0525

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

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.407         | 1.0   | 599  | 0.3073          |
| 0.2242        | 2.0   | 1198 | 0.1043          |
| 0.0142        | 3.0   | 1797 | 0.0525          |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
