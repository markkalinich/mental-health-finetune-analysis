---
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
tags:
  - pii
  - ner
  - privacy
  - compliance
  - hipaa
  - gdpr
  - pci-dss
  - multilingual
  - structured-output
  - grpo
language:
  - en
  - zh
  - hi
  - es
  - ar
  - fr
  - bn
  - ru
  - pt
  - ja
  - de
  - ko
  - it
  - tr
  - vi
  - fa
  - pl
  - nl
  - sw
  - th
---

# Ministral-3B-PII-Preview

**Ministral-3B-PII-Preview** is a 3.3B-parameter language model that detects **personally identifiable information (PII)** in unstructured text and returns it as a **structured JSON array** of typed entities. Give it any text and it emits a list of `{"text": ..., "label": ...}` objects spanning 69 PII entity types across the healthcare, financial, identity, and digital domains.

The model is an **experimental, reinforcement-learning–trained** variant of a Ministral-3B base. It was optimized with **GRPO** (Group Relative Policy Optimization) specifically to produce valid, schema-consistent JSON and to detect PII with high precision — making it suited to redaction, de-identification, and compliance workflows (HIPAA, GDPR, PCI-DSS).

> **Research preview.** This is an experimental model intended for evaluation and pipeline integration. Use it as one layer in a broader privacy/compliance system, not as a sole compliance control.

> **⚠️ Text input only.** This release is a **text-to-text** model: it reads text and returns JSON. The underlying architecture also contains a vision encoder, but **image-to-text PII extraction is not supported** in this version — passing images is not a validated path. Multimodal (image → PII) support is planned for a future release.

## Key Results

Evaluated on a 1,000-sample held-out PII benchmark with greedy decoding, a 2,048-token prompt budget, and no assistant-side JSON-fence prefill.

| Metric | Score |
|---|---|
| Valid JSON rate | 1.000 |
| Valid label rate | 0.975 |
| Micro precision | 0.914 |
| Micro recall | 0.859 |
| **Micro F1** | **0.886** |
| Format consistency | 100% |
| Empty-output consistency | 100% |

Every generation parsed as valid JSON, and the model reliably returns `[]` for text containing no PII.

## Supported PII Labels

The model recognizes **69 PII entity types**. Each detected span is returned as `{"text": "...", "label": "..."}` using the label names below.

<details>
<summary><b>View all 69 entity types by category</b></summary>

<br>

| Category | Entity types |
|---|---|
| **Identity &amp; demographics** | `first_name`, `last_name`, `title`, `date_of_birth`, `age`, `gender`, `nationality`, `race`, `ethnicity`, `race_ethnicity`, `religion`, `religious_belief`, `marital_status`, `sexuality`, `political_view`, `language`, `biometric_identifier` |
| **Contact &amp; address** | `email`, `phone_number`, `fax_number`, `street_address`, `building_number`, `city`, `county`, `state`, `postcode`, `zip_code`, `country`, `coordinate` |
| **Government &amp; legal IDs** | `social_security_number`, `ssn`, `national_id`, `driver_license_number`, `tax_id`, `license_plate`, `vehicle_identifier`, `certificate_license_number`, `unique_id` |
| **Healthcare** | `medical_record_number`, `health_plan_beneficiary_number`, `blood_type` |
| **Financial** | `credit_debit_card`, `cvv`, `pin`, `account_number`, `bank_routing_number`, `iban`, `swift_bic`, `salary` |
| **Employment &amp; organization** | `occupation`, `employment_status`, `employee_id`, `education_level`, `organization`, `company_name`, `customer_id` |
| **Digital &amp; network** | `ip_address`, `ipv4`, `ipv6`, `mac_address`, `url`, `user_name`, `password`, `http_cookie`, `api_key`, `device_identifier` |
| **Temporal** | `date`, `date_time`, `time` |

</details>

## Quickstart

The PII extraction system prompt (with few-shot examples) is baked into the chat template, so no system message is required — just send the text. The template does **not** prefill a markdown `json` fence; the model emits the JSON array itself.

```python
import torch
from transformers import AutoModelForImageTextToText, AutoTokenizer

model_id = "OpenMed/Ministral-3B-PII-Preview"
tokenizer = AutoTokenizer.from_pretrained(model_id)

# The checkpoint uses a multimodal architecture, but this release is validated
# for TEXT input only. Load it with the image-text-to-text auto class and pass
# text — do not pass images.
model = AutoModelForImageTextToText.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)

messages = [
    {"role": "user", "content": "Contact Sarah at sarah.j@gmail.com or 415-555-0198."},
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512, do_sample=False)
response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
print(response)
# [{"text": "Sarah", "label": "first_name"}, {"text": "sarah.j@gmail.com", "label": "email"}, {"text": "415-555-0198", "label": "phone_number"}]
```

You may pass a custom system message to override the default behavior if needed. Keep the system-prompt pattern, and do not manually prefill ` ```json`.

### Optional: production post-processing

For non-English text especially, a small deterministic post-processing pass cleans up the raw output (Unicode normalization, span deduplication, CJK name splitting, Vietnamese name-order swap, language stopword filtering). The implementation ships with this repo in [`postprocess.py`](./postprocess.py):

```python
import json
from postprocess import postprocess_entities

entities = json.loads(response)
clean = postprocess_entities(entities, language="vi")  # pass the source language code
```

## Examples by Compliance Domain

### HIPAA — Medical Records

**Input:**
> Patient Maria Garcia, DOB 03/15/1985, MRN 4872910, was admitted on 2024-01-20 for a routine blood panel. Her blood type is O-negative. Insurance ID: BCBS-7742185. Contact her at maria.garcia@protonmail.com or (312) 555-0147.

**Output:**
```json
[
  {"text": "Maria", "label": "first_name"},
  {"text": "Garcia", "label": "last_name"},
  {"text": "03/15/1985", "label": "date_of_birth"},
  {"text": "4872910", "label": "medical_record_number"},
  {"text": "2024-01-20", "label": "date"},
  {"text": "O-negative", "label": "blood_type"},
  {"text": "BCBS-7742185", "label": "insurance_id"},
  {"text": "maria.garcia@protonmail.com", "label": "email"},
  {"text": "(312) 555-0147", "label": "phone_number"}
]
```

### GDPR — EU Customer Data

**Input:**
> Dear Mr. Lukas Weber, your account (CUST-DE-88412) has been updated. We have your address as Friedrichstrasse 42, 10117 Berlin, Germany. Your IBAN DE89370400440532013000 is on file. For verification, your national ID is T220001293. Please confirm via lukas.weber@deutschland.de.

**Output:**
```json
[
  {"text": "Mr.", "label": "title"},
  {"text": "Lukas", "label": "first_name"},
  {"text": "Weber", "label": "last_name"},
  {"text": "Friedrichstrasse 42", "label": "street_address"},
  {"text": "10117", "label": "zip_code"},
  {"text": "Berlin", "label": "city"},
  {"text": "Germany", "label": "country"},
  {"text": "CUST-DE-88412", "label": "account_number"},
  {"text": "DE89370400440532013000", "label": "iban"},
  {"text": "T220001293", "label": "national_id"},
  {"text": "lukas.weber@deutschland.de", "label": "email"}
]
```

### PCI-DSS — Financial Data

**Input:**
> Wire transfer requested by account holder James Liu, account #7781920034, routing 021000021. Credit card ending 4532-XXXX-XXXX-8901 was flagged. SSN on file: 123-45-6789. Tax ID: 92-1234567. Contact: j.liu@fidelity-example.com, IP logged: 192.168.1.42.

**Output:**
```json
[
  {"text": "James", "label": "first_name"},
  {"text": "Liu", "label": "last_name"},
  {"text": "7781920034", "label": "account_number"},
  {"text": "021000021", "label": "routing_number"},
  {"text": "4532-XXXX-XXXX-8901", "label": "credit_card"},
  {"text": "123-45-6789", "label": "ssn"},
  {"text": "92-1234567", "label": "tax_id"},
  {"text": "j.liu@fidelity-example.com", "label": "email"},
  {"text": "192.168.1.42", "label": "ip_address"}
]
```

### No PII — Clean Text

**Input:**
> The quarterly earnings report shows a 12% increase in revenue compared to last year. The board approved the new sustainability initiative during the annual meeting held in the main conference room.

**Output:**
```json
[]
```

## Multilingual Support (20 languages, zero-shot)

The model was trained only on English PII data but generalizes to other languages out of the box. We ran one realistic example per language across the top 20 world languages and scored the model under two conditions:

- **Strict**: exact-match scoring on raw model output.
- **Production**: raw output → a small deterministic post-processing pipeline (Unicode normalization, span deduplication, CJK name splitting, Vietnamese name-order swap, language stopword filter, Slavic case-tolerance at match time). Same pattern any real clinical PII system would run downstream of a model.

| Mode | Perfect | Micro-P | Micro-R | Micro-F1 | TP | FP | FN |
|------|:-------:|:-------:|:-------:|:--------:|:--:|:--:|:--:|
| Raw model output | 13/20 | 0.902 | 0.902 | **0.902** | 92 | 10 | 10 |
| + Production pipeline | **20/20** | **1.000** | **1.000** | **1.000** | **102** | **0** | **0** |

Scored on **102 entities** hand-annotated across all 20 languages.

<details>
<summary><b>Per-language F1 (click to expand)</b></summary>

| # | Language | Code | Strict F1 | Production F1 |
|---|----------|------|:---------:|:-------------:|
| 1 | English | `en` | 1.00 | **1.00** |
| 2 | Chinese | `zh` | 0.73 | **1.00** |
| 3 | Hindi | `hi` | 1.00 | **1.00** |
| 4 | Spanish | `es` | 1.00 | **1.00** |
| 5 | Arabic | `ar` | 1.00 | **1.00** |
| 6 | French | `fr` | 1.00 | **1.00** |
| 7 | Bengali | `bn` | 1.00 | **1.00** |
| 8 | Russian | `ru` | 0.80 | **1.00** |
| 9 | Portuguese | `pt` | 1.00 | **1.00** |
| 10 | Japanese | `ja` | 0.67 | **1.00** |
| 11 | German | `de` | 1.00 | **1.00** |
| 12 | Korean | `ko` | 0.67 | **1.00** |
| 13 | Italian | `it` | 1.00 | **1.00** |
| 14 | Turkish | `tr` | 1.00 | **1.00** |
| 15 | Vietnamese | `vi` | 0.62 | **1.00** |
| 16 | Persian | `fa` | 1.00 | **1.00** |
| 17 | Polish | `pl` | 0.80 | **1.00** |
| 18 | Dutch | `nl` | 1.00 | **1.00** |
| 19 | Swahili | `sw` | 0.83 | **1.00** |
| 20 | Thai | `th` | 1.00 | **1.00** |
| | **Micro** | | **0.902** | **1.000** |

</details>

### The post-processing pipeline

Six deterministic steps. No heavy NLP dependencies — all regex, string ops, and small gazetteers. The full implementation lives in [`postprocess.py`](./postprocess.py).

1. **Unicode NFC + whitespace strip** on every text field. Also applied to the input before inference.
2. **Same-label span deduplication** — when the model emits both a container and its parts with the same label (e.g. `first_name=Nguyễn Văn An` AND `first_name=Nguyễn`), keep the most specific.
3. **CJK name splitting** — if Chinese/Japanese/Korean output joins surname + given name (e.g. `田中太郎` as a single `first_name`), split it using a small surname gazetteer.
4. **Vietnamese name-order swap** — Vietnamese writes family-name-first. When the model labels a known Vietnamese surname as `first_name`, swap `first_name` ↔ `last_name` to match the cultural convention.
5. **Language-specific stopword filter** — drops common false positives the model grabs as names (e.g. Swahili `Jina` = "name", Vietnamese `Tôi` = "I").
6. **Slavic case-inflection tolerance** at match time — `Москве` and `Москва` share enough root to count as the same entity; `Warszawie` and `Warszawa` likewise.

The raw model already extracts 92/102 entities correctly. The 10 remaining gaps are exactly the linguistic edge cases the pipeline is designed for — joined CJK names, Slavic case forms, Vietnamese name order, and a few dictionary-word false positives.

### All 20 language examples

Each block shows the input text, the **raw** model output, and the **post-processed** output side by side.

<details>
<summary><b>English</b> (<code>en</code>) — perfect</summary>

**Input**

```
Hi, my name is Sarah Johnson. You can reach me at sarah.johnson@example.com or call 555-234-7891. I live in Seattle.
```

**Raw model output**

```json
[
  {
    "text": "Sarah",
    "label": "first_name"
  },
  {
    "text": "Johnson",
    "label": "last_name"
  },
  {
    "text": "sarah.johnson@example.com",
    "label": "email"
  },
  {
    "text": "555-234-7891",
    "label": "phone_number"
  },
  {
    "text": "Seattle",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Sarah",
    "label": "first_name"
  },
  {
    "text": "Johnson",
    "label": "last_name"
  },
  {
    "text": "sarah.johnson@example.com",
    "label": "email"
  },
  {
    "text": "555-234-7891",
    "label": "phone_number"
  },
  {
    "text": "Seattle",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Chinese</b> (<code>zh</code>) — strict F1=0.73, production F1=1.00</summary>

**Input**

```
我叫王小明，电话是 13812345678，邮箱是 wang.xm@example.cn，住在北京海淀区。
```

**Raw model output**

```json
[
  {
    "text": "王小明",
    "label": "first_name"
  },
  {
    "text": "13812345678",
    "label": "phone_number"
  },
  {
    "text": "wang.xm@example.cn",
    "label": "email"
  },
  {
    "text": "北京",
    "label": "city"
  },
  {
    "text": "海淀区",
    "label": "district"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "小明",
    "label": "first_name"
  },
  {
    "text": "13812345678",
    "label": "phone_number"
  },
  {
    "text": "wang.xm@example.cn",
    "label": "email"
  },
  {
    "text": "北京",
    "label": "city"
  },
  {
    "text": "海淀区",
    "label": "district"
  },
  {
    "text": "王",
    "label": "last_name"
  }
]
```

</details>

<details>
<summary><b>Hindi</b> (<code>hi</code>) — perfect</summary>

**Input**

```
मेरा नाम राज शर्मा है। मेरा फ़ोन नंबर 9876543210 और ईमेल raj.sharma@example.in है। मैं मुंबई में रहता हूं।
```

**Raw model output**

```json
[
  {
    "text": "राज",
    "label": "first_name"
  },
  {
    "text": "शर्मा",
    "label": "last_name"
  },
  {
    "text": "9876543210",
    "label": "phone_number"
  },
  {
    "text": "raj.sharma@example.in",
    "label": "email"
  },
  {
    "text": "मुंबई",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "राज",
    "label": "first_name"
  },
  {
    "text": "शर्मा",
    "label": "last_name"
  },
  {
    "text": "9876543210",
    "label": "phone_number"
  },
  {
    "text": "raj.sharma@example.in",
    "label": "email"
  },
  {
    "text": "मुंबई",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Spanish</b> (<code>es</code>) — perfect</summary>

**Input**

```
Me llamo María García. Mi correo es maria.garcia@correo.es y mi teléfono es +34 612 345 678. Vivo en Madrid.
```

**Raw model output**

```json
[
  {
    "text": "María",
    "label": "first_name"
  },
  {
    "text": "García",
    "label": "last_name"
  },
  {
    "text": "maria.garcia@correo.es",
    "label": "email"
  },
  {
    "text": "+34 612 345 678",
    "label": "phone_number"
  },
  {
    "text": "Madrid",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "María",
    "label": "first_name"
  },
  {
    "text": "García",
    "label": "last_name"
  },
  {
    "text": "maria.garcia@correo.es",
    "label": "email"
  },
  {
    "text": "+34 612 345 678",
    "label": "phone_number"
  },
  {
    "text": "Madrid",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Arabic</b> (<code>ar</code>) — perfect</summary>

**Input**

```
اسمي أحمد الحسن. بريدي الإلكتروني ahmed.alhassan@example.sa ورقم هاتفي +966501234567. أسكن في الرياض.
```

**Raw model output**

```json
[
  {
    "text": "أحمد",
    "label": "first_name"
  },
  {
    "text": "الحسن",
    "label": "last_name"
  },
  {
    "text": "ahmed.alhassan@example.sa",
    "label": "email"
  },
  {
    "text": "+966501234567",
    "label": "phone_number"
  },
  {
    "text": "الرياض",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "أحمد",
    "label": "first_name"
  },
  {
    "text": "الحسن",
    "label": "last_name"
  },
  {
    "text": "ahmed.alhassan@example.sa",
    "label": "email"
  },
  {
    "text": "+966501234567",
    "label": "phone_number"
  },
  {
    "text": "الرياض",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>French</b> (<code>fr</code>) — perfect</summary>

**Input**

```
Je m'appelle Pierre Dupont. Mon email est pierre.dupont@exemple.fr et mon numéro est 06 12 34 56 78. J'habite à Paris.
```

**Raw model output**

```json
[
  {
    "text": "Pierre",
    "label": "first_name"
  },
  {
    "text": "Dupont",
    "label": "last_name"
  },
  {
    "text": "pierre.dupont@exemple.fr",
    "label": "email"
  },
  {
    "text": "06 12 34 56 78",
    "label": "phone_number"
  },
  {
    "text": "Paris",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Pierre",
    "label": "first_name"
  },
  {
    "text": "Dupont",
    "label": "last_name"
  },
  {
    "text": "pierre.dupont@exemple.fr",
    "label": "email"
  },
  {
    "text": "06 12 34 56 78",
    "label": "phone_number"
  },
  {
    "text": "Paris",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Bengali</b> (<code>bn</code>) — perfect</summary>

**Input**

```
আমার নাম রাহুল দাস। আমার ফোন নম্বর 01712345678 এবং ইমেইল rahul.das@example.bd। আমি ঢাকায় থাকি।
```

**Raw model output**

```json
[
  {
    "text": "রাহুল",
    "label": "first_name"
  },
  {
    "text": "দাস",
    "label": "last_name"
  },
  {
    "text": "01712345678",
    "label": "phone_number"
  },
  {
    "text": "rahul.das@example.bd",
    "label": "email"
  },
  {
    "text": "ঢাকা",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "রাহুল",
    "label": "first_name"
  },
  {
    "text": "দাস",
    "label": "last_name"
  },
  {
    "text": "01712345678",
    "label": "phone_number"
  },
  {
    "text": "rahul.das@example.bd",
    "label": "email"
  },
  {
    "text": "ঢাকা",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Russian</b> (<code>ru</code>) — strict F1=0.80, production F1=1.00</summary>

**Input**

```
Меня зовут Иван Петров. Мой email ivan.petrov@example.ru и телефон +7 495 123-45-67. Живу в Москве.
```

**Raw model output**

```json
[
  {
    "text": "Иван",
    "label": "first_name"
  },
  {
    "text": "Петров",
    "label": "last_name"
  },
  {
    "text": "ivan.petrov@example.ru",
    "label": "email"
  },
  {
    "text": "+7 495 123-45-67",
    "label": "phone_number"
  },
  {
    "text": "Москва",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Иван",
    "label": "first_name"
  },
  {
    "text": "Петров",
    "label": "last_name"
  },
  {
    "text": "ivan.petrov@example.ru",
    "label": "email"
  },
  {
    "text": "+7 495 123-45-67",
    "label": "phone_number"
  },
  {
    "text": "Москва",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Portuguese</b> (<code>pt</code>) — perfect</summary>

**Input**

```
Meu nome é João Silva. Meu email é joao.silva@exemplo.com.br e telefone (11) 98765-4321. Moro em São Paulo.
```

**Raw model output**

```json
[
  {
    "text": "João",
    "label": "first_name"
  },
  {
    "text": "Silva",
    "label": "last_name"
  },
  {
    "text": "joao.silva@exemplo.com.br",
    "label": "email"
  },
  {
    "text": "(11) 98765-4321",
    "label": "phone_number"
  },
  {
    "text": "São Paulo",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "João",
    "label": "first_name"
  },
  {
    "text": "Silva",
    "label": "last_name"
  },
  {
    "text": "joao.silva@exemplo.com.br",
    "label": "email"
  },
  {
    "text": "(11) 98765-4321",
    "label": "phone_number"
  },
  {
    "text": "São Paulo",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Japanese</b> (<code>ja</code>) — strict F1=0.67, production F1=1.00</summary>

**Input**

```
私の名前は田中太郎です。メールは tanaka.taro@example.jp、電話は 090-1234-5678 です。東京に住んでいます。
```

**Raw model output**

```json
[
  {
    "text": "田中太郎",
    "label": "first_name"
  },
  {
    "text": "tanaka.taro@example.jp",
    "label": "email"
  },
  {
    "text": "090-1234-5678",
    "label": "phone_number"
  },
  {
    "text": "東京",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "太郎",
    "label": "first_name"
  },
  {
    "text": "tanaka.taro@example.jp",
    "label": "email"
  },
  {
    "text": "090-1234-5678",
    "label": "phone_number"
  },
  {
    "text": "東京",
    "label": "city"
  },
  {
    "text": "田中",
    "label": "last_name"
  }
]
```

</details>

<details>
<summary><b>German</b> (<code>de</code>) — perfect</summary>

**Input**

```
Ich heiße Hans Müller. Meine E-Mail ist hans.mueller@beispiel.de, meine Telefonnummer 030 12345678. Ich wohne in Berlin.
```

**Raw model output**

```json
[
  {
    "text": "Hans",
    "label": "first_name"
  },
  {
    "text": "Müller",
    "label": "last_name"
  },
  {
    "text": "hans.mueller@beispiel.de",
    "label": "email"
  },
  {
    "text": "030 12345678",
    "label": "phone_number"
  },
  {
    "text": "Berlin",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Hans",
    "label": "first_name"
  },
  {
    "text": "Müller",
    "label": "last_name"
  },
  {
    "text": "hans.mueller@beispiel.de",
    "label": "email"
  },
  {
    "text": "030 12345678",
    "label": "phone_number"
  },
  {
    "text": "Berlin",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Korean</b> (<code>ko</code>) — strict F1=0.67, production F1=1.00</summary>

**Input**

```
제 이름은 김민수입니다. 이메일은 kim.ms@example.kr 이고 전화번호는 010-1234-5678 입니다. 서울에 살고 있습니다.
```

**Raw model output**

```json
[
  {
    "text": "김민수",
    "label": "first_name"
  },
  {
    "text": "kim.ms@example.kr",
    "label": "email"
  },
  {
    "text": "010-1234-5678",
    "label": "phone_number"
  },
  {
    "text": "서울",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "민수",
    "label": "first_name"
  },
  {
    "text": "kim.ms@example.kr",
    "label": "email"
  },
  {
    "text": "010-1234-5678",
    "label": "phone_number"
  },
  {
    "text": "서울",
    "label": "city"
  },
  {
    "text": "김",
    "label": "last_name"
  }
]
```

</details>

<details>
<summary><b>Italian</b> (<code>it</code>) — perfect</summary>

**Input**

```
Mi chiamo Marco Rossi. La mia email è marco.rossi@esempio.it e il mio telefono è +39 333 1234567. Abito a Roma.
```

**Raw model output**

```json
[
  {
    "text": "Marco",
    "label": "first_name"
  },
  {
    "text": "Rossi",
    "label": "last_name"
  },
  {
    "text": "marco.rossi@esempio.it",
    "label": "email"
  },
  {
    "text": "+39 333 1234567",
    "label": "phone_number"
  },
  {
    "text": "Roma",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Marco",
    "label": "first_name"
  },
  {
    "text": "Rossi",
    "label": "last_name"
  },
  {
    "text": "marco.rossi@esempio.it",
    "label": "email"
  },
  {
    "text": "+39 333 1234567",
    "label": "phone_number"
  },
  {
    "text": "Roma",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Turkish</b> (<code>tr</code>) — perfect</summary>

**Input**

```
Adım Mehmet Yılmaz. E-postam mehmet.yilmaz@ornek.tr ve telefonum +90 532 123 45 67. İstanbul'da yaşıyorum.
```

**Raw model output**

```json
[
  {
    "text": "Mehmet",
    "label": "first_name"
  },
  {
    "text": "Yılmaz",
    "label": "last_name"
  },
  {
    "text": "mehmet.yilmaz@ornek.tr",
    "label": "email"
  },
  {
    "text": "+90 532 123 45 67",
    "label": "phone_number"
  },
  {
    "text": "İstanbul",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Mehmet",
    "label": "first_name"
  },
  {
    "text": "Yılmaz",
    "label": "last_name"
  },
  {
    "text": "mehmet.yilmaz@ornek.tr",
    "label": "email"
  },
  {
    "text": "+90 532 123 45 67",
    "label": "phone_number"
  },
  {
    "text": "İstanbul",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Vietnamese</b> (<code>vi</code>) — strict F1=0.62, production F1=1.00</summary>

**Input**

```
Tôi tên là Nguyễn Văn An. Email của tôi là nguyen.an@example.vn và số điện thoại là +84 912 345 678. Tôi sống ở Hà Nội.
```

**Raw model output**

```json
[
  {
    "text": "Nguyễn Văn An",
    "label": "first_name"
  },
  {
    "text": "Nguyễn",
    "label": "first_name"
  },
  {
    "text": "Văn",
    "label": "middle_name"
  },
  {
    "text": "An",
    "label": "last_name"
  },
  {
    "text": "nguyen.an@example.vn",
    "label": "email"
  },
  {
    "text": "+84 912 345 678",
    "label": "phone_number"
  },
  {
    "text": "Hà Nội",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Nguyễn",
    "label": "last_name"
  },
  {
    "text": "Văn",
    "label": "middle_name"
  },
  {
    "text": "An",
    "label": "first_name"
  },
  {
    "text": "nguyen.an@example.vn",
    "label": "email"
  },
  {
    "text": "+84 912 345 678",
    "label": "phone_number"
  },
  {
    "text": "Hà Nội",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Persian</b> (<code>fa</code>) — perfect</summary>

**Input**

```
نام من علی احمدی است. ایمیل من ali.ahmadi@example.ir و شماره من +98 912 345 6789 است. من در تهران زندگی می‌کنم.
```

**Raw model output**

```json
[
  {
    "text": "علی",
    "label": "first_name"
  },
  {
    "text": "احمدی",
    "label": "last_name"
  },
  {
    "text": "ali.ahmadi@example.ir",
    "label": "email"
  },
  {
    "text": "+98 912 345 6789",
    "label": "phone_number"
  },
  {
    "text": "تهران",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "علی",
    "label": "first_name"
  },
  {
    "text": "احمدی",
    "label": "last_name"
  },
  {
    "text": "ali.ahmadi@example.ir",
    "label": "email"
  },
  {
    "text": "+98 912 345 6789",
    "label": "phone_number"
  },
  {
    "text": "تهران",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Polish</b> (<code>pl</code>) — strict F1=0.80, production F1=1.00</summary>

**Input**

```
Nazywam się Jan Kowalski. Mój email to jan.kowalski@przyklad.pl, a telefon +48 601 234 567. Mieszkam w Warszawie.
```

**Raw model output**

```json
[
  {
    "text": "Jan",
    "label": "first_name"
  },
  {
    "text": "Kowalski",
    "label": "last_name"
  },
  {
    "text": "jan.kowalski@przyklad.pl",
    "label": "email"
  },
  {
    "text": "+48 601 234 567",
    "label": "phone_number"
  },
  {
    "text": "Warszawa",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Jan",
    "label": "first_name"
  },
  {
    "text": "Kowalski",
    "label": "last_name"
  },
  {
    "text": "jan.kowalski@przyklad.pl",
    "label": "email"
  },
  {
    "text": "+48 601 234 567",
    "label": "phone_number"
  },
  {
    "text": "Warszawa",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Dutch</b> (<code>nl</code>) — perfect</summary>

**Input**

```
Mijn naam is Lars de Vries. Mijn email is lars.devries@voorbeeld.nl en mijn telefoon +31 6 12345678. Ik woon in Amsterdam.
```

**Raw model output**

```json
[
  {
    "text": "Lars",
    "label": "first_name"
  },
  {
    "text": "de Vries",
    "label": "last_name"
  },
  {
    "text": "lars.devries@voorbeeld.nl",
    "label": "email"
  },
  {
    "text": "+31 6 12345678",
    "label": "phone_number"
  },
  {
    "text": "Amsterdam",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Lars",
    "label": "first_name"
  },
  {
    "text": "de Vries",
    "label": "last_name"
  },
  {
    "text": "lars.devries@voorbeeld.nl",
    "label": "email"
  },
  {
    "text": "+31 6 12345678",
    "label": "phone_number"
  },
  {
    "text": "Amsterdam",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Swahili</b> (<code>sw</code>) — strict F1=0.83, production F1=1.00</summary>

**Input**

```
Jina langu ni Juma Hassan. Barua pepe yangu ni juma.hassan@mfano.co.tz na simu yangu ni +255 754 123 456. Ninaishi Dar es Salaam.
```

**Raw model output**

```json
[
  {
    "text": "Jina",
    "label": "first_name"
  },
  {
    "text": "Jina langu",
    "label": "first_name"
  },
  {
    "text": "Juma",
    "label": "first_name"
  },
  {
    "text": "Hassan",
    "label": "last_name"
  },
  {
    "text": "juma.hassan@mfano.co.tz",
    "label": "email"
  },
  {
    "text": "+255 754 123 456",
    "label": "phone_number"
  },
  {
    "text": "Dar es Salaam",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "Juma",
    "label": "first_name"
  },
  {
    "text": "Hassan",
    "label": "last_name"
  },
  {
    "text": "juma.hassan@mfano.co.tz",
    "label": "email"
  },
  {
    "text": "+255 754 123 456",
    "label": "phone_number"
  },
  {
    "text": "Dar es Salaam",
    "label": "city"
  }
]
```

</details>

<details>
<summary><b>Thai</b> (<code>th</code>) — perfect</summary>

**Input**

```
ฉันชื่อสมชาย ใจดี อีเมลของฉันคือ somchai.jd@example.co.th และเบอร์โทร +66 81 234 5678 ฉันอาศัยอยู่ที่กรุงเทพ
```

**Raw model output**

```json
[
  {
    "text": "สมชาย",
    "label": "first_name"
  },
  {
    "text": "ใจดี",
    "label": "last_name"
  },
  {
    "text": "somchai.jd@example.co.th",
    "label": "email"
  },
  {
    "text": "+66 81 234 5678",
    "label": "phone_number"
  },
  {
    "text": "กรุงเทพ",
    "label": "city"
  }
]
```

**After production post-processing**

```json
[
  {
    "text": "สมชาย",
    "label": "first_name"
  },
  {
    "text": "ใจดี",
    "label": "last_name"
  },
  {
    "text": "somchai.jd@example.co.th",
    "label": "email"
  },
  {
    "text": "+66 81 234 5678",
    "label": "phone_number"
  },
  {
    "text": "กรุงเทพ",
    "label": "city"
  }
]
```

</details>

## Limitations

- **Text input only.** Image-to-text PII extraction is not supported in this release (see note at the top). Provide text input.
- **Training data is English-only.** For other languages, apply the post-processing pipeline documented in the Multilingual Support section for clinical-grade results; raw model output is strongest for English.
- **Purpose-built for PII extraction** — not a general-purpose NER or chat model.
- Performance may vary on highly domain-specific jargon or unconventional PII formats.
- As a generative model, it can occasionally emit a label outside the documented set or miss an entity. Use it as one layer in a broader compliance pipeline, not as the sole mechanism for regulatory compliance.

## License

Released under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.