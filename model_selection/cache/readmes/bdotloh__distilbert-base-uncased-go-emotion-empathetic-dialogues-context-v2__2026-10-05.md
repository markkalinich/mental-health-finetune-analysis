---
language: en
tags:
- emotion-classification
datasets:
- go-emotions
- bdotloh/empathetic-dialogues-contexts
---


# Model Description

We performed transfer learning experiments on a distilbert-base-uncased model fine-tuned on the GoEmotions dataset for the purpose of classifying [(emotional) contexts in the Empathetic Dialogues dataset](https://huggingface.co/datasets/bdotloh/empathetic-dialogues-contexts). 

The fine-tuned distilbert-base-uncased can be found [here](https://huggingface.co/bhadresh-savani/bert-base-go-emotion).

### Limitations and bias

GoEmotions:
1) Demographics of Reddit Users 
2) Imbalanced class distribution
3) ...

EmpatheticDialogues: 
1) Unable to ascertain the degree of cultural specificity for the context that a respondent described when given an emotion label (i.e., p(description | emotion, *culture*))
2) ...


## Training data

## Training procedure

### Preprocessing

## Evaluation results

