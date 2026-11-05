---
language: fr
license: mit
tags:
- named-entity-recognition
- token-classification
- camembert
- french
- pii
- anonymization
- privacy
datasets:
- TypicaAI/pii-masking-60k_fr
metrics:
- f1
- precision
- recall
model-index:
- name: V2-camembert-ner-pii-french
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    metrics:
    - type: f1
      value: 0.932683797665605
      name: F1 Score
---

# V2 CamemBERT-NER-PII French

Modèle **CamemBERT V2** fine-tuné pour la détection de **PII (Personally Identifiable Information)** dans des documents juridiques français.

## 🎯 Cas d'usage

Anonymisation/pseudonymisation de documents confidentiels pour professions réglementées :
- Avocats
- Experts-comptables
- Experts judiciaires

Permet l'utilisation sécurisée de LLM en ligne (GPT, Gemini) sans exposer les données personnelles brutes.

## 📊 Performance

- **F1 Score** : 0.932683797665605
- **Epoch** : 4
- **Dataset** : Hybride (~57k exemples)
  - Dataset synthétique juridique français (15k)
  - Dataset réel multidomaine (TypicaAI/pii-masking-60k_fr)

## 🏷️ Entités détectées

### Personnes
- `NOM_PERSONNE` : Noms de famille
- `PRENOM_PERSONNE` : Prénoms

### Adresses
- `NUMERO_VOIE` : Numéros de rue
- `NOM_VOIE` : Noms de voies
- `CODE_POSTAL` : Codes postaux
- `VILLE` : Villes

### Contact
- `EMAIL` : Adresses email
- `TELEPHONE` : Numéros de téléphone

### Identifiants
- `NUM_SECURITE_SOCIALE` : Numéros de sécurité sociale (NIR)
- `IBAN` : Numéros IBAN français
- `NUM_DOSSIER` : Références de dossiers juridiques
- `REF_CADASTRALE` : Références cadastrales

### Organisations
- `NOM_SOCIETE` : Noms de sociétés

Et 70+ autres catégories PII (voir documentation complète).

## 🚀 Utilisation

### Installation

```bash
pip install transformers torch
```

### Détection PII

```python
from transformers import pipeline

# Charger le pipeline NER
ner = pipeline("ner",
               model="Anonym-IA/V2-camembert-ner-pii-french",
               aggregation_strategy="simple")

# Texte à anonymiser
text = """
Jean Dupont, demeurant au 42 rue de la République, 75011 Paris,
email: jean.dupont@example.com, tél: 01 42 35 67 89
"""

# Détecter les entités
entities = ner(text)

for entity in entities:
    print(f"{entity['entity_group']}: {entity['word']} ({entity['score']:.2%})")
```

### Anonymisation complète

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

model = AutoModelForTokenClassification.from_pretrained("Anonym-IA/V2-camembert-ner-pii-french")
tokenizer = AutoTokenizer.from_pretrained("Anonym-IA/V2-camembert-ner-pii-french")

ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def anonymize(text):
    entities = ner(text)

    # Trier par position décroissante
    entities_sorted = sorted(entities, key=lambda e: e['start'], reverse=True)

    mapping = {}
    counters = {}

    anonymized = text
    for entity in entities_sorted:
        entity_type = entity['entity_group']

        # Générer marqueur
        counters[entity_type] = counters.get(entity_type, 0) + 1
        marker = f"[{entity_type}{counters[entity_type]}]"

        # Remplacer
        mapping[marker] = entity['word']
        anonymized = anonymized[:entity['start']] + marker + anonymized[entity['end']:]

    return anonymized, mapping

# Anonymiser
anonymized_text, mapping = anonymize(text)
print("Anonymisé:", anonymized_text)
print("Mapping:", mapping)
```

## 🌐 Versions ONNX (navigateur)

Deux versions ONNX sont disponibles pour l'exécution dans le navigateur :

### 1️⃣ ONNX FP32 (Précision maximale)
```
Anonym-IA/V2-camembert-ner-pii-onnx-fp32
```
- Taille : ~440 MB
- Précision : 100% identique au modèle PyTorch
- Usage : Serveurs, applications avec ressources suffisantes

### 2️⃣ ONNX INT8 Quantifié (Optimisé navigateur)
```
Anonym-IA/V2-camembert-ner-pii-onnx-int8
```
- Taille : ~110 MB (réduction de 75%)
- Précision : ~98-99% du modèle FP32
- Usage : Navigateurs web, appareils mobiles
- Chargement : ~3x plus rapide

## 📚 Entraînement

### Dataset

**Hybride** :
- **15k exemples synthétiques** : Documents juridiques français (jugements, actes notariés, courriers d'avocats)
- **42k exemples réels** : Dataset multidomaine (TypicaAI/pii-masking-60k_fr)

### Modèle de base

- **CamemBERT-base** (almanach/camembert-base)
- 110M paramètres
- Tokenizer SentencePiece (32k vocabulaire)

### Hyperparamètres

- Epochs : 3
- Batch size : 16
- Learning rate : 2e-5
- Optimizer : AdamW (weight decay 0.01)
- Warmup ratio : 0.1

### Corrections appliquées

✅ **Pré-tokenisation** : Évite fragmentation emails/IBANs
✅ **Variantes NIR** : Avec/sans espaces (format officiel)
✅ **Templates juridiques** : Contexte professionnel réaliste
✅ **Noms avec particules** : Le, De, Du, Des

## 🔧 Système d'anonymisation

Format de marqueurs compatible avec systèmes existants :

| Type | Format | Exemple |
|------|--------|---------|
| Nom | `NOM{n}` | `NOM1` |
| Prénom | `PN{n}` | `PN1` |
| Email | `E{n}` | `E1` |
| Téléphone | `T{n}` | `T1` |
| NIR | `NIR{n}` | `NIR1` |
| IBAN | `IBAN{n}` | `IBAN1` |

## 📄 Licence

MIT License - Libre d'utilisation, y compris à des fins commerciales.

## 👥 Auteurs

Projet **Anonym-IA** - Anonymisation de documents pour professions réglementées.

## 🔗 Liens

- **Repo GitHub** : [Anonym-IA_LLM_Pseudonymisation](https://github.com/VOTRE_USERNAME/Anonym-IA_LLM_Pseudonymisation)
- **Documentation** : Voir dossier `docs/`
- **Notebook Kaggle** : [Lien vers votre notebook]

## 📊 Citation

```bibtex
@misc{camembert-ner-pii-french-v2,
  author = {Anonym-IA},
  title = {V2 CamemBERT-NER-PII French},
  year = {2025},
  publisher = {HuggingFace},
  url = {https://huggingface.co/Anonym-IA/V2-camembert-ner-pii-french}
}
```

---

**Généré automatiquement le 2026-01-19 21:55:17**
