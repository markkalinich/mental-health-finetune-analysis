---
license: apache-2.0
base_model: manucos/final-ft__roberta-base-biomedical-clinical-es__70k-ultrasounds
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: final-ft__roberta-base-biomedical-clinical-es__70k-ultrasounds-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# final-ft__roberta-base-biomedical-clinical-es__70k-ultrasounds-ner

This model is a fine-tuned version of [manucos/final-ft__roberta-base-biomedical-clinical-es__70k-ultrasounds](https://huggingface.co/manucos/final-ft__roberta-base-biomedical-clinical-es__70k-ultrasounds) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3148
- Precision: 0.8725
- Recall: 0.9022
- F1: 0.8871
- Accuracy: 0.9419

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
| No log        | 1.0   | 280  | 0.3056          | 0.7819    | 0.8444 | 0.8120 | 0.9198   |
| 0.4846        | 2.0   | 560  | 0.2545          | 0.8126    | 0.88   | 0.8450 | 0.9360   |
| 0.4846        | 3.0   | 840  | 0.2269          | 0.8671    | 0.8889 | 0.8778 | 0.9414   |
| 0.1366        | 4.0   | 1120 | 0.2519          | 0.8225    | 0.8993 | 0.8592 | 0.9372   |
| 0.1366        | 5.0   | 1400 | 0.2449          | 0.8472    | 0.9037 | 0.8746 | 0.9445   |
| 0.0788        | 6.0   | 1680 | 0.2839          | 0.8725    | 0.9022 | 0.8871 | 0.9419   |
| 0.0788        | 7.0   | 1960 | 0.2849          | 0.8631    | 0.8963 | 0.8794 | 0.9386   |
| 0.0441        | 8.0   | 2240 | 0.2987          | 0.8736    | 0.9007 | 0.8869 | 0.9397   |
| 0.0335        | 9.0   | 2520 | 0.3192          | 0.8602    | 0.9022 | 0.8807 | 0.9377   |
| 0.0335        | 10.0  | 2800 | 0.3094          | 0.8734    | 0.8993 | 0.8861 | 0.9414   |
| 0.0242        | 11.0  | 3080 | 0.3233          | 0.8748    | 0.9007 | 0.8876 | 0.9383   |
| 0.0242        | 12.0  | 3360 | 0.3215          | 0.8764    | 0.9037 | 0.8899 | 0.9417   |
| 0.0189        | 13.0  | 3640 | 0.3155          | 0.8684    | 0.8993 | 0.8836 | 0.9405   |
| 0.0189        | 14.0  | 3920 | 0.3156          | 0.8725    | 0.9022 | 0.8871 | 0.9425   |
| 0.0172        | 15.0  | 4200 | 0.3148          | 0.8725    | 0.9022 | 0.8871 | 0.9419   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
