---
library_name: transformers
license: gemma
base_model: google/gemma-2-2b-it
tags:
- generated_from_trainer
model-index:
- name: gemma-2-2b-it-finetuned-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gemma-2-2b-it-finetuned-medical

This model is a fine-tuned version of [google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1961

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
| 0.4325        | 1.0   | 753  | 0.1505          |
| 0.0941        | 2.0   | 1506 | 0.1415          |
| 0.0417        | 3.0   | 2259 | 0.1961          |


### Framework versions

- Transformers 4.57.2
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
