---
library_name: transformers
license: mit
base_model: jhu-clsp/mmBERT-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-dual-mmbert-base-v4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-dual-mmbert-base-v4

This model is a fine-tuned version of [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0002
- Precision: 0.9997
- Recall: 0.9998
- F1: 0.9997
- Accuracy: 0.9999

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
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 200
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0005        | 1.0455 | 2000 | 0.0017          | 0.9988    | 0.9992 | 0.9990 | 0.9997   |
| 0.0006        | 2.0910 | 4000 | 0.0002          | 0.9997    | 0.9998 | 0.9997 | 0.9999   |
| 0.0001        | 3.1365 | 6000 | 0.0002          | 0.9996    | 0.9998 | 0.9997 | 0.9999   |
| 0.0002        | 4.0    | 7652 | 0.0002          | 0.9997    | 0.9998 | 0.9997 | 0.9999   |


### Framework versions

- Transformers 5.16.1
- Pytorch 2.13.0+cu130
- Datasets 5.0.1
- Tokenizers 0.23.1
