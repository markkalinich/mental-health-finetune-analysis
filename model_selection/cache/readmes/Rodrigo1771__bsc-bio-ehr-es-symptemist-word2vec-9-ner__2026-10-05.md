---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-9-ner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: output
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: Rodrigo1771/symptemist-9-ner
      type: Rodrigo1771/symptemist-9-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6742268041237114
    - name: Recall
      type: recall
      value: 0.715927750410509
    - name: F1
      type: f1
      value: 0.6944518184231484
    - name: Accuracy
      type: accuracy
      value: 0.9509608906285091
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-9-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2718
- Precision: 0.6742
- Recall: 0.7159
- F1: 0.6945
- Accuracy: 0.9510

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 154  | 0.1469          | 0.5508    | 0.6623 | 0.6014 | 0.9455   |
| No log        | 2.0   | 308  | 0.1436          | 0.6304    | 0.6683 | 0.6488 | 0.9495   |
| No log        | 3.0   | 462  | 0.1611          | 0.6217    | 0.7143 | 0.6648 | 0.9471   |
| 0.1255        | 4.0   | 616  | 0.1982          | 0.6643    | 0.7028 | 0.6830 | 0.9491   |
| 0.1255        | 5.0   | 770  | 0.2229          | 0.6471    | 0.7006 | 0.6728 | 0.9480   |
| 0.1255        | 6.0   | 924  | 0.2297          | 0.6421    | 0.7099 | 0.6743 | 0.9482   |
| 0.0246        | 7.0   | 1078 | 0.2565          | 0.6665    | 0.7022 | 0.6839 | 0.9495   |
| 0.0246        | 8.0   | 1232 | 0.2617          | 0.6824    | 0.7022 | 0.6922 | 0.9510   |
| 0.0246        | 9.0   | 1386 | 0.2718          | 0.6742    | 0.7159 | 0.6945 | 0.9510   |
| 0.0087        | 10.0  | 1540 | 0.2742          | 0.6672    | 0.7143 | 0.6899 | 0.9506   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
