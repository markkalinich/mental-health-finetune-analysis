---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-small
tags:
- generated_from_trainer
metrics:
- recall
- precision
model-index:
- name: PII-Binary-Filter-Extreme-Recall
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Binary-Filter-Extreme-Recall

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8377
- F1 At 10 Thresh: 0.7490
- Recall: 0.9871
- Precision: 0.6035
- Trash Caught: 0.1396

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1 At 10 Thresh | Recall | Precision | Trash Caught |
|:-------------:|:-----:|:----:|:---------------:|:---------------:|:------:|:---------:|:------------:|
| 0.1651        | 1.0   | 1569 | 2.0216          | 0.7403          | 0.9908 | 0.5909    | 0.0900       |
| 0.1066        | 2.0   | 3138 | 2.6117          | 0.7482          | 0.9906 | 0.6011    | 0.1279       |
| 0.0671        | 3.0   | 4707 | 2.8377          | 0.7490          | 0.9871 | 0.6035    | 0.1396       |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu129
- Tokenizers 0.22.0
