---
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - text-classification
  - korean
  - ecommerce
  - fashion
library_name: transformers
license: apache-2.0
language:
  - ko
widget:
  - text: "배송이 빠르고 품질도 좋아요"
  - text: "원단이 얇고 마감이 별로네요"
  - text: "가격은 괜찮은데 디자인이 마음에 안 들어요"
model-index:
  - name: eCommerce Fashion 3-class (KoELECTRA)
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: Custom Fashion Reviews (ko)
          type: custom
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.91
          - name: F1 (weighted)
            type: f1
            value: 0.90
---

# 🛍️ eCommerce Fashion 한국어 감정분석 (3-Class)

[![Transformers](https://img.shields.io/badge/HF-Transformers-blue?logo=huggingface)](https://huggingface.co/solbi12/ecommers_fasion_fine_tuned_3class_model)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Lang](https://img.shields.io/badge/Language-Korean-orange)
![Task](https://img.shields.io/badge/Task-Sentiment%20Analysis-purple)

한국어 **패션 리뷰** 도메인에 특화된 **3-클래스 감정분석 모델**입니다.  
`KoELECTRA-base`를 기반으로 파인튜닝 했으며, 라벨은 **NEGATIVE(0) / NEUTRAL(1) / POSITIVE(2)** 입니다.

---

## ✨ 특징
- 한국어 패션 리뷰(배송/품질/디자인 등)에 최적화
- 부정/중립/긍정 **3-class 분류**
- Hugging Face Inference Widget 및 Transformers 라이브러리로 즉시 사용 가능

---

## 🚀 사용법

### 👉 파이프라인
```python
from transformers import pipeline

repo_id = "solbi12/ecommers_fasion_fine_tuned_3class_model"
clf = pipeline("text-classification", model=repo_id, truncation=True)

clf("배송이 빠르고 품질도 좋아요")
# [{'label': 'POSITIVE', 'score': 0.98}]

---


## 📜 README.md (마크다운 형식)

### 💻 모델 사용 방법: PyTorch 직접 사용

이 모델은 한국어 패션 리뷰의 감정을 긍정(POSITIVE), 부정(NEGATIVE), 중립(NEUTRAL) 3가지로 분류하도록 파인튜닝되었습니다. `transformers` 라이브러리를 사용하여 쉽게 로드하고 추론할 수 있습니다.

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 모델 ID
repo_id = "solbi12/ecommers_fasion_fine_tuned_3class_model"

# 모델 및 토크나이저 로드 (Hugging Face Hub에서 자동 다운로드)
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id).eval()

# 테스트 텍스트
text = "원단이 얇고 마감이 별로네요"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

# 추론
with torch.no_grad():
    logits = model(**inputs).logits
    pred = int(logits.argmax(dim=-1))

# 라벨 출력
label_map = {0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE"}
print(f"입력 텍스트: '{text}'")
print(f"분류 결과: {label_map[pred]}")
```

-----

### 🏷️ 라벨 정의

| 라벨 ID | 라벨명 |
| :--- | :--- |
| **0** | **NEGATIVE** (부정) |
| **1** | **NEUTRAL** (중립) |
| **2** | **POSITIVE** (긍정) |

> `id2label` 및 `label2id`가 모델 설정(`config.json`)에 저장되어 있어 Hugging Face `pipeline` 사용 시에도 라벨명이 자동으로 출력됩니다.

-----

### 📊 성능 (Validation Set 기준)

| 지표 | 점수 |
| :--- | :--- |
| Accuracy | **0.91** |
| F1-score | **0.90** |

> **데이터**: "[AI HUB 데이터셋](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&searchKeyword=%EC%86%8D%EC%84%B1%EA%B8%B0%EB%B0%98%20%EA%B0%90%EC%A0%95%EB%B6%84%EC%84%9D%20%EB%8D%B0%EC%9D%B4%ED%84%B0&aihubDataSe=data&dataSetSn=71603)"

-----

### 🏗️ 학습 정보

  - **Base Model**: `jaehyeong/koelectra-base-v3-generalized-sentiment-analysis`
  - **최대 입력 길이**: 512 토큰
  - **배치 크기**: 32
  - **에포크**: 5
  - **학습률**: 2e-5 (`warmup` 10%)
  - **옵티마이저**: AdamW (`weight decay` 0.01)
  - **손실 함수**: 가중치 부여 교차 엔트로피 (`Weighted CrossEntropy`)

-----

### 📦 파일 구성

  - `config.json` : 모델 구조 및 학습 설정
  - `model.safetensors` : 파인튜닝된 모델 가중치
  - 토크나이저 파일들 :
      - `tokenizer.json`
      - `tokenizer_config.json`
      - `vocab.txt`
      - `special_tokens_map.json`

-----

### ⚠️ 한계와 주의 사항

  - **도메인 특화**: 이 모델은 **패션 리뷰 도메인에 최적화**되어 학습되었습니다. 다른 도메인(예: IT 기기, 영화 리뷰)의 텍스트에 대해서는 성능이 저하될 수 있습니다.
  - **입력 길이 제한**: 입력 텍스트가 512 토큰을 초과할 경우, 초과된 부분은 **자동으로 잘립니다(truncation)**.
  - **컨텍스트 부재**: 이 모델은 텍스트 자체만을 분석하며, 리뷰에 첨부된 상품 이미지, 가격, 사용자 평점 등의 **외부 컨텍스트는 고려하지 않습니다.**

-----

### 🔒 라이선스

  - **라이선스**: Apache-2.0
  - **면책 조항**: 모델 사용 시 **데이터 및 도메인 적합성**은 사용자 본인의 책임입니다.

-----

### 🙌 인용 (Citation)

본 모델을 학술적 또는 상업적 목적으로 사용할 경우, 아래와 같이 인용해 주세요.

```
@article{lee2025ecommers,
  title={eCommerce Fashion Korean Sentiment (3-Class)},
  author={Lee, Solbi},
  year={2025},
  note={https://huggingface.co/solbi12/ecommers_fasion_fine_tuned_3class_model}
}
```

또는 일반적인 텍스트 형식으로:
**Solbi Lee, eCommerce Fashion Korean Sentiment (3-Class), 2025.**
**모델 링크:** [https://huggingface.co/solbi12/ecommers\_fasion\_fine\_tuned\_3class\_model](https://huggingface.co/solbi12/ecommers_fasion_fine_tuned_3class_model)