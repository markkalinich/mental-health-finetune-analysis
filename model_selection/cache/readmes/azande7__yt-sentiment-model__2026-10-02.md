---
tags:
- text-classification
- sentiment-analysis
language:
- en
pipeline_tag: text-classification
---
## Youtube Comment Sentiment Classifier

This project fine-tunes a DistilBERT transformer model to classify YouTube comments into Positive, Neutral, or Negative sentiments. The goal was to explore Natural Language Processing (NLP) concepts and learn in detail the process of fine-tuning pretrained language models using Hugging Face Transformers and PyTorch. Additionally, the dataset, sourced from Kaggle, consists of user comments retrieved from YouTube videos, each labeled with a sentiment category; positive, neutral, and negative respectively.

### Tools and Libraries used;
- Python 3.13
- Hugging Face Transformers (v4.57.1)
- Datasets (Hugging Face)
- PyTorch 2.8.0
- Accelerate 1.10.1
### Dataset;
**File:** `YoutubeCommentsDataSet.csv`
**columns;**
- `comment` the text of the YouTube comment
- `sentiment` label (*positive*, *neutral*, *negative*)

After preprocessing;
- The `text` transformed into tokenized input to the model.
- The `label` was encoded with integer values, 0 = negative, 1 = neutral, 2 = positive.

### Model and Training Details
| Parameter | Value |
|------------|--------|
| **Model** | `distilbert-base-uncased` |
| **Task** | Sequence Classification (3 labels) |
| **Train/Test Split** | 80/20 |
| **Batch Size** | 8 |
| **Learning Rate** | 2e-5 |
| **Epochs** | 2 |
| **Weight Decay** | 0.01 |
| **Optimizer** | AdamW |

---

### Results
| Metric | Score |
|---------|:------:|
| **Training Loss** | 0.37 |
| **Evaluation Loss** | 0.49 |
| **Accuracy** | 0.84 |
| **Weighted F1 Score** | 0.84 |

Overall the model achieved strong performance on unseen YouTube comments, which demonstrated effective transfer learning from pretrained weights to real-world text.

### How to Run the Project
# 1. Clone the repository
```bash 
git clone https://github.com/<your-username>/yt_comment_classifier.git
cd yt_comment_classifier

# 2. Install dependencies
pip install torch transformers datasets evaluate accelerate

# 3. Run the Jupyter notebook
jupyter notebook

# Author
Benjamin Henson
https://www.linkedin.com/in/hensonben/

---
language: en
tags:
- text-classification
- sentiment-analysis
pipeline_tag: text-classification
license: mit
---