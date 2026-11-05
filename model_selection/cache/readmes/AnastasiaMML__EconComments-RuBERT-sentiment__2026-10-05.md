---
license: apache-2.0
language:
- ru
base_model: ai-forever/ruBert-base
tags:
- economic comments
- sentiment
- multiclass
pipeline_tag: text-classification
---

# EconComments-RuBERT-sentiment

This model is a fine-tuned version of [ai-forever/ruBert-base](https://huggingface.co/ai-forever/ruBert-base) 
on a dataset of 7,000 Russian-language comments on economic topics from the VKontakte social network

## Task
For comments on economic topics from the social network, the task of multiclass sentiment classification into 3 classes (negative, neutral, positive) was solved
- Quadratic Weighted Kappa: 0.532

## Training hyperparameters
- learning_rate: 1e-05
- weight_decay: 0.01
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- num_epochs: 2

