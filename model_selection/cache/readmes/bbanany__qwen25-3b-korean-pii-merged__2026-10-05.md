---
base_model: Qwen/Qwen2.5-3B-Instruct
language:
- ko
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen2.5
- korean
- pii
- privacy
- merged
- vllm
---

# Qwen2.5-3B Korean PII — merged checkpoint

독립 실행형 Hugging Face 체크포인트입니다. `bbanany/qwen25-3b-korean-pii-qlora2`의 LoRA 어댑터를
`Qwen/Qwen2.5-3B-Instruct` FP16 베이스에 적용한 후 `merge_and_unload()`로 병합했습니다.
따라서 PEFT 어댑터, bitsandbytes, NF4 또는 NVIDIA GPU 없이 일반 Transformers 및 vLLM에서 바로 로드할 수 있습니다.

## vLLM

```bash
vllm serve bbanany/qwen25-3b-korean-pii-merged --dtype half --max-model-len 1024
```

OpenAI 호환 엔드포인트는 `http://localhost:8000/v1`입니다.

## CPU / Apple Silicon

Mac CPU용 경량 실행은 GGUF 배포본을 사용하세요:
[`bbanany/qwen25-3b-korean-pii-gguf`](https://huggingface.co/bbanany/qwen25-3b-korean-pii-gguf)

## Input

원본 모델 카드의 Qwen chat template을 적용하고, 아래 JSON 문자열을 user 메시지로 넣습니다.

```json
{"answer":"김민수의 고객 원장에 연락처 010-1234-5678이 기록되어 있습니다.","candidate":{"text":"010-1234-5678","tag":"PHONE_NUMBER","start":16,"end":29}}
```

출력은 `PII` 또는 `NOT_PII`입니다. 실제 개인정보 처리의 최종 판정에는 독립 평가와 사람 검토가 필요합니다.

## License

Apache-2.0. 베이스 모델의 이용 조건도 함께 적용됩니다.
