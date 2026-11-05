---
license: apache-2.0
base_model: pradanaadn/vit-emotional-classifier
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vit-emotional-classifier
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
      value: 0.65625
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-emotional-classifier

This model is a fine-tuned version of [pradanaadn/vit-emotional-classifier](https://huggingface.co/pradanaadn/vit-emotional-classifier) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1495
- Accuracy: 0.6562

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.4801        | 0.5   | 20   | 1.2238          | 0.5875   |
| 0.4681        | 1.0   | 40   | 1.2062          | 0.6188   |
| 0.3414        | 1.5   | 60   | 1.1674          | 0.6      |
| 0.2972        | 2.0   | 80   | 1.1362          | 0.6125   |
| 0.2503        | 2.5   | 100  | 1.1508          | 0.6      |
| 0.1872        | 3.0   | 120  | 1.1495          | 0.6562   |
| 0.1929        | 3.5   | 140  | 1.1998          | 0.5875   |
| 0.1883        | 4.0   | 160  | 1.2023          | 0.5938   |
| 0.1729        | 4.5   | 180  | 1.2130          | 0.6      |
| 0.2007        | 5.0   | 200  | 1.2021          | 0.5813   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.2
- Tokenizers 0.19.1
