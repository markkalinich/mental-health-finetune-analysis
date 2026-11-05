---
base_model: distilbert-base-uncased
library_name: transformers
license: apache-2.0
metrics:
- accuracy
tags:
- generated_from_trainer
model-index:
- name: medical_condition_classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_condition_classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an [Drugs.com](https://archive.ics.uci.edu/dataset/462/drug+review+dataset+drugs+com) dataset.
It achieves the following results on the test data set:
- Loss: 0.8930
- Accuracy: 0.7951

## Model description

The Goal of the model is to predict the medical condition based on the review of the drug. There're `751` classes.

## Intended uses & limitations

More information needed

## Training and evaluation data

The training, evaluation & testing data can be found under [samsaara/medical_condition_classification](https://huggingface.co/datasets/samsaara/medical_condition_classification) of the 🤗 `Datasets` and the process itself can be found in the `modeling.ipynb` notebook.

By default, the dataset has `train, test` splits. `train` is then further divided into `train, validation` splits with `0.8, 0.2` ratio. Final results shown are on the `test` dataset.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Accuracy |
|:-------------:|:------:|:-----:|:---------------:|:--------:|
| 1.8625        | 0.4329 | 2000  | 1.7199          | 0.6397   |
| 1.459         | 0.8658 | 4000  | 1.3696          | 0.6890   |
| 1.1737        | 1.2987 | 6000  | 1.2131          | 0.7172   |
| 1.042         | 1.7316 | 8000  | 1.1014          | 0.7329   |
| 0.8431        | 2.1645 | 10000 | 1.0322          | 0.7510   |
| 0.8012        | 2.5974 | 12000 | 0.9889          | 0.7587   |
| 0.7312        | 3.0303 | 14000 | 0.9497          | 0.7727   |
| 0.6561        | 3.4632 | 16000 | 0.9338          | 0.7805   |
| 0.6132        | 3.8961 | 18000 | 0.9073          | 0.7875   |
| 0.5195        | 4.3290 | 20000 | 0.9011          | 0.7929   |
| 0.5015        | 4.7619 | 22000 | 0.8930          | 0.7951   |


### Framework versions

- Transformers 4.45.2
- Pytorch 2.4.1
- Datasets 3.0.1
- Tokenizers 0.20.1
