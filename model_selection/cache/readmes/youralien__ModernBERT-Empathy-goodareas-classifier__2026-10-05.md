---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: ModernBERT-Empathy-goodareas-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ModernBERT-Empathy-goodareas-classifier

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5969
- F1: 0.7723

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
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.5319        | 1.0   | 231  | 0.4996          | 0.7473 |
| 0.4312        | 2.0   | 462  | 0.4623          | 0.7861 |
| 0.2423        | 3.0   | 693  | 0.5881          | 0.7765 |
| 0.0425        | 4.0   | 924  | 1.3316          | 0.7700 |
| 0.0021        | 5.0   | 1155 | 1.5969          | 0.7723 |


### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.4.1+cu121
- Datasets 3.1.0
- Tokenizers 0.21.0
