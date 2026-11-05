---
language: en
license: apache-2.0
library_name: transformers
tags:
- emotions
- text-classification
- embeddings
- bert
- goemotions
- safetensors
pipeline_tag: text-classification
base_model: google-bert/bert-base-uncased
---

# EmotiSpace-128

EmotiSpace-128 is a BERT-based hybrid emotion model that maps text into a 128-dimensional emotional embedding space and also predicts GoEmotions-style emotion labels.

It is not only a classifier. The main goal is to produce a reusable emotional latent space where similar emotional meanings are close together, while still exposing readable emotion probabilities.

## What it does

Input:

```text
I feel devastated.
```

Output:

* a normalized 128D emotion embedding
* raw logits
* sigmoid probabilities for emotion labels

Example labels:

```text
sadness
remorse
disappointment
grief
gratitude
```

## Architecture

```text
bert-base-uncased
-> pooled BERT output
-> projection head: 768 -> 256 -> 128
-> normalized 128D EmotiSpace embedding
-> classifier head
-> emotion probabilities
```

The model uses a custom Transformers architecture:

```text
model_type: bert_emotispace
```

Load it with `trust_remote_code=True`.

## Training

The model was trained in two passes.

Pass 1 focused on emotion classification using GoEmotions labels.

Pass 2 continued training with a combined objective:

```text
loss = classification_loss + 0.05 * embedding_geometry_loss
```

The second pass was used to make the 128D embedding space more useful for cosine similarity and custom emotion anchors.

Training used the last 4 BERT layers unfrozen, with early stopping.

## Intended use

EmotiSpace-128 is useful for:

* emotion classification
* emotion embeddings
* emotional similarity search
* custom emotion anchors beyond fixed labels
* character mood systems
* dialogue tone control
* TTS/prosody control pipelines
* conversation mood tracking

It can be used in two modes:

### Easy mode

Use the emotion probabilities as a normal classifier.

### Advanced mode

Use the 128D embedding directly and compare it against custom emotion anchors.

For example, you can define anchors such as:

```text
nostalgia
warmth
calm
playfulness
emotional flatness
bittersweetness
```

without retraining the model.

## Usage

```py
import torch
from transformers import AutoModel, AutoTokenizer

model_id = "lunahr/emotispace-128"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(
    model_id,
    trust_remote_code=True,
)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

@torch.no_grad()
def analyze(texts, top_k=5):
    if isinstance(texts, str):
        texts = [texts]
    tokens = tokenizer(
        texts,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=128,
    ).to(device)
    out = model(**tokens)
    embeddings = out["embeddings"].cpu()
    probs = out["probs"].cpu()
    results = []
    for i, text in enumerate(texts):
        top = torch.topk(probs[i], k=top_k)
        results.append({
            "text": text,
            "embedding": embeddings[i],
            "labels": [
                {
                    "label": model.config.label_names[idx.item()],
                    "score": score.item(),
                }
                for score, idx in zip(top.values, top.indices)
            ],
        })
    return results

for item in analyze([
    "I feel devastated.",
    "This is amazing, I am so happy!",
]):
    print(item["text"])
    print(item["embedding"].shape)
    print(item["labels"])
    print()
```

## Example behavior

Example output:

```py
I feel devastated.
embedding shape: torch.Size([128])
sadness, remorse, disappointment, grief
This is amazing, I am so happy!
embedding shape: torch.Size([128])
joy, excitement, admiration, love
```

The embedding space can also separate emotional and non-emotional text. For example, emotionally charged text can be far away from factual neutral sentences like:

```text
The table is made of wood.
```

## Notes on embeddings

The 128D embedding is normalized and can be compared with cosine similarity.

Example use:

```text
similarity = embedding_a @ embedding_b.T
```

The embedding space is designed to support emotional similarity, not just exact label matching.

For example:

```text
"I feel devastated."
```

should be close to:

```text
"I am so sad I could cry."
```

and far from:

```text
"This is amazing, I am so happy!"
```

## Limitations

This model is trained from English text and should be treated as English-first.

It is based on GoEmotions-style labels, so the classifier output is limited to that label space. The embedding space is more flexible, but custom emotion anchors should still be tested carefully.

The model does not actually “feel” emotions. It estimates emotional meaning from text.

Embeddings are useful for similarity and downstream control, but they are not a psychological diagnosis or a reliable mental health assessment tool.

## Suggested downstream design

A recommended pattern is:

```text
recent messages
-> EmotiSpace embeddings
-> weighted rolling mood embedding
-> compare against persona-agnostic emotion anchors
-> map to character response style or TTS controls
```

Keep emotion anchors persona-agnostic. Define what the emotion means generally, not how a specific character expresses it.

Good anchor style:

```text
A calm emotional state with low tension, steady energy, and no urgency.
```

Avoid persona-specific anchors like:

```text
Luna feels calm and wants to comfort you.
```

This prevents one character’s style from leaking into unrelated characters.

## Citation

This model is based on BERT and trained using GoEmotions-style emotion supervision.

If you use this model, please credit:

```text
lunahr/emotispace-128
```
