---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: depression_classifier_weighted_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# depression_classifier_weighted_2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0299
- F1: {'f1': 0.5274571619747097}
- Accuracy: {'accuracy': 0.5993836671802774}

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1                          | Accuracy                         |
|:-------------:|:-----:|:----:|:---------------:|:---------------------------:|:--------------------------------:|
| No log        | 1.0   | 451  | 0.9802          | {'f1': 0.48800261330578315} | {'accuracy': 0.561171032357473}  |
| 0.8742        | 2.0   | 902  | 0.8159          | {'f1': 0.5567921899894229}  | {'accuracy': 0.636055469953775}  |
| 0.7241        | 3.0   | 1353 | 0.8759          | {'f1': 0.5323551976865734}  | {'accuracy': 0.5950693374422188} |
| 0.5999        | 4.0   | 1804 | 1.0016          | {'f1': 0.5186059710481855}  | {'accuracy': 0.5685670261941448} |
| 0.465         | 5.0   | 2255 | 1.0535          | {'f1': 0.5143537550061232}  | {'accuracy': 0.5722650231124807} |
| 0.3788        | 6.0   | 2706 | 1.0299          | {'f1': 0.5274571619747097}  | {'accuracy': 0.5993836671802774} |


### Framework versions

- Transformers 4.28.0
- Pytorch 2.0.1+cu118
- Datasets 2.12.0
- Tokenizers 0.13.3
