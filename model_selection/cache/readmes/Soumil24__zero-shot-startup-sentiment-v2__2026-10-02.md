---
library_name: transformers
tags:
- zero-shot-classification
- sentiment-analysis
- financial-news
- startups
- nli
- business-intelligence
- transformers
license: mit
datasets:
- financial_phrasebank
- synthetic_competitive_nli
pipeline_tag: text-classification
base_model:
- microsoft/deberta-v3-base
---

# Zero-Shot News Sentiment Analyzer for Startups (v2)

**Model ID:** `Soumil24/zero_shot_news_sentiment_analyzer_startups`  
**Developed by:** [Soumil Malik](https://huggingface.co/Soumil24)  
**Base model:** `microsoft/deberta-v3-base`  
**Finetuned for:** Zero-shot startup-specific news sentiment classification  
**Languages:** English  
**Library:** 🤗 Transformers  
**License:** MIT  

---

## Model Description

This model is a **zero-shot sentiment classification model** fine-tuned to analyze **news articles, press releases, and financial updates** about **startups and companies**.  

It is trained in a **Natural Language Inference (NLI)** format to interpret how a piece of text (news headline or article) relates to hypotheses describing sentiment polarity (**positive**, **neutral**, **negative**) for a given entity (startup/company).

Unlike standard sentiment models, this model can reason about **multiple companies in a single article**, identifying **who benefits and who suffers** in competitive contexts like _"Swiggy beats Zomato"_ or _"Ola faces losses while Uber grows"_.

---

## Key Features

| Feature | Description |
|----------|-------------|
| **Zero-shot capable** | Works with any unseen startup or company name |
| **Business-aware** | Trained on financial and business news |
| **Competition reasoning** | Distinguishes sentiment across multiple entities in the same article |
| **Probability outputs** | Returns sentiment probabilities for positive, neutral, and negative classes |
| **Transformer-based** | Built on `microsoft/deberta-v3-base` architecture |
| **Language** | English only (financial and tech domains) |

---

## Model Sources

- **Repository:** [GitHub (Project Notebook)](https://github.com/SoumilMalik24)  
- **Base Model:** [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base)  
- **Datasets Used:**
  - Financial PhraseBank (Kaggle / Hugging Face)
  - Synthetic competition NLI dataset (custom generated)
  - [SweatSmile News Sentiment](https://huggingface.co/datasets/sweatSmile/news-sentiment-data) *(for future expansion)*

---

## Model Architecture

- Base: **DeBERTa-v3-base**
- Objective: **Natural Language Inference (entailment / neutral / contradiction)**
- Output Classes: `entailment (positive)`, `neutral`, `contradiction (negative)`
- Tokenizer: DeBERTa-v3 tokenizer (WordPiece)
- Framework: PyTorch + Hugging Face Transformers

---

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch, torch.nn.functional as F

tokenizer = AutoTokenizer.from_pretrained("Soumil24/zero_shot_news_sentiment_analyzer_startups")
model = AutoModelForSequenceClassification.from_pretrained("Soumil24/zero_shot_news_sentiment_analyzer_startups")

def predict_single_company(text, company):
    hypotheses = [
        f"The news is positive for {company}.",
        f"The news is neutral for {company}.",
        f"The news is negative for {company}.",
    ]
    inputs = tokenizer([text]*3, hypotheses, return_tensors="pt", truncation=True, padding='max_length', max_length=256)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=1)
    entailment_scores = probs[:, 0].tolist()
    labels = ["positive", "neutral", "negative"]
    best_label = labels[int(torch.argmax(torch.tensor(entailment_scores)))]
    return {labels[i]: round(entailment_scores[i], 4) for i in range(3)}, best_label

text = "Swiggy beats Zomato stocks"
print(predict_single_company(text, "Swiggy"))
```

---

## Example Outputs

| Input | Company | Output |
|--------|----------|--------|
| "Swiggy beats Zomato stocks" | Swiggy | **Positive (0.98)** |
| "Swiggy beats Zomato stocks" | Zomato | **Negative (0.99)** |
| "Ola faces losses while Uber expands" | Ola | **Negative (0.99)** |
| "Ola faces losses while Uber expands" | Uber | **Positive (0.99)** |
| "Tata Motors appoints new CFO" | Tata Motors | **Neutral (0.74)** |

---

## Training Details

**Datasets Used:**
- Financial PhraseBank (Kaggle)
- Synthetic NLI data generated for competitive understanding (Swiggy, Zomato, Ola, Uber, Flipkart, Amazon)

**Dataset Size:**
- Financial PhraseBank: ~4,800 samples  
- Expanded NLI form: ~14,000 rows  
- Synthetic relational data: ~400–500 samples  

**Training Environment:**
- Hardware: Google Colab (T4 GPU)  
- Framework: Transformers 4.57.1, PyTorch 2.7  
- Precision: FP16 Mixed Precision  
- Epochs: 3 (2 + 1 refinement)  
- Batch Size: 8  
- Optimizer: AdamW  
- Learning Rate: 2e-5  
- **Validation Accuracy:** 97.7%  
- **Weighted F1:** 97.7%  

---

## Evaluation

| Metric | Value |
|--------|-------|
| Validation Accuracy | **0.977** |
| Weighted F1 | **0.977** |
| Eval Loss | **0.12** |
| Eval Samples/sec | ~127 |

---

## Intended Uses

### Direct Use
- Classify sentiment of business or financial news articles about startups/companies  
- Extract per-company sentiment in multi-entity articles  
- Build startup news monitoring dashboards or trend analysis tools  

### Downstream Use
- Integrate into data pipelines for sentiment-based analytics  
- Power news alert systems for VCs or analysts  
- Enrich financial data with sentiment metadata  

### Out-of-Scope
- Political or non-business text sentiment  
- Non-English content  
- Sarcasm or figurative language detection  

---

## Bias, Risks & Limitations

- Trained primarily on **financial and business English news** — may not generalize to other domains  
- Limited exposure to **non-Indian startup names** (can be expanded in v3)  
- Competitive context improved, but can still miss **subtle neutral tones**  
- The model does not understand **numerical or market data (e.g., stock values)** directly  

---

## Environmental Impact (approx.)

| Factor | Estimate |
|--------|-----------|
| Hardware | NVIDIA T4 GPU |
| Runtime | ~1.5 hrs total |
| Cloud Provider | Google Colab |
| Carbon Emission | ~0.25 kg CO₂ |

---

## Technical Specs

| Component | Detail |
|------------|--------|
| Framework | PyTorch + Hugging Face Transformers |
| Model Type | DeBERTa-v3-base (encoder) |
| Objective | Natural Language Inference (3-way classification) |
| Precision | Mixed FP16 |
| Hardware Used | NVIDIA T4 GPU |
| Environment | Google Colab Pro |

---

## 🏷️ Citation

### BibTeX
```bibtex
@misc{soumil2025zeroshotstartupsentiment,
  title = {Zero-Shot News Sentiment Analyzer for Startups},
  author = {Soumil Malik},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Soumil24/zero_shot_news_sentiment_analyzer_startups}},
}
```

---

## APA

> Malik, S. (2025). *Zero-Shot News Sentiment Analyzer for Startups (v2)*. Hugging Face.  
> Retrieved from [https://huggingface.co/Soumil24/zero_shot_news_sentiment_analyzer_startups](https://huggingface.co/Soumil24/zero_shot_news_sentiment_analyzer_startups)

---

## Model Card Authors

- **Author:** Soumil Malik  
- **Contact:** [LinkedIn](https://www.linkedin.com/in/soumilmalik24/) / [Hugging Face](https://huggingface.co/Soumil24)  
- **Created:** November 2025  
- **Version:** v2 *(Competition-aware)*  

---

## Summary

This model demonstrates how a transformer can be **taught to reason about sentiment across multiple entities** in business and startup contexts —  
a key building block for **automated financial news intelligence systems**.

---

### Future Versions (v3) Will:
- Include **30+ company entities**  
- Add **more diverse templates**  
- Expand beyond **India-focused datasets**  
- Include a **multi-label scoring mode**  

---

**Built with ❤️ by [Soumil Malik](https://huggingface.co/Soumil24)**  
as part of the **Startup Sentiment Intelligence Project (Minor Project 2025)**.
