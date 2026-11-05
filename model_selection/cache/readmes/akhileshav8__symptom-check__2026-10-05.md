---
license: apache-2.0
base_model: distilgpt2
tags:
- generated_from_trainer
model-index:
- name: symptom-check
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# symptom-check

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6910

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.4284        | 1.0   | 920  | 0.8556          |
| 0.8893        | 2.0   | 1840 | 0.7561          |
| 0.8055        | 3.0   | 2760 | 0.7150          |
| 0.7702        | 4.0   | 3680 | 0.6964          |
| 0.7548        | 5.0   | 4600 | 0.6910          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
