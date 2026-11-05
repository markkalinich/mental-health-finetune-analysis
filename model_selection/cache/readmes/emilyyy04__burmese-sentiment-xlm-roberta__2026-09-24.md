---
license: mit
datasets:
- kalixlouiis/burmese-sentiment-analysis
- chuuhtetnaing/myanmar-social-media-sentiment-analysis-dataset
language:
- my
- en
metrics:
- f1
- precision
- recall
- accuracy
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
library_name: transformers
tags:
- sentiment
- pytorch
- transformers
- burmese
---
# Burmese Sentiment Analysis with XLM-RoBERTa

## Model Details

### Model Description
This model is a fine-tuned version of **FacebookAI/xlm-roberta-base** for **Burmese sentiment analysis**.  
It classifies Burmese text into one of three sentiment categories:
- **Positive**
- **Negative**
- **Neutral**

The model was trained using publicly available Burmese sentiment datasets and additional manually curated data, with careful preprocessing to normalize encoding (Zawgyi → Unicode conversion).

- **Developer:** Yoon Thiri Aung ([GitHub](https://github.com/yoon-thiri04))
- **Model type:** Transformer-based multilingual masked language model fine-tuned for text classification
- **Languages:** Burmese (`my`), with multilingual base model support
- **License:** MIT
- **Finetuned from:** FacebookAI/xlm-roberta-base
- **Demo:** https://huggingface.co/spaces/emilyyy04/burmese-sentiment-analysis-demo
---

## Uses

### Direct Use
- Sentiment classification of Burmese text from social media, reviews, comments, and other user-generated content.
- Building sentiment-aware Burmese NLP applications such as chatbots, analytics dashboards, and content moderation tools.

### Limitations
- May not generalize well to domains significantly different from the training data.
- May misclassify sentences with mixed sentiments or sarcasm.
- Performance may drop for code-mixed Burmese-English text with heavy slang or informal spelling.

---

## Training Details

### Training Data
- **Sources:**
  - [`kalixlouiis/burmese-sentiment-analysis`](https://huggingface.co/datasets/kalixlouiis/burmese-sentiment-analysis)
  - [`chuuhtetnaing/myanmar-social-media-sentiment-analysis-dataset`](https://huggingface.co/datasets/chuuhtetnaing/myanmar-social-media-sentiment-analysis-dataset)
  - Additional curated data collected and annotated by the author.

- **Preprocessing:**
  - Converted Zawgyi-encoded text to Unicode.
  - Cleaned and normalized text fields.
  - Tokenized using the XLM-RoBERTa tokenizer with:
    - `max_length=128`
    - Truncation and padding to maximum length.

### Training Procedure
- **Optimizer:** AdamW (default in Hugging Face `Trainer`)
- **Learning rate:** 2e-5
- **Batch size:** 8 (train & eval)
- **Epochs:** 3
- **Weight decay:** 0.01
- **Mixed precision (fp16):** Enabled when training on GPU
- **Metric for best model:** F1 score (weighted average)
- **Evaluation strategy:** Per epoch
- **Model selection:** Best F1 score checkpoint

---

## Evaluation

### Metrics
The model was evaluated on a held-out validation set using accuracy, precision, recall, and F1 score.

| Epoch | Val Loss  | Accuracy | Precision | Recall   | F1       |
|-------|-----------|----------|-----------|----------|----------|
| 1     | 0.6171    | 0.7859   | 0.7994    | 0.7859   | 0.7875   |
| 2     | 0.4268    | 0.8470   | 0.8465    | 0.8470   | 0.8464   |
| 3     | 0.4115    | 0.8451   | 0.8447    | 0.8451   | 0.8448   |

The final model used is the checkpoint with the highest **F1 score**.

---

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "emilyyy04/burmese-sentiment-xlm-roberta"  # Replace with actual repo name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "ဒီဇာတ်လမ်းက တကယ်ကောင်းတယ်။"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
predicted_class = torch.argmax(outputs.logits, dim=1).item()

label_map = {0: "positive", 1: "negative", 2: "neutral"}
print("Predicted Sentiment:", label_map[predicted_class])