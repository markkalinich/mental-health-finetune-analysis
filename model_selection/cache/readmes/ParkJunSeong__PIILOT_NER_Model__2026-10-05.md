---
language:
- ko
license: apache-2.0
base_model: monologg/koelectra-base-v3-discriminator
tags:
- ner
- token-classification
- pii-detection
- generated_from_trainer
- koelectra
pipeline_tag: token-classification
library_name: transformers
metrics:
- f1
- precision
- recall
widget:
- text: "제 이름은 홍길동이고, 주민등록번호는 900101-1234567입니다."
  example_title: "PII Example 1"
- text: "문의사항은 help@example.com으로 연락주세요."
  example_title: "PII Example 2"
---

# KoELECTRA for PII Detection (Korean)

This model is a fine-tuned version of [monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator) for **Personally Identifiable Information (PII) Detection** in Korean text.

## Model Description
이 모델은 한국어 텍스트 내에서 개인정보(이름, 주민등록번호, 전화번호, 이메일 등)를 식별하기 위해 KoELECTRA를 기반으로 미세조정(Fine-tuning)되었습니다.

- **Developed by:** ParkJunSeong
- **Shared by:** ParkJunSeong
- **Language(s):** Korean
- **License:** Apache-2.0
- **Base model:** monologg/koelectra-base-v3-discriminator
- **Task:** Token Classification (NER)

## Intended Uses
이 모델은 다음과 같은 6가지 개인정보 엔티티를 탐지하는 데 사용할 수 있습니다.

| Label | Description | Example |
| :--- | :--- | :--- |
| **p_nm** | 이름 (Name) | 홍길동 |
| **p_rrn** | 주민등록번호 (Resident Registration Number) | 900101-1234567 |
| **p_ph** | 전화번호 (Phone Number) | 010-1234-5678 |
| **p_em** | 이메일 (Email) | example@email.com |
| **p_add** | 주소 (Address) | 서울시 강남구 |
| **p_ip** | IP 주소 (IP Address) | 192.168.0.1 |
| **p_acn** | 계좌번호 (Account Number) | 123-45-67890 |
| **p_pp** | 여권번호 (Passport Number) | M12345678 |
| **O** | 비정형 데이터 (Outside/Non-PII) | 안녕하세요 |


## Evaluation Results
*(만약 성능 지표가 있다면 이 부분을 채워주세요, 없다면 생략 가능합니다)*
- **F1 Score:** 95.92
- **Precision:** 95.46
- **Recall:** 96.38
- **Accuracy:** 99.69

## Usage
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# 1. Load Model & Tokenizer
model_name = "ParkJunSeong/PIILOT_NER_Model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# 2. Create Inference Pipeline
# aggregation_strategy="simple" merges tokens (e.g., "홍", "##길동" -> "홍길동")
nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# 3. Run Inference
text = "제 이름은 홍길동이고, 전화번호는 010-1234-5678입니다."
results = nlp(text)

# 4. Check Results
for entity in results:
    print(f"Entity: {entity['word']}, Label: {entity['entity_group']}, Score: {entity['score']:.4f}")