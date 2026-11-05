---
library_name: transformers
tags:
- sentiment-analysis
- text-classification
- turkish
license: mit
base_model:
- FacebookAI/xlm-roberta-base
---

# 🏆 TurkReviewSentiment-RoBERTa: Sentiment Analysis Model for Turkish Texts

📢 **A fine-tuned XLM-RoBERTa model for sentiment analysis in Turkish texts!**  
This model can classify user reviews and texts as **positive** or **negative** sentiment.

---

## 🔍 **Model Details**

### Model Description
✅ **Base Model:** XLM-RoBERTa  
✅ **Finetuned from:** `xlm-roberta-base`  
✅ **Training Data:** User reviews from e-commerce platforms  
✅ **Task:** Sentiment Analysis (Binary Classification: Positive / Negative)  
✅ **Language:** Turkish  
✅ **Use Cases:** Customer feedback analysis, social media monitoring, market research  
✅ **License:** MIT  

### Model Sources
- **Repository:** [Hugging Face Model Page](https://huggingface.co/fundaylnci/TurkReviewSentiment-RoBERTa)

---

## 📌 **How to Use the Model**
```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def load_model(model_path):
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

def get_sentiment(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return "positive" if predicted_class == 1 else "negative"

    
model_path = "fundaylnci/TurkReviewSentiment-RoBERTa"
model, tokenizer = load_model(model_path)

text ="Bu ürün harika!"
get_sentiment(text,model, tokenizer)

## Training Details

### Training Data

Dataset: E-commerce product reviews + manually labeled sentiment data


#### Preprocessing [optional]

Tokenization with xlm-roberta-base tokenizer


#### Training Hyperparameters

        training_args = TrainingArguments(
            output_dir="./results",
            evaluation_strategy="epoch",
            learning_rate=learning_rate,
            per_device_train_batch_size=batch_size,
            num_train_epochs=3,
            weight_decay=0.01,
            logging_dir="./logs",
            logging_steps=10,
        )

#### Speeds, Sizes, Times [optional]

Checkpoint Size: ~500MB

Training Time: ~6 hours on NVIDIA T4 GPU

## Evaluation

Evaluation Metrics: Accuracy, F1-score

# Version 149608e489c0979a661489d53245a30a48d3d38e
Accuracy: 0.961
Precision: 0.977
Recall: 0.980
F1 Score: 0.979


## Environmental Impact

Carbon emissions can be estimated using the Machine Learning Impact calculator.

Hardware: NVIDIA T4 GPU
Training Hours: ~6 hours
Cloud Provider: Google Cloud
Estimated CO2 Emitted: ~3.2 kg

## Citation [optional]

**BibTeX:**

@article{turkreviewsentiment2025,
  title={TurkReviewSentiment-RoBERTa: Sentiment Analysis for Turkish Reviews},
  author={Your Name},
  journal={Hugging Face Model Hub},
  year={2025}
}
