---
language:
- knc
library_name: transformers
pipeline_tag: text-classification
license: cc-by-nc-4.0
base_model: facebook/nllb-200-distilled-600M
tags:
- sentiment-analysis
- kanuri
- nllb
- custom_code
metrics:
- accuracy
- f1
model-index:
- name: nllb-kanuri-sentiment-analysis
  results:
  - task:
      type: text-classification
      name: Sentiment analysis
    dataset:
      name: Kanuri polarity lexicon (held-out test split)
      type: kanuri-polarity-lexicon
    metrics:
    - type: accuracy
      value: 0.6895
    - type: f1
      name: Macro-F1
      value: 0.6823
---

# Kanuri Sentiment Analysis (NLLB encoder)

Classifies short Central Kanuri (Latin script) text as **negative**, **neutral** or **positive**.

The model is the encoder of [`facebook/nllb-200-distilled-600M`](https://huggingface.co/facebook/nllb-200-distilled-600M) with masked mean pooling and a linear classification head. The decoder is not used, so the checkpoint is small (about 0.8 GB in fp16).

## How to use

The model uses custom code, so `trust_remote_code=True` is required.

```python
import re, unicodedata
from transformers import pipeline

def norm_kanuri(t):
    # same cleaning as in training: the model expects lowercase, NFC-normalised text
    t = unicodedata.normalize("NFC", str(t)).lower().replace("\u2019", "'").replace("`", "'")
    t = re.sub(r"(?<=[a-z\u0259'])3|3(?=[a-z\u0259'])", "\u0259", t)
    t = re.sub(r"[^\w' \-]", " ", t)
    return re.sub(r"\s+", " ", t).strip(" -")

clf = pipeline("text-classification", model="IsahMBukar/nllb-kanuri-sentiment-analysis", trust_remote_code=True)
print(clf([norm_kanuri(x) for x in ["nasara bo", "kam girta", "fuye"]]))
```

Without the pipeline:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo = "IsahMBukar/nllb-kanuri-sentiment-analysis"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo, trust_remote_code=True).eval()

batch = tok(["nasara bo"], return_tensors="pt", truncation=True, max_length=32)
with torch.no_grad():
    probs = model(**batch).logits.softmax(-1)[0]
print({model.config.id2label[i]: round(p.item(), 3) for i, p in enumerate(probs)})
```

## Training

- **Data:** a Kanuri polarity lexicon of about 10,000 short phrases with polarity labels and English translations. Rows with corrupted characters and phrases with conflicting labels were removed. A label audit with a cross-validated English classifier flagged 598 suspect training labels (7.6%), which were removed. Validation and test sets were left untouched.
- **Setup:** encoder fine-tuned with AdamW (3e-5 for the encoder, 2e-4 for the head), batch size 32, maximum length 32, up to 10 epochs with early stopping on validation macro-F1, fp16 mixed precision, embedding matrix frozen.

## Evaluation

Held-out test split of 979 phrases (seed 42 run):

| Metric | Value |
|---|---|
| Macro-F1 | 0.6823 |
| Accuracy | 0.6895 |
| Validation macro-F1 | 0.7103 |

Test macro-F1 across three training seeds ranged from 0.676 to 0.691. With a test set this size, differences of about 0.03 are within noise.

## Limitations

- Trained on short dictionary-style phrases. It may do worse on long sentences, conversational text or social-media posts.
- Labels come from a lexicon, not from sentence-level annotation of real usage. Some labels are subjective.
- Performance is moderate (macro-F1 around 0.68). Do not use it for decisions about people.
- Input should be normalised as shown above. The tokenizer is case-sensitive.
- The hosted Inference widget does not run custom-code models. Use the snippets above locally.

## License

CC-BY-NC-4.0 (non-commercial), inherited from the NLLB-200 base model. Check the terms of the lexicon before reusing the data.
