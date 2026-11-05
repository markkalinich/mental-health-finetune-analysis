---
language: en
tags:
- emotion-classification
- multilabel-classification
- text-classification
- pytorch
- transformers
datasets:
- emotion
metrics:
- f1
- accuracy
library_name: transformers
pipeline_tag: text-classification
---

# Multilabel Emotion Classification Model - FirstTimeUp

This model is fine-tuned for multilabel emotion classification using distilbert-base-uncased as the base model.

## Model Details
- **Model Name**: FirstTimeUp
- **Base Model**: distilbert-base-uncased
- **Task**: Multilabel Emotion Classification
- **Emotions**: amusement, anger, annoyance, caring, confusion, disappointment, disgust, embarrassment, excitement, fear, gratitude, joy, love, sadness
- **Total Parameters**: 66,373,646
- **Trainable Parameters**: 66,373,646

## Quick Start

### Installation
```bash
pip install torch transformers huggingface_hub
```

### Usage

```python
# Download the repository
from huggingface_hub import snapshot_download
import sys
import os

# Download model files
model_path = snapshot_download(repo_id="EnJiZ/FirstTimeUp")

# Add to path and import
sys.path.append(model_path)
from model import predict_emotions

# Predict emotions
text = "I am so happy and excited!"
emotions = predict_emotions(text, model_path)
print(emotions)
```

### Advanced Usage

```python
import torch
from transformers import AutoTokenizer
import sys
sys.path.append(model_path)
from model import MultiLabelEmotionClassifier, load_model

# Load model manually
model, config = load_model(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Custom prediction with different threshold
def custom_predict(text, threshold=0.3):
    encoding = tokenizer(
        text,
        truncation=True,
        padding='max_length',
        max_length=128,
        return_tensors='pt'
    )
    
    model.eval()
    with torch.no_grad():
        logits = model(encoding['input_ids'], encoding['attention_mask'])
        probabilities = torch.sigmoid(logits)
        predictions = (probabilities > threshold).int()
    
    emotion_labels = ['amusement', 'anger', 'annoyance', 'caring', 'confusion', 'disappointment', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'joy', 'love', 'sadness']
    result = {emotion: {
        'predicted': bool(pred), 
        'probability': float(prob)
    } for emotion, pred, prob in zip(emotion_labels, predictions[0], probabilities[0])}
    return result

# Example with probabilities
result = custom_predict("I feel great today!", threshold=0.3)
print(result)
```

## Model Architecture
- **Base**: distilbert-base-uncased
- **Classification Head**: Linear layer with dropout (dropout_rate=0.3)
- **Loss Function**: BCEWithLogitsLoss
- **Activation**: Sigmoid (for multilabel classification)

## Training Details
- **Epochs**: 3
- **Batch Size**: 32
- **Learning Rate**: 2e-05
- **Max Sequence Length**: 128
- **Optimizer**: AdamW with weight decay (0.01)
- **Scheduler**: Linear warmup + decay

## Files in this Repository
- `config.json`: Model configuration
- `pytorch_model.bin`: Model weights
- `tokenizer.json`, `tokenizer_config.json`: Tokenizer files
- `model.py`: Custom model class and utility functions
- `README.md`: This file

## Performance
- **Task**: Multilabel Emotion Classification
- **Metrics**: F1-Score (Micro & Macro), Accuracy
- **Validation Strategy**: 80/20 train-validation split

## Supported Emotions
amusement, anger, annoyance, caring, confusion, disappointment, disgust, embarrassment, excitement, fear, gratitude, joy, love, sadness

## License
This model is released under the Apache 2.0 license.

## Citation
```bibtex
@misc{firsttimeup2024,
  title={FirstTimeUp: Multilabel Emotion Classification Model},
  author={EnJiZ},
  year={2024},
  url={https://huggingface.co/EnJiZ/FirstTimeUp}
}
```

## Contact
For questions or issues, please open an issue in the repository.
