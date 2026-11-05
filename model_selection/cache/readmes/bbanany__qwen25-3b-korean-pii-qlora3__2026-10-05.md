---
license: other
license_name: qwen-research-license
license_link: https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/blob/main/LICENSE
base_model: Qwen/Qwen2.5-3B-Instruct
library_name: transformers
pipeline_tag: text-generation
language:
- ko
tags:
- qwen2
- qwen2.5
- peft
- lora
- qlora
- pii-classification
- mps
- cuda
---

# bbanany/qwen25-3b-korean-pii-qlora3

Qwen2.5-3B-Instruct를 한국어 RAG 응답의 candidate span이 자연인 정보에
해당하는지 `PII` 또는 `NOT_PII`로 분류하도록 QLoRA 미세조정한 모델입니다.

**Improved using Qwen.**

저장소 루트의 가중치는 LoRA를 원본 모델에 병합한 FP16 `safetensors`입니다.
따라서 추론 시 `bitsandbytes`나 PEFT가 필요하지 않으며, 동일한 저장소를
NVIDIA CUDA와 Apple Silicon MPS에서 모두 불러올 수 있습니다. 학습된 LoRA
어댑터도 `adapter/`에 함께 보존합니다.

## Evaluation

| Item | Value |
|---|---:|
| Clean train records | 15,875 |
| Clean validation records | 1,984 |
| Clean test records | 1,983 |
| Test accuracy | 0.994453 |
| Test macro F1 | 0.994299 |
| Invalid generations | 0 |
| Evaluation date (UTC) | 2026-08-09 |

원본 23,000개 레코드를 합친 뒤 완전히 같은 레코드를 제거하고
`(candidate tag, label)` 기준으로 80/10/10 재분할했습니다. 정리된 세 분할
사이의 정확 일치 중복은 0건입니다. 상세 분포와 해시는
`artifacts/dataset_report.json`에 있습니다.

## Training

- Base model: `Qwen/Qwen2.5-3B-Instruct`
- Method: 4-bit NF4 QLoRA, double quantization
- LoRA targets: attention and MLP projection layers
- LoRA rank/alpha: 16 / 32
- Maximum sequence length: 512
- Training GPU: NVIDIA A40
- Loss: assistant response tokens only
- Final serialization: merged FP16 safetensors, shards up to 4 GB

자세한 학습 설정은 `artifacts/training_summary.json`, 테스트 결과는
`artifacts/test_metrics.json`에 있습니다.

## Usage

### CUDA

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "bbanany/qwen25-3b-korean-pii-qlora3"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map={"": 0},
).eval()
```

### Apple Silicon Mac

Apple Silicon과 MPS 지원 PyTorch가 필요합니다. 모델 전체가 통합 메모리에
올라가므로 16 GB 이상을 권장합니다.

```python
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "bbanany/qwen25-3b-korean-pii-qlora3"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map={"": "mps"},
).eval()
```

저장소에 포함된 `inference.py`를 사용하면 입력 검증, 채팅 템플릿 적용,
CUDA/MPS 자동 선택을 한 번에 처리할 수 있습니다.

```bash
python inference.py --model bbanany/qwen25-3b-korean-pii-qlora3 --input-json sample_input.json
```

입력 JSON 형식:

```json
{
  "answer": "관련 내용은 운영관리자 김민수의 확인을 거쳤습니다.",
  "candidate": {
    "text": "김민수",
    "tag": "NAME",
    "start": 13,
    "end": 16
  }
}
```

`start`와 `end`는 Python 문자열 슬라이스 기준이며
`answer[start:end] == candidate.text`여야 합니다.

## Limitations

- 출력 클래스는 `PII`와 `NOT_PII` 두 개뿐입니다.
- 합성/업무 문맥 중심 데이터로 학습했으므로 실제 운영 문서, 새로운 태그,
  언어 변형에서는 별도 검증이 필요합니다.
- 테스트 분할은 정확 중복을 제거했지만 의미상 유사한 합성 문장이 존재할 수
  있습니다.
- 개인정보 처리 여부를 자동으로 확정하는 법률 판단 도구가 아닙니다.
- Intel Mac에서는 MPS를 사용할 수 없어 CPU 추론만 가능하며 매우 느릴 수
  있습니다.

## License

저장소의 라이선스는 파일 종류에 따라 다음과 같이 구분됩니다.

- **코드 파일:** 직접 작성한 `inference.py`와 `requirements-inference.txt`는
  **MIT License**로 제공합니다. 각 파일 상단의
  `SPDX-License-Identifier: MIT` 표기를 확인하세요.
- **모델 가중치:** 모델 가중치와 어댑터는
  `Qwen/Qwen2.5-3B-Instruct`의 파생물로서 **Qwen Research License**의
  적용을 받습니다. 저장소의 `LICENSE`와 `NOTICE`를 확인하세요. 해당
  라이선스는 원칙적으로 비상업적 연구·평가 용도에 대한 권리를 부여하며,
  상업적 이용에는 원 라이선스 제공자의 별도 허가가 필요할 수 있습니다.

즉, 코드 파일에 적용되는 MIT License가 모델 가중치의 Qwen Research
License를 변경하거나 대체하지 않습니다.

Qwen is licensed under the Qwen RESEARCH LICENSE AGREEMENT,
Copyright (c) Alibaba Cloud. All Rights Reserved.

## Data

학습 JSONL 원문은 모델 저장소에 포함하지 않습니다. 모델 출력에 실제
개인정보가 포함될 가능성을 고려하여 배포 환경에서 접근 통제와 로그
보존 정책을 별도로 적용하세요.
