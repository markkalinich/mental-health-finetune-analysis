---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: twitter_empathy_Miles
  results: []

widget:

- text: "We feel you and we care about you!"

- text: "I don't think I need to do anything."

- text: "As our global team focuses on producing critical medical devices and developing and deploying rapid diagnostic tests for COVID-19, BD is helping 7 non-profit partners advance their work to contain COVID-19, support healthcare workers and treat patients around the world."


- text: "...While we don't know if Covid19 is more than 2% lethal we have to remember that Family come first, before our work, before our social life and before our personal needs. We will all be tested soon as the disease spreads whether we care for ourselves or care for others."

- text: "@jeffiel with the words I was looking for. I acknowledge the pain Black Americans feel. I am here for you. And I understand the skepticism you have that meaningful change will arrive quickly. We will bend this system toward justice."
---
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_empathy_Miles

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1421
- Mse: 0.1421
- Mae: 0.2240
- R2: 0.0840
- Accuracy: 0.8190

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

| Training Loss | Epoch | Step | Validation Loss | Mse    | Mae    | R2      | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:-------:|:--------:|
| No log        | 1.0   | 125  | 0.1507          | 0.1507 | 0.2374 | 0.0279  | 0.8081   |
| No log        | 2.0   | 250  | 0.1554          | 0.1554 | 0.2196 | -0.0018 | 0.8129   |
| No log        | 3.0   | 375  | 0.1421          | 0.1421 | 0.2240 | 0.0840  | 0.8190   |


### Framework versions

- Transformers 4.30.1
- Pytorch 2.0.1+cu118
- Datasets 2.12.0
- Tokenizers 0.13.3
