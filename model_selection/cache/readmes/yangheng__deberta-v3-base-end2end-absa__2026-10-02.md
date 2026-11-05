---
language:
- en
- zh
tags:
- token-classification
- aspect-based-sentiment-analysis
- sentiment-analysis
- sequence-labeling
- transformers
- deberta
license: mit
pipeline_tag: token-classification
widget:
- text: The user interface is brilliant, but the documentation is a total mess.
- text: 这家餐厅的牛排很好吃，但是服务很慢。
---

# Multilingual End-to-End Aspect-based Sentiment Analysis

This model performs end-to-end Aspect-Based Sentiment Analysis (ABSA) by jointly extracting aspect terms and their sentiments via a single token-classification head. Labels are merged as IOB-with-sentiment, e.g. `B-ASP-Positive`, `I-ASP-Negative`, or `O` for non-aspect tokens.

## What it does
- Detects aspect terms as spans in text
- Assigns a sentiment for each detected aspect (Positive/Negative/Neutral)
- Returns character-level offsets (`start`, `end`) in the original input

## How to use (Transformers pipeline)

```python
from transformers import pipeline

nlp = pipeline(
    "token-classification",
    model="yangheng/deberta-v3-base-end2end-absa",  # replace with your repo id
    aggregation_strategy="simple",  # aggregates sub-tokens into word-level entities
)

text = "The user interface is brilliant, but the documentation is a total mess."
preds = nlp(text)
print(preds)
# Example entity structure:
# [{
#   'entity_group': 'B-ASP-Positive',
#   'word': 'user interface',
#   'start': 4,
#   'end': 19,
#   'score': 0.98
# }, {
#   'entity_group': 'B-ASP-Negative',
#   'word': 'documentation',
#   'start': 41,
#   'end': 54,
#   'score': 0.99
# }]
```

### Convert entities to aspect-level results
```python
def postprocess_entities(entities):
    aspects = []
    for ent in entities:
        label = ent["entity_group"]  # e.g. B-ASP-Positive or I-ASP-Positive
        parts = label.split("-")
        # Expected formats: O, B-ASP-<SENT>, I-ASP-<SENT>
        if label == "O":
            continue
        prefix, _, sentiment = parts[0], parts[1], parts[2]
        aspects.append({
            "aspect": ent["word"],
            "sentiment": sentiment,
            "start": int(ent["start"]),
            "end": int(ent["end"]),
            "score": float(ent.get("score", 0.0)),
        })
    return aspects

aspects = postprocess_entities(preds)
print(aspects)
```

## Enhanced Sentiment classification
The aspect sentiment analysis performance can be improved by the joint aspect term extraction and aspect sentiment classification. 
Find the example [here](https://huggingface.co/yangheng/deberta-v3-base-absa-v1.1/blob/main/end2end_absa.py)

## FastAPI serving (optional)

You can deploy a simple REST service using FastAPI:

```bash

python serve_singlehead_api.py --model yangheng/deberta-v3-base-end2end-absa --host 0.0.0.0 --port 8000
```

Predict:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"The user interface is brilliant, but the documentation is a total mess."}'
```

Notes:
- `start`/`end` are character offsets in the original string.
- `aggregation_strategy='simple'` merges sub-tokens into word-level spans. Set to `none|first|average|max` as needed.

## Model details
- Base model: `microsoft/deberta-v3-base`
- Task: Token classification with merged labels: `O`, `B-ASP-{Positive|Negative|Neutral}`, `I-ASP-{Positive|Negative|Neutral}`
- Training: Fine-tuned with Hugging Face Transformers. The model config includes `id2label/label2id` for native pipeline compatibility and Hub Inference API.

## Limitations
- Long texts are truncated to the maximum sequence length of the model (typically 512). Adjust during training/inference if required.
- Sentiments limited to Positive/Negative/Neutral unless retrained with extended schema.

## License
MIT


