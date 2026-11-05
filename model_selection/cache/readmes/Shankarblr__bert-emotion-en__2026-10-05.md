---
license: mit
library_name: transformers
pipeline_tag: text-classification
base_model: google-bert/bert-base-uncased
datasets:
  - dair-ai/emotion
language:
  - en
metrics:
  - accuracy
  - f1
tags:
  - bert
  - lora
  - peft
  - emotion
  - text-classification
  - sentiment
model-index:
  - name: shankar-bert-emotion-en
    results:
      - task:
          type: text-classification
          name: Emotion classification
        dataset:
          name: dair-ai/emotion
          type: dair-ai/emotion
          split: test
        metrics:
          - type: accuracy
            value: 0.9319
            name: Accuracy
          - type: f1
            value: 0.9328
            name: Macro F1
---

# BERT emotion classifier (English)

Merged 6-class emotion classifier built on [`google-bert/bert-base-uncased`](https://huggingface.co/google-bert/bert-base-uncased).

This is the **inference repo**. Use this one with `pipeline("text-classification")`.

The PEFT adapter-only artifact (learning / resume / smaller download) lives in  
[`Shankarblr/bert-emotion-lora-adapter`](https://huggingface.co/Shankarblr/bert-emotion-lora-adapter).

## Labels

| id | label |
|---:|---|
| 0 | sadness |
| 1 | joy |
| 2 | love |
| 3 | anger |
| 4 | fear |
| 5 | surprise |

Single-label classification. `id2label` / `label2id` are in `config.json`, so the pipeline prints the label name, not `LABEL_3`.

## Use it

```python
from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="Shankarblr/shankar-bert-emotion-en",  # or your current repo id
)

print(clf("I like ML"))
print(clf("I started annoyed with laptops"))
print(clf("I am low today"))
print(clf("I am tensed if I am not going to get the job in ML"))
print(clf("I am worried with the current job market"))
```

Expected shape:

```text
[{'label': 'joy', 'score': 0.77}]
[{'label': 'anger', 'score': 0.99}]
[{'label': 'sadness', 'score': 0.995}]
[{'label': 'fear', 'score': 0.98}]
[{'label': 'fear', 'score': 0.81}]
```

Scores come from the `learning_rate=2e-4` run logged during training. Re-run inference after you replace Hub weights if your local checkpoint changed.

### Load the model directly

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo = "Shankarblr/shankar-bert-emotion-en"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo)

inputs = tok("I am low today", return_tensors="pt")
pred = model(**inputs).logits.argmax(-1).item()
print(model.config.id2label[pred])
```

## Training

| Item | Value |
|---|---|
| Base | `bert-base-uncased` |
| Method | LoRA (PEFT), then merged for this repo |
| Task | 6-class emotion (`dair-ai/emotion`) |
| Train / val / test | 11,200 / 1,600 / 3,200 |
| Trainable params | 2,683,398 / 112,170,252 (**2.39%**) |
| Epochs / steps | 4 / 1,400 |
| Device | CUDA |
| Best run LR | **2e-4** (2e-5 underfit on the same adapters) |
| Train wall time | ~4.7 min |

### Why 2e-4, not 2e-5

LoRA plus a newly initialized classification head needs a larger step than full BERT fine-tunes. Same trainable parameter count on both runs; only the step size changed.

| Run | LR | Val acc | Val F1 | Test acc | Test F1 | Avg train loss |
|---|---|---:|---:|---:|---:|---:|
| Underfit | 2e-5 | 0.725 | 0.671 | 0.717 | 0.661 | 1.139 |
| **Published** | **2e-4** | **0.941** | **0.942** | **0.932** | **0.933** | **0.344** |

Val loss on the published run: 0.152 (epoch 2) → 0.167 (epoch 3) → 0.142 (epoch 4). Small bump, then recovered. Test is within ~1 point of val.

## Intended use

- Short English utterances / social-style sentences
- Emotion tagging demos, teaching PEFT vs merged inference, baseline for a product classifier

Not intended for:

- Clinical or crisis detection
- Long documents (tokenizer max length 512; this dataset is sentence-level)
- Languages other than English
- Multi-label emotion (one label per text only)

## Limitations

- Trained on `dair-ai/emotion`. That set is clean, short, and class-imbalanced toward `joy` / `sadness`. Real chat and tickets will look different.
- `love` and `surprise` are the usual weak / confusable classes. Overall 93% can hide a weaker minority class — check per-class F1 before you ship.
- Merged weights are fp32 (~110M params, ~438 MB). For a few-MB download use the adapter repo.

## Files in this repo

| File | Role |
|---|---|
| `model.safetensors` | Full `BertForSequenceClassification` (base + trained head, LoRA merged) |
| `config.json` | Architecture + label maps |
| `tokenizer.json` / `tokenizer_config.json` | Same WordPiece tokenizer as BERT uncased |
| `training_args.bin` | Hugging Face Trainer args from the run |
| `README.md` | This card |

Do **not** upload `checkpoint-350` … `checkpoint-1400`. Those are Trainer resume snapshots (optimizer + RNG), not inference artifacts.

## Related

- Adapter-only (PEFT) repo: [`Shankarblr/bert-emotion-lora-adapter`](https://huggingface.co/Shankarblr/bert-emotion-lora-adapter)
- Dataset: [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion)
- Base: [`google-bert/bert-base-uncased`](https://huggingface.co/google-bert/bert-base-uncased)

## License

MIT. Base BERT is Apache 2.0. Dataset license follows `dair-ai/emotion`.
