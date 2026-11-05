---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-small
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: PII-Token-Filter-Hard-gretel
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Token-Filter-Hard-gretel

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1881
- Precision: 0.5606
- Recall: 0.5286
- F1: 0.5441
- Accuracy: 0.9297

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 14   | 0.4122          | 0.1461    | 0.1857 | 0.1635 | 0.8421   |
| No log        | 2.0   | 28   | 0.2819          | 0.472     | 0.4214 | 0.4453 | 0.8919   |
| No log        | 3.0   | 42   | 0.2216          | 0.5546    | 0.4714 | 0.5097 | 0.9165   |
| No log        | 4.0   | 56   | 0.1960          | 0.5814    | 0.5357 | 0.5576 | 0.9275   |
| No log        | 5.0   | 70   | 0.1881          | 0.5606    | 0.5286 | 0.5441 | 0.9297   |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu129
- Datasets 4.8.2
- Tokenizers 0.22.0
