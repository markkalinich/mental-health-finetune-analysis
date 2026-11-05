---
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: Bert Uncased + 
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tmp_trainer

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on an unknown dataset.

## Model description

More information needed
This repository contains code and instructions for fine-tuning a token classification model (BERT/DeBERTa) on the Ai4Bharat Naamapadam dataset for multilingual Named Entity Recognition (NER) across Indian languages. This work was done for the GE Hackathon PII detection challenge.

https://github.com/kaushiksaravanan/PII-Deberta-finetuning-Ai4Bharat-naamapadam

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed
https://github.com/kaushiksaravanan/PII-Deberta-finetuning-Ai4Bharat-naamapadam
Dataset: Ai4Bharat Naamapadam
Model: Google BERT
https://huggingface.co/datasets/ai4bharat/naamapadam

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.41.2
- Pytorch 2.1.2
- Datasets 2.19.2
- Tokenizers 0.19.1
