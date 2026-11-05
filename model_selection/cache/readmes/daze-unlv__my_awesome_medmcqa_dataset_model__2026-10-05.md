---
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: my_awesome_medmcqa_dataset_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_medmcqa_dataset_model

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5770
- Accuracy: 0.3624

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3078        | 1.0   | 2857 | 1.3420          | 0.3359   |
| 1.1281        | 2.0   | 5714 | 1.4420          | 0.3634   |
| 0.9295        | 3.0   | 8571 | 1.5770          | 0.3624   |


### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.2.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.0
