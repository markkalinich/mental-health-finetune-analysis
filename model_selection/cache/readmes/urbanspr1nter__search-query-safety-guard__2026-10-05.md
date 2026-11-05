---
library_name: transformers
license: mit
language:
  - en
tags:
  - safety
  - guardrail
  - text-classification
  - distilbert
  - llm-guardrails
base_model: distilbert-base-uncased
pipeline_tag: text-classification
---

# Search Query Safety Guard

A DistilBERT-base-uncased guardrail that classifies an AI agent's **search query** as `SAFE` or `DANGEROUS` before it reaches a web search/scrape tool. It is designed to sit as a proxy between an agent's search tool and the real search service.

- **0 → SAFE** — allow the search
- **1 → DANGEROUS** — block and return an error to the agent

## Intended use

Wrap a search/scrape tool so every query is classified first. Safe queries pass through to the real service; dangerous queries are blocked and surfaced to the agent as an error.

The model is trained to flag queries that seek to obtain, produce, or facilitate clearly harmful or illegal outcomes, across categories including:

- terrorism and violent extremism
- sexual content, including material involving minors
- controlled substances — procurement, manufacture, distribution
- weapons and explosives — unlawful manufacture or acquisition
- violence and physical harm
- self-harm
- hate, harassment, and targeting of individuals or groups
- kidnapping and human trafficking
- fraud, counterfeiting, and money laundering
- arson
- **theft or sale of credentials and secrets** — e.g. stolen authentication tokens, leaked API keys, session cookies, private keys

It also distinguishes these from legitimate, allow-listed intent: historical and policy education, public-health research, reporting a crime, and seeking help or resources.

## Cyber policy (intent, not keywords)

This model also backs a **cyber-defense agent**, so the security boundary is drawn by *intent* rather than by topic:

- **SAFE** — researching how an attack technique works, or how to detect, prevent, or train against it (e.g. explaining ransomware behavior and incident-response steps, or how credential stuffing works and how rate limiting mitigates it).
- **DANGEROUS** — procuring, selling, harvesting, or exfiltrating credentials, secrets, or PII, or targeting a specific person's or organization's accounts.

The rule of thumb: a query about *understanding or defending against* a threat is allowed; a query about *obtaining or selling* the means to carry one out is blocked.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model = AutoModelForSequenceClassification.from_pretrained("urbanspr1nter/search-query-safety-guard")
tokenizer = AutoTokenizer.from_pretrained("urbanspr1nter/search-query-safety-guard")
model.eval()

def predict(query: str) -> dict:
    enc = tokenizer(query, return_tensors="pt", max_length=256, truncation=True, padding=True)
    with torch.no_grad():
        probs = torch.softmax(model(**enc).logits, dim=-1)
    pred = int(torch.argmax(probs, dim=-1).item())
    return {
        "query": query,
        "label": model.config.id2label[pred],   # "SAFE" or "DANGEROUS"
        "safe": pred == 0,
        "confidence": float(probs[0, pred].item()),
    }

predict("how to cook pasta")          # -> SAFE
predict("how does a buffer overflow work and how is it prevented")   # -> SAFE
# a query seeking to buy or harvest credentials -> DANGEROUS
```

## Evaluation

Trained and evaluated with **two held-out sets**, both verified disjoint from the training data:

| Set | Accuracy | DANGER F1 | Dangerous leaks (FN) | Safe blocked (FP) |
|-----|----------|-----------|----------------------|--------------------|
| primary (137 examples) | 99.27% | 0.9937 | 0 | 1 |
| fresh generalization (43 examples) | 100% | 1.0000 | 0 | 0 |

**Recall on dangerous queries is 1.000** on both held-out sets — no dangerous query reached the web. The second set uses fresh wording of the same patterns and exists specifically to guard against the model memorizing the first.

## Training

- Base: `distilbert-base-uncased`, 2 labels, max 256 tokens
- Optimizer: AdamW, lr 2e-5, batch 8, early stopping on F1
- Data: 2,313 examples (~61% SAFE / ~39% DANGEROUS), grown from 1,973 with a leakage guard that rejected any addition ≥82% similar to an eval query
- The training dataset and held-out evaluation sets are **not** published; only the model is distributed.

## Limitations

- English only
- Evaluates a single query — no conversation history
- A small dataset cannot cover every edge case; deploy with a confidence threshold and log the grey zone
