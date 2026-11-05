---
license: mit
base_model: roberta-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: roberta-base-finetuned-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-depression

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7662
- Precision: 0.8912
- Recall: 0.9136
- F1: 0.9018
- Accuracy: 0.9104

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 469  | 0.5219          | 0.8220    | 0.7921 | 0.8000 | 0.8603   |
| 0.602         | 2.0   | 938  | 0.6344          | 0.9039    | 0.8257 | 0.8538 | 0.8753   |
| 0.3573        | 3.0   | 1407 | 0.4821          | 0.8818    | 0.8902 | 0.8859 | 0.8870   |
| 0.2511        | 4.0   | 1876 | 0.6265          | 0.8511    | 0.8965 | 0.8676 | 0.8934   |
| 0.1614        | 5.0   | 2345 | 0.5439          | 0.8908    | 0.8992 | 0.8919 | 0.9041   |
| 0.1107        | 6.0   | 2814 | 0.6237          | 0.8838    | 0.8990 | 0.8886 | 0.9009   |
| 0.0756        | 7.0   | 3283 | 0.6915          | 0.8930    | 0.9062 | 0.8988 | 0.9083   |
| 0.057         | 8.0   | 3752 | 0.6572          | 0.8736    | 0.9107 | 0.8905 | 0.9062   |
| 0.0664        | 9.0   | 4221 | 0.8022          | 0.8692    | 0.8987 | 0.8804 | 0.8977   |
| 0.0392        | 10.0  | 4690 | 0.7953          | 0.8931    | 0.8847 | 0.8844 | 0.8977   |
| 0.0472        | 11.0  | 5159 | 0.7757          | 0.8951    | 0.8886 | 0.8885 | 0.8998   |
| 0.0375        | 12.0  | 5628 | 0.7821          | 0.8881    | 0.9029 | 0.8939 | 0.9072   |
| 0.0292        | 13.0  | 6097 | 0.8124          | 0.8793    | 0.8982 | 0.8870 | 0.9009   |
| 0.0373        | 14.0  | 6566 | 0.9106          | 0.8774    | 0.8818 | 0.8735 | 0.8934   |
| 0.0227        | 15.0  | 7035 | 0.8325          | 0.8876    | 0.8855 | 0.8825 | 0.8966   |
| 0.0249        | 16.0  | 7504 | 0.7662          | 0.8912    | 0.9136 | 0.9018 | 0.9104   |
| 0.0249        | 17.0  | 7973 | 0.8383          | 0.8804    | 0.8905 | 0.8833 | 0.8955   |
| 0.0245        | 18.0  | 8442 | 0.8073          | 0.8844    | 0.9000 | 0.8907 | 0.9030   |
| 0.0188        | 19.0  | 8911 | 0.8137          | 0.8850    | 0.9012 | 0.8917 | 0.9041   |
| 0.0203        | 20.0  | 9380 | 0.8234          | 0.8850    | 0.8993 | 0.8905 | 0.9030   |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
