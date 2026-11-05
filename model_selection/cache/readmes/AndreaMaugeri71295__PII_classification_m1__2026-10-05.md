---
library_name: transformers
license: apache-2.0
base_model: yonigo/distilbert-base-multilingual-cased-pii
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: PII_classification_m1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII_classification_m1

This model is a fine-tuned version of [yonigo/distilbert-base-multilingual-cased-pii](https://huggingface.co/yonigo/distilbert-base-multilingual-cased-pii) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5114
- Precision: 0.2198
- Recall: 0.2152
- F1: 0.2175
- Accuracy: 0.8536

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.5054        | 1.0   | 5036  | 0.4803          | 0.1488    | 0.1167 | 0.1308 | 0.8323   |
| 0.4305        | 2.0   | 10072 | 0.4536          | 0.1928    | 0.1756 | 0.1838 | 0.8416   |
| 0.3903        | 3.0   | 15108 | 0.4378          | 0.2003    | 0.1759 | 0.1873 | 0.8495   |
| 0.3317        | 4.0   | 20144 | 0.4314          | 0.2001    | 0.1782 | 0.1885 | 0.8501   |
| 0.2925        | 5.0   | 25180 | 0.4395          | 0.2194    | 0.2068 | 0.2130 | 0.8523   |
| 0.2609        | 6.0   | 30216 | 0.4759          | 0.2195    | 0.2129 | 0.2162 | 0.8529   |
| 0.2272        | 7.0   | 35252 | 0.4924          | 0.2228    | 0.2140 | 0.2183 | 0.8531   |
| 0.2059        | 8.0   | 40288 | 0.5114          | 0.2198    | 0.2152 | 0.2175 | 0.8536   |


### Framework versions

- Transformers 4.50.0
- Pytorch 2.6.0+cu124
- Datasets 3.4.1
- Tokenizers 0.21.1
