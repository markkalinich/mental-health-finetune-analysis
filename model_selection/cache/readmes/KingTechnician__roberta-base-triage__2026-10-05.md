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
finetuned_from: FacebookAI/roberta-base
---
# roberta-base-triage

This model is a fine-tuned version of **FacebookAI/roberta-base** for a 5-class triage classification task.
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
    "learning_rate": 8.469674869548409e-05,
    "num_train_epochs": 2,
    "seed": 24,
    "per_device_train_batch_size": 16
}
```


## Evaluation Results

The model was optimized for **Macro-F1 Score** on the test set to ensure balanced performance across unique objectives.

### Classification Report (test set)

```text
                   precision    recall  f1-score   support

      ADDR_DIRECT      0.923     0.750     0.828        96
     ADDR_PARTIAL      0.721     0.967     0.826        91
       NOADDR_OFF      0.929     0.963     0.946        82
        NOADDR_ON      0.989     0.967     0.978        90
NOADDR_TANGENTIAL      1.000     0.833     0.909        84

         accuracy                          0.894       443
        macro avg      0.912     0.896     0.897       443
     weighted avg      0.911     0.894     0.895       443

```

### Confusion Matrix (test set)
![Confusion matrix](confusion_matrix.png)

