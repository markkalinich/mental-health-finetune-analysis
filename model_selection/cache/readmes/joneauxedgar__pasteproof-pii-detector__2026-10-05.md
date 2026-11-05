---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: pasteproof-pii-detector
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pasteproof-pii-detector

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000
- Precision: 1.0
- Recall: 1.0
- F1: 1.0

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|
| 0.0003        | 0.3555 | 1000 | 0.0001          | 0.9999    | 1.0000 | 0.9999 |
| 0.0001        | 0.7110 | 2000 | 0.0002          | 0.9988    | 0.9993 | 0.9991 |
| 0.0001        | 1.0665 | 3000 | 0.0000          | 1.0       | 1.0    | 1.0    |
| 0.0001        | 1.4220 | 4000 | 0.0000          | 1.0       | 1.0    | 1.0    |
| 0.0           | 1.7775 | 5000 | 0.0000          | 1.0       | 1.0    | 1.0    |
| 0.0           | 2.1330 | 6000 | 0.0000          | 1.0       | 1.0    | 1.0    |
| 0.0           | 2.4884 | 7000 | 0.0000          | 1.0       | 1.0    | 1.0    |
| 0.0           | 2.8439 | 8000 | 0.0000          | 1.0       | 1.0    | 1.0    |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
