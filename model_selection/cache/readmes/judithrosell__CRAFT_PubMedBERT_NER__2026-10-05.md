---
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
model-index:
- name: CRAFT_PubMedBERT_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CRAFT_PubMedBERT_NER

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1043
- Seqeval classification report:               precision    recall  f1-score   support

       CHEBI       0.71      0.73      0.72       616
          CL       0.85      0.89      0.87      1740
         GGP       0.84      0.76      0.80       611
          GO       0.89      0.90      0.90      3810
          SO       0.81      0.83      0.82      8854
       Taxon       0.58      0.60      0.59       284

   micro avg       0.82      0.84      0.83     15915
   macro avg       0.78      0.79      0.78     15915
weighted avg       0.82      0.84      0.83     15915


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

| Training Loss | Epoch | Step | Validation Loss | Seqeval classification report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| No log        | 1.0   | 347  | 0.1260          |               precision    recall  f1-score   support

       CHEBI       0.66      0.61      0.63       616
          CL       0.81      0.86      0.83      1740
         GGP       0.74      0.54      0.63       611
          GO       0.86      0.89      0.87      3810
          SO       0.73      0.78      0.76      8854
       Taxon       0.47      0.57      0.52       284

   micro avg       0.76      0.80      0.78     15915
   macro avg       0.71      0.71      0.71     15915
weighted avg       0.76      0.80      0.78     15915
 |
| 0.182         | 2.0   | 695  | 0.1089          |               precision    recall  f1-score   support

       CHEBI       0.69      0.74      0.71       616
          CL       0.84      0.88      0.86      1740
         GGP       0.83      0.74      0.78       611
          GO       0.88      0.90      0.89      3810
          SO       0.79      0.82      0.81      8854
       Taxon       0.57      0.60      0.58       284

   micro avg       0.81      0.84      0.82     15915
   macro avg       0.77      0.78      0.77     15915
weighted avg       0.81      0.84      0.82     15915
 |
| 0.0443        | 3.0   | 1041 | 0.1043          |               precision    recall  f1-score   support

       CHEBI       0.71      0.73      0.72       616
          CL       0.85      0.89      0.87      1740
         GGP       0.84      0.76      0.80       611
          GO       0.89      0.90      0.90      3810
          SO       0.81      0.83      0.82      8854
       Taxon       0.58      0.60      0.59       284

   micro avg       0.82      0.84      0.83     15915
   macro avg       0.78      0.79      0.78     15915
weighted avg       0.82      0.84      0.83     15915
 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
