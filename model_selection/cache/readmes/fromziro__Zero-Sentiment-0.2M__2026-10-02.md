---
license: apache-2.0
datasets:
- stanfordnlp/imdb
- nyu-mll/glue
- SetFit/sst5
- cardiffnlp/tweet_eval
pipeline_tag: text-classification
tags:
- sentiment-classification
- custom_code
- custom_tokenizer
- sentiment
---

# Zero-Sentiment-0.2M

Zero-Sentiment-0.2M is a 0.2M-parameter bidirectional sentiment classification model trained on 189k rows from four distinct datasets. 

## Architecture

Zero-Sentiment-0.2M uses a compact and parameter-efficient architecture, featuring GQA, RoPE, RMSNorm, Hadamard FFNs with SwiGLU intervals, and a small, custom 1024-vocab tokenizer.

- Hidden Size: `48`
- Vocab Size: `1024`
- Number of Layers: `12`
- Number of Attention Heads: `4`
- Number of KV Heads: `2`
- Intermediate Size (for SwiGLU): `96`
- SwiGLU Interval: `3` (every 3rd layer)
- RoPE Theta: `2500.0`
- Max Position Embeddings: `96`
- Tie Word Embeddings: `true`
- Use Engram: `false`

## Training

Zero-Sentiment-0.2M was trained with the Muon-AdamW optimser and the WSD scheduler for 4 epochs.

### Training datasets 

- stanfordnlp/imdb
- nyu-mll/glue
- SetFit/sst5
- cardiffnlp/tweet_eval

### Training Results

- Final Eval Acc: 72.49%
- Final Eval F1 Macro: 71.09%
- Final Eval F1 Weighted: 72.49%
- Final Eval Loss: 0.6587

## Evaluation on `fancyzhx/yelp_polarity`

| Metric | Result |
| :--- | :--- |
| **Overall Accuracy** | **70.34%** (26,731 / 38,000) |
| **Overall Macro F1** | **70.34%** |
| **Overall Weighted F1** | **70.34%** |
| **Negative F1 (Class 0)** | **70.78%** (Precision: 69.76% / Recall: 71.84%) |
| **Positive F1 (Class 2)** | **69.90%** (Precision: 70.97% / Recall: 68.85%) |
| **Total Test Samples** | **38,000** |
| **Inference Throughput** | **382.1 samples/sec** (CPU) |

The model achieves an overall accuracy of 70.34% with only 0.2M parameters, while being exceptionally fast.

## Generated Predictions

| Input Text | Prediction | Confidence | Neg / Neu / Pos Breakdown |
| :--- | :--- | :--- | :--- |
| "This was an absolutely breathtaking masterpiece, loved every second..." | [POSITIVE] | 98.7% | 0.7% / 0.5% / 98.7% |
| "So happy today! Everything went perfectly and I cannot stop smiling!" | [POSITIVE] | 98.5% | 0.4% / 1.1% / 98.5% |
| "Genuinely fantastic performance by the lead actor, highly recommended!" | [POSITIVE] | 77.7% | 4.0% / 18.3% / 77.7% |
| "Complete disaster. Awful acting, boring plot, and a total waste of time." | [NEGATIVE] | 98.5% | 98.5% / 1.3% / 0.2% |
| "Terrible food and rude staff. Never coming back to this place." | [NEGATIVE] | 93.0% | 93.0% / 5.6% / 1.3% |
| "Worst customer support ever, they refused to refund my broken order." | [NEGATIVE] | 55.7% | 55.7% / 39.1% / 5.2% |
| "The package arrived on Tuesday as scheduled by the delivery service." | [NEUTRAL] | 60.8% | 30.1% / 60.8% / 9.1% |
| "The concert starts at 8 PM at the downtown arena." | [NEUTRAL] | 67.8% | 2.4% / 67.8% / 29.8% |
| "The meeting has been rescheduled to Thursday morning at 10 AM." | [NEUTRAL] | 60.6% | 1.6% / 60.6% / 37.8% |
| "I thought it was okay, not great but certainly not the worst thing either." | [NEGATIVE] | 74.6% | 74.6% / 20.0% / 5.3% |

The model predicted correctly 9 out of 10 times on the sample test suite. Internal testing shows that it performs exceptionally well on clear positive and negative inputs, but can struggle with subtle, neutral, or ambiguous sentences where it tends to lean negative.

## How to use

```
import torch
import torch.nn.functional as F
from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer

MODEL_ID = "fromziro/Zero-Sentiment-0.2M"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
config = AutoConfig.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, config=config, trust_remote_code=True)
model.eval()

# 3-Class label mapping
LABEL_MAP = {0: "Negative", 1: "Neutral", 2: "Positive"}

text = "Replace with whatever you want"

# Tokenize input (max length 96 tokens)
inputs = tokenizer(text, max_length=96, padding="max_length", truncation=True, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)[0]
    pred_label = torch.argmax(probs).item()

print(f"Prediction: {LABEL_MAP[pred_label]}")
print(f"Confidence: {probs[pred_label] * 100:.1f}%")
print(f"Probabilities -> Neg: {probs[0]*100:.1f}% | Neu: {probs[1]*100:.1f}% | Pos: {probs[2]*100:.1f}%")
```

## License

Apache 2.0.