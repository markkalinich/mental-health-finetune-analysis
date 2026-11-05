---
license: apache-2.0
base_model: plncmm/roberta-clinical-wl-es
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: roberta-clinical-wl-es-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-clinical-wl-es-ner

This model is a fine-tuned version of [plncmm/roberta-clinical-wl-es](https://huggingface.co/plncmm/roberta-clinical-wl-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3453
- Precision: 0.8647
- Recall: 0.8993
- F1: 0.8816
- Accuracy: 0.9391

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
| No log        | 1.0   | 280  | 0.3149          | 0.7822    | 0.8356 | 0.8080 | 0.9164   |
| 0.5325        | 2.0   | 560  | 0.2693          | 0.8291    | 0.8696 | 0.8489 | 0.9271   |
| 0.5325        | 3.0   | 840  | 0.2509          | 0.8438    | 0.8726 | 0.8580 | 0.9299   |
| 0.1484        | 4.0   | 1120 | 0.2511          | 0.8425    | 0.9037 | 0.8721 | 0.9380   |
| 0.1484        | 5.0   | 1400 | 0.2873          | 0.8371    | 0.8830 | 0.8594 | 0.9307   |
| 0.0854        | 6.0   | 1680 | 0.3025          | 0.8725    | 0.9022 | 0.8871 | 0.9403   |
| 0.0854        | 7.0   | 1960 | 0.3040          | 0.8610    | 0.8993 | 0.8797 | 0.9403   |
| 0.0499        | 8.0   | 2240 | 0.3211          | 0.8683    | 0.8889 | 0.8785 | 0.9363   |
| 0.0359        | 9.0   | 2520 | 0.3294          | 0.8620    | 0.8978 | 0.8795 | 0.9366   |
| 0.0359        | 10.0  | 2800 | 0.3374          | 0.8900    | 0.8993 | 0.8946 | 0.9394   |
| 0.0248        | 11.0  | 3080 | 0.3543          | 0.8712    | 0.8919 | 0.8814 | 0.9372   |
| 0.0248        | 12.0  | 3360 | 0.3390          | 0.8606    | 0.8963 | 0.8781 | 0.9366   |
| 0.0209        | 13.0  | 3640 | 0.3337          | 0.8712    | 0.9022 | 0.8865 | 0.9394   |
| 0.0209        | 14.0  | 3920 | 0.3449          | 0.8698    | 0.9007 | 0.8850 | 0.9391   |
| 0.0182        | 15.0  | 4200 | 0.3453          | 0.8647    | 0.8993 | 0.8816 | 0.9391   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
