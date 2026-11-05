---
license: apache-2.0
library_name: laya
tags:
- decision-model
- routing
- examflow
- fine-tuned
---

# head-triage-gold — examflow triage router (Laya fine-tune)

Fine-tuned [`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya)
(Apache-2.0) for one job: route exam-pipeline page states among 4 actions —
`auto-accept`, `route-to-GLM-OCR`, `escalate-to-council`, `flag-human` —
in a single encoder pass (~ms on GPU).

## Training (all $0: Kaggle T4 x2)
- 2,000 gold construction-truth cases (incl. trap patterns), 0 eval overlap
- Full fine-tune, 3 epochs, lr 2e-5, batch 8, bf16; option order shuffled
  per sample + 3 instruction variants (anti-prior-collapse)
- Held-out synthetic eval (n=200): **1.0000** vs heuristic 0.81 (+19pp)

## Scope & limits (read before use)
- SYNTHETIC distribution: proves the loop, not real-world accuracy.
- Confidence is temp-uncalibrated until per-head refit (base checkpoint
  ships invalid temperatures — refit before trusting it).
- Never final-judge duty: dispatcher/signal layer only, abstain below tau.
- Safe format: `model.safetensors` (no pickle, no code execution on load).

## Load
```python
from laya import Agent
agent = Agent(model_id_or_path="ngdghfdc/head-triage-gold")
out = agent.predict(state, {"route": {"type": "choice",
    "instructions": "Pick the best next action.",
    "criteria": {o: o for o in ["auto-accept", "route-to-GLM-OCR",
                                "escalate-to-council", "flag-human"]}}})
```
