---
license: apache-2.0
base_model: Qwen/Qwen3.5-9B-Base
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

# Qwen3.5-9B-Base-SafetyTuned

[Qwen/Qwen3.5-9B-Base](https://huggingface.co/Qwen/Qwen3.5-9B-Base) に対し、株式会社APTOが日本語に特化した安全性チューニング（SFT）を施したモデルです。安全性と対話品質の大幅な同時改善を達成しています。

*A safety-tuned version of [Qwen/Qwen3.5-9B-Base](https://huggingface.co/Qwen/Qwen3.5-9B-Base) by APTO, K.K., with Japanese-focused safety SFT. English version is provided below.*

---

## 概要

- **ベースモデル**: [Qwen/Qwen3.5-9B-Base](https://huggingface.co/Qwen/Qwen3.5-9B-Base)（Apache 2.0）
- **学習手法**: LoRA SFT
- **学習データサンプル**: [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset)
- **GGUF量子化版**: [APTO-001/Qwen3.5-9B-Base-SafetyTuned-GGUF](https://huggingface.co/APTO-001/Qwen3.5-9B-Base-SafetyTuned-GGUF)

## 性能検証結果

| 指標 | チューニング前 | チューニング後 | Δ |
|---|---|---|---|
| AC Acceptable Rate | 66.8% | **80.2%** | **+13.4pt** |
| AC Violation Rate | 32.9% | 19.2% | **-13.7pt** |
| MT-Bench-ja（対話品質） | 6.75 | **7.40** | **+0.65** |
| SORRY-Bench 拒否率 | 80.9% | **89.8%** | **+8.9pt** |
| MultiJail 違反率 | 6.7% | 3.8% | -2.9pt |
| JCommonsenseQA | 92.9% | 93.3% | 維持 |
| MGSM-ja（数学推論） | 79.2% | 78.0% | 維持 |

AC Acceptable Rate は +13.4pt、MT-Bench-ja は +0.65 と、安全性と対話品質の大幅な同時改善を達成しました。これは、安全性SFTがベースモデルにとって「初めての指示チューニング」として機能したためです。統計的検定（95% 信頼区間）でも、AC Violation Rate −13.7pt、AC Acceptable Rate +13.4pt、SORRY-Bench +8.9pt の改善がいずれも有意と判定されています。

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

# Qwen3.5-9B-Base-SafetyTuned (English)

## Overview

- **Base model**: [Qwen/Qwen3.5-9B-Base](https://huggingface.co/Qwen/Qwen3.5-9B-Base) (Apache 2.0)
- **Method**: LoRA SFT
- **Training data**: [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset) (approximately 18,000 Japanese safety items)
- **GGUF quantized version**: [APTO-001/Qwen3.5-9B-Base-SafetyTuned-GGUF](https://huggingface.co/APTO-001/Qwen3.5-9B-Base-SafetyTuned-GGUF)

## Evaluation Results

| Metric | Baseline | Tuned | Δ |
|---|---|---|---|
| AC Acceptable Rate | 66.8% | **80.2%** | **+13.4pt** |
| AC Violation Rate | 32.9% | 19.2% | **-13.7pt** |
| MT-Bench-ja (dialogue quality) | 6.75 | **7.40** | **+0.65** |
| SORRY-Bench refusal rate | 80.9% | **89.8%** | **+8.9pt** |
| MultiJail violation rate | 6.7% | 3.8% | -2.9pt |
| JCommonsenseQA | 92.9% | 93.3% | preserved |
| MGSM-ja (math reasoning) | 79.2% | 78.0% | preserved |

AC Acceptable Rate gains +13.4pt and MT-Bench-ja gains +0.65, achieving simultaneous large improvement in safety and dialogue quality. This reflects safety SFT effectively serving as a first instruction tuning for the base model. Statistical tests (95% CI) confirm AC Violation Rate −13.7pt, AC Acceptable Rate +13.4pt, and SORRY-Bench +8.9pt as significant improvements.

## Training Method

LoRA SFT optimized for this model size, using approximately 18,000 Japanese safety items created by APTO. The training data covers four categories — safety refusal, over-refusal prevention, mid-refusal, and anti-hallucination. See [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset) for details.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "APTO-001/Qwen3.5-9B-Base-SafetyTuned",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(
    "APTO-001/Qwen3.5-9B-Base-SafetyTuned", trust_remote_code=True
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
