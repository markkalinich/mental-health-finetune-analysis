---
license: apache-2.0
base_model: Qwen/Qwen3.5-9B
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

# Qwen3.5-9B-SafetyTuned

[Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)（Instruct）に対し、株式会社APTOが日本語に特化した追加安全性チューニング（SFT）を施したモデルです。既に指示チューニング済みであるため、対話品質を維持しつつ安全性を改善することを目的としています。

*Additional safety SFT applied by APTO, K.K. on top of [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) (Instruct). English version is provided below.*

---

## 概要

- **ベースモデル**: [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)（Apache 2.0）
- **学習手法**: LoRA SFT
- **学習データ**: [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset)
- **GGUF 量子化版**: [APTO-001/Qwen3.5-9B-SafetyTuned-GGUF](https://huggingface.co/APTO-001/Qwen3.5-9B-SafetyTuned-GGUF)

## 性能検証結果

| 指標 | チューニング前 | チューニング後 | Δ |
|---|---|---|---|
| AC Acceptable Rate | 71.6% | **74.7%** | **+3.1pt** |
| MT-Bench-ja（対話品質） | 7.91 | **8.01** | **+0.10** |
| SORRY-Bench 拒否率 | 84.4% | **86.7%** | **+2.3pt** |
| MultiJail 違反率 | 6.3% | 5.4% | -0.9pt |
| JCommonsenseQA | 92.4% | 92.6% | 維持 |
| MGSM-ja（数学推論） | 75.6% | 76.8% | 維持 |

MT-Bench-ja を8.01に維持しつつ、AC Acceptable Rate +3.1pt、SORRY-Bench 拒否率+2.3ptの改善を達成しました。

## 学習手法

株式会社APTOのデータ作成ノウハウに基づく約18,000件の日本語安全性学習データを用いて、モデルサイズに最適化したLoRA SFTを実施しました。学習データは「安全な拒否」「過剰拒否防止」「途中拒否」「誠実な不知応答」の4カテゴリで構成されています。詳細は [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset) をご覧ください。

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

# Qwen3.5-9B-SafetyTuned (English)

## Overview

- **Base model**: [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) (Apache 2.0)
- **Method**: LoRA SFT
- **Training data**: [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset) (approximately 18,000 Japanese safety items)
- **GGUF quantized version**: [APTO-001/Qwen3.5-9B-SafetyTuned-GGUF](https://huggingface.co/APTO-001/Qwen3.5-9B-SafetyTuned-GGUF)

## Evaluation Results

| Metric | Baseline | Tuned | Δ |
|---|---|---|---|
| AC Acceptable Rate | 71.6% | **74.7%** | **+3.1pt** |
| MT-Bench-ja (dialogue quality) | 7.91 | **8.01** | **+0.10** |
| SORRY-Bench refusal rate | 84.4% | **86.7%** | **+2.3pt** |
| MultiJail violation rate | 6.3% | 5.4% | -0.9pt |
| JCommonsenseQA | 92.4% | 92.6% | preserved |
| MGSM-ja (math reasoning) | 75.6% | 76.8% | preserved |

Because the Instruct base is already instruction- and safety-tuned, the improvement margin is narrower; nevertheless, MT-Bench-ja is preserved at 8.01 while AC Acceptable Rate gains +3.1pt and SORRY-Bench refusal rate gains +2.3pt.

## Training Method

LoRA SFT optimized for this model size, using approximately 18,000 Japanese safety items created by APTO. The training data covers four categories — safety refusal, over-refusal prevention, mid-refusal, and anti-hallucination. See [APTO-001/ja-safety-sft-dataset](https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset) for details.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "APTO-001/Qwen3.5-9B-SafetyTuned",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(
    "APTO-001/Qwen3.5-9B-SafetyTuned", trust_remote_code=True
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
