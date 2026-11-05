---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-small
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: PII-Binary-Filter-Hard-gretel-pii-ready
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Binary-Filter-Hard-gretel-pii-ready

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9574
- Accuracy: 0.7767
- F1: 0.7702
- Precision: 0.9321
- Recall: 0.6562

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.435         | 1.0   | 539  | 0.6876          | 0.7028   | 0.6830 | 0.8713    | 0.5616 |
| 0.2579        | 2.0   | 1078 | 0.8187          | 0.7670   | 0.7649 | 0.9005    | 0.6649 |
| 0.1915        | 3.0   | 1617 | 0.9574          | 0.7767   | 0.7702 | 0.9321    | 0.6562 |
| 0.1375        | 4.0   | 2156 | 1.3507          | 0.7528   | 0.7345 | 0.9474    | 0.5998 |
| 0.103         | 5.0   | 2695 | 1.2331          | 0.7728   | 0.7621 | 0.9461    | 0.6380 |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu129
- Datasets 4.8.2
- Tokenizers 0.22.0
