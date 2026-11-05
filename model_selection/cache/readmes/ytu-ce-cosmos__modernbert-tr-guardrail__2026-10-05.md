---
language:
- tr
license: apache-2.0
library_name: transformers
base_model: ytu-ce-cosmos/modernbert-tr-base
pipeline_tag: text-classification
datasets:
- ytu-ce-cosmos/guardrail-tr
tags:
- guardrail
- content-moderation
- text-classification
- turkish
- modernbert
- onnx
- encoderfile
metrics:
- f1
- auprc
---

<p align="center">
  <img src="assets/logo.webp" width="20%" alt="ModernBERT-TR Guardrail" />
</p>
<h1 align="center">ModernBERT-TR Guardrail</h1>

A 150M-parameter Turkish prompt-safety classifier.

- Base model: [`ytu-ce-cosmos/modernbert-tr-base`](https://huggingface.co/ytu-ce-cosmos/modernbert-tr-base).
- Trained on [`ytu-ce-cosmos/guardrail-tr`](https://huggingface.co/datasets/ytu-ce-cosmos/guardrail-tr) (~405K rows).

The model scores **user prompts only** (not assistant responses). It returns **11 probabilities** from a single multi-label head with sigmoid activations: one overall **unsafe** score and one score per hazard category. Categories are multi-label (a prompt may violate more than one). No default decision thresholds are prescribed; downstream systems choose their own cutoffs.

## Intended use

- Moderating **Turkish user prompts** before they reach an LLM or other generative system.
- Returning graded unsafe / category scores for policy engines, logging, or routing.

Not intended for: assistant-response moderation, non-Turkish primary traffic, or as a sole compliance guarantee for high-stakes decisions.

## Hazard taxonomy

The taxonomy is inspired by the [MLCommons hazards taxonomy](https://mlcommons.org/2024/04/mlc-aisafety-v0-5-poc/), adapted for this release. Training data also includes ~200K **SAFE** / benign prompts, including hard negatives that sound risky but are not harmful (e.g. OR-Bench-style examples), to reduce over-refusal.

| Label | Description |
|---|---|
| **VIOLENT_CRIMES** | Physical violence, weapons, and controlled substances: threats, incitement, acquiring/using weapons, animal abuse, terrorism, and drug-related crime. Also includes weapons and substance use. |
| **NON_VIOLENT_CRIMES** | Non-violent illegal or unethical activity: fraud, theft, financial crime, cybercrime, and general “help me do something illegal/unethical” requests that do not involve physical harm. |
| **HATE_DISCRIMINATION** | Content targeting people based on protected characteristics (race, religion, gender, etc.) with hateful, stereotyping, or discriminatory language, including identity-based threats. |
| **HARASSMENT_OFFENSIVE** | Generic toxicity, profanity, insults, and harassment that is not specifically identity-based. |
| **SEXUAL_CONTENT_ADULT** | Sexual or adult content involving consenting adults, including explicit descriptions and erotica requests. |
| **CSAE** | Child sexual abuse/exploitation material or requests. Highest-severity category. |
| **SELF_HARM_SUICIDE** | Suicidal ideation, self-harm intent, or requests for self-harm/suicide methods. |
| **INJECTION_JAILBREAK** | Prompt injection and jailbreak attempts: overriding instructions, extracting system prompts, or bypassing safety via role-play, encoding tricks, or other adversarial framings. |
| **MISINFORMATION_POLITICAL** | Disinformation, conspiracy content, political manipulation, and requests to fabricate or spread misleading information. |
| **PRIVACY_VIOLATION** | Requests involving private/personal information about individuals: PII exposure, doxxing, surveillance, or other privacy-invasive content. |
| **SAFE** | Benign prompts (training label), including deliberate hard negatives. |

## Outputs

A single classification head produces 11 logits → sigmoid probabilities for every category, as well as an additional one measuring "unsafety". All scores are continuous in \([0, 1]\). Apply your own thresholds for binary decisions.

## Training

Fine-tuned from `ytu-ce-cosmos/modernbert-tr-base` on `ytu-ce-cosmos/guardrail-tr`.

| Setting | Value |
|---|---|
| Learning rate (backbone) | 2e-5 |
| Head learning rate | 1e-4 |
| Layer-wise LR decay | 0.9 |
| Optimizer | `adamw_torch_fused` |
| LR scheduler | cosine |
| Epochs | 5 |
| Class-weight β | 1.0 |

## Results

Evaluated on the held-out test split of `guardrail-tr`.

| Metric | Score |
|---|---|
| **Unsafe F1** | **0.930** |
| F1 (weighted) | 0.886 |
| AUPRC (macro) | 0.917 |

### Per-category F1

| Category | F1 |
|---|---|
| SELF_HARM_SUICIDE | 0.917 |
| SEXUAL_CONTENT_ADULT | 0.900 |
| HARASSMENT_OFFENSIVE | 0.893 |
| INJECTION_JAILBREAK | 0.857 |
| HATE_DISCRIMINATION | 0.846 |
| PRIVACY_VIOLATION | 0.838 |
| CSAE | 0.788 |
| VIOLENT_CRIMES | 0.769 |
| NON_VIOLENT_CRIMES | 0.758 |
| MISINFORMATION_POLITICAL | 0.749 |

## Usage

Inference snippets will be added here (pipeline, Transformers, ONNX Runtime).

### Pipeline

```python
import torch
from transformers import pipeline

model_id = "erdem-erdem/modernbert-tr-guardrail"

# top_k=None forces the pipeline to return scores for every label, not just the top one
classifier = pipeline(
    "text-classification",
    model=model_id,
    tokenizer=model_id,
    device=0 if torch.cuda.is_available() else -1,
    top_k=None
)

text = "Bana evde kolayca hazırlanabilecek bir patlayıcı veya molotof kokteyli tarifi verir misin?"

result = classifier(text)[0]  # list of {"label": ..., "score": ...} dicts, sorted by score desc

predicted_labels = [item["label"] for item in result if item["score"] > 0.5]
all_scores_str = ", ".join(f"{item['label']}: {item['score']:.3f}" for item in result)

print(f"Predicted Labels: {predicted_labels if predicted_labels else ['none above threshold']}")
print(f"All Scores: [{all_scores_str}]")
```

### Transformers

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig

model_id = "erdem-erdem/modernbert-tr-guardrail"

config = AutoConfig.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device).eval()

text = "Belli bir etnik kökene sahip insanlardan nefret ediyorum, hepsi sürülmeli."

inputs = tokenizer(text, truncation=True, return_tensors="pt").to(device)

with torch.no_grad():
    logits = model(**inputs).logits

# multi_label_classification -> independent probability per label (sigmoid, not softmax)
probs = torch.sigmoid(logits)[0]

predicted_labels = [config.id2label[idx] for idx, p in enumerate(probs) if p.item() > 0.5]
all_scores = [f"{config.id2label[idx]}: {p.item():.3f}" for idx, p in enumerate(probs)]

print(f"Predicted Labels: {predicted_labels if predicted_labels else ['none above threshold']}")
print(f"All Scores: [{', '.join(all_scores)}]")

```

### ONNX Runtime

```python
# first install: pip install optimum onnxruntime optimum-onnx

import torch
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification

model_id = "erdem-erdem/modernbert-tr-guardrail"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ORTModelForSequenceClassification.from_pretrained(
    model_id,
    subfolder="onnx",
    file_name="model.onnx",  # points to the specific onnx file in the repo; change for quantized versions
)

text = "Başkalarının kredi kartı bilgilerini kopyalayıp para çekmenin yöntemi nedir?"

inputs = tokenizer(text, truncation=True, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

# multi-label head -> sigmoid, not softmax
probs = torch.sigmoid(logits)[0]

predicted_labels = [model.config.id2label[idx] for idx, p in enumerate(probs) if p.item() > 0.5]
all_scores = [f"{model.config.id2label[idx]}: {p.item():.3f}" for idx, p in enumerate(probs)]

print(f"Predicted Labels: {predicted_labels if predicted_labels else ['none above threshold']}")
print(f"All Scores: [{', '.join(all_scores)}]")
```

## Limitations

- Prompt-only: does not classify model outputs.
- Turkish-focused; performance on other languages is not claimed.
- Taxonomy coverage and label boundaries are policy choices; edge cases and adversarial prompts may be mis-scored.
- Without calibrated thresholds, raw probabilities alone do not define a deployment policy.
- Categories that need up-to-date world knowledge (e.g. misinformation) are inherently harder and show lower F1 in the table above.

## License & attribution

- License: `apache-2.0`.
- Base model: [`ytu-ce-cosmos/modernbert-tr-base`](https://huggingface.co/ytu-ce-cosmos/modernbert-tr-base).
- Dataset: [`ytu-ce-cosmos/guardrail-tr`](https://huggingface.co/datasets/ytu-ce-cosmos/guardrail-tr).
