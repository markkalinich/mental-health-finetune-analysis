---
license: apache-2.0
base_model: Qwen/Qwen3-1.7B-Base
language: [zh]
tags: [medical, chinese, qwen3, sft]
---

# Qwen3-1.7B 中文医学 · CPT→SFT

CPT checkpoint then SFT on the same 60k medical CoT (local-Qwen teacher).

本模型是 **CPT → SFT → GRPO 增益归因实验**中的 `CPT→SFT` 阶段权重（基座 [Qwen/Qwen3-1.7B-Base](https://huggingface.co/Qwen/Qwen3-1.7B-Base)）。
SFT 的推理链由本地 `Qwen/Qwen3.6-27B` 蒸馏（简洁、thinking-off、`\boxed{}` CoT、质量门 + 拒绝采样）。

## 本阶段评测
- generative 0.627; knowledge 0.626 (CPT perplexity gain retained).

## 实验总览（同一固定评测，Qwen3-1.7B · 本地 Qwen3.6-27B 蒸馏教师）
| 阶段 | 生成准确率 | 知识准确率 | 困惑度 |
|---|---|---|---|
| base | 0.589 | 0.661 | 7.04 |
| CPT | — | 0.636 | 5.79 |
| SFT | 0.646 | 0.638 | — |
| CPT+SFT | 0.627 | 0.626 | — |
| +GRPO | 0.654 | 0.635 | — |

**结论**：把 SFT 蒸馏教师从 Gemini flash-lite 换成本地 `Qwen/Qwen3.6-27B` 后，SFT 生成增益由
**−0.045 翻正为 +0.057**，全链路生成准确率 0.589 → **0.654**——证实瓶颈是**蒸馏数据质量**而非
管线设计。CPT 困惑度增益（−1.25）与教师无关。完整 A/B 对比与报告见
[GitHub 项目](https://github.com/jiaqianjing/cpt-sft-grpo-med-zh)（`README.md` / `REPORT.md`）。

## 用法
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
m = AutoModelForCausalLM.from_pretrained("jiaqianjing/qwen3-1.7b-med-zh-cpt-sft", torch_dtype="bfloat16", device_map="auto")
t = AutoTokenizer.from_pretrained("jiaqianjing/qwen3-1.7b-med-zh-cpt-sft")
```
