---
tags: [text-classification, emotion-detection, roberta, llm-augmentation, hci]
datasets: [dair-ai/emotion]
---
# MoodShift — RoBERTa+ESA+TF-IDF+FL (Balanced 4500/class)

Novel contribution: LLM-based minority class augmentation via Groq (llama-3.3-70b)
with self-consistency filtering using the trained model itself.

## Results
| Model | Accuracy | Macro F1 |
|-------|----------|----------|
| Original (imbalanced) | 0.9250 | 0.8849 |
| **LLM-Augmented (4500/class)** | **0.9285** | **0.8893** |

## Key Improvements
- Love F1: 0.8344 → 0.8613 (+0.0269)
- Surprise F1: 0.7521 → 0.7576 (+0.0054)

ICCA 2026 HCI Research — MoodShift Adaptive Chatbot
