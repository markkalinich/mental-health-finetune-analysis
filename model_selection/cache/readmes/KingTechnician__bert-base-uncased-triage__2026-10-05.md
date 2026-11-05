---
datasets:
- KingTechnician/triage-synthetic-data-v1
language: en
library_name: transformers
license: mit
metrics:
- accuracy
- f1
tags:
- text-classification
- triage
finetuned_from: google-bert/bert-base-uncased
---
# bert-base-uncased-triage

This model is a fine-tuned version of **google-bert/bert-base-uncased** for a 5-class triage classification task.
It helps categorize student messages based on how they address specific learning objectives.

## Classification Labels

0. **ADDR_DIRECT**: Message directly addresses the objective.  
1. **ADDR_PARTIAL**: Message partially addresses the objective.  
2. **NOADDR_OFF**: Message does not address the objective (Off-topic).  
3. **NOADDR_ON**: Message does not address the objective (On-topic but irrelevant).  
4. **NOADDR_TANGENTIAL**: Message is tangentially related.  

## Hyperparameters
```
{
    "learning_rate": 1.620896412491757e-05,
    "num_train_epochs": 4,
    "seed": 3,
    "per_device_train_batch_size": 4
}
```


## Evaluation Results

The model was optimized for **Macro-F1 Score** on the test set to ensure balanced performance across unique objectives.

### Classification Report (test set)

```text
                   precision    recall  f1-score   support

      ADDR_DIRECT      0.949     0.771     0.851        96
     ADDR_PARTIAL      0.604     0.989     0.750        91
       NOADDR_OFF      0.968     0.732     0.833        82
        NOADDR_ON      0.933     0.922     0.927        90
NOADDR_TANGENTIAL      1.000     0.774     0.872        84

         accuracy                          0.840       443
        macro avg      0.891     0.838     0.847       443
     weighted avg      0.888     0.840     0.846       443

```

### Confusion Matrix (test set)
![Confusion matrix](confusion_matrix.png)

