---
license: apache-2.0
base_model: plncmm/roberta-clinical-wl-es
tags:
- generated_from_trainer
model-index:
- name: finetuned__roberta-clinical-wl-es__augmented-ultrasounds
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned__roberta-clinical-wl-es__augmented-ultrasounds

This model is a fine-tuned version of [plncmm/roberta-clinical-wl-es](https://huggingface.co/plncmm/roberta-clinical-wl-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6340

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

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 198  | 0.9956          |
| No log        | 2.0   | 396  | 0.8742          |
| No log        | 3.0   | 594  | 0.8004          |
| 1.0236        | 4.0   | 792  | 0.7610          |
| 1.0236        | 5.0   | 990  | 0.7348          |
| 1.0236        | 6.0   | 1188 | 0.7259          |
| 1.0236        | 7.0   | 1386 | 0.7036          |
| 0.7694        | 8.0   | 1584 | 0.6969          |
| 0.7694        | 9.0   | 1782 | 0.6789          |
| 0.7694        | 10.0  | 1980 | 0.6774          |
| 0.7694        | 11.0  | 2178 | 0.6756          |
| 0.7115        | 12.0  | 2376 | 0.6663          |
| 0.7115        | 13.0  | 2574 | 0.6564          |
| 0.7115        | 14.0  | 2772 | 0.6517          |
| 0.7115        | 15.0  | 2970 | 0.6511          |
| 0.6834        | 16.0  | 3168 | 0.6383          |
| 0.6834        | 17.0  | 3366 | 0.6400          |
| 0.6834        | 18.0  | 3564 | 0.6483          |
| 0.6834        | 19.0  | 3762 | 0.6439          |
| 0.6716        | 20.0  | 3960 | 0.6340          |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
