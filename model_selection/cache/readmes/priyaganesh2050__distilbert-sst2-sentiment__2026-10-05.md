---
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: distilbert/distilbert-base-uncased-finetuned-sst-2-english
language:
- en
tags:
- sentiment-analysis
- text-classification
- distilbert
- sst-2
widget:
- text: A gorgeous, witty film that earns every one of its two hours.
- text: I wanted to like it, but the plot never goes anywhere.
---

# distilbert-sst2-sentiment (mirror)

DistilBERT fine-tuned on **SST-2** for binary sentiment classification (`NEGATIVE` / `POSITIVE`).
Reports ~91% accuracy on the SST-2 dev set at roughly half the size and twice the speed of
BERT-base — the standard default for quick English sentiment work.

> [!NOTE]
> **This is a mirror.** The weights and tokenizer files here are an unmodified copy of
> [`distilbert/distilbert-base-uncased-finetuned-sst-2-english`](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english), re-hosted on this profile for reproducibility and
> convenience. All credit for the original work belongs to its authors. The upstream license
> (`apache-2.0`) is preserved and applies to this copy. If you need the canonical version, please
> use the upstream repository.

This mirror carries **only the safetensors weights and tokenizer** (~268 MB); the upstream ONNX,
TensorFlow and Rust variants were left out to keep the repo small.

## Usage

```python
from transformers import pipeline

clf = pipeline("sentiment-analysis", model="priyaganesh2050/distilbert-sst2-sentiment")
print(clf("A gorgeous, witty film that earns every one of its two hours."))
# [{'label': 'POSITIVE', 'score': 0.9998}]
```

Batched, with explicit control:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained("priyaganesh2050/distilbert-sst2-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("priyaganesh2050/distilbert-sst2-sentiment")

texts = ["Loved every minute.", "Painfully slow and predictable."]
batch = tok(texts, padding=True, truncation=True, return_tensors="pt")
with torch.no_grad():
    probs = model(**batch).logits.softmax(-1)

for t, p in zip(texts, probs):
    print(f"{t:35s} -> {model.config.id2label[int(p.argmax())]} ({p.max():.3f})")
```

Pairs directly with [`priyaganesh2050/rotten-tomatoes-sentiment`](https://huggingface.co/datasets/priyaganesh2050/rotten-tomatoes-sentiment)
for zero-shot evaluation, since both use the same movie-review, binary-sentiment setup.

## Limitations

- **Binary only** — there is no neutral class. Neutral or mixed text is forced to one side, usually
  with a confident-looking score. Do not read the softmax as calibrated confidence.
- **Domain** — trained on movie-review sentences. Accuracy drops on tweets, support tickets,
  clinical or financial text.
- **Bias** — the upstream card documents biased associations (for example, sentiment shifting with
  the country named in an otherwise neutral sentence). Audit before any consequential use.
- Sentence-length input works best; long documents should be split and aggregated.
