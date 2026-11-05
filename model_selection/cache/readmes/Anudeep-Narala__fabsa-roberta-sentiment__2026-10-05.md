---
language: en
tags:
- sentiment-analysis
- aspect-based-sentiment-analysis
- roberta
- food-delivery
- text-classification
license: mit
base_model: cardiffnlp/twitter-roberta-base-sentiment-latest
metrics:
- accuracy
widget:
- text: "The food was amazing but delivery took forever [SEP] delivery"
  example_title: "Delivery Sentiment"
- text: "Great prices and fantastic customer service [SEP] service"
  example_title: "Service Sentiment"
- text: "The app is really easy to use and intuitive [SEP] interface"
  example_title: "Interface Sentiment"
---

# FABSA RoBERTa Sentiment Analysis Model

<div align="center">
  <img src="https://img.shields.io/badge/Accuracy-93.97%25-brightgreen" alt="Accuracy">
  <img src="https://img.shields.io/badge/Model-RoBERTa-blue" alt="Model">
  <img src="https://img.shields.io/badge/Task-ABSA-orange" alt="Task">
</div>

## 📊 Model Overview

This is a **fine-tuned RoBERTa model** for **Aspect-Based Sentiment Analysis (ABSA)** on food delivery reviews, achieving **93.97% accuracy** on the validation set. The model analyzes customer reviews across multiple specific aspects like food quality, delivery service, pricing, and more.

### 🎯 What is Aspect-Based Sentiment Analysis?

Unlike traditional sentiment analysis that gives one overall sentiment, ABSA identifies sentiment for **specific aspects** of a product or service. For example:

> *"The food was amazing but delivery took forever"*

- **Food aspect**: ✅ Positive
- **Delivery aspect**: ❌ Negative

This granular analysis helps businesses identify exactly what customers love and what needs improvement.

## 🚀 Quick Start

### Using the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "Anudeep-Narala/fabsa-roberta-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example: Analyze a review
review = "The food was delicious but the delivery was slow"
aspect = "delivery"  # Can be: food, delivery, service, price, interface, overall

# Format input
input_text = f"Review: {review} | Aspect: {aspect}"
inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=256)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1).item()
    confidence = predictions[0][predicted_class].item()

# Map prediction to sentiment
sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}
print(f"Aspect: {aspect}")
print(f"Sentiment: {sentiment_map[predicted_class]}")
print(f"Confidence: {confidence:.2%}")
```

### Batch Processing Multiple Aspects

```python
def analyze_review(review_text, aspects=["food", "delivery", "service", "price"]):
    """Analyze a review across multiple aspects"""
    results = {}

    for aspect in aspects:
        input_text = f"Review: {review_text} | Aspect: {aspect}"
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=256)

        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
            predicted_class = torch.argmax(predictions, dim=-1).item()
            confidence = predictions[0][predicted_class].item()

        sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}
        results[aspect] = {
            "sentiment": sentiment_map[predicted_class],
            "confidence": confidence
        }

    return results

# Example usage
review = "Great food and reasonable prices, but the app keeps crashing"
results = analyze_review(review)

for aspect, result in results.items():
    print(f"{aspect.capitalize()}: {result['sentiment']} (confidence: {result['confidence']:.2%})")
```

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| **Validation Accuracy** | 93.97% |
| **Training Loss** | 0.1611 |
| **Validation Loss** | 0.1749 |
| **Training Time** | 302.74 seconds |
| **Training Examples** | 13,998 |
| **Validation Examples** | 1,858 |

## 🎯 Supported Aspects

The model is trained to analyze sentiment for these specific aspects:

1. **food** - Food quality, taste, freshness, presentation
2. **delivery** - Delivery speed, reliability, driver behavior, packaging
3. **service** - Customer support, staff attitude, responsiveness
4. **price** - Value for money, fees, discounts, pricing fairness
5. **interface** - App/website usability, navigation, features
6. **overall** - General satisfaction and overall experience

## 🏷️ Sentiment Classes

- **Positive** (2): Favorable opinion, satisfaction, praise
- **Neutral** (1): Mixed feelings, objective statements, neutral tone
- **Negative** (0): Complaints, dissatisfaction, criticism

## 🛠️ Technical Details

### Model Architecture
- **Base Model**: [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)
- **Architecture**: RoBERTa (Robustly Optimized BERT Pretraining Approach)
- **Model Type**: Encoder-based transformer
- **Number of Parameters**: ~125M
- **Fine-tuning Task**: Sequence Classification (3 classes)

### Training Configuration
- **Epochs**: 3
- **Learning Rate**: 8e-6 with cosine restarts
- **Batch Size**: 16
- **Max Sequence Length**: 128 tokens
- **Optimizer**: AdamW
- **Framework**: PyTorch + Hugging Face Transformers

### Dataset
- **Name**: [jordiclive/FABSA](https://huggingface.co/datasets/jordiclive/FABSA)
- **Domain**: FABSA, An aspect-based sentiment analysis dataset in the Customer Feedback space (Trustpilot, Google Play and Apple Store reviews).
- **Training Set**: 13,998 labeled examples
- **Validation Set**: 1,858 examples
- **Test Set**: 1,587 examples (reserved)
- **Languages**: English
- **Annotation**: Aspect-level sentiment labels

## 💡 Use Cases

### Business Intelligence
- **Customer Feedback Analysis**: Automatically categorize and analyze thousands of reviews
- **Competitive Analysis**: Compare sentiment across platforms and competitors
- **Product Development**: Identify which aspects need improvement
- **Quality Monitoring**: Track sentiment trends over time

### Real-time Applications
- **Dashboard Analytics**: Build live sentiment monitoring dashboards
- **Alert Systems**: Trigger alerts when negative sentiment spikes
- **Customer Support**: Prioritize reviews that need immediate attention
- **A/B Testing**: Measure impact of changes on specific aspects

### Research
- **Sentiment Analysis Studies**: Benchmark against other ABSA models
- **Multi-aspect Learning**: Study aspect-specific sentiment patterns
- **Transfer Learning**: Fine-tune for other domains (e-commerce, hospitality)

## 📊 Example Results

```python
review = "Amazing pizza and great prices! The delivery was fast but the driver was rude."
```

**Analysis Output**:
- 🍕 **Food**: Positive (98.5% confidence)
- 💰 **Price**: Positive (94.2% confidence)
- 🚚 **Delivery**: Negative (87.6% confidence)
- 👤 **Service**: Negative (91.3% confidence)

This granular insight shows that while the product and pricing are excellent, there are service issues that need addressing.

## 🔧 Installation

```bash
pip install transformers torch
```

For production environments with GPU acceleration:
```bash
pip install transformers torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## ⚡ Performance Tips

1. **Batch Processing**: Process multiple reviews at once for better throughput
2. **GPU Acceleration**: Use CUDA for ~10x faster inference
3. **Model Quantization**: Use quantization for reduced memory footprint
4. **ONNX Export**: Convert to ONNX for optimized production deployment

```python
# Enable GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

## 🔄 Model Evolution

This model represents the final iteration of extensive experimentation:

1. **Red-Pajama-7B**: 8% accuracy (decoder limitations for classification)
2. **DialoGPT-small**: 51.5% (baseline)
3. **RoBERTa Basic**: 86% (initial fine-tuning)
4. **RoBERTa Enhanced**: 90.7% (improved hyperparameters)
5. **RoBERTa Neutral-focused**: 91.7% (class imbalance handling)
6. **RoBERTa Final**: **93.97%** ✅ (optimal configuration)

## 📚 Related Resources

- **GitHub Repository**: [aspect-based-sentiment-analysis](https://github.com/Anudeepreddynarala/aspect-based-sentiment-analysis)
- **Interactive Demo**: See the repository for visualization dashboard
- **Dataset Schema**: CSV format with aspect-level annotations
- **Training Code**: Available in the repository

## 📄 Citation

If you use this model in your research or application, please cite:

```bibtex
@misc{narala2025fabsa,
  author = {Anudeep Reddy Narala},
  title = {FABSA RoBERTa: Fine-tuned Model for Aspect-Based Sentiment Analysis on Food Delivery Reviews},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/Anudeep-Narala/fabsa-roberta-sentiment}},
}
```

## 📧 Contact

- **Author**: Anudeep Reddy Narala
- **Email**: anudeepreddynarala1@gmail.com
- **GitHub**: [@Anudeepreddynarala](https://github.com/Anudeepreddynarala)

## 📜 License

This model is released under the **MIT License**. Feel free to use it for commercial and non-commercial applications.

## 🙏 Acknowledgments

- Base model: [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)
- Framework: Hugging Face Transformers
- Compute: Training performed on GPU infrastructure

---

**Ready to analyze your customer feedback?** Try the model now! 🚀