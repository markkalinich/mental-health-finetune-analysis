---
library_name: transformers
tags:
  - text-classification
  - sentiment-analysis
  - imdb
  - bert
  - colab
  - huggingface
  - fine-tuned
license: apache-2.0
---

# 🤖 BERT IMDb Sentiment Classifier

A fine-tuned `bert-base-uncased` model for **binary sentiment classification** on the [IMDb movie reviews dataset](https://huggingface.co/datasets/imdb).  
Trained in Google Colab using Hugging Face Transformers with ~93% test accuracy.

---

## 📌 Model Details

### Model Description

- **Developed by:** Shubham Swarnakar
- **Shared by:** [ShubhamSwarnakar](https://huggingface.co/ShubhamSwarnakar)
- **Model type:** `BERTForSequenceClassification`
- **Language(s):** English 🇺🇸
- **License:** Apache-2.0
- **Fine-tuned from:** [bert-base-uncased](https://huggingface.co/bert-base-uncased)

### Model Sources

- **Repository:** https://huggingface.co/ShubhamSwarnakar/bert-imdb-colab-model
- **Demo:** Available via Hugging Face Inference Widget

---

## ✅ Uses

### Direct Use

Use this model for **sentiment analysis** on English movie reviews or similar texts.  
Returns either a `positive` or `negative` classification.

### Downstream Use

Can be fine-tuned further for domain-specific sentiment classification tasks.

### Out-of-Scope Use

Not designed for:
- Multilingual sentiment analysis
- Nuanced emotion detection (e.g., joy, anger, sarcasm)
- Non-movie domains without re-training

---

## ⚠️ Bias, Risks, and Limitations

This model inherits potential biases from:
- Pretrained BERT weights
- IMDb dataset (may reflect demographic or cultural skew)

### Recommendations

Avoid deploying this model in high-risk applications without auditing or further fine-tuning. Misclassification risk exists, especially with ambiguous or sarcastic text.

---

## 🚀 How to Get Started

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="ShubhamSwarnakar/bert-imdb-colab-model")
classifier("This movie was surprisingly entertaining!")




🧠 Training Details
Training Data
Dataset: IMDb Dataset

Format: Binary sentiment (positive = 1, negative = 0)

Training Procedure
Preprocessing: Tokenized with BertTokenizerFast

Epochs: 3

Optimizer: AdamW

Scheduler: Linear LR

Batch size: 8

Trained using Colab with limited GPU resources

📊 Evaluation
Metrics

Final test accuracy: 93.47%

Results Summary
Epoch	Validation Accuracy
1	        91.80%
2	        92.04%
3	        92.92%

Final test accuracy on held-out IMDb test split: 93.47%

🌱 Environmental Impact
Estimated based on lightweight training:

Hardware Type: Google Colab GPU (T4)

Training Duration: ~2 hours

Cloud Provider: Google

Region: Unknown

Emissions Estimate: ~0.15 kg CO₂eq

Estimate via ML CO2 Impact Calculator

🏗️ Technical Specifications
Architecture
BERT-base (12-layer, 768-hidden, 12-heads, 110M parameters)

Compute Infrastructure
Hardware: Google Colab with GPU

Software:

Python 3.11

Transformers 4.x

Datasets

PyTorch 2.x

📚 Citation

@misc{shubhamswarnakar_bert_imdb_2025,
  author       = {Shubham Swarnakar},
  title        = {BERT IMDb Sentiment Classifier},
  year         = 2025,
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ShubhamSwarnakar/bert-imdb-colab-model}},
}

🙋 More Info
For questions or collaboration, contact @ShubhamSwarnakar.
