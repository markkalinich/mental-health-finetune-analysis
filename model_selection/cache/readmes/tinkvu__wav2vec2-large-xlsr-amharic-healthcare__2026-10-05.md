---
license: apache-2.0
language:
- am
base_model:
- agkphysics/wav2vec2-large-xlsr-53-amharic
- facebook/wav2vec2-large-xlsr-53
---

# wav2vec2-large-xlsr-amharic-healthcare

This model is a fine-tuned version of [`agkphysics/wav2vec2-large-xlsr-53-amharic`](https://huggingface.co/agkphysics/wav2vec2-large-xlsr-53-amharic) for **Amharic automatic speech recognition (ASR)** in the **healthcare domain**. It is trained to recognize domain-specific vocabulary commonly used in clinical or health-related audio.

## 🧠 Model Details

- **Base model**: `agkphysics/wav2vec2-large-xlsr-53-amharic`
- **Language**: Amharic (`am`)
- **Domain**: Healthcare / Medical
- **Training Data**: Domain-specific recordings

## 🛠️ Usage

```python
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import torchaudio

model = Wav2Vec2ForCTC.from_pretrained("tinkvu/wav2vec2-large-xlsr-amharic-healthcare")
processor = Wav2Vec2Processor.from_pretrained("tinkvu/wav2vec2-large-xlsr-amharic-healthcare")

# Load and preprocess audio
speech_array, sampling_rate = torchaudio.load("your_audio_file.wav")
inputs = processor(speech_array[0], sampling_rate=sampling_rate, return_tensors="pt")

# Perform inference
with torch.no_grad():
    logits = model(**inputs).logits

predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)[0]
print(transcription)