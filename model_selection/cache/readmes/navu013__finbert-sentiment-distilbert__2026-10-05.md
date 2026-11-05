---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - text-classification
  - finance
  - sentiment-analysis
datasets:
  - financial_phrasebank
metrics:
  - accuracy
  - f1
---
 
# Financial Sentiment Classifier (DistilBERT fine-tuned)
 
Fine-tuned `distilbert-base-uncased` for 3-class sentiment classification
(negative / neutral / positive) on the Financial PhraseBank dataset —
short financial news sentences labeled by finance-background annotators.
 
## Intended use
 
Classifies the sentiment of short financial/business news sentences, e.g.
company earnings reports, market commentary, or corporate announcements.
Not intended for general-purpose sentiment analysis outside a finance context.
 
## Training details
 
- **Base model:** distilbert-base-uncased
- **Dataset:** Financial PhraseBank ({~4,850} sentences, train/val/test split)
- **Epochs:** 3
- **Learning rate:** 2e-5
- **Hardware:** free Colab T4 GPU
 
## Evaluation results (held-out test set)
 
| Metric | Score |
|---|---|
| Accuracy | 0.838 |
| Weighted F1 | 0.84 |
 
| Class | Precision | Recall | F1 |
|---|---|---|---|
| Negative | 0.79 | 0.81 | 0.80 |
| Neutral | 0.87 | 0.88 | 0.88 |
| Positive | 0.79 | 0.76 | 0.78 |
 
## Known limitations
 
The model performs well on sentences with explicit sentiment language, but
struggles on sentences requiring **implicit domain reasoning** — e.g. "the
company will deliver X units to a buyer" implies a sale (positive) without
using any positive-sounding words. It also has difficulty with sentences
containing **mixed or competing signals** (e.g. two market indices moving in
opposite directions within one sentence). The most common error pattern is
misclassifying positive or negative sentences as neutral, likely influenced
by class imbalance in the training data (neutral is the majority class).
 
## Usage
 
```python
from transformers import pipeline
 
classifier = pipeline("text-classification", model="navu013/finbert-sentiment-distilbert")
result = classifier("The company reported record profits this quarter.")
print(result)
```
 
## Training data note
 
This is a learning/portfolio project — trained on a public academic dataset,
not intended for production financial decision-making.
