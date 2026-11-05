---
language:
- en
license: mit
library_name: transformers
tags:
- finance
- sentiment
- finbert
- multi-task-learning
datasets:
- financial_phrasebank
- zeroshot/twitter-financial-news-sentiment
- TheFinAI/fiqa-sentiment-classification
metrics:
- accuracy
- f1
base_model: ProsusAI/finbert
widget:
- text: "The company reported a record 20% increase in revenue this quarter."
  example_title: "Strong Earnings"
- text: "Analysts are worried about the looming debt crisis."
  example_title: "Negative Outlook"
---

# Financial-Sentiment-LLM (Multi-Task FinBERT)

A production-ready financial sentiment classifier fine-tuned on **FinBERT**. This model utilizes a **Multi-Task Architecture** (Classification + Regression) to achieve state-of-the-art performance across diverse financial text sources, including professional news, social media, and forum discussions.

- **🚀 Live Demo:** [Hugging Face Space](https://huggingface.co/spaces/pmatorras/financial-sentiment-demo)
- **💻 Source Code:** [GitHub Repository](https://github.com/pmatorras/financial-sentiment-llm)
- **👨‍💻 Author:** [Pablo Matorras-Cuevas](https://pablo.matorras.com/)

## Model Performance

This Multi-Task model achieves **85.4% overall accuracy**, significantly outperforming standard baselines, particularly on noisy social media data.

| Metric / Dataset | **FinBERT (Multi-Task)** | FinBERT (LoRA) |
| :--- | :--- | :--- |
| **Overall Accuracy** | **85.4%** | 83.2% |
| **Macro F1-Score** | **0.83** | 0.80 |
| **Financial PhraseBank** (News) | 95.9% | **97.1%** |
| **Twitter Financial News** | **83.3%** | 80.5% |
| **FiQA** (Forums) | **81.5%** | 72.6% |

> **Note:** For edge deployment or low-memory environments, check out the [LoRA version](https://huggingface.co/pmatorras/financial-sentiment-analysis-lora) which reduces storage by 99% (5MB vs 420MB).

## Architecture

Unlike standard sentiment classifiers, this model shares a `bert-base` backbone with two task-specific heads:
1.  **Classification Head:** Predicts `Negative`/`Neutral`/`Positive` (Optimized for News & Twitter).
2.  **Regression Head:** Predicts a continuous sentiment score (Optimized for FiQA forum discussions).

This approach yielded a **+6.1% accuracy boost** on Twitter data compared to single-task training, proving that learning continuous sentiment intensity helps the model understand noisy social text better.

## Usage

You can use this model directly with the Hugging Face `pipeline` or `AutoModel`:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the model and tokenizer
model_name = "pmatorras/financial-sentiment-multi-task"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Inference
text = "The stock market rally is driven by strong tech earnings."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)

print(probabilities)
```
## Training Details
- **Base Model**: ProsusAI/finbert
- **Optimizer**: AdamW
- **Loss Function**: Weighted sum of Cross-Entropy (Classification) and MSE (Regression).
- **Compute**: Trained on NVIDIA RTX 4050.
