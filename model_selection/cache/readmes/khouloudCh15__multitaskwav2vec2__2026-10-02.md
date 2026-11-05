---
language: en
tags:
- audio
- speech
- emotion-recognition
- wav2vec2
datasets:
- TESS
- CREMA-D
- SAVEE
- RAVDESS
license: mit
metrics:
- accuracy
- f1
---

# wav2vec2-emotion-recognition

This model is fine-tuned on the Wav2Vec2 architecture for speech emotion recognition. It can classify speech into 8 different emotions with corresponding confidence scores.

## Model Description

- **Model Architecture:** Wav2Vec2 with sequence classification head
- **Language:** English
- **Task:** Speech Emotion Recognition
- **Fine-tuned from:** facebook/wav2vec2-base
- **Datasets:** Combined emotion datasets
 - [TESS](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess)
 - [CREMA-D](https://www.kaggle.com/datasets/ejlok1/cremad)
 - [SAVEE](https://www.kaggle.com/datasets/barelydedicated/savee-database)
 - [RAVDESS](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

## Performance Metrics
- **Accuracy:** 79.57%
- **F1 Score:** 79.43%

## Supported Emotions
- 😠 Angry
- 😌 Calm
- 🤢 Disgust
- 😨 Fearful
- 😊 Happy
- 😐 Neutral
- 😢 Sad
- 😲 Surprised

## Training Details

The model was trained with the following configuration:
- **Epochs:** 15
- **Batch Size:** 16
- **Learning Rate:** 5e-5
- **Optimizer:** AdamW
- **Weight Decay:** 0.03
- **Gradient Accumulation Steps:** 2
- **Mixed Precision:** fp16

For detailed training process, check out the [Fine-tuning Notebook](https://colab.research.google.com/drive/1VNhIjY7gW29d0uKGNDGN0eOp-pxr_pFL?usp=drive_link)

## Limitations

### Audio Requirements:

- Sampling rate: 16kHz (will be automatically resampled)
- Maximum duration: 1 minute
- Clear speech with minimal background noise recommended

### Performance Considerations:

- Best results with clear speech audio
- Performance may vary with different accents
- Background noise can affect accuracy


## Demo
https://huggingface.co/spaces/Dpngtm/Audio-Emotion-Recognition

## Contact
* **GitHub**: [DGautam11](https://github.com/DGautam11)
* **LinkedIn**: [Deepan Gautam](https://www.linkedin.com/in/deepan-gautam)  
* **Hugging Face**: [@Dpngtm](https://huggingface.co/Dpngtm)

For issues and questions, feel free to:
1. Open an issue on the [Model Repository](https://huggingface.co/Dpngtm/wav2vec2-emotion-recognition)
2. Comment on the [Demo Space](https://huggingface.co/spaces/Dpngtm/Audio-Emotion-Recognition)

## Usage

```python
from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2Processor
import torch
import torchaudio

# Load model and processor
model = Wav2Vec2ForSequenceClassification.from_pretrained("Dpngtm/wav2vec2-emotion-recognition")
processor = Wav2Vec2Processor.from_pretrained("Dpngtm/wav2vec2-emotion-recognition")

# Load and preprocess audio
speech_array, sampling_rate = torchaudio.load("path_to_audio.wav")
if sampling_rate != 16000:
   resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16000)
   speech_array = resampler(speech_array)

# Convert to mono if stereo
if speech_array.shape[0] > 1:
   speech_array = torch.mean(speech_array, dim=0, keepdim=True)

speech_array = speech_array.squeeze().numpy()

# Process through model
inputs = processor(speech_array, sampling_rate=16000, return_tensors="pt", padding=True)
with torch.no_grad():
   outputs = model(**inputs)
   predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Get predicted emotion
emotion_labels = ["angry", "calm", "disgust", "fearful", "happy", "neutral", "sad", "surprised"]
predicted_emotion = emotion_labels[predictions.argmax().item()]