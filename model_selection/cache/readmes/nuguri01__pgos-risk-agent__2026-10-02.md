---
language: ko
license: mit
tags:
  - korean
  - psychology
  - risk-assessment
  - suicide-prevention
  - counseling
  - kcelectra
metrics:
  - f1
  - recall
---

# PGOS Risk Agent

**Psychological Growth OS(PGOS)** 프로젝트의 위험도 분류 모델입니다.

## 모델 개요

심리상담 대화에서 내담자의 위험도를 5단계로 분류합니다.

| 클래스 | 정의 | 예시 |
|---|---|---|
| normal | 위험 신호 없는 일상 대화 | 날씨, 음식, 학교생활 |
| concern | 심리적 고통 표현 | "너무 힘들어요", "지쳐요" |
| caution | 소극적 자살 관념 | "사라지고 싶어요", "아무 의미 없어요" |
| warning | 능동적 자살 관념 | "죽고 싶어요", "끝내고 싶어요" |
| crisis | 즉각적 위기 | "오늘 죽을 거예요", "방법 생각해뒀어요" |

## 성능 (v2)

| 지표 | 값 |
|---|---|
| Macro F1 | **0.718** |
| Crisis Recall | **0.984** ← 핵심 지표 |
| Normal F1 | **0.607** |
| Accuracy | **0.726** |

### 클래스별 F1
| 클래스 | F1 | Recall |
|---|---|---|
| normal | 0.607 | 0.532 |
| concern | 0.697 | 0.606 |
| caution | 0.601 | 0.557 |
| warning | 0.863 | 0.999 |
| crisis | 0.819 | 0.984 |

## 설계 원칙

**이중 안전망 구조:**

규칙 필터 (즉각 반응)
↓ 키워드 기반 즉시 탐지
KcELECTRA 모델 (맥락 기반)
↓ Crisis Recall 0.984
Coordinator → 위기 시 즉각 안전망 응답

**임상 근거:** C-SSRS(Columbia Suicide Severity Rating Scale) 5단계 기반

## 학습 데이터

- **주 데이터 (87.2%)**: AI Hub 024 아동·청소년 상담 데이터
  - 임상심리사 직접 라벨링
  - 5개 진단군: 정상군/상담필요/관찰필요/학대의심/위기아동
- **보조 데이터 (8.4%)**: AI Hub 016 심리상담데이터 + 행동 상담 데이터 GPT 증강
- **Normal 보강 (4.4%)**: 일상 대화 GPT 증강
- **총 학습 데이터**: 21,000개 (클래스당 4,000~5,000개)

## 클래스 가중치

```python
weights = [1.3, 1.0, 1.0, 1.3, 1.5]
# normal, concern, caution, warning, crisis
```

## 베이스 모델

[beomi/KcELECTRA-base-v2022](https://huggingface.co/beomi/KcELECTRA-base-v2022)

## PGOS 아키텍처에서의 역할

사용자 발화
↓
Risk Agent (이 모델) + 규칙 필터
↓
crisis 감지 시 → 즉각 위기 개입 (다른 에이전트 중단)
자살예방상담전화 1393 안내
warning 감지 시 → 안전 확인 + 전문가 연결 안내
concern/caution → 공감 강화 + 탐색 유도
normal → 일반 대화 흐름 유지
↓
Coordinator → 최종 응답 생성

## 관련 모델

- [pgos-emotion-stage1-major](https://huggingface.co/nuguri01/pgos-emotion-stage1-major)
- [pgos-behavior-agent](https://huggingface.co/nuguri01/pgos-behavior-agent)
