---
license: gpl-3.0
datasets:
- financial_phrasebank
language:
- en
metrics:
- accuracy : 0.92
- f1 : 0.92
library_name: transformers
tags:
- bert
- transformers
- sentiment-analysis
- finance
- english
- text-classification
---

# FinanceBERT

FinanceBERT is a transformer-based model specifically fine-tuned for sentiment analysis in the financial sector. It's designed to assess sentiments expressed in financial texts, aiding stakeholders in making data-driven financial decisions.

## Model Description

FinanceBERT uses the BERT architecture, renowned for its deep contextual understanding. This model helps analyze sentiments in financial news articles, reports, and social media content, categorizing them into positive, negative, or neutral sentiments.

## How to Use

To use FinanceBERT, you can load it with the Transformers library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained('marcev/financebert')
model = AutoModelForSequenceClassification.from_pretrained('marcev/financebert')

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return predictions

text = "Your sample text here."
predict(text)
```
# Examples
Try out these examples to see FinanceBert in action:

examples:
  - text: "The company's financial performance exceeded expectations this quarter."
  - text: "There are concerns that the recent scandal could lead to a decrease in shareholder trust."

# Evaluation Results
FinanceBERT was evaluated on a held-out test set and achieved the following performance metrics:

- Accuracy: 92%
- F1-Score (Weighted): 92%
- Evaluation Loss: 0.320


# Detailed Performance Metrics

Classification Report:

Negative Sentiment - class_index: 0
  -  precision: 0.84
  -  recall: 0.90
  -  f1_score: 0.87
  -  support: 29
    
Neutral Sentiment - class_index: 1
  -  precision: 0.94
  -  recall: 0.94
  -  f1_score: 0.94
  -  support: 199

Positive Setniment - class_index: 2
  -  precision: 0.90
  -  recall: 0.88
  -  f1_score: 0.89
  -  support: 83

Confusion Matrix:
  
| Predicted       | Negative | Neutral | Positive |
|-----------------|----------|---------|----------|
| Actual Negative | 26       | 2       | 1        |
| Actual Neutral  | 4        | 188     | 7        |
| Actual Positive | 1        | 9       | 73       |

# Limitations
FinanceBERT has been rigorously trained and tested to ensure reliable performance across a variety of financial texts. However, there are several limitations to consider:

- Domain Specificity: Optimized for financial contexts, may not perform well on non-financial texts.
- Language Support: Currently supports English only.
- Data Bias: Reflects the bias inherent in its training data, which may not include diverse global financial perspectives.
- Interpretability: As a deep learning model, it does not offer easy interpretability of its decision-making process.

# License
This model is released under the GNU General Public License v3.0 (GPL-3.0), requiring that modifications and derivatives remain open source under the same license.

# Acknowledgements
FinanceBERT was developed using the Transformers library by Hugging Face, trained on a curated dataset of financial texts.
