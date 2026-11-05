---
library_name: transformers
license: apache-2.0
base_model: google-bert/bert-base-cased
tags:
- generated_from_trainer
- sentiment-analysis
metrics:
- accuracy
model-index:
- name: bert-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-imdb

This model is a fine-tuned version of [google-bert/bert-base-cased](https://huggingface.co/google-bert/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1992
- Accuracy: 0.9401

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:--------:|
| 0.1955        | 0.4997 | 833  | 0.2076          | 0.917    |
| 0.1495        | 0.9994 | 1666 | 0.2185          | 0.9221   |
| 0.1898        | 1.4991 | 2499 | 0.1974          | 0.9387   |
| 0.1098        | 1.9988 | 3332 | 0.1992          | 0.9401   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
