---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- text-classification
- sentiment-analysis
- imdb
- distilbert
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: imdb-sentiment-with-distilbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# imdb-sentiment-with-distilbert

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3526
- Accuracy: 0.9192
- F1: 0.9192

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 0.2368        | 1.0   | 2500  | 0.2220          | 0.9116   | 0.9116 |
| 0.1472        | 2.0   | 5000  | 0.3138          | 0.9014   | 0.9011 |
| 0.0795        | 3.0   | 7500  | 0.3530          | 0.9178   | 0.9178 |
| 0.0473        | 4.0   | 10000 | 0.4096          | 0.916    | 0.9160 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.11.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
