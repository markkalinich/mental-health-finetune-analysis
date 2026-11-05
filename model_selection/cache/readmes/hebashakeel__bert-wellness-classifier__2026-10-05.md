---
library_name: transformers
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-wellness-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-wellness-classifier

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0333
- Accuracy: 0.648
- Auc: 0.878
- Precision Class 0: 0.409
- Precision Class 1: 0.769
- Precision Class 2: 0.382
- Precision Class 3: 0.729
- Precision Class 4: 0.833
- Precision Class 5: 0.478
- Recall Class 0: 0.474
- Recall Class 1: 0.87
- Recall Class 2: 0.481
- Recall Class 3: 0.745
- Recall Class 4: 0.781
- Recall Class 5: 0.333

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Auc   | Precision Class 0 | Precision Class 1 | Precision Class 2 | Precision Class 3 | Precision Class 4 | Precision Class 5 | Recall Class 0 | Recall Class 1 | Recall Class 2 | Recall Class 3 | Recall Class 4 | Recall Class 5 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|
| 1.5028        | 1.0   | 62   | 1.1703          | 0.528    | 0.852 | 0.5               | 0.889             | 0.0               | 0.769             | 0.595             | 0.282             | 0.28           | 0.4            | 0.0            | 0.714          | 0.701          | 0.556          |
| 1.1661        | 2.0   | 124  | 1.0814          | 0.575    | 0.868 | 0.6               | 0.515             | 0.375             | 0.935             | 0.712             | 0.333             | 0.36           | 0.85           | 0.136          | 0.69           | 0.627          | 0.611          |
| 1.0576        | 3.0   | 186  | 1.0438          | 0.585    | 0.876 | 0.394             | 0.737             | 0.308             | 0.755             | 0.719             | 0.467             | 0.52           | 0.7            | 0.545          | 0.881          | 0.612          | 0.194          |
| 0.9603        | 4.0   | 248  | 1.0368          | 0.637    | 0.877 | 0.688             | 0.846             | 0.44              | 0.868             | 0.6               | 0.4               | 0.44           | 0.55           | 0.5            | 0.786          | 0.94           | 0.167          |
| 0.8873        | 5.0   | 310  | 1.0208          | 0.571    | 0.877 | 0.667             | 0.75              | 0.333             | 0.886             | 0.651             | 0.311             | 0.48           | 0.6            | 0.091          | 0.738          | 0.612          | 0.639          |
| 0.866         | 6.0   | 372  | 0.9809          | 0.604    | 0.877 | 0.484             | 0.684             | 0.312             | 0.892             | 0.671             | 0.259             | 0.6            | 0.65           | 0.227          | 0.786          | 0.821          | 0.194          |
| 0.8203        | 7.0   | 434  | 0.9894          | 0.637    | 0.882 | 0.519             | 0.75              | 0.4               | 0.8               | 0.696             | 0.4               | 0.56           | 0.6            | 0.455          | 0.857          | 0.821          | 0.222          |
| 0.8024        | 8.0   | 496  | 0.9797          | 0.632    | 0.882 | 0.484             | 0.682             | 0.45              | 0.889             | 0.693             | 0.393             | 0.6            | 0.75           | 0.409          | 0.762          | 0.776          | 0.306          |
| 0.7558        | 9.0   | 558  | 0.9738          | 0.594    | 0.883 | 0.6               | 0.765             | 0.375             | 0.766             | 0.694             | 0.32              | 0.48           | 0.65           | 0.273          | 0.857          | 0.642          | 0.444          |
| 0.7319        | 10.0  | 620  | 0.9632          | 0.632    | 0.884 | 0.519             | 0.722             | 0.36              | 0.8               | 0.708             | 0.44              | 0.56           | 0.65           | 0.409          | 0.857          | 0.761          | 0.306          |


### Framework versions

- Transformers 4.45.1
- Pytorch 2.4.0
- Datasets 3.0.1
- Tokenizers 0.20.0
