---
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
model-index:
- name: BC5CDR_ClinicalBERT_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BC5CDR_ClinicalBERT_NER

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1107
- Seqeval classification report:               precision    recall  f1-score   support

    Chemical       0.71      0.73      0.72     10493
     Disease       0.82      0.82      0.82      6944

   micro avg       0.75      0.77      0.76     17437
   macro avg       0.76      0.78      0.77     17437
weighted avg       0.75      0.77      0.76     17437


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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Seqeval classification report                                                                                                                                                                                                                                                                                                          |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| No log        | 1.0   | 143  | 0.1255          |               precision    recall  f1-score   support

    Chemical       0.67      0.68      0.68     10493
     Disease       0.79      0.78      0.78      6944

   micro avg       0.72      0.72      0.72     17437
   macro avg       0.73      0.73      0.73     17437
weighted avg       0.72      0.72      0.72     17437
 |
| No log        | 2.0   | 286  | 0.1160          |               precision    recall  f1-score   support

    Chemical       0.69      0.71      0.70     10493
     Disease       0.77      0.83      0.80      6944

   micro avg       0.72      0.76      0.74     17437
   macro avg       0.73      0.77      0.75     17437
weighted avg       0.72      0.76      0.74     17437
 |
| No log        | 3.0   | 429  | 0.1107          |               precision    recall  f1-score   support

    Chemical       0.71      0.73      0.72     10493
     Disease       0.82      0.82      0.82      6944

   micro avg       0.75      0.77      0.76     17437
   macro avg       0.76      0.78      0.77     17437
weighted avg       0.75      0.77      0.76     17437
 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
