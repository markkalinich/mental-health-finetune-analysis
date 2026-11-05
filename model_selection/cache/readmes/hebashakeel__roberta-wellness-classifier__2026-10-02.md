---
library_name: transformers
license: mit
base_model: roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta-wellness-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-wellness-classifier

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8807
- Accuracy: 0.71
- Auc: 0.871
- Precision Class 0: 0.787
- Precision Class 1: 0.857
- Precision Class 2: 0.731
- Precision Class 3: 0.645
- Recall Class 0: 0.698
- Recall Class 1: 0.667
- Recall Class 2: 0.603
- Recall Class 3: 0.796

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Auc   | Precision Class 0 | Precision Class 1 | Precision Class 2 | Precision Class 3 | Recall Class 0 | Recall Class 1 | Recall Class 2 | Recall Class 3 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:--------------:|:--------------:|:--------------:|:--------------:|
| 1.0423        | 1.0   | 140  | 0.7782          | 0.685    | 0.888 | 0.732             | 0.727             | 0.595             | 0.734             | 0.774          | 0.593          | 0.794          | 0.592          |
| 0.6558        | 2.0   | 280  | 0.7589          | 0.714    | 0.902 | 0.733             | 0.85              | 0.78              | 0.658             | 0.83           | 0.63           | 0.508          | 0.806          |
| 0.4306        | 3.0   | 420  | 1.0251          | 0.73     | 0.89  | 0.738             | 0.857             | 0.64              | 0.795             | 0.849          | 0.667          | 0.873          | 0.592          |
| 0.3002        | 4.0   | 560  | 1.2314          | 0.726    | 0.908 | 0.816             | 0.938             | 0.707             | 0.669             | 0.755          | 0.556          | 0.651          | 0.806          |
| 0.2117        | 5.0   | 700  | 1.3601          | 0.714    | 0.888 | 0.857             | 0.941             | 0.645             | 0.67              | 0.679          | 0.593          | 0.778          | 0.724          |
| 0.1606        | 6.0   | 840  | 1.4648          | 0.718    | 0.887 | 0.784             | 0.933             | 0.682             | 0.679             | 0.755          | 0.519          | 0.714          | 0.755          |
| 0.1135        | 7.0   | 980  | 1.6228          | 0.714    | 0.883 | 0.78              | 0.826             | 0.698             | 0.667             | 0.736          | 0.704          | 0.698          | 0.714          |
| 0.0686        | 8.0   | 1120 | 1.8947          | 0.71     | 0.866 | 0.809             | 0.857             | 0.745             | 0.635             | 0.717          | 0.667          | 0.556          | 0.816          |
| 0.0525        | 9.0   | 1260 | 1.8817          | 0.718    | 0.875 | 0.796             | 0.864             | 0.74              | 0.65              | 0.736          | 0.704          | 0.587          | 0.796          |
| 0.0526        | 10.0  | 1400 | 1.8807          | 0.71     | 0.871 | 0.787             | 0.857             | 0.731             | 0.645             | 0.698          | 0.667          | 0.603          | 0.796          |


### Framework versions

- Transformers 4.45.1
- Pytorch 2.4.0
- Datasets 3.0.1
- Tokenizers 0.20.0
