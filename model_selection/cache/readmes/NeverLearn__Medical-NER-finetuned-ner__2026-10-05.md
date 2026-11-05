---
license: mit
base_model: Clinical-AI-Apollo/Medical-NER
tags:
- generated_from_trainer
datasets:
- maccrobat_biomedical_ner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Medical-NER-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: maccrobat_biomedical_ner
      type: maccrobat_biomedical_ner
      config: default
      split: train
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.842486314674201
    - name: Recall
      type: recall
      value: 0.8537938439513243
    - name: F1
      type: f1
      value: 0.8481023908985867
    - name: Accuracy
      type: accuracy
      value: 0.9046288534972525
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Medical-NER-finetuned-ner

This model is a fine-tuned version of [Clinical-AI-Apollo/Medical-NER](https://huggingface.co/Clinical-AI-Apollo/Medical-NER) on the maccrobat_biomedical_ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5635
- Precision: 0.8425
- Recall: 0.8538
- F1: 0.8481
- Accuracy: 0.9046

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8.26814930103799e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 20   | 0.3925          | 0.8364    | 0.8307 | 0.8335 | 0.8912   |
| No log        | 2.0   | 40   | 0.3671          | 0.8266    | 0.8529 | 0.8395 | 0.8954   |
| No log        | 3.0   | 60   | 0.4077          | 0.8073    | 0.8388 | 0.8227 | 0.8843   |
| No log        | 4.0   | 80   | 0.3630          | 0.8531    | 0.8463 | 0.8497 | 0.9045   |
| No log        | 5.0   | 100  | 0.3717          | 0.8413    | 0.8484 | 0.8449 | 0.9017   |
| No log        | 6.0   | 120  | 0.3721          | 0.8433    | 0.8425 | 0.8429 | 0.9015   |
| No log        | 7.0   | 140  | 0.3679          | 0.8553    | 0.8529 | 0.8541 | 0.9069   |
| No log        | 8.0   | 160  | 0.3840          | 0.8394    | 0.8504 | 0.8449 | 0.9012   |
| No log        | 9.0   | 180  | 0.4124          | 0.8430    | 0.8520 | 0.8475 | 0.9040   |
| No log        | 10.0  | 200  | 0.4328          | 0.8358    | 0.8450 | 0.8404 | 0.9004   |
| No log        | 11.0  | 220  | 0.4395          | 0.8395    | 0.8552 | 0.8473 | 0.9033   |
| No log        | 12.0  | 240  | 0.4490          | 0.8399    | 0.8490 | 0.8444 | 0.9011   |
| No log        | 13.0  | 260  | 0.4592          | 0.8411    | 0.8497 | 0.8454 | 0.9027   |
| No log        | 14.0  | 280  | 0.4623          | 0.8435    | 0.8525 | 0.8480 | 0.9047   |
| No log        | 15.0  | 300  | 0.4858          | 0.8416    | 0.8540 | 0.8478 | 0.9040   |
| No log        | 16.0  | 320  | 0.4986          | 0.8393    | 0.8499 | 0.8446 | 0.9019   |
| No log        | 17.0  | 340  | 0.5152          | 0.8367    | 0.8474 | 0.8420 | 0.9012   |
| No log        | 18.0  | 360  | 0.5138          | 0.8474    | 0.8508 | 0.8491 | 0.9055   |
| No log        | 19.0  | 380  | 0.5414          | 0.8384    | 0.8488 | 0.8436 | 0.9015   |
| No log        | 20.0  | 400  | 0.5483          | 0.8401    | 0.8508 | 0.8454 | 0.9029   |
| No log        | 21.0  | 420  | 0.5465          | 0.8386    | 0.8454 | 0.8420 | 0.9008   |
| No log        | 22.0  | 440  | 0.5463          | 0.8410    | 0.8520 | 0.8465 | 0.9034   |
| No log        | 23.0  | 460  | 0.5434          | 0.8441    | 0.8545 | 0.8493 | 0.9053   |
| No log        | 24.0  | 480  | 0.5516          | 0.8439    | 0.8493 | 0.8466 | 0.9041   |
| 0.1398        | 25.0  | 500  | 0.5618          | 0.8398    | 0.8518 | 0.8458 | 0.9032   |
| 0.1398        | 26.0  | 520  | 0.5583          | 0.8428    | 0.8550 | 0.8489 | 0.9046   |
| 0.1398        | 27.0  | 540  | 0.5632          | 0.8427    | 0.8524 | 0.8475 | 0.9042   |
| 0.1398        | 28.0  | 560  | 0.5674          | 0.8393    | 0.8522 | 0.8457 | 0.9029   |
| 0.1398        | 29.0  | 580  | 0.5625          | 0.8429    | 0.8527 | 0.8478 | 0.9046   |
| 0.1398        | 30.0  | 600  | 0.5635          | 0.8425    | 0.8538 | 0.8481 | 0.9046   |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.1
- Datasets 2.18.0
- Tokenizers 0.15.2
