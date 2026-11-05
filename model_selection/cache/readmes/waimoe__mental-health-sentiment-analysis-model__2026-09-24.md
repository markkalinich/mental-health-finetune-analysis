---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mental-health-sentiment-analysis-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental-health-sentiment-analysis-model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6196
- Accuracy: 0.8364
- F1 Macro: 0.8086
- F1 Weighted: 0.8373

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1 Macro | F1 Weighted |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:--------:|:-----------:|
| 0.5535        | 1.0   | 5305  | 0.6005          | 0.8033   | 0.7794   | 0.8047      |
| 0.4085        | 2.0   | 10610 | 0.5424          | 0.8335   | 0.8050   | 0.8350      |
| 0.2513        | 3.0   | 15915 | 0.6196          | 0.8364   | 0.8086   | 0.8373      |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.1
