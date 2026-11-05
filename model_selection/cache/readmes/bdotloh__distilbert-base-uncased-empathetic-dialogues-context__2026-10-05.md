---
language: en
tags:
- emotion-classification
datasets:
- bdotloh/empathetic-dialogues-contexts
---


# Model Description

This is a distilbert-base-uncased model fine-tuned for the purpose of classifying [(emotional) contexts in the Empathetic Dialogues dataset](https://huggingface.co/datasets/bdotloh/empathetic-dialogues-contexts). 


### Limitations and bias

EmpatheticDialogues: 
1) Unable to ascertain the degree of cultural specificity for the context that a respondent described when given an emotion label (i.e., p(description | emotion, *culture*))
2) ...


## Training data
see [dataset](https://huggingface.co/datasets/bdotloh/empathetic-dialogues-contexts)
## Training procedure

### Preprocessing

## Evaluation results

## Test results
Top 1 accuracy: 53.4
Top 5 accuracy: 86.1
