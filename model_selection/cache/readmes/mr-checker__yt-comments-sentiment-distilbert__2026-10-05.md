---
license: apache-2.0
datasets:
- mr-checker/yt-tech-comments-dataset
language:
- en
metrics:
- accuracy
- f1
base_model:
- distilbert/distilbert-base-uncased
new_version: mr-checker/yt-comments-sentiment-distilbert
pipeline_tag: text-classification
library_name: transformers
tags:
- text-classification
- youtube
- comments
- sentiment-analysis
- pytorch
- transformers
---

# 📄 Model Card — YouTube Comment Sentiment (DistilBERT Fine‑Tuned)

### Model Details
- **Base model**: distilbert
- **Framework**: Hugging Face Transformers (PyTorch backend)
- **Task**: Multi‑class text classification
- **Classes**:  
  - Positive  
  - Negative  
  - Neutral  
  - Off‑topic  
  - Question  

### Training Data
- **Source**: [yt-tech-comments-dataset](https://huggingface.co/datasets/mr-checker/yt-tech-comments-dataset)
- **Language**: English and Hinglish.  
- **Preprocessing**:  
  - Null values removed  
  - Combined `title + comment_text` for context  
  - Tokenized with DistilBERT tokenizer (max length = 256)  

### Evaluation
- **Metrics used**: Accuracy, F1‑score
- **Observations**:  
  - Performs well on clear positive/negative sentiment.  
  - Misclassifies requests (“Give me credits”) and ambiguous remarks (“Sometimes I do think he is also AI”).  
  - Needs more training examples for **Off‑topic** and **Question** categories.  

### Intended Use
- **Primary**: Sentiment and intent analysis of YouTube comments for content creators and marketers.  
- **Secondary**: Dashboard visualization of per‑video sentiment distribution.  

### Limitations
- Struggles with sarcasm, mixed sentiment, and multilingual comments.  
- Off‑topic and question detection accuracy depends heavily on balanced training data.  
- Not suitable for toxic content moderation without additional fine‑tuning.  

### Example Inference
```python
import pandas as pd
from transformers import pipeline

# Load your fine-tuned model
sentiment_pipeline = pipeline(
    "text-classification",
    model="mr-checker/yt-comments-sentiment-distilbert",  # replace with your repo/local path
    tokenizer="mr-checker/yt-comments-sentiment-distilbert"
)

# Example dataframe (already merged with titles)
eval_df = pd.DataFrame({
    "title": ["I Created a $1.000.000 Beauty Brand Using AI"],
    "comment_text": ["This video is amazing, but credits are too expensive!"]
})

# Combine title + comment_text
eval_df["text"] = (
    eval_df["title"].astype(str)
    + " [SEP] "
    + eval_df["comment_text"].astype(str)
)

# Run inference
results = sentiment_pipeline(
    list(eval_df["text"]),
    truncation=True,
    max_length=256
)

# Attach predictions back to dataframe
eval_df["predicted_label"] = [r["label"] for r in results]
eval_df["confidence"] = [r["score"] for r in results]

print(eval_df[["title", "comment_text", "predicted_label", "confidence"]])
```
