---
license: mit
language:
- ko
base_model:
- beomi/KcELECTRA-base
pipeline_tag: text-classification
tags:
- digitalhumanities
- emotion
- classification
---

**KPoEM (Korean Poetry Emotion Mapping) 모델**은 한국 근대시에 특화된 KcELECTRA 기반의 감정 분류 모델로, [KcELECTRA-base](https://huggingface.co/beomi/KcELECTRA-base/tree/main)에 [KOTE dataset](https://huggingface.co/datasets/searle-j/kote)을 파인튜닝한 모델을, 다시 KPoEM dataset으로 파인튜닝하여 구현한 모델입니다.

# Contributors
 LIM, I., Ji, H., & Kim, B.
 The study is associated with the following publication:

## 🖌️ Citations
* LIM, I., Ji, H., & Kim, B. (2026). KPoEM: A Human-Annotated Dataset for Emotion Classification and RAG-Based Poetry Generation in Korean Modern Poetry. *The Review of Korean Studies, 29*(1), 161-206. [10.25024/review.2026.29.1.006](https://doi.org/10.25024/review.2026.29.1.006)
  - 📄 Prerprint Paper: [KPoEM: A Human-Annotated Dataset for Emotion Classification and RAG-Based Poetry Generation in Korean Modern Poetry](https://arxiv.org/abs/2509.03932)
 
# Resources
모델 학습에 사용한 자원들은 아래 링크에서 확인하실 수 있습니다.
- 데이터세트: Zenodo, [KPoEM dataset](https://zenodo.org/records/15572285) Hugging Face, [KPoEM dataset](https://huggingface.co/datasets/AKS-DHLAB/KPoEM)
- 파인튜닝 소스코드: GitHub, [AKS-DHLAB/KPoEM](https://github.com/AKS-DHLAB/KPoEM)

# Model
KPoEM 모델의 활용은 다음의 코드를 참고해 주시기를 바랍니다.

```
# 필요 라이브러리 설치 (최초 1회만 실행)
!pip install -q transformers torch huggingface_hub

# 라이브러리 임포트
import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import hf_hub_download


# 기초 세팅
REPO_ID = "AKS-DHLAB/KPoEM"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# KPoEM_Classifier 클래스
class KPoEM_Classifier(nn.Module):

    # 클래스 생성 시 모든 초기화(모델/토크나이저/가중치 로드) 수행
    def __init__(self, repo_id, device):
        self.labels = [
            '불평/불만', '환영/호의', '감동/감탄', '지긋지긋', '고마움', '슬픔', '화남/분노', '존경',
            '기대감', '우쭐댐/무시함', '안타까움/실망', '비장함', '의심/불신', '뿌듯함', '편안/쾌적',
            '신기함/관심', '아껴주는', '부끄러움', '공포/무서움', '절망', '한심함', '역겨움/징그러움',
            '짜증', '어이없음', '없음', '패배/자기혐오', '귀찮음', '힘듦/지침', '즐거움/신남', '깨달음',
            '죄책감', '증오/혐오', '흐뭇함(귀여움/예쁨)', '당황/난처', '경악', '부담/안_내킴', '서러움',
            '재미없음', '불쌍함/연민', '놀람', '행복', '불안/걱정', '기쁨', '안심/신뢰'
        ]
        num_labels = len(self.labels)

        super().__init__()
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(repo_id)
        self.electra = AutoModel.from_pretrained(repo_id)
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.1),
            nn.Linear(self.electra.config.hidden_size, num_labels)
        )

        weights_path = hf_hub_download(repo_id=repo_id, filename="classifier_state.bin")
        self.classifier.load_state_dict(torch.load(weights_path, map_location=self.device))
        self.to(self.device)
        self.eval()

    # 텍스트를 입력받아 최종 logits 반환
    def forward(self, text: str):
        encoding = self.tokenizer(
          text,
          add_special_tokens=True,
          max_length=512,
          padding="max_length",
          truncation=True,
          return_tensors='pt',
        ).to(self.device)

        with torch.no_grad():
            outputs = self.electra(
                input_ids=encoding["input_ids"],
                attention_mask=encoding["attention_mask"],
                token_type_ids=encoding["token_type_ids"]
            )

        pooled_output = outputs.last_hidden_state[:, 0, :]
        logits = self.classifier(pooled_output)
        return logits

    # 텍스트 분석 결과 반환
    def analyze(self, text: str, threshold=0):
        logits = self.forward(text)
        probabilities = torch.sigmoid(logits.squeeze())
        predictions = (probabilities > threshold).int()

        detected_emotions = []
        for i, label_id in enumerate(predictions):
            if label_id == 1:
                emotion = self.labels[i]
                probability = probabilities[i].item()
                detected_emotions.append((emotion, probability))
        
        # 확률값을 기준으로 내림차순 정렬
        detected_emotions.sort(key=lambda x: x[1], reverse=True)
        return detected_emotions


# KPoEM 모델 로드
print(f"... '{DEVICE}' 환경에서 '{REPO_ID}' 모델을 로드하고 있습니다 ...")
kpoem_model = KPoEM_Classifier(repo_id=REPO_ID, device=DEVICE)
print("KPoEM 모델을 성공적으로 로드하였습니다.")
```

상기 코드의 대화형 환경에서의 실행 결과는 다음과 같습니다.

```
... 'cpu' 환경에서 'AKS-DHLAB/KPoEM' 모델을 로드하고 있습니다 ...
KPoEM 모델을 성공적으로 로드하였습니다.
```

다음은 로드한 모델을 실행하는 예시 코드입니다.

```
# 예시1
example1 = "나의 생은 미친듯이 사랑을 찾아 헤매었으나"
result1 = kpoem_model.analyze(example1)
result1
```

다음은 예시 코드를 실행한 결과입니다.

```
[('슬픔', 0.9469444751739502),
 ('서러움', 0.937518298625946),
 ('안타까움/실망', 0.9196950793266296),
 ('불안/걱정', 0.7706277966499329),
 ('힘듦/지침', 0.7137402892112732),
 ('깨달음', 0.6845079660415649),
 ('비장함', 0.6476397514343262),
 ('불쌍함/연민', 0.6128569841384888),
 ('부담/안_내킴', 0.5575793981552124),
 ('기대감', 0.4775768220424652),
 ('당황/난처', 0.4501192569732666),
 ('패배/자기혐오', 0.4364185035228729),
 ('절망', 0.4248308539390564),
 ('불평/불만', 0.3876761496067047),
 ('아껴주는', 0.3849319517612457),
 ('감동/감탄', 0.31014394760131836),
 ('신기함/관심', 0.2456621527671814),
 ('지긋지긋', 0.20546969771385193),
 ('놀람', 0.18827176094055176),
 ('한심함', 0.1782034933567047),
 ('재미없음', 0.1595412939786911),
 ('죄책감', 0.15579494833946228),
 ('부끄러움', 0.13476116955280304),
 ('환영/호의', 0.13304632902145386),
 ('의심/불신', 0.12566028535366058),
 ('존경', 0.11981170624494553),
 ('기쁨', 0.11800216883420944),
 ('행복', 0.08473784476518631),
 ('뿌듯함', 0.07957974821329117),
 ('어이없음', 0.07822196185588837),
 ('없음', 0.07102902233600616),
 ('경악', 0.07033637911081314),
 ('짜증', 0.06384478509426117),
 ('화남/분노', 0.06323148310184479),
 ('흐뭇함(귀여움/예쁨)', 0.06262417882680893),
 ('즐거움/신남', 0.06152398884296417),
 ('고마움', 0.056765031069517136),
 ('우쭐댐/무시함', 0.05257101356983185),
 ('공포/무서움', 0.05099816992878914),
 ('귀찮음', 0.043061513453722),
 ('편안/쾌적', 0.042331695556640625),
 ('안심/신뢰', 0.04192497953772545),
 ('증오/혐오', 0.03919696435332298),
 ('역겨움/징그러움', 0.013086128979921341)]
```

다음과 같이 임계값(threshold)을 임의로 줄 수도 있습니다.

```
# 예시2
example2 = '''
나의 생은 미친듯이 사랑을 찾아 헤매었으나
단 한번도 스스로를 사랑하지 않았노라
'''
result2 = kpoem_model.analyze(example2, threshold=0.3)  # 임계값 0.3으로 설정
result2
```

위와 같이 threshold 인자를 줄 경우, 확률 값이 0.3 이상인 감정만 반환됩니다.

```
[('슬픔', 0.9411415457725525),
 ('서러움', 0.9244144558906555),
 ('안타까움/실망', 0.9239906668663025),
 ('깨달음', 0.7170049548149109),
 ('불안/걱정', 0.6184237599372864),
 ('힘듦/지침', 0.6009577512741089),
 ('불쌍함/연민', 0.5903952121734619),
 ('패배/자기혐오', 0.5515390038490295),
 ('비장함', 0.5166702270507812),
 ('당황/난처', 0.48103633522987366),
 ('부담/안_내킴', 0.45452776551246643),
 ('절망', 0.4479917585849762),
 ('불평/불만', 0.388106107711792),
 ('한심함', 0.34834057092666626),
 ('아껴주는', 0.3062174916267395),
 ('부끄러움', 0.3003148138523102)]
```
 
# References
- [KcELECTRA](https://github.com/Beomi/KcELECTRA)
- [KOTE](https://github.com/searle-j/KOTE)
- [KOTE Dataset](https://huggingface.co/datasets/searle-j/kote)