---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mood_classifier_distilbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mood_classifier_distilbert

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1151
- Accuracy: 0.9779

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6246        | 1.0   | 164  | 0.1772          | 0.9535   |
| 0.1157        | 2.0   | 328  | 0.1541          | 0.9627   |
| 0.0486        | 3.0   | 492  | 0.1017          | 0.9779   |
| 0.0222        | 4.0   | 656  | 0.1021          | 0.9794   |
| 0.0115        | 5.0   | 820  | 0.1151          | 0.9779   |


### Framework versions

- Transformers 4.53.1
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.2
