---
license: apache-2.0
base_model: distilgpt2
tags:
- generated_from_trainer
model-index:
- name: symptom-check-april-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# symptom-check-april-3

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6371

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.4394        | 1.0   | 925  | 0.8613          |
| 0.8897        | 2.0   | 1850 | 0.7525          |
| 0.7971        | 3.0   | 2775 | 0.7043          |
| 0.7505        | 4.0   | 3700 | 0.6795          |
| 0.7253        | 5.0   | 4625 | 0.6628          |
| 0.7079        | 6.0   | 5550 | 0.6519          |
| 0.6999        | 7.0   | 6475 | 0.6450          |
| 0.692         | 8.0   | 7400 | 0.6404          |
| 0.6859        | 9.0   | 8325 | 0.6379          |
| 0.6821        | 10.0  | 9250 | 0.6371          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
