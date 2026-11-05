---
language:
- ko
base_model:
- beomi/KcELECTRA-base
pipeline_tag: text-classification
tags:
- emotion
- sentiment
---

## Text의 감정을 분석하기 위한 모델입니다.
## KcELECTRA 모델을 기반으로 약 22만개의 감정 문장을 학습하였습니다.

### 감정은 총 6개의 카테고리로 도출되며 기쁨, 당황, 분노, 불안, 상처, 슬픔 입니다.

```
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "noridorimari/emotion_classifier"

# 감정 라벨 매핑
id2label = {
    0: "기쁨",       # happy
    1: "당황",       # embarrass
    2: "분노",       # anger
    3: "불안",       # unrest
    4: "상처",       # damaged
    5: "슬픔"        # sadness
}
label2id = {v: k for k, v in id2label.items()}

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# id2label 정보를 직접 설정 (config에 추가)
model.config.id2label = id2label
model.config.label2id = label2id

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    return_all_scores=True,
    device=0 if torch.cuda.is_available() else -1
)

texts = [
    "오늘 회사에서 실수해서 너무 불안해.",
    "친구가 나한테 거짓말해서 정말 화가 났어.",
    "좋은 소식이 있어서 하루 종일 기분이 좋아!"
]

for text in texts:
    preds = classifier(text)[0]
    # 확률 높은 순으로 정렬
    preds = sorted(preds, key=lambda x: x["score"], reverse=True)
    top = preds[0]
    print(f"\n문장: {text}")
    print(f"예측 감정: {top['label']} ({top['score']*100:.2f}%)")
    print("상세 확률 분포:")
    for p in preds:
        print(f"  {p['label']:>4} : {p['score']*100:.2f}%")

```


```
@misc{lee2021kcelectra,
  author = {Junbum Lee},
  title = {KcELECTRA: Korean comments ELECTRA},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Beomi/KcELECTRA}}
}
```