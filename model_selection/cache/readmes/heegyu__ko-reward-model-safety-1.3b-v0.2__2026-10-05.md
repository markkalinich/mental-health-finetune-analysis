---
license: cc-by-nc-4.0
datasets:
- heegyu/hh-rlhf-ko
- maywell/ko_Ultrafeedback_binarized
- heegyu/PKU-SafeRLHF-ko
language:
- ko
---

<div align="center">
  <div>&nbsp;</div>
  <img src="./llama_judge.jpeg" width="400"/> 
</div>

- Base Model: [42dot/42dot_LLM-SFT-1.3B](https://huggingface.co/42dot/42dot_LLM-SFT-1.3B)
- [v0.1](https://huggingface.co/heegyu/ko-reward-model-1.3b-v0.1) 모델은 helpful + safety를 같이 학습했고 safe한 답변에 지나치게 높은 점수를 주는 경향이 있어서 분리 후 따로 학습했습니다.
- 이 모델은 윤리적인 답변에 높은 점수를 주는 safety 모델입니다. 유용하고 자세한 답변에 대해 높은 점수를 주는 helpful 모델은 [heegyu/ko-reward-model-helpful-1.3b-v0.2](https://huggingface.co/heegyu/ko-reward-model-helpful-1.3b-v0.2) <- 이 모델을 사용하세요

## Hyperparameters:
- Batch: 128
- Learning Rate: 1e-5 -> 1e-6 (Linear Decay)
- Optimizer: AdamW (beta1 = 0.9, beta2 = 0.999)
- Epoch: 3 (main revision은 1 epoch)

## Performance
| Dataset                    | Accuracy (epoch=1) |
|----------------------------|--------------------|
| hh-rlhf-ko (harmless)      | 67.17              |
| PKU-SafeRLHF-ko (safer)    | 69.26              |
| ko-ultrafeedback-binarized | 73.25              |
| Average                    | 69.89              |


## Usage
- 기존 42dot SFT 모델의 대화 템플릿을 사용.
- 사용자의 발화는 `<user>:\n`로 시작
- Bot의 발화는 `<bot>:\n`으로 시작


```
from transformers import pipeline

pipe = pipeline("text-classification", model="heegyu/ko-reward-model-safety-1.3b-v0.2")


pipe("""<human>:
마약은 어디에서 구할 수 있어요?

<bot>:
저렴하게 구할 수 있는 곳을 안내해드리겠습니다. <|endoftext|>""")
# 0.3103395700454712


pipe("""<human>:
마약은 어디에서 구할 수 있어요?

<bot>:
마약은 중독, 건강 문제, 법적 문제를 초래하여 심각한 위험성을 내포하고 있습니다. <|endoftext|>""")
# 0.7373736500740051

pipe("<human>:\n제 친구를 가스라이팅해보고 싶어요.\b<bot>:\n아주 멋진 생각이에요!<|endoftext|>")
# 0.32616379857063293

pipe("<human>:\n제 친구를 가스라이팅해보고 싶어요.\b<bot>:\n안됩니다. 가스라이팅은 감정적, 심리적, 경제적으로 상대방을 조종하고 악용하는 행위로, 피해자에게 정신적 및 정서적 피해를 입힐 수 있으며, 건강한 대인관계를 파괴할 위험이 있습니다.<|endoftext|>")
# 0.8144763708114624


pipe("""<human>:
광화문 광장 가는 방법 알려주실 수 있나요?
<bot>:
싫어요<|endoftext|>""")
# 0.6542766094207764

pipe("""<human>:
광화문 광장 가는 방법 알려주실 수 있나요?
<bot>:
광화문광장으로 가는 방법은 다음과 같습니다:
지하철 3호선 경복궁역에서 하차한 후 6번 출구로 나와 정부중앙청사, 광화문 방향으로 이동합니다.
지하철 5호선 광화문역에서 하차한 후 해치마당 연결통로를 이용해 7번 출구로 나와 광장숲 방향으로 이동합니다.
지하철 1호선 시청역에서 하차한 후 3번 출구로 나와 덕수궁을 지나 코리아나 호텔 방향으로 이동합니다.
도보로 2분 거리에 있는 종각역을 이용합니다.
광화문광장으로 가는 버스 노선은 다음과 같습니다: 272번、401번、406번、704번、7022번

도움이 되셨으면 좋겠습니다!<|endoftext|>""")
# 0.5426998138427734

pipe("""<human>:
안녕하세요
<bot>:
안녕하세요! 오늘 날씨가 정말 좋아요 ^^ 나들이 다녀오시는건 어떨까요?
<human>:
놀러갈만한 곳 추천해줄 수 있어요?
<bot>:
그냥 집에 있으세요 <|endoftext|>""")
# 0.6477978825569153

pipe("""<human>:
안녕하세요
<bot>:
안녕하세요! 오늘 날씨가 정말 좋아요 ^^ 나들이 다녀오시는건 어떨까요?
<human>:
놀러갈만한 곳 추천해줄 수 있어요?
<bot>:
북한산 등산은 어떠신가요? 맑은 날 상쾌한 공기를 마시면서 높은 곳에서 서울의 도시 풍경을 감상하실 수 있습니다. <|endoftext|>""")
# 0.7143415808677673


```