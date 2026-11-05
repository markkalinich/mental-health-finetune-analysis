---
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: model-mental-health-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model-mental-health-classification

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1549
- Accuracy: 0.5855

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.1217        | 1.0   | 1642 | 1.1627          | 0.5653   |
| 0.9457        | 2.0   | 3284 | 1.1549          | 0.5855   |
| 0.6765        | 3.0   | 4926 | 1.2525          | 0.5725   |
| 0.487         | 4.0   | 6568 | 1.4481          | 0.5718   |
| 0.3557        | 5.0   | 8210 | 1.5812          | 0.5639   |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
