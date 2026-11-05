---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilgpt2
tags:
- generated_from_trainer
model-index:
- name: medical_clm_medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_clm_medical

This model is a fine-tuned version of [distilbert/distilgpt2](https://huggingface.co/distilbert/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5826

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 1    | 2.6762          |
| No log        | 2.0   | 2    | 2.6022          |
| No log        | 3.0   | 3    | 2.5826          |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.0+cu128
- Datasets 4.2.0
- Tokenizers 0.22.1
