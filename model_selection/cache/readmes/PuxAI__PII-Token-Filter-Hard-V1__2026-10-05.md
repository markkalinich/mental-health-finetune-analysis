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
- name: PII-Token-Filter-Hard-V1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Token-Filter-Hard-V1

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9765
- Precision: 0.2376
- Recall: 0.9901
- F1: 0.3832
- Accuracy: 0.7629

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

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0147        | 1.0   | 2651  | 1.9499          | 0.2339    | 0.9274 | 0.3735 | 0.7659   |
| 0.0065        | 2.0   | 5302  | 2.4256          | 0.2371    | 0.9862 | 0.3823 | 0.7620   |
| 0.003         | 3.0   | 7953  | 2.6138          | 0.2390    | 0.9833 | 0.3845 | 0.7651   |
| 0.0013        | 4.0   | 10604 | 2.8710          | 0.2366    | 0.9869 | 0.3817 | 0.7624   |
| 0.0005        | 5.0   | 13255 | 2.9765          | 0.2376    | 0.9901 | 0.3832 | 0.7629   |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu129
- Datasets 4.8.2
- Tokenizers 0.22.0
