---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- fr
base_model: LiquidAI/LFM2-350M
tags:
- text-generation
- emotion-classification
- lfm
- lfm2
---

# French Emotion Recognition Model: french-emotion-recognition

This repository contains a fine-tuned version of the `LiquidAI/LFM2-350M` model, specialized in classifying emotions from French text.

> **GGUF Version Available**
> Looking for a version that runs efficiently on your CPU? A GGUF-quantized version of this model is available here:
> **[JusteLeo/french-emotion-recognition-GGUF](https://huggingface.co/JusteLeo/french-emotion-recognition-GGUF)**

---
## 🇬🇧 English Version

### Model Description

This model is a fine-tune of **[LiquidAI/LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M)**. It has been trained to identify and classify the following emotions from a given text:
- `joy` (joie)
- `anger` (colere)
- `sadness` (tristesse)
- `fear` (peur)
- `surprise` (surprise)
- `disgust` (dégout)
- `neutral` (neutre)

The model was trained on the following synthetic dataset: **[JusteLeo/French-emotion](https://huggingface.co/datasets/JusteLeo/French-emotion)**.

### How to Use

This model can be used directly with the `text-generation` pipeline from the `transformers` library.

```python
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_id = "JusteLeo/french-emotion-recognition"
model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Create the pipeline
emotion_classifier = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

# --- Examples ---
prompts = [
    "Je viens de gagner au loto, c'est incroyable !", # "I just won the lottery, it's incredible!"
    "Ce plat a un goût vraiment étrange, je n'aime pas du tout.", # "This dish has a really weird taste, I don't like it at all."
    "La date limite pour le projet est demain et je n'ai rien commencé.", # "The project deadline is tomorrow and I haven't started anything."
    "Il est 15h00." # "It's 3:00 PM."
]

for prompt in prompts:
    # The model expects a simple instruction; the prompt is the sentence to analyze.
    # The generated response will be the detected emotion.
    result = emotion_classifier(
        prompt,
        max_new_tokens=10,  # 10 tokens are enough for the emotion name
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )
    print(f"Sentence: '{prompt}'")
    # The response contains the prompt + emotion, we only display the generated part.
    print(f"Predicted Emotion: {result[0]['generated_text'][len(prompt):].strip()}")
    print("-" * 20)
```

### Acknowledgements

- A big thank you to **[Liquid AI](https://huggingface.co/LiquidAI)** for sharing the weights of their excellent `LFM2-350M` model.
- Thanks also to **[Unsloth](https://huggingface.co/unsloth)** to share simple codes for the development process.

---
## 🇫🇷 Version Française

### Description du Modèle

Ce modèle est un affinage de **[LiquidAI/LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M)**. Il a été entraîné pour identifier et classifier les émotions suivantes dans un texte donné :
- `joie`
- `colere`
- `tristesse`
- `peur`
- `surprise`
- `dégout`
- `neutre`

Le modèle a été entraîné sur le jeu de données synthétique suivant : **[JusteLeo/French-emotion](https://huggingface.co/datasets/JusteLeo/French-emotion)**.

### Comment l'utiliser ?

Ce modèle peut être utilisé directement avec la pipeline `text-generation` de la bibliothèque `transformers`.

```python
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Charger le modèle et le tokenizer
model_id = "JusteLeo/french-emotion-recognition"
model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Créer la pipeline
emotion_classifier = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

# --- Exemples ---
prompts = [
    "Je viens de gagner au loto, c'est incroyable !",
    "Ce plat a un goût vraiment étrange, je n'aime pas du tout.",
    "La date limite pour le projet est demain et je n'ai rien commencé.",
    "Il est 15h00."
]

for prompt in prompts:
    # Le modèle attend une instruction simple, le prompt est la phrase à analyser.
    # La réponse générée sera l'émotion détectée.
    result = emotion_classifier(
        prompt,
        max_new_tokens=10,  # Une dizaine de tokens est suffisant pour le nom de l'émotion
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )
    print(f"Phrase : '{prompt}'")
    # La réponse contient le prompt + l'émotion, nous affichons seulement la partie générée.
    print(f"Émotion prédite : {result[0]['generated_text'][len(prompt):].strip()}")
    print("-" * 20)
```

### Remerciements

- Un grand merci à **[Liquid AI](https://huggingface.co/LiquidAI)** pour avoir partagé les poids de leur excellent modèle `LFM2-350M`.
- Merci également à **[Unsloth](https://huggingface.co/unsloth)** de partager des codes simples pour le processus de fine-tuning.