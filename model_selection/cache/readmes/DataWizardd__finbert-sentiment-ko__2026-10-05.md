---
language: ko
datasets: naver-finance-news
tags:
  - sentiment-analysis
  - korean
  - finance
  - finbert
  - transformers
license: mit
model-index:
  - name: finbert-sentiment-ko
    results:
      - task:
          name: Sentiment Analysis
          type: text-classification
        metrics:
          - type: accuracy
            value: 0.93
---

# FinBERT Sentiment Analysis (Korean, Finance Domain)

이 모델은 **한국어 환율(금융) 뉴스 요약문**을 대상으로 감정을 분류하기 위해 파인튜닝된 BERT 기반 모델입니다.  
감정 분류는 다음 세 가지 클래스 중 하나로 수행됩니다:

- `0`: 부정  
- `1`: 중립  
- `2`: 긍정

## 🧠 학습 정보

- 기반 모델: [`snunlp/KR-FinBERT-SC`](https://huggingface.co/snunlp/KR-FinBERT-SC)
- 데이터: 직접 수집한 **네이버 환율(금융) 뉴스** 요약 + 감정 수작업 라벨링
- 총 샘플 수: 약 200
- Optimizer: AdamW
- Epochs: 4
- 최대 길이: 128
- 평가 지표: Accuracy, F1 Score

## 📊 성능 평가

| 감정 클래스 | Precision | Recall | F1-score | Support |
|-------------|-----------|--------|----------|---------|
| 부정        | 0.89      | 1.00   | 0.94     | 17      |
| 중립        | 1.00      | 0.82   | 0.90     | 11      |
| 긍정        | 0.93      | 0.93   | 0.93     | 14      |
| **정확도**  |           |        | **0.93** | 42      |

> 전체 정확도: **93%**  
> Macro F1-score: **0.92**

---

## 🛠 사용 방법

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="DataWizardd/finbert-sentiment-ko")

pipe("환율이 급등하며 시장 불안이 커지고 있다.")
# 출력: [{'label': '부정', 'score': 0.95}]
