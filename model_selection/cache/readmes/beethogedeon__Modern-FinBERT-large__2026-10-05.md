---
license: apache-2.0
datasets:
- takala/financial_phrasebank
language:
- en
metrics:
- f1
base_model:
- answerdotai/ModernBERT-large
pipeline_tag: text-classification
library_name: transformers
tags:
- finance
- sentiment
- financial-sentiment-analysis
- sentiment-analysis
widget:
- text: Stocks rallied and the British pound gained.
---

# Modern-FinBERT-large: Financial Sentiment Analysis  

[`Modern-FinBERT-large`](https://huggingface.co/answerdotai/ModernBERT-large) is a **pre-trained NLP model** designed for **financial sentiment analysis**. It extends the [`ModernBERT-large`](https://huggingface.co/answerdotai/ModernBERT-large) language model by further training it on a **large financial corpus**, making it highly specialized for **financial text classification**.  

For fine-tuning, the model leverages the **[Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts)** by Malo et al. (2014), a widely recognized benchmark dataset for financial sentiment analysis.  

### Sentiment Labels  
The model generates a **softmax probability distribution** across three sentiment categories:  

- ✅ **Positive**  
- ❌ **Negative**  
- ⚖ **Neutral**  

For more technical insights on `ModernBERT`, check out the research paper:  
🔍 **[ModernBERT Technical Details](https://arxiv.org/abs/2412.13663)**  

# How to use
You can use this model with Transformers pipeline for sentiment analysis.
```bash
pip install -U transformers
```

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load the pre-trained model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained('beethogedeon/Modern-FinBERT-large', num_labels=3)
tokenizer = AutoTokenizer.from_pretrained('beethogedeon/Modern-FinBERT-large')

# Initialize the NLP pipeline
nlp = pipeline("text-classification", model=model, tokenizer=tokenizer)

sentence = "Stocks rallied and the British pound gained."

print(nlp(sentence))
```