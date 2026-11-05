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
- name: tuning-sentiment-abp-v2.1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tuning-sentiment-abp-v2.1

This model is a fine-tuned version of [5CD-AI/Vietnamese-Sentiment-visobert](https://huggingface.co/5CD-AI/Vietnamese-Sentiment-visobert) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5126
- Accuracy: 0.7136
- F1: 0.5817
- Precision: 0.6377
- Recall: 0.6576

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
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.5366        | 1.0   | 826  | 0.4949          | 0.7140   | 0.5837 | 0.6513    | 0.6571 |
| 0.4734        | 2.0   | 1652 | 0.4961          | 0.7146   | 0.5818 | 0.6756    | 0.6580 |
| 0.4645        | 3.0   | 2478 | 0.5126          | 0.7136   | 0.5817 | 0.6377    | 0.6576 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
