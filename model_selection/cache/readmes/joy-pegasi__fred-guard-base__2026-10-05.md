---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: fred-guard-base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fred-guard-base

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0508
- Accuracy: 0.9806
- Precision: 1.0
- Recall: 0.9611
- F1: 0.9802

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
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9662        | 0.1111 | 5    | 0.7300          | 0.5194   | 0.5099    | 1.0    | 0.6754 |
| 0.6438        | 0.2222 | 10   | 0.5574          | 0.6778   | 0.6553    | 0.75   | 0.6995 |
| 0.6016        | 0.3333 | 15   | 0.4892          | 0.7667   | 0.8038    | 0.7056 | 0.7515 |
| 0.4617        | 0.4444 | 20   | 0.4301          | 0.7972   | 0.7512    | 0.8889 | 0.8142 |
| 0.3779        | 0.5556 | 25   | 0.3152          | 0.8528   | 0.8588    | 0.8444 | 0.8515 |
| 0.3712        | 0.6667 | 30   | 0.2228          | 0.8944   | 0.9437    | 0.8389 | 0.8882 |
| 0.2169        | 0.7778 | 35   | 0.2674          | 0.8806   | 0.9928    | 0.7667 | 0.8652 |
| 0.2445        | 0.8889 | 40   | 0.1471          | 0.9306   | 0.9189    | 0.9444 | 0.9315 |
| 0.1838        | 1.0    | 45   | 0.2446          | 0.8833   | 0.9929    | 0.7722 | 0.8688 |
| 0.1249        | 1.1111 | 50   | 0.1212          | 0.9472   | 0.9215    | 0.9778 | 0.9488 |
| 0.0775        | 1.2222 | 55   | 0.1005          | 0.9556   | 0.9940    | 0.9167 | 0.9538 |
| 0.0776        | 1.3333 | 60   | 0.0783          | 0.9722   | 0.9775    | 0.9667 | 0.9721 |
| 0.0577        | 1.4444 | 65   | 0.0924          | 0.9722   | 0.9942    | 0.95   | 0.9716 |
| 0.0753        | 1.5556 | 70   | 0.0763          | 0.9722   | 0.9942    | 0.95   | 0.9716 |
| 0.0733        | 1.6667 | 75   | 0.0453          | 0.975    | 0.9831    | 0.9667 | 0.9748 |
| 0.0866        | 1.7778 | 80   | 0.0576          | 0.9778   | 1.0       | 0.9556 | 0.9773 |
| 0.041         | 1.8889 | 85   | 0.0583          | 0.9778   | 1.0       | 0.9556 | 0.9773 |
| 0.0579        | 2.0    | 90   | 0.0508          | 0.9806   | 1.0       | 0.9611 | 0.9802 |


### Framework versions

- Transformers 4.55.4
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.21.4
