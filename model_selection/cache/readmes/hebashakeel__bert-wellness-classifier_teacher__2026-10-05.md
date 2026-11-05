---
library_name: transformers
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-wellness-classifier_teacher
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-wellness-classifier_teacher

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7694
- Accuracy: 0.688
- Auc: 0.9
- Precision Class 0: 0.862
- Precision Class 1: 0.739
- Precision Class 2: 0.613
- Precision Class 3: 0.538
- Recall Class 0: 0.781
- Recall Class 1: 0.81
- Recall Class 2: 0.704
- Recall Class 3: 0.483

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Auc   | Precision Class 0 | Precision Class 1 | Precision Class 2 | Precision Class 3 | Recall Class 0 | Recall Class 1 | Recall Class 2 | Recall Class 3 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:--------------:|:--------------:|:--------------:|:--------------:|
| 1.3247        | 1.0   | 63   | 1.1856          | 0.569    | 0.819 | 0.759             | 0.727             | 0.414             | 0.727             | 0.688          | 0.381          | 0.889          | 0.276          |
| 1.0767        | 2.0   | 126  | 1.0166          | 0.587    | 0.857 | 0.667             | 0.643             | 1.0               | 0.462             | 0.75           | 0.429          | 0.259          | 0.828          |
| 0.9285        | 3.0   | 189  | 0.9616          | 0.633    | 0.875 | 0.846             | 0.486             | 1.0               | 0.528             | 0.688          | 0.857          | 0.37           | 0.655          |
| 0.8628        | 4.0   | 252  | 0.8910          | 0.624    | 0.885 | 0.88              | 0.514             | 0.64              | 0.5               | 0.688          | 0.857          | 0.593          | 0.414          |
| 0.7828        | 5.0   | 315  | 0.8369          | 0.679    | 0.888 | 0.88              | 0.667             | 0.75              | 0.514             | 0.688          | 0.857          | 0.556          | 0.655          |
| 0.7489        | 6.0   | 378  | 0.7962          | 0.706    | 0.899 | 0.857             | 0.762             | 0.704             | 0.545             | 0.75           | 0.762          | 0.704          | 0.621          |
| 0.6981        | 7.0   | 441  | 0.8118          | 0.679    | 0.896 | 0.88              | 0.708             | 0.633             | 0.533             | 0.688          | 0.81           | 0.704          | 0.552          |
| 0.6634        | 8.0   | 504  | 0.7915          | 0.688    | 0.898 | 0.889             | 0.708             | 0.655             | 0.517             | 0.75           | 0.81           | 0.704          | 0.517          |
| 0.6651        | 9.0   | 567  | 0.7777          | 0.67     | 0.9   | 0.862             | 0.739             | 0.576             | 0.5               | 0.781          | 0.81           | 0.704          | 0.414          |
| 0.6591        | 10.0  | 630  | 0.7694          | 0.688    | 0.9   | 0.862             | 0.739             | 0.613             | 0.538             | 0.781          | 0.81           | 0.704          | 0.483          |


### Framework versions

- Transformers 4.45.1
- Pytorch 2.4.0+cpu
- Datasets 3.0.1
- Tokenizers 0.20.0
