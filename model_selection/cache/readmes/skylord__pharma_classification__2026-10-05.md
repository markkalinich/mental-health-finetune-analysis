---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: pharma_classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pharma_classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5315
- Accuracy: 0.9581
- F1: 0.9506

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 30000

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 0.0035        | 5.99  | 5000  | 0.2892          | 0.9539   | 0.9554 |
| 0.0137        | 11.98 | 10000 | 0.2620          | 0.9641   | 0.9600 |
| 0.0           | 17.96 | 15000 | 0.4022          | 0.9611   | 0.9586 |
| 0.0001        | 23.95 | 20000 | 0.3838          | 0.9611   | 0.9552 |
| 0.0           | 29.94 | 25000 | 0.4363          | 0.9575   | 0.9490 |
| 0.0           | 35.93 | 30000 | 0.5315          | 0.9581   | 0.9506 |


### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.2.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
