---
license: mit
language:
- en
library_name: adaptive-classifier
tags:
- sentiment-analysis
- adaptive-classifier
- few-shot-learning
- continual-learning
- text-classification
- nlp
pipeline_tag: text-classification
widget:
- text: "I love this new technology!"
  example_title: "Positive Example"
- text: "This is terrible and I hate it."
  example_title: "Negative Example"
- text: "Learning is a process of gaining knowledge or skills."
  example_title: "Neutral Example"
- text: "Do you know what Granite Guardian 4 is?"
  example_title: "Neutral Question"
datasets:
- SetFit/tweet_sentiment_extraction
metrics:
- accuracy
model-index:
- name: adaptive-sentiment-classifier
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: SetFit/tweet_sentiment_extraction
      type: tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 0.800
      name: Test Accuracy
---

# Adaptive Sentiment Classifier

An improved sentiment analysis model using the adaptive-classifier library, designed for accurate classification of positive, negative, and neutral sentiments with special focus on technical and informational content.

## Model Description

This model is based on the [adaptive-classifier](https://github.com/MemChainAI/adaptive-classifier) library and uses DistilBERT as the underlying transformer. It has been specifically trained to properly classify:

- **Positive sentiment**: Expressions of satisfaction, enthusiasm, approval
- **Negative sentiment**: Expressions of dissatisfaction, frustration, criticism  
- **Neutral sentiment**: Factual information, questions, technical descriptions

## Key Improvements

- ✅ **Technical Content**: Properly classifies technical descriptions as neutral
- ✅ **Questions**: Correctly identifies questions as neutral rather than negative
- ✅ **Educational Content**: Handles informational text appropriately
- ✅ **Balanced Training**: Uses detailed class descriptions for better embeddings

## Training Data

- **Primary Dataset**: SetFit/tweet_sentiment_extraction (114 examples)
- **Training Method**: Adaptive classifier with continual learning
- **Class Distribution**: Balanced training with quality filtering
- **Additional Features**: Detailed class descriptions for stronger initial embeddings

## Performance

- **Test Accuracy**: 80.0%
- **Problematic Cases Resolved**: 8/10 challenging examples correctly classified
- **Improvement**: 100% increase from baseline accuracy

### Benchmark Examples

| Text | Expected | Predicted | ✓ |
|------|----------|-----------|---|
| "Granite Guardian 4 is a type of AI model..." | neutral | neutral | ✅ |
| "Do you know what Granite Guardian 4 is?" | neutral | neutral | ✅ |
| "Learning is a process of gaining knowledge..." | neutral | neutral | ✅ |
| "I love this new technology!" | positive | positive | ✅ |
| "This is terrible and I hate it." | negative | negative | ✅ |

## Usage

### Installation

```bash
pip install adaptive-classifier
```

### Basic Usage

```python
from adaptive_classifier import AdaptiveClassifier

# Load the model
classifier = AdaptiveClassifier.from_pretrained("MemChainAI/adaptive-sentiment-classifier")

# Make predictions
text = "This is a great product!"
predictions = classifier.predict(text)

# Get top prediction
label, confidence = predictions[0]
print(f"Sentiment: {label} ({confidence:.3f})")
```

### API Integration

This model is designed to work with the MemChain Models API:

```python
import requests

response = requests.post(
    "http://localhost:8033/model/sentiment/predict",
    json={"text": "Your text here", "k": 3}
)
result = response.json()
```

### Batch Processing

```python
texts = [
    "I love this!",
    "This is terrible.",
    "The system processes data automatically."
]

# Batch prediction
batch_results = classifier.predict_batch(texts)
for i, predictions in enumerate(batch_results):
    label, confidence = predictions[0]
    print(f"Text {i+1}: {label} ({confidence:.3f})")
```

## Training Methodology

1. **Class Descriptions**: Started with detailed descriptions of each sentiment class
2. **Quality Examples**: Used filtered, high-quality examples from the dataset
3. **Iterative Training**: Added examples gradually with evaluation at each step
4. **Continual Learning**: Leveraged adaptive classifier's continual learning capabilities

## Intended Use

- **Content Moderation**: Analyze user-generated content sentiment
- **Customer Feedback**: Classify customer reviews and feedback
- **Social Media**: Monitor social media sentiment
- **Technical Documentation**: Properly classify technical content as neutral
- **Educational Content**: Handle informational and educational text appropriately

## Limitations

- Optimized for English text
- Best performance on text similar to training data (tweets, reviews, questions)
- May require additional examples for domain-specific terminology
- Performance may vary on very long texts (>200 characters)

## Ethical Considerations

- The model should not be used as the sole basis for important decisions
- Bias may exist reflecting the training data
- Regular evaluation and retraining recommended for production use
- Consider cultural and contextual factors when interpreting results

## Citation

```bibtex
@misc{adaptive-sentiment-classifier-2025,
  title={Adaptive Sentiment Classifier},
  author={MemChain AI},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/MemChainAI/adaptive-sentiment-classifier}
}
```

## License

MIT License - see LICENSE file for details.

## Contact

For questions, issues, or contributions, please visit the [MemChain AI](https://www.memchain.ai/contact/).
