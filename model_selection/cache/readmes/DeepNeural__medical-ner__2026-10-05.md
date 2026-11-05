---
license: apache-2.0
language:
- en
metrics:
- seqeval
base_model:
- google-bert/bert-base-uncased
pipeline_tag: token-classification
library_name: transformers
tags:
- medical
- healthcare
---
# Model Name: DeepNeural_NER-I

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bert-base-uncased

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on the medical-ner-bleurt-separated dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0
- F1: 1.0

## Model description

The DeepNeural NER-I model is exclusively designed to identify body parts in textual documents. 
This clinical support model is one of many to be released, and is a crucial aspect  of clinical support systems. 

## Intended uses & limitations

The model is meant to be used for research and development purposes by Data Scientists, ML & Software Engineers for the development of NER applications 
capable of identifying body parts in medical EHR systems to augment patient health processing.

## Training and evaluation data

Training 

## Training procedure
The DeepNeural_NER-I model was trained with precision and accuracy in mind, and therefore 
the model was trained for 3 epochs and 13500 global steps per epoch. The training scores utilized
are highlighted in the table below.

| Training Method | # Score |
|:-------------:|:-----:|
| Precision       | 1.0   |           
| Recall         | 1.0   |            
| F1-Score        | 1.0  |            
| Accuracy       | 1.0   |          

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 24
- eval_batch_size: 24
- lr_scheduler_type: linear
- num_epochs: 3
- weight_decay: 0.01

### Training results

| Training Loss | Epoch |  Validation Loss | F1     |
|:-------------:|:-----:|:---------------:|:------:|
| 2.61          | 1.0   | 0.0          | 1.0 |
| 2.61          | 2.0   | 0.0          | 1.0 |
| 2.61          | 3.0   | 0.0          | 1.0 |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
