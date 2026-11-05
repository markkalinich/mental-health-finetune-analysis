---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- f1
- precision
- recall
model-index:
- name: multilabel_mood_distilbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# multilabel_mood_distilbert

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0852
- F1: 0.5646
- Precision: 0.7199
- Recall: 0.4644

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
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:------:|:---------:|:------:|
| 0.138         | 1.0   | 1357 | 0.0932          | 0.5104 | 0.7194    | 0.3955 |
| 0.0888        | 2.0   | 2714 | 0.0860          | 0.5498 | 0.7359    | 0.4389 |
| 0.0807        | 3.0   | 4071 | 0.0852          | 0.5646 | 0.7199    | 0.4644 |


### Framework versions

- Transformers 4.53.2
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.2
