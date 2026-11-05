---
base_model: plncmm/beto-clinical-wl-es
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: beto-clinical-wl-es-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# beto-clinical-wl-es-ner

This model is a fine-tuned version of [plncmm/beto-clinical-wl-es](https://huggingface.co/plncmm/beto-clinical-wl-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3299
- Precision: 0.8665
- Recall: 0.9037
- F1: 0.8847
- Accuracy: 0.9418

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 280  | 0.2544          | 0.8328    | 0.8489 | 0.8408 | 0.9247   |
| 0.3847        | 2.0   | 560  | 0.2645          | 0.8170    | 0.8667 | 0.8411 | 0.9236   |
| 0.3847        | 3.0   | 840  | 0.2372          | 0.8512    | 0.8726 | 0.8617 | 0.9338   |
| 0.1056        | 4.0   | 1120 | 0.2749          | 0.8403    | 0.8963 | 0.8674 | 0.9327   |
| 0.1056        | 5.0   | 1400 | 0.2895          | 0.8557    | 0.9052 | 0.8798 | 0.9354   |
| 0.057         | 6.0   | 1680 | 0.2630          | 0.8707    | 0.9081 | 0.8891 | 0.9408   |
| 0.057         | 7.0   | 1960 | 0.2759          | 0.8614    | 0.9022 | 0.8813 | 0.9418   |
| 0.031         | 8.0   | 2240 | 0.3099          | 0.8689    | 0.9037 | 0.8860 | 0.9408   |
| 0.0222        | 9.0   | 2520 | 0.3506          | 0.8597    | 0.9081 | 0.8833 | 0.9386   |
| 0.0222        | 10.0  | 2800 | 0.2962          | 0.8693    | 0.8963 | 0.8826 | 0.9421   |
| 0.0169        | 11.0  | 3080 | 0.3218          | 0.8709    | 0.8993 | 0.8848 | 0.9432   |
| 0.0169        | 12.0  | 3360 | 0.3459          | 0.8672    | 0.9096 | 0.8879 | 0.9400   |
| 0.0134        | 13.0  | 3640 | 0.3299          | 0.8661    | 0.9007 | 0.8831 | 0.9413   |
| 0.0134        | 14.0  | 3920 | 0.3318          | 0.8707    | 0.9081 | 0.8891 | 0.9429   |
| 0.0126        | 15.0  | 4200 | 0.3299          | 0.8665    | 0.9037 | 0.8847 | 0.9418   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
