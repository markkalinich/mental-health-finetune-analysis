---
library_name: transformers
base_model: 5CD-AI/Vietnamese-Sentiment-visobert
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
- name: tuning-sentiment-abp-neu
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tuning-sentiment-abp-v2.3

This model is a fine-tuned version of [5CD-AI/Vietnamese-Sentiment-visobert](https://huggingface.co/5CD-AI/Vietnamese-Sentiment-visobert) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0
- Accuracy: 1.0
- F1: 1.0
- Precision: 1.0
- Recall: 1.0

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1  | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---:|:---------:|:------:|
| No log        | 1.0   | 239  | 0.0             | 1.0      | 1.0 | 1.0       | 1.0    |
| No log        | 2.0   | 478  | 0.0             | 1.0      | 1.0 | 1.0       | 1.0    |
| 0.0145        | 3.0   | 717  | 0.0             | 1.0      | 1.0 | 1.0       | 1.0    |
| 0.0145        | 4.0   | 956  | 0.0             | 1.0      | 1.0 | 1.0       | 1.0    |
| 0.0           | 5.0   | 1195 | 0.0             | 1.0      | 1.0 | 1.0       | 1.0    |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
