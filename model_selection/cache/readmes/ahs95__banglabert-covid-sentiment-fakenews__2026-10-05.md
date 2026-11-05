---
language: bn
license: apache-2.0
library_name: transformers
tags:
- banglabert
- sentiment-analysis
- fake-news-detection
- multi-task-learning
- covid-19
- bengali-nlp
metrics:
- accuracy
- f1
base_model:
- csebuetnlp/banglabert
pipeline_tag: text-classification
---

# BanglaBERT Multi-Task: Joint Sentiment & Fake News Detection for COVID-19 Bengali Content

This model is a fine-tuned **BanglaBERT** for **multi-task learning**, simultaneously performing:
1.  **Sentiment Classification** (Negative, Neutral, Positive)
2.  **Truthfulness Detection** (Fake, Real)

Trained on 35,526 Bengali social media posts related to the COVID-19 pandemic, this model establishes a new benchmark for jointly modeling emotional framing and misinformation in a low-resource language setting.

This repository accompanies the research paper:  
[**"Multi-Task BanglaBERT for Joint Sentiment and Fake News Detection in COVID-19 Social Media Posts"**](https://zenodo.org/records/17212702?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6Ijk1OWY2NzcyLWYyYzYtNDVmMi1hYjMzLTAwMjA0M2FjMGMwZiIsImRhdGEiOnt9LCJyYW5kb20iOiI5ZmY4YTg5MWZkMzk0NjVjMGFkMjliNTdmZGMzYWMzMCJ9.40Xy_43jSkBm8cvFAUwe1xSjS8Xle93HYgicU9E1KqrjdOfYNrhB_ZSex9SJg1snurEva-nsh5sCDNfRgz_frQ)


## Model Description

- **Base Model:** [`csebuetnlp/banglabert`](https://huggingface.co/csebuetnlp/banglabert)
- **Architecture:** Dual-head classifier on top of the BanglaBERT encoder. The `[CLS]` token representation is fed into two separate linear layers for sentiment (3 classes) and truthfulness (2 classes).
- **Training Objective:** Joint loss combining Focal Loss (for sentiment) and Weighted Cross-Entropy (for truthfulness).
- **Key Innovation:** Uses **class-specific Focal Loss** (α_neutral=1.5) to handle the underrepresented and semantically ambiguous neutral sentiment class, while prioritizing the sentiment task (α=0.90) in the joint loss.

## Performance

Evaluated on a held-out test set of 3,553 samples:

| Task             | Accuracy | Macro F1 | Class (F1)                     |
|------------------|----------|----------|--------------------------------|
| Sentiment        | 75.1%    | 0.707    | Negative: 0.77, Neutral: 0.57, Positive: 0.78 |
| Truthfulness     | 88.0%    | 0.851    | Fake: 0.79, Real: 0.92         |

> 📊 **Insight:** The model excels at detecting polarized sentiment and real news. The neutral sentiment class remains the primary challenge (F1=0.57), often confused with negative or positive due to semantic ambiguity.

## Intended Uses & Limitations

### ✅ Intended Use
- Analyzing public sentiment and veracity of Bengali social media content, particularly during public health crises like COVID-19.
- Supporting fact-checking initiatives and misinformation monitoring in Bengali.
- Serving as a strong baseline for future multi-task NLP research in Bangla.

### ⚠️ Limitations
- **Domain Specific:** Trained on COVID-19 related content. Performance may degrade on topics outside this domain.
- **Neutral Sentiment:** Struggles with the semantic ambiguity of neutral statements, which are often misclassified as weakly positive or negative.
- **Stylistic Bias:** May misclassify sensational (but factual) real news as fake, and conversely, well-written fake news as real.
- **Data Size:** While large for Bangla, the dataset is modest compared to high-resource languages, potentially limiting generalization.

## How to Use

You can use this model directly with the 🤗 Transformers library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load tokenizer and model
model_name = "your-hf-username/banglabert-multitask-covid-sa-fake"  # Replace with your model ID
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# For inference, you need to handle the dual-head output manually.
# This model returns two logits tensors: one for sentiment (3 classes), one for truthfulness (2 classes).

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        # The model returns a tuple: (sentiment_logits, truthfulness_logits)
        sent_logits = outputs[0]  # Shape: [1, 3]
        truth_logits = outputs[1] # Shape: [1, 2]

        sent_pred = torch.argmax(sent_logits, dim=-1).item()
        truth_pred = torch.argmax(truth_logits, dim=-1).item()

        # Map IDs to labels
        sentiment_labels = ["negative", "neutral", "positive"]
        truth_labels = ["fake", "real"]

        return {
            "sentiment": sentiment_labels[sent_pred],
            "truthfulness": truth_labels[truth_pred],
            "sentiment_confidence": torch.softmax(sent_logits, dim=-1).tolist()[0],
            "truthfulness_confidence": torch.softmax(truth_logits, dim=-1).tolist()[0]
        }

# Example usage
text = "করোনা ভাইরাস নিয়ে সরকারের পদক্ষেপ অত্যন্ত প্রশংসনীয়।"
result = predict(text)
print(result)
# Output: {'sentiment': 'positive', 'truthfulness': 'real', ...}
```
Note: Since this is a custom multi-task model, AutoModelForSequenceClassification will load it, but you must handle the tuple output (logits_sentiment, logits_truthfulness) manually, as shown above. Standard .pipeline() will not work out-of-the-box.

## Training Details

- **Hardware:** 2× NVIDIA T4 GPUs (16 GB each)  
- **Precision:** Mixed-precision (FP16)  
- **Optimizer:** AdamW (lr = 2e-5, weight_decay = 0.01)  
- **Scheduler:** Cosine decay with 10% warmup  
- **Batch size:** Effective 64 (16 per GPU, gradient accumulation over 4 steps)  
- **Epochs:** 4 (early stopping triggered)

### Loss Functions
- **Sentiment:** FocalLoss(gamma = 2, alpha = [1.0, 1.5, 1.0])  
- **Truthfulness:** CrossEntropyLoss(weight = inverse_frequency)  
- **Joint loss:** L = 0.9 * L_sent + 0.1 * L_truth

## Dataset

- 35,526 Bengali social media posts  
- Sources: Facebook, Bangla Newspaper Dataset (ebD), BanFakeNews-2.0, Rumor Scanner fact-checking portal  
- Annotations: Dual-annotated for sentiment (Negative, Neutral, Positive) and truthfulness (Fake, Real)

## Citation

If you use this model or its code in your research, please cite the paper:

```bibtex
@article{banglabert-covid-sentiment-fakenews_2025,
  title={Multi-Task BanglaBERT for Joint Sentiment and Fake News Detection in COVID-19 Social Media Posts},
  author={Arshadul Hoque},
  journal={Zenodo},
  year={2025},
  url={https://zenodo.org/records/17212702?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6Ijk1OWY2NzcyLWYyYzYtNDVmMi1hYjMzLTAwMjA0M2FjMGMwZiIsImRhdGEiOnt9LCJyYW5kb20iOiI5ZmY4YTg5MWZkMzk0NjVjMGFkMjliNTdmZGMzYWMzMCJ9.40Xy_43jSkBm8cvFAUwe1xSjS8Xle93HYgicU9E1KqrjdOfYNrhB_ZSex9SJg1snurEva-nsh5sCDNfRgz_frQ}
}
```

## Acknowledgements

- The original [csebuetnlp/banglabert](https://huggingface.co/csebuetnlp/banglabert) model.  
- The [CSEBUET NLP normalizer](https://github.com/csebuetnlp/normalizer) for text preprocessing.  
- The Hugging Face community for providing the platform and tools.

## Contact

For questions or issues, please open an issue on the model's repository or contact the authors.