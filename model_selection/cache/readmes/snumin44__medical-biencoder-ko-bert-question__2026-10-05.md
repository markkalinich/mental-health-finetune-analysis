---
license: mit
language:
- ko
base_model:
- klue/bert-base
pipeline_tag: feature-extraction
tags:
- medical
---

# 🍊 Korean Medical DPR(Dense Passage Retrieval)

## 1. Intro
**의료 분야**에서 사용할 수 있는 Bi-Encoder 구조의 검색 모델입니다.        
한·영 혼용체의 의료 기록을 처리하기 위해 **SapBERT-KO-EN** 을 베이스 모델로 이용했습니다.            
질문은 Question Encoder로, 텍스트는 Context Encoder를 이용해 인코딩합니다.       

- Question Encoder : [https://huggingface.co/snumin44/medical-biencoder-ko-bert-question](https://huggingface.co/snumin44/medical-biencoder-ko-bert-question)

(※ 이 모델은 AI Hub의 [초거대 AI 헬스케어 질의 응답 데이터](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71762)로 학습한 모델입니다.)


## 2. Model

**(1) Self Alignment Pretraining (SAP)**

한국 의료 기록은 **한·영 혼용체**로 쓰여, 영어 용어도 인식할 수 있는 모델이 필요합니다.        
Multi Similarity Loss를 이용해 **동일한 코드의 용어** 간에 높은 유사도를 갖도록 학습했습니다.        
```
예) C3843080 || 고혈압 질환 
    C3843080 || Hypertension
    C3843080 || High Blood Pressure
    C3843080 || HTN
    C3843080 || HBP
```


- SapBERT-KO-EN : [https://huggingface.co/snumin44/sap-bert-ko-en](https://huggingface.co/snumin44/sap-bert-ko-en)
- Github : [https://github.com/snumin44/SapBERT-KO-EN](https://github.com/millet04/SapBERT-KO-EN)

**(2) Dense Passage Retrieval (DPR)**

SapBERT-KO-EN을 검색 모델로 만들기 위해 추가적인 Fine-tuning을 해야 합니다.      
Bi-Encoder 구조로 질의와 텍스트의 유사도를 계산하는 DPR 방식으로 Fine-tuning 했습니다.    
다음과 같이 기존의 데이터 셋에 **한·영 혼용체 샘플을 증강**한 데이터 셋을 사용했습니다.
```
예) 한국어 병명: 고혈압
    영어 병명: Hypertenstion
    질의 (원본): 아버지가 고혈압인데 그게 뭔지 모르겠어. 고혈압이 뭔지 설명좀 해줘.
    질의 (증강): 아버지가 Hypertenstion 인데 그게 뭔지 모르겠어. Hypertenstion 이 뭔지 설명좀 해줘.
```

- Github : [https://github.com/snumin44/DPR-KO](https://github.com/millet04/DPR-KO)


## 3. Training

**(1) Self Alignment Pretraining (SAP)**

SapBERT-KO-EN 학습에 활용한 베이스 모델 및 하이퍼 파라미터는 다음과 같습니다.    
한·영 의료 용어를 수록한 의료 용어 사전인 **KOSTOM**을 학습 데이터로 사용했습니다.

- Model : klue/bert-base
- Dataset : **KOSTOM**
- Epochs : 1
- Batch Size : 64
- Max Length : 64
- Dropout : 0.1
- Pooler : 'cls'
- Eval Step : 100
- Threshold : 0.8
- Scale Positive Sample : 1
- Scale Negative Sample : 60 

**(2) Dense Passage Retrieval (DPR)**

Fine-tuning에 활용한 베이스 모델 및 하이퍼 파라미터는 다음과 같습니다.

- Model : SapBERT-KO-EN(klue/bert-base)
- Dataset : **초거대 AI 헬스케어 질의 응답 데이터(AI Hub)**
- Epochs : 10
- Batch Size : 64
- Dropout : 0.1
- Pooler : 'cls' 


## 4. Example
이 모델은 질문을 인코딩하는 모델로, Context 모델과 함께 사용해야 합니다.       
동일한 질병에 관한 질문과 텍스트가 높은 유사도를 보인다는 사실을 확인할 수 있습니다.     

(※ 아래 코드의 예시는 ChatGPT를 이용해 생성한 의료 텍스트입니다.)     
(※ 학습 데이터의 특성 상 예시 보다 정제된 텍스트에 대해 더 잘 작동합니다.)

```python
import numpy as np
from transformers import AutoModel, AutoTokenizer

# Question Model
q_model_path = 'snumin44/medical-biencoder-ko-bert-question'
q_model = AutoModel.from_pretrained(q_model_path)
q_tokenizer = AutoTokenizer.from_pretrained(q_model_path)

# Context Model
c_model_path = 'snumin44/medical-biencoder-ko-bert-context'
c_model = AutoModel.from_pretrained(c_model_path)
c_tokenizer = AutoTokenizer.from_pretrained(c_model_path)


query = 'high blood pressure 처방 사례'

targets = [
    """고혈압 진단.
    환자 상담 및 생활습관 교정 권고. 저염식, 규칙적인 운동, 금연, 금주 지시.
    환자 재방문. 혈압: 150/95mmHg. 약물치료 시작. Amlodipine 5mg 1일 1회 처방.""",
    
    """응급실 도착 후 위 내시경 진행.
    소견: Gastric ulcer에서 Forrest IIb 관찰됨. 출혈은 소량의 삼출성 출혈 형태.
    처치: 에피네프린 주사로 출혈 감소 확인. Hemoclip 2개로 출혈 부위 클리핑하여 지혈 완료.""",
    
    """혈중 높은 지방 수치 및 지방간 소견.
    다발성 gallstones 확인. 증상 없을 경우 경과 관찰 권장.
    우측 renal cyst, 양성 가능성 높으며 추가적인 처치 불필요 함."""
]

query_feature = q_tokenizer(query, return_tensors='pt')
query_outputs = q_model(**query_feature, return_dict=True)
query_embeddings = query_outputs.pooler_output.detach().numpy().squeeze()

def cos_sim(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

for idx, target in enumerate(targets):
    target_feature = c_tokenizer(target, return_tensors='pt')
    target_outputs = c_model(**target_feature, return_dict=True)
    target_embeddings = target_outputs.pooler_output.detach().numpy().squeeze()
    similarity = cos_sim(query_embeddings, target_embeddings)
    print(f"Similarity between query and target {idx}: {similarity:.4f}")
```
```
Similarity between query and target 0: 0.2674
Similarity between query and target 1: 0.0416
Similarity between query and target 2: 0.0476
```


## Citing
```
@inproceedings{liu2021self,
    title={Self-Alignment Pretraining for Biomedical Entity Representations},
    author={Liu, Fangyu and Shareghi, Ehsan and Meng, Zaiqiao and Basaldella, Marco and Collier, Nigel},
    booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
    pages={4228--4238},
    month = jun,
    year={2021}
}
@article{karpukhin2020dense,
  title={Dense Passage Retrieval for Open-Domain Question Answering},
  author={Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih},
  journal={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year={2020}
}
```