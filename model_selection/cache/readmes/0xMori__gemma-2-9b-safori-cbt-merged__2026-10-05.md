---
library_name: transformers
base_model:
- google/gemma-2-9b-it
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

# 🧠 Doran-i (CBT Counseling Specialist)

![Model Architecture](https://img.shields.io/badge/Model-Gemma_2_9B-blue) ![Task](https://img.shields.io/badge/Task-CBT_Counseling-green) ![Technique](https://img.shields.io/badge/Technique-QLoRA_Fine_Tuning-orange) ![Status](https://img.shields.io/badge/Status-Stable_Release-brightgreen)

## 📖 Model Details

### Model Description

**Doran-i(도란이)**는 구글의 고성능 오픈 모델인 `gemma-2-9b-it`를 기반으로, **CBT(인지행동치료) 기법**을 수행할 수 있도록 정교하게 미세조정(Fine-tuning)된 한국어 심리 상담 AI 모델입니다.

기존 `Gemma 3`의 실험적 아키텍처 대신, 검증된 성능과 안정성을 자랑하는 **Gemma 2 9B**를 채택하여 한국어 뉘앙스 파악 능력과 상담의 깊이를 대폭 강화했습니다.

단순한 위로를 넘어, 내담자의 말 속에 숨겨진 **12가지 인지 왜곡(Cognitive Distortion)**을 탐지하고, **소크라테스식 질문(Socratic Questioning)**을 통해 내담자가 스스로 부정적 사고의 고리를 끊도록 돕습니다.

- **Developed by:** Kong Yoonseo (0xMori) @ Safori
- **Model type:** Causal Language Model (QLoRA Fine-tuned)
- **Language(s):** Korean (한국어)
- **License:** Gemma Terms of Use
- **Base Model:** `google/gemma-2-9b-it`
- **Hardware:** Trained on NVIDIA T4, Merged on TPU v5e-8

### Model Sources

- **Repository:** [https://huggingface.co/0xMori/gemma-2-9b-safori-cbt-merged](https://huggingface.co/0xMori/gemma-2-9b-safori-cbt-merged)
- **Service Github:** [[Team Safori](https://github.com/safori-team)]

## 🎯 Uses

### Direct Use (JSON Output)
이 모델은 구조화된 JSON 형식으로 상담 결과를 출력하도록 훈련되었습니다:
```json
{
  "emotion": "sad",
  "empathy": "내담자의 감정에 대한 깊은 공감 멘트",
  "detected_distortion": "흑백논리",
  "analysis": "내담자가 왜 그런 생각을 하게 되었는지에 대한 분석",
  "socratic_question": "반박 증거를 찾도록 유도하는 질문",
  "alternative_thought": "긍정적 대안 사고 예시"
}
```

### Out-of-Scope Use (사용 제한)
- **의료적 진단:** 이 모델은 의사가 아니며, 정신질환을 진단하거나 약물을 처방할 수 없습니다.
- **즉각적인 위기 개입:** 자살/자해 등 응급 상황 발생 시 핫라인 안내가 필요합니다.

## 💻 How to Get Started

**Hugging Face Transformers** 라이브러리를 사용하여 바로 실행할 수 있습니다.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Merged Model (어댑터 병합 완료)
model_id = "0xMori/gemma-2-9b-safori-cbt-merged"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16
)

# Alpaca 포맷 (학습 시 사용한 포맷 준수 권장)
prompt = """당신은 전문적인 인지행동치료(CBT) AI 상담사 '도란이'입니다.
### 사용자 입력:
사람들이 다 나를 싫어하는 것 같아서 모임에 나가기가 두려워.
### 응답 (JSON):
""

input_ids = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(
    **input_ids,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## ⚙️ Training Details

### Training Data
- **Custom Dataset (Safori CBT):** 인지행동치료 이론을 바탕으로 자체 구축한 고품질 한국어 상담 대화셋 (약 400건).
- **Preprocessing:**
    - `Input(내담자 발화)` - `Output(JSON 구조)` 형태의 Alpaca 프롬프트 포맷 적용.
    - 다양한 인지 왜곡 유형(흑백사고, 과잉일반화 등)을 골고루 분포시킴.

### Training Procedure
- **Technique:** QLoRA (Quantized Low-Rank Adaptation)
- **Optimization Strategy:**
    - **Early Stopping:** Training Loss 0.65 도달 시 과적합 방지를 위해 조기 종료.
    - **Stable Environment:** 호환성 이슈가 있는 Unsloth 대신 **Pure Hugging Face (TRL 0.8.6)** 라이브러리 사용.

- **Hyperparameters:**
    - Learning Rate: 2e-4
    - Batch Size: 1 (Gradient Accumulation: 8) -> Effective Batch Size 8
    - Optimizer: paged_adamw_8bit
    - Quantization: 4-bit (NF4)
    - LoRA Rank (r): 16, Alpha: 16
    - Max Sequence Length: 2048
