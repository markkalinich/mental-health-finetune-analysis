---
license: apache-2.0
base_model: google-bert/bert-base-cased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pharmaconer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pharmaconer

This model is a fine-tuned version of [google-bert/bert-base-cased](https://huggingface.co/google-bert/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0513
- Precision: 0.9074
- Recall: 0.8889
- F1: 0.8981
- Accuracy: 0.9933

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0466        | 1.0   | 1017  | 0.0446          | 0.8008    | 0.8026 | 0.8017 | 0.9875   |
| 0.0224        | 2.0   | 2034  | 0.0380          | 0.8177    | 0.8826 | 0.8489 | 0.9899   |
| 0.0111        | 3.0   | 3051  | 0.0403          | 0.9174    | 0.8560 | 0.8856 | 0.9922   |
| 0.0069        | 4.0   | 4068  | 0.0404          | 0.9024    | 0.8829 | 0.8925 | 0.9929   |
| 0.004         | 5.0   | 5085  | 0.0409          | 0.9060    | 0.8869 | 0.8963 | 0.9932   |
| 0.0017        | 6.0   | 6102  | 0.0447          | 0.8896    | 0.8949 | 0.8922 | 0.9928   |
| 0.001         | 7.0   | 7119  | 0.0499          | 0.8992    | 0.8901 | 0.8946 | 0.9930   |
| 0.0006        | 8.0   | 8136  | 0.0507          | 0.9047    | 0.8886 | 0.8966 | 0.9931   |
| 0.0003        | 9.0   | 9153  | 0.0500          | 0.9089    | 0.8895 | 0.8991 | 0.9933   |
| 0.0004        | 10.0  | 10170 | 0.0513          | 0.9074    | 0.8889 | 0.8981 | 0.9933   |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
