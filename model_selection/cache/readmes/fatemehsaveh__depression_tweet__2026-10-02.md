---
base_model: rafalposwiata/deproberta-large-v1
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: depression_tweet
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# depression_tweet

This model is a fine-tuned version of [rafalposwiata/deproberta-large-v1](https://huggingface.co/rafalposwiata/deproberta-large-v1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0646
- Accuracy: 0.9836
- Precision: 0.9656
- Recall: 0.9977
- F1: 0.9814

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
- train_batch_size: 128
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 200

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 0.2   | 50   | 0.1556          | 0.9684   | 0.9508    | 0.9777 | 0.9641 |
| No log        | 0.4   | 100  | 0.1399          | 0.9646   | 0.9354    | 0.9865 | 0.9603 |
| No log        | 0.61  | 150  | 0.1118          | 0.9631   | 0.9279    | 0.9920 | 0.9589 |
| No log        | 0.81  | 200  | 0.1090          | 0.9659   | 0.9333    | 0.9922 | 0.9619 |
| No log        | 1.01  | 250  | 0.0819          | 0.9759   | 0.9556    | 0.9905 | 0.9727 |
| No log        | 1.21  | 300  | 0.0548          | 0.9831   | 0.9831    | 0.9777 | 0.9804 |
| No log        | 1.42  | 350  | 0.1162          | 0.9587   | 0.9435    | 0.9624 | 0.9529 |
| No log        | 1.62  | 400  | 0.1167          | 0.9657   | 0.9303    | 0.9955 | 0.9618 |
| No log        | 1.82  | 450  | 0.0859          | 0.9776   | 0.9549    | 0.9955 | 0.9747 |
| 0.0575        | 2.02  | 500  | 0.0564          | 0.9848   | 0.9707    | 0.9950 | 0.9827 |
| 0.0575        | 2.23  | 550  | 0.0591          | 0.9839   | 0.9693    | 0.9945 | 0.9817 |
| 0.0575        | 2.43  | 600  | 0.0913          | 0.9814   | 0.9623    | 0.9962 | 0.9790 |
| 0.0575        | 2.63  | 650  | 0.0633          | 0.9847   | 0.9686    | 0.9970 | 0.9826 |
| 0.0575        | 2.83  | 700  | 0.1171          | 0.9762   | 0.9493    | 0.9985 | 0.9733 |
| 0.0575        | 3.04  | 750  | 0.0646          | 0.9836   | 0.9656    | 0.9977 | 0.9814 |


### Framework versions

- Transformers 4.37.1
- Pytorch 2.0.1
- Datasets 2.16.1
- Tokenizers 0.15.1
