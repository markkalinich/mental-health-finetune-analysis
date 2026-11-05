---
pipeline_tag: audio-classification

language:
  - en
tags:
  - emotion-recognition
  - speech-recognition
  - wav2vec2
---

# 🎤 Wav2Vec2 Speech Emotion Recognition for English

## 🧠 Model Overview
🔹 **Model name:** `dihuzz/wav2vec2-ser-english-finetuned`  
✨ This model is fine-tuned for recognizing emotions in English speech using the Wav2Vec2 architecture. It can detect the following emotions:
- 😢 Sadness
- 😠 Anger
- 🤢 Disgust
- 😨 Fear
- 😊 Happiness
- 😐 Neutral

🔧 The model was created by fine-tuning `r-f/wav2vec-english-speech-emotion-recognition` on several prominent Speech Emotion Recognition datasets containing English emotional speech samples.

**📊 Performance Metrics:**
- 🎯 Accuracy: 92.42%
- 📉 Loss: 0.219

## 🏋️ Training Procedure

### ⚙️ Training Details
- **Base Model:** `r-f/wav2vec-english-speech-emotion-recognition`
- **💻 Hardware:** P100 GPU on Kaggle
- **⏱ Training Duration:** 10 epochs
- **📚 Learning Rate:** 5e-4
- **🧩 Batch Size:** 4
- **📈 Gradient Accumulation Steps:** 8
- **⚖️ Optimizer:** AdamW (β₁=0.9, β₂=0.999)
- **📉 Loss Function:** Cross Entropy Loss
- **⏳ Learning Rate Scheduler:** None

### 📜 Training Results
| Epoch | Loss   | Accuracy |
|-------|--------|----------|
| 1     | 1.0257 | 61.20%   |
| 2     | 0.7025 | 73.88%   |
| 3     | 0.5901 | 78.25%   |
| 4     | 0.4960 | 81.56%   |
| 5     | 0.4105 | 85.04%   |
| 6     | 0.3516 | 87.70%   |
| 7     | 0.3140 | 88.87%   |
| 8     | 0.2649 | 90.45%   |
| 9     | 0.2178 | 92.42%   |
| 10    | 0.2187 | 92.29%   |

## 🛠 How to Use
### 🔌 Installation
```bash
pip install transformers torch torchaudio
```

## 💻 Example Usage
Here is an example of how to use the model to classify emotions in a .wav format English audio file:

```python
import torch
from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2FeatureExtractor
import torchaudio  

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# Load the fine-tuned model and feature extractor
model_name = "dihuzz/wav2vec2-ser-english-finetuned"
model = Wav2Vec2ForSequenceClassification.from_pretrained(model_name).to(device)
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()

# Load and preprocess the audio file
def predict_emotion(audio_path):
    # Load audio
    waveform, sample_rate = torchaudio.load(audio_path) 
    # Alternatively, librosa can also be used to load the audio file

    # Resample if necessary
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)

    # Convert to mono if stereo
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)

    # Extract features and move them to device
    inputs = feature_extractor(
        waveform.squeeze().numpy(),
        sampling_rate=16000,
        return_tensors="pt",
        padding=True
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Perform inference (here we are using a batch size of 1 but you can increase batch size for faster inference)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=-1).item()

    # Map predicted class ID to emotion label
    label = model.config.id2label[predicted_class_id]
    return label

# Example usage
audio_file = "/path/to/your/audio.wav"
predicted_emotion = predict_emotion(audio_file)
print(f"Predicted Emotion: {predicted_emotion}")
```

## 📝 Example Output
The model returns a string representing the predicted emotion:

```json
Predicted Emotion: <emotion_label>
```

## Limitations

📌 **Note:** This model has several important limitations:
- 🌐 **Language Specificity:** English-only support
- 🗣️ **Dialect Sensitivity:** Variable performance across accents
- 🎧 **Audio Quality Needs:** Requires clean, clear recordings
- ⚖️ **Potential Biases:** May reflect cultural biases in training data
- 6️⃣ **Limited Categories:** Only detects 6 basic emotions
- 🧠 **Context Unaware:** Doesn't consider speech content meaning

