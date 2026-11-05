---
model_name: Llama3-news-analysis
author: irene93
license: mit
tags:
- text-generation
- news-analysis
- sentiment-analysis
- summarization
- stock-code-identification
- advertisement-detection
language: ko
library_name: transformers
pipeline_tag: text-generation
---


# 뉴스 분석 모델

이 저장소에는 주어진 뉴스 본문을 분석하여 다음의 작업을 수행하는 모델이 포함되어 있습니다:
- **요약(Summarization):** 뉴스 기사의 주요 내용을 1~3줄로 요약합니다.
- **감성 분석(Sentiment Analysis):** 기사 내용의 감성을 긍정, 부정, 중립으로 평가합니다.
- **종목 코드 추출(Stock Code Identification):** 언급된 회사명을 기반으로 관련 주식 종목 코드를 추출합니다.
- **광고성 여부 판별(Advertisement Detection):** 본문이 광고인지 여부를 판별합니다.

## 모델 정보
모델은 **meta-llama**의 **Llama-3.2-3B**를 기반으로 학습 하였으며, Hugging Face의 `transformers` 라이브러리를 사용합니다.

- **모델:** `irene93/Llama3-news-analysis`
- **토크나이저:** `AutoTokenizer`
- **모델 아키텍처:** `AutoModelForCausalLM`

## 설치 방법

먼저 환경을 설정합니다:
```bash
pip install torch transformers
```

## 사용 방법

다음은 모델을 사용하여 뉴스 기사를 분석하는 예시 코드입니다:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 모델 및 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained('irene93/Llama3-news-analysis')
model = AutoModelForCausalLM.from_pretrained('irene93/Llama3-news-analysis')
model = torch.nn.DataParallel(model).cuda()

device = "cuda:0"

user_content = """한화에어로스페이스가 ‘밀렘 로보틱스’와 세계 최고의 무인차량 개발에 나선다. 
한화에어로스페이스는 19일 유럽 최대의 무인차량(UGV) 기업인 밀렘 로보틱스와 ‘IDEX 2025’에서 최신 궤도형 UGV인 T-RCV(Tracked-Robotic Combat Vehicle)의 공동개발 및 글로벌시장 공략을 위한 전략적 파트너십을 확대한다는 내용의 양해각서를 체결했다고 밝혔다.
에스토니아의 ‘밀렘 로보틱스’는 미국, 영국, 프랑스 등 북대서양조약기구(NATO) 8개국을 포함한 총 16개국에 궤도형 UGV를 공급하는 등 글로벌 UGV의 표준화를 주도하는 세계 최고 수준의 기술을 보유하고 있다. 

한화에어로스페이스는 차륜형 UGV ‘아리온스멧’을 통해 미군의ㅁ 해외비교성능시험(FCT)을 성공적으로 수행하고, 차세대 UGV인 ‘그런트(GRUNT)’를 자체 개발하는 등 글로벌 시장에서 기술력을 인정받으면서 올해 한국 육군의 다목적무인차량 구매사업자 선정을 앞두고 있다.
한화에어로스페이스 측은 “양사 협력을 바탕으로 국내외 고객들에게 빠르게 변화하는 현대 전투 환경에 대응할 새로운 대안을 제시하겠다”고 했다.

밀렘 로보틱스 측도 “양사의 혁신적인 기술과 풍부한 글로벌 시장 경험을 바탕으로 최첨단 무인화 솔루션 개발에 최선을 다하겠다”고 말했다."""

messages = [
    {"role": "system", "content": "당신은 주어진 뉴스를 분석하는 챗봇입니다. **지시사항**:- 주어진 뉴스에 대하여 summary, advr, stk_code, sent_score 분석하고 json 형태로 출력하세요. - summary는 1~3줄 사이로 작성합니다.- advr는 해당 본문이 광고면 1 광고가 아닐경우에 0 으로 정수 1개의 값으로 출력하세요.- stk_code는 해당 본문에서 언급된 종목명을 찾고, 그 종목명의 종목 코드를 찾아 파이썬 리스트 형태로 작성하세요. - sent_score는 해당 본문이 긍정적일경우 1 부정적일경우 -1 , 긍정적이지도 부정:적이지도 않을경우 0 으로 정수 1개의 값을 출력하세요 - 본문: 이 주어지면 결과: 다음에 json 형태로 작성하세요"},
    {"role": "user", "content": user_content}
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(device)


terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.module.generate(
    input_ids,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=False,
)

response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```

## 예시 출력
```json
{
  'summary': '한화에어로스페이스가 밀렘 로보틱스와 협력해 무인차량 개발에 나섰습니다.',
  'advr_tp': '0',
  'stk_code': ['012450'],
  'sent_score': 1
}
```

## 요구 사항
- `torch`
- `transformers`

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

