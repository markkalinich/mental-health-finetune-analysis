---
language: en
license: apache-2.0
base_model: distilbert-base-uncased
datasets:
- stanfordnlp/imdb
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- sentiment-analysis
- its-academy-lab
---

# DistilBERT – IMDB sentiment (v1)

Classificatore di sentiment **positivo/negativo** per recensioni di film in inglese,
ottenuto con fine-tuning di `distilbert-base-uncased`.
Progetto del laboratorio *Servizi Cloud Gestiti per l'IA* – ITS Academy Piemonte.

## Dati
- Dataset: [IMDB](https://huggingface.co/datasets/stanfordnlp/imdb) (recensioni di film, etichette 0=NEGATIVE, 1=POSITIVE)
- Snapshot `imdb_v1`: **2000** esempi di training e **500** di validazione, estratti con `shuffle(seed=42)`
- Classi bilanciate (train 1000/1000, validazione 254/246)

## Training
| Parametro | Valore |
|---|---|
| Learning rate | 5e-5 |
| Epoche | 3 (modello migliore: epoca 1) |
| Batch size | 16 |
| Max length | 256 token |
| Precisione | fp16 su GPU T4 (Google Colab) |
| Selezione | `load_best_model_at_end` su accuratezza di validazione |

## Metriche (validazione, 500 esempi)
| Run | Learning rate | Accuratezza migliore |
|---|---|---|
| **lr5e-5 (questo modello)** | 5e-5 | **0.880** |
| lr2e-5 | 2e-5 | 0.874 |

Esperimenti tracciati con MLflow.

## Uso
```python
from transformers import pipeline
clf = pipeline("text-classification", model="zazz99/distilbert-imdb-sentiment", revision="v1")
clf("This movie was absolutely wonderful!")
```

## Limiti
- Solo **inglese**: su testi in altre lingue le previsioni non sono affidabili.
- Addestrato su **recensioni di film**: prestazioni inferiori su altri domini (prodotti, social, news).
- Solo 2000 esempi di training: modello didattico, non pensato per la produzione.
- Testi troncati a 256 token: le recensioni lunghe vengono valutate solo sulla parte iniziale.
- Classificazione binaria: nessuna classe "neutro"; fatica con sarcasmo, ironia e recensioni miste.
- Può ereditare bias presenti in IMDB e in DistilBERT.

## Versioni
- `v1`: prima versione (lr=5e-5, val acc 0.880)
- `v2`: lr=3e-05, 2 epoche, val acc 0.874
