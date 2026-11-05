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
finetuned_from: google-bert/bert-large-uncased
---
# bert-large-uncased-triage

This model is a fine-tuned version of **google-bert/bert-large-uncased** for a 5-class triage classification task.
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
    "learning_rate": 9.424049824827477e-05,
    "num_train_epochs": 3,
    "seed": 7,
    "per_device_train_batch_size": 32
}
```


## Evaluation Results

The model was optimized for **Macro-F1 Score** on the test set to ensure balanced performance across unique objectives.

### Classification Report (test set)

```text
                   precision    recall  f1-score   support

      ADDR_DIRECT      0.875     0.729     0.795        96
     ADDR_PARTIAL      0.571     0.978     0.721        91
       NOADDR_OFF      1.000     0.634     0.776        82
        NOADDR_ON      0.987     0.833     0.904        90
NOADDR_TANGENTIAL      0.873     0.821     0.847        84

         accuracy                          0.801       443
        macro avg      0.861     0.799     0.808       443
     weighted avg      0.858     0.801     0.808       443

```

### Confusion Matrix (test set)
![Confusion matrix](confusion_matrix.png)

