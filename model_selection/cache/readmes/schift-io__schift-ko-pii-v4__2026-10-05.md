---
language: ko
license: other
license_name: schift-2.0
license_link: LICENSE
library_name: transformers
pipeline_tag: token-classification
tags:
  - pii
  - korean
  - ner
  - privacy
  - token-classification
datasets:
  - custom
model-index:
  - name: schift-ko-pii-v4
    results:
      - task:
          type: token-classification
          name: Korean PII Detection
        dataset:
          type: custom
          name: benchmark_v1 (93 cases)
        metrics:
          - type: f1
            value: 0.863
            name: F1 (raw, no postprocess)
          - type: f1
            value: 0.968
            name: F1 (with postprocess)
      - task:
          type: token-classification
          name: Korean PII Detection
        dataset:
          type: custom
          name: benchmark_v2 (253 cases)
        metrics:
          - type: f1
            value: 0.702
            name: F1 (raw, no postprocess)
          - type: f1
            value: 0.802
            name: F1 (with postprocess)
---

# schift-ko-pii-v4

**111M parameter Korean PII detector that outperforms models 3x its size.**

Fine-tuned from `klue/roberta-base` with LoRA on Korean legal, financial, and administrative texts. Distributed as bf16 safetensors (210 MB).

## Benchmark

Two benchmark suites are included in this repository under `benchmark/`.

### benchmark_v1 (93 cases)

Same benchmark, same scoring (50% overlap match), no postprocessing on either side.

| Model | Params | micro F1 | strong F1 | Size |
|---|---|---|---|---|
| **schift-ko-pii-v4** | **111M** | **0.863** | **0.893** | **210 MB** (bf16) |
| LFM2.5-PII-Detector | 350M | 0.663 | 0.645 | ~1.4 GB |

### benchmark_v2 (253 cases)

Expanded benchmark with harder cases: investigation reports, complex address formats, foreign/Hanja names, mixed-entity documents.

| Model | Params | raw F1 | raw P | raw R |
|---|---|---|---|---|
| LFM2.5-Encoder-350M-PII | 350M | 0.254 | 0.207 | 0.328 |
| **schift-ko-pii-v4** | **111M** | **0.702** | 0.602 | **0.842** |

With postprocessing enabled (`postprocess=True`):

| Benchmark | F1 | P | R |
|---|---|---|---|
| v1 (93 cases) | **0.968** | 0.947 | 0.991 |
| v2 (253 cases) | **0.802** | 0.802 | 0.802 |

### Category breakdown (benchmark_v1, raw model)

| Category | schift-ko-pii | LFM2.5-PII |
|---|---|---|
| Person (standard) | **1.00** | 0.67 |
| Person (rare surnames) | **1.00** | 0.60 |
| Person (short names) | **1.00** | 0.57 |
| Phone | 0.86 | **0.92** |
| Email | **1.00** | 0.86 |
| Address (urban) | **1.00** | 0.67 |
| Address (rural) | **1.00** | 0.60 |
| Vehicle plate | **1.00** | 0.00 |
| Date (Korean) | **1.00** | 0.00 |
| Resident ID | **1.00** | 0.75 |
| Passport | **1.00** | 1.00 |

LFM2.5 is a strong multilingual model, but it was not trained on Korean-specific
formats: vehicle plates (`52가1234`), resident registration numbers
(`850205-1234567`), Korean date expressions (`2024년 3월 15일`), or rare Korean
surnames (`황보`, `남궁`, `독고`).

## Quick start

```bash
pip install schift-ko-pii
```

```python
from schift_ko_pii import detect, mask, apply

# Detect PII spans (each entity gets a sequential id)
spans = detect("피고 김민수의 전화번호는 010-1234-5678이다.")
# [
#   {"id": "person_1", "start": 3, "end": 6, "label": "private_person", ...},
#   {"id": "phone_1", "start": 14, "end": 27, "label": "phone_number", ...},
# ]

# Mask: get masked text + entity map in one call
result = mask("피의자 김철수가 피해자 박영희에게 서울시 강남구에서 금품을 전달하였다.")
print(result["masked"])
# 피의자 [사람1]가 피해자 [사람2]에게 [주소1]에서 금품을 전달하였다.

for e in result["entities"]:
    print(f"  {e['id']}: {e['text']}")
# person_1: 김철수
# person_2: 박영희
# address_1: 서울시 강남구

# Apply: replace selected entities (user can edit the map before applying)
text = apply(
    "피의자 김철수가 피해자 박영희에게 서울시 강남구에서 금품을 전달하였다.",
    result["entities"],
    replacements={"person_1": "OOO", "person_2": "△△△"}
    # address_1 omitted → left unmasked
)
# 피의자 OOO가 피해자 △△△에게 서울시 강남구에서 금품을 전달하였다.

# With postprocessing (regex validation + structured-ID rules)
spans = detect("주민번호 850205-1234567을 확인.", postprocess=True)
```

### Postprocessing

The `postprocess=True` flag applies Korean-specific rules:

- Regex validation for structured IDs (resident numbers, passports, vehicle plates, bank accounts)
- Luhn/checksum verification where applicable
- Context-aware span merging
- False-positive suppression for legal case numbers and statute references

### API (free)

For production use without managing model files:

```python
from schift import Schift

client = Schift(api_key="...")  # free at schift.io
result = client.pii.redact("김민수의 전화번호는 010-1234-5678입니다.")
# Postprocessing is always enabled on the API.
```

## Labels

| Label | Description | Examples |
|---|---|---|
| `private_person` | Person names (Korean, Hanja, foreign) | 김민수, 황보영희, Lee Jenny |
| `private_phone` | Phone numbers | 010-1234-5678, 02-1234-5678 |
| `private_email` | Email addresses | user@example.com |
| `private_address` | Street/postal addresses | 서울특별시 강남구 테헤란로 521 |
| `private_date` | Dates | 2024년 3월 15일, 2024-03-15 |
| `private_url` | URLs, SNS links, IP addresses | instagram.com/user, 192.168.1.1 |
| `account_number` | Structured IDs: resident/business/bank/passport/vehicle | 850205-1234567, M12345678 |
| `secret` | Secrets, API keys, passwords | |

## Running benchmarks

```bash
# Benchmark this model (v1, 93 cases)
python benchmark/run_benchmark.py

# Benchmark v2 (253 cases)
python benchmark/run_benchmark.py --benchmark benchmark/benchmark_v2.jsonl

# With postprocess
python benchmark/run_benchmark.py --postprocess

# Compare any HuggingFace model
python benchmark/run_benchmark.py --hf-model LiquidAI/LFM2.5-Encoder-350M-PII-Detector
```

## Model details

- **Base model**: `klue/roberta-base` (111M params)
- **Training**: LoRA adapter on ~20k Korean legal/financial/admin examples
- **Format**: safetensors bf16 (210 MB)
- **Inference**: `transformers` pipeline, CPU or GPU
- **Max length**: 512 tokens
- **Tagging scheme**: BIES (Begin/Inside/End/Single)

## License

[Schift License v2.0](LICENSE) — Apache 2.0 base with a revenue threshold.
Free for everyone under $10M annual revenue. Research, education, and non-profit
use always permitted. Companies above the threshold: contact hello@schift.io.

## Citation

```bibtex
@software{schift_ko_pii_2026,
  author = {Schift Inc.},
  title = {schift-ko-pii: Korean PII Detection Model},
  year = {2026},
  url = {https://huggingface.co/schift-io/schift-ko-pii-v4},
}
```
