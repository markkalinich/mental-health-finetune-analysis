---
license: apache-2.0
base_model: plncmm/roberta-clinical-wl-es
tags:
- generated_from_trainer
model-index:
- name: final-ft__roberta-clinical-wl-es__70k-ultrasounds
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# final-ft__roberta-clinical-wl-es__70k-ultrasounds

This model is a fine-tuned version of [plncmm/roberta-clinical-wl-es](https://huggingface.co/plncmm/roberta-clinical-wl-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6177

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss |
|:-------------:|:-------:|:----:|:---------------:|
| No log        | 0.9967  | 229  | 0.9228          |
| No log        | 1.9978  | 459  | 0.8047          |
| No log        | 2.9989  | 689  | 0.7665          |
| 0.958         | 4.0     | 919  | 0.7180          |
| 0.958         | 4.9967  | 1148 | 0.7044          |
| 0.958         | 5.9978  | 1378 | 0.6875          |
| 0.958         | 6.9989  | 1608 | 0.6674          |
| 0.7197        | 8.0     | 1838 | 0.6454          |
| 0.7197        | 8.9967  | 2067 | 0.6485          |
| 0.7197        | 9.9978  | 2297 | 0.6411          |
| 0.7197        | 10.9989 | 2527 | 0.6292          |
| 0.665         | 12.0    | 2757 | 0.6223          |
| 0.665         | 12.9967 | 2986 | 0.6311          |
| 0.665         | 13.9978 | 3216 | 0.6128          |
| 0.665         | 14.9989 | 3446 | 0.6141          |
| 0.6398        | 16.0    | 3676 | 0.6028          |
| 0.6398        | 16.9967 | 3905 | 0.6064          |
| 0.6398        | 17.9978 | 4135 | 0.6148          |
| 0.6398        | 18.9989 | 4365 | 0.6032          |
| 0.6398        | 19.9347 | 4580 | 0.6177          |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
