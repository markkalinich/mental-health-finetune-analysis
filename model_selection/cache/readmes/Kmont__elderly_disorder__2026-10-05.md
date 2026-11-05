---
language:
- ko
tags:
- pytorch
- mental
- medical
- elderly
- disorder
- NLP
---

https://github.com/K-Saaan/elderly_mental_disorder-BERT

# Elderly-Mental-Disorder 
elderly-mental-disorder는 일상 대화 텍스트에서 정신 질환을 분류하는 모델입니다.
현재 한국 사회가 초고령화에 접어듬에 따라 발생하는 문제 중 고령층의 다양한 정신질환에 집중하여 연구했습니다. 고령층의 일상 대화에서 다양한 정신질환에 대한 가능성을 사전에 확인하고자 모델을 개발하게 되었습니다.

분류 질환은 다음과 같습니다.

1. ADHD : 주의력결핍과다장애
2. PTSD(posttraumatic_stress_disorder) : 외상후스트레스장애
3. bipolar_disorder : 양극성장애
4. obsessive_compulsive_disorder : 강박장애
5. paranoid_personality_disorder : 편집성 인격장애
6. avoidant_personality_disorder : 회피성 인격장애
7. seperation_anxiety_disorder : 분리불안장애
8. MDD(major_depressive_disorder) : 주요우울장애
9. generalized_anxiety_disorder : 범불안장애
10. neurocognitive_disorders : 신경인지장애

총 10가지의 정신 질환을 분류할 수 있도록 했습니다. (neurocognitive_disorders의 경우 데이터 양이 극단적으로 적어 최종적으로는 반영하지 못함)


## 학습 데이터
| Source                              |Size (MB) | Link                                  |
|----------------------------------|---------|------------------------------------------|
| AIHub 감성 대화 말뭉치    | 42.6   | aihub.or.kr |
| AIHub 노년층 대상 감성 분류 모델    | 4.8   | aihub.or.kr |
| AIHub 의료, 법률 전문 서적 말뭉치    | 351.0   | aihub.or.kr |
| AIHub 전문분야 한영 말뭉치          | 63.4  | aihub.or.kr|
| 질병관리청 국가건강정보포털          | 8.33  | health.kdca.go.kr     |
| 보건복지부 국가정신건강정보포털       | < 1.0  | mentalhealth.go.kr   |

---

## 학습
elderly-mental-disorder는 [snunlp/KR-BERT-char16424](https://huggingface.co/snunlp/KR-BERT-char16424)모델로 학습 됐습니다.

<img width="675" alt="Image" src="https://github.com/user-attachments/assets/ff787d80-c811-4143-b0dc-e4c1286ac51b" />

정신질환에 대한 도메인 학습을 위해 Intermediate 학습 과정을 추가해 정신질환 및 의학 관련 정보를 학습하도록 했다. 이후 노년층 감성분류 데이터를 Fine-tuning하여 원하는 결과를 출력하도록 했다.

| Text                                                   | Label     |
|-------------------------------------------------------|---------------------|
| 어렵게 자식들을 키웠는데 치료비 얘기를 꺼낸 뒤 아무도 연락하지 않아              | MDD(major_depressive_disorder) |

---
