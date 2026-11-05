---
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: NHS-pubmedbert-binary
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NHS-pubmedbert-binary

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5861
- Accuracy: 0.8246
- Precision: 0.8180
- Recall: 0.8240
- F1: 0.8202

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.0592        | 1.0   | 397  | 0.3980          | 0.8246   | 0.8179    | 0.8220 | 0.8196 |
| 0.0542        | 2.0   | 794  | 0.4714          | 0.7943   | 0.7960    | 0.8064 | 0.7929 |
| 0.6307        | 3.0   | 1191 | 0.5861          | 0.8246   | 0.8180    | 0.8240 | 0.8202 |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
