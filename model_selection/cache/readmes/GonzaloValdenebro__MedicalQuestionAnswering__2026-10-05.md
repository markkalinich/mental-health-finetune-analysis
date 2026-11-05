---
license: apache-2.0
base_model: Intel/dynamic_tinybert
tags:
- generated_from_trainer
model-index:
- name: MedicalQuestionAnswering
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedicalQuestionAnswering

This model is a fine-tuned version of [Intel/dynamic_tinybert](https://huggingface.co/Intel/dynamic_tinybert) on the [Medical Question Asnwering Dataset](https://huggingface.co/datasets/GonzaloValdenebro/MedicalQuestionAnsweringDataset).

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results



### Framework versions

- Transformers 4.33.1
- Pytorch 2.1.0
- Datasets 2.14.5
- Tokenizers 0.13.3
