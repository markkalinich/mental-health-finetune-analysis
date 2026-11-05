---
license: apache-2.0
base_model: distilbert/distilbert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: my_Pytorch_pii_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_Pytorch_pii_model

This model is a fine-tuned version of [distilbert/distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0593
- Precision: 0.9370
- Recall: 0.9595
- F1: 0.9481
- Accuracy: 0.9816

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine_with_restarts
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.06          | 1.0   | 10463 | 0.0544          | 0.9232    | 0.9433 | 0.9331 | 0.9753   |
| 0.0507        | 2.0   | 20926 | 0.0484          | 0.9342    | 0.9536 | 0.9438 | 0.9782   |
| 0.04          | 3.0   | 31389 | 0.0473          | 0.9347    | 0.9558 | 0.9451 | 0.9800   |
| 0.0272        | 4.0   | 41852 | 0.0549          | 0.9379    | 0.9591 | 0.9484 | 0.9811   |
| 0.0209        | 5.0   | 52315 | 0.0593          | 0.9370    | 0.9595 | 0.9481 | 0.9816   |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
