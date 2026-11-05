---
library_name: transformers
tags:
- emotion-detection
- audio-emotion-detection
base_model:
- MIT/ast-finetuned-audioset-14-14-0.443
pipeline_tag: audio-classification
---

## 📊 Model Performance

| Metric     | Score     |
|------------|-----------|
| Accuracy   | 0.38      |
| Precision  | 0.3075    |
| Recall     | 0.38      |
| F1-Score   | 0.2871    |

> **Note**: This model is a first iteration and may benefit from further fine-tuning and data augmentation.

---

## 🗂️ Emotion Classes

The model classifies audio samples into the following 9 emotions:

```
0 - angry
1 - apologetic
2 - base
3 - calm
4 - excited
5 - fear
6 - happy
7 - sad
8 - surprise
```

---

## 🏋️‍♂️ Training Details

- **Dataset**: Custom dataset with `audio_path` and `emotion` columns.
- **Sampling Rate**: Resampled to 16kHz
- **Max Audio Length**: 10 seconds
- **Training Epochs**: 2
- **Training/Validation Split**: 80/20
- **Optimization**: AdamW
- **Precision**: Full (fp32)

---

## 🧪 Training Logs (Loss)

| Step | Training Loss | Validation Loss |
|------|----------------|------------------|
| 0    | 2.23          | 1.91             |
| 350  | 0.88          | 0.86             |
| 525  | 0.98          | 0.53             |
| 750  | 0.22          | 0.35             |
| 1125 | 0.25          | 0.30             |

> Full logs available in training script output.

---

## 🚀 Usage

```python
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
import torchaudio

model = AutoModelForAudioClassification.from_pretrained("aicinema69/audio-emotion-detector-v1.0")
feature_extractor = AutoFeatureExtractor.from_pretrained("aicinema69/audio-emotion-detector-v1.0")

# Load your audio (16kHz recommended)
waveform, sample_rate = torchaudio.load("your_audio.wav")

# Preprocess
inputs = feature_extractor(waveform.squeeze().numpy(), sampling_rate=sample_rate, return_tensors="pt", padding=True)

# Predict
with torch.no_grad():
    logits = model(**inputs).logits
    predicted_class = logits.argmax(-1).item()

print("Predicted emotion:", model.config.id2label[predicted_class])
```

---

## 🛠️ Model Card Notes

- You **should fine-tune this model on your downstream task** for better performance.
- Feature extractor is stored in `trainer.tokenizer` (note: `tokenizer` is deprecated in future 🤗 releases, use `processing_class`).
- Model and extractor pushed to Hub using `push_to_hub`.

---

## 📦 Deployment

After training:
```python
model.push_to_hub("aicinema69/audio-emotion-detector-v1.0")
feature_extractor.push_to_hub("aicinema69/audio-emotion-detector-v1.0")
```

---

## ✍️ Author

Satyam Singh  
GitHub: [SatyamSingh8306](https://github.com/SatyamSingh8306)  
Hugging Face: [aicinema69](https://huggingface.co/aicinema69)

---
