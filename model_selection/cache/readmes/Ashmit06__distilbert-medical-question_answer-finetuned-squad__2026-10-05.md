---
license: apache-2.0
base_model: OnePoint16/distilbert-medical-question_answer
tags:
- generated_from_trainer
model-index:
- name: distilbert-medical-question_answer-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-medical-question_answer-finetuned-squad

This model is a fine-tuned version of [OnePoint16/distilbert-medical-question_answer](https://huggingface.co/OnePoint16/distilbert-medical-question_answer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1247

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

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 32   | 2.6234          |
| No log        | 2.0   | 64   | 2.1904          |
| No log        | 3.0   | 96   | 2.1247          |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.1+cu121
- Datasets 2.19.2
- Tokenizers 0.19.1
