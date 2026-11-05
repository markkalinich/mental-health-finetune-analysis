---
language: en
license: mit
tags:
- finance
- sentiment-analysis
- financial-news
- stock-market
- roberta
- transformers
- huggingface
- pytorch
metrics:
- accuracy
- f1
library_name: transformers
pipeline_tag: text-classification
model-index:
- name: FinRoBERTa-Mendeley
  results:
  - task:
      name: Sentiment Analysis
      type: text-classification
    dataset:
      name: Financial News Headlines (Balanced)
      type: custom
      split: test
      size: 3,500
    metrics:
      - name: Accuracy
        type: accuracy
        value: 0.78
      - name: F1 Macro
        type: f1
        value: 0.72
---

# FinRoBERTa-Mendeley

A fine-tuned DistilRoBERTa model for *financial sentiment analysis*,  
trained on a balanced dataset of financial news headlines.

It predicts Positive, Neutral, or Negative sentiment for text related to the stock market,  company earnings, or financial trends.

---

## Model Details

| Property | Description |
|-----------|-------------|
| **Base model** | `distilroberta-base` |
| **Task** | Financial sentiment classification (3 labels) |
| **Dataset** | Balanced Financial News Headlines (≈18k samples) |
| **Languages** | English |
| **Domain** | Finance / Stock Market / Economy |
| **Fine-tuning epochs** | 3 |
| **Batch size** | 16 |
| **Optimizer** | AdamW (lr=2e-5) |
| **Framework** | PyTorch + Transformers |
| **Accuracy** | ~78% |
| **F1 (macro)** | ~0.72 |

---

## Labels

| ID | Label | Description |
|----|--------|-------------|
| 0 | Negative | Bearish / pessimistic financial outlook |
| 1 | Neutral | Mixed or uncertain tone |
| 2 | Positive | Bullish / optimistic market sentiment |

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load model and tokenizer
model_name = "AurelPx/FinRoBERTa-Mendeley"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)

text = "Tesla shares rally after strong earnings report"

# Tokenize and move to correct device
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)

# Predict
with torch.no_grad():
    logits = model(**inputs).logits

# Compute probabilities and predicted label
probs = F.softmax(logits, dim=-1)
pred = probs.argmax().item()

labels = ["Negative", "Neutral", "Positive"]
print(f"Sentence: {text}")
print(f"Predicted Sentiment: {labels[pred]}")
print(f"Probabilities: {probs.cpu().numpy()}")
```

---

## Evaluation


The model was evaluated on a held-out test set of 20% of the dataset.

| Metric     | Score    |
| ---------- | -------- |
| Accuracy   | **0.78** |
| F1 (macro) | **0.72** |
| Precision  | **0.75** |
| Recall     | **0.76** |

## Performance Comparison

| Model                                          | Accuracy | F1 Macro | Observations                                             |
| :--------------------------------------------- | :------: | :------: | :------------------------------------------------------- |
| **CardiffNLP/twitter-roberta-base-sentiment**  |   0.44   |   0.36   | Performs poorly on financial news; biased toward Neutral |
| **Sigma/financial-sentiment-analysis**         |   0.55   |   0.51   | More balanced, but weak recall on Negative headlines     |
| **RashidNLP/Finance-Sentiment-Classification** |   0.41   |   0.35   | Strong Positive recall but poor Neutral precision        |
| 🟢 **FinRoBERTa-Mendeley**          | **0.78** | **0.72** | Best overall balance across all three classes            |




The model shows robust generalization to finance-related texts such as:

- Company earnings releases

- Market commentary

- Analyst outlooks

- Economic updates

---

## Citation

@misc{distilroberta_financial_sentiment_mendeley,
  title={FinRoBERTa-Mendeley},
  author={Your Name},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/your-username/FinRoBERTa-Mendeley}},
  note={Fine-tuned DistilRoBERTa for financial sentiment analysis on the Mendeley/Financial News dataset}
}

---

## Limitations & Future Work

The dataset is limited to English financial headlines.

It may not generalize perfectly to social media or retail investor sentiment (e.g., Reddit).

Next step: multi-source fine-tuning on tweets, Reddit posts, and news summaries.

---

## License

MIT License — free for commercial and research use.