---
base_model: Finisha-F-scratch/Learnia
library_name: transformers
model_name: Learnia-Empathic-Tchat
tags:
- Instruct
- Assistant
- love
- Empathic
licence: license
license: other
language:
- en
pipeline_tag: text-generation
---
# 🧠 Learnia-Empathic-Tchat

![Learnia-Empathic-Tchat](http://www.image-heberg.fr/files/17735744612790649150.jpg)

Learnia-Empathic-Tchat est un Small Language Model (SLM) de 51.6M de paramètres, affiné par SFT (Supervised Fine-Tuning) pour devenir un assistant spécialisé dans le dialogue émotionnel et relationnel. Basé sur l'architecture Learnia, ce modèle prouve qu'une petite taille peut offrir une profondeur de compréhension étonnante lorsqu'elle est couplée à un dataset ultra-spécialisé.

# 🌟 Points Forts
 * Ultra-Léger : 51.6M de paramètres pour une exécution fluide sur n'importe quel CPU ou GPU virtuel.
 * Spécialisation Émotionnelle : Entraîné sur 10 000 dialogues ciblant la résolution de conflits, la tristesse, la trahison et la gestion du stress relationnel.
 * Format Chat-Ready : Utilise un template de chat standard pour une intégration immédiate dans des applications de messagerie.

# 📊 Fiche Technique
| Caractéristique | Détail |
|---|---|
| Base | Learnia (Foundation) |
| Paramètres | 51.6 Millions |
| Méthode | Fine-tuning SFT (Instruct) |
| Dataset | 10k dialogues |
| Format | Hugging Face Transformers |

# 🚀 Utilisation (Inférence)
Pour discuter avec Learnia-Empathic-Tchat, tu peux utiliser le code suivant via la bibliothèque transformers :

```
from transformers import AutoTokenizer, AutoModelForCausalLM

# Chargement du modèle et du tokenizer
checkpoint = "Clem27-Assistants/Learnia-Empathic-Tchat"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

# Structure de la conversation
messages = [
    {"role": "user", "content": "Hello! My mother yelled at me. What should I do?"},
]

# Application du chat template
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

# Génération de la réponse
outputs = model.generate(
    **inputs,
    max_new_tokens=200, 
    do_sample=True, 
    temperature=0.7,
    eos_token_id=tokenizer.eos_token_id,
    stop_strings=["<|im_end|>"],
    tokenizer=tokenizer
)

# Décodage et post-process
decoded_output = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:])
clean_output = decoded_output.replace("<|im_end|>", "").strip()

print(f"Assistant: {clean_output}")
```

# ⚠️ Limitations
Étant un modèle de 51.6M de paramètres, Learnia-Empathic-Tchat est conçu pour la texture conversationnelle et l'empathie, et non pour le calcul mathématique ou la génération de code complexe. Il brille par sa capacité à maintenir un ton humain et réconfortant.

**nos conditions d'utilisation et politique de confidentialité officielles** :
https://learnia-gazelle-empathy.lovable.app/