---
library_name: transformers
license: apache-2.0
base_model: distilgpt2
tags:
- generated_from_trainer
model-index:
- name: distilgpt2-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilgpt2-medical

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8685

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
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 106  | 1.9726          |
| No log        | 2.0   | 212  | 1.8889          |
| No log        | 3.0   | 318  | 1.8729          |
| No log        | 4.0   | 424  | 1.8685          |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.1+cpu
- Datasets 5.0.0
- Tokenizers 0.22.2
