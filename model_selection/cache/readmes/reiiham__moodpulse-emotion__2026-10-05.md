---
language: en
license: apache-2.0
tags:
  - text-classification
  - emotion-detection
  - music-mood
  - distilbert
  - fine-tuned
datasets:
  - go_emotions
metrics:
  - accuracy
  - f1
model-index:
  - name: moodpulse-emotion
    results:
      - task:
          type: text-classification
        dataset:
          name: go_emotions
          type: go_emotions
        metrics:
          - type: accuracy
            value: 0.7584
          - type: f1
            value: 0.7566
---

# 🎵 MoodPulse Emotion Classifier

Fine-tuned `distilbert-base-uncased` on [GoEmotions](https://huggingface.co/datasets/go_emotions) 
for music mood prediction. Part of the **MoodPulse** project — an app that analyzes your 
Spotify top tracks and predicts your current emotional state.

## Labels

| ID | Label | Emoji |
|----|-------|-------|
| 0  | joy      | 😄 |
| 1  | sadness  | 😢 |
| 2  | anger    | 😠 |
| 3  | fear     | 😨 |
| 4  | love     | 💖 |
| 5  | surprise | 😲 |

## Performance

| Metric | Score |
|--------|-------|
| Accuracy | 75.84% |
| F1 (weighted) | 0.7566 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Reiiham/moodpulse-emotion",
    return_all_scores=True
)

result = classifier("I feel so alive, dancing under the stars!")
# Returns scores for all 6 emotions
```

## Training details

- **Base model:** distilbert-base-uncased
- **Dataset:** GoEmotions (simplified, 27 labels collapsed to 6)
- **Epochs:** 4 (early stopping)
- **Batch size:** 32
- **Learning rate:** 2e-5 with cosine scheduler
- **Hardware:** Google Colab T4 GPU

## About MoodPulse

MoodPulse connects to your Spotify account, fetches your top 5 tracks of the week,
analyzes the lyrics using this model + Spotify audio features (valence, energy, danceability),
and predicts your current emotional mood with a clean data visualization.

Built by [Reiiham](https://github.com/Reiiham)
