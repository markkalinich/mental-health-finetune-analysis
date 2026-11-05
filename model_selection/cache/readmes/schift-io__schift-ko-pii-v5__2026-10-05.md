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
  - name: schift-ko-pii-v5
    results:
      - task:
          type: token-classification
          name: Korean PII Detection
        dataset:
          type: custom
          name: benchmark_v2 (253 cases)
        metrics:
          - type: f1
            value: 0.823
            name: F1 (with postprocess)
          - type: precision
            value: 0.812
            name: Precision (with postprocess)
          - type: recall
            value: 0.834
            name: Recall (with postprocess)
---

# schift-ko-pii-v5

**34M parameter Korean PII detector — 3x smaller, beats the 111M v4.**

Hybrid detection: the model handles person names and addresses, the SDK postprocessor handles structured patterns (phone numbers, ID numbers, dates, URLs). 136 MB, CPU-only.

## Benchmark (benchmark_v2, 253 cases)

Compared against every public Korean PII model on HuggingFace (as of Aug 2026).

| Model | Params | F1 | P | R |
|---|---|---|---|---|
| OpenMed-PII-Korean-NomicMed-Large | 395M | 0.041 | 0.029 | 0.071 |
| OpenMed-PII-Korean-QwenMed-XLarge | 600M | 0.084 | 0.061 | 0.138 |
| LFM2.5-Encoder-350M-PII | 350M | 0.254 | 0.207 | 0.328 |
| FrameByFrame/korean-pii-e5-base | ~110M | 0.435 | 0.319 | 0.684 |
| seungkukim/korean-pii-masking-v2 | ~110M | 0.553 | 0.672 | 0.470 |
| vmaca123/korean-pii-ner-v3 | ~125M | 0.569 | 0.810 | 0.439 |
| schift-ko-pii-v4 | 111M | 0.702 | 0.602 | 0.842 |
| **schift-ko-pii-v5** | **34M** | **0.823** | **0.812** | **0.834** |

All models evaluated raw (no postprocessing) except v4/v5 which use the SDK postprocessor (regex for structured patterns). v5 with postprocess disabled scores F1=0.578 (P=0.847, R=0.439) — still competitive, and the hybrid approach pushes it to #1.

Not included: `bbanany/qwen25-3b-korean-pii-*` (3B CausalLM, binary PII/NOT_PII classifier on pre-extracted spans — different task, not NER), `upgle/bert-pii-korean` and `alphagyuu/*` (no model weights uploaded), `psh3333/*` (gated), `mncai/*` (broken config).

v5 is 3x smaller than v4 and scores higher on the harder benchmark.

### Raw model (no postprocess)

| Model | Params | raw F1 | raw P | raw R |
|---|---|---|---|---|
| LFM2.5-350M-PII | 350M | 0.254 | 0.207 | 0.328 |
| schift-ko-pii-v4 | 111M | 0.702 | 0.602 | 0.842 |
| schift-ko-pii-v5 | 34M | 0.578 | 0.847 | 0.439 |

v5 raw recall is low because the model only predicts `private_person` and `private_address`. All other categories (phone, email, dates, IDs) are handled by the regex postprocessor — by design, not by limitation.

### Category breakdown (benchmark_v1, 93 cases)

| Category | v5 (34M) | v4 (111M) | LFM2.5 (350M) |
|---|---|---|---|
| Person (standard) | **1.00** | **1.00** | 0.67 |
| Person (rare surnames) | **1.00** | **1.00** | 0.60 |
| Person (short names) | **1.00** | **1.00** | 0.57 |
| Address (urban) | **1.00** | **1.00** | 0.67 |
| Address (rural) | **1.00** | **1.00** | 0.60 |
| Phone (via postprocess) | **0.86** | **0.86** | 0.92 |
| Vehicle plate | **1.00** | **1.00** | 0.00 |
| Date (Korean) | **1.00** | **1.00** | 0.00 |
| Resident ID | **1.00** | **1.00** | 0.75 |

## Installation

```bash
pip install schift-ko-pii
```

## Usage

### 1. Basic detection

```python
from schift_ko_pii import detect

# Raw model output (person + address only)
spans = detect("피고 김민수의 전화번호는 010-1234-5678이다.")
for s in spans:
    print(f"  [{s['id']}] {s['label']}: {s['text']} (score: {s['score']})")
# [person_1] private_person: 김민수 (score: 0.99)

# With postprocessing — adds regex-based detection for phone, ID, dates, etc.
spans = detect("피고 김민수의 전화번호는 010-1234-5678이다.", postprocess=True)
# [person_1] private_person: 김민수
# [phone_1] phone_number: 010-1234-5678
```

### 2. Mask and review

```python
from schift_ko_pii import mask

result = mask(
    "피의자 김철수(주민번호 850205-1234567)가 피해자 박영희에게 "
    "서울특별시 강남구 테헤란로 521에서 금 3,000만원을 전달하였다.",
    postprocess=True
)

print(result["masked"])
# 피의자 [사람1](주민번호 [주민번호1])가 피해자 [사람2]에게
# [주소1]에서 금 3,000만원을 전달하였다.

# Entity map — review what was detected
for e in result["entities"]:
    print(f"  {e['id']:>15}: {e['text']}")
#       person_1: 김철수
#  resident_id_1: 850205-1234567
#       person_2: 박영희
#      address_1: 서울특별시 강남구 테헤란로 521
```

### 3. Selective replacement

```python
from schift_ko_pii import mask, apply

text = ("계약자 남궁혜진(010-9876-5432)의 거주지 "
        "부산광역시 해운대구 우동 1414번지 마린시티 102동 305호에서 "
        "참고인 Mike Johnson을 면담하였다.")

result = mask(text, postprocess=True)

# User reviews and decides what to redact
redacted = apply(text, result["entities"], {
    "person_1": "○○○",       # 남궁혜진 → ○○○
    "person_2": "외국인A",    # Mike Johnson → 외국인A
    "phone_1": "010-****-****",
    # address_1 intentionally left unmasked
})
print(redacted)
# 계약자 ○○○(010-****-****)의 거주지
# 부산광역시 해운대구 우동 1414번지 마린시티 102동 305호에서
# 참고인 외국인A을 면담하였다.
```

### 4. Bulk masking (replace all with ***)

```python
from schift_ko_pii import mask, apply

text = "피해자 이도(여권 M12345678)는 서울 서초구 반포대로 58에 거주한다."
result = mask(text, postprocess=True)

# Replace everything with ***
clean = apply(text, result["entities"])
# 피해자 ***(여권 ***)는 ***에 거주한다.
```

### 5. Using transformers directly

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

model = AutoModelForTokenClassification.from_pretrained(
    "schift-io/schift-ko-pii-v5", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("schift-io/schift-ko-pii-v5")

pipe = pipeline("token-classification", model=model, tokenizer=tokenizer,
                aggregation_strategy="simple")

results = pipe("참고인 제갈량의 증언을 채택한다.")
for r in results:
    print(f"  {r['entity_group']}: {r['word']} ({r['score']:.2f})")
# private_person: 제갈량 (0.95)
```

### 6. Processing files

```python
from schift_ko_pii import mask, apply

with open("document.txt") as f:
    text = f.read()

result = mask(text, postprocess=True)

# Show what was found
print(f"Found {len(result['entities'])} PII entities:")
for e in result["entities"]:
    print(f"  {e['id']}: {e['text']}")

# Redact all and save
clean = apply(text, result["entities"])
with open("document_redacted.txt", "w") as f:
    f.write(clean)
```

### API (free, no model download needed)

```python
from schift import Schift

client = Schift(api_key="...")  # free at schift.io
result = client.pii.redact("김민수의 전화번호는 010-1234-5678입니다.")
# Postprocessing is always enabled on the API.
```

## Labels

| Label | Description | Detected by | Examples |
|---|---|---|---|
| `private_person` | Person names (Korean, Hanja, foreign) | **Model** | 김민수, 남궁혜진, Mike Johnson, 田中太郎 |
| `private_address` | Street/postal addresses | **Model** | 서울특별시 강남구 테헤란로 521 |
| `phone_number` | Phone numbers | Postprocess (regex) | 010-1234-5678, 02-1234-5678 |
| `resident_id` | Resident registration numbers | Postprocess (regex + checksum) | 850205-1234567 |
| `account_number` | Bank accounts, passport, vehicle plates, business IDs | Postprocess (regex) | M12345678, 52가1234 |
| `private_date` | Dates in Korean format | Postprocess (regex) | 2024년 3월 15일 |
| `private_url` | URLs, IP addresses | Postprocess (regex) | 192.168.1.1 |
| `secret` | API keys, passwords | Postprocess (regex) | |

## Architecture

- **Encoder**: Conv + attention hybrid, 6 layers, hidden 512
- **Head**: Linear classifier (512 → 33 labels)
- **Params**: 34M
- **Format**: safetensors float32 (136 MB)
- **Tokenizer**: klue/roberta-base
- **Max length**: 512 tokens
- **Tagging**: BIES (Begin/Inside/End/Single)
- **Requires**: `trust_remote_code=True`

## Running benchmarks

```bash
python benchmark/run_benchmark.py --benchmark benchmark/benchmark_v2.jsonl --postprocess
```

## License

[Schift License v2.0](LICENSE) — Apache 2.0 base with revenue threshold.
Free for everyone under $10M annual revenue. Research, education, and non-profit always permitted.

## Citation

```bibtex
@software{schift_ko_pii_v5_2026,
  author = {Schift Inc.},
  title = {schift-ko-pii-v5: 34M Korean PII Detection Model},
  year = {2026},
  url = {https://huggingface.co/schift-io/schift-ko-pii-v5},
}
```
