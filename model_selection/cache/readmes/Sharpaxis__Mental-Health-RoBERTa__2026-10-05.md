---
library_name: transformers
license: mit
base_model: FacebookAI/roberta-base
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: Mental-Health-RoBERTa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Mental-Health-RoBERTa

This model is a fine-tuned version of [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base) on an Mental Health Issues detection dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3713
- F1: 0.8578
- Acc: 0.8573

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Acc    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 0.5312        | 1.0   | 1255 | 0.4397          | 0.8295 | 0.8287 |
| 0.3378        | 2.0   | 2510 | 0.3662          | 0.8535 | 0.8534 |
| 0.262         | 3.0   | 3765 | 0.3713          | 0.8578 | 0.8573 |


### Framework versions

- Transformers 4.45.1
- Pytorch 2.4.0
- Datasets 3.0.1
- Tokenizers 0.20.0

### Labels
'Normal':0,'Depression':1,'Suicidal':2,'Anxiety':3,'Bipolar':4,'Stress':5,'Personality disorder':6