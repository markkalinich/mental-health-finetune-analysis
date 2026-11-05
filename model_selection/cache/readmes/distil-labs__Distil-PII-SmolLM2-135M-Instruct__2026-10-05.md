---

license: apache-2.0
language: en
base_model: HuggingFaceTB/SmolLM2-135M-Instruct
pipeline_tag: text-generation
tags: [pii-redaction, privacy, slm, distil-labs]
---

# Distil-PII-SmolLM2-135M-Instruct

A **small language model** (SLM) fine-tuned by Distil Labs for **policy-aware PII redaction** that outputs a single JSON object with `redacted_text` and `entities`. Optimized to run locally with strong accuracy and strict schema adherence.

## Model Details

* **Developed by:** Distil Labs GmbH
* **License:** Apache 2
* **Finetuned from:** HuggingFaceTB/SmolLM2-135M-Instruct

## Intended Use & Limitations

* **Use cases:** Redacting support chats, logs, tickets, transcripts—removing identity while preserving ops signals (IDs last-4, order numbers, etc.).
* **Out of scope:** Legal or compliance advice; languages beyond English (generalization not guaranteed); domain-specific IDs unseen in training.

## Input & Output

**Input:** A plain-text prompt with task instruction + context.
**Output (JSON only):**

```json
{
  "redacted_text": "Text with in-place tokens",
  "entities": [
    {"value": "<original>", "replacement_token": "[TOKEN]", "reason": "<why>"}
  ]
}
```

**Tokens:** `[PERSON] [EMAIL] [PHONE] [ADDRESS] [SSN] [ID] [UUID] [CARD_LAST4:####] [IBAN_LAST4:####] [GENDER] [AGE] [RACE] [MARITAL_STATUS]`

## Training

Instruction-tuned on a compact policy spec + ~20 curated examples emphasizing **exact JSON schema**, **minimal in-place edits**, and **entity correctness**.

## Evaluation

Judged by a frontier LLM using a deterministic rubric: JSON-only, schema validity, **redacted_text exact match**, and **set-equality** of `(value, replacement_token)` pairs (reason/order ignored). Score: **0.25 +/- 0.05**.

## How to Use
Details of deployment can be found in https://docs.distillabs.ai/how-to/model-deployment


## Risks & Mitigations

* **False negatives/positives:** May miss novel formats or over-redact generic terms. Mitigate via guardrails + post-validation.
* **Policy drift:** Keep task preamble fixed; monitor with unit tests.

## Model Sources

* **Homepage:** [https://distillabs.ai](https://distillabs.ai)
* **Contact:** [contact@distillabs.ai](mailto:contact@distillabs.ai)
