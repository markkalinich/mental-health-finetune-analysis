---
language: ["en"]
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - imdb
  - distilbert
pipeline_tag: text-classification
library_name: transformers
datasets:
  - imdb
model-index:
  - name: omaressamrme/tuning
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: IMDb
          type: imdb
          split: test
        metrics:
          - type: accuracy
            value: 0.31
          - type: f1
            value: 0.0
widget:
  - text: "I absolutely loved this movie!"
  - text: "This was a terrible film. I want my time back."
---


# omaressamrme/tuning

Fine-tuned DistilBERT for sentiment analysis on the IMDb dataset.

## Training setup
- Base model: distilbert-base-uncased
- Dataset: IMDb (train/test)
- Epochs: 1
- Learning rate: 2e-05
- Train batch size: 16
- Eval batch size: 32
- Max train samples: 1000
- Max eval samples: 500

## Evaluation (test split)
- Accuracy: 0.31
- F1 (binary): 0.0

## Usage
```python
from transformers import pipeline
clf = pipeline("text-classification", model="omaressamrme/tuning")
print(clf("I absolutely loved this movie!"))
```

## Hugging Face Inference API
```bash
curl -H "Authorization: Bearer $HF_TOKEN"      -H "Content-Type: application/json"      -d '{"inputs": "I absolutely loved this movie!"}'      https://api-inference.huggingface.co/models/omaressamrme/tuning
```

## Space demo
Open the Space: https://huggingface.co/spaces/omaressamrme/tuning-space

## Batch inference
You can batch texts using the pipeline:
```python
texts = ["Great film!", "Worst plot ever."]
preds = clf(texts)
```

## Model comparison
Try comparing against another sentiment model (e.g., distilbert-base-uncased-finetuned-sst-2-english) in the Space "Compare" tab.

## Intended uses & limitations
- Intended for educational/demo sentiment classification.
- Trained on a subset of IMDb for speed; performance is lower than full training.
- May reflect dataset biases; do not use for critical decisions.

## Reproducibility
See the training script in the associated GitHub repo.
