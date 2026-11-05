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
- name: PII-Filter-SpanBased-Stage2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Filter-SpanBased-Stage2

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0206
- F1: 0.9976
- Recall: 0.9964
- Precision: 0.9988
- Trash Caught: 0.9506

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

| Training Loss | Epoch | Step  | Validation Loss | F1     | Recall | Precision | Trash Caught |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:---------:|:------------:|
| 0.1385        | 1.0   | 10726 | 0.0340          | 0.9953 | 0.9983 | 0.9923    | 0.6691       |
| 0.1042        | 2.0   | 21452 | 0.0263          | 0.9964 | 0.9953 | 0.9974    | 0.8903       |
| 0.0713        | 3.0   | 32178 | 0.0183          | 0.9977 | 0.9977 | 0.9978    | 0.9049       |
| 0.0664        | 4.0   | 42904 | 0.0206          | 0.9976 | 0.9964 | 0.9988    | 0.9506       |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu129
- Datasets 4.8.3
- Tokenizers 0.22.0
