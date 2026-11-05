---
license: mit
datasets:
- Yelp/yelp_review_full
language:
- en
base_model:
- FacebookAI/roberta-large
pipeline_tag: text-classification
tags:
- sentiment-analysis
---
# yelp-sentiment-roberta-large

[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/Zhoyang/yelp-sentiment-analyzer)

RoBERTa-large fine-tuned for **3-class sentiment 
classification** on Yelp reviews.

**Weighted F1: 0.9389 | Accuracy: 93.76%**  
Evaluated on 40,000 held-out samples.

## Labels
| Label | Meaning | Stars |
|-------|---------|-------|
| 0 | Negative | 1–2 ⭐ |
| 1 | Neutral  | 3 ⭐  |
| 2 | Positive | 4–5 ⭐ |

## Per-class Performance
| Class    | Precision | Recall | F1     |
|----------|-----------|--------|--------|
| Negative | 0.9393    | 0.9261 | 0.9327 |
| Neutral  | 0.6934    | 0.7661 | 0.7280 |
| Positive | —         | —      | 0.9731 |

## How to use

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Zhoyang/yelp-sentiment-roberta-large"
)

result = classifier("The food was amazing!")
print(result)
# Output: [{'label': 'LABEL_2', 'score': 0.97}]
# Mapping: LABEL_0 -> Negative (1-2 ⭐) | LABEL_1 -> Neutral (3 ⭐) | LABEL_2 -> Positive (4-5 ⭐)
```

## Training Details

- **Dataset**: Yelp Academic Dataset  
  (499,229 reviews → 239,870 training samples)
- **Base model**: roberta-large (355M parameters)
- **Hardware**: NVIDIA A4000 via Paperspace Gradient
- **Key decisions**:
  - max_len=512 (largest single-step F1 gain: +0.012)
  - Class-weighted loss: Neg 3.0 / Neu 8.0 / Pos 1.5
  - 7 controlled iterations from BERT-base baseline

## Iteration History
| Version | Key Change | Weighted F1 | Neutral F1 |
|---------|-----------|-------------|------------|
| v1 | BERT-base baseline | 0.881 | 0.514 |
| v3 | RoBERTa-base | 0.892 | 0.573 |
| v4 | max_len 256→512 | 0.904 | 0.604 |
| v6 | RoBERTa-large | 0.912 | 0.612 |
| Final | EDA-driven weights | **0.9389** | **0.647** |

## Cross-Domain Generalization (Uber Eats & Food Delivery)

Although fine-tuned on Yelp restaurant reviews, this model demonstrates strong **zero-shot domain generalization** to food delivery platforms (such as **Uber Eats** and **DoorDash**):
- **Delivery Logistics**: Accurately detects sentiment around delayed delivery, temperature loss (cold food), and courier communication.
- **Packaging & Accuracy**: Handles delivery-specific issues such as spills, damaged boxes, and missing items.
- **Nuanced Neutral Reviews**: Successfully identifies mixed dining experiences (e.g., generous portions but soggy dumplings from condensation).

👉 Try it live with both restaurant and delivery reviews on our [Gradio Space](https://huggingface.co/spaces/Zhoyang/yelp-sentiment-analyzer)!

## Citation

Developed as part of Georgia Tech OMSA Practicum,
Spring 2026 — PathSynch Labs Pod C.