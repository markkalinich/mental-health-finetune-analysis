---
library_name: transformers
license: mit
tasks:
- text-classification
datasets:
- imdb
pipeline_tag: text-classification
language:
- en
tags:
- distilbert
- sentiment-analysis
- movie-reviews
---

# DistilBERT Sentiment — IT (Gillone06)

Classificatore di **sentimento binario** su recensioni di film (dataset IMDB), basato su
[distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased).

- **Etichette:** `NEGATIVE` (id 0), `POSITIVE` (id 1)
- **Lingua:** solo inglese (il modello è addestrato su recensioni IMDB in inglese)

## Versioni

| Tag | Descrizione | Test accuracy |
|-----|-------------|---------------|
| `v1` | Fine-tuning iniziale: 1 epoca, 2000 train / 500 test (seed 42), lr 2e-5. Pubblicato in forma incompleta (config senza label mapping). | 82,8 % |
| `v2` | **Continuazione del training** da v1 su dataset allargato: 8000 train / 2000 test (stesso seed 42), 3 epoche, lr 2e-5 con warmup 10 %, fp16 (GPU). Config completata (`num_labels=2`, `id2label`/`label2id`). | **86,45 %** (test da 2000) / 85,4 % sul test v1 originale |

### Metriche di v2
- Test accuracy: **86,45 %** su 2000 recensioni di test (1000 positive / 1000 negative)
- Matrice di confusione (v2): `[[869, 131], [140, 860]]` → errori totali 271/2000
- Confidenza media sulle predizioni corrette: ~0,94 (contro ~0,80 di v1)

## Addestramento

Il modello `v2` riprende i pesi del checkpoint `v1` e continua l'addestramento
(`train_v2.py`, tracking con MLflow nell'esperimento `sentiment-analysis-lab`):

- snapshot dati versionata: `data/v2` (seed 42, 8000 train / 2000 test)
- tokenizzazione: `max_length=128`, padding a lunghezza massima
- ottimizzatore AdamW (default Trainer), lr picco 2e-5, decay lineare con warmup
- il checkpoint migliore è scelto per **accuracy di validazione** a fine epoca (migliore: epoch 2)

## Uso

```python
from transformers import pipeline

clf = pipeline("sentiment-analysis", model="Gillone06/distilbert-sentiment-its")
print(clf("This was an incredible movie! The acting was superb."))
# [{'label': 'POSITIVE', 'score': 0.98...}]
```

oppure direttamente con `transformers`:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained("Gillone06/distilbert-sentiment-its")
model = AutoModelForSequenceClassification.from_pretrained("Gillone06/distilbert-sentiment-its")
inp = tok("A waste of time, flat characters.", return_tensors="pt", truncation=True)
probs = torch.softmax(model(**inp).logits, dim=-1)
print(probs.argmax(), probs.max())  # → NEGATIVE con score ~0.99
```

Nell'API FastAPI di accompagnamento (`serve.py`) il modello viene caricato dalla revisione
indicata dalla variabile d'ambiente `MODEL_REVISION` (es. `v2`, `v1`).

## Limitazioni

- Addestrato **solo su recensioni di film in inglese**: non generalizza ad altre lingue o domini.
- Classifica solo in positivo/negativo: frasi neutre o ambigue possono essere classificate
  come POSITIVE con confidenza moderata (~0,8).
- Testi più lunghi di 128 token vengono troncati.
