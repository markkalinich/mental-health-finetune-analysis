---
license: apache-2.0
language:
- en
base_model:
- google/flan-t5-base
pipeline_tag: text-generation
tags:
- MBTI
- psychology
- question-generation
- profiling
- random-question-generator
---

# Flan-T5 Base — MBTI Random Question Generator

This repository hosts a fine-tuned version of **google/flan-t5-base**, adapted for generating *random, personality-themed questions* in the context of the **Myers–Briggs Type Indicator (MBTI)** framework.

The model produces short, standalone prompts designed to encourage self-reflection and discussion related to personality traits, emotions, and decision-making.  
It operates as a **randomized question generator** rather than an interactive conversational model.

---

## Model Purpose

The goal of this model is to generate concise, psychologically relevant questions similar to those found in MBTI-style interviews or self-assessment forms.  
Each output question is intended to provoke reflection or reveal an aspect of human cognition, motivation, or behavior.

**Key Characteristics:**
- Generates *independent questions* — no memory or contextual carryover between generations.  
- Optimized for **single-turn usage** (no long-term dialogue support).  
- Produces diverse questions across multiple MBTI domains (e.g., intuition, sensing, thinking, feeling, judging, perceiving).  
- Ideal for personality research tools, psychological chatbots, or training datasets for reflective AI dialogue.

---

## Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("f3nsmart/ft-flan-t5-base-qgen")
tokenizer = AutoTokenizer.from_pretrained("f3nsmart/ft-flan-t5-base-qgen")

prompt = "Generate a question about emotional decision-making."
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=60)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
