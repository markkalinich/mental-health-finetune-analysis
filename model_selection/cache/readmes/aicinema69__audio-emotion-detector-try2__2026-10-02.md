---
license: mit  
tags:
- audio-classification
- emotion-detection
- speech-emotion-recognition
- huggingface
- qlora
- bitsandbytes
- transformers
---

# 🎧 Audio Emotion Detector - Finetuned AST Model

This is a fine-tuned version of [`MIT/ast-finetuned-audioset-14-14-0.443`](https://huggingface.co/MIT/ast-finetuned-audioset-14-14-0.443) for **audio emotion classification** using a custom labeled dataset of voice samples tagged with 9 emotion classes. The model was trained using Hugging Face Transformers with QLoRA and 4-bit quantization (bitsandbytes) for efficient finetuning on a limited compute setup [[1]].

---

## 📝 Model Details

- **Base Model**: MIT/ast-finetuned-audioset-14-14-0.443  
- **Task**: Audio Emotion Classification  
- **Fine-tuned Model Name**: `audio-emotion-detector`  
- **Labels**:  
  - angry (0)  
  - apologetic (1)  
  - base (2)  
  - calm (3)  
  - excited (4)  
  - fear (5)  
  - happy (6)  
  - sad (7)  
  - surprise (8)  
- **Quantization**: 4-bit (nf4) via `bitsandbytes`  
- **Training Framework**: Hugging Face Transformers, Trainer API  
- **Optimization**: QLoRA with LoRA rank 64, α=16, dropout=0.1  
- **Compute**: Single GPU with mixed precision disabled (fp16=False)  

---

## 📊 Training Results (2 Epochs)

| Step | Training Loss | Validation Loss |
|:------|:---------------|:----------------|
| 25   | 2.3754         | 1.9816          |
| 200  | 0.7936         | 0.5268          |
| 375  | 0.2698         | 0.3061          |
| 450  | 0.0878         | 0.1847          |
| 550  | 0.1707         | 0.1864          |

- **Best Validation Loss**: 0.1625  
- **Metric for Model Selection**: Validation Loss (best model loaded at end)  

---

## 📂 Dataset

- **Dataset**: [Emotion TTS Dataset](https://github.com/skit-ai/emotion-tts-dataset?tab=readme-ov-file)  
- **Size**: Split 80% train / 20% validation  
- **Sampling Rate**: 16kHz  
- **Max Audio Length**: 10 seconds  
- **Classes**: 9 audio-based emotions  

---

## 🛠️ How to Use

```python
from transformers import AutoModelForAudioClassification, AutoFeatureExtractor
import torchaudio

# Load model and feature extractor
model = AutoModelForAudioClassification.from_pretrained("aicinema69/audio-emotion-detector-try2")
feature_extractor = AutoFeatureExtractor.from_pretrained("aicinema69/audio-emotion-detector-try2")

# Load audio (16kHz WAV)
audio_input, sample_rate = torchaudio.load("your_audio_file.wav")

# Preprocess audio
inputs = feature_extractor(audio_input.squeeze().numpy(), sampling_rate=16000, return_tensors="pt")

# Predict
logits = model(**inputs).logits
predicted_class = logits.argmax(-1).item()

# Label mapping
id2label = model.config.id2label
print(f"Predicted Emotion: {id2label[predicted_class]}")
'''



@misc{aicinema69_audio_emotion_detector,
  title={Audio Emotion Detector},
  author={Satyam Singh},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/aicinema69/audio-emotion-detector-try2}}
}