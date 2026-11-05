---
license: apache-2.0
language:
- ru
base_model:
- ai-forever/ruRoberta-large
tags:
- economic comments
- sentiment
- multiclass
pipeline_tag: text-classification
---
# LoRA-RuRoBERTa-econ-sentiment
This model is a LoRA fine-tuned version of [ai-forever/ruRoberta-large](https://huggingface.co/ai-forever/ruRoberta-large) on a dataset of 7,000 Russian-language comments on economic topics from the VKontakte social network

## Task
For comments on economic topics from the social network, the task of multiclass sentiment classification into 3 classes (negative, neutral, positive) was solved
- Quadratic Weighted Kappa: 0.625

## Training hyperparameters
- batch_size: 32
- grad_acc_steps: 2
- max_length: 512
- num_epochs: 5
- use_mixed_precision: True

- LoRA_r: 16
- LoRA_alpha: 32
- LoRA_dropout: 0.1

- optimizer: AdamW
- learning_rate: 2e-4
- weight_decay: 0.01

