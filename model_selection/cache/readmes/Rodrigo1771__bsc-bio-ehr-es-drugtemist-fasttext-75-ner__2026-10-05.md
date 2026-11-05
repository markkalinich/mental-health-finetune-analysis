---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/drugtemist-fasttext-75-ner
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
      name: Rodrigo1771/drugtemist-fasttext-75-ner
      type: Rodrigo1771/drugtemist-fasttext-75-ner
      config: DrugTEMIST NER
      split: validation
      args: DrugTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.9447963800904977
    - name: Recall
      type: recall
      value: 0.9595588235294118
    - name: F1
      type: f1
      value: 0.9521203830369357
    - name: Accuracy
      type: accuracy
      value: 0.9991418018042759
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/drugtemist-fasttext-75-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0044
- Precision: 0.9448
- Recall: 0.9596
- F1: 0.9521
- Accuracy: 0.9991

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
| No log        | 1.0   | 488  | 0.0039          | 0.9005    | 0.9733 | 0.9355 | 0.9988   |
| 0.0189        | 2.0   | 976  | 0.0032          | 0.9239    | 0.9596 | 0.9414 | 0.9989   |
| 0.0027        | 3.0   | 1464 | 0.0044          | 0.9192    | 0.9623 | 0.9403 | 0.9989   |
| 0.0015        | 4.0   | 1952 | 0.0036          | 0.9424    | 0.9467 | 0.9445 | 0.9991   |
| 0.0007        | 5.0   | 2440 | 0.0044          | 0.9448    | 0.9596 | 0.9521 | 0.9991   |
| 0.0004        | 6.0   | 2928 | 0.0055          | 0.9594    | 0.9338 | 0.9464 | 0.9990   |
| 0.0002        | 7.0   | 3416 | 0.0049          | 0.9397    | 0.9458 | 0.9427 | 0.9990   |
| 0.0002        | 8.0   | 3904 | 0.0053          | 0.9434    | 0.9504 | 0.9469 | 0.9991   |
| 0.0001        | 9.0   | 4392 | 0.0050          | 0.9434    | 0.9494 | 0.9464 | 0.9991   |
| 0.0001        | 10.0  | 4880 | 0.0052          | 0.9417    | 0.9494 | 0.9455 | 0.9991   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
