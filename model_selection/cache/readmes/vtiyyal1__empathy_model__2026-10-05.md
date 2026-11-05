---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: empathy_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# empathy_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0043
- Mse: 0.0043

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
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Mse    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0109        | 0.05  | 50   | 0.0050          | 0.0050 |
| 0.0063        | 0.11  | 100  | 0.0092          | 0.0092 |
| 0.0074        | 0.16  | 150  | 0.0045          | 0.0045 |
| 0.0056        | 0.22  | 200  | 0.0060          | 0.0060 |
| 0.0082        | 0.27  | 250  | 0.0046          | 0.0046 |
| 0.0055        | 0.32  | 300  | 0.0056          | 0.0056 |
| 0.0061        | 0.38  | 350  | 0.0045          | 0.0045 |
| 0.0079        | 0.43  | 400  | 0.0060          | 0.0060 |
| 0.0061        | 0.48  | 450  | 0.0043          | 0.0043 |
| 0.0078        | 0.54  | 500  | 0.0046          | 0.0046 |
| 0.0066        | 0.59  | 550  | 0.0043          | 0.0043 |
| 0.0055        | 0.65  | 600  | 0.0044          | 0.0044 |
| 0.0059        | 0.7   | 650  | 0.0043          | 0.0043 |
| 0.0048        | 0.75  | 700  | 0.0056          | 0.0056 |
| 0.0051        | 0.81  | 750  | 0.0043          | 0.0043 |
| 0.0046        | 0.86  | 800  | 0.0043          | 0.0043 |
| 0.0055        | 0.92  | 850  | 0.0043          | 0.0043 |
| 0.0053        | 0.97  | 900  | 0.0043          | 0.0043 |


### Framework versions

- Transformers 4.39.1
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
