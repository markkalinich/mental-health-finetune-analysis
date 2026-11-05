---
language:
- fr
- en
tags:
- nps
- sentiment
- regression
- customer-experience
- luxury
license: mit
---

# NPS Score Prediction — distilbert_multilingual

Fine-tuned **distilbert-base-multilingual-cased** pour prédire le score NPS sentimental (0–10) depuis les commentaires clients.  
Projet : Système NPS Dior/Reetain — Nada El Maliki

## Métriques (val set)
| Métrique | Valeur |
|----------|--------|
| MAE | 0.894 |
| RMSE | 1.230 |
| Acc@1 | 0.753 |
| Seg Accuracy | 0.996 |
| Pearson R | 0.912 |

## Usage

```python
import torch
from transformers import AutoTokenizer
from modeling_nps_score import NPSScoreModel

model = NPSScoreModel.from_pretrained(
    "nada-05/nps-score-distilbert-multilingual", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(
    "nada-05/nps-score-distilbert-multilingual", trust_remote_code=True
)
model.eval()

text = "J'ai attendu 40 minutes sans assistance. Vendeur peu aimable."
enc  = tokenizer(text, return_tensors="pt", max_length=256,
                 truncation=True, padding="max_length")
with torch.no_grad():
    out = model(**enc)
score_nps = round(out.logits.item() * 10, 1)  # → ex: 2.8
print(f"Score IA : {score_nps}/10")
```

## Architecture
- Encoder : `distilbert-base-multilingual-cased`
- Tête : Linear(hidden→128) → GELU → Dropout → Linear(128→1) → Sigmoid
- Loss d'entraînement : MSE
- Dataset : 3018 réponses NPS FR/EN (2095 train / 449 val / 449 test)
