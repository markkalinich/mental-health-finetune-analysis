---
language:
- ko
license: cc-by-sa-4.0
library_name: transformers
pipeline_tag: token-classification
base_model: klue/roberta-large
tags:
- ner
- korean
- pii
- privacy
- guardrail
- roberta
datasets:
- klue
metrics:
- f1
model-index:
- name: korean-pii-ner-v3
  results:
  - task:
      type: token-classification
      name: Korean PII NER
    dataset:
      type: custom
      name: PII NER internal test (3,401 sentences)
    metrics:
    - type: f1
      value: 0.878
      name: macro F1
    - type: f1
      value: 0.887
      name: micro F1
  - task:
      type: token-classification
      name: Korean PII NER
    dataset:
      type: klue
      name: KLUE-NER validation (5,000 sentences)
    metrics:
    - type: f1
      value: 0.766
      name: macro F1
    - type: f1
      value: 0.792
      name: micro F1
---

# Korean PII NER v3 (klue/roberta-large fine-tuned)

한국어 PII (Personally Identifiable Information) 가드레일용 NER 모델. **NAME / ADDRESS / ORG** 3 엔티티 7-label BIO 분류.

## Quick Start

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("vmaca123/korean-pii-ner-v3")
model = AutoModelForTokenClassification.from_pretrained("vmaca123/korean-pii-ner-v3")

ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
print(ner("저는 홍길동이고 서울시 강남구 테헤란로 152에 거주합니다. 삼성전자 소속입니다."))
# [{'entity_group': 'NAME', 'start': 6, 'end': 9, 'word': '홍길동', ...},
#  {'entity_group': 'ADDRESS', 'start': 13, 'end': 29, 'word': '서울시 강남구 테헤란로 152', ...},
#  {'entity_group': 'ORG', 'start': 35, 'end': 39, 'word': '삼성전자', ...}]
```

## Labels (BIO, 7 classes)

| ID | Label | Maps to v0.2 EntityType |
|---:|---|---|
| 0 | O | (non-entity) |
| 1 | B-NAME | PERSON_NAME |
| 2 | I-NAME | PERSON_NAME |
| 3 | B-ADDRESS | ADDRESS_FULL |
| 4 | I-ADDRESS | ADDRESS_FULL |
| 5 | B-ORG | ORGANIZATION |
| 6 | I-ORG | ORGANIZATION |

PHONE / EMAIL / RRN / CREDIT_CARD 등 정형 PII는 본 모델 scope 밖 (regex/dict 책임).

## Training data

| Source | Count | License |
|---|---:|---|
| KLUE-NER train | 21,008 | CC-BY-SA |
| Faker-ko baseline (real admin divisions) | 10,000 | self-generated |
| Faker conjunctive composite | 2,000 | self-generated |
| Hard negatives (하늘/사랑/대표번호/예시번호) | 1,000 | self-generated |
| **Total train pool** | **34,008** | |

데이터 split: 8:1:1 (train 27,206 / val 3,401 / test 3,401). KLUE-NER validation 5,000은 학습 미포함 외부 평가용.

## Training details

- **Base**: `klue/roberta-large` (335M params)
- **Phase 1**: encoder freeze, classifier head 1 epoch, LR 5e-4
- **Phase 2**: full unfreeze, 5 epochs, LR 2e-5, warmup ratio 0.1, weight decay 0.01
- **Batch**: 16, max_length 128, fp16
- **Hardware**: RTX 3090 24GB (Vast.ai)
- **Wall clock**: ~30 minutes

## Evaluation results

| Eval set | macro-F1 | micro-F1 | size |
|---|---:|---:|---:|
| Internal val | 0.872 | 0.880 | 3,401 |
| **Internal test** | **0.878** | **0.887** | 3,401 |
| **KLUE-NER val (외부)** | **0.766** | **0.792** | 5,000 |

### Iteration comparison (6 training runs)

| Run | Base | Data | Internal test | KLUE val |
|---:|---|---:|---:|---:|
| 1 | bert-base, 2ep | 31k | 0.776 | 0.630 |
| 2 | bert-base, 5ep | 31k | 0.798 | 0.669 |
| 3 | roberta-base, 5ep | 31k | 0.830 | 0.697 |
| 4 (v1) | roberta-large, 5ep | 31k | 0.865 | 0.764 |
| 5 (v2) | roberta-large + Naver/WikiAnn | 139k | 0.708 | 0.664 ❌ |
| **6 (v3)** | **roberta-large + augment** | **34k** | **0.878** | **0.766** ★ |

v2 실패 lesson: Naver NER 90k + WikiAnn 20k 통합이 KLUE val -10%p. 어절 라벨의 char-level 변환 노이즈 + multi-source distribution shift가 원인. v3는 v1 setup 그대로 + composite/hard-negative augment만 추가하는 conservative 접근.

## Sample outputs

| Input | NER output |
|---|---|
| "안녕하세요, 저는 홍길동이고 서울시 강남구 테헤란로 152에 거주합니다. 삼성전자 소속입니다." | NAME=홍길동, ADDR=서울시 강남구 테헤란로 152, ORG=삼성전자 |
| "저는 박정희이고 부산광역시 해운대구에 거주하며 LG전자 소속입니다." | NAME + ADDR + ORG |
| "오늘 하늘이 맑네요." | (no spans) ✓ hard negative |
| "사랑은 중요한 가치입니다." | (no spans) ✓ hard negative |
| "예시 전화번호는 010-0000-0000입니다." | (no spans) ✓ NER scope 밖 |

## Limitations & known issues

- **Conjunctive 패턴**: `{name}이고 {address}` 같은 케이스 v3에서 학습 데이터로 보강했으나 일부 변형 (지명+호칭 인접 등) 에서 boundary 오류 가능
- **ADDRESS_UNIT 미지원**: "101동 1203호" 같은 unit은 dict 후처리에서 분기 (NER은 ADDRESS_FULL만 emit)
- **SCHOOL/HOSPITAL 미세분**: ORG 단일 라벨로 emit, dict로 SCHOOL/HOSPITAL reclassification
- **외부 도메인 transfer 약함**: KLUE val 0.766 vs internal 0.878. 도메인 특화 fine-tuning 권장 (의료/금융/법률 등)
- **PHONE/EMAIL/RRN 미지원**: 정형 PII는 regex 책임

## Intended use

- 한국어 텍스트에서 PII 후보 (PERSON_NAME / ADDRESS_FULL / ORGANIZATION) 탐지
- v0.2 가드레일 파이프라인의 NER detector 모듈 (Korean PII Guardrail v0.2)
- Production 환경: regex / dictionary / context scorer / boundary corrector와 함께 사용 권장 (단일 NER만으로는 99% target 미달)

## Out of scope

- 정형 PII (전화번호, 이메일, 주민등록번호 등) — regex/validator 사용
- 멀티 턴 / RAG 환경에서의 컨텍스트 추적 — v0.2 single-turn 범위 밖
- 의료 차트, 법률 문서 등 도메인 특화 텍스트 (성능 저하 예상)

## License

CC-BY-SA-4.0 (KLUE base 모델 라이선스 상속).

## Citation

```bibtex
@misc{kimminwoo2026koreanpiinerv3,
  title={Korean PII NER v3: klue/roberta-large fine-tuned for PII guardrails},
  author={Kim, Minwoo},
  year={2026},
  url={https://huggingface.co/vmaca123/korean-pii-ner-v3}
}
```

## Companion project

이 모델은 [Korean PII Guardrail v0.2](https://github.com/vmaca123/My-AI-Security-Project) 프로젝트의 NER detector 모듈입니다.

- Wrapper code: `PII/ner/ner_wrapper.py` (v0.2 `BaseNERDetector` Protocol 준수)
- Design doc: `korean_pii_guardrail_v0_2/docs/14_NER_DESIGN_v1.md`
- Training results: `PII/ner/TRAINING_RESULTS_v3.md`
