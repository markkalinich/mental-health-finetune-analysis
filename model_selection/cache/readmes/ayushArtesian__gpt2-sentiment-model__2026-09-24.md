---
language:
- en
license: mit
tags:
- text-classification
- sentiment-analysis
- gpt2
- twitter
- nlp
datasets:
- mteb/tweet_sentiment_extraction
metrics:
- accuracy
base_model: gpt2
pipeline_tag: text-classification
---

# GPT-2 Sentiment Analysis Model

A fine-tuned **GPT-2** model for **3-class sentiment classification** (negative / neutral / positive), trained on the [Tweet Sentiment Extraction](https://huggingface.co/datasets/mteb/tweet_sentiment_extraction) dataset.

---

## Model Details

| Property | Details |
|---|---|
| **Base Model** | `gpt2` (117M parameters) |
| **Task** | Text Classification (Sentiment Analysis) |
| **Labels** | `0 → negative`, `1 → neutral`, `2 → positive` |
| **Dataset** | `mteb/tweet_sentiment_extraction` |
| **Training Samples** | 1,000 (shuffled subset, seed=42) |
| **Eval Samples** | 1,000 (shuffled subset, seed=42) |
| **Max Token Length** | 512 |
| **Checkpoint** | `test_trainer/checkpoint-375` |

---

## Training Details

### Hyperparameters

| Parameter | Value |
|---|---|
| Epochs | 3 |
| Train Batch Size | 8 |
| Eval Batch Size | 8 |
| Gradient Accumulation Steps | 1 |
| Precision | FP16 (mixed precision) |
| Logging Steps | 10 |
| Optimizer | AdamW (default Trainer) |

### Training Infrastructure

- **Hardware:** GPU (CUDA)
- **Framework:** HuggingFace `transformers` + `Trainer` API
- **Libraries:** `transformers`, `datasets`, `evaluate`, `torch`, `accelerate`

### Key Implementation Notes

- `pad_token` is set to `eos_token` (GPT-2 has no native pad token)
- `model.config.pad_token_id` is explicitly set to avoid generation warnings
- `DataCollatorWithPadding` is used for dynamic padding during training
- Token embeddings are resized after loading the classification head

---

## Usage

### Install Dependencies

```bash
pip install transformers torch
```

### Quick Start — Inference

```python
import torch
from transformers import GPT2ForSequenceClassification, GPT2Tokenizer

model_name = "ayushArtesian/gpt2-sentiment-model"

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2ForSequenceClassification.from_pretrained(model_name)

# Required — GPT-2 has no native pad token
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.pad_token_id

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

label_map = {0: "negative", 1: "neutral", 2: "positive"}

def predict_sentiment(text: str) -> str:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    predicted_class = torch.argmax(outputs.logits, dim=1).item()
    return label_map[predicted_class]

# Example
print(predict_sentiment("I hope your day is as pleasant as you are"))
# → positive

print(predict_sentiment("This is the worst experience I've ever had"))
# → negative
```

### Using HuggingFace Pipeline

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="ayushArtesian/gpt2-sentiment-model"
)

result = classifier("I absolutely love this!")
print(result)
# → [{'label': 'LABEL_2', 'score': 0.91}]  (LABEL_2 = positive)
```

---

## Dataset

The model was trained on the **[mteb/tweet_sentiment_extraction](https://huggingface.co/datasets/mteb/tweet_sentiment_extraction)** dataset, which contains tweets labelled with three sentiment classes:

| Label | Meaning |
|---|---|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

Only a 1,000-sample subset of the training and test splits was used for this experiment.

---

## Limitations & Intended Use

- **Domain:** Primarily optimized for short, informal social media text (tweets). Performance may degrade on longer or more formal text.
- **Training size:** Fine-tuned on a small 1,000-sample subset — results may vary compared to full-dataset training.
- **Language:** English only.
- **Not recommended for:** High-stakes decisions (medical, legal, financial), multilingual sentiment, or formal document analysis.

---

## Citation

If you use this model, please consider citing the original GPT-2 paper:

```bibtex
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  year={2019}
}
```

---

## Author

**ayushArtesian** — [HuggingFace Profile](https://huggingface.co/ayushArtesian)