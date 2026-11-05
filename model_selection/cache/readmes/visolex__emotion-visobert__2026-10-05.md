---
license: apache-2.0
base_model: uitnlp/visobert
tags:
- vietnamese
- emotion-recognition
- text-classification
- VSMEC
datasets:
- visolex/VSMEC
metrics:
- accuracy
- macro-f1
model-index:
- name: emotion-visobert
  results:
  - task:
      type: text-classification
      name: Emotion Recognition
    dataset:
      name: VSMEC
      type: VSMEC
    metrics:
      - type: accuracy
        value: 0.0
      - type: macro-f1
        value: 0.0
---

# emotion-visobert: Emotion Recognition for Vietnamese Text

This model is a fine-tuned version of [uitnlp/visobert](https://huggingface.co/uitnlp/visobert) on the **VSMEC** dataset for emotion recognition in Vietnamese text.

## Model Details

* **Base Model**: uitnlp/visobert
* **Description**: ViSoBERT - Vietnamese SentenceBERT
* **Dataset**: VSMEC (Vietnamese Social Media Emotion Corpus)
* **Fine-tuning Framework**: HuggingFace Transformers
* **Task**: Emotion Classification (7 classes)

### Hyperparameters

* Batch size: `32`
* Learning rate: `2e-5`
* Epochs: `100`
* Max sequence length: `256`
* Weight decay: `0.01`
* Warmup steps: `500`

## Dataset

The model was trained on the **VSMEC** dataset, which contains 6,927 Vietnamese social media text samples annotated with emotion labels. The dataset includes the following emotion categories:

* **Enjoyment** (0): Positive emotions, joy, happiness
* **Sadness** (1): Sad, disappointed, gloomy feelings
* **Anger** (2): Angry, frustrated, irritated
* **Fear** (3): Scared, anxious, worried
* **Disgust** (4): Disgusted, repelled
* **Surprise** (5): Surprised, shocked, amazed
* **Other** (6): Neutral or unclassified emotions

## Results

The model was evaluated using the following metrics:

* **Accuracy**: `0.0000`
* **Macro-F1**: `0.0000`
* **Macro-Precision**: `0.0000`
* **Macro-Recall**: `0.0000`

## Usage

You can use this model for emotion recognition in Vietnamese text. Below is an example of how to use it with the HuggingFace Transformers library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("visolex/emotion-visobert")
model = AutoModelForSequenceClassification.from_pretrained("visolex/emotion-visobert")

# Example text
text = "Tôi rất vui vì hôm nay trời đẹp!"

# Tokenize
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)

# Predict
outputs = model(**inputs)
predicted_class = outputs.logits.argmax(dim=-1).item()

# Map to emotion name
emotion_map = {
    0: "Enjoyment",
    1: "Sadness",
    2: "Anger",
    3: "Fear",
    4: "Disgust",
    5: "Surprise",
    6: "Other"
}

predicted_emotion = emotion_map[predicted_class]
print(f"Text: {text}")
print(f"Predicted emotion: {predicted_emotion}")
```

## License

This model is released under the Apache-2.0 license.

## Acknowledgments

* Base model: [uitnlp/visobert](https://huggingface.co/uitnlp/visobert)
* Dataset: VSMEC (Vietnamese Social Media Emotion Corpus)
* ViSoLex Toolkit
