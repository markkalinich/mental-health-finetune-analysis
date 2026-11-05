---
license: mit
language:
- ko
base_model:
- gogamza/kobart-base-v2
pipeline_tag: summarization
---

# kobart-summarization-counseling
- 이 모델은 [kobart-base-v2](https://huggingface.co/gogamza/kobart-base-v2)의 fine-tuned 모델로, [심리상담 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71806), [복지 분야 콜센터 상담데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=470)를 사용하여 심리 상담 대화문 요약 작업에 대해 학습한 모델입니다.

## Evaluations
Validation set
- Rouge-L F1: 0.26156

## Datasets
### AI-Hub (https://www.aihub.or.kr)
- [심리상담 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71806)
- [복지 분야 콜센터 상담데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=470)

## Usage
- transformers: v4.45.2
```bash
pip install torch transformers
```
```python
import torch
from transformers import BartForConditionalGeneration, PreTrainedTokenizerFast

tokenizer = PreTrainedTokenizerFast.from_pretrained("shlee5784/kobart-summarization-counseling-v1")
model = BartForConditionalGeneration.from_pretrained("shlee5784/kobart-summarization-counseling-v1")

text = """
상담자:김○○님, 오늘 이 자리에 오신 것만으로도 충분히 의미 있는 시작이에요. 지금 어떤 어려움을 겪고 계신지 천천히 이야기해 주셔도 괜찮습니다.
내담자:몇 달 전부터 아무것도 하고 싶지 않아요. 잠도 잘 안 오고, 회사 일도 집중이 안 되다 보니 자꾸 실수를 해요. 사람을 만나는 것도 피하게 되고, 그냥 사는 게 의미 없다는 생각이 계속 들어요.
상담자:그런 생각이 반복되면 많이 지치고 힘드셨을 것 같아요. 요즘에도 그런 무의미한 감정이 자주 드시나요?
내담자:네, 거의 매일 그래요. 아침에 눈뜨는 것도 버겁고, 그냥 누워 있고 싶어요. 가끔은 이렇게 사는 게 무슨 의미가 있나 싶고, 모든 걸 끝내고 싶다는 생각도 들긴 해요. 하지만 실제로 뭘 하진 않았어요.
상담자:그럴 때 마음을 진정시키거나 스스로를 달래기 위해 해보셨던 방법이 있으실까요?
내담자:잠을 자려고 애쓰거나 이어폰 끼고 음악을 듣기도 해요. 친구한테 연락할까 생각은 하지만 괜히 더 피곤해질까 봐 망설이게 돼요.
상담자:잘 견디고 계셨네요. 지금 말씀해 주신 걸 보면 우울감이 꽤 오랫동안 지속되고 있고, 수면이나 집중 같은 일상 기능에도 영향을 주고 있는 것 같아요. 자살에 대한 생각은 드시지만 구체적인 계획은 없으신 거죠?
내담자:네. 그냥 생각만 들어요. 부모님하고 동생이 있어서 자주 보진 않지만 연락은 주고받아요.
상담자:지금 중요한 건 ○○님이 안전하게 이 시기를 지나가실 수 있도록 도와드리는 거예요. 오늘은 우선 위기 상황에서 사용할 수 있는 안전계획부터 함께 만들어 볼게요. 믿고 연락할 수 있는 사람, 마음을 안정시킬 수 있는 방법, 그리고 도움이 필요할 때 연락할 수 있는 기관 정보도 함께 안내드릴 거예요.
내담자:알겠습니다.
상담자:그리고 다음 상담부터는 생각의 흐름을 함께 점검하고, 조금씩 균형을 찾을 수 있도록 돕는 인지행동치료를 시작해보려 해요. 그 과정에서 ○○님이 자주 떠올리는 부정적인 생각들을 다루게 될 거예요. 부담이 크지 않도록 천천히 진행할 테니 편하게 임해주시면 좋겠습니다.
내담자:해볼게요.
상담자:잘 따라와 주셔서 감사해요. 오늘 이야기해주신 내용은 아주 중요한 첫걸음이었고, 상담이 끝난 뒤 48시간 이내에 전화로 안부를 한 번 여쭤볼 예정이에요. 필요한 경우 정신과적인 평가도 함께 고려해볼 수 있어요. 다음 상담에서 조금 더 편안한 마음으로 뵐 수 있기를 바라요.
내담자:감사합니다.
"""

raw_input_ids = tokenizer.encode(text)
input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

summary_ids = model.generate(torch.tensor([input_ids]), num_beams=5, max_length=512, eos_token_id=1, no_repeat_ngram_size=3)
tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
```
```python
output: "증상:내담자는 몇 달 전부터 시작된 지속된 우울감과 무기력감을 호소하며, 일상 기능 저하와 자살 생각을 경험하고 있다. 수면장애와 집중력 저하, 대인기피도 나타나고 있다. 대응:상담자는 내담자의 감정을 공감하며 안전계획을 수립하고, 인지행동 치료를 통해 생각의 흐름을 점검하고 부정적인 사고를 다루도록 지도할 예정이다. 또한 위기 상황에서 안전계획 수립과 심리적 지지를 제공하며, 내담자가 편안하게 상담에 임할 수 있도록 안내하였다."
```
### Input type
```python
"""
상담자:<상담자 텍스트>
내담자:<내담자 텍스트>
상담자:<상담자 텍스트>
...
"""
```

## License
Licensed under the [modified MIT](LICENSE) License.