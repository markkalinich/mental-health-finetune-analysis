---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-small
tags:
- generated_from_trainer
metrics:
- f1
- recall
- precision
model-index:
- name: PII-Filter-TokenBased-Stage2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Filter-TokenBased-Stage2

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0327
- F1: 0.9947
- Recall: 0.9905
- Precision: 0.9989
- Trash Caught: 0.7051

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
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Recall | Precision | Trash Caught |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:---------:|:------------:|
| 0.3218        | 1.0   | 1202 | 0.0478          | 0.9954 | 0.9931 | 0.9977    | 0.3718       |
| 0.2561        | 2.0   | 2404 | 0.0269          | 0.9963 | 0.9946 | 0.9980    | 0.4487       |
| 0.1991        | 3.0   | 3606 | 0.0435          | 0.9938 | 0.9888 | 0.9988    | 0.6667       |
| 0.1645        | 4.0   | 4808 | 0.0327          | 0.9947 | 0.9905 | 0.9989    | 0.7051       |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu129
- Datasets 4.8.3
- Tokenizers 0.22.0
