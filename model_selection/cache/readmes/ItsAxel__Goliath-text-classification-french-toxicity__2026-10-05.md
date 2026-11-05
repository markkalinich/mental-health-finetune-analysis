---
language:
- fr
license: apache-2.0
tags:
- classification
- toxicité
- sentiment
- nlproc
base_model: xlm-roberta-base
datasets:
- custom/dataset.csv
---

# Goliath-text-classification-french-toxicity

Ce modèle est une **classification de texte binaire** basée sur l’architecture **XLM-RoBERTa base** fine-tunée pour détecter si un texte est **toxique** ou **neutre**.  
Il a été entraîné sur un dataset personnel contenant des exemples de phrases toxiques et non toxiques.

---

## 🔍 Description

Ce modèle classe des phrases en deux catégories :

- `neutral` → phrase non toxique  
- `toxic` → phrase toxique  

Il est particulièrement adapté à des tâches de **modération automatique de contenu** ou de **filtrage de textes nuisibles** dans des applications web, chatbots, forums, etc.

---

## 🛠️ Utilisation

### Python — Transformers

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("ItsAxel/Goliath-text-classification-french-toxicity")
model = AutoModelForSequenceClassification.from_pretrained("ItsAxel/Goliath-text-classification-french-toxicity")

clf = pipeline("text-classification", model=model, tokenizer=tokenizer)

result = clf("Ce message est vraiment insultant.")
print(result)