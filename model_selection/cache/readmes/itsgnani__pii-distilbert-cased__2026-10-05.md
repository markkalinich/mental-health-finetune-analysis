---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-cased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-distilbert-cased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-distilbert-cased

This model is a fine-tuned version of [distilbert/distilbert-base-cased](https://huggingface.co/distilbert/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2186
- Precision: 0.4770
- Recall: 0.6135
- F1: 0.5367
- Accuracy: 0.9395

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
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.06
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.8739        | 1.0   | 94   | 0.3850          | 0.2288    | 0.3663 | 0.2816 | 0.8968   |
| 0.4575        | 2.0   | 188  | 0.2407          | 0.3931    | 0.5246 | 0.4494 | 0.9307   |
| 0.4248        | 3.0   | 282  | 0.2186          | 0.4770    | 0.6135 | 0.5367 | 0.9395   |


### Framework versions

- Transformers 5.6.2
- Pytorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2
