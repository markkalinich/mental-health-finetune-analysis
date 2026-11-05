---
license: cc-by-nc-4.0
base_model: mental/mental-bert-base-uncased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: mental-bert-base-uncased-finetuned-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental-bert-base-uncased-finetuned-depression

This model is a fine-tuned version of [mental/mental-bert-base-uncased](https://huggingface.co/mental/mental-bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5358
- Precision: 0.8986
- Recall: 0.8885
- F1: 0.8933
- Accuracy: 0.9158

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
| No log        | 1.0   | 469  | 0.3929          | 0.8744    | 0.8346 | 0.8516 | 0.8849   |
| 0.4726        | 2.0   | 938  | 0.4405          | 0.9052    | 0.8359 | 0.8660 | 0.8955   |
| 0.2165        | 3.0   | 1407 | 0.4594          | 0.8627    | 0.8435 | 0.8515 | 0.8891   |
| 0.1263        | 4.0   | 1876 | 0.5213          | 0.9012    | 0.8781 | 0.8886 | 0.9094   |
| 0.0719        | 5.0   | 2345 | 0.4879          | 0.9036    | 0.8694 | 0.8851 | 0.9083   |
| 0.0471        | 6.0   | 2814 | 0.5628          | 0.9185    | 0.8639 | 0.8880 | 0.9104   |
| 0.0431        | 7.0   | 3283 | 0.5592          | 0.8980    | 0.8731 | 0.8846 | 0.9104   |
| 0.0402        | 8.0   | 3752 | 0.5948          | 0.9166    | 0.8591 | 0.8848 | 0.9094   |
| 0.0348        | 9.0   | 4221 | 0.5358          | 0.8986    | 0.8885 | 0.8933 | 0.9158   |
| 0.0276        | 10.0  | 4690 | 0.6361          | 0.9116    | 0.8619 | 0.8843 | 0.9094   |
| 0.0281        | 11.0  | 5159 | 0.6535          | 0.9095    | 0.8726 | 0.8897 | 0.9147   |
| 0.029         | 12.0  | 5628 | 0.6776          | 0.9098    | 0.8673 | 0.8868 | 0.9136   |
| 0.0188        | 13.0  | 6097 | 0.6940          | 0.9072    | 0.8629 | 0.8829 | 0.9072   |
| 0.0215        | 14.0  | 6566 | 0.7022          | 0.9168    | 0.8606 | 0.8856 | 0.9115   |
| 0.0184        | 15.0  | 7035 | 0.6996          | 0.9027    | 0.8687 | 0.8846 | 0.9126   |
| 0.0204        | 16.0  | 7504 | 0.6990          | 0.9063    | 0.8687 | 0.8861 | 0.9126   |
| 0.0204        | 17.0  | 7973 | 0.7268          | 0.9103    | 0.8677 | 0.8871 | 0.9115   |
| 0.0185        | 18.0  | 8442 | 0.7210          | 0.9066    | 0.8766 | 0.8907 | 0.9147   |
| 0.0181        | 19.0  | 8911 | 0.7346          | 0.9096    | 0.8732 | 0.8902 | 0.9147   |
| 0.0151        | 20.0  | 9380 | 0.7363          | 0.9090    | 0.8720 | 0.8892 | 0.9136   |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
