---
library_name: transformers
license: apache-2.0
base_model: distilgpt2
tags:
- generated_from_trainer
model-index:
- name: mental_health_gpt2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental_health_gpt2

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5340

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.8297        | 1.0   | 1810 | 1.7047          |
| 1.6464        | 2.0   | 3620 | 1.6081          |
| 1.6108        | 3.0   | 5430 | 1.5645          |
| 1.5652        | 4.0   | 7240 | 1.5420          |
| 1.4691        | 5.0   | 9050 | 1.5340          |


### Framework versions

- Transformers 4.52.2
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.1
