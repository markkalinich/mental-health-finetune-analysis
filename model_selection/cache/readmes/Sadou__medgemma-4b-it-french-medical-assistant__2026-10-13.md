---
license: apache-2.0
base_model: google/medgemma-4b-it
tags:
- medical
- french
- healthcare
- text-generation
- fine-tuned
language:
- fr
pipeline_tag: text-generation
widget:
- example_title: "Question médicale générale"
  text: "Comment traiter une migraine ?"
- example_title: "Symptômes"
  text: "Quels sont les symptômes de l'hypertension ?"
- example_title: "Prévention"
  text: "Comment prévenir les infections urinaires ?"
---

# MedGemma 4B-IT Assistant Médical Français

## Description

Ce modèle est une version fine-tunée de **google/medgemma-4b-it** spécialement optimisée pour fournir des **réponses médicales courtes et précises en français**. 

Le modèle a été entraîné pour donner des réponses concises (2-3 phrases maximum) tout en maintenant la précision médicale.

## 🎯 Caractéristiques

- **Modèle de base**: google/medgemma-4b-it
- **Langue**: Français 🇫🇷
- **Spécialisation**: Réponses médicales courtes et précises
- **Technique**: Fine-tuning direct
- **Type**: Text Generation
- **Paramètres**: ~4B

## 🚀 Utilisation

### Installation

```bash
pip install transformers torch accelerate bitsandbytes
```

### Code d'utilisation

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# Configuration
model_id = "Sadou/medgemma-4b-it-french-medical-assistant"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Chargement du modèle fine-tuné
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=BitsAndBytesConfig(load_in_4bit=True),
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

tokenizer = AutoTokenizer.from_pretrained(model_id)

def generate_medical_response(question, max_length=500, temperature=0.2):
    messages = [
        {
            "role": "system",
            "content": "Tu es un assistant médical expert. Réponds toujours en français de manière claire et précise."
        },
        {
            "role": "user", 
            "content": question
        }
    ]
    
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)
    
    input_len = inputs["input_ids"].shape[-1]
    
    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_length,
            do_sample=True,
            temperature=temperature,
            pad_token_id=tokenizer.eos_token_id,
           
        )
    
    response = tokenizer.decode(outputs[0][input_len:], skip_special_tokens=True)
    return response.strip()

# Exemple d'utilisation
question = "Comment traiter une migraine ?"
response = generate_medical_response(question)
print(f"Question: {question}")
print(f"Réponse: {response}")
```

### Version Simple

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Chargement simple
model_id = "Sadou/medgemma-4b-it-french-medical-assistant"
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Usage
question = "Comment traiter une migraine ?"
messages = [
    {"role": "system", "content": "Tu es un assistant médical expert."},
    {"role": "user", "content": question}
]

inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
outputs = model.generate(inputs, max_new_tokens=200, temperature=0.7)
response = tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)
print(response)
```

## 📝 Exemples

### Exemple 1: Traitement
**Input:** "Comment traiter une migraine ?"

**Output:** "Prenez un antalgique (paracétamol 1g ou ibuprofène 600mg) dès les premiers signes. Reposez-vous dans un endroit sombre et silencieux avec une compresse froide sur le front. Si migraines fréquentes (>4/mois), consultez pour un traitement préventif."

## ⚠️ Avertissements

- **Usage médical**: Ce modèle est destiné à l'information générale uniquement
- **Pas un remplacement**: Ne remplace pas une consultation médicale professionnelle
- **Urgences**: En cas d'urgence médicale, contactez immédiatement les services d'urgence

## 👨‍💻 Auteur

**Sadou BARRY**

## 📄 License

Apache 2.0

---

*Modèle créé pour améliorer l'accès à l'information médicale en français* 🇫🇷
