---
language:
  - ko
license: apache-2.0
base_model: Qwen/Qwen3-4B
tags:
  - sentinel-solution
  - dlp
  - guardrails
  - pii
  - secrets
  - korean
  - synthetic-data
pipeline_tag: token-classification
library_name: transformers
model-index:
  - name: sentinel-qwen3-4b-kr-sensitive-guard-v3
    results: []
---

# sentinel-qwen3-4b-kr-sensitive-guard-v3

## Overview
**sentinel-qwen3-4b-kr-sensitive-guard-v3** is a Korean guardrail-oriented model fine-tuned from **Qwen/Qwen3-4B** to detect **sensitive entities** using a **strict whitelist-only** label set.

This repository provides the **merged full-weight model** (LoRA adapter merged into the base model) for straightforward deployment.

## Intended Use
- Detect sensitive information in Korean text (e.g., prompts, chat messages, logs) **before** sending content to external LLM services.
- Build enterprise DLP / LLM guardrails (warn / block / mask / redact).
- Extract sensitive entities using a fixed whitelist of labels (no extra categories).

## Not Intended Use
- Real-person identification, re-identification, or privacy-invasive profiling.
- Treating model outputs as ground truth without validation.
- Assuming real-world distributions (training used synthetic data; domain shift may occur).

## Training Data
This model was trained on the following synthetic dataset:
- Dataset: `BoB14TeamSentinel/sentinel-kr-sensitive-entities-synthetic-v3`
- Notes: All sensitive values were **AI-generated synthetic** values (not collected from real people or incidents).

> Important: The dataset is released under **CC BY 4.0**. If you reuse the dataset or derivatives, please provide appropriate attribution.

## Whitelist Label Set (Allowed Labels)
The model is expected to output **only** the following labels:

### Basic identity
- `NAME` — Person name  
- `PHONE` — Phone number  
- `EMAIL` — Email address  
- `ADDRESS` — Address (road name / district / detailed address)  
- `POSTAL_CODE` — Postal/ZIP code  

### Government / official identifiers
- `PERSONAL_CUSTOMS_ID` — Personal Customs Clearance Code (KR)  
- `RESIDENT_ID` — Resident Registration Number (KR)  
- `PASSPORT` — Passport number  
- `DRIVER_LICENSE` — Driver’s license number  
- `FOREIGNER_ID` — Foreigner registration number  
- `HEALTH_INSURANCE_ID` — Health insurance ID  
- `BUSINESS_ID` — Business registration number  
- `MILITARY_ID` — Military service number  

### Authentication / secrets
- `JWT` — JSON Web Token  
- `API_KEY` — API key (vendor-agnostic)  
- `GITHUB_PAT` — GitHub Personal Access Token  
- `PRIVATE_KEY` — Private key material (SSH/TLS/PGP)  

### Financial
- `CARD_NUMBER` — Card number  
- `CARD_EXPIRY` — Card expiry (MM/YY etc.)  
- `BANK_ACCOUNT` — Bank account number  
- `CARD_CVV` — CVC/CVV  
- `PAYMENT_PIN` — Payment/ATM PIN  
- `MOBILE_PAYMENT_PIN` — Mobile payment PIN  

### Crypto
- `MNEMONIC` — Recovery seed phrase / mnemonic  
- `CRYPTO_PRIVATE_KEY` — Crypto private key  
- `HD_WALLET` — HD wallet extended key  
- `PAYMENT_URI_QR` — Payment URI / QR payload (BTC/ETH/XRP/SOL/TRON etc.)  

### Network / device
- `IPV4` — IPv4 address  
- `IPV6` — IPv6 address  
- `MAC_ADDRESS` — MAC address  
- `IMEI` — IMEI  

## Output Contract (Recommended)
This model was fine-tuned for guardrail usage where the assistant returns **JSON only** with:
- `text`: the original input text
- `has_sensitive`: boolean
- `entities`: list of `{ value, begin, end, label }`  
  - `begin` / `end` are **0-based character offsets** (`begin` inclusive, `end` exclusive)

Example:
```json
{
  "text": "문의: minseo.kim@example.com / 010-1234-5678",
  "has_sensitive": true,
  "entities": [
    {"value": "minseo.kim@example.com", "begin": 4, "end": 24, "label": "EMAIL"},
    {"value": "010-1234-5678", "begin": 27, "end": 40, "label": "PHONE"}
  ]
}
```

## How to Use (Transformers)

> Note: This is a chat/instruct-style model. Use your preferred chat template and enforce JSON-only output in the system prompt.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "BoB14TeamSentinel/sentinel-qwen3-4b-kr-sensitive-guard-v3"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)

system = (
    "You are a strict whitelist-only detector for sensitive entities. "
    "Given the user's text, return ONLY a JSON object with keys "
    "`text`, `has_sensitive`, `entities`. "
    "Do not output any labels outside the whitelist. No extra commentary."
    "<List of the whitelist>"
)

user_text = "문의: minseo.kim@example.com / 010-1234-5678"

messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": user_text},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

with torch.no_grad():
    out = model.generate(
        input_ids,
        max_new_tokens=512,
        do_sample=False,
        temperature=0.0,
    )

print(tokenizer.decode(out[0], skip_special_tokens=True))
```

## Limitations
- Synthetic generation may not perfectly match real-world traffic (domain shift).
- Certain formats may be over/under-represented depending on generation prompts.
- Ambiguous numeric strings may cause false positives in some settings.

## Safety & Ethics
- Trained on synthetic data to reduce privacy risk.
- Do not use for real-person identification or any privacy-invasive purpose.
- Always validate outputs before applying automated enforcement in production.

## License
- Model weights: **Apache-2.0**
- Training dataset: **CC BY 4.0** (attribution required)

## Citation / Attribution
If you use this model or the dataset, please attribute:
- **BoB14TeamSentinel**, *sentinel-qwen3-4b-kr-sensitive-guard-v3* (Hugging Face model)
- **BoB14TeamSentinel**, *sentinel-kr-sensitive-entities-synthetic-v3* (Hugging Face dataset)

## Project
- Project: **Sentinel Solution**
- Organization: **Team.될것같은데**
