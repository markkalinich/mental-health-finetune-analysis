---
license: mit
language:
  - ko
  - en
tags:
  - pii-detection
  - token-classification
  - korean
  - xlm-roberta
  - multilingual-e5
  - bioes
base_model: intfloat/multilingual-e5-base
pipeline_tag: token-classification
---

# Korean PII — multilingual-e5-base

Span-level **Korean PII detection**, fine-tuned from
[`intfloat/multilingual-e5-base`](https://huggingface.co/intfloat/multilingual-e5-base)
(a multilingual XLM-RoBERTa bidirectional encoder). It detects 9 PII categories as
character-offset spans and is trained for **multi-domain** Korean coverage
(conversational, news, and a range of document domains).


**[Open PII Notebook](https://huggingface.co/FrameByFrame/korean-pii-e5-base/blob/main/pii_demo.ipynb)** — load the model and redact Korean PII interactively.

## Capabilities

| Category | Description | Example |
|---|---|---|
| `private_person` | Personal name (Korean / Western / handles) | 김민수, John Smith |
| `private_address` | Physical / postal address | 서울특별시 강남구 테헤란로 123 |
| `private_phone` | Phone number | 010-1234-5678 |
| `private_email` | Email address | minsu@example.com |
| `private_date` | Birthday / personally-identifying date | 1985년 3월 12일 |
| `private_url` | Personal URL | github.com/minsu |
| `account_number` | Bank, card, RRN, passport, etc. | 110-234-567890 |
| `personal_handle` | Username / handle | rainbow879612 |
| `ip_address` | IP address | 192.168.1.5 |

## Benchmark Results

Evaluated across three domains, exact character-span F1, with deterministic span
normalization (see `extract_pii` below).

| eval set | what it measures | Overall F1 |
|---|---|---:|
| **KDPII test** (2,252) | conversational Korean (in-domain) | **0.943** |
| **Held-out document domains** (insurance, government) | unseen domains | **0.995** |
| **KLUE-NER `person`** | real Korean **news** text | **0.866** (recall 0.92) |

### KDPII per-class (conversational, in-domain)
| label | F1 | | label | F1 |
|---|---:|---|---|---:|
| `private_email` | 1.000 | | `private_person` | 0.909 |
| `private_url` | 1.000 | | `private_address` | 0.922 |
| `ip_address` | 1.000 | | `account_number` | 0.979 |
| `private_date` | 0.980 | | `personal_handle` | 0.863 |
| `private_phone` | 0.993 | | | |


## Quick Start

### Install

```bash
pip install "transformers>=4.40" torch safetensors
```

### Load

```python
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

MODEL_ID = "FrameByFrame/korean-pii-e5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForTokenClassification.from_pretrained(MODEL_ID, torch_dtype=torch.bfloat16)
model.eval()
if torch.cuda.is_available():
    model.cuda()
```

### Inference

The model emits per-token BIOES labels. The helper decodes them into character-offset
spans and applies light, deterministic **span normalization** (strips trailing Korean
particles / whitespace from a span, e.g. `민수씨` → `민수`, `송파구에` → `송파구`). The
benchmark numbers above include this normalization.

```python
import re

_TRAILING_JOSA = ["이에요","이라고","입니다","이야","이랑","한테","에게","으로","이가","이는",
                  "에서","이고","예요","씨","님","이","가","은","는","을","를","야","아","에","의","랑","께","고"]
_DATE_END = re.compile(r".*(?:일|[0-9])", re.S)

def _normalize(text, label, s, e):
    while s < e and text[s] in " .,\t\n": s += 1
    while e > s and text[e-1] in " .,\t\n": e -= 1
    if label == "private_date":
        m = _DATE_END.match(text[s:e])
        if m and m.end() > 0: e = s + m.end()
    elif label in ("private_person", "personal_handle", "private_address"):
        for _ in range(2):
            seg = text[s:e]
            for j in _TRAILING_JOSA:
                if seg.endswith(j) and (e - s) - len(j) >= 2:
                    e -= len(j); break
            else:
                break
    return s, e

def extract_pii(text: str, max_length: int = 256):
    enc = tokenizer(text, truncation=True, max_length=max_length,
                    return_offsets_mapping=True, return_tensors="pt")
    offsets = enc.pop("offset_mapping")[0].tolist()
    with torch.no_grad():
        logits = model(**{k: v.to(model.device) for k, v in enc.items()}).logits
    pred = logits.argmax(-1)[0].tolist()
    id2label = model.config.id2label

    spans, active = [], None  # active = [label, start, end]
    for i, lid in enumerate(pred):
        label = id2label[int(lid)]
        cs, ce = offsets[i]
        if cs == ce:  # special token
            if active: spans.append(active); active = None
            continue
        if label == "O":
            if active: spans.append(active); active = None
            continue
        prefix, cat = label.split("-", 1)
        if prefix in ("B", "S") or not active or active[0] != cat:
            if active: spans.append(active)
            active = [cat, cs, ce]
        else:
            active[2] = ce
    if active: spans.append(active)

    out = []
    for cat, s, e in spans:
        s, e = _normalize(text, cat, s, e)
        if text[s:e].strip():
            out.append({"label": cat, "start": s, "end": e, "text": text[s:e]})
    return out
```

### Redaction

```python
def redact(text: str) -> str:
    spans = sorted(extract_pii(text), key=lambda s: s["start"], reverse=True)
    for s in spans:
        text = text[:s["start"]] + f"[{s['label'].upper()}]" + text[s["end"]:]
    return text

>>> redact("김민수님의 번호는 010-1234-5678입니다.")
"[PRIVATE_PERSON]님의 번호는 [PRIVATE_PHONE]입니다."
```

## Output Schema

| field | description |
|---|---|
| `label` | one of the 9 categories above |
| `start` | character offset start (inclusive) |
| `end` | character offset end (exclusive) |
| `text` | the matched substring |

## Training Details

| | |
|---|---|
| **Base model** | [`intfloat/multilingual-e5-base`](https://huggingface.co/intfloat/multilingual-e5-base) (XLM-RoBERTa, ~278M) |
| **Task** | token classification, BIOES (9 PII classes → 37 labels) |
| **Method** | full fine-tune (token head randomly initialized; encoder fully trained) |
| **Datasets** | **multi-domain Korean mix** — KDPII (conversational, CC BY 4.0) + KLUE-NER person spans (news) + LLM-generated multi-domain documents (medical, legal, finance, e-commerce, HR, real-estate, social, gaming, IT, telecom, education, travel, delivery, email) with placeholder-filled PII + distribution-matched synthetic PII. All PII is synthetic/generated, never real. |
| **Split** | KDPII test held out (seed 42); 2 document domains (insurance, government) fully held out for unseen-domain eval; KLUE-val held out |
| **Optimizer** | AdamW, lr 3e-5, linear schedule, warmup 0.05 |
| **Batch / seq** | 32 per device, max_length 256 |
| **Epochs** | 3, best checkpoint by `eval_span_f1` |
| **Precision** | bf16 |
| **Hardware** | 1× NVIDIA RTX A5000 |

## Known Limitations

- **`personal_handle` (~0.86 in-domain)** is the weakest class — handles are open-vocabulary
  (arbitrary usernames) and overlap with names; near its practical ceiling.
- **Held-out document-domain F1 (0.995) is optimistic** — those domains are unseen, but share
  the *generator/entity distribution* of the synthetic training data. It shows domain-content
  transfer, not guaranteed real-world-text robustness. Treat real-world performance as bounded
  by the KDPII (0.94, real conversational) and KLUE-news (0.87, real news) numbers.
- **Evaluate on your own domain before high-stakes use.** Coverage is broad but not exhaustive;
  Korean PII annotation conventions vary by source.
- **Structured PII** (phone/email/url/ip/account/RRN) is best paired with a regex/checksum
  validator in production for guaranteed precision.
- The `extract_pii` helper applies span normalization; if you decode logits yourself, apply
  equivalent trimming to reproduce the reported numbers.

## License

MIT — inherited from the base [`intfloat/multilingual-e5-base`](https://huggingface.co/intfloat/multilingual-e5-base) (MIT). Training data includes KDPII (CC BY 4.0).

## Citation

```bibtex
@misc{framebyframe-korean-pii-e5-base-2026,
  title  = {Korean PII (multilingual-e5-base): token classification for Korean PII},
  author = {Mariappan, Vijayachandran},
  year   = {2026},
  url    = {https://huggingface.co/FrameByFrame/korean-pii-e5-base}
}
```

## Contact

For inquiries, please contact vijay@artelligence.ai
