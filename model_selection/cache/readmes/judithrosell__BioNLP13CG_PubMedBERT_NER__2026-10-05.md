---
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
model-index:
- name: BioNLP13CG_PubMedBERT_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioNLP13CG_PubMedBERT_NER

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2066
- Seqeval classification report:                                  precision    recall  f1-score   support

                     Amino_acid       0.78      0.81      0.79       301
              Anatomical_system       0.00      0.00      0.00         3
                         Cancer       0.00      0.00      0.00        37
                           Cell       0.79      0.85      0.82       446
             Cellular_component       0.00      0.00      0.00        19
Developing_anatomical_structure       0.55      0.78      0.65       399
           Gene_or_gene_product       0.68      0.41      0.51       128
   Immaterial_anatomical_entity       0.00      0.00      0.00        45
         Multi-tissue_structure       0.25      0.02      0.04        98
                          Organ       0.00      0.00      0.00        19
                       Organism       0.90      0.93      0.92      1108
           Organism_subdivision       0.71      0.12      0.21       120
             Organism_substance       0.62      0.59      0.60       128
         Pathological_formation       0.00      0.00      0.00        41
                Simple_chemical       0.87      0.86      0.86      4397
                         Tissue       0.90      0.93      0.91      1790

                      micro avg       0.84      0.83      0.84      9079
                      macro avg       0.44      0.39      0.39      9079
                   weighted avg       0.83      0.83      0.82      9079


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

| Training Loss | Epoch | Step | Validation Loss | Seqeval classification report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-------------:|:-----:|:----:|:---------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| No log        | 0.99  | 95   | 0.3390          |                                  precision    recall  f1-score   support

                     Amino_acid       0.81      0.10      0.18       301
              Anatomical_system       0.00      0.00      0.00         3
                         Cancer       0.00      0.00      0.00        37
                           Cell       0.82      0.76      0.79       446
             Cellular_component       0.00      0.00      0.00        19
Developing_anatomical_structure       0.90      0.07      0.13       399
           Gene_or_gene_product       0.00      0.00      0.00       128
   Immaterial_anatomical_entity       0.00      0.00      0.00        45
         Multi-tissue_structure       0.00      0.00      0.00        98
                          Organ       0.00      0.00      0.00        19
                       Organism       0.64      0.86      0.73      1108
           Organism_subdivision       0.00      0.00      0.00       120
             Organism_substance       0.00      0.00      0.00       128
         Pathological_formation       0.00      0.00      0.00        41
                Simple_chemical       0.83      0.79      0.81      4397
                         Tissue       0.74      0.91      0.82      1790

                      micro avg       0.77      0.71      0.74      9079
                      macro avg       0.30      0.22      0.22      9079
                   weighted avg       0.73      0.71      0.69      9079
 |
| No log        | 2.0   | 191  | 0.2209          |                                  precision    recall  f1-score   support

                     Amino_acid       0.76      0.75      0.76       301
              Anatomical_system       0.00      0.00      0.00         3
                         Cancer       0.00      0.00      0.00        37
                           Cell       0.78      0.87      0.82       446
             Cellular_component       0.00      0.00      0.00        19
Developing_anatomical_structure       0.52      0.75      0.61       399
           Gene_or_gene_product       0.65      0.24      0.35       128
   Immaterial_anatomical_entity       0.00      0.00      0.00        45
         Multi-tissue_structure       0.00      0.00      0.00        98
                          Organ       0.00      0.00      0.00        19
                       Organism       0.89      0.92      0.91      1108
           Organism_subdivision       0.50      0.05      0.09       120
             Organism_substance       0.61      0.52      0.56       128
         Pathological_formation       0.00      0.00      0.00        41
                Simple_chemical       0.86      0.86      0.86      4397
                         Tissue       0.87      0.93      0.90      1790

                      micro avg       0.83      0.82      0.83      9079
                      macro avg       0.40      0.37      0.37      9079
                   weighted avg       0.81      0.82      0.81      9079
 |
| No log        | 2.98  | 285  | 0.2066          |                                  precision    recall  f1-score   support

                     Amino_acid       0.78      0.81      0.79       301
              Anatomical_system       0.00      0.00      0.00         3
                         Cancer       0.00      0.00      0.00        37
                           Cell       0.79      0.85      0.82       446
             Cellular_component       0.00      0.00      0.00        19
Developing_anatomical_structure       0.55      0.78      0.65       399
           Gene_or_gene_product       0.68      0.41      0.51       128
   Immaterial_anatomical_entity       0.00      0.00      0.00        45
         Multi-tissue_structure       0.25      0.02      0.04        98
                          Organ       0.00      0.00      0.00        19
                       Organism       0.90      0.93      0.92      1108
           Organism_subdivision       0.71      0.12      0.21       120
             Organism_substance       0.62      0.59      0.60       128
         Pathological_formation       0.00      0.00      0.00        41
                Simple_chemical       0.87      0.86      0.86      4397
                         Tissue       0.90      0.93      0.91      1790

                      micro avg       0.84      0.83      0.84      9079
                      macro avg       0.44      0.39      0.39      9079
                   weighted avg       0.83      0.83      0.82      9079
 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
