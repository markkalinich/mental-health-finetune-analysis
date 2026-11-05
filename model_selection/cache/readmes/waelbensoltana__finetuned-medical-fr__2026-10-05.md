---
language: fr
license: apache-2.0
tags:
  - classification
  - medical
  - french
  - fine-tuning
  - torch
  - transformers
  - healthcare
datasets:
  - custom
model-index:
  - name: FinetunedMedicalModel
    results: []
---

# 🧠 FinetunedMedicalModel

Modèle de classification fine-tuné sur des textes médicaux en français. Il a été entraîné avec 🤗 Transformers et PyTorch à partir d’un modèle pré-entraîné.

---

## 📦 Utilisation

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("waelbensoltana/finetuned-medical-fr")
model = AutoModelForSequenceClassification.from_pretrained("waelbensoltana/finetuned-medical-fr")

text = "Le patient présente une douleur abdominale persistante."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
prediction = outputs.logits.argmax(dim=-1).item()

print("Classe prédite :", prediction)
```
🔬 Détails
Langue : Français 🇫🇷
Tâche : Classification de texte médical
Framework : PyTorch
Base de données : Jeu de données personnalisé (non public)

📄 Licence
Ce modèle est publié sous la licence Apache 2.0 :
✅ libre d’usage, modification, et distribution, même à des fins commerciales.

Pour plus d’infos : https://www.apache.org/licenses/LICENSE-2.0

✨ Auteur
Ce modèle a été entraîné et publié par waelbensoltana.
