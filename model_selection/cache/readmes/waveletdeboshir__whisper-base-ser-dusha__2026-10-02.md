---
language:
- ru
base_model:
- openai/whisper-base
pipeline_tag: audio-classification
library_name: transformers
tags:
- SER
- speech
- emotion
model-index:
- name: Whisper-base for Speech Emotion Recognition in Russian
  results:
  - task:
      name: Audio Classification
      type: speech-emotion-recognition
    dataset:
      name: Sberdevices Dusha (crowd)
      type: SberDevices/Dusha
      args: ru
    metrics:
    - name: Test Weighted Accuracy
      type: acc
      value: 0.8364
    - name: Test F1 macro
      type: f1
      value: 0.8429
    - name: Test Recall macro
      type: recall
      value: 0.83
    - name: Test Precision macro
      type: precision
      value: 0.85
metrics:
- f1
---
# Whisper-base for Speech Emotion Recognition in Russian on Dusha dataset
Whisper-base encoder with classification head for speech emotion recognition.

**Dusha dataset**: https://github.com/salute-developers/golos/tree/master/dusha

**Multiclass classification into 5 classes:**
* angry 0
* sad 1
* neutral 2
* positive 3
* other 4

Model was fine-tuned on full Dusha-crowd with
* augmentations Time Shift, Time Masking and Colored Noise;
* WeightedRandomSampler.

## Usage
```python
import torch
import torchaudio
from transformers import WhisperForAudioClassification, WhisperFeatureExtractor

# load model and feature extractor
model = WhisperForAudioClassification.from_pretrained("waveletdeboshir/whisper-base-ser-dusha")
model.eval()
feature_extractor = WhisperFeatureExtractor.from_pretrained("waveletdeboshir/whisper-base-ser-dusha")

# load audio and resample if necessary
wav, sr = torchaudio.load("audio.wav")
if sr != 16000:
    wav = torchaudio.functional.resample(wav, sr, 16000)

# compute predictions
features = feature_extractor(wav[0], sampling_rate=16000, return_tensors="pt").input_features
with torch.no_grad():
    preds = model(features)

# get emotion and its probability
probs = torch.nn.functional.softmax(preds.logits, dim=-1)
print(f"Predicted emotion: {model.config.id2label[probs.argmax().item()]} with probability {probs.max().item():.4f}")
```