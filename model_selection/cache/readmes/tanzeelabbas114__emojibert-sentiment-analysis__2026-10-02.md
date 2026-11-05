---
library_name: transformers
tags:
  - sentiment-analysis
  - emoji
  - twitter
  - bert
  - text-classification
  - scientific-reports
  - airline-tweets
license: apache-2.0
datasets:
  - tweet_eval
language: en
pipeline_tag: text-classification
metrics:
  - accuracy
---

# Emoji-Fused Sentiment Analysis BERT (94% Accuracy)

**Official Model from Scientific Reports (2025)**  
Paper: [Sentiment analysis of emoji fused reviews using machine learning and Bert](https://www.nature.com/articles/s41598-025-92286-0)  
DOI: https://doi.org/10.1038/s41598-025-92286-0

**Authors**: Amit Khan, Dipankar Majumdar, Bikromadittya Mondal

This is the **official model** that achieved **94% accuracy** by **preserving and enhancing emojis** using the copyrighted **EMOJIXT** dictionary — instead of removing them like most models do.

---

## Key Innovation

We replace emojis with sentiment-rich words:
- Happy emoji → happy joyful
- Crying emoji → crying sad
- Heart emoji → love adore
- Thumbs up emoji → thumbs up good

Result: **+9% accuracy gain** over state-of-the-art baselines.

---

## Labels

| Label | Sentiment |
|-------|-----------|
| 0     | Negative  |
| 1     | Neutral   |
| 2     | Positive  |

---

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="tanzeelabbas114/emojibert-sentiment-analysis")

print(classifier("flight delayed again crying sad")) 
# → LABEL_0 (Negative)

print(classifier("best airline ever love adore happy joyful"))
# → LABEL_2 (Positive)
```

---

## Performance

- **Accuracy**: 94%
- **Dataset**: Twitter US Airline Sentiment (tweet_eval)
- **Baseline Improvement**: +11% over BERT without emoji handling

---

## Citation

```bibtex
@article{khan2025sentiment,
  title={{Sentiment analysis of emoji fused reviews using machine learning and Bert}},
  author={Khan, Amit and Majumdar, Dipankar and Mondal, Bikromadittya},
  journal={Scientific Reports},
  volume={15},
  pages={7538},
  year={2025},
  doi={10.1038/s41598-025-92286-0}
}
```

---

**Reproduced & uploaded by tanzeelabbas114** — making published research openly accessible!