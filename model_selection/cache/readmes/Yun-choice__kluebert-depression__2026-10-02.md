---
license: cc-by-sa-4.0
language: ko
base_model: klue/bert-base
tags:
  - bert
  - korean
  - mental-health
  - regression
---
# kluebert-<label>

한국어 심리상담 채록 1,609건으로 fine-tune된 `klue/bert-base` 회귀 모델 (CounsHelper F1 1단계).
회귀 출력을 `[0, 3]` 정수에 클리핑한 뒤 `0 → 0, 그 외 → 1`로 binary 변환하여 사용한다.
추론 사용 예시는 [Space](https://huggingface.co/spaces/Yun-choice/kluebert-counshelper) 참조.