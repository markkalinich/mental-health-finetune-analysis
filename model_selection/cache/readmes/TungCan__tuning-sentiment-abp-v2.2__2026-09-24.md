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
- name: tuning-sentiment-abp-v2.2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tuning-sentiment-abp-v2.2

This model is a fine-tuned version of [5CD-AI/Vietnamese-Sentiment-visobert](https://huggingface.co/5CD-AI/Vietnamese-Sentiment-visobert) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9679
- Accuracy: 0.4844
- F1: 0.5232
- Precision: 0.5186
- Recall: 0.5436

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
| 0.6162        | 1.0   | 607  | 0.7060          | 0.6096   | 0.5219 | 0.5977    | 0.5816 |
| 0.6188        | 2.0   | 1214 | 0.7061          | 0.6074   | 0.5241 | 0.5668    | 0.5931 |
| 0.6158        | 3.0   | 1821 | 0.7626          | 0.5935   | 0.5223 | 0.5325    | 0.5822 |
| 0.6077        | 4.0   | 2428 | 0.8325          | 0.5916   | 0.5283 | 0.5217    | 0.5974 |
| 0.5846        | 5.0   | 3035 | 0.9679          | 0.4844   | 0.5232 | 0.5186    | 0.5436 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
