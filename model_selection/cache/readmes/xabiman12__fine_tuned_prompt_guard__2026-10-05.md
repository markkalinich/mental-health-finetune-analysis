---
library_name: transformers
license: llama3.1
base_model: meta-llama/Prompt-Guard-86M
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: fine_tuned_prompt_guard
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine_tuned_prompt_guard

This model is a fine-tuned version of [meta-llama/Prompt-Guard-86M](https://huggingface.co/meta-llama/Prompt-Guard-86M) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0658
- Accuracy: 0.982

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
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 32   | 0.1427          | 0.956    |
| No log        | 2.0   | 64   | 0.0773          | 0.97     |
| No log        | 3.0   | 96   | 0.0658          | 0.982    |


### Framework versions

- Transformers 4.46.3
- Pytorch 2.5.1+cpu
- Datasets 2.16.1
- Tokenizers 0.20.3
