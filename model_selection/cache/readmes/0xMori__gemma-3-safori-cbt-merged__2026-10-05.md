---
library_name: transformers
base_model:
- google/gemma-3-4b-it
- 0xMori/gemma-3-safori-cbt-v1
language:
- ko
pipeline_tag: text-generation
tags:
- mental-health
- cbt
- counseling
- psychology
- wellness
- qlora
license: gemma
---

# 🧠 Mind-Gemma (CBT Counseling Specialist)

![Model Architecture](https://img.shields.io/badge/Model-Gemma_4B-blue) ![Task](https://img.shields.io/badge/Task-CBT_Counseling-green) ![Technique](https://img.shields.io/badge/Technique-QLoRA_Fine_Tuning-orange)

## 📖 Model Details

### Model Description

**Mind-Gemma**는 구글의 경량 거대 언어 모델인 `gemma-3-4b-it`를 기반으로,  **CBT(인지행동치료) 기법**을 수행할 수 있도록 특화 학습(Fine-tuning)된 한국어 심리 상담 AI 모델입니다.

기존의 LLM이 단순히 기계적인 위로를 건네는 것과 달리, Mind-Gemma는 내담자의 발화에서 **인지적 왜곡(Cognitive Distortion)** 을 포착하고, **소크라테스식 질문(Socratic Questioning)** 을 통해 내담자가 스스로 합리적인 사고를 도출하도록 유도합니다.

이 모델은 Safori의 **'마음일기(Mind Diary) 기반의 CBT 상담 챗봇(도란이)'** 서비스의 핵심 상담 엔진으로 개발되었습니다.

- **Developed by:** Kong Yoonseo (0xMori) @ Safori
- **Model type:** Causal Language Model (QLoRA Fine-tuned)
- **Language(s):** Korean (한국어)
- **License:** Gemma Terms of Use
- **Finetuned from model:** `google/gemma-3-4b-it`

### Model Sources

- **Repository:** [https://huggingface.co/0xMori/gemma-3-safori-cbt-v1](https://huggingface.co/0xMori/gemma-3-safori-cbt-v1)
- **Service Github:** [서비스 Github(https://github.com/safori-team)]

## 🎯 Uses

### Direct Use
이 모델은 다음과 같은 상황에서 최적의 성능을 발휘합니다:
- **심리 상담 챗봇:** 우울, 불안, 스트레스를 호소하는 사용자와의 1:1 대화.
- **감정 분석 및 케어:** 사용자의 일기나 텍스트에서 감정을 추출하고 적절한 피드백 제공.
- **CBT 훈련:** 인지행동치료 기법을 적용한 대화 시나리오 생성.

### Out-of-Scope Use (사용 제한)
- **의료적 진단:** 이 모델은 의사가 아니며, 정신질환을 진단하거나 약물을 처방할 수 없습니다.
- **응급 위기 상황:** 자살 위험, 자해 등 즉각적인 개입이 필요한 응급 상황에서는 사용할 수 없으며, 전문 기관 안내가 필요합니다.

## 💻 How to Get Started

아래 코드를 통해 **Mind-Gemma**와 대화를 시작할 수 있습니다.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "0xMori/gemma-3-safori-cbt-v1"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16
)

messages = [
    {"role": "user", "content": "사람들이 다 나를 싫어하는 것 같아서 모임에 나가기가 두려워."},
]

input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to("cuda")

outputs = model.generate(
    input_ids,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

print(tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True))
```

## ⚙️ Training Details
### Training Data
- Source1: AI-Hub ('웰니스 대화 스크립트')[https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=267]
- Source2: AI-Hub ('감성 대화 말뭉치')[https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=86]
- Preprocessing: - 상담사의 답변을 CBT 기법(공감 → 분석 → 반박 질문)에 맞춰 재구성.
- JSONL 포맷 변환 및 gemma Chat Template 적용.

### Training Procedure
- Technique: QLoRA (Quantized Low-Rank Adaptation)
- Hardware: NVIDIA T4 GPU (Google Colab Environment)
- Frameworks: transformers, peft, trl, bitsandbytes
- Hyperparameters
- Learning Rate: 2e-4
- Batch Size: 2 (Gradient Accumulation: 4)
- Optimizer: paged_adamw_8bit
- Quantization: 4-bit (NF4)
- LoRA Rank (r): 16
- LoRA Alpha: 16