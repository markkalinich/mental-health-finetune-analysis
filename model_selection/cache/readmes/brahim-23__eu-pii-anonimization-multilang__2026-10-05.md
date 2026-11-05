---
license: apache-2.0
language:
- en
- pl
- de
- fr
- es
- it
- nl
- pt
- ro
- cs
- sv
- el
- hu
- bg
- hr
- da
- et
- fi
- ga
- lv
- lt
- mt
- sk
- sl
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: token-classification
tags:
- pii-detection
- token-classification
- privacy
- sensitive-data
- multilingual
- bards-ai
inference: true
widget:
- text: "John Smith, passport AB123456, phone +48 123 456 789, email john.smith@example.com."
  example_title: "English — passport, phone, email"
- text: "Jan Kowalski, PESEL 80010112345, ul. Marszałkowska 12, Warszawa."
  example_title: "Polish — PESEL + address"
- text: "Maria Müller, IBAN DE89370400440532013000, München."
  example_title: "German — IBAN"
- text: "Pierre Dupont, sécurité sociale 1 85 12 75 116 001 23, Paris."
  example_title: "French — SSN"
- text: "Carlos García, DNI 12345678Z, Madrid, +34 612 345 678."
  example_title: "Spanish — DNI"
- text: "Giulia Rossi, codice fiscale RSSGLI85M41H501Z, Roma."
  example_title: "Italian — codice fiscale"
---
# EU PII Anonimization Multilingual Detector

A multilingual PII detector built for EU compliance reality: 24 official languages, GDPR special categories, AI Act high-risk data - in one model.

![Zrzut ekranu 2026-05-5 o 08.47.14](https://cdn-uploads.huggingface.co/production/uploads/61deb858807c926c6423340c/3-Sje3Dpc88X4NK93ppPl.png)


## Try it

🔗 [Live demo in Browser](https://eu-pii.bards.ai/)

## Why this exists

GDPR and the AI Act require you to detect and redact personal data across every language your users write in. Most open-source PII models were trained on English with a few translations bolted on, and they cover the basics — names, emails, phone numbers — while missing exactly the categories regulators care about: biometric data, genetic data, health information, political opinions, ethnic origin.

`bardsai/eu-pii-anonimization-multilang` is trained end-to-end on real multilingual data (not English-translated), covers **36 entity classes** mapped to GDPR Article 9 special categories and AI Act high-risk identifiers, and ships with quantized ONNX weights so you can run it in production pipelines without GPU infrastructure.

## What's different

- **Native multilingual training.** Real text in EU languages. Performance on Polish, German, French, Italian, and Spanish is comparable to the English baseline.
- **GDPR special categories covered.** Health, biometric, genetic, and other Article 9 entities that most OSS PII models skip entirely.
- **Production-ready.** ONNX export and INT8 quantized weights included. Runs on CPU at latencies that work inside RAG ingestion or real-time redaction pipelines.

## Who this is for

Compliance and privacy engineers at EU companies who need to:
- Redact PII from documents, support tickets, emails, and chat logs before storage or analysis
- Sanitize datasets before training, sharing, or moving across jurisdictions
- Filter inputs to RAG pipelines and search indexes so personal data doesn't leak into prompts or logs
- Build audit trails for what was redacted, when, and why

<iframe
  src="https://eu-pii.bards.ai"
  frameborder="0"
  width="100%"
  height="640"
></iframe>

## Quick start

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

model_name = "bardsai/eu-pii-anonimization-multilang"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

text = "John Smith, passport AB123456, phone +48 123 456 789"
inputs = tokenizer(text, return_tensors="pt", truncation=True)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)

tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
labels = [model.config.id2label[p.item()] for p in predictions[0]]

for token, label in zip(tokens, labels):
    if label != "O":
        print(label, token)
```

For production, use the quantized ONNX weights in `onnx/model_quantized.onnx` — same outputs, ~4x smaller, CPU-friendly latency.

## Entity coverage

36 classes across eight families, with `B-`/`I-` BIO labeling:

- **Personal identity** — names, dates of birth, national ID numbers
- **Contact and location** — addresses, emails, phone numbers, geolocation
- **Official documents** — passports, driver's licenses, tax IDs
- **Financial** — IBAN, credit card, account numbers
- **Technical identifiers** — IP addresses, MAC addresses, device IDs, usernames
- **Organization data** — employer, institutional affiliations
- **Health, biometric, genetic** (GDPR Art. 9) — medical conditions, biometric identifiers, genetic data
- **Special-category** (GDPR Art. 9) — racial/ethnic origin, political opinions, religious beliefs, sexual orientation, trade union membership

Full label list in `config.json` (`id2label` / `label2id`).

## Limitations

This is a model, not a compliance program. A few things to keep in mind:

- Performance varies by language, domain, and input quality. OCR noise, code-switching, and unusual formatting will degrade recall.
- Ambiguous mentions (a name that's also a place, an ID-shaped number that isn't an ID) need post-processing rules or human review.
- Detection ≠ legal sufficiency. Use this to support a redaction workflow, not to replace your DPO's judgment.
- Threshold tuning matters. The right operating point depends on whether you're optimizing for recall (compliance) or precision (data utility).

## Files

- `model.safetensors` — model weights
- `config.json` — config and label mapping
- `tokenizer.json`, `tokenizer_config.json` — tokenizer assets
- `onnx/model.onnx` — ONNX export
- `onnx/model_quantized.onnx` — INT8 quantized for CPU production
- `training_args.bin` — training metadata

## Citation
```
@misc{bards.ai_2026,
	author       = { bards.ai and Michał Swędrowski and Michał Pogoda-Rosikoń and Karol Samorański },
	title        = { eu-pii-anonimization-multilang (Revision 6de9f68) },
	year         = 2026,
	url          = { https://huggingface.co/bardsai/eu-pii-anonimization-multilang },
	doi          = { 10.57967/hf/8721 },
	publisher    = { Hugging Face }
}
```

## About bards.ai

We build product ML for teams shipping AI to real users — RAG, agents, fine-tuned models, evals, and the unglamorous infrastructure that keeps them working. 16+ open models on Hugging Face, 10+ publications, production deployments at Comcast, Chili Piper, and Surfer SEO.

[bards.ai](https://bards.ai)
