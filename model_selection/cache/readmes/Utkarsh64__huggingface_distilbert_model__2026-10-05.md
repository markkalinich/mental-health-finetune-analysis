---
license: mit
tags:
- emotion-classification
- mental-health
- multi-label
- transformers
- distilbert
- goemotions
language:
- en
metrics:
- f1
- precision
- recall
pipeline_tag: text-classification
base_model: distilbert-base-uncased
---

# Mental Health Emotion Detection - Enhanced DistilBERT

This model is a fine-tuned DistilBERT for multi-label emotion classification in mental health applications, detecting 28 different emotions from text input with enhanced architecture and advanced training techniques.

## Model Description

- **Model Type:** Enhanced DistilBERT (Fine-tuned)
- **Base Model:** distilbert-base-uncased
- **Task:** Multi-label emotion classification
- **Dataset:** GoEmotions (balanced and enhanced)
- **Languages:** English
- **Architecture:** Enhanced with additional layers, focal loss, and class balancing

## Performance

| Metric | Score |
|--------|-------|
| F1-Score | 0.298 |
| Precision | 0.459 |
| Recall | 0.260 |
| Accuracy | 89.5% |
| Improvement | 7.6x over baseline |

## Emotions Detected

The model can detect 28 emotions: admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("YOUR_USERNAME/mental-health-enhanced-distilbert")
model = AutoModelForSequenceClassification.from_pretrained("YOUR_USERNAME/mental-health-enhanced-distilbert")

# Example usage
text = "I'm feeling really anxious about tomorrow"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.sigmoid(outputs.logits)

# Get emotion labels
emotions = []
for i, score in enumerate(predictions[0]):
    if score > 0.4:  # Threshold
        emotion = model.config.id2label[i]
        emotions.append((emotion, score.item()))

print(emotions)
```

## Training Details

### Enhanced Architecture
- **Base:** DistilBERT with additional hidden layers
- **Enhancements:** 
  - Layer normalization
  - Dropout regularization
  - Enhanced forward pass with ReLU activations
  - Multi-layer classification head (768 → 512 → 256 → 128 → 28)

### Advanced Training Techniques
- **Loss Function:** Focal Loss for class imbalance handling
- **Class Weighting:** Advanced weighting for rare emotions
- **Data Balancing:** Oversampling rare emotions, undersampling common ones
- **Optimization:** AdamW with cosine scheduling
- **Early Stopping:** Patience-based with best model saving

### Training Data
- **Dataset:** GoEmotions (balanced subset)
- **Training Samples:** ~12,750
- **Validation Samples:** ~2,250
- **Preprocessing:** Contraction expansion, lowercase normalization
- **Balancing:** Advanced sampling for 28 emotion categories

## Model Architecture

```
Input Text → DistilBERT Encoder → Enhanced Classification Head
                                        ↓
                                   Hidden Layer 1 (768→512)
                                        ↓
                                   Hidden Layer 2 (512→256)  
                                        ↓
                                   Hidden Layer 3 (256→128)
                                        ↓
                                   Output Layer (128→28)
```

## Intended Use

This model is designed for:
- Mental health chatbots and companions
- Emotion-aware dialogue systems
- Mental health screening tools
- Research in computational psychology
- Empathetic AI applications

## Limitations

- Trained primarily on English text
- Performance may vary with very informal language
- Should not be used as sole diagnostic tool for mental health
- Requires context for optimal performance

## Training Metrics by Epoch

| Epoch | F1-Score | Precision | Recall |
|-------|----------|-----------|--------|
| 1 | 0.0145 | 0.0419 | 0.0089 |
| 2 | 0.1430 | 0.2797 | 0.1211 |
| 3 | 0.2141 | 0.4751 | 0.1804 |
| 4 | 0.2749 | 0.4317 | 0.2340 |
| 5 | 0.2897 | 0.4524 | 0.2533 |
| 6 | 0.2981 | 0.4592 | 0.2597 |

## Citation

If you use this model, please cite:

```
@misc{mental-health-emotion-distilbert,
  title={Mental Health Emotion Detection - Enhanced DistilBERT},
  author={Your Name},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/YOUR_USERNAME/mental-health-enhanced-distilbert}
}
```

## Acknowledgments

- Built on DistilBERT by Hugging Face
- Trained on GoEmotions dataset
- Enhanced with advanced ML techniques for mental health applications
