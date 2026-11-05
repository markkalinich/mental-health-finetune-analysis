---
license: other
license_name: composite-license
license_link: LICENSE.md
language:
  - en
  - fr
  - de
  - it
tags:
  - pii
  - anonymization
  - privacy
  - synthetic-data
  - qlora
  - unsloth
  - data-privacy
  - gdpr
  - hipaa
  - named-entity-recognition
  - text-rewriting
base_model: Qwen/Qwen2.5-0.5B-Instruct
datasets:
  - nvidia/Nemotron-PII
  - ai4privacy/pii-masking-200k
pipeline_tag: text-generation
model-index:
  - name: qwen2.5-0.5b-pii-anonymizer
    results: []
---

# qwen2.5-0.5b-pii-anonymizer

A **context-aware PII anonymization model** fine-tuned from [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct). Unlike traditional redaction tools that insert ugly `[REDACTED]` or `<PERSON>` placeholders, this model **replaces personally identifiable information with realistic synthetic data** while preserving the original grammar, formatting, tone, and semantic flow of the text.

This is **Phase 1** of an enterprise grade PII anonymization pipeline. THIS CANNOT BE USED FOR ANY COMMERCIAL PURPOSE WITHOUT LICENSE APPROVAL FROM AI4PRIVACY. Phase 2 combines this model with [Microsoft Presidio](https://github.com/microsoft/presidio) and [GLiNER](https://github.com/urchade/GLiNER) for production-grade, compliance-ready deployment.

---

## Table of Contents

- [What This Model Does](#what-this-model-does)
- [Why Context-Aware Rewriting](#why-context-aware-rewriting)
- [Training Details](#training-details)
- [Datasets](#datasets)
- [Data Engineering Pipeline](#data-engineering-pipeline)
- [Model Architecture & Fine-Tuning](#model-architecture--fine-tuning)
- [Training Infrastructure](#training-infrastructure)
- [Training Results](#training-results)
- [Inference Examples](#inference-examples)
- [Usage](#usage)
  - [Quick Start — Test It in 30 Seconds](#quick-start--test-it-in-30-seconds)
  - [Run the Full Test Suite](#run-the-full-test-suite--see-results-across-12-pii-categories)
  - [With Unsloth (2× Faster)](#with-unsloth-2-faster-inference-60-less-memory)
  - [Batch Processing](#batch-processing--anonymize-multiple-documents)
  - [Process a File Line-by-Line](#process-a-file-line-by-line)
  - [Integration with Pandas DataFrames](#integration-with-pandas-dataframes)
- [Known Limitations](#known-limitations)
- [Phase 2 Roadmap](#phase-2-roadmap)
- [License](#license)
- [Citation](#citation)
- [Acknowledgments](#acknowledgments)

---

## What This Model Does

Given any text containing personally identifiable information, the model outputs the **same text** with all PII replaced by realistic, contextually appropriate synthetic entities:

| PII Type | Input | Output |
|----------|-------|--------|
| Names | "Dear Mr. Arjun Mehta" | "Dear Mr. John Davis" |
| Emails | "sarah.johnson@globalfinance.com" | "jason69@example.net" |
| Phone numbers | "+91-22-4567-8901" | "001-727-944-3626" |
| SSN | "SSN: 321-45-6789" | "SSN: 458-78-3375" |
| Addresses | "42 Baker Street, London" | "50783 Wilson Stream, New York" |
| Passport | "Passport L8472910" | "Passport xQyFZbWd" |
| Mixed PII | "I'm David Chen (david.chen@techcorp.io, +1-415-555-0198)" | "I'm Michael Smith (kathleen32@example.com, 676-297-4529)" |

The model handles 55+ PII categories across corporate, medical, financial, conversational, and multilingual contexts.

---

## Why Context-Aware Rewriting

Traditional PII tools fall into two camps, each with significant drawbacks:

**Rule-based redaction** (regex, Presidio alone) catches structured patterns well (SSNs, credit cards) but produces unreadable output filled with `[PERSON]` and `[ADDRESS]` tokens. This breaks downstream NLP tasks, makes documents unusable for analytics, and is immediately obvious to anyone reading the text.

**Naive masking** (simple find-and-replace) often breaks grammar, misses contextual PII like "my boss David" or "send it to the Baker Street office", and can't handle the same entity appearing in different syntactic roles.

**This model combines both strengths**: it understands context deeply enough to identify PII that rule-based systems miss, while generating natural-sounding replacements that maintain document utility. A medical record that says "Patient: Robert Williams, DOB: 1985-04-12" becomes "Patient: Michael Rodriguez, DOB: 1976-03-25" — still perfectly usable for analytics, training other models, or sharing with third parties.

---

## Training Details

### Summary

| Parameter | Value |
|-----------|-------|
| **Base model** | [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) |
| **Parameters** | 502.8M total, 8.8M trainable (1.75%) |
| **Method** | QLoRA (4-bit NF4 quantization + LoRA r=16) |
| **Framework** | [Unsloth](https://github.com/unslothai/unsloth) + HuggingFace TRL |
| **Training samples** | 309,225 (after validation filtering) |
| **Train/eval split** | 293,763 / 15,462 (95/5) |
| **Epochs** | 2 |
| **Batch size** | 64 |
| **Total steps** | 9,182 |
| **Learning rate** | 2e-4 (cosine schedule, 100 warmup steps) |
| **Optimizer** | AdamW 8-bit |
| **Precision** | bfloat16 |
| **Final training loss** | 1.0588 |
| **Training time** | ~2.3 hours |
| **Hardware** | NVIDIA RTX PRO 6000 Blackwell (95.6 GB VRAM) |

---

## Datasets

This model was trained on a merged corpus from two high-quality open-source PII datasets:

### nvidia/Nemotron-PII

- **Source**: [huggingface.co/datasets/nvidia/Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII)
- **Size**: 100,000 English records
- **License**: CC-BY-4.0
- **Description**: A synthetic, persona-grounded dataset for PII/PHI detection. Contains span-level annotations for 55+ PII/PHI categories across 50+ industries, generated with NVIDIA NeMo Data Designer using synthetic personas grounded in U.S. Census data. Includes both structured (forms, invoices) and unstructured (emails, free text) documents.
- **Categories covered**: first_name, last_name, date_of_birth, street_address, email, phone_number, ssn, credit_card, company_name, vehicle_identifier, url, blood_type, employment_status, and 40+ more.

### ai4privacy/pii-masking-200k

- **Source**: [huggingface.co/datasets/ai4privacy/pii-masking-200k](https://huggingface.co/datasets/ai4privacy/pii-masking-200k)
- **Size**: 209,261 multilingual records (English, French, German, Italian)
- **License**: AI4Privacy Free/Corporate License (see LICENSE.md)
- **Description**: Built by AI4Privacy (Ai Suisse SA) using the p5y framework with human-in-the-loop validation. Features diverse real-world PII scenarios across multiple domains and languages. Contains span-level privacy masks with entity types and positions.
- **Categories covered**: FIRSTNAME, LASTNAME, EMAIL, PHONE, STREETADDRESS, CITY, ZIPCODE, COUNTRY, JOBAREA, JOBTYPE, CREDITCARDNUMBER, IBAN, BITCOINADDRESS, VEHICLEVIN, USERAGENT, and 30+ more.

---

## Data Engineering Pipeline

Neither dataset provides ready-made "input → synthetic output" pairs. A custom data engineering pipeline was built to transform both datasets into training-ready format.

### The Challenge

- **Nvidia Nemotron-PII** provides `text` (raw) + `spans` (PII positions with labels), but no synthetic replacements. The spans use Python-style single-quoted dictionaries (not JSON), requiring `ast.literal_eval` for parsing.
- **AI4Privacy** provides `source_text` (raw) + `target_text` (with `[LABEL]` mask tokens, not synthetic data) + `privacy_mask` (PII values with positions and labels).

### The Solution

Both datasets were processed through a label-aware synthetic data generation pipeline using [Faker](https://faker.readthedocs.io/):

```
[Raw text + PII span annotations]
         │
         ▼
[Parse spans (ast.literal_eval for Nvidia, JSON for AI4Privacy)]
         │
         ▼
[Sort spans by position (descending) to preserve indices during replacement]
         │
         ▼
[For each span: generate synthetic value via label→Faker mapping]
    first_name  → fake.first_name()
    email       → fake.email()
    ssn         → fake.ssn()
    street_addr → fake.street_address()
    phone       → fake.phone_number()
    ... (55+ label types mapped)
         │
         ▼
[Validate: non-empty, changed from original, structurally coherent]
         │
         ▼
[Format as ChatML: system instruction + user input + assistant output]
```

**Results**: 99,994 valid pairs from Nvidia (6 skipped) + 209,231 from AI4Privacy (30 skipped) = **309,225 total training samples**.

### ChatML Format

Every training sample follows the Qwen ChatML template:

```
<|im_start|>system
You are an enterprise data privacy engine. Analyze the input text, identify all
Personally Identifiable Information (PII), and output the text with the PII seamlessly
replaced by realistic synthetic data. Maintain the exact original formatting, syntax,
and tone.<|im_end|>
<|im_start|>user
I, Jason, am applying for a financial services account. My date of birth is
1987-05-22. I live at 87 Avenida De La Estrella.<|im_end|>
<|im_start|>assistant
I, Jeffery, am applying for a financial services account. My date of birth is
1947-04-28. I live at 43321 Brittany Bypass.<|im_end|>
```

---

## Model Architecture & Fine-Tuning

### Base Model: Qwen2.5-0.5B-Instruct

Selected for its optimal balance of speed and linguistic capability at 500M parameters:

- **Architecture**: Dense Causal LM with RoPE (Rotary Position Embedding), SwiGLU activation, and Grouped-Query Attention (GQA)
- **Vocabulary**: 151,936 tokens (large vocab enables strong multilingual performance)
- **Context window**: 2,048 tokens (sufficient for document-level PII rewriting)
- **License**: Apache 2.0

### QLoRA Configuration

The base model weights are frozen with 4-bit NormalFloat (NF4) quantization. Low-Rank Adaptation (LoRA) matrices are injected across **all** linear projections:

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Rank (r) | 16 | Good capacity-to-memory ratio for 0.5B models |
| Alpha (α) | 16 | α/r = 1.0 effective scaling factor |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj | Full coverage for deep contextual rewriting |
| Dropout | 0 | Clean SFT data doesn't need dropout regularization |
| Gradient checkpointing | Unsloth optimized | 30% memory savings |
| Trainable parameters | 8,798,208 / 502,830,976 | 1.75% of total |

### Training Hyperparameters

| Parameter | Value |
|-----------|-------|
| Batch size | 64 per device |
| Gradient accumulation | 1 |
| Effective batch size | 64 |
| Epochs | 2 |
| Learning rate | 2e-4 |
| LR scheduler | Cosine decay |
| Warmup steps | 100 |
| Weight decay | 0.01 |
| Optimizer | AdamW 8-bit |
| Precision | bfloat16 |
| Seed | 3407 |

---

## Training Results

### Loss Curve

![Training Loss Curve](training_loss_curve.png)

The training loss shows healthy convergence:

- **Starting loss**: 2.65 (step 10)
- **Rapid descent**: 2.65 → 1.25 in the first 300 steps
- **Gradual refinement**: 1.25 → 1.00 over remaining steps
- **Final loss**: 1.0588 (stable, no oscillation)
- **No overfitting**: Loss continues decreasing smoothly through epoch 2

### Training Metrics

| Metric | Value |
|--------|-------|
| Final training loss | 1.0588 |
| Training runtime | 8,189 seconds (~2.3 hours) |
| Samples per second | 71.7 |
| Steps per second | 1.12 |
| Total FLOPs | 1.29 × 10¹⁸ |

---

## Inference Examples

Results from the post-training evaluation on 12 diverse PII scenarios:

| # | Category | Input | Output |
|---|----------|-------|--------|
| 1 | Names | Dear Mr. Arjun Mehta, your appointment with Dr. Priya Sharma is confirmed for July 15th. | Dear John Davis, your appointment with Dr. Michael Johnson is confirmed for 2006-04-18. |
| 2 | Emails | contact sarah.johnson@globalfinance.com or accounts@globalfinance.com | contact jason69@example.net or smithmichael@example.org |
| 3 | Phone | Call our Mumbai office at +91-22-4567-8901 | Call our Port Michaelborough office at 001-727-944-3626x015 |
| 4 | Address | Ship to 42 Baker Street, London, NW1 6XE, United Kingdom | Ship to 50783 Wilson Stream Suite 979, New York |
| 5 | National ID | Aadhaar ID 2345-6789-0123 issued to Neha Gupta | Aadhaar ID cHkYtWjJwQXz issued to Christopher Jones |
| 6 | Financial | Payment on Visa ending 4829. Ref: TXN-2024-09-17-0042 | Payment on Visa ending 4829. Ref: TXN-1963-12-15-0042 |
| 7 | Mixed PII | I'm David Chen (david.chen@techcorp.io, +1-415-555-0198) | I'm Michael Smith (kathleen32@example.com, 676-297-4529x992) |
| 8 | Passport | Passport L8472910 belonging to Maria Gonzalez | Passport xQyFZbWd belonging to Christopher Williams |
| 9 | Medical | Patient: Robert Williams, DOB: 1985-04-12, MRN: MED-2024-88451 | Patient: Michael Rodriguez, DOB: 1976-03-25, MRN: MED-2024-88451 |
| 10 | Employee | Name: Tanaka Yuki, SSN: 321-45-6789 | Name: Williams James, SSN: 458-78-3375 |
| 11 | Informal | Hey Lisa, it's Mike from the gym. Text me at 555-867-5309 | Hey Michael, it's David from the gym. Text me at 412.938.3297x641 |
| 12 | Hindi-English | Ramesh ji ka address hai 14, MG Road, Pune 411001 | Lori ji ka address hai 92953 Michael Plaza Suite 825 |

**Coherence check**: All 12 samples passed — no empty outputs, no placeholder tokens, all outputs structurally coherent with the input.

---

## Usage

### Quick Start — Test It in 30 Seconds

```python
# pip install transformers torch accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "AXONVERTEX-AI-RESEARCH/qwen2.5-0.5b-pii-anonymizer"

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def anonymize(text):
    """Anonymize PII in the given text and return the result."""
    messages = [
        {"role": "system", "content": (
            "You are an enterprise data privacy engine. Analyze the input text, identify all "
            "Personally Identifiable Information (PII), and output the text with the PII seamlessly "
            "replaced by realistic synthetic data. Maintain the exact original formatting, syntax, "
            "and tone."
        )},
        {"role": "user", "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)
    
    outputs = model.generate(
        inputs,
        max_new_tokens=512,
        temperature=0.3,
        top_p=0.9,
        do_sample=True,
    )
    return tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)

# Try it
result = anonymize("Hi, I'm John Doe. Email me at john.doe@acme.com or call +1-555-867-5309.")
print(result)
```

### Run the Full Test Suite — See Results Across 12 PII Categories

Copy and run this script to test the model against names, emails, phones, addresses, national IDs, financial data, passports, medical records, employee records, informal text, and multilingual input:

```python
# pip install transformers torch accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "AXONVERTEX-AI-RESEARCH/qwen2.5-0.5b-pii-anonymizer"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

SYSTEM_PROMPT = (
    "You are an enterprise data privacy engine. Analyze the input text, identify all "
    "Personally Identifiable Information (PII), and output the text with the PII seamlessly "
    "replaced by realistic synthetic data. Maintain the exact original formatting, syntax, "
    "and tone."
)

TEST_CASES = [
    ("Names",        "Dear Mr. Arjun Mehta, your appointment with Dr. Priya Sharma is confirmed for July 15th."),
    ("Emails",       "For billing inquiries, contact sarah.johnson@globalfinance.com or accounts@globalfinance.com."),
    ("Phones",       "Call our Mumbai office at +91-22-4567-8901 or reach Raj directly on 9876543210."),
    ("Addresses",    "Ship the package to 42 Baker Street, London, NW1 6XE, United Kingdom."),
    ("National ID",  "Aadhaar verification complete for ID 2345-6789-0123 issued to Neha Gupta."),
    ("Financial",    "Payment processed on Visa ending 4829. Transaction ref: TXN-2024-09-17-0042."),
    ("Mixed PII",    "Hi, I'm David Chen (david.chen@techcorp.io, +1-415-555-0198). Please update my records."),
    ("Passport",     "Passport number L8472910 belonging to Maria Gonzalez expires on 2027-03-22."),
    ("Medical",      "Patient: Robert Williams, DOB: 1985-04-12, MRN: MED-2024-88451. Prescribed metformin 500mg."),
    ("Employee",     "Employee ID: EMP-30291, Name: Tanaka Yuki, Department: Engineering, SSN: 321-45-6789."),
    ("Informal",     "Hey Lisa, it's Mike from the gym. Text me at 555-867-5309 about Saturday's class!"),
    ("Hindi-English", "Ramesh ji ka address hai 14, MG Road, Pune 411001. Unka number 9823456789 hai."),
]

def anonymize(text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)
    outputs = model.generate(inputs, max_new_tokens=512, temperature=0.3, top_p=0.9, do_sample=True)
    return tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)

print("=" * 80)
print("PII ANONYMIZER — FULL TEST SUITE")
print("=" * 80)

for i, (category, text) in enumerate(TEST_CASES, 1):
    result = anonymize(text)
    print(f"\n── {i}. {category} ──")
    print(f"  INPUT:  {text}")
    print(f"  OUTPUT: {result}")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
```

### With Unsloth (2× Faster Inference, 60% Less Memory)

```python
# pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="AXONVERTEX-AI-RESEARCH/qwen2.5-0.5b-pii-anonymizer",
    max_seq_length=2048,
    dtype=None,        # auto-detect
    load_in_4bit=True, # uses ~1.5GB VRAM
)
FastLanguageModel.for_inference(model)

SYSTEM_PROMPT = (
    "You are an enterprise data privacy engine. Analyze the input text, identify all "
    "Personally Identifiable Information (PII), and output the text with the PII seamlessly "
    "replaced by realistic synthetic data. Maintain the exact original formatting, syntax, "
    "and tone."
)

def anonymize(text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)
    outputs = model.generate(inputs, max_new_tokens=512, temperature=0.3, top_p=0.9, do_sample=True)
    return tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)

print(anonymize("Call Dr. Sarah Chen at +44-20-7946-0958 or email s.chen@hospital.nhs.uk"))
```

### Batch Processing — Anonymize Multiple Documents

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "AXONVERTEX-AI-RESEARCH/qwen2.5-0.5b-pii-anonymizer"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

SYSTEM_PROMPT = (
    "You are an enterprise data privacy engine. Analyze the input text, identify all "
    "Personally Identifiable Information (PII), and output the text with the PII seamlessly "
    "replaced by realistic synthetic data. Maintain the exact original formatting, syntax, "
    "and tone."
)

def anonymize(text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)
    outputs = model.generate(inputs, max_new_tokens=512, temperature=0.3, top_p=0.9, do_sample=True)
    return tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)

def anonymize_batch(texts):
    """Anonymize a list of texts and return results."""
    results = []
    for text in texts:
        results.append(anonymize(text))
    return results

# Example: process a list of customer support tickets
tickets = [
    "Customer Jane Smith (jane.smith@outlook.com) reported billing issue on account #4481-2290.",
    "Technician Raj Patel visited 15 Elm Street, Apt 3B. Contact: +91-98765-43210.",
    "Refund processed for order #ORD-2024-1847 to card ending 9012. Customer: Liu Wei.",
]

anonymized = anonymize_batch(tickets)
for original, cleaned in zip(tickets, anonymized):
    print(f"ORIGINAL: {original}")
    print(f"CLEANED:  {cleaned}")
    print()
```

### Process a File Line-by-Line

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "AXONVERTEX-AI-RESEARCH/qwen2.5-0.5b-pii-anonymizer"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

SYSTEM_PROMPT = (
    "You are an enterprise data privacy engine. Analyze the input text, identify all "
    "Personally Identifiable Information (PII), and output the text with the PII seamlessly "
    "replaced by realistic synthetic data. Maintain the exact original formatting, syntax, "
    "and tone."
)

def anonymize(text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)
    outputs = model.generate(inputs, max_new_tokens=512, temperature=0.3, top_p=0.9, do_sample=True)
    return tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)

input_file = "customer_data.txt"
output_file = "customer_data_anonymized.txt"

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line_num, line in enumerate(f_in, 1):
        line = line.strip()
        if not line:
            f_out.write("\n")
            continue
        cleaned = anonymize(line)
        f_out.write(cleaned + "\n")
        if line_num % 10 == 0:
            print(f"Processed {line_num} lines...")

print(f"Done. Anonymized output saved to {output_file}")
```

### Integration with Pandas DataFrames

```python
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

MODEL_NAME = "AXONVERTEX-AI-RESEARCH/qwen2.5-0.5b-pii-anonymizer"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

SYSTEM_PROMPT = (
    "You are an enterprise data privacy engine. Analyze the input text, identify all "
    "Personally Identifiable Information (PII), and output the text with the PII seamlessly "
    "replaced by realistic synthetic data. Maintain the exact original formatting, syntax, "
    "and tone."
)

def anonymize(text):
    if not isinstance(text, str) or not text.strip():
        return text
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)
    outputs = model.generate(inputs, max_new_tokens=512, temperature=0.3, top_p=0.9, do_sample=True)
    return tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)

# Load your data
df = pd.read_csv("customers.csv")

# Anonymize specific columns
tqdm.pandas(desc="Anonymizing")
df["name_clean"] = df["full_name"].progress_apply(anonymize)
df["email_clean"] = df["email"].progress_apply(anonymize)
df["notes_clean"] = df["support_notes"].progress_apply(anonymize)

# Save
df.to_csv("customers_anonymized.csv", index=False)
print(f"Anonymized {len(df)} rows.")
```

### Recommended Generation Parameters

| Parameter | Value | Why |
|-----------|-------|-----|
| temperature | 0.3 | Low randomness for consistent PII replacement |
| top_p | 0.9 | Nucleus sampling for natural-sounding output |
| max_new_tokens | 512 | Sufficient for most document chunks |
| do_sample | True | Required for temperature/top_p to take effect |

---

## Known Limitations

This is a Phase 1 model. Honest assessment of current limitations:

1. **Occasional artifact tokens**: Rare garbage tokens (e.g., "xQZo") can appear before synthetic names. Occurs in <5% of outputs.
2. **Over-replacement**: Sometimes replaces non-PII context (e.g., "Mumbai" → "Port Michaelborough", "Engineering" → "Engineer, technical sales"). The model can be too aggressive.
3. **Format-unaware replacements**: Aadhaar numbers replaced with non-numeric strings, postal codes with random characters. The model doesn't always respect the format constraints of specific ID types.
4. **Missed PII**: Card endings ("4829"), MRN numbers, and some phone numbers in Hindi-English text were not replaced.
5. **English-primary**: While the training data includes French, German, and Italian text, the model performs best on English. Multilingual coverage is inconsistent.
6. **No deterministic guarantees**: As a generative model, outputs can vary between runs. Not suitable as a sole compliance mechanism.

These limitations are precisely why Phase 2 adds Presidio as a pre/post-processing safety net.

---

## Phase 2 Roadmap

Phase 2 wraps this model in a production-ready serving architecture:

```
[Raw Text Input]
       │
       ▼
[Microsoft Presidio Analyzer]  →  Detect PII with high-precision rules
       │
       ▼
[GLiNER NER Model]  →  Catch contextual PII that rules miss
       │
       ▼
[This Fine-Tuned Model]  →  Generate natural synthetic replacements
       │
       ▼
[Presidio Analyzer (2nd pass)]  →  Verify no PII leaked through
       │
       ▼
[Clean Output via FastAPI]
```

- Presidio handles the "don't miss anything" job (structured PII: SSNs, credit cards, IBANs)
- GLiNER handles contextual entity recognition
- This model handles the "make it read naturally" job
- The second Presidio pass acts as a compliance safety net

---

## License

This model is released under a **composite license** reflecting the licenses of all components used in training. See [LICENSE.md](LICENSE.md) for complete terms.

| Component | License | Commercial Use |
|-----------|---------|----------------|
| Qwen2.5-0.5B-Instruct (base model) | Apache 2.0 | Yes |
| nvidia/Nemotron-PII (dataset) | CC-BY-4.0 | Yes, with attribution |
| ai4privacy/pii-masking-200k (dataset) | AI4Privacy Free/Corporate License | Free for individuals and small businesses (≤3 employees). Larger organizations require a corporate license from licensing@ai4privacy.com |
| Unsloth (training framework) | Apache 2.0 | Yes |
| Model weights (this repository) | Subject to the most restrictive upstream license | See LICENSE.md |

**Important**: If you are a commercial entity with more than 3 employees, you must obtain a corporate license from AI4Privacy before using this model in production. Contact licensing@ai4privacy.com.

---

## Citation

If you use this model in your research or products, please cite:

```bibtex
@misc{qwen25-pii-anonymizer-2025,
  title={Qwen2.5-0.5B PII Anonymizer: Context-Aware Synthetic PII Rewriting via QLoRA},
  year={2025},
  publisher={HuggingFace},
  url={https://huggingface.co/AXONVERTEX-AI-RESEARCH/qwen2.5-0.5b-pii-anonymizer}
}
```

Please also cite the upstream datasets:

```bibtex
@dataset{nvidia_nemotron_pii_2024,
  title={Nemotron-PII: Synthetic Persona-Grounded PII/PHI Detection Dataset},
  author={NVIDIA},
  year={2024},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/nvidia/Nemotron-PII},
  license={CC-BY-4.0}
}

@dataset{ai4privacy_pii_masking_200k_2023,
  title={PII Masking 200K Dataset},
  author={AI4Privacy (Ai Suisse SA)},
  year={2023},
  publisher={HuggingFace},
  doi={10.57967/hf/1532},
  url={https://huggingface.co/datasets/ai4privacy/pii-masking-200k}
}
```

---

## Acknowledgments

- **[Qwen Team (Alibaba Cloud)](https://github.com/QwenLM)** for the Qwen2.5 base model family
- **[NVIDIA](https://huggingface.co/nvidia)** for the Nemotron-PII dataset and NeMo Data Designer
- **[AI4Privacy (Ai Suisse SA)](https://huggingface.co/ai4privacy)** for the PII Masking 200K dataset
- **[Unsloth](https://github.com/unslothai/unsloth)** for the optimized QLoRA training framework
- **[Faker](https://faker.readthedocs.io/)** for synthetic data generation during data engineering
- **[HuggingFace](https://huggingface.co)** for the Transformers, TRL, and Datasets libraries
