---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- sentiment-analysis
- text-classification
- pytorch
- distilbert
- fine-tuned
datasets:
- imdb
language:
- en
pipeline_tag: text-classification
widget:
- text: "This movie is absolutely amazing! I loved every minute of it."
  example_title: "Positive Example"
- text: "Terrible film, complete waste of time and money."
  example_title: "Negative Example"
---

# DistilBERT Sentiment Analysis Model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) for **2-class sentiment analysis** (Positive, Negative) on movie reviews.

## 🎯 Model Description

- **Model Type:** Text Classification
- **Base Architecture:** DistilBERT (Distilled BERT)
- **Language:** English
- **Task:** Sentiment Analysis
- **Classes:** 2 (Negative, Positive)
- **Parameters:** ~66M
- **Model Size:** ~250MB

## 🚀 Quick Start

### Using Transformers Pipeline

```python
from transformers import pipeline

# Load the model
classifier = pipeline("sentiment-analysis", 
                     model="your-username/sentiment-analysis-distilbert")

# Single prediction
result = classifier("This movie is fantastic!")
print(result)
# Output: [{'label': 'POSITIVE', 'score': 0.9987}]

# Batch prediction
texts = [
    "Amazing cinematography and great acting!",
    "Boring and predictable storyline.",
    "It was an okay movie, nothing extraordinary."
]
results = classifier(texts)
for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']} (Confidence: {result['score']:.3f})")
```

### Using AutoModel and AutoTokenizer

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "your-username/sentiment-analysis-distilbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare input
text = "This movie exceeded my expectations!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
# Get predicted class
predicted_class = torch.argmax(predictions, dim=-1).item()
confidence = predictions[0][predicted_class].item()

labels = ["NEGATIVE", POSITIVE"]
print(f"Sentiment: {labels[predicted_class]} (Confidence: {confidence:.3f})")
```

## 📊 Training Details

### Dataset
- **Source:** IMDB Movie Reviews Dataset
- **Training Samples:** 5,000 (balanced: 1,667 per class)
- **Evaluation Samples:** 1,000
- **Data Split:** 80% train, 20% validation
- **Preprocessing:** Tokenization with DistilBERT tokenizer, max length 256

### Training Configuration
- **Base Model:** `distilbert-base-uncased`
- **Training Framework:** PyTorch + Transformers
- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Batch Size:** 8
- **Epochs:** 3
- **Warmup Steps:** 100
- **Weight Decay:** 0.01
- **Max Sequence Length:** 256 tokens

### Hardware
- **Platform:** Google Colab
- **GPU:** Tesla T4 (15GB VRAM)
- **Training Time:** ~30-45 minutes

## 📈 Performance

| Metric | Score |
|--------|-------|
| Training Accuracy | ~95% |
| Validation Accuracy | ~93% |
| Training Loss | 0.12 |
| Validation Loss | 0.18 |

### Class Distribution
- **Negative:** 33.3% (2500 samples)
- **Positive:** 33.3% (2500 samples)

## 🎯 Intended Use

### Primary Use Cases
- **Movie Review Analysis:** Classify sentiment of movie reviews
- **Product Review Sentiment:** Analyze customer feedback
- **Social Media Monitoring:** Track sentiment in posts and comments
- **Content Moderation:** Identify negative sentiment in user-generated content

### Suitable Domains
- Entertainment and media reviews
- E-commerce product feedback
- Social media posts
- Customer service interactions
- General English text sentiment analysis

## ⚠️ Limitations and Biases

### Known Limitations
- **Domain Specificity:** Primarily trained on movie reviews, may not generalize well to other domains
- **Language:** English only, no multilingual support
- **Context Length:** Limited to 256 tokens, longer texts are truncated
- **Cultural Bias:** May reflect biases present in IMDB dataset

### Potential Biases
- **Genre Bias:** May perform differently across movie genres
- **Temporal Bias:** Training data may reflect sentiment patterns from specific time periods
- **Demographic Bias:** May not equally represent all demographic groups' sentiment expressions

### Not Recommended For
- Non-English text
- Highly specialized domains (medical, legal, technical)
- Real-time critical applications
- Texts longer than 256 tokens without preprocessing
- Sarcasm or irony detection

## 🔧 Technical Specifications

### Model Architecture
```
DistilBERT Base
├── Transformer Layers: 6
├── Hidden Size: 768
├── Attention Heads: 12
├── Intermediate Size: 3072
└── Classification Head: Linear(768 → 3)
```

### Input Format
- **Text Encoding:** UTF-8
- **Tokenization:** WordPiece
- **Special Tokens:** [CLS], [SEP]
- **Max Length:** 256 tokens
- **Padding:** Right padding with [PAD] tokens

### Output Format
```python
{
    'label': 'POSITIVE',  # One of: NEGATIVE, POSITIVE
    'score': 0.9987       # Confidence score (0-1)
}
```

## 📝 Citation

If you use this model in your research or applications, please cite:

```bibtex
@misc{sentiment-analysis-distilbert,
  title={Fine-tuned DistilBERT for Sentiment Analysis},
  author={Your Name},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/your-username/sentiment-analysis-distilbert}
}
```

## 📄 License

This model is released under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Issues and pull requests are welcome! Please feel free to:
- Report bugs or issues
- Suggest improvements
- Share your use cases
- Contribute to documentation

## 🙏 Acknowledgments

- **Hugging Face** for the Transformers library and model hosting
- **Google Research** for the original BERT and DistilBERT models
- **Stanford AI Lab** for the IMDB dataset
- **Google Colab** for providing free GPU resources for training

---

*This model was created as part of a sentiment analysis fine-tuning project using modern NLP techniques and best practices.*