---
language:
  - en
  - vi
  - fr
  - de
  - es
  - lo
  - th
  - my
  - id
  - fil
  - ms
  - ta
  - pt
  - ru
  - zh
  - ja
  - ko
license: cc-by-nc-4.0
library_name: transformers
pipeline_tag: text-generation
tags:
  - pii
  - pii-detection
  - named-entity-recognition
  - medical
  - grpo
  - rl
  - lora
  - lfm2
  - multilingual
datasets:
  - Meddies/meddies-pii
model-index:
  - name: Meddies/meddies-pii
    results:
      - task:
          type: token-classification
          name: PII Extraction
        dataset:
          name: Meddies PII Eval
          type: Meddies/meddies-pii
          config: eval
          split: train
        metrics:
          - name: Entity F1
            type: f1
            value: 0.8110
          - name: Precision
            type: precision
            value: 0.8112
          - name: Recall
            type: recall
            value: 0.8109
      - task:
          type: token-classification
          name: PII Extraction
        dataset:
          name: Meddies PII Test
          type: Meddies/meddies-pii
          config: test
          split: train
        metrics:
          - name: Entity F1
            type: f1
            value: 0.8380
          - name: Precision
            type: precision
            value: 0.8116
          - name: Recall
            type: recall
            value: 0.8663
---

# Meddies PII — Multilingual PII Extraction Model

<p align="left">
  <a href="https://huggingface.co/Meddies"><img alt="Meddies organization" src="https://img.shields.io/badge/Meddies-organization-0F766E"></a>
  <a href="https://meddies.ai"><img alt="Website" src="https://img.shields.io/badge/website-meddies.ai-0B4F6C"></a>
  <a href="mailto:contact@meddies.ai"><img alt="Email" src="https://img.shields.io/badge/contact-contact%40meddies.ai-1ABBC7"></a>
  <a href="https://huggingface.co/datasets/Meddies/meddies-pii"><img alt="Dataset" src="https://img.shields.io/badge/Dataset-024C6F?style=flat&logo=huggingface&logoColor=white"></a>
  <a href="https://huggingface.co/spaces/Meddies/meddies-pii-extractor"><img alt="Browser demo" src="https://img.shields.io/badge/Demo-0F172A?style=flat&logo=googlechrome&logoColor=white"></a>
  <a href="https://huggingface.co/Meddies/meddies-pii-onnx"><img alt="ONNX" src="https://img.shields.io/badge/ONNX-1ABBC7?style=flat&logo=huggingface&logoColor=white"></a>
  <img alt="License" src="https://img.shields.io/badge/license-CC--BY--NC--4.0-475569">
</p>

A multilingual PII extractor for teams that need structured JSON from clinical and administrative text.

> [!IMPORTANT]
> This is a research artifact for privacy and healthcare AI teams. It is not medical advice, not a redaction tool, and not a substitute for local validation before any clinical deployment, compliance workflow, or high-stakes privacy claim.
> If you want to use this model in commercial work, please contact us at [contact@meddies.ai](mailto:contact@meddies.ai).

<p align="center">
  <img src="./assets/hero-meddies-pii.png" alt="Meddies PII hero banner for a multilingual PII extraction model" width="100%" />
</p>

## Why this model

PII handling is a load-bearing constraint in healthcare AI.

A model can sound clinically useful and still be unsafe if it leaks names, identifiers, phone numbers, email addresses, or addresses. Traditional NER pipelines also create friction: token alignment bugs, language-specific span normalization, and brittle post-processing when the document format shifts. `Meddies PII` is built for that problem. Give it raw multilingual text in chat format, and it returns normalized JSON keyed by the target entity families.

The goal is simple: keep extraction behavior stable when the language, document format, or runtime changes.

## What this model does

`Meddies PII` is a causal language model used as a structured PII extractor.

Capabilities:
- multilingual extraction across 17 languages
- 7 normalized PII entity families
- deterministic JSON-friendly prompting
- a small enough footprint for consumer GPUs and browser deployment

Out of scope:
- automatic redaction or anonymization
- nested-entity reasoning
- adversarial hardening against evasive inputs

## Quick start

### Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Meddies/meddies-pii",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("Meddies/meddies-pii")

messages = [
    {
        "role": "system",
        "content": "Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number>, <id_number>, <date>",
    },
    {
        "role": "user",
        "content": "Patient John Smith, DOB 03/15/1985, was admitted to Mercy General Hospital. Contact: john.smith@email.com, (555) 123-4567. Address: 742 Evergreen Terrace, Springfield, IL 62704.",
    },
]

input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
).to(model.device)

output_ids = model.generate(
    input_ids,
    max_new_tokens=256,
    temperature=0.0,
    do_sample=False,
)

response = tokenizer.decode(
    output_ids[0][input_ids.shape[-1]:],
    skip_special_tokens=True,
)
print(response)
```

**Expected output**

```json
{
  "human_name": ["John Smith"],
  "date": ["03/15/1985"],
  "company_name": ["Mercy General Hospital"],
  "email_address": ["john.smith@email.com"],
  "phone_number": ["(555) 123-4567"],
  "address": ["742 Evergreen Terrace, Springfield, IL 62704"]
}
```

> [!NOTE]
> The bundled `chat_template.jinja` now defaults to the full 7-label schema. Passing an explicit system prompt is still the safest way to keep extraction keys tight for your exact workflow.

### vLLM

```python
from vllm import LLM, SamplingParams

llm = LLM(model="Meddies/meddies-pii", dtype="bfloat16")
sampling = SamplingParams(temperature=0.0, max_tokens=512)

messages = [
    {
        "role": "system",
        "content": "Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number>, <id_number>, <date>",
    },
    {
        "role": "user",
        "content": "Dr. Nguyen Van An, SĐT: 0912-345-678, email: an.nguyen@benhvien.vn",
    },
]

output = llm.chat(messages, sampling_params=sampling)
print(output[0].outputs[0].text)
```

### Transformers.js (browser / Node.js)

```javascript
import { pipeline } from "@huggingface/transformers";

const extractor = await pipeline("text-generation", "Meddies/meddies-pii-onnx", {
  dtype: "q4",
  device: "webgpu", // or "wasm" for broader compatibility
});

const messages = [
  {
    role: "system",
    content: "Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number>, <id_number>, <date>",
  },
  {
    role: "user",
    content: "Patient John Smith, DOB 03/15/1985, contact: john.smith@email.com",
  },
];

const output = await extractor(messages, {
  max_new_tokens: 512,
  do_sample: false,
  temperature: 0.0,
});

console.log(output[0].generated_text.at(-1).content);
```

### ONNX Runtime (Python)

```python
from optimum.onnxruntime import ORTModelForCausalLM
from transformers import AutoTokenizer

model = ORTModelForCausalLM.from_pretrained("Meddies/meddies-pii-onnx")
tokenizer = AutoTokenizer.from_pretrained("Meddies/meddies-pii-onnx")
```

## Evaluation details

<p align="center">
  <img src="./assets/results-meddies-pii.png" alt="Meddies-styled evaluation board showing overall eval and test metrics, per-entity F1, and per-language F1 for Meddies PII" width="100%" />
</p>

*Figure 1. Overall metrics first, then entity and language slices in the Meddies visual system.*

| Metric | Dataset / split | Result | Notes |
| --- | --- | --- | --- |
| Entity F1 | `Meddies/meddies-pii` / `eval` | **0.8110** | Mixed-language validation slice |
| Precision | `Meddies/meddies-pii` / `eval` | 0.8112 | Exact-match entity scoring |
| Recall | `Meddies/meddies-pii` / `eval` | 0.8109 | Exact-match entity scoring |
| Entity F1 | `Meddies/meddies-pii` / `test` | **0.8380** | Held-out test slice |
| Precision | `Meddies/meddies-pii` / `test` | 0.8116 | Exact-match entity scoring |
| Recall | `Meddies/meddies-pii` / `test` | **0.8663** | Highest overall headline metric |
| Value hallucination | `eval` / `test` | 1.31% / 1.35% | Generated entity values not found in the input |

Evaluation uses entity-level set-based exact match on `(value, label)` pairs. That is stricter than token overlap and closer to the extraction behavior a downstream system actually consumes.

### Per-entity performance (eval)

| Entity type | F1 | Reading |
| --- | ---: | --- |
| `phone_number` | **0.9484** | Strongest class; formatting regularity helps |
| `email_address` | 0.9252 | Also strong due to rigid surface form |
| `date` | 0.8607 | Solid despite multilingual date variation |
| `id_number` | 0.8132 | Usable, but depends on locale formatting |
| `address` | 0.7952 | Harder because boundary detection is messy |
| `human_name` | 0.7587 | Sensitive to naming style and nested context |
| `company_name` | **0.3277** | Known weak spot from label-definition mismatch |

### Per-language performance (eval)

<details>
<summary>Full language table</summary>

| Language | F1 |
| --- | ---: |
| Malay | 0.8588 |
| Korean | 0.8539 |
| Japanese | 0.8497 |
| Chinese | 0.8461 |
| Vietnamese | 0.8251 |
| Filipino | 0.8126 |
| Indonesian | 0.8079 |
| Burmese | 0.7851 |
| Portuguese | 0.7802 |
| Tamil | 0.7740 |
| Spanish | 0.7772 |
| French | 0.7623 |
| English | 0.7528 |
| German | 0.7376 |
| Thai | 0.7303 |
| Russian | 0.7117 |
| Lao | 0.7077 |

</details>

The spread is usable but not flat. The model holds together across 17 languages, but the lower-resource slices still lag the stronger East Asian and Southeast Asian sources.

## How it was built

- **Foundation model:** [`LiquidAI/LFM2-350M`](https://huggingface.co/LiquidAI/LFM2-350M)
- **Training dataset:** [`Meddies/meddies-pii`](https://huggingface.co/datasets/Meddies/meddies-pii)
- **Browser / ONNX variant:** [`Meddies/meddies-pii-onnx`](https://huggingface.co/Meddies/meddies-pii-onnx)

<p align="center">
  <img src="./assets/training-pipeline-meddies-pii.png" alt="Training pipeline for Meddies PII from LFM2 foundation model through SFT, GRPO, exact-match evaluation, and Hub plus ONNX release" width="100%" />
</p>

*Figure 2. LFM2 foundation → full SFT on multilingual PII extraction → GRPO alignment with extraction-specific rewards → exact-match evaluation on eval and test → Hub and ONNX release.*

Full reward design and GRPO configuration now live in [TRAINING.md](./TRAINING.md).

## Good fits

Use this model when you care about extracted values more than token-level tagging internals.

Good fits include multilingual de-identification of clinical notes, discharge summaries, admin forms, and mixed healthcare documents; browser or edge experiments where larger extractors are too heavy; and evaluation baselines for structured extraction across multilingual healthcare text.

## Limits

This is an extractor. Treat it that way.

- It does not redact or anonymize source text for you.
- Good benchmark numbers do not prove GDPR, HIPAA, or local-regulation compliance on your data.
- `company_name` is the weakest class in the current release.
- Around 1.3% of generated values are hallucinated rather than copied from the input.
- Nested entities are out of scope.
- If you omit the explicit system message, the bundled chat template defaults to five labels, not seven.
- Inputs designed to evade detection can still break this model.
- Medical measurements such as blood pressure, labs, dosages, and ages are intentionally excluded from the target label set.

## Feedback

Send us the failures.

The useful reports are concrete: broken quick-start paths, false positives on measurements, misses on localized identifiers, hallucinated values, browser-runtime regressions, or language slices that collapse on your documents.

You can find Meddies on Hugging Face at [huggingface.co/Meddies](https://huggingface.co/Meddies) and on the web at [meddies.ai](https://meddies.ai).

## Collaboration and sponsorship

Meddies is building verifiable clinical intelligence and the infrastructure around it.

We are a small team. Compute and review time are still tight.

If this work matters to you—sponsorship, collaboration, clinician review, or a larger conversation about the Meddies vision—email us at [contact@meddies.ai](mailto:contact@meddies.ai).

## Citation

```bibtex
@misc{meddies-pii-2026,
  title={Meddies PII: Multilingual PII Extraction with GRPO},
  author={Meddies Team},
  year={2026},
  url={https://huggingface.co/Meddies/meddies-pii}
}
```
