---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
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
- name: distilbert-sentiment-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-sentiment-imdb

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3717
- Accuracy: 0.899
- F1: 0.8989

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
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.2682        | 1.0   | 500  | 0.2768          | 0.8915   | 0.8935 |
| 0.2280        | 2.0   | 1000 | 0.2720          | 0.897    | 0.8964 |
| 0.0938        | 3.0   | 1500 | 0.3717          | 0.899    | 0.8989 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
