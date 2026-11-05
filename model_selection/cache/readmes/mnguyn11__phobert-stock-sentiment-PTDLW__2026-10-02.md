---
license: mit
language:
- vi
pipeline_tag: text-classification
tags:
- vietnamese
- sentiment-analysis
- finance
- phobert
library_name: transformers
---

# Vietnamese Stock Sentiment Analysis (PhoBERT)

## Model Description

This model is a **Vietnamese financial sentiment analysis model** fine-tuned from 
**vinai/phobert-base** for classifying the sentiment of Vietnamese financial news and stock-related text.

The model predicts **three sentiment classes**:

- **NEG** – Negative sentiment  
- **NEU** – Neutral sentiment  
- **POS** – Positive sentiment  

It is designed to analyze **Vietnamese financial news, stock market reports, and investment-related text**.

---

## Model Details

- **Developed by:** Minh Nguyen  
- **Model type:** Sequence Classification  
- **Base model:** vinai/phobert-base  
- **Language:** Vietnamese  
- **Task:** Sentiment Analysis  
- **Number of labels:** 3  

---

## Intended Use

### Direct Use

The model can be used to classify sentiment in:

- Vietnamese financial news
- Stock market analysis
- Investment reports
- Financial social media posts

Example applications:

- Market sentiment monitoring
- Financial news analysis
- Algorithmic trading signals
- Sentiment-based stock screening

---

## Out-of-Scope Use

This model is **not designed for**:

- General Vietnamese sentiment analysis outside finance
- Non-Vietnamese languages
- Legal or medical text
- Critical decision-making systems without human oversight

---

## How to Use

Install required libraries:

```bash
pip install transformers torch pyvi
#Example inference:

!git clone https://huggingface.co/mnguyn11/phobert-stock-sentiment-PTDLW


import sys
import os
# Add the directory containing 'predict.py' to the Python path
project_dir = "/content/phobert-stock-sentiment-PTDLW"
if project_dir not in sys.path:
    sys.path.append(project_dir)


from predict import predict
predict(" Trong bối cảnh giá chung cư nội đô tăng mạnh và duy trì ở mức cao, dòng tiền đang dần chuyển sang các dự án còn nhiều dư địa tăng trưởng.")
```

## Training Data

The model was fine-tuned using a dataset of Vietnamese financial news and stock-related sentences.

Dataset characteristics:

Domain: Finance / Stock Market

Language: Vietnamese

Labels:

NEG

NEU

POS

Approximate dataset size: ~1,200 labeled samples
## Training Hyperparameters

Base model: vinai/phobert-base

Task: Sequence Classification

Number of labels: 3

Learning rate: 2e-5

Epochs: 3

Batch size: 16

Max sequence length: 256
## Evaluation
Metrics

Evaluation metrics include:

Accuracy

Precision

Recall

F1-score

Results
Model	Accuracy
Base PhoBERT	~33%
Fine-tuned Model	~90%

The fine-tuned model significantly outperforms the base PhoBERT model on the financial sentiment classification task.
## Limitations

The dataset size is relatively small (~1k samples)

The model is domain-specific to financial text

Performance may degrade on informal or slang-heavy Vietnamese

## Environmental Impact

Training was conducted on a consumer GPU environment for experimentation purposes.

## Acknowledgements

This model is based on the Vietnamese language model:

PhoBERT developed by VinAI Research.