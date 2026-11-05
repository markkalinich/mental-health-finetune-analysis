---
language: en
license: apache-2.0
library_name: transformers
tags:
- gpt2
- text-generation
- empathy
- conversational
model_name: Rex Anima Mark I
base_model: gpt2
pipeline_tag: text-generation
---

# Rex Anima Mark I (110M)

Rex Anima Mark I is a custom-trained conversational model built on the GPT-2 architecture. It features a unique "Soul Layer" fine-tuned for emotional intelligence and empathy.

## Model Details
- **Architecture:** GPT-2 (Causal LM)
- **Parameters:** ~125M
- **Vocabulary Size:** 32,000
- **Special Tokens:** Includes emotional identifiers like `<emo:joy>`, `<emo:sadness>`, and interaction tokens like `[HUMAN]`, `[ANIMA]`, `[EMPATHIZE]`.

## Training Stages
1. **Pre-train:** OpenWebText + WikiText-103
2. **Conv Fine-tune:** PersonaChat + CounselChat
3. **Emotion Fine-tune:** EmpatheticDialogues (Soul Layer)