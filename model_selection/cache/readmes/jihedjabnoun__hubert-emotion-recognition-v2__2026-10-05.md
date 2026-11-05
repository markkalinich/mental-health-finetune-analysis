---
language: en
license: mit
tags:
- audio
- speech-emotion-recognition
- hubert
- emotion-classification
- pytorch
datasets:
- MELD
- CREMA-D  
- TESS
- RAVDESS
- SAVEE
metrics:
- accuracy
- f1
base_model: facebook/hubert-base-ls960
---

# 🎭 Speech Emotion Recognition - HuBERT

Fine-tuned HuBERT model for 7-class speech emotion recognition achieving **71.8% accuracy**.

## 📊 Model Performance
- **Overall Accuracy**: 0.7178 (71.8%)
- **Training Samples**: 12,285
- **Validation Samples**: 3,072
- **Base Model**: facebook/hubert-base-ls960
- **Parameters**: ~95M (all trainable)

## 🎯 Emotions Detected
The model can classify audio into 7 emotional categories:
- **Anger** (F1: 0.80) - High performance
- **Disgust** (F1: 0.68) - Good performance  
- **Fear** (F1: 0.71) - Good performance
- **Happiness** (F1: 0.69) - Good performance
- **Neutral** (F1: 0.80) - High performance
- **Sadness** (F1: 0.64) - Moderate performance
- **Surprise** (F1: 0.70) - Good performance

## 🚀 Quick Usage

```python
from transformers import Wav2Vec2FeatureExtractor, Wav2Vec2ForSequenceClassification
import librosa
import torch
import numpy as np

# Load model and feature extractor
model = Wav2Vec2ForSequenceClassification.from_pretrained("jihedjabnoun/hubert-emotion-recognition-v2")
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("jihedjabnoun/hubert-emotion-recognition-v2")

# Load and process audio (16kHz sample rate)
audio, sr = librosa.load("your_audio.wav", sr=16000)

# Preprocess audio
inputs = feature_extractor(
    audio, 
    sampling_rate=16000, 
    return_tensors="pt", 
    padding=True
)

# Predict emotion
with torch.no_grad():
    logits = model(**inputs).logits
    predicted_id = torch.argmax(logits, dim=-1).item()
    
# Get prediction confidence
probabilities = torch.softmax(logits, dim=-1)[0]
confidence = probabilities[predicted_id].item()

# Emotion labels
emotions = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']

print(f"Predicted Emotion: {emotions[predicted_id]}")
print(f"Confidence: {confidence:.3f}")

# Get all emotion probabilities
for i, emotion in enumerate(emotions):
    prob = probabilities[i].item()
    print(f"{emotion}: {prob:.3f}")
```

## 📈 Model Architecture
- **Base Model**: HuBERT (Hidden Unit BERT) - facebook/hubert-base-ls960
- **Architecture**: Transformer-based speech representation learning
- **Classification Head**: Linear layer with 7 output classes
- **Input**: Raw audio waveform (16kHz)
- **Output**: Emotion classification logits

## 🎵 Audio Requirements
- **Sample Rate**: 16kHz (automatically resampled if different)
- **Duration**: Optimal 2-10 seconds (longer audio will be truncated)
- **Format**: Any format supported by librosa (WAV, MP3, FLAC, etc.)
- **Quality**: Clear speech with minimal background noise for best results

## 📊 Training Details
- **Training Epochs**: 4
- **Batch Size**: 6 (optimized for GPU memory)
- **Learning Rate**: 2e-5 with cosine scheduling
- **Optimizer**: AdamW with weight decay (0.01)
- **Precision**: Mixed precision (FP16) for efficiency
- **Hardware**: NVIDIA GPU (15.8GB VRAM)
- **Training Time**: ~70 minutes

## 🔍 Per-Class Performance
| Emotion   | Precision | Recall | F1-Score | Support |
|-----------|-----------|--------|----------|---------|
| Anger     | 0.776     | 0.828  | 0.801    | 443     |
| Disgust   | 0.747     | 0.620  | 0.677    | 442     |
| Fear      | 0.758     | 0.673  | 0.713    | 443     |
| Happiness | 0.777     | 0.614  | 0.686    | 443     |
| Neutral   | 0.761     | 0.838  | 0.797    | 437     |
| Sadness   | 0.667     | 0.614  | 0.639    | 443     |
| Surprise  | 0.593     | 0.846  | 0.697    | 421     |

**Best performing emotions**: Anger, Neutral, Surprise  
**Most challenging emotions**: Sadness, Happiness

## 🗃️ Training Datasets
The model was trained on a diverse collection of emotional speech datasets:
- **MELD** - Multimodal EmotionLines Dataset
- **CREMA-D** - Crowdsourced Emotional Multimodal Actors Dataset  
- **TESS** - Toronto Emotional Speech Set
- **RAVDESS** - Ryerson Audio-Visual Database of Emotional Speech
- **SAVEE** - Surrey Audio-Visual Expressed Emotion Database

Total: **12,285** training samples, **3,072** validation samples

## ⚡ Performance Tips
1. **Audio Quality**: Use clear recordings with minimal background noise
2. **Duration**: 2-10 second clips work best
3. **Sample Rate**: Model expects 16kHz (will auto-resample)
4. **Language**: Optimized for English speech
5. **Context**: Works best with natural emotional expressions

## 🔧 Technical Specifications
- **Model Size**: ~378MB
- **Inference Speed**: Real-time capable on modern hardware
- **Memory Usage**: ~2GB GPU memory for inference
- **Framework**: PyTorch + Transformers
- **Compatibility**: Python 3.7+, transformers 4.0+

## 🚫 Limitations
- Trained primarily on English speech
- Performance may vary with accents or non-native speakers
- Background noise can affect accuracy
- Very short (<1s) or very long (>15s) audio may have reduced performance
- Cultural expressions of emotion may not be fully captured

## 📚 Citation
If you use this model in your research, please cite:

```bibtex
@misc{hubert-emotion-recognition-2025,
  title={Speech Emotion Recognition with Fine-tuned HuBERT},
  author={Jihed Jabnoun},
  year={2025},
  url={https://huggingface.co/jihedjabnoun/hubert-emotion-recognition-v2},
  note={Fine-tuned HuBERT model for 7-class emotion recognition}
}
```

## 🤝 Contact & Support
- **Model Repository**: [jihedjabnoun/hubert-emotion-recognition-v2](https://huggingface.co/jihedjabnoun/hubert-emotion-recognition-v2)
- **Issues**: Please report bugs or issues in the model repository
- **Improvements**: Suggestions for model improvements are welcome
- **Mail**: jihed.jabnoun@fsm.u-monastir.tn

## 📜 License
This model is released under the MIT License. The base HuBERT model follows its original license terms.

---
*Last updated: June 2025*