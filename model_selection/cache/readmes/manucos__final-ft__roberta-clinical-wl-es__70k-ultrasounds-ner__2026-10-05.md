---
license: apache-2.0
base_model: manucos/final-ft__roberta-clinical-wl-es__70k-ultrasounds
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: final-ft__roberta-clinical-wl-es__70k-ultrasounds-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# final-ft__roberta-clinical-wl-es__70k-ultrasounds-ner

This model is a fine-tuned version of [manucos/final-ft__roberta-clinical-wl-es__70k-ultrasounds](https://huggingface.co/manucos/final-ft__roberta-clinical-wl-es__70k-ultrasounds) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3411
- Precision: 0.8624
- Recall: 0.9007
- F1: 0.8812
- Accuracy: 0.9380

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
| No log        | 1.0   | 280  | 0.3115          | 0.7961    | 0.8444 | 0.8196 | 0.9220   |
| 0.5059        | 2.0   | 560  | 0.2686          | 0.8117    | 0.8815 | 0.8452 | 0.9321   |
| 0.5059        | 3.0   | 840  | 0.2472          | 0.8623    | 0.8815 | 0.8718 | 0.9386   |
| 0.143         | 4.0   | 1120 | 0.2720          | 0.8505    | 0.8933 | 0.8714 | 0.9341   |
| 0.143         | 5.0   | 1400 | 0.2730          | 0.8541    | 0.8933 | 0.8733 | 0.9366   |
| 0.0852        | 6.0   | 1680 | 0.2987          | 0.8665    | 0.9037 | 0.8847 | 0.9394   |
| 0.0852        | 7.0   | 1960 | 0.2896          | 0.8671    | 0.8993 | 0.8829 | 0.9374   |
| 0.0475        | 8.0   | 2240 | 0.3160          | 0.8770    | 0.9081 | 0.8923 | 0.9405   |
| 0.0334        | 9.0   | 2520 | 0.3321          | 0.8640    | 0.9037 | 0.8834 | 0.9377   |
| 0.0334        | 10.0  | 2800 | 0.3392          | 0.8696    | 0.8993 | 0.8842 | 0.9374   |
| 0.0248        | 11.0  | 3080 | 0.3368          | 0.8636    | 0.9007 | 0.8818 | 0.9394   |
| 0.0248        | 12.0  | 3360 | 0.3502          | 0.8655    | 0.8963 | 0.8806 | 0.9358   |
| 0.0209        | 13.0  | 3640 | 0.3377          | 0.8755    | 0.8963 | 0.8858 | 0.9405   |
| 0.0209        | 14.0  | 3920 | 0.3408          | 0.8624    | 0.9007 | 0.8812 | 0.9383   |
| 0.0175        | 15.0  | 4200 | 0.3411          | 0.8624    | 0.9007 | 0.8812 | 0.9380   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
