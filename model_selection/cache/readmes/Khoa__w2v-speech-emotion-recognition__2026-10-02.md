---
pipeline_tag: audio-classification

language:
  - en
tags:
  - emotion-recognition
  - speech-recognition
  - wav2vec2
license: mit
---

### Wav2Vec2 Speech Emotion Recognition for English

## Model Overview
This model is fine-tuned for recognizing emotions in English speech using the Wav2Vec2 architecture. It is capable of detecting the following emotions:

- Sadness
- Anger
- Disgust
- Fear
- Happiness
- Neutral
The model was trained on the Speech Emotion Recognition dataset from Kaggle, which consists of English emotional speech samples. The dataset includes audio files labeled with various emotional states, making it ideal for training models in emotion recognition tasks.

## Model Details
- Architecture: Wav2Vec2
- Languages: English
- Dataset: Speech Emotion Recognition Dataset (Kaggle)
- Emotions Detected: Sadness, Anger, Disgust, Fear, Happiness, Neutral

## Training Results

The model achieved the following results on the test set:

**Test Accuracy**: `0.7435`

**Classification Report**:

```plaintext
              precision    recall  f1-score   support

     sadness       0.68      0.71      0.70       251
       angry       0.75      0.93      0.83       258
     disgust       0.86      0.64      0.73       250
        fear       0.75      0.61      0.67       287
       happy       0.73      0.68      0.71       231
     neutral       0.72      0.92      0.81       212

    accuracy                           0.74      1489
   macro avg       0.75      0.75      0.74      1489
weighted avg       0.75      0.74      0.74      1489
```

## How to Use
### Installation
To use this model, you need to install the transformers and torchaudio packages:

```bash
pip install transformers
pip install torchaudio
```

## Example Usage
Here is an example of how to use the model to classify emotions in an English audio file:

```bash
from transformers import pipeline

# Load the fine-tuned model and feature extractor
pipe = pipeline("audio-classification", model="Khoa/w2v-speech-emotion-recognition")

# Path to your audio file
audio_file = "path_to_your_audio_file.wav"

# Perform emotion classification
predictions = pipe(audio_file)

# Map predictions to real emotion labels
label_map = {
    "LABEL_0": "sadness",
    "LABEL_1": "angry",
    "LABEL_2": "disgust",
    "LABEL_3": "fear",
    "LABEL_4": "happy",
    "LABEL_5": "neutral"
}

# Convert predictions to readable labels
mapped_predictions = [
    {"score": pred["score"], "label": label_map[pred["label"]]} 
    for pred in predictions
]

# Display results
print(mapped_predictions)
```

## Example Output
The model outputs a list of predictions with scores for each emotion. For example:

```json
[
    {"score": 0.95, "label": "angry"},
    {"score": 0.02, "label": "happy"},
    {"score": 0.01, "label": "disgust"},
    {"score": 0.01, "label": "neutral"},
    {"score": 0.01, "label": "fear"}
]
````

## Training Details
The model was fine-tuned on the Speech Emotion Recognition Dataset, using the Wav2Vec2 architecture. The training process involved multiple epochs with a learning rate of 1e-5.

## Limitations and Biases
This model is specifically trained on English speech data and may not perform well on other languages or dialects. Additionally, as with any machine learning model, there may be biases present in the training data that could affect the model's predictions.