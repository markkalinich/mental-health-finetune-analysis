---
library_name: transformers
base_model: Qwen/Qwen3.5-2B
tags:
- pii
- privacy
- guard
- qwen
- lora
- merged
- vllm
license: apache-2.0
---

# Qwen PII Guard (merged)

Fine-tuned from `Qwen/Qwen3.5-2B` to detect personally-identifiable information in
user prompts and emit a single JSON object listing the values found in each of
15 categories.

Output schema:

```json
{"is_valid": true,
 "category": {"Name": ["John Doe"], "Email": ["john@example.com"]}}
```

`is_valid` is `false` and `category` is `{}` when the prompt contains no PII.

## Categories

name, email, phone_number, address, date, national_id, passport_number, drivers_license, tax_id, card_number, bank_account, credentials, ip_address, username

## Evaluation (transformers reference path)

- test rows: **200** (held-out, from `test_dataset_pii.csv`)
- `is_valid` accuracy: **1.0000**
- category key-set accuracy: **0.9350**
- category value-set accuracy: **0.8300**
- binary F1 (`is_valid`): **1.0000**  (P=1.000  R=1.000)
- macro F1 over categories (key-presence): **0.9791**
- macro F1 over categories (value-set): **0.9529**
- parse errors: 0/200

Binary confusion matrix (positive = "contains PII"):

| | predicted PII | predicted clean |
|---|---:|---:|
| actual PII   | 177 | 0 |
| actual clean | 0 | 23 |

Per-category KEY-presence (did the model emit this category at all?):

| Category | Support | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| address | 79 | 0.987 | 0.987 | 0.987 |
| bank_account | 12 | 1.000 | 1.000 | 1.000 |
| card_number | 25 | 1.000 | 1.000 | 1.000 |
| credentials | 10 | 1.000 | 1.000 | 1.000 |
| date | 95 | 1.000 | 1.000 | 1.000 |
| drivers_license | 27 | 0.957 | 0.815 | 0.880 |
| email | 76 | 0.987 | 1.000 | 0.993 |
| ip_address | 9 | 1.000 | 1.000 | 1.000 |
| name | 107 | 1.000 | 0.991 | 0.995 |
| national_id | 52 | 0.911 | 0.981 | 0.944 |
| passport_number | 21 | 0.955 | 1.000 | 0.977 |
| phone_number | 63 | 1.000 | 0.984 | 0.992 |
| tax_id | 24 | 0.920 | 0.958 | 0.939 |
| username | 9 | 1.000 | 1.000 | 1.000 |

Per-category VALUE-set (did the exact strings match within the category?):

| Category | Support (string-spans) | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| address | 79 | 0.924 | 0.924 | 0.924 |
| bank_account | 12 | 1.000 | 1.000 | 1.000 |
| card_number | 26 | 1.000 | 1.000 | 1.000 |
| credentials | 10 | 1.000 | 1.000 | 1.000 |
| date | 123 | 1.000 | 1.000 | 1.000 |
| drivers_license | 27 | 0.957 | 0.815 | 0.880 |
| email | 82 | 0.988 | 1.000 | 0.994 |
| ip_address | 9 | 1.000 | 1.000 | 1.000 |
| name | 242 | 0.863 | 0.835 | 0.849 |
| national_id | 59 | 0.869 | 0.898 | 0.883 |
| passport_number | 21 | 0.955 | 1.000 | 0.977 |
| phone_number | 65 | 0.984 | 0.969 | 0.977 |
| tax_id | 24 | 0.840 | 0.875 | 0.857 |
| username | 9 | 1.000 | 1.000 | 1.000 |

Latency (transformers, single-prompt, greedy decoding):

| mean | median | p95 | max |
|---:|---:|---:|---:|
| 3.15s | 2.77s | 6.45s | 9.82s |

## Quick start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tok = AutoTokenizer.from_pretrained("Accuknoxtechnologies/PII-Qwen3.5-2B-v8")
model = AutoModelForCausalLM.from_pretrained("Accuknoxtechnologies/PII-Qwen3.5-2B-v8", torch_dtype="auto", device_map="auto")

prompt = "Please contact me at jane@example.com or +1 415 555 0100."
msgs = [
    {"role": "system", "content": "<see SYSTEM_MSG in train_qwen_pii.py>"},
    {"role": "user", "content": prompt},
]
text = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
out = model.generate(**tok(text, return_tensors="pt").to(model.device),
                    max_new_tokens=512, do_sample=False, pad_token_id=tok.pad_token_id)
print(tok.decode(out[0], skip_special_tokens=True))
```

## Evaluation — vLLM serving (merged model, text-only)
Same **200 held-out prompts**, served through **vLLM `0.21.0`** instead of the transformers `.generate()` loop. Greedy decoding, dtype bf16, `enable_prefix_caching=True`, `enable_chunked_prefill=True`. This reflects production serving accuracy + latency.
- JSON parse errors: `0/200` (`0.0%`)

### Accuracy (vLLM)
| Metric | Value |
|---|---:|
| `is_valid` accuracy | **1.0000** |
| category key-set accuracy | **0.9350** |
| category value-set accuracy | **0.8300** |
| Binary F1 (positive = contains PII) | **1.0000** |
| Binary precision | 1.0000 |
| Binary recall | 1.0000 |
| Macro F1 (key-presence) | **0.9791** |
| Macro F1 (value-set) | **0.9529** |

### Confusion matrix — binary `is_valid` (vLLM)
| | predicted PII | predicted clean |
|---|---:|---:|
| **actual PII** | TP = 177 | FN = 0 |
| **actual clean** | FP = 0 | TN = 23 |

### Per-category key-presence (vLLM)
| Category | Support | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| address | 79 | 0.987 | 0.987 | 0.987 |
| bank_account | 12 | 1.000 | 1.000 | 1.000 |
| card_number | 25 | 1.000 | 1.000 | 1.000 |
| credentials | 10 | 1.000 | 1.000 | 1.000 |
| date | 95 | 1.000 | 1.000 | 1.000 |
| drivers_license | 27 | 0.957 | 0.815 | 0.880 |
| email | 76 | 0.987 | 1.000 | 0.993 |
| ip_address | 9 | 1.000 | 1.000 | 1.000 |
| name | 107 | 1.000 | 0.991 | 0.995 |
| national_id | 52 | 0.911 | 0.981 | 0.944 |
| passport_number | 21 | 0.955 | 1.000 | 0.977 |
| phone_number | 63 | 1.000 | 0.984 | 0.992 |
| tax_id | 24 | 0.920 | 0.958 | 0.939 |
| username | 9 | 1.000 | 1.000 | 1.000 |

### vLLM inference latency (single-stream, batch = 1)
| Stat | ms / prompt |
|---|---:|
| Mean | **576.0** |
| Median | 511.6 |
| p95 | 1151.7 |
| p99 | 1440.7 |
| Max | 3209.3 |
| Under 1 s | 89.0% |

### vLLM throughput (single batched submit)
- Prompts/sec: **27.73**
- Output tokens/sec: 1569.0
- Input tokens/sec: 35596.5
- Batched wall time for all 200 prompts: 7.21 s

---
*Card generated at 2026-05-31 07:39 UTC. Adapter weights: `Accuknoxtechnologies/PII-Qwen3.5-2B-v8`.*
