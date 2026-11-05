---
language:
- es
- en
tags:
- sentiment-analysis
- xlm-roberta
- multilingual
- movies
license: apache-2.0
base_model:
- FacebookAI/xlm-roberta-base
---

# XLM-R Sentiment EN/ES (Movie Reviews)

Clasificador binario (*Positive/Negative*) para reseñas de películas en **inglés y español**, fine-tuned desde `xlm-roberta-base` con  **Rotten Tomatoes movies and critic reviews dataset** from [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset)

**Métricas:** 

Acc **0.8519** · F1 **0.8876** · Prec **0.8646** · Rec **0.9119** · AUC **0.9260**  
*Umbral recomendado:** **0.48*

## Uso rápido
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
m = "Ricardouchub/xlmr-sentiment-es-en"; thr = 0.48
tok = AutoTokenizer.from_pretrained(m, use_fast=True)
mdl = AutoModelForSequenceClassification.from_pretrained(m).eval()
enc = tok(["Excelente actuación, final predecible."], truncation=True, max_length=224, padding=True, return_tensors="pt")
p = torch.softmax(mdl(**enc).logits, dim=-1)[:,1].item()
print(("POSITIVE" if p>=thr else "NEGATIVE"), round(p*100,1), "%")
```

*Notas: split por película (evita fuga); limpieza mínima de texto. No apto para usos sensibles.*

**Autor: Ricardo Urdaneta**