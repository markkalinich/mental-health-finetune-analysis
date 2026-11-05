---
license: apache-2.0
datasets:
- FinGPT/fingpt-sentiment-train
language:
- en
metrics:
- accuracy
- f1
- recall
- precision
base_model:
- ProsusAI/finbert
pipeline_tag: text-classification
tags:
- finance
- financial
- news
- sentiment-analysis
- finbert
- transfomer
- text-classification
- financial-news
- financial-news-sentiment
library_name: transformers
---


# 📊 FinBERT Fine-Tuned on Financial News/Texts

A fine-tuned version of [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert) trained for **financial sentiment analysis**  on financial news texts and headlines. 
This fine-tuned model achieves a significant improvement over the original finbert, **outperforming it by over 38% in accuracy** on financial sentiment classification tasks.

---

## 🔧 Model Objective

The goal of this model is to detect **positive**, **neutral**, or **negative sentiment** on financial texts and headlines.

---

## 🗂️ Training Dataset

**Primary Dataset**: [`fingpt-sentiment-train`](https://huggingface.co/datasets/FinGPT/fingpt-sentiment-train) (~60,000 examples)

- Labeled financial text samples (positive / neutral / negative)
- Includes earnings statements, market commentary, and financial news headlines
- Only included **neutral**, **positive** and **negative** texts.

---

## 🧪 Benchmark Evaluation

The model was evaluated against **three benchmark datasets**:
- **[Financial PhraseBank (All Agree and All Combined)](https://www.researchgate.net/publication/251231364_FinancialPhraseBank-v10)**
- **[FiQA + PhraseBank Kaggle Merge](https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis/data)**
- **[fingpt-sentiment-train (test split)](https://huggingface.co/datasets/FinGPT/fingpt-sentiment-train)**

Metrics used:
- **Accuracy**
- **F1 Score**
- **Precision**
- **Recall**


We benchmarked this model against the original [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert) on multiple financial datasets:

| Dataset                            | Samples | Model                   | Accuracy      | F1 (Macro)    | F1 (Weighted) | Precision (Macro) | Precision (Weighted) | Recall (Macro) | Recall (Weighted) |
|------------------------------------|---------|--------------------------|---------------|---------------|----------------|--------------------|------------------------|----------------|--------------------|
| **fingpt-sentiment-train Eval**    | 12511   | FinBERT                  | 0.7131        | 0.70          | 0.71           | 0.71               | 0.72                   | 0.70           | 0.71               |
|                                    |         | **FinBERT-Finetuned (Ours)** | **0.9894 (+38.8%)** | **0.99 (+41.4%)** | **0.99 (+39.4%)** | **0.99 (+39.4%)**      | **0.99 (+37.5%)**          | **0.99 (+41.4%)**  | **0.99 (+39.4%)**      |
| **Financial Phrasebank (Agree)**   | 2264    | FinBERT                  | 0.9717        | 0.96          | 0.97           | 0.95               | 0.97                   | 0.98           | 0.97               |
|                                    |         | **FinBERT-Finetuned (Ours)** | **0.9912 (+2.0%)**  | **0.99 (+3.1%)**  | **0.99 (+2.1%)**  | **0.99 (+4.2%)**       | **0.99 (+2.1%)**           | **0.99 (+1.0%)**   | **0.99 (+2.1%)**       |
| **Financial Phrasebank (Combined)**| 14780   | FinBERT                  | 0.9238        | 0.91          | 0.92           | 0.89               | 0.93                   | 0.94           | 0.92               |
|                                    |         | **FinBERT-Finetuned (Ours)** | **0.9792 (+6.0%)**  | **0.98 (+7.7%)**  | **0.98 (+6.5%)**  | **0.98 (+10.1%)**      | **0.98 (+5.4%)**           | **0.98 (+4.3%)**   | **0.98 (+6.5%)**       |
| **FiQA + PhraseBank (Kaggle)**     | 5842    | FinBERT                  | 0.7581        | 0.74          | 0.77           | 0.73               | 0.79                   | 0.77           | 0.76               |
|                                    |         | **FinBERT-Finetuned (Ours)** | **0.8879 (+17.1%)** | **0.87 (+17.6%)** | **0.89 (+15.6%)** | **0.85 (+16.4%)**      | **0.92 (+16.5%)**          | **0.92 (+19.5%)**  | **0.89 (+17.1%)**      |


> **Note:** All metrics represent classification performance improvements after fine-tuning FinBERT on respective financial sentiment datasets. Metrics in parentheses represent relative improvement over base FinBERT performance.

---
## 🧠 Text-Level Comparison: FinBERT vs FinBERT-Finetuned (Ours)

### 🔴 FinBERT Failed Texts (as per discussed in its [`Paper`](https://arxiv.org/abs/1908.10063)) (Correctly Predicted by Ours)
| Text                                                                                                                        | Expected  | FinBERT                     | Ours                          |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------|-------------------------------|
| Pre-tax loss totaled euro 0.3 million, compared to a loss of euro 2.2 million in the first quarter of 2005.                | Positive  | ❌ Negative (0.7223)         | ✅ Positive (0.9997)           |
| This implementation is very important to the operator, since it is about to launch its Fixed to Mobile convergence service | Neutral   | ❌ Positive (0.7204)         | ✅ Neutral (0.9998)            |
| The situation of coated magazine printing paper will continue to be weak.                                                  | Negative  | ✅ Negative (0.8811)         | ✅ Negative (0.9996)           |

### 🟡 FinBERT Incorrect, Ours Corrected It
| Text                                                                                                           | Expected  | FinBERT                     | Ours                          |
|----------------------------------------------------------------------------------------------------------------|-----------|------------------------------|-------------------------------|
| The debt-to-equity ratio was 1.15, flat quarter-over-quarter.                                                 | Neutral   | ❌ Negative (0.6239)         | ✅ Neutral (0.9998)            |
| Earnings smashed expectations $AAPL posts $0.89 EPS vs $0.78 est. Bullish momentum incoming!                  | Positive  | ❌ Neutral (0.4237)          | ✅ Positive (0.9998)           |
| $TSLA growth is slowing — but hey, at least Elon tweeted something funny today. #Tesla #markets              | Negative  | ❌ Neutral (0.5884)          | ✅ Negative (0.7084)           |

### ⚪ Out-of-Context Texts (FinBERT Misclassified, Ours Handled Properly)
| Text                                                                                       | Expected  | FinBERT                     | Ours                          |
|--------------------------------------------------------------------------------------------|-----------|------------------------------|-------------------------------|
| Unexpected Snowstorm Hits Sahara Desert, Blanketing Sand Dunes                            | Neutral   | ❌ Negative (0.8675)         | ✅ Neutral (0.9993)            |
| Virtual Reality Therapy Shows Promise for Treating PTSD                                    | Neutral   | ❌ Positive (0.8522)         | ✅ Neutral (0.9997)            |

> **Note**: These examples demonstrate improvements in real-world understanding, context handling, and sentiment differentiation with our FinBERT-finetuned model.  Values in parentheses (e.g., `0.9485`) indicate the model’s confidence score for its predicted sentiment.

---

## ⚠️ Limitations & Failure Cases

While the model outperformed the base FinBERT across benchmarks, **some failure cases** were observed in statements involving **fine-grained numerical reasoning**, particularly when numerical comparison semantics are complex or subtle.

| Text                                                                                                    | Expected  | FinBERT                     | Ours                          |
|---------------------------------------------------------------------------------------------------------|-----------|------------------------------|-------------------------------|
| Net profit to euro 203 million from euro 172 million in the previous year.                              | Positive  | ✅ Positive (0.9485)         | ✅ Positive (0.9995)           |
| Net profit to euro 103 million from euro 172 million in the previous year.                              | Negative  | ❌ Positive (0.9486)         | ❌ Positive (0.9994)           |
| Pre-tax loss totaled euro 0.3 million, compared to a loss of euro 2.2 million in Q1 2005.               | Positive  | ❌ Negative (0.7223)         | ✅ Positive (0.9997)           |
| Pre-tax loss totaled euro 5.3 million, compared to a loss of euro 2.2 million in Q1 2005.               | Negative  | ✅ Negative (0.7205)         | ❌ Positive (0.9997)           |
| Net profit totaled euro 5.3 million, compared to euro 2.2 million in the previous quarter of 2005.      | Positive  | ❌ Negative (0.6347)         | ❌ Negative (0.9996)           |
| Net profit totaled euro 0.3 million, compared to euro 2.2 million in the previous quarter of 2005.      | Negative  | ✅ Negative (0.6320)         | ✅ Negative (0.9996)           |

> **Note**: Values in parentheses (e.g., `0.9485`) indicate the model’s confidence score for its predicted sentiment.

This suggests that **explicit numerical comparison reasoning** still remains challenging without targeted pretraining or numerical reasoning augmentation.

---

## Hyperparameters

During fine-tuning, the following hyperparameters were used to optimize model performance:

- **Learning Rate:** 2e-5  
- **Batch Size:** 32  
- **Number of Epochs:** 3  
- **Max Sequence Length:** 128 tokens  
- **Optimizer:** AdamW  
- **Weight Decay:** 0.01  
- **Evaluation Strategy:** Evaluation performed after each epoch

> **Note**: These settings were chosen to balance training efficiency and accuracy for financial news sentiment classification.

---

## 💡 Summary

✅ **Better generalization** than FinBERT on both benchmark and noisy real-world samples  
✅ **Strong accuracy and F1 scores**  
⚠️ Room to improve on **numerical reasoning comparisons** — potential for integration with numerical-aware transformers or contrastive fine-tuning

---
## Usage

### Pipeline Approach
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

model_name = "project-aps/finbert-finetune"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Override the config's id2label and label2id
label_map = {0: "neutral", 1: "negative", 2: "positive"}
model.config.id2label = label_map
model.config.label2id = {v: k for k, v in label_map.items()}

pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

text = "Earnings smashed expectations AAPL posts $0.89 EPS vs $0.78 est. Bullish momentum incoming! #EarningsSeason"
print(pipe(text)) #Output: [{'label': 'positive', 'score': 0.9997484087944031}]

```

### Simple Approach
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "project-aps/finbert-finetune"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Earnings smashed expectations AAPL posts $0.89 EPS vs $0.78 est. Bullish momentum incoming! #EarningsSeason"
inputs = tokenizer(text, return_tensors="pt", truncation=True)
outputs = model(**inputs)
predicted_class = torch.argmax(outputs.logits, dim=1).item()

label_map = {0: "neutral", 1: "negative", 2: "positive"}
print(f"Text : {text}")
print(f"Sentiment: {label_map[predicted_class]}")

```

---
## Acknowledgements

We gratefully acknowledge the creators and maintainers of the resources used in this project:

- **[ProsusAI/FinBERT](https://huggingface.co/ProsusAI/finbert)** – A pre-trained BERT model specifically designed for financial sentiment analysis, which served as the foundation for our fine-tuning efforts.
  
- **[FinGPT Sentiment Train Dataset](https://huggingface.co/datasets/FinGPT/fingpt-sentiment-train)** – The dataset used for fine-tuning, containing a large collection of finance-related news headlines and sentiment annotations.

- **[Financial PhraseBank Dataset](https://www.researchgate.net/publication/251231364_FinancialPhraseBank-v10)** – A widely used benchmark dataset for financial sentiment classification, including the *All Agree* and *All Combined* subsets.
  
- **[FiQA + PhraseBank Kaggle Merged Dataset](https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis/data)** – A merged dataset combining FiQA and Financial PhraseBank entries, used for broader benchmarking of sentiment performance.


We thank these contributors for making their models and datasets publicly available, enabling high-quality research and development in financial NLP.


---