---
library_name: transformers
license: cc-by-nc-4.0
base_model: mental/mental-bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mentalBERT-wellness-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mentalBERT-wellness-classifier

This model is a fine-tuned version of [mental/mental-bert-base-uncased](https://huggingface.co/mental/mental-bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0471
- Accuracy: 0.722
- Auc: 0.915
- Precision Class 0: 0.765
- Precision Class 1: 0.762
- Precision Class 2: 0.745
- Precision Class 3: 0.684
- Recall Class 0: 0.736
- Recall Class 1: 0.593
- Recall Class 2: 0.651
- Recall Class 3: 0.796
- F1 Score Class 0: 0.75
- F1 Score Class 1: 0.667
- F1 Score Class 2: 0.695
- F1 Score Class 3: 0.736

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Auc   | Precision Class 0 | Precision Class 1 | Precision Class 2 | Precision Class 3 | Recall Class 0 | Recall Class 1 | Recall Class 2 | Recall Class 3 | F1 Score Class 0 | F1 Score Class 1 | F1 Score Class 2 | F1 Score Class 3 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:--------------:|:--------------:|:--------------:|:--------------:|:----------------:|:----------------:|:----------------:|:----------------:|
| 0.0887        | 1.0   | 140  | 1.2702          | 0.73     | 0.91  | 0.783             | 0.773             | 0.746             | 0.693             | 0.679          | 0.63           | 0.698          | 0.806          | 0.727            | 0.694            | 0.721            | 0.745            |
| 0.2058        | 2.0   | 280  | 1.0340          | 0.718    | 0.916 | 0.75              | 0.72              | 0.736             | 0.694             | 0.736          | 0.667          | 0.619          | 0.786          | 0.743            | 0.692            | 0.672            | 0.737            |
| 0.1921        | 3.0   | 420  | 1.0234          | 0.739    | 0.919 | 0.733             | 0.731             | 0.75              | 0.737             | 0.83           | 0.704          | 0.667          | 0.745          | 0.779            | 0.717            | 0.706            | 0.741            |
| 0.184         | 4.0   | 560  | 1.0486          | 0.73     | 0.917 | 0.719             | 0.773             | 0.738             | 0.723             | 0.774          | 0.63           | 0.714          | 0.745          | 0.745            | 0.694            | 0.726            | 0.734            |
| 0.1666        | 5.0   | 700  | 1.0084          | 0.747    | 0.918 | 0.769             | 0.739             | 0.738             | 0.743             | 0.755          | 0.63           | 0.762          | 0.765          | 0.762            | 0.68             | 0.75             | 0.754            |
| 0.1558        | 6.0   | 840  | 1.0314          | 0.739    | 0.917 | 0.759             | 0.773             | 0.738             | 0.721             | 0.774          | 0.63           | 0.714          | 0.765          | 0.766            | 0.694            | 0.726            | 0.743            |
| 0.138         | 7.0   | 980  | 1.0733          | 0.73     | 0.915 | 0.776             | 0.773             | 0.75              | 0.693             | 0.717          | 0.63           | 0.667          | 0.806          | 0.745            | 0.694            | 0.706            | 0.745            |
| 0.1481        | 8.0   | 1120 | 1.0656          | 0.722    | 0.914 | 0.787             | 0.773             | 0.741             | 0.678             | 0.698          | 0.63           | 0.635          | 0.816          | 0.74             | 0.694            | 0.684            | 0.741            |
| 0.1433        | 9.0   | 1260 | 1.0520          | 0.718    | 0.915 | 0.765             | 0.762             | 0.741             | 0.678             | 0.736          | 0.593          | 0.635          | 0.796          | 0.75             | 0.667            | 0.684            | 0.732            |
| 0.1577        | 10.0  | 1400 | 1.0471          | 0.722    | 0.915 | 0.765             | 0.762             | 0.745             | 0.684             | 0.736          | 0.593          | 0.651          | 0.796          | 0.75             | 0.667            | 0.695            | 0.736            |


### Framework versions

- Transformers 4.45.1
- Pytorch 2.4.0
- Datasets 3.0.1
- Tokenizers 0.20.0
