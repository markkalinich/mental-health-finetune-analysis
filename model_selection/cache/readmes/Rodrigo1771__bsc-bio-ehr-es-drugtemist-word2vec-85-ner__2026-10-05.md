---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/drugtemist-85-ner
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
      name: Rodrigo1771/drugtemist-85-ner
      type: Rodrigo1771/drugtemist-85-ner
      config: DrugTEMIST NER
      split: validation
      args: DrugTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.9461187214611873
    - name: Recall
      type: recall
      value: 0.9522058823529411
    - name: F1
      type: f1
      value: 0.9491525423728814
    - name: Accuracy
      type: accuracy
      value: 0.9989426998228679
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/drugtemist-85-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0048
- Precision: 0.9461
- Recall: 0.9522
- F1: 0.9492
- Accuracy: 0.9989

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
| No log        | 1.0   | 466  | 0.0031          | 0.9292    | 0.9412 | 0.9352 | 0.9989   |
| 0.0199        | 2.0   | 932  | 0.0031          | 0.9212    | 0.9568 | 0.9387 | 0.9989   |
| 0.0026        | 3.0   | 1398 | 0.0040          | 0.9365    | 0.9357 | 0.9361 | 0.9989   |
| 0.0011        | 4.0   | 1864 | 0.0052          | 0.9400    | 0.9219 | 0.9309 | 0.9987   |
| 0.001         | 5.0   | 2330 | 0.0048          | 0.9461    | 0.9522 | 0.9492 | 0.9989   |
| 0.0005        | 6.0   | 2796 | 0.0046          | 0.9376    | 0.9522 | 0.9448 | 0.9989   |
| 0.0004        | 7.0   | 3262 | 0.0050          | 0.9328    | 0.9568 | 0.9446 | 0.9990   |
| 0.0002        | 8.0   | 3728 | 0.0055          | 0.9423    | 0.9449 | 0.9436 | 0.9989   |
| 0.0001        | 9.0   | 4194 | 0.0057          | 0.9399    | 0.9485 | 0.9442 | 0.9989   |
| 0.0001        | 10.0  | 4660 | 0.0058          | 0.9348    | 0.9485 | 0.9416 | 0.9989   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
