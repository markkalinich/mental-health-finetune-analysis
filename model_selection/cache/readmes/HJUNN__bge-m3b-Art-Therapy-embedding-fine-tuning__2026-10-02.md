---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:573
- loss:MultipleNegativesRankingLoss
base_model: BAAI/bge-m3
widget:
- source_sentence: 지붕이 없는 집이 간단한 선으로만 그려져 있습니다.
  sentences:
  - ■ 목의 생략： 10대 후반에게서 많이 나타나는 그림 양상으로, 아직 사회적으로 미성숙한 부분이 존재함을 말한다 성인의 경우, 태어날 때 부터
    신체적 어려움을 겪었을 수 있다 아동의 경우, 사회 적응에 어려움을 겪을 수 있다 목젖을 그린다. 또는 강조한다 자신의 성 역할에 혼란을 겪고
    있을 수 있다 남성다움을 강력하게 바라고 남자답고 싶다고 표현한다 일부의 경우, 동성애적 성적기호를 가진 경우가 존재한다. 단 이것이 성적기호를
    판가름하는 판단기준이 되어서는 안 된다
  - ■ 지붕이 없다 지능 발달이 뒤쳐져 있을 수 있다. 단 이것이 지능 발달의 수준을 판가름 하는 진단기준이 되어서는 안 된다. 자신을 표현하는
    방법을 완전히 잃어 버린 경우가 존재한다 단순한 직선, 또는 1차원 적으로 간단히 지붕을 표현한다 매우 경직되어 있다 남에게 잘 어울리지 못
    한다
  - '* 다리와 발 다리와 발은 세상을 딛고 있는 우리의 몸이다. 다리가 굳건하게 뻗어있어야 우리가 안정감을 느끼며, 어디든 두 발로 걸어갈 수
    있는 능동적인 역할을 하기도 한다. 사회적인 부분에서 한 사람이 어떻게 행동하는가 알아볼 수 있는 지표이다'
- source_sentence: 집의 구조물 위에 크고 작은 굴뚝들이 빼곡히 배치되어 있다.
  sentences:
  - 9. 위급한 상황임을 의심해 볼 수 있는 묘사 다음과 같은 그림의 묘사가 반복해서 나타날 경우, 상대방이 정신적으로 극도로 혼란스럽거나 위험한
    상태임을 암시할 수 있다. (Donald P. Ogdon, 1981) 단 이것이 정신적 어려움을 판단하는 진단기준이 되어서는 안 된다. •
    남성이 지나치게 큰 머리를 그린다 • 머리만 똑 떼어 그린다 • 눈을 그리지 않는다 • 옆 모습 그림에서 눈을 두 개 그린다 • 머리카락이
    없다 • 이빨을 그린다 • 괴물, 귀신 혹은 동물을 그린다 • 기괴한 얼굴 표정을 그린다 • 비정상적으로 길고 얇은 목을 그린다 • 몸통만
    그린다 • 기계, 또는 로봇을 그린다 • 사각형, 또는 기하학적인 몸통을 그린다 • 어깨가 없다 • 팔이 없다 • 팔을 날개처럼 그렸다 •
    관절을 매우 강조했다 • 손이 없다 • 남자가 그린 ‘여성’ 그림에서 지나치게 가슴을 크게 그렸다 • 발이 없다 • 자세가 경직되어 있다 •
    성기를 그린다 • 옷을 입지 않았다 • 옷 속이 비치듯, 몸의 세부사항을 그린다 • 단추를 강조한다 • 장기 내부를 표현한다 • 허리 아래를
    그리기 거부한다 • 줄 몇개로 허리 아래를 표시한다 • 뒷 모습을 그린다 • 옆 얼굴과 앞 얼굴이 뒤섞여있다 • 빙빙 돌고 있거나 과한 움직임을
    나타낸다 • 토막난 사람을 그린다
  - ■ 많은 굴뚝을 그린다 자신이 성적으로 충동적임에 대하여 염려하고 있다 나 자신이 성적으로 만족스럽지 못하다는 표시가 될 수 있다. (이와
    같은 경우, 자신과 다른 다른 성별에 대하여 부적절한 언급을 하는 경우가 있다.) 굴뚝을 그리지 않는다 가족 관계에서 따뜻함을 느끼지 못했다는
    표시가 될 수 있다. 단, 자신이 살던 집 (단독주택, 아파트, 빌라 등)을 표현한 경우에는 해당되지 않을 수 있다. 성적 만족감을 느끼지
    못한다는 표현일 수 있다. 단 이것은 극도로 심각한 수준은 아니다.
  - ■ 연기가 나는 굴뚝을 그린다 연기가 왼쪽에서 오른쪽으로 적당한 수준으로 있다면, 정상적인 경우가 많다. 단 일정 수준 과하게 그린다면 보수적인
    태도를 드러내는 경향이 될 수 있다. (이와 같은 경우, 자신의 성별에 대하여 당연한 사회적 관습을 언급한다. "남자라면 당연히" 또는 "여자라면
    당연히") 연기가 오른쪽에서 왼쪽으로 불어간다면, 세상에 대해 불신과 회의적인 태도를 가지고 있다. (이와 같은 경우 무언가에 '압박을 받고
    있다'고 표현한다.) 연기가 오른쪽과 왼쪽 양측으로 불어간다면, 정신적인 고통을 극심하게 겪고 있을 수 있으며 이로인해 현실판단이 극도로 어려운
    상태일 수 있다. 단 이것이 정신적인 고통을 판가름하는 진단기준이 되어서는 안 된다.
- source_sentence: 이미지에서 머리 부분이 비어 있는 인물이 보입니다.
  sentences:
  - ■ 눈을 크게 그린다 무언가를 알고 싶어한다 알아보고, 조사하고, 느끼는 것을 좋아한다 외부 세계에 대해 내가 '손해'입는 것에 대하여 극도로
    집착할 수 있다 눈을 작거나 눈을 감은 그림을 그린다 무언가를 외면하고 싶어한다 또는 세상일에 관심이 '없어 보일 수' 있다 걱정 또는 힘든
    일에 사로잡혀 있다 어떤 과거 경험 중, 무언가를 본 것에 대해 죄책감을 가진다 눈을 그리지 않는다 아동의 경우, 일상생활 또는 학교생활 등에
    적응을 힘들어 할 수 있다 타인의 상태가 양호하지 않은경우, 다음을 고려할 수 있다 1) 성적인 부분에서, 타인을 보며 남 몰래 부적절한 성적
    흥분을 가질 수 있다 2) 환각또는 ,환시 , 또는 영적인 것을 볼 수 있다 3) 정신이 극도로 혼란스러운 사람일 수 있다.
  - '* 단추 단추는 ''어머니''를 나타낸다. ''어머니와 같은'' 따뜻하고 포근한 느낌을 주는 인상이 드러날 수 있다. -단추를 강조한다.
    또는 단추를 제 위치에 그리지 않는다. 의존하려는 마음이 크다 정신적으로 유아스럽다 나이에 맞지 않은 생각 및 행동양상을 보인다 -가운데 줄줄이
    강조되어 있는 단추들이 있다 자기 자신을 위해 이기적으로 행동한다 신체 일부에 집착한다 -장식용 단추, 브로치, 또는 의류 장신구를 그린다
    생각이나 행동을 통해 완벽함을 추구하는 경향이 있다'
  - ■ 머리를 그리지 않는다 불쾌한 생각을 떠올리기 싫어한다 상대방이 심리적으로 어려워 보이는 경우에 한하여, 다음과 같은 증세를 예측해 볼 수
    있다. 단 이것이 심리적 어려움, 또는 신체적 어려움을 판단하는 진단기준이 되어서는 안 된다. 1) 극도의 스트레스를 받고 있음 2) 정신적으로
    혼란한 상태임
- source_sentence: 굴뚝이 평면적으로 표현되어 있으며, 배경과 구별되지 않는다.
  sentences:
  - ■ 평면적인 또는 단순하고 2차원적인 굴뚝을 그린다 남자의 경우, 성적으로 만족하고 있지 못하다는 느낌의 표현이 될 수 있다. 또는 동성애적
    경향을 드러낼 수 있다. (이와 같은 경우, 자신의 성에 대해 불만족스러운 모습을 보인다.) 단 이것이 성적기호를 판가름하는 판단 기준이 되어서는
    안 된다.
  - ■ 매우 거대한 나무를 그린다 공격적인 모습을 보인다. 타인을 지배하려 든다. 내가 힘들었던 일에 대하여 보상을 받기를 원한다 무언가 환상적인
    것에 심취해 있을 수 있다 타인의 자극에 대하여 과민하게 반응한다 언덕위에 나무가 거대하게 있는 경우, 어떤 것을 지배하고 차지하는 것을 암시하기도
    한다. 아동의 경우, 부모나 가족, 또는 선생님과 같은 자기보다 권위적인 사람을 무시하려는 표현이기도 하다. (이와 같은 경우, 아동이 자기중심적으로
    행동하고 이기적인 면모를 보인다.)
  - ■ 코를 크게 그린다 성적으로 불만족한 상태이다. 또는 성적으로 원활하지 못한 경험을 가지고 있다 청소년의 경우, '남자다운 역할'을 추구하나
    그를 원활이 이행하지 못한 경우 많이 드러난다. 극도로 큰 코를 그린다 갱년기 우울함을 겪는 남성에게서 많이 드러나는 그림 양상이다 코를 그리지
    않는다 아동의 경우, 수줍은 성격이고 무언가를 책임지지 못하며, 평소에 우울한 기분을 많이 느낄 수 있다
- source_sentence: '"위급한 상황에서 빠른 결정을 위해 사용되는 이분법적 질문의 예시입니다."'
  sentences:
  - ■ 기형적인 머리를 그린다 상대방이 심리적으로 어려워 보이는 경우에 한하여, 다음과 같은 증세를 예측해 볼 수 있다. 단 이것이 심리적 어려움,
    또는 신체적 어려움을 판단하는 진단기준이 되어서는 안 된다. 1) 뇌 손상을 입은 경우 2) 지능발달이 원활이 이루어지지 않은 경우 3) 심리적으로
    극도로 혼란스러운 경우 자신과 다른 성별의 머리를 눈에 띄게 크게 그린다 이성이 자신의 성별보다 훨신 유능하고 우월한 능력이 있다고 믿는다.
    성인 남성의 경우, 어머니에 대한 정서적인 문제를 가질 수 있다.
  - ■ 1번. 네/아니오 를 이끌어 내는 질문 원하는 답을 재빠르게 얻는다는 장점이 있다. 이는 위급한 상황에서 매우 유용한데, 만약 상대방의
    의사와 상관없이 위기상황을 판단해야 하는 경우에 매우 효과적으로 사용된다. → 당신은 혹시 현재 자살에 대한 생각이 있으십니까? 단점으로는
    질문을 받는 사람에 대한 의견 표출의 기회가 단 두개로 국한됨으로, 상대방이 의도한 정확한 느낌을 무시해버리는 경우가 있다. → 자살을 하고
    싶은 이유는 무엇인지, 또는 언제부터 그런 생각을 하게 됬는지에 대해 알 수 없다. 그러므로 확실하게 답을 알아야겠다고 판단되는 경우에 이러한
    질문을 사용하여야 한다.
  - ■ 구름 처럼 뭉글뭉글한 수관을 그린다 현실을 부정하려 한다. (이와 같은 경우 적극적으로 망상 및 공상에 빠지며 현실적인 면모를 부정하려
    한다. ex. 돈, 학업, 친구 등) 전반적으로 힘이 없고 에너지가 없어 축 쳐진 느낌을 준다 아무렇게나 수관을 그린다 혼란스러운 상태이다
    또는 무언가에 강하게 몰입되고 흥분되는 상태일 수 있따 충동적인 기분, 또는 불안정한 느낌을 받는다
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on BAAI/bge-m3

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3). It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) <!-- at revision 5617a9f61b028005a4858fdac845db406aefb181 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 1024 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False, 'architecture': 'XLMRobertaModel'})
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    '"위급한 상황에서 빠른 결정을 위해 사용되는 이분법적 질문의 예시입니다."',
    '■ 1번. 네/아니오 를 이끌어 내는 질문 원하는 답을 재빠르게 얻는다는 장점이 있다. 이는 위급한 상황에서 매우 유용한데, 만약 상대방의 의사와 상관없이 위기상황을 판단해야 하는 경우에 매우 효과적으로 사용된다. → 당신은 혹시 현재 자살에 대한 생각이 있으십니까? 단점으로는 질문을 받는 사람에 대한 의견 표출의 기회가 단 두개로 국한됨으로, 상대방이 의도한 정확한 느낌을 무시해버리는 경우가 있다. → 자살을 하고 싶은 이유는 무엇인지, 또는 언제부터 그런 생각을 하게 됬는지에 대해 알 수 없다. 그러므로 확실하게 답을 알아야겠다고 판단되는 경우에 이러한 질문을 사용하여야 한다.',
    '■ 기형적인 머리를 그린다 상대방이 심리적으로 어려워 보이는 경우에 한하여, 다음과 같은 증세를 예측해 볼 수 있다. 단 이것이 심리적 어려움, 또는 신체적 어려움을 판단하는 진단기준이 되어서는 안 된다. 1) 뇌 손상을 입은 경우 2) 지능발달이 원활이 이루어지지 않은 경우 3) 심리적으로 극도로 혼란스러운 경우 자신과 다른 성별의 머리를 눈에 띄게 크게 그린다 이성이 자신의 성별보다 훨신 유능하고 우월한 능력이 있다고 믿는다. 성인 남성의 경우, 어머니에 대한 정서적인 문제를 가질 수 있다.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 1024]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.5284, 0.2025],
#         [0.5284, 1.0000, 0.1227],
#         [0.2025, 0.1227, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 573 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 573 samples:
  |         | sentence_0                                                                         | sentence_1                                                                           |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                               |
  | details | <ul><li>min: 11 tokens</li><li>mean: 21.47 tokens</li><li>max: 38 tokens</li></ul> | <ul><li>min: 51 tokens</li><li>mean: 140.53 tokens</li><li>max: 347 tokens</li></ul> |
* Samples:
  | sentence_0                                            | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  |:------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>화면 왼쪽 하단에는 작은 새가 앉아 있습니다.</code>                | <code>■ 두 번째로 '왜 그것을 그렸는가(Why?)'에 대한 전략이다. 어떤 대상을 그렸는지 명확히 파악이 되었다면, 그 대상을 어떤 이유로 그렸는지 유추해 보는 과정이 필요하다.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | <code>그림 속에는 메마른 뿌리가 꼬여 있는 모습이 보입니다.</code>           | <code>■ 죽은 뿌리를 그린다 현실을 살아갈 수 있는 능력을 잃어버린 듯한 느낌을 받는다 자신이 가지고 있던 '삶의 목표' 또는 '동기 부여'를 잃어버렸던 적이 존재한다. (이와 같은 경우, 삶을 살아가며 혼란스럽다고 표현한다.) 무언가에 극도로 절박하게 매달리듯이, 반복적으로 한 주제에 대하여 상상하고 행동한다. (이와 같은 경우, 목적과 행동이 뒤바뀐 듯한 인상을 준다. ex. 깨끗하기 위해서 손을 씻는 것이 아닌 손을 씻기 위해 미친듯이 깨끗해지길 바람. 수업을 듣기 위해 제 시간에 맞춰 일어나는 것이 아닌 모든 계획대로 행동해야 수업이라는 '관문'을 통과했다고 생각함.)</code>                                                                                                                                                                                                                                                                                                                                        |
  | <code>한 남성이 비정상적으로 큰 머리와 긴 목을 가진 인물을 그리고 있습니다.</code> | <code>9. 위급한 상황임을 의심해 볼 수 있는 묘사 다음과 같은 그림의 묘사가 반복해서 나타날 경우, 상대방이 정신적으로 극도로 혼란스럽거나 위험한 상태임을 암시할 수 있다. (Donald P. Ogdon, 1981) 단 이것이 정신적 어려움을 판단하는 진단기준이 되어서는 안 된다. • 남성이 지나치게 큰 머리를 그린다 • 머리만 똑 떼어 그린다 • 눈을 그리지 않는다 • 옆 모습 그림에서 눈을 두 개 그린다 • 머리카락이 없다 • 이빨을 그린다 • 괴물, 귀신 혹은 동물을 그린다 • 기괴한 얼굴 표정을 그린다 • 비정상적으로 길고 얇은 목을 그린다 • 몸통만 그린다 • 기계, 또는 로봇을 그린다 • 사각형, 또는 기하학적인 몸통을 그린다 • 어깨가 없다 • 팔이 없다 • 팔을 날개처럼 그렸다 • 관절을 매우 강조했다 • 손이 없다 • 남자가 그린 ‘여성’ 그림에서 지나치게 가슴을 크게 그렸다 • 발이 없다 • 자세가 경직되어 있다 • 성기를 그린다 • 옷을 입지 않았다 • 옷 속이 비치듯, 몸의 세부사항을 그린다 • 단추를 강조한다 • 장기 내부를 표현한다 • 허리 아래를 그리기 거부한다 • 줄 몇개로 허리 아래를 표시한다 • 뒷 모습을 그린다 • 옆 얼굴과 앞 얼굴이 뒤섞여있다 • 빙빙 돌고 있거나 과한 움직임을 나타낸다 • 토막난 사람을 그린다</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `num_train_epochs`: 2
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 2
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Framework Versions
- Python: 3.12.12
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.8.0+cu126
- Accelerate: 1.11.0
- Datasets: 4.0.0
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->