---
library_name: transformers
license: mit
base_model: neuralmind/bert-base-portuguese-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-safety-monitor-balanced
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-safety-monitor-balanced

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5227
- Accuracy: 0.8558
- F1 Macro: 0.8384

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
| No log        | 1.0   | 355  | 0.3471          | 0.8257   | 0.8129   |
| 0.4798        | 2.0   | 710  | 0.4387          | 0.7940   | 0.7977   |
| 0.2958        | 3.0   | 1065 | 0.4714          | 0.8288   | 0.8202   |
| 0.2958        | 4.0   | 1420 | 0.3727          | 0.8447   | 0.8293   |
| 0.2308        | 5.0   | 1775 | 0.4305          | 0.8621   | 0.8417   |
| 0.1741        | 6.0   | 2130 | 0.5189          | 0.8558   | 0.8384   |
| 0.1741        | 7.0   | 2485 | 0.4521          | 0.8605   | 0.8363   |
| 0.163         | 8.0   | 2840 | 0.5227          | 0.8558   | 0.8384   |


### Framework versions

- Transformers 4.57.2
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
