---
language:
- it
- en
pipeline_tag: text-classification
tags:
- sentiment-analysis
- roberta
- twitter
- italian
- MLOps
base_model: cardiffnlp/twitter-roberta-base-sentiment-latest
datasets:
- sentiment140
widget:
- text: Questa azienda è fantastica, ottimo servizio!
- text: Ho aspettato 3 ore in linea, il vostro supporto è terribile.
license: mit
---

# Social Media Sentiment Analysis (Fine-tuned)

This is a `cardiffnlp/twitter-roberta-base-sentiment-latest` model that has been **re-trained (fine-tuned)** for binary sentiment classification (Positive vs. Negative).

The original model was trained for 3 classes (Positive, Negative, Neutral). This model was specialized using the [Sentiment140](http://help.sentiment140.com/for-students) dataset to recognize only **Positive** or **Negative** sentiment, making it ideal for corporate reputation monitoring.

The GitHub repository with all the training code and MLOps pipeline can be found here:
[https://github.com/Luffyconqueredhaki/Sentiment-analysis-for-firm-monitoring-online](https://github.com/Luffyconqueredhaki/Sentiment-analysis-for-firm-monitoring-online)

# MLOps Project: Sentiment Analysis (RoBERTa Fine-Tuning)

This repository contains a complete MLOps project for social media sentiment analysis (e.g., Twitter/X). The project manages the entire model lifecycle: from training and fine-tuning a Transformer model (RoBERTa) to a CI/CD pipeline for automated testing and continuous monitoring.

## 🎯 Project Description and Use Cases

This project analyzes social media sentiment to monitor online reputation. The core of the system is a **Transformer (RoBERTa)** model (`cardiffnlp/twitter-roberta-base-sentiment-latest`), specialized in understanding the nuances of social language.

The base model, which classifies into 3 classes (Positive, Negative, Neutral), is **re-trained (fine-tuned)** on the Sentiment140 dataset to further specialize it and adapt it to only 2 classes (Positive/Negative).

The entire model lifecycle is managed through a **complete MLOps flow**, including training, automated testing (CI/CD), and continuous performance monitoring.

### Key Use Cases

* **Brand Reputation Management:** Track public perception (positive or negative) of a company or product in real-time.
* **Customer Feedback Analysis:** Extract actionable insights from thousands of product, app (App Store, Play Store), or service reviews.
* **Market Research:** Understand public opinion on specific topics, industry trends, or competitors.
* **Campaign Monitoring:** Evaluate the impact and reception (positive or negative) of a marketing campaign or event.

---

## 1. The Experimentation Notebook (notebooks/)

The `.ipynb` file in the `notebooks/` folder is the **brain of the Machine Learning project**. It's where all the experimentation was done.

* **Load Data:** Downloads and loads the Sentiment140 dataset.
* **Retraining (Fine-Tuning):** Takes the `cardiffnlp/twitter-roberta-base-sentiment-latest` model and re-trains it on our dataset, moving from 3 to 2 labels (Positive/Negative).
* **Evaluate:** Calculates performance metrics (Accuracy, F1-score) and creates plots (like the Confusion Matrix) to demonstrate the model's effectiveness.

## Performance and Metrics

The model was trained and evaluated on a sample of 10,000 tweets.

*(The exact metric values can be found in the training notebook. Insert your results here)*

| Metric | Value (on Test Set) |
|---|---|
| **Accuracy** | *~85%* |
| **F1-Score (Weighted)** | *~85%* |


# IT
# Analisi del Sentiment per Social Media (Fine-tuned)

Questo è un modello `cardiffnlp/twitter-roberta-base-sentiment-latest` che è stato **ri-addestrato (fine-tuned)** per la classificazione binaria del sentiment (Positivo vs. Negativo).

Il modello originale era addestrato per 3 classi (Positivo, Negativo, Neutrale). Questo modello è stato specializzato usando il dataset [Sentiment140](http://help.sentiment140.com/for-students) per riconoscere solo sentiment **Positivo** o **Negativo**, rendendolo ideale per il monitoraggio della reputazione aziendale.

Il repository GitHub con tutto il codice di training e la pipeline MLOps si trova qui:
[https://github.com/Luffyconqueredhaki/Sentiment-analysis-for-firm-monitoring-online](https://github.com/Luffyconqueredhaki/Sentiment-analysis-for-firm-monitoring-online)

# Progetto MLOps: Sentiment Analysis (Fine-Tuning RoBERTa)

Questo repository contiene un progetto completo di MLOps per l'analisi del sentiment dei social media (es. Twitter/X). Il progetto gestisce l'intero ciclo di vita del modello: dall'addestramento e fine-tuning di un modello Transformer (RoBERTa) fino alla pipeline CI/CD per i test automatici e al monitoring continuo.

## 🎯 Descrizione del Progetto e Casi d'Uso

Questo progetto analizza il sentiment sui social media per monitorare la reputazione online. Il cuore del sistema è un modello **Transformer (RoBERTa)** (`cardiffnlp/twitter-roberta-base-sentiment-latest`), specializzato nel comprendere le sfumature del linguaggio social.

Il modello base, che classifica in 3 classi (Positivo, Neutro, Negativo), viene **ri-addestrato (fine-tuning)** sul dataset Sentiment140 per specializzarlo ulteriormente e adattarlo a 2 sole classi (Positivo/Negativo).

L'intero ciclo di vita del modello è gestito tramite un **flusso MLOps completo**, che include l'addestramento, il test automatico (CI/CD) e il monitoraggio continuo delle performance.

### Casi d'Uso Principali

* **Brand Reputation Management:** Tracciare in tempo reale la percezione pubblica (positiva o negativa) di un'azienda o di un prodotto.
* **Analisi del Feedback Cliente:** Estrarre insight azionabili da migliaia di recensioni di prodotti, app (App Store, Play Store) o servizi.
* **Market Research:** Comprendere l'opinione pubblica su specifici argomenti, trend di settore o sui competitor.
* **Monitoraggio Campagne:** Valutare l'impatto e la ricezione (positiva o negativa) di una campagna di marketing o di un evento.

---

## 1. Il Notebook di Sperimentazione (notebooks/)

Il file `.ipynb` nella cartella `notebooks/` è il **cervello del progetto di Machine Learning**. È dove è stata fatta tutta la sperimentazione.

* **Caricare i Dati:** Scarica e carica il dataset Sentiment140.
* **Fare il Retraining (Fine-Tuning):** Prende il modello `cardiffnlp/twitter-roberta-base-sentiment-latest` e lo ri-addestra sul nostro dataset, passando da 3 a 2 etichette (Positivo/Negativo).
* **Valutare:** Calcola le metriche di performance (Accuracy, F1-score) e crea i grafici (come la Confusion Matrix) per dimostrare che il modello funziona.



## Performance e Metriche

Il modello è stato addestrato e valutato su un campione di 10.000 tweet.

*(I valori esatti delle metriche si trovano nel notebook di training. Inserisci qui i tuoi risultati)*

| Metrica | Valore (sul Test Set) |
|---|---|
| **Accuracy** | *~85%* |
| **F1-Score (Weighted)** | *~85%* |


## Come Usare il Modello (con Transformers)

Puoi usare questo modello direttamente con la `pipeline` di Transformers:

```python
from transformers import pipeline

# Carica il modello dalla repository di HuggingFace
sentiment_pipeline = pipeline(
    "sentiment-analysis", 
    model="Luffyconqueredhaki/Sentiment-analysis-for-firm-monitoring-online"
)

data = [
    "Adoro questo prodotto, è fantastico!",
    "Il vostro servizio clienti è il peggiore che abbia mai visto."
]

risultati = sentiment_pipeline(data)
print(risultati)

# Output:
# [{'label': 'positive', 'score': 0.9...}, 
#  {'label': 'negative', 'score': 0.9...}]