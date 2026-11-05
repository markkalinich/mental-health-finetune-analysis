---
language:
- en
license: gemma
base_model: google/gemma-3-270m-it
tags:
- medical
- fine-tuned
- gemma
- healthcare
- question-answering
datasets:
- lavita/ChatDoctor-HealthCareMagic-100k
pipeline_tag: text-generation
---

# Medical Gemma 3 270M — Fine-Tuned

A small language model fine-tuned on medical Q&A data
to act as a domain-specific medical assistant.

## Model Details
- Base Model : google/gemma-3-270m-it
- Dataset    : ChatDoctor-HealthCareMagic (4,500 samples)
- Training   : 2 epochs, RTX 3050 (4.3GB VRAM)
- Framework  : HuggingFace Transformers + TRL SFTTrainer

## What it Does
Answers medical questions in a conversational
doctor-patient style learned from real doctor responses.

## Example

**Input:**
What are the symptoms of diabetes?

**Output:**
Hi, Thanks for asking. Diabetes is a condition
in which the body has an excess of sugar. It is
usually caused by high blood sugar levels...

## Metrics vs Base Model

| Metric              | Base Model | Fine-Tuned |
|---------------------|------------|------------|
| Avg ROUGE-1         | 0.2577     | 0.1724     |
| Avg ROUGE-2         | 0.1139     | 0.0593     |
| Avg ROUGE-L         | 0.2082     | 0.1356     |
| Avg Response Time   | 6.10s      | 3.01s      |
| Avg Response Length | 104.8      | 63.8       |

## Key Observations
- Fine-tuned model is 2x faster than base model
- Learned concise doctor-style conversational responses
- Lower ROUGE scores reflect focused answers
  not longer generic responses

## Disclaimer
This model is for educational purposes only.
Not intended for real medical advice or diagnosis.
Always consult a qualified doctor.

## Author
Divyansh Vats — github.com/vatsdivyansh