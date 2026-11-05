---
license: apache-2.0
language:
- en
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: text-classification
tags:
- synthetic data
- financial-sentiment-analysis
- sentiment-analysis
- crypto
- stocks
- finbert
- modernfinbert
- synthetic
---

# ModernFinBERT

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/Discord%20button.png" width="200"/>](https://discord.gg/sznxwdqBXj)


<p align="center">
  <img src="ModernFinBERT.png" alt="ModernFinBERT" width="360">
</p>


A fine-tuned financial sentiment analysis model based on **ModernBERT**, trained on synthetic and real financial data cleaned through an automated AI agentic pipeline. The model covers diverse financial domains including news, tweets, crypto, and macroeconomics, making it the most general-purpose financial sentiment classifier. Benchmark results show superior performance with up to 48% accuracy improvement over existing models across multiple financial datasets.

For private API access or access to even more powerful financial models, contact us at **info@tabularis.ai**

# Quick Start
```python
from transformers import pipeline

# Load model
classifier = pipeline('text-classification', model='tabularisai/ModernFinBERT')

# Test sentences
sentences = [
    "The company reported strong quarterly earnings with revenue growth of 15% year-over-year, exceeding analyst expectations.",
    "Due to rising inflation and supply chain disruptions, the Federal Reserve decided to increase interest rates by 0.75 basis points.",
    "The merger between the two pharmaceutical giants is expected to create significant synergies and reduce operational costs by $2 billion annually."
]

# Evaluate
for i, sentence in enumerate(sentences, 1):
    result = classifier(sentence)
    print(f"Sentence {i}: {result[0]['label']} ({result[0]['score']:.3f})")
```


## Benchmark Results
| Dataset | Model | Accuracy | F1-Score | Precision | Recall | ROC-AUC |
|---------|-------|----------|----------|-----------|--------|---------|
| FIQA | ModernFinBERT | **0.80** | **0.61** | **0.64** | **0.88** | **0.96** |
| FIQA | distilroberta_financial | *0.54* | *0.47* | 0.61 | *0.71* | 0.71 |
| FIQA | finbert | 0.48 | 0.43 | 0.59 | 0.66 | 0.76 |
| FIQA | finbert-tone | 0.36 | 0.36 | *0.62* | 0.58 | 0.77 |
| FIQA | roberta_sentiment | 0.36 | 0.35 | 0.60 | 0.58 | *0.89* |
| Twitter | ModernFinBERT | 0.71 | *0.70* | *0.68* | **0.81** | **0.94** |
| Twitter | distilroberta_financial | *0.75* | **0.71** | *0.68* | *0.75* | *0.87* |
| Twitter | finbert-tone | 0.75 | 0.66 | **0.68** | 0.64 | 0.83 |
| Twitter | finbert | 0.73 | 0.67 | 0.65 | 0.70 | 0.86 |
| Twitter | roberta_sentiment | 0.70 | 0.61 | 0.63 | 0.60 | 0.82 |
| JeanBaptiste | ModernFinBERT | 0.74 | 0.58 | 0.71 | 0.56 | 0.84 |
| JeanBaptiste | distilroberta_financial | **0.88** | **0.79** | **0.92** | **0.74** | 0.86 |
| JeanBaptiste | finbert | *0.77* | *0.68* | 0.70 | *0.67* | **0.88** |
| JeanBaptiste | finbert-tone | 0.74 | 0.60 | 0.72 | 0.56 | *0.86* |
| JeanBaptiste | roberta_sentiment | 0.70 | 0.55 | *0.79* | 0.51 | 0.83 |

## Model Averages Across All Datasets
| Model | Accuracy | F1-Score | Precision | Recall | ROC-AUC |
|-------|----------|----------|-----------|--------|---------|
| **ModernFinBERT** | **0.75** | *0.63* | *0.68* | **0.75** | **0.91** |
| distilroberta_financial | *0.73* | **0.66** | **0.73** | *0.73* | 0.82 |
| finbert | 0.66 | 0.59 | 0.65 | 0.68 | *0.84* |
| finbert-tone | 0.62 | 0.54 | *0.68* | 0.59 | 0.82 |
| roberta_sentiment | 0.59 | 0.50 | 0.67 | 0.56 | *0.84* |

### Legend:
**Bold** = Best result per metric per dataset

*Italic* = Second best result per metric per dataset



<table align="center">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/company/tabularis-ai/">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" alt="LinkedIn" width="30" height="30">
      </a>
    </td>
    <td align="center">
      <a href="https://x.com/tabularis_ai">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/x.svg" alt="X" width="30" height="30">
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/tabularis-ai">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" alt="GitHub" width="30" height="30">
      </a>
    </td>
    <td align="center">
      <a href="https://tabularis.ai">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/internetarchive.svg" alt="Website" width="30" height="30">
      </a>
    </td>
  </tr>
</table>