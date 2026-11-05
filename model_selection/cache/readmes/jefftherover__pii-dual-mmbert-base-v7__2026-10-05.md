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
- name: pii-dual-mmbert-base-v7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-dual-mmbert-base-v7

This model is a fine-tuned version of [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0022
- Precision: 0.9972
- Recall: 0.9981
- F1: 0.9977
- Accuracy: 0.9995

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

| Training Loss | Epoch  | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0091        | 0.6584 | 2000  | 0.0039          | 0.9932    | 0.9962 | 0.9947 | 0.9989   |
| 0.0097        | 1.3167 | 4000  | 0.0047          | 0.9948    | 0.9969 | 0.9959 | 0.9988   |
| 0.0028        | 1.9751 | 6000  | 0.0020          | 0.9961    | 0.9978 | 0.9969 | 0.9994   |
| 0.0015        | 2.6334 | 8000  | 0.0018          | 0.9973    | 0.9984 | 0.9978 | 0.9995   |
| 0.0003        | 3.2917 | 10000 | 0.0021          | 0.9973    | 0.9982 | 0.9977 | 0.9995   |
| 0.0002        | 3.9501 | 12000 | 0.0022          | 0.9972    | 0.9981 | 0.9977 | 0.9995   |
| 0.0003        | 4.0    | 12152 | 0.0022          | 0.9972    | 0.9981 | 0.9977 | 0.9995   |


### Framework versions

- Transformers 5.16.1
- Pytorch 2.14.0+cu130
- Datasets 5.0.1
- Tokenizers 0.23.1
