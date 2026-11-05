---
language: en
license: mit
tags:
- text-classification
- pytorch
- roberta
- emotion-detection
- steam
- gaming
datasets:
- bramb0/synthetic-steam-emotions
base_model: roberta-base
widget:
- text: The gameplay is a bit mid but overall it's a 7/10 game, it has good story
    and lore!
- text: I can't believe the developers released this buggy mess.
- text: Absolutely stunning graphics and the combat is incredibly satisfying.
---
# RoBERTa Steam Review Emotions

This is a fine-tuned `roberta-base` model trained specifically to detect **28 distinct emotional states** within the context of Steam video game reviews. 

## Model Details
- **Base Model:** `roberta-base`
- **Task:** Text Classification (Multi-class / 28 Labels)
- **Language:** English
- **Training Dataset:** `bramb0/synthetic-steam-emotions`

## Intended Use
This model is designed to perform highly nuanced emotion detection on gaming-related text, such as Steam reviews, Reddit threads, and Discord messages. It goes beyond standard Positive/Negative sentiment by predicting the probabilities of 28 distinct GoEmotion labels.

## Labels
The model predicts the following 28 emotions:
`admiration`, `amusement`, `anger`, `annoyance`, `approval`, `caring`, `confusion`, `curiosity`, `desire`, `disappointment`, `disapproval`, `disgust`, `embarrassment`, `excitement`, `fear`, `gratitude`, `grief`, `joy`, `love`, `nervousness`, `optimism`, `pride`, `realization`, `relief`, `remorse`, `sadness`, `surprise`, `neutral`.

## Training Data
The model was trained on a custom dataset of Steam Reviews. The reviews were split into individual clauses and tagged with one of the 28 emotion labels using an LLM to generate synthetic ground-truth data.

## Usage
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="bramb0/roberta-steam-review-emotions", return_all_scores=True)
results = classifier("The gameplay is a bit mid but overall it's a 7/10 game, it has good story and lore!")
print(results)
```
