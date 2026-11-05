---
language:
  - en
license: mit
library_name: transformers
tags:
  - audio
  - emotion-classification
  - arousal-valence
  - speech
  - pytorch
  - custom
pipeline_tag: audio-classification
datasets:
  - TESS
  - CREMA-D
metrics:
  - accuracy
  - mse
model-index:
  - name: emotion-av-model
    results:
      - task:
          type: audio-classification
          name: Audio Emotion Classification
        dataset:
          type: tess-crema-d
          name: Combined TESS and CREMA-D
        metrics:
          - type: accuracy
            value: 0.96
            name: Test Accuracy
          - type: mse
            value: 0.094
            name: Arousal-Valence MSE
---

# Audio Emotion Classification with Arousal-Valence Prediction

This model performs audio emotion classification while simultaneously predicting continuous arousal and valence values. It combines multiple audio features (Wav2Vec2, MFCC, and prosodic features) to achieve robust emotion recognition.

## Model Description

- **Task**: Audio emotion classification with arousal-valence prediction
- **Architecture**: Dual-branch neural network (emotion + arousal-valence)
- **Features**: Wav2Vec2 (768) + MFCC (13) + Prosodic (6) = 787 dimensions
- **Emotions**: angry, disgust, fear, happy, neutral, sad
- **Performance**: ~96% accuracy on test set, MSE ~0.094 for arousal-valence

## Quick Start

### Using the Pipeline (Recommended)

```python
from pipeline_emotion_av import pipeline

# Create pipeline
emotion_pipeline = pipeline(
    "audio-emotion-classification",
    model="pricklypearhealth/emotion-av-model"
)

# Process audio
result = emotion_pipeline("path/to/audio.wav", return_all_scores=True)
print(result)
```

### Direct Model Usage

```python
from modeling_emotion_av import EmotionAVModel
from feature_extraction_emotion_av import EmotionAVFeatureExtractor

# Load model and feature extractor
model = EmotionAVModel.from_pretrained("pricklypearhealth/emotion-av-model")
feature_extractor = EmotionAVFeatureExtractor.from_pretrained("pricklypearhealth/emotion-av-model")

# Process audio file
features = feature_extractor.from_file("path/to/audio.wav", return_tensors="pt")
result = model.predict_emotion(features["input_features"])

print(f"Emotion: {result['emotion']}")
print(f"Confidence: {result['confidence']:.4f}")
print(f"Arousal: {result['arousal']:.4f}")
print(f"Valence: {result['valence']:.4f}")
```

## Features

### Multi-Modal Feature Extraction

- **Wav2Vec2**: Pre-trained transformer features from facebook/wav2vec2-base-960h
- **MFCC**: 13 Mel-frequency cepstral coefficients
- **Prosodic**: Pitch (mean/std), energy, zero-crossing rate, jitter, shimmer

### Dual Prediction Output

- **Discrete Emotions**: 6-class classification (angry, disgust, fear, happy, neutral, sad)
- **Continuous Values**: Arousal (-1 to +1) and Valence (-1 to +1) scores

### Flexible Input Formats

- Audio file paths (WAV, MP3, etc.)
- Raw audio arrays (numpy)
- List of audio samples
- Batch processing support

## Training Details

- **Datasets**: TESS + CREMA-D (balanced via oversampling)
- **Features**: Wav2Vec2 + MFCC + Prosodic (787 total dimensions)
- **Architecture**: Dual-branch neural network with BatchNorm and Dropout
- **Training**: 30 epochs with early stopping, ReduceLROnPlateau scheduler

## Model Architecture

```
Input Audio (16kHz)
    ↓
Feature Extraction:
├── Wav2Vec2 (768 features)
├── MFCC (13 features)
└── Prosodic (6 features)
    ↓
Combined Features (787 dims)
    ↓
Dual Branch Network:
├── Emotion Branch → 6-class Classification
└── AV Branch → 2D Regression (Arousal, Valence)
```

## API Usage

### Inference API

This model supports the Hugging Face Inference API. You can use it directly:

```python
import requests
import base64

# Encode audio file
with open("audio.wav", "rb") as f:
    audio_bytes = f.read()
    audio_b64 = base64.b64encode(audio_bytes).decode()

# Make API request
response = requests.post(
    "https://api-inference.huggingface.co/models/pricklypearhealth/emotion-av-model",
    headers={"Authorization": "Bearer YOUR_HF_TOKEN"},
    json={"inputs": audio_b64}
)

result = response.json()
print(result)
```

### Expected Response Format

```json
[
  {
    "label": "happy",
    "score": 0.8542,
    "arousal": 0.7234,
    "valence": 0.9123,
    "all_scores": [
      { "label": "happy", "score": 0.8542 },
      { "label": "neutral", "score": 0.0892 },
      { "label": "sad", "score": 0.0456 }
    ]
  }
]
```

### Using Inference Endpoints

For production use, you can deploy this model on Hugging Face Inference Endpoints:

```python
import requests
import base64

# Encode audio file
with open("audio.wav", "rb") as f:
    audio_bytes = f.read()
    audio_b64 = base64.b64encode(audio_bytes).decode()

# Make request to your Inference Endpoint
response = requests.post(
    "https://YOUR_ENDPOINT_URL.endpoints.huggingface.cloud",
    headers={
        "Authorization": "Bearer YOUR_HF_TOKEN",
        "Content-Type": "application/json",
    },
    json={
        "inputs": audio_b64,
        "parameters": {
            "return_all_scores": True,
            "sampling_rate": 16000
        }
    }
)

result = response.json()
print(result)
```

## Citation

If you use this model, please cite:

```bibtex
@misc{emotion-av-model,
  title={Audio Emotion Classification with Arousal-Valence Prediction},
  author={Your Name},
  year={2024},
  url={https://huggingface.co/pricklypearhealth/emotion-av-model}
}
```
