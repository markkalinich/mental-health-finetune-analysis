---
license: mit
language:
  - en
library_name: transformers
tags:
  - emoji
  - text-classification
  - sentiment
  - deberta
  - deberta-v3
  - emoji-prediction
datasets:
  - custom
base_model: microsoft/deberta-v3-small
pipeline_tag: text-classification
metrics:
  - accuracy
model-index:
  - name: bertmoji-deberta-v3-small
    results:
      - task:
          type: text-classification
          name: Emoji Prediction
        metrics:
          - type: accuracy
            value: 0.9019
            name: Validation Accuracy
          - type: accuracy
            value: 0.9761
            name: Top-3 Accuracy
---

# BertMoji: Emoji Prediction with DeBERTa-v3

BertMoji predicts the most appropriate emoji for a given text message. Built on DeBERTa-v3-small, it classifies text into 250 emoji categories with 90.2% accuracy.

## Model Description

- **Base Model:** [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small)
- **Task:** Multi-class emoji classification (250 classes)
- **Architecture:** DeBERTa-v3 encoder + classification head
- **Training:** Fine-tuned on ~23,500 synthetic text-emoji pairs. The model was refined over several fine-tuning sessions and evaluations.

## Performance

| Metric | Value |
|--------|-------|
| Validation Accuracy | **90.2%** |
| Top-3 Accuracy | **97.6%** |
| Number of Classes | 250 |

## Quick Start

```python
import torch
import torch.nn as nn
from transformers import AutoTokenizer, DebertaV2Model
import json

class BertmojiClassifier(nn.Module):
    def __init__(self, model_name, num_classes):
        super().__init__()
        self.encoder = DebertaV2Model.from_pretrained(model_name)
        hidden_size = self.encoder.config.hidden_size
        self.classifier = nn.Sequential(
            nn.Dropout(0.1),
            nn.Linear(hidden_size, hidden_size),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_size, num_classes)
        )

    def forward(self, input_ids, attention_mask):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        pooled = outputs.last_hidden_state[:, 0, :]
        return self.classifier(pooled)

# Load model
model_path = "your-username/bertmoji-deberta-v3-small"
tokenizer = AutoTokenizer.from_pretrained(model_path)

with open(f"{model_path}/emoji_mappings.json") as f:
    mappings = json.load(f)
id_to_emoji = {int(k): v for k, v in mappings['id_to_emoji'].items()}

model = BertmojiClassifier("microsoft/deberta-v3-small", len(id_to_emoji))
model.load_state_dict(torch.load(f"{model_path}/pytorch_model.bin", map_location="cpu"))
model.eval()

# Predict
def predict_emoji(text, top_k=3):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=96)
    with torch.no_grad():
        logits = model(inputs["input_ids"], inputs["attention_mask"])
        probs = torch.softmax(logits, dim=-1)
        top_probs, top_ids = probs.topk(top_k)
    return [(id_to_emoji[idx.item()], prob.item()) for idx, prob in zip(top_ids[0], top_probs[0])]

# Example
print(predict_emoji("This pizza is absolutely incredible"))
# Output: [('pizza_emoji', 0.98), ...]
```

## Demo Examples

| Message | Top-1 | Top-2 | Top-3 |
|---------|-------|-------|-------|
| "I got the promotion! All those late nights finally paid off" | 😴 25% | 😃 12% | ✈️ 10% |
| "Done with finals! Time to sleep for three days straight" | 😴 51% | ☔ 17% | ✈️ 10% |
| "My little one turns 5 today! Where did the time go" | 🎂 41% | 🐶 6% | 🐕 6% |
| "New personal record on deadlifts this morning" | 🏋️ 72% | 🎊 8% | 💼 3% |
| "You're going to crush that interview! Believe in yourself" | 💪 55% | 💅 19% | ✨ 7% |
| "This pizza is absolutely incredible" | 🍕 98% | 🍔 1% | 🍽️ 0% |
| "Look at this adorable face! My puppy is the cutest" | 🐶 80% | 🐱 9% | 🐕 3% |
| "Cheers to the weekend! We earned this" | 🥂 92% | 🍾 2% | 🎂 1% |
| "Off to Tokyo! Can't wait to explore" | ✈️ 58% | ⛰️ 16% | 🏋️ 4% |
| "What a goal! My team is on fire tonight" | 💪 61% | ✨ 8% | 💅 5% |
| "So grateful for my amazing team. Couldn't do it without you all" | 💙 44% | 💕 14% | ✊ 7% |
| "Rainy day, hot coffee, good book. Perfect Sunday" | ☔ 65% | 🚗 25% | ❄️ 2% |

## Training Details

| Parameter | Value |
|-----------|-------|
| Base Model | microsoft/deberta-v3-small |
| Hidden Size | 768 |
| Max Sequence Length | 96 |
| Batch Size | 32 |
| Learning Rate | 2e-6 |
| Optimizer | AdamW |
| Training Samples | ~23,500 |

## Limitations

- Trained on synthetic English text; may not generalize to all languages or dialects
- Some emoji categories have limited training data
- Model reflects biases present in training data generation

## License

MIT License

## Citation

```bibtex
@misc{bertmoji2024,
  title={BertMoji: Emoji Prediction with DeBERTa-v3},
  author={Mitchell Currie},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/your-username/bertmoji-deberta-v3-small}
}
```
