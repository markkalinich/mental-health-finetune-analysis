---
language:
- ko
- en
tags:
- medical
- skin-cancer
- dermatology
- vision
- classification
- gemma3
- korean
- healthcare
datasets:
- custom-skin-lesion-dataset
metrics:
- accuracy
- precision
- recall
- f1
model_type: multimodal
pipeline_tag: image-classification
widget:
- src: https://example.com/skin_lesion_sample.jpg
  candidate_labels: 광선각화증,기저세포암,멜라닌세포모반,보웬병,비립종,사마귀,악성흑색종,지루각화증,편평세포암,표피낭종,피부섬유종,피지샘증식증,혈관종,화농 육아종,흑색점
model-index:
- name: gemma3-skin-tumor-diagnosis
  results:
  - task:
      type: image-classification
      name: Skin Tumor Classification
    dataset:
      type: custom
      name: Korean Skin Lesion Dataset
    metrics:
    - type: accuracy
      value: 0.7640
      name: Accuracy
    - type: f1
      value: 0.7511
      name: F1 Score
---

# Gemma3 피부종양 진단 모델

이 모델은 15가지 피부 질환을 진단할 수 있는 Gemma3 기반 멀티모달 모델입니다.

## 모델 성능
- 정확도: 76.4%
- F1 Score: 0.751
- 평가 이미지: 500개

## 주의사항
⚠️ 이 모델은 의료 참고용으로만 사용하며, 실제 진단은 반드시 전문의와 상담하세요.
\n# Gemma3 피부종양 진단 모델

## 📋 모델 개요
이 모델은 Google의 Gemma3를 기반으로 15가지 피부 종양을 분류하기 위해 파인튜닝된 멀티모달 모델입니다.

## 🎯 성능 지표
- **정확도 (Accuracy)**: 0.7640 (76.40%)
- **정밀도 (Precision)**: 0.7847
- **재현율 (Recall)**: 0.7575
- **F1 Score**: 0.7511
- **평가 이미지 수**: 500개

## 🏥 분류 가능한 피부 질환 (15개 클래스)

| 번호 | 질환명 | 영문명 | Code |
|------|--------|--------|------|
| 0 | 광선각화증 | Actinic Keratosis | AK |
| 1 | 기저세포암 | Basal Cell Carcinoma | BCC |
| 2 | 멜라닌세포모반 | Melanocytic Nevus | MN |
| 3 | 보웬병 | Bowen's Disease | BD |
| 4 | 비립종 | Milia | MI |
| 5 | 사마귀 | Wart | WA |
| 6 | 악성흑색종 | Malignant Melanoma | MM |
| 7 | 지루각화증 | Seborrheic Keratosis | SK |
| 8 | 편평세포암 | Squamous Cell Carcinoma | SCC |
| 9 | 표피낭종 | Epidermal Cyst | EC |
| 10 | 피부섬유종 | Dermatofibroma | DF |
| 11 | 피지샘증식증 | Sebaceous Hyperplasia | SH |
| 12 | 혈관종 | Hemangioma | HE |
| 13 | 화농 육아종 | Pyogenic Granuloma | PG |
| 14 | 흑색점 | Lentigo | LE |

## 📊 평가 데이터셋
- **총 평가 이미지**: 500개
- **평가 방식**: 랜덤 샘플링
- **출력 형식**: XML 구조화된 진단 결과
- **평가 일자**: 2025년 8월 14일

## 🔬 모델 아키텍처
- **Base Model**: Google Gemma3
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Task Type**: Multi-modal (Image + Text) Classification
- **Input**: 피부 병변 이미지 + 진단 instruction
- **Output**: 구조화된 XML 진단 결과

## 💻 사용 방법

### vLLM + OpenAI 호환 API 사용 (현재 설정)
```python
from openai import OpenAI
import base64

# 현재 사용 중인 설정 (localhost의 vLLM 서버)
client = OpenAI(
    api_key="empty",  # vLLM은 빈 키 사용
    base_url="http://localhost:8001/v1"  # vLLM 서버 주소
)

# 또는 RunPod 엔드포인트 사용 시
# client = OpenAI(
#     api_key="rpa_토큰",
#     base_url="https://api.runpod.ai/v2/엔드포인트/openai/v1"
# )

# 이미지 인코딩
def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# 피부 진단 instruction (한국어)
instruction = """너는 피부 병변을 진단하는 전문 AI이다. 다음은 네가 진단할 수 있는 피부 병변 목록이며, 각 병변의 임상적 특징은 아래와 같다. 환자에게 나타난 병변의 이미지와 설명을 바탕으로 가장 적합한 질병을 하나 선택하여 진단하라.

0: 광선각화증
1: 기저세포암
2: 멜라닌세포모반
3: 보웬병
4: 비립종
5: 사마귀
6: 악성흑색종
7: 지루각화증
8: 편평세포암
9: 표피낭종
10: 피부섬유종
11: 피지샘증식증
12: 혈관종
13: 화농 육아종
14: 흑색점

<root><label id_code="{코드}" score="{점수}">{진단명}</label><summary>{진단소견}</summary><similar_labels><similar_label id_code="{코드}" score="{점수}">{유사질병명}</similar_label></similar_labels></root>
"""

# 진단 수행
image_base64 = encode_image("path_to_skin_image.jpg")
response = client.chat.completions.create(
    model="model_name",  # vLLM에서 로드된 모델명
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": instruction},
                {
                    "type": "image_url", 
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}",
                    },
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)
```

### 출력 형식 예시
```xml
<root>
<label id_code="1" score="85.2">기저세포암</label>
<summary>이미지에서는 진주빛 반투명 결절 형태의 병변이 관찰됩니다. 이러한 병변은 일반적으로 천천히 성장하며 주변 조직으로 깊게 침습할 수 있는 특성을 가지고 있습니다...</summary>
<similar_labels>
<similar_label id_code="3" score="12.0">보웬병</similar_label>
<similar_label id_code="0" score="8.5">광선각화증</similar_label>
</similar_labels>
</root>
```

## ⚠️ 중요 안내사항
- 이 모델은 의료진을 대체할 수 없으며, **참고용**으로만 사용해야 합니다
- 실제 진단 및 치료에는 반드시 **전문 의료진의 상담**이 필요합니다
- 모델의 결과는 확률적 추정치이며, 100% 정확하지 않을 수 있습니다
- 이 모델은 교육 및 연구 목적으로만 사용하시기 바랍니다

## 📈 클래스별 성능
자세한 클래스별 성능은 `class_performance.csv` 파일을 참조하세요.

| 클래스 | Precision | Recall | F1-Score |
|---------|-----------|--------|----------|
| 광선각화증 | 0.929 | 0.382 | 0.542 |
| 기저세포암 | 0.786 | 0.595 | 0.677 |
| 멜라닌세포모반 | 0.679 | 1.000 | 0.809 |
| 보웬병 | 0.615 | 0.552 | 0.582 |
| 비립종 | 0.905 | 0.950 | 0.927 |
| 사마귀 | 0.829 | 0.895 | 0.861 |
| 악성흑색종 | 0.517 | 0.455 | 0.484 |
| 지루각화증 | 0.732 | 0.789 | 0.759 |
| 편평세포암 | 0.697 | 0.852 | 0.767 |
| 표피낭종 | 0.900 | 0.621 | 0.735 |
| 피부섬유종 | 0.681 | 0.941 | 0.790 |
| 피지샘증식증 | 0.757 | 0.933 | 0.836 |
| 혈관종 | 1.000 | 0.679 | 0.808 |
| 화농 육아종 | 0.745 | 1.000 | 0.854 |
| 흑색점 | 1.000 | 0.719 | 0.836 |

## 🛠️ 개발 환경
- Python 3.11+
- vLLM OpenAI 호환 서버
- RunPod 클라우드 환경
- CUDA 지원 GPU

## 📁 저장소 파일 구조
```
├── evaluation_results.json    # 상세 평가 결과
├── class_performance.csv      # 클래스별 성능 지표
├── confusion_matrix.png       # 혼동행렬 시각화
├── class_performance.png      # 성능 차트
└── README.md                  # 모델 문서 (이 파일)
```

## 📝 라이선스
이 모델은 연구 및 교육 목적으로만 사용하시기 바랍니다.

## 📞 문의사항
모델 사용 중 문제가 발생하면 이슈를 등록해 주세요.

---
**개발**: Gemma3 기반 피부질환 진단 모델  
**평가일**: 2025-08-14  
**정확도**: 76.40%
