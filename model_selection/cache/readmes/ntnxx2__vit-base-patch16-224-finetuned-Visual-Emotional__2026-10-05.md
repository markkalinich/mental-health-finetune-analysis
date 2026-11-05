---
library_name: transformers
license: apache-2.0
base_model: google/vit-base-patch16-224
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vit-base-patch16-224-finetuned-Visual-Emotional
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
      value: 0.65
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-finetuned-Visual-Emotional

This model is a fine-tuned version of [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0819
- Accuracy: 0.65

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 32

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Accuracy |
|:-------------:|:-------:|:----:|:---------------:|:--------:|
| No log        | 0.8696  | 5    | 2.1918          | 0.1125   |
| 2.1428        | 1.9130  | 11   | 2.1017          | 0.1625   |
| 2.1428        | 2.9565  | 17   | 1.9293          | 0.1875   |
| 1.8582        | 4.0     | 23   | 1.7163          | 0.325    |
| 1.8582        | 4.8696  | 28   | 1.5777          | 0.375    |
| 1.4818        | 5.9130  | 34   | 1.4303          | 0.45     |
| 1.1661        | 6.9565  | 40   | 1.3146          | 0.475    |
| 1.1661        | 8.0     | 46   | 1.2160          | 0.525    |
| 0.9421        | 8.8696  | 51   | 1.2096          | 0.55     |
| 0.9421        | 9.9130  | 57   | 1.1362          | 0.5875   |
| 0.8003        | 10.9565 | 63   | 1.1598          | 0.525    |
| 0.8003        | 12.0    | 69   | 1.0878          | 0.6      |
| 0.678         | 12.8696 | 74   | 1.0940          | 0.6375   |
| 0.5888        | 13.9130 | 80   | 1.0819          | 0.65     |
| 0.5888        | 14.9565 | 86   | 1.0700          | 0.625    |
| 0.5086        | 16.0    | 92   | 1.0758          | 0.625    |
| 0.5086        | 16.8696 | 97   | 1.0804          | 0.625    |
| 0.4454        | 17.9130 | 103  | 1.0704          | 0.6      |
| 0.4454        | 18.9565 | 109  | 1.1111          | 0.575    |
| 0.3758        | 20.0    | 115  | 1.0619          | 0.5875   |
| 0.3402        | 20.8696 | 120  | 1.0846          | 0.6125   |
| 0.3402        | 21.9130 | 126  | 1.1042          | 0.6125   |
| 0.3247        | 22.9565 | 132  | 1.0926          | 0.6375   |
| 0.3247        | 24.0    | 138  | 1.0908          | 0.625    |
| 0.3142        | 24.8696 | 143  | 1.0964          | 0.6      |
| 0.3142        | 25.9130 | 149  | 1.0999          | 0.6125   |
| 0.3081        | 26.9565 | 155  | 1.1036          | 0.625    |
| 0.276         | 27.8261 | 160  | 1.1019          | 0.625    |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Datasets 3.0.2
- Tokenizers 0.19.1
