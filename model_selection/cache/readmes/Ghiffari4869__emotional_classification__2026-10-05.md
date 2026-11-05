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
- name: emotional_classification
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
      value: 0.59375
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotional_classification

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1401
- Accuracy: 0.5938

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 40   | 1.7535          | 0.3375   |
| No log        | 2.0   | 80   | 1.5659          | 0.3875   |
| No log        | 3.0   | 120  | 1.4480          | 0.4562   |
| No log        | 4.0   | 160  | 1.3839          | 0.4938   |
| No log        | 5.0   | 200  | 1.3246          | 0.5125   |
| No log        | 6.0   | 240  | 1.3297          | 0.4875   |
| No log        | 7.0   | 280  | 1.2665          | 0.5312   |
| No log        | 8.0   | 320  | 1.2979          | 0.5625   |
| No log        | 9.0   | 360  | 1.1959          | 0.5687   |
| No log        | 10.0  | 400  | 1.2104          | 0.55     |
| No log        | 11.0  | 440  | 1.2401          | 0.5687   |
| No log        | 12.0  | 480  | 1.1960          | 0.5437   |
| 1.0885        | 13.0  | 520  | 1.1571          | 0.6188   |
| 1.0885        | 14.0  | 560  | 1.2241          | 0.575    |
| 1.0885        | 15.0  | 600  | 1.2355          | 0.5625   |
| 1.0885        | 16.0  | 640  | 1.1830          | 0.6      |
| 1.0885        | 17.0  | 680  | 1.2906          | 0.5625   |
| 1.0885        | 18.0  | 720  | 1.2705          | 0.525    |
| 1.0885        | 19.0  | 760  | 1.2643          | 0.5563   |
| 1.0885        | 20.0  | 800  | 1.1538          | 0.5813   |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1
