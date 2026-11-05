---
license: apache-2.0
base_model: albert-base-v2
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
model-index:
- name: Emotion_Albert
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: emotion
      type: emotion
      config: split
      split: validation
      args: split
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9295
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Emotion_Albert

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1537
- Accuracy: 0.9295

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.3094        | 1.0   | 1000 | 0.2669          | 0.9145   |
| 0.1776        | 2.0   | 2000 | 0.2013          | 0.928    |
| 0.1129        | 3.0   | 3000 | 0.1541          | 0.936    |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
