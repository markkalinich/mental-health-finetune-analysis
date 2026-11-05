---
library_name: transformers
license: mit
base_model: neuralmind/bert-base-portuguese-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-safety-monitor-complete
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-safety-monitor-complete

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5434
- Accuracy: 0.8307
- F1 Macro: 0.7834

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
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Macro |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| No log        | 1.0   | 353  | 0.3735          | 0.8227   | 0.7834   |
| 0.46          | 2.0   | 706  | 0.5032          | 0.7987   | 0.7740   |
| 0.2828        | 3.0   | 1059 | 0.4577          | 0.8147   | 0.7760   |
| 0.2828        | 4.0   | 1412 | 0.5434          | 0.8307   | 0.7834   |


### Framework versions

- Transformers 4.57.2
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
