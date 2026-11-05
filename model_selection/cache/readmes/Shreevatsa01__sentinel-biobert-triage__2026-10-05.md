---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: sentinel-biobert-triage
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentinel-biobert-triage

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2133
- Accuracy: 0.9583
- F1: 0.9287
- Precision: 0.9140
- Recall: 0.9438

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
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.2163        | 1.0   | 882  | 0.1343          | 0.9575   | 0.9280 | 0.9045    | 0.9527 |
| 0.0812        | 2.0   | 1764 | 0.1716          | 0.9544   | 0.9223 | 0.9027    | 0.9428 |
| 0.031         | 3.0   | 2646 | 0.2133          | 0.9583   | 0.9287 | 0.9140    | 0.9438 |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2
