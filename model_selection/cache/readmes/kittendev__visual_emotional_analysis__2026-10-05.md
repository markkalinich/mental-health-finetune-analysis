---
license: apache-2.0
base_model: google/vit-base-patch16-224-in21k
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: visual_emotional_analysis
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.55625
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# visual_emotional_analysis

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2815
- Accuracy: 0.5563

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 20   | 1.8308          | 0.375    |
| No log        | 2.0   | 40   | 1.5510          | 0.4875   |
| No log        | 3.0   | 60   | 1.4138          | 0.5062   |
| No log        | 4.0   | 80   | 1.3845          | 0.4875   |
| No log        | 5.0   | 100  | 1.3245          | 0.525    |
| No log        | 6.0   | 120  | 1.2645          | 0.6      |
| No log        | 7.0   | 140  | 1.2887          | 0.5188   |
| No log        | 8.0   | 160  | 1.2395          | 0.5875   |
| No log        | 9.0   | 180  | 1.2267          | 0.55     |
| No log        | 10.0  | 200  | 1.1883          | 0.6      |


### Framework versions

- Transformers 4.33.2
- Pytorch 2.0.1+cu118
- Datasets 2.14.5
- Tokenizers 0.13.3
