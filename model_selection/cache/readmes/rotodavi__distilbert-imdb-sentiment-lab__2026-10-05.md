---
language:
- en
tags:
- sentiment-analysis
- text-classification
- distilbert
dataset:
- imdb
metrics:
- accuracy
---

# Sentiment Analysis Lab - DistilBERT v1

Questo modello è una versione fine-tuned di `distilbert-base-uncased` sul dataset **IMDB** (sottoinsieme di 2000 esempi per l'addestramento e 500 per il test) per la classificazione del sentiment (positivo/negativo).

L'addestramento è stato condotto all'interno del laboratorio di **Servizi Cloud Gestiti per l'IA** dell'ITS Academy Piemonte.

## Dettagli del Modello
- **Architettura di Base:** DistilBERT
- **Task:** Classificazione del Testo Binaria (0: Negativo, 1: Positivo)
- **Versione/Tag:** `v1`
- **Metrica di Ottimizzazione:** Accuracy

## Parametri di Addestramento
- **Learning Rate:** 5e-5
- **Batch Size:** 16
- **Epoche:** 3
- **Precisione:** Mixed Precision (fp16)

## Limitazioni
- Il modello è stato addestrato su un sottoinsieme limitato (2000 esempi) per scopi accademici e di laboratorio, pertanto potrebbe non generalizzare perfettamente su testi complessi, gergali o fuori dominio.
