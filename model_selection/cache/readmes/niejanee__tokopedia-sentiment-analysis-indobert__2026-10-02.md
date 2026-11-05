---
language: id
license: apache-2.0
tags:
- sentiment-analysis
- indonesian
- indobert
- classification
- customer-reviews
pipeline_tag: text-classification
widget:
- text: "Produk sangat bagus, pengiriman cepat, recommended!"
  example_title: "Positive Review"
- text: "Barang jelek, tidak sesuai deskripsi, kecewa banget"
  example_title: "Negative Review"  
- text: "Produk biasa saja, tidak ada yang istimewa"
  example_title: "Neutral Review"
---

# Indonesian Sentiment Analysis with IndoBERT

This model is a fine-tuned version of `indobenchmark/indobert-base-p2` for sentiment analysis of Indonesian customer reviews.

## Model Description

- **Model Type**: BERT-based sequence classification
- **Language**: Indonesian (Bahasa Indonesia)
- **Base Model**: indobenchmark/indobert-base-p2
- **Task**: Sentiment Analysis (3 classes: Negative, Neutral, Positive)
- **Dataset**: Tokopedia Product Reviews 2019

## Intended Uses

This model is intended for sentiment analysis of Indonesian text, particularly customer reviews and product feedback.

### Direct Use

```python
from transformers import pipeline

# Load the model
sentiment_pipeline = pipeline("text-classification", model="niejanee/tokopedia-sentiment-analysis-indobert")

# Analyze sentiment
result = sentiment_pipeline("Produk sangat memuaskan, kualitas premium!")
print(result)
# Output: [{'label': 'LABEL_2', 'score': 0.9876}]  # LABEL_2 = Positive
```

### API Usage

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/niejanee/tokopedia-sentiment-analysis-indobert"
headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "Produk sangat bagus!",
})
print(output)
```

## Label Mapping

- `LABEL_0`: Negative sentiment
- `LABEL_1`: Neutral sentiment  
- `LABEL_2`: Positive sentiment

## Training Details

### Training Data

The model was trained on Indonesian customer reviews from Tokopedia with the following distribution:
- Negative: Reviews with ratings 1-2
- Neutral: Reviews with rating 3
- Positive: Reviews with ratings 4-5

### Training Procedure

- **Training Framework**: Hugging Face Transformers
- **Optimizer**: AdamW
- **Learning Rate**: 2e-5
- **Batch Size**: 16
- **Epochs**: 3
- **Max Sequence Length**: 512

## Usage Examples

### Python

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("niejanee/tokopedia-sentiment-analysis-indobert")
tokenizer = AutoTokenizer.from_pretrained("niejanee/tokopedia-sentiment-analysis-indobert")

# Create pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Predict sentiment
texts = [
    "Barang sangat bagus, pelayanan memuaskan!",
    "Produk tidak sesuai ekspektasi",
    "Kualitas standar, harga wajar"
]

results = classifier(texts)
for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']} (Score: {result['score']:.4f})")
```

### JavaScript

```javascript
async function analyzeSentiment(text) {
    const response = await fetch(
        "https://api-inference.huggingface.co/models/niejanee/tokopedia-sentiment-analysis-indobert",
        {
            method: "POST",
            headers: {
                "Authorization": "Bearer YOUR_HF_TOKEN",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "inputs": text
            }),
        }
    );
    
    const result = await response.json();
    return result;
}
```

## Limitations

- The model is specifically trained on Indonesian customer reviews and may not perform well on other types of Indonesian text
- Performance may vary on informal language, slang, or text with many typos
- The model was trained on e-commerce reviews and may have domain-specific biases

## License

This model is licensed under Apache 2.0.