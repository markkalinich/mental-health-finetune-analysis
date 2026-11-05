---
base_model: manucos/final-ft__beto-clinical-wl-es__70k-ultrasounds
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: final-ft__beto-clinical-wl-es__70k-ultrasounds-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# final-ft__beto-clinical-wl-es__70k-ultrasounds-ner

This model is a fine-tuned version of [manucos/final-ft__beto-clinical-wl-es__70k-ultrasounds](https://huggingface.co/manucos/final-ft__beto-clinical-wl-es__70k-ultrasounds) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3314
- Precision: 0.8841
- Recall: 0.9156
- F1: 0.8996
- Accuracy: 0.9469

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
| No log        | 1.0   | 280  | 0.2352          | 0.8355    | 0.8652 | 0.8501 | 0.9295   |
| 0.3458        | 2.0   | 560  | 0.2126          | 0.8347    | 0.8904 | 0.8616 | 0.9354   |
| 0.3458        | 3.0   | 840  | 0.2240          | 0.8670    | 0.8978 | 0.8821 | 0.9389   |
| 0.1005        | 4.0   | 1120 | 0.2357          | 0.8478    | 0.8993 | 0.8728 | 0.9408   |
| 0.1005        | 5.0   | 1400 | 0.2944          | 0.8738    | 0.9126 | 0.8928 | 0.9416   |
| 0.0527        | 6.0   | 1680 | 0.2760          | 0.8971    | 0.9170 | 0.9070 | 0.9459   |
| 0.0527        | 7.0   | 1960 | 0.2987          | 0.8791    | 0.9052 | 0.8920 | 0.9408   |
| 0.0313        | 8.0   | 2240 | 0.2889          | 0.8811    | 0.9111 | 0.8958 | 0.9464   |
| 0.0217        | 9.0   | 2520 | 0.3301          | 0.8802    | 0.9037 | 0.8918 | 0.9394   |
| 0.0217        | 10.0  | 2800 | 0.3171          | 0.8937    | 0.9096 | 0.9016 | 0.9459   |
| 0.016         | 11.0  | 3080 | 0.3314          | 0.8973    | 0.9185 | 0.9078 | 0.9477   |
| 0.016         | 12.0  | 3360 | 0.3348          | 0.8879    | 0.9156 | 0.9015 | 0.9459   |
| 0.0122        | 13.0  | 3640 | 0.3349          | 0.8857    | 0.9185 | 0.9018 | 0.9461   |
| 0.0122        | 14.0  | 3920 | 0.3292          | 0.8841    | 0.9156 | 0.8996 | 0.9469   |
| 0.0115        | 15.0  | 4200 | 0.3314          | 0.8841    | 0.9156 | 0.8996 | 0.9469   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
