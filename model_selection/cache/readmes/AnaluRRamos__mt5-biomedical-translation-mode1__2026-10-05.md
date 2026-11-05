---
language: [en, pt]
license: mit
tags:
- translation
- mt5
- biomedical
- named-entity
- pytorch
- transformers
datasets:
- biomedical-translation-corpus
metrics:
- bleu
- rouge
- comet
---

# MT5 Biomedical Translator (Mode 1 with NE Embeddings)

This is a fine-tuned [MT5](https://huggingface.co/google/mt5-base) model for **English-to-Portuguese biomedical translation**. It uses **named entity-aware embeddings** to prioritise the translation of biomedical terms.

## 🧠 Model Highlights

- ✅ Based on `google/mt5-base`
- 🧬 Trained with additional **Named Entity (NE) tag embeddings**
- ⚙️ Mode 1: injects NE embeddings during both training and inference
- 📊 Achieved BLEU score of **52.27** on validation set

## 📂 Files

This repository includes:
- `pytorch_model.bin` or `model.safetensors`
- `config.json`
- `tokenizer.json` + sentencepiece files

## 💻 Usage

```python
from transformers import MT5ForConditionalGeneration, AutoTokenizer

model = MT5ForConditionalGeneration.from_pretrained("AnaluRRamos/mt5-biomedical-translation-mode1")
tokenizer = AutoTokenizer.from_pretrained("AnaluRRamos/mt5-biomedical-translation-mode1")

input_text = "Translate this English biomedical abstract."
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs)
translated = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(translated)
