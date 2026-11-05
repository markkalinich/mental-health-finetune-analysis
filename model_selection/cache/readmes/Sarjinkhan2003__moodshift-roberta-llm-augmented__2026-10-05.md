---
tags: [text-classification, emotion-detection, roberta, data-augmentation, llm, hci]
datasets: [dair-ai/emotion]
---
# MoodShift — RoBERTa+ESA+TF-IDF+FL with LLM Data Augmentation
Novel contribution: LLM-based minority class augmentation via Groq (llama-3.3-70b)

with self-consistency filtering for label fidelity.

Test Accuracy: **0.9265** | Macro F1: **0.8926**

Baseline (no augmentation): Acc=0.9235 | F1=0.8831

ICCA 2026 HCI Research — MoodShift Adaptive Chatbot
