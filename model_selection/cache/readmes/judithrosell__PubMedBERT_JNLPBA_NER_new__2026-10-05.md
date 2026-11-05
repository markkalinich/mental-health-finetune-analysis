---
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: PubMedBERT_JNLPBA_NER_new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PubMedBERT_JNLPBA_NER_new

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1464
- Precision: 0.9598
- Recall: 0.9557
- F1: 0.9577
- Accuracy: 0.9520

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
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1709        | 1.0   | 1164 | 0.1493          | 0.9566    | 0.9534 | 0.9550 | 0.9492   |
| 0.134         | 2.0   | 2328 | 0.1501          | 0.9585    | 0.9549 | 0.9567 | 0.9501   |
| 0.112         | 3.0   | 3492 | 0.1464          | 0.9598    | 0.9557 | 0.9577 | 0.9520   |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.0
