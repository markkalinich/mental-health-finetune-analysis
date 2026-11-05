---
license: mit
base_model: Clinical-AI-Apollo/Medical-NER
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Medical-NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Medical-NER

This model is a fine-tuned version of [Clinical-AI-Apollo/Medical-NER](https://huggingface.co/Clinical-AI-Apollo/Medical-NER) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1694
- Precision: 0.9149
- Recall: 0.8666
- F1: 0.8901
- Accuracy: 0.9427

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.2
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0013        | 1.0   | 4159 | 0.1694          | 0.9149    | 0.8666 | 0.8901 | 0.9427   |


### Framework versions

- Transformers 4.37.0
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.1
