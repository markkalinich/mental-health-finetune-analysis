---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
model-index:
- name: suicide-distilbert-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# suicide-distilbert-2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4305
- Accuracy: {'accuracy': 0.4}
- Precision: 0.2743
- Recall: 0.4
- Fscore: 0.2992

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy           | Precision | Recall | Fscore |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 10   | 1.6207          | {'accuracy': 0.31} | 0.0981    | 0.31   | 0.1490 |
| No log        | 2.0   | 20   | 1.5899          | {'accuracy': 0.31} | 0.0961    | 0.31   | 0.1467 |
| No log        | 3.0   | 30   | 1.5121          | {'accuracy': 0.35} | 0.2121    | 0.35   | 0.2258 |
| No log        | 4.0   | 40   | 1.4855          | {'accuracy': 0.37} | 0.2008    | 0.37   | 0.2468 |
| No log        | 5.0   | 50   | 1.4565          | {'accuracy': 0.36} | 0.1844    | 0.36   | 0.2381 |
| No log        | 6.0   | 60   | 1.4514          | {'accuracy': 0.38} | 0.1923    | 0.38   | 0.2495 |
| No log        | 7.0   | 70   | 1.4609          | {'accuracy': 0.39} | 0.2949    | 0.39   | 0.2934 |
| No log        | 8.0   | 80   | 1.4545          | {'accuracy': 0.4}  | 0.2776    | 0.4    | 0.3212 |
| No log        | 9.0   | 90   | 1.4673          | {'accuracy': 0.37} | 0.2889    | 0.37   | 0.2762 |
| No log        | 10.0  | 100  | 1.4305          | {'accuracy': 0.4}  | 0.2743    | 0.4    | 0.2992 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
