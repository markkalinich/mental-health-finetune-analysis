---
library_name: transformers
tags:
  - sentiment-analysis
  - roberta
  - twitter
  - huggingface
  - sentiment140
datasets:
  - sentiment140
model_name: cardiffnlp/twitter-roberta-base-sentiment-latest
task: text-classification
license: apache-2.0
---

# Twitter-RoBERTa Sentiment140 Fine-tuned

Questo modello è una versione fine-tuned di `cardiffnlp/twitter-roberta-base-sentiment-latest` sul dataset Sentiment140, ottimizzato per l'analisi del sentiment di tweet in italiano e inglese. Il modello classifica i testi in tre categorie: negativo, neutro, positivo.

## Caratteristiche tecniche
- **Base model:** cardiffnlp/twitter-roberta-base-sentiment-latest
- **Dataset:** Sentiment140 (5000 esempi train, 500 validazione, 5000 test)
- **Task:** Sentiment Analysis (3 classi: negativo, neutro, positivo)
- **Tokenizzazione:** max_length=128, padding='max_length', truncation=True
- **Batch size:** 16
- **Epochs:** 3
- **Learning rate:** 2e-5
- **Weight decay:** 0.01

## Come usare il modello

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("<MODEL_DIR>")
model = AutoModelForSequenceClassification.from_pretrained("<MODEL_DIR>")

text = "Questo è un tweet fantastico!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=128)
with torch.no_grad():
    logits = model(**inputs).logits
    predicted_class = logits.argmax(-1).item()

# Mappatura delle classi:
# 0 = Negativo, 1 = Neutro, 2 = Positivo
print(f"Sentiment: {predicted_class}")
```
Sostituisci `<MODEL_DIR>` con il percorso della cartella del modello salvato (es. `./results/hf_model`).

## Dataset
Il dataset Sentiment140 contiene tweet etichettati come negativo (0), neutro (2), positivo (4). Le etichette sono state rimappate come segue:
- 0 → 0 (Negativo)
- 2 → 1 (Neutro)
- 4 → 2 (Positivo)

## Addestramento
L'addestramento è stato effettuato con HuggingFace Transformers Trainer, utilizzando una suddivisione 90/10 per train/validation e limitando la dimensione dei dati per rapidità di test.

## Licenza
Apache 2.0

## Autore
Machine Innovators (proai-machineinnovators)
