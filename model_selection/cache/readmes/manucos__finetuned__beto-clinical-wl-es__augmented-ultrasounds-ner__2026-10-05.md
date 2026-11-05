---
base_model: manucos/finetuned__beto-clinical-wl-es__augmented-ultrasounds
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: finetuned__beto-clinical-wl-es__augmented-ultrasounds-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned__beto-clinical-wl-es__augmented-ultrasounds-ner

This model is a fine-tuned version of [manucos/finetuned__beto-clinical-wl-es__augmented-ultrasounds](https://huggingface.co/manucos/finetuned__beto-clinical-wl-es__augmented-ultrasounds) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3556
- Precision: 0.8057
- Recall: 0.8897
- F1: 0.8456
- Accuracy: 0.9216

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 206  | 0.2470          | 0.7303    | 0.8441 | 0.7831 | 0.9080   |
| No log        | 2.0   | 412  | 0.2471          | 0.7632    | 0.8644 | 0.8106 | 0.9182   |
| 0.3075        | 3.0   | 618  | 0.2838          | 0.7661    | 0.8553 | 0.8082 | 0.9106   |
| 0.3075        | 4.0   | 824  | 0.3057          | 0.7802    | 0.8765 | 0.8255 | 0.9170   |
| 0.0622        | 5.0   | 1030 | 0.2932          | 0.7844    | 0.8836 | 0.8310 | 0.9204   |
| 0.0622        | 6.0   | 1236 | 0.3435          | 0.8037    | 0.8907 | 0.8449 | 0.9211   |
| 0.0622        | 7.0   | 1442 | 0.3464          | 0.8013    | 0.8856 | 0.8413 | 0.9196   |
| 0.0255        | 8.0   | 1648 | 0.3470          | 0.7980    | 0.8877 | 0.8404 | 0.9224   |
| 0.0255        | 9.0   | 1854 | 0.3556          | 0.8055    | 0.8887 | 0.8450 | 0.9201   |
| 0.0159        | 10.0  | 2060 | 0.3556          | 0.8057    | 0.8897 | 0.8456 | 0.9216   |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
