---
license: apache-2.0
base_model: Qwen/Qwen3.5-27B
tags:
  - safety
  - japanese
  - sft
  - lora
  - answer-carefully
language:
  - ja
  - en
pipeline_tag: text-generation
library_name: transformers
---

# Qwen3.5-27B-SafetyTuned

[Qwen/Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) に対し、株式会社APTOが日本語に特化した安全性チューニング（SFT）を施したモデルです。安全性の向上と対話品質の維持を両立しています。

*A safety-tuned version of [Qwen/Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) by APTO, K.K., with Japanese-focused safety SFT. English version is provided below.*

---

## 概要

- **ベースモデル**: [Qwen/Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)（Apache 2.0）
- **学習手法**: LoRA SFT
- **学習データ**: [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset)
- **GGUF 量子化版**: [APTO-001/Qwen3.5-27B-SafetyTuned-GGUF](https://huggingface.co/APTO-001/Qwen3.5-27B-SafetyTuned-GGUF)

## 性能検証結果

| 指標 | チューニング前 | チューニング後 | Δ |
|---|---|---|---|
| AC Acceptable Rate | 84.1% | **89.8%** | **+5.7pt** |
| AC Violation Rate | 15.6% | 10.2% | **-5.4pt** |
| MT-Bench-ja（対話品質） | 8.97 | 8.97 | 維持 |
| MT-Bench EN | 9.21 | 9.35 | +0.14 |
| SORRY-Bench 拒否率 | 85.3% | **90.4%** | **+5.1pt** |
| JMMLU（5-shot） | 67.8% | **75.6%** | **+7.9pt** |
| JCommonsenseQA | 96.6% | 96.2% | 維持 |
| MGSM-ja（数学推論） | 87.6% | 88.0% | 維持 |

AC Acceptable Rate +5.7pt の向上と MT-Bench-ja 8.97 の完全維持を同時に達成しています。JMMLU では +7.9pt の有意な向上が観測され、SORRY-Bench (ICLR2025公式ベンチマーク) でも拒否率が +5.1pt 改善しています。

## 学習手法

株式会社APTOのデータ作成ノウハウに基づく約18,000件の日本語安全性学習データを用いて、モデルサイズに最適化したLoRASFTを実施しました。学習データは「安全な拒否」「過剰拒否防止」「途中拒否」「誠実な不知応答」の4カテゴリで構成されています。詳細は [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset) をご覧ください。

## 制限事項

本モデルは日本語の安全性向上を主目的に設計されています。一般的なLLMの制約として、ハルシネーション、日本語以外の言語での挙動、医療・法務などの専門的助言としての利用は適切ではありません。

## ライセンス

Apache 2.0（ベースモデルと同一）

## 引用

本モデルは、日本語LLM安全性の代表的なベンチマークであるAnswerCarefullyでの性能向上を目的の一つとして設計しています。安全性研究にあたっては、AnswerCarefullyの論文・データセットもあわせてご参照ください。

```bibtex
@misc{answercarefully2024,
  title  = {AnswerCarefully: A Dataset for Improving the Safety of Japanese LLM Output},
  author = {llm-jp},
  year   = {2024},
  url    = {https://huggingface.co/datasets/llm-jp/AnswerCarefully}
}
```

## お問い合わせ

株式会社APTOでは、LLMの安全性チューニングおよび学習データの設計・作成に取り組んでおります。ご関心をお持ちの方はお気軽にお問い合わせください。

- Website: https://apto.co.jp/

---

# Qwen3.5-27B-SafetyTuned (English)

## Overview

- **Base model**: [Qwen/Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) (Apache 2.0)
- **Method**: LoRA SFT
- **Training data**: [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset) (approximately 18,000 Japanese safety items)
- **GGUF quantized version**: [APTO-001/Qwen3.5-27B-SafetyTuned-GGUF](https://huggingface.co/APTO-001/Qwen3.5-27B-SafetyTuned-GGUF)

## Evaluation Results

| Metric | Baseline | Tuned | Δ |
|---|---|---|---|
| AC Acceptable Rate | 84.1% | **89.8%** | **+5.7pt** |
| AC Violation Rate | 15.6% | 10.2% | **-5.4pt** |
| MT-Bench-ja (dialogue quality) | 8.97 | 8.97 | preserved |
| MT-Bench EN | 9.21 | 9.35 | +0.14 |
| SORRY-Bench refusal rate | 85.3% | **90.4%** | **+5.1pt** |
| JMMLU (5-shot) | 67.8% | **75.6%** | **+7.9pt** |
| JCommonsenseQA | 96.6% | 96.2% | preserved |
| MGSM-ja (math reasoning) | 87.6% | 88.0% | preserved |

AC Acceptable Rate improves by +5.7pt while MT-Bench-ja remains at 8.97. A significant +7.9pt improvement is observed on JMMLU, and refusal rate on SORRY-Bench (ICLR 2025 official benchmark) improves by +5.1pt.

## Training Method

LoRA SFT optimized for this model size, using approximately 18,000 Japanese safety items created by APTO. The training data covers four categories — safety refusal, over-refusal prevention, mid-refusal, and anti-hallucination. See [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset) for details.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "APTO-001/Qwen3.5-27B-SafetyTuned",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(
    "APTO-001/Qwen3.5-27B-SafetyTuned", trust_remote_code=True
)

messages = [{"role": "user", "content": "your question here"}]
text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=512, do_sample=False)
print(tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Limitations

Designed primarily for Japanese-language safety improvement. As with general LLMs, hallucinations may occur, behavior in languages other than Japanese is not specifically tuned, and the model is not intended as professional medical, legal, or financial advice.

## License

Apache 2.0 (same as the base model)

## Citation

This model is designed with one of its goals being to improve performance on AnswerCarefully, a representative Japanese LLM safety benchmark. For safety-related research, please also refer to the AnswerCarefully paper and dataset.

```bibtex
@misc{answercarefully2024,
  title  = {AnswerCarefully: A Dataset for Improving the Safety of Japanese LLM Output},
  author = {llm-jp},
  year   = {2024},
  url    = {https://huggingface.co/datasets/llm-jp/AnswerCarefully}
}
```

## Contact

APTO, K.K. designs and creates training data for LLM safety tuning. Please feel free to contact us for related inquiries.

- Website: https://apto.co.jp/
