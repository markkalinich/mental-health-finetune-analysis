---
license: apache-2.0
datasets:
- winddude/finacial_pharsebank_66agree_split
- financial_phrasebank
language:
- en
metrics:
- accuracy
model-index:
- name: financial-sentiment-analysis
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: financial_phrasebank
      type: financial_phrasebank
      args: sentences_66agree
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.84
pipeline_tag: text-classification
tags:
- finance
- sentiment
---

# Mamba Finacial Headline Sentiment

Score 0.84 on accuracy for the finacial phrasebank dataset. A completely huggingface capitable implementation of sequence classification with mamba using: <https://github.com/getorca/mamba_for_sequence_classification>.

## Inference:

```
from transformers import pipeline


model_path = 'winddude/mamba_finacial_phrasebank_sentiment'

classifier = pipeline("text-classification", model=model_path, trust_remote_code=True)

text = "Finnish retail software developer Aldata Solution Oyj reported a net loss of 11.7 mln euro $ 17.2 mln for 2007 versus a net profit of 2.5 mln euro $ 3.7 mln for 2006 ."

classifier(text)
```
gives:
`[{'label': 'NEGATIVE', 'score': 0.8793253302574158}]`