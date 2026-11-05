---
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
model-index:
- name: BioNLP13CG_ClinicalBERT_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioNLP13CG_ClinicalBERT_NER

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3339
- Seqeval classification report:                                  precision    recall  f1-score   support

                     Amino_acid       0.81      0.59      0.68       297
              Anatomical_system       0.70      0.78      0.74       297
                         Cancer       0.74      0.73      0.73      3490
                           Cell       0.72      0.87      0.79      1360
             Cellular_component       0.00      0.00      0.00        99
Developing_anatomical_structure       0.00      0.00      0.00        11
           Gene_or_gene_product       0.67      0.25      0.37       174
   Immaterial_anatomical_entity       0.52      0.76      0.62       432
         Multi-tissue_structure       0.83      0.59      0.69       317
                          Organ       0.00      0.00      0.00        49
                       Organism       0.71      0.48      0.57       464
           Organism_subdivision       0.70      0.72      0.71       678
             Organism_substance       0.00      0.00      0.00       128
         Pathological_formation       0.62      0.05      0.09       108
                Simple_chemical       0.00      0.00      0.00        56
                         Tissue       0.80      0.85      0.82      1566

                      micro avg       0.73      0.71      0.72      9526
                      macro avg       0.49      0.42      0.43      9526
                   weighted avg       0.71      0.71      0.70      9526


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
| No log        | 0.99  | 95   | 0.4681          |                                  precision    recall  f1-score   support

                     Amino_acid       1.00      0.02      0.04       297
              Anatomical_system       0.44      0.68      0.54       297
                         Cancer       0.68      0.63      0.65      3490
                           Cell       0.59      0.85      0.70      1360
             Cellular_component       0.00      0.00      0.00        99
Developing_anatomical_structure       0.00      0.00      0.00        11
           Gene_or_gene_product       0.00      0.00      0.00       174
   Immaterial_anatomical_entity       0.40      0.60      0.48       432
         Multi-tissue_structure       0.86      0.06      0.11       317
                          Organ       0.00      0.00      0.00        49
                       Organism       0.88      0.02      0.03       464
           Organism_subdivision       0.62      0.54      0.58       678
             Organism_substance       0.00      0.00      0.00       128
         Pathological_formation       0.00      0.00      0.00       108
                Simple_chemical       0.00      0.00      0.00        56
                         Tissue       0.70      0.84      0.76      1566

                      micro avg       0.63      0.58      0.60      9526
                      macro avg       0.39      0.27      0.24      9526
                   weighted avg       0.63      0.58      0.55      9526
 |
| No log        | 2.0   | 191  | 0.3526          |                                  precision    recall  f1-score   support

                     Amino_acid       0.81      0.52      0.63       297
              Anatomical_system       0.66      0.77      0.71       297
                         Cancer       0.74      0.73      0.73      3490
                           Cell       0.71      0.87      0.78      1360
             Cellular_component       0.00      0.00      0.00        99
Developing_anatomical_structure       0.00      0.00      0.00        11
           Gene_or_gene_product       0.76      0.20      0.32       174
   Immaterial_anatomical_entity       0.46      0.76      0.57       432
         Multi-tissue_structure       0.83      0.57      0.68       317
                          Organ       0.00      0.00      0.00        49
                       Organism       0.68      0.44      0.54       464
           Organism_subdivision       0.71      0.67      0.69       678
             Organism_substance       0.00      0.00      0.00       128
         Pathological_formation       1.00      0.01      0.02       108
                Simple_chemical       0.00      0.00      0.00        56
                         Tissue       0.78      0.85      0.81      1566

                      micro avg       0.72      0.70      0.71      9526
                      macro avg       0.51      0.40      0.41      9526
                   weighted avg       0.70      0.70      0.68      9526
 |
| No log        | 2.98  | 285  | 0.3339          |                                  precision    recall  f1-score   support

                     Amino_acid       0.81      0.59      0.68       297
              Anatomical_system       0.70      0.78      0.74       297
                         Cancer       0.74      0.73      0.73      3490
                           Cell       0.72      0.87      0.79      1360
             Cellular_component       0.00      0.00      0.00        99
Developing_anatomical_structure       0.00      0.00      0.00        11
           Gene_or_gene_product       0.67      0.25      0.37       174
   Immaterial_anatomical_entity       0.52      0.76      0.62       432
         Multi-tissue_structure       0.83      0.59      0.69       317
                          Organ       0.00      0.00      0.00        49
                       Organism       0.71      0.48      0.57       464
           Organism_subdivision       0.70      0.72      0.71       678
             Organism_substance       0.00      0.00      0.00       128
         Pathological_formation       0.62      0.05      0.09       108
                Simple_chemical       0.00      0.00      0.00        56
                         Tissue       0.80      0.85      0.82      1566

                      micro avg       0.73      0.71      0.72      9526
                      macro avg       0.49      0.42      0.43      9526
                   weighted avg       0.71      0.71      0.70      9526
 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
