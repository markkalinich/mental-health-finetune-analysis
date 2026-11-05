---
license: mit
base_model: klue/bert-base
tags:
- bert
- lora
- korean
- text-classification
- sentiment-analysis
language:
- ko
datasets:
- nsmc
---
# NSMC 감정 분석 LoRA 모델

NSMC 데이터셋으로 파인튜닝된 한국어 분석 모델입니다.
## 모델 정보
- ** 베이스 모델** : klue/bert-base
- ** 파인튜닝 방법** : LoRA
- ** 언어** : 한국어
## 성능
- **최종 성능**: Accuracy 85%
## 학습정보
### 학습설정
- **epoch**: 3
## 사용 방법
```python
from peft import PeftModel

# 베이스 모델 로드 (분류용)
print("베이스 모델 로딩")
base_model_reload = AutoModelForSequenceClassification.from_pretrained(
    "klue/bert-base",
    num_labels=2
)

# 업로드한 LoRA 어댑터 로드
print(f"LoRA 어댑터 로딩: jihun-pae/nsmc-sentiment-lora")
model_reload = PeftModel.from_pretrained(base_model_reload, model_name_upload)
tokenizer_reload = AutoTokenizer.from_pretrained(model_name_upload)

# GPU로 이동
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_reload = model_reload.to(device)
model_reload.eval()

print("모델 로드 완료!")
print("이제 이 코드로 어디서든 내 모델을 사용할 수 있습니다!")
```

**Note**: 이 모델은 교육 목적으로 만들어졌습니다.
