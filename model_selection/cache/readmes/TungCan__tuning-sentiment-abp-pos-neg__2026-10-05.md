---
library_name: transformers
base_model: TungCan/tuning-sentiment-abp-pos-neg
tags:
- text-classification
- vietnamese
- sentiment-analysis
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: tuning-sentiment-abp-pos-neg
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tuning-sentiment-abp-pos-neg

This model is a fine-tuned version of [TungCan/tuning-sentiment-abp-pos-neg](https://huggingface.co/TungCan/tuning-sentiment-abp-pos-neg) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9952
- Accuracy: 0.6892
- F1: 0.7495
- Precision: 0.7517
- Recall: 0.7474

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 387  | 0.5820          | 0.6994   | 0.7588 | 0.7572    | 0.7613 |
| 0.3956        | 2.0   | 774  | 0.6367          | 0.7430   | 0.7868 | 0.7988    | 0.7929 |
| 0.3357        | 3.0   | 1161 | 0.7205          | 0.7234   | 0.7728 | 0.7863    | 0.7738 |
| 0.2778        | 4.0   | 1548 | 0.8257          | 0.6962   | 0.7561 | 0.7644    | 0.7495 |
| 0.2778        | 5.0   | 1935 | 0.9952          | 0.6892   | 0.7495 | 0.7517    | 0.7474 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
