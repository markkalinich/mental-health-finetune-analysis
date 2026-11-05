---
language: it
license: apache-2.0
tags:
  - sentiment-analysis
  - roberta
  - twitter
  - mlflow
pipeline_tag: text-classification
widget:
  - text: "Oggi è una splendida giornata!"
  - text: "Questo prodotto fa davvero schifo..."
---

# Modello di Sentiment Analysis

Questo modello utilizza la base **cardiffnlp/twitter-roberta-base-sentiment-latest** ed è stato generato in modalità **pretrained**.  
Classifica i testi in tre categorie: **positivo**, **neutro** e **negativo**.

## Dettagli tecnici
- Architettura: RoBERTa-base
- Dataset: tweet_eval/sentiment
- Librerie: Hugging Face Transformers, MLflow
- Device di training: cpu

## Output
Il modello e il tokenizer sono salvati nella directory:
`F:\Documenti\slide uni\professionAI\modulo 10 - MLOps\outputs\model_pretrained`
