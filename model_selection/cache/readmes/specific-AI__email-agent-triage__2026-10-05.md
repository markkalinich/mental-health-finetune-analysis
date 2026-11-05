---
license: mit
language:
  - en
library_name: transformers
pipeline_tag: text-classification
tags:
  - email
  - triage
  - classification
  - bert
  - specific-ai
  - gguf
base_model: google-bert/bert-base-uncased
---

# specific-AI/email-agent-triage

A compact **BERT** email triage classifier distilled with **[Specific AI](https://specific.ai)**.
It assigns each email to one of five action-oriented categories so agentic
workflows can decide whether to reply, archive, or take no action.

| | |
|---|---|
| **Task** | Single-label text classification |
| **Base model** | `bert-base-uncased` |
| **Training data** | ~15,000 examples |
| **License** | MIT |

## Input format

Examples were trained on emails formatted as plain text with `From`, `Subject`,
and body (blank line between the headers and the body):

```text
From: <from>
Subject: <subject>

<body>
```

Pass inputs in this same shape at inference time for best results.

## Labels

| Label | Meaning | Suggested next action |
|---|---|---|
| **URGENT** | Requires immediate attention (e.g. critical system failure, hard deadline right now). | Reply |
| **NEEDS_RESPONSE** | A task or response is owed, but it is not a drop-everything emergency. | Reply |
| **PROMOTIONAL** | Bulk mail, unsolicited promotions, or newsletters. | Archive |
| **PERSONAL** | Non-business, personal communications. | None |
| **FYI** | Informational only — the recipient should know, but no reply is required. | None |

## Evaluation

Compared against **gpt-5.4-mini** as a teacher / baseline on the same evaluation set:

| Metric | gpt-5.4-mini | SpecificAI |
|---|---:|---:|
| Accuracy | 0.693 | **0.720** |
| Precision | 0.810 | 0.763 |
| Recall | 0.693 | **0.720** |
| F1 score | 0.693 | **0.716** |

## Repository contents

This card ships both a full Hugging Face checkpoint and GGUF-ready artifacts:

- Full `BertForSequenceClassification` weights (`model.safetensors`) + tokenizer
- Head layers as NumPy files (`pooler_*.npy`, `classifier_*.npy`) for GGUF / Lemonade fusion
- Encoder GGUF: `bert-base-only.gguf` (CLS pooling; use with raw / unnormalized embeddings)

## Quick start — Transformers

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "specific-AI/email-agent-triage"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

text = """From: ops@example.com
Subject: Production outage

Production is down — please escalate immediately."""
inputs = tokenizer(text, return_tensors="pt", truncation=True)
with torch.no_grad():
    logits = model(**inputs).logits
pred = model.config.id2label[int(logits.argmax(-1))]
print(pred)
```

## Quick start — Lemonade + specific-ai-tools

When running the GGUF encoder through Lemonade Server:

```bash
pip install specific-ai-tools
```

```python
from specific_ai_tools.embedding_heads import LemonadeEmbeddingClassifier

classifier = LemonadeEmbeddingClassifier(
    lemonade_model_name="user.email-agent-triage",
    checkpoint="specific-AI/email-agent-triage:bert-base-only.gguf",
    lemonade_base_url="http://localhost:13305",
)

text = """From: user@example.com
Subject: Billing question

Please escalate this ticket to billing."""
result = classifier.predict_one(text)
print(result.predicted_labels, result.predicted_confidences)
```

See the Specific AI toolkit docs for llama-cpp and other embedding backends.

## Intended use

- Email / inbox agent triage in production or on-device / CPU deployments
- Routing messages into reply / archive / no-action queues

**Out of scope:** legal advice, medical triage, or safety-critical decisions without
human review. Labels reflect email workflow intent, not sender identity verification.

## About Us

**[Specific AI](https://specific.ai)** is the automatic SLM distillation platform
that turns task prompts into production-grade small language models in days —
not weeks — so your subject matter experts can ship models without waiting on
scarce data-science bandwidth.

We help enterprises move agentic AI from prototype to production with SLMs that
are typically **1,000×–10,000× smaller** than teacher LLMs, run in
**milliseconds** on CPUs or edge devices, and deliver the same or better
task quality at a fraction of the cost — self-hosted on your cloud or
downloaded for your own inference stack.

**Prompt → Distill → Deploy.** Bring your prompt and data, drop them into
Specific AI, and get a validated small model ready to test and ship.

Ready to create SLMs at scale? Visit **[specific.ai](https://specific.ai)**.

## License

MIT — see [LICENSE](LICENSE).

Copyright (C) 2026 Specific AI Inc. All rights reserved.
