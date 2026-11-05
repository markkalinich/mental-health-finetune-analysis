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

# NPS Score Prediction — xlm_roberta

Fine-tuned **xlm-roberta-base** pour prédire le score NPS sentimental (0–10) depuis les commentaires clients.  
Projet : Système NPS Dior/Reetain — Nada El Maliki

## Métriques (val set)
| Métrique | Valeur |
|----------|--------|
| MAE | 0.879 |
| RMSE | 1.208 |
| Acc@1 | 0.757 |
| Seg Accuracy | 0.998 |
| Pearson R | 0.916 |

## Usage

```python
import torch
from transformers import AutoTokenizer
from modeling_nps_score import NPSScoreModel

model = NPSScoreModel.from_pretrained(
    "nada-05/nps-score-xlm-roberta", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(
    "nada-05/nps-score-xlm-roberta", trust_remote_code=True
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
- Encoder : `xlm-roberta-base`
- Tête : Linear(hidden→128) → GELU → Dropout → Linear(128→1) → Sigmoid
- Loss d'entraînement : MSE
- Dataset : 3018 réponses NPS FR/EN (2095 train / 449 val / 449 test)
