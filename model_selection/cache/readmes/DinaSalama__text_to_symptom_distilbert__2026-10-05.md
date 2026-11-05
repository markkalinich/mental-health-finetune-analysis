---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: text_to_symptom_distbert
  results: []
datasets:
- venetis/symptom_text_to_disease_mk4
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# text_to_symptom_distbert

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on [venetis/symptom_text_to_disease_mk4](https://huggingface.co/datasets/venetis/symptom_text_to_disease_mk4/viewer/venetis--symptom_text_to_disease_mk4/).

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 30

### Training results



### Framework versions

- Transformers 4.30.2
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.13.3