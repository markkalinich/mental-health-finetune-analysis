---
license: mit
datasets:
- byeolki/Llama-KoEmpathy-Dataset
language:
- ko
base_model:
- unsloth/Meta-Llama-3.1-8B
- meta-llama/Llama-3.1-8B
tags:
- korean
- 한국어
- empathy
- 공감
- chatbot
- 챗봇
- transformers
---
# 🤗 Llama-KoEmpathy 💝

Llama-KoEmpathy는 Llama-3.1-8B를 AIHub 공감형대화 데이터셋으로 파인튜닝한 언어 모델입니다. 이 모델은 사용자의 감정을 이해하고 공감하는 대화를 생성하는 것을 목표로 합니다. 💭✨<br>

*Built with Llama*

## ✨ Features
- LLaMA 아키텍처 기반 한국어 챗봇
- 감정 인식 및 공감 능력
- LoRA를 활용한 효율적인 파인튜닝

## ⚠️ Licensing Notice

이 모델은 Llama 3.1 Community License에 따라 제공됩니다. 모델 사용 시 다음 사항을 준수해야 합니다:
- Meta의 [Acceptable Use Policy](https://llama.meta.com/llama3_1/use-policy)를 따라야 합니다
- 월간 활성 사용자가 7억명을 초과하는 제품/서비스에 사용할 경우 Meta의 별도 라이선스가 필요합니다

## 📋 Model Description

- 🦙 Base Model: unsloth/Meta-Llama-3.1-8B
- 📚 Dataset: [AIHub 공감형대화](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71305)
- 🔧 Training Method: LoRA (r=16, alpha=16)

## ⚙️ Training Configuration

- 📏 Max Sequence Length: 2048
- 📦 Batch Size: 128
- 🔄 Gradient Accumulation Steps: 4
- 📈 Learning Rate: 2e-4
- 🛠️ Optimizer: AdamW 8bit
- 💾 Quantization: GGUF q8_0
- 🔁 Training Epochs: 3

TIP: 데이터의 크기나 Epoch을 늘리면 좀 더 좋은 결과를 가져올 수 있을거에요!

## 💻 Usage
모델을 사용하는 방법은 다음과 같습니다:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
max_length = 512
temperture = 0.7

model_name = "byeolki/Llama-KoEmpathy"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
prompt = """아래는 작업을 설명하는 지시사항입니다. 입력된 내용을 바탕으로 적절한 응답을 작성하세요.
### 지시사항:
입력에 대해서 공감해주세요.
### 입력:
{input}
### 응답:
"""
input_text = "안녕하세요. 저 오늘 기분이 안 좋아요."

inputs = tokenizer(prompt.format(input=input_text), return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_length=max_length,
    temperature=temperture,
    top_p=0.9,
    do_sample=True,
    pad_token_id=tokenizer.pad_token_id,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
    num_return_sequences=1
)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
try:
    response = generated_text.split("### 응답:\n")[-1].strip()
except:
    response = generated_text
print(response)
```

## 💬 Example Conversations

👤 User: 나 오늘 속상한 일이 있었어. <br>
🤖 Assistant: 무슨 일인데 그래? 기분이 많이 안 좋았나 보네.

👤 User: 나 살이 너무 많이 찐거 같아서 속상해. <br>
🤖 Assistant: 살이 쪄서 속상하다니. 왜 그래?

## ⚖️ License

MIT License

Copyright (c) 2024 byeolki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 📝 Notice

Llama 3.1 is licensed under the Llama 3.1 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.