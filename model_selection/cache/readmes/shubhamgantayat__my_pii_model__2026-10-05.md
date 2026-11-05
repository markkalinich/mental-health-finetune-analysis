---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: my_pii_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_pii_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0010

## Model description

num_labels=13

id2label = {
  0: 'I-STREET_ADDRESS',
  1: 'I-ID_NUM',
  2: 'I-NAME_STUDENT',
  3: 'B-PHONE_NUM',
  4: 'B-USERNAME',
  5: 'B-EMAIL',
  6: 'I-PHONE_NUM',
  7: 'O',
  8: 'B-STREET_ADDRESS',
  9: 'B-URL_PERSONAL',
  10: 'I-URL_PERSONAL',
  11: 'B-ID_NUM',
  12: 'B-NAME_STUDENT'
}

label2id = {
  'I-STREET_ADDRESS': 0,
  'I-ID_NUM': 1,
  'I-NAME_STUDENT': 2,
  'B-PHONE_NUM': 3,
  'B-USERNAME': 4,
  'B-EMAIL': 5,
  'I-PHONE_NUM': 6,
  'O': 7,
  'B-STREET_ADDRESS': 8,
  'B-URL_PERSONAL': 9,
  'I-URL_PERSONAL': 10,
  'B-ID_NUM': 11,
  'B-NAME_STUDENT': 12
}


## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 383  | 0.0016          |
| 0.04          | 2.0   | 766  | 0.0010          |
| 0.0012        | 3.0   | 1149 | 0.0010          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
