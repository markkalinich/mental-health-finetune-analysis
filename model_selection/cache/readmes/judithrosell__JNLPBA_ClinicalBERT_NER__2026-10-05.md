---
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
model-index:
- name: JNLPBA_ClinicalBERT_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# JNLPBA_ClinicalBERT_NER

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1723
- Seqeval classification report:               precision    recall  f1-score   support

         DNA       0.72      0.81      0.77      1351
         RNA       0.71      0.86      0.78       723
   cell_line       0.84      0.74      0.78       582
   cell_type       0.72      0.75      0.73      5623
     protein       0.85      0.85      0.85      3501

   micro avg       0.76      0.79      0.78     11780
   macro avg       0.77      0.80      0.78     11780
weighted avg       0.76      0.79      0.78     11780


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

| Training Loss | Epoch | Step | Validation Loss | Seqeval classification report                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 0.336         | 1.0   | 582  | 0.1930          |               precision    recall  f1-score   support

         DNA       0.72      0.77      0.75      1351
         RNA       0.70      0.84      0.77       723
   cell_line       0.85      0.70      0.77       582
   cell_type       0.71      0.68      0.69      5623
     protein       0.85      0.80      0.83      3501

   micro avg       0.76      0.74      0.75     11780
   macro avg       0.77      0.76      0.76     11780
weighted avg       0.76      0.74      0.75     11780
 |
| 0.1841        | 2.0   | 1164 | 0.1762          |               precision    recall  f1-score   support

         DNA       0.73      0.78      0.76      1351
         RNA       0.70      0.87      0.78       723
   cell_line       0.86      0.71      0.78       582
   cell_type       0.71      0.73      0.72      5623
     protein       0.86      0.83      0.84      3501

   micro avg       0.76      0.77      0.77     11780
   macro avg       0.77      0.78      0.78     11780
weighted avg       0.77      0.77      0.77     11780
 |
| 0.1582        | 3.0   | 1746 | 0.1723          |               precision    recall  f1-score   support

         DNA       0.72      0.81      0.77      1351
         RNA       0.71      0.86      0.78       723
   cell_line       0.84      0.74      0.78       582
   cell_type       0.72      0.75      0.73      5623
     protein       0.85      0.85      0.85      3501

   micro avg       0.76      0.79      0.78     11780
   macro avg       0.77      0.80      0.78     11780
weighted avg       0.76      0.79      0.78     11780
 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
