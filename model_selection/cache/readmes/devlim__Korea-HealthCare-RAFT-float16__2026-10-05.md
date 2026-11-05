## 모델 개요

이 프로젝트는 대규모 헬스케어 데이터셋을 기반으로 사용자가 신뢰성 있는 의료 정보를 언제 어디서든 얻을 수 있도록 돕는 플랫폼 구축을 목표로 하였습니다. **초거대 AI 헬스케어 질의응답 데이터**를 활용하여 의료 분야의 전문 지식을 포함한 대규모 AI 모델을 기반으로 하며, 환자들에게 신속하고 정확한 의료 정보를 제공합니다.

## 모델 상세 설명

- **모델명**: RAFT + RAG 기반 의료 상담 챗봇
- **기반 모델**: Gemma-2-2b-it
- **학습 방법**: GPT 4o-mini를 활용한 데이터 증강 및 RAFT 방법 적용
- **아키텍처**: Gemma-2-2b-it과 동일한 구조 사용

## 데이터셋

- **데이터셋 이름**: 초거대 AI 헬스케어 질의응답 데이터
- **출처**: [AI 허브](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71762)
- **데이터 구성**:
  - 40%: 정답이 포함된 문서 1개 + 정답과 관련 없는 문서 1개
  - 60%: 정답과 관련 없는 문서 2개

## 학습 방법

모델은 GPT 4o-mini를 활용한 데이터 증강 기법과 RAFT([Adapting Language Model to Domain Specific RAG](https://arxiv.org/abs/2403.10131)) 방법을 적용하여 학습되었습니다. 이러한 방법을 통해 모델은 복잡한 문맥 이해와 정확한 정보 검색 능력을 향상시켰습니다.

### 예시

````plaintext
<bos><start_of_turn>user
<Question>: 족저 근막염 재활을 위해 어떤 조치를 취해야 하나요?
<Documents>: [
  '족저 근막염 재활은 발 건강을 회복하고 통증을 완화하기 위해 다양한 조치들을 취하는 것이 중요합니다. ...',
  '외상 후 스트레스 장애 치료를 위해 약물 치료가 선택될 수 있습니다. ...'
]
<end_of_turn>
<start_of_turn>model
<Answer>: 족저 근막염 재활을 위해 취해야 할 조치는 다음과 같습니다: ...
<end_of_turn><eos>
````
### 예시
#### 질문:
````plaintext
두통이 자주 발생하는 이유가 궁금합니다. 스트레스 때문일까요, 아니면 다른 건강 문제일까요? 어떤 상황에서 두통이 심해지는지와 함께 주의할 점을 알고 싶어요.
````
#### 답변:
````markdown
## 두통의 원인

두통은 여러 가지 원인으로 발생할 수 있습니다. 가장 일반적인 원인으로는 다음과 같은 것들이 있습니다:

1. **스트레스**: 일상생활에서의 스트레스는 두통을 유발할 수 있습니다. 특히 업무나 학업, 가족 관계에서의 압박감이 두통을 악화시킬 수 있습니다.
2. **신체적 요인**: 근육의 긴장, 혈액 순환 문제, 호르몬 변화 등 신체적인 요인도 두통을 유발할 수 있습니다.
3. **영양 결핍**: 비타민 B6 결핍이나 단백질 부족은 두통을 일으킬 수 있습니다.
4. **약물**: 특정 약물, 특히 항우울제나 진통제 등이 두통을 유발할 수 있습니다.
5. **비만**: 체중이 과다하면 혈액순환이 저하되어 두통이 발생할 수 있습니다.

## 두통의 주의점

두통이 자주 발생하는 경우, 다음과 같은 주의점을 따르는 것이 중요합니다:

- **스트레스 관리**: 스트레스를 줄이기 위해 명상, 요가, 심호흡 등의 방법을 시도해보세요.
- **건강한 식습관**: 균형 잡힌 식사를 하고, 과식이나 탄수화물 과다 섭취를 피하세요.
- **규칙적인 운동**: 매일 짧은 운동을 통해 혈액순환을 개선하고 스트레스를 줄이는 데 도움이 됩니다.
- **충분한 수면**: 규칙적인 수면 패턴을 유지하고, 잠자기 전에는 스트레스를 줄이는 것이 중요합니다.
- **전문가 상담**: 두통이 반복적으로 발생하거나 심각한 증상이 있을 경우, 의사와 상담하여 적절한 진단과 치료를 받는 것이 필요합니다.

두통은 일반적으로 일상생활에 큰 지장을 주지 않지만, 만약 자주 발생하거나 심각한 증상이 나타난다면 전문가의 도움을 받는 것이 좋습니다.

````
## 평가 결과

본 연구에서는 RAFT + RAG 모델과 기존 모델인 Gemma-2-2b-it을 비교하여 **RAGAS: Automated Evaluation of Retrieval Augmented Generation** 방법론을 사용하여 답변 유사도를 평가했습니다.

- **Gemma-2-2b-it 모델**: 평균 **79.98%** 의 유사도 기록
- **RAFT + RAG 모델**: 평균 **96.02%** 의 유사도 기록
  - 최소 유사도: **92.39%**
  - 최대 유사도: **98.56%**

약 **16%** 의 성능 향상이 확인되었으며, 이는 RAFT + RAG 모델이 복잡한 문맥과 정보 검색에서 우수한 처리 능력을 보유하고 있음을 나타냅니다.

<img src="https://cdn-uploads.huggingface.co/production/uploads/64252e69120a3ed323304387/kcy1FWOJ2OxCtyhakfTGe.png" alt="image" width="80%">

## 사용 방법

사용 방법과 아키텍처는 **Gemma-2-2b-it** 모델과 동일합니다. 모델은 한국어 의료 질의에 대해 전문적인 답변을 제공합니다.

## 모델 및 양자화 버전

아래는 본 모델과 양자화한 버전, 그리고 DSF(Domain-Specific Fine-tuning) 모델의 링크입니다:

- **RAFT 모델**
  - [devlim/Korea-HealthCare-RAFT-float16](https://huggingface.co/devlim/Korea-HealthCare-RAFT-float16)
  - [devlim/Korea-HealthCare-RAFT-unit8](https://huggingface.co/devlim/Korea-HealthCare-RAFT-unit8)
- **DSF 모델**
  - [devlim/Korea-HealthCare-DSF-float16](https://huggingface.co/devlim/Korea-HealthCare-DSF-float16)
  - [devlim/Korea-HealthCare-DSF-unit8](https://huggingface.co/devlim/Korea-HealthCare-DSF-unit8)

## 제한 사항 및 주의사항

- **의료 조언**: 이 모델은 의료 정보를 제공하지만, 전문적인 의료 상담이나 진단을 대체하지 않습니다. 건강 관련 의사 결정은 반드시 의료 전문가와 상의하시기 바랍니다.
- **데이터 한계**: 모델은 학습된 데이터 범위 내에서 답변을 제공합니다. 최신 의료 지침이나 개인별 상황에 대한 고려는 부족할 수 있습니다.
- **책임 한계**: 이 모델의 사용으로 발생하는 결과에 대해 개발자는 책임을 지지 않습니다.

## 인용

이 모델을 사용하거나 연구에 참고하실 경우 다음 문헌을 인용해주시기 바랍니다:

- **초거대 AI 헬스케어 질의응답 데이터**: AI 허브, [초거대 AI 헬스케어 질의응답 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71762)
- **Gemma 2 모델**: "Gemma 2: Improving Open Language Models at a Practical Size", *2023*.
- **RAFT 방법론**: "Adapting Language Model to Domain Specific RAG", *arXiv preprint arXiv:2403.10131*, 2023.
- **RAGAS 평가 방법론**: "RAGAS: Automated Evaluation of Retrieval Augmented Generation", *2023*.

## 라이선스

이 모델은 해당 데이터셋과 원천 모델의 라이선스 조건에 따라 사용해야 합니다. 사용 전에 반드시 라이선스 내용을 확인하시기 바랍니다.

