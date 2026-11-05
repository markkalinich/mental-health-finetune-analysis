---
base_model: manucos/finetuned__roberta-base-biomedical-clinical-es__augmented-ultrasounds
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: finetuned__roberta-base-biomedical-clinical-es__augmented-ultrasounds-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned__roberta-base-biomedical-clinical-es__augmented-ultrasounds-ner

This model is a fine-tuned version of [manucos/finetuned__roberta-base-biomedical-clinical-es__augmented-ultrasounds](https://huggingface.co/manucos/finetuned__roberta-base-biomedical-clinical-es__augmented-ultrasounds) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3648
- Precision: 0.8205
- Recall: 0.8927
- F1: 0.8551
- Accuracy: 0.9264

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
| No log        | 1.0   | 206  | 0.2948          | 0.7527    | 0.8411 | 0.7945 | 0.9132   |
| No log        | 2.0   | 412  | 0.2572          | 0.7746    | 0.8522 | 0.8116 | 0.9235   |
| 0.4194        | 3.0   | 618  | 0.2866          | 0.7759    | 0.8482 | 0.8104 | 0.9215   |
| 0.4194        | 4.0   | 824  | 0.2813          | 0.7878    | 0.8866 | 0.8343 | 0.9235   |
| 0.0971        | 5.0   | 1030 | 0.2902          | 0.7969    | 0.8856 | 0.8389 | 0.9249   |
| 0.0971        | 6.0   | 1236 | 0.3229          | 0.8055    | 0.8846 | 0.8432 | 0.9239   |
| 0.0971        | 7.0   | 1442 | 0.3422          | 0.8028    | 0.8775 | 0.8385 | 0.9208   |
| 0.0459        | 8.0   | 1648 | 0.3215          | 0.8297    | 0.8877 | 0.8577 | 0.9253   |
| 0.0459        | 9.0   | 1854 | 0.3568          | 0.8119    | 0.8866 | 0.8476 | 0.9235   |
| 0.0285        | 10.0  | 2060 | 0.3520          | 0.8145    | 0.8887 | 0.8500 | 0.9235   |
| 0.0285        | 11.0  | 2266 | 0.3597          | 0.8255    | 0.8907 | 0.8569 | 0.9264   |
| 0.0285        | 12.0  | 2472 | 0.3599          | 0.8183    | 0.8887 | 0.8520 | 0.9266   |
| 0.0203        | 13.0  | 2678 | 0.3612          | 0.8195    | 0.8917 | 0.8541 | 0.9246   |
| 0.0203        | 14.0  | 2884 | 0.3649          | 0.8180    | 0.8917 | 0.8533 | 0.9258   |
| 0.0164        | 15.0  | 3090 | 0.3648          | 0.8205    | 0.8927 | 0.8551 | 0.9264   |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
