---
language:
- zh
license: apache-2.0
size_categories:
- 1B<n<10B
pipeline_tag: text-generation
tags:
- medical
- tcm
- traditional-chinese-medicine
- qwen3
- sft
- chinese
- thinking
base_model: Qwen/Qwen3-8B
---

# Medical v5 — Qwen3-8B 中医西医兼通临床助手

基于 **Qwen3-8B** 的医疗 SFT 模型, 用 37k 临床数据 + Baichuan-M2-32B 蒸馏 thinking 链 训练. 保留显式推理段, 推理时通过 `enable_thinking` 切换 reasoning 模式.

## 模型规格

| 项 | 值 |
|---|---|
| 底座 | Qwen/Qwen3-8B |
| 参数量 | 8.19 B |
| 精度 | bfloat16 (~16 GB) |
| max_model_len | 8192 |
| 训练 | 4 节点 × 8 卡 A800, 2 epoch full SFT, 2h 09min |
| 训练框架 | ms-swift 4.2.3 + DeepSpeed ZeRO-3 |
| chat_template | Qwen3 风格 (`<think>...</think>` + final answer) |

## 训练数据 (37,353 条)

| 子集 | 规模 | 来源 | thinking |
|---|---|---|---|
| A | 32,057 | v3 chosen prompt × **M2-32B 重新生成** thinking 链 | ✅ |
| C | 5,000 | M2 thinking 数据 (回避修正版) | ✅ |
| D1 | 296 | 国家药典教材方剂 | ❌ schema 标准 |

`<think>` 闭合率 99.97%. p99 长度 3959 < max 5120.

## 评估结果 (210 题套件)

210 题 = 60 open + 100 CMB mcq + 50 C-Eval mcq.

| 模型 | CMB | C-Eval | open v2_seed | open new_30 |
|---|---|---|---|---|
| Qwen3-8B base | — | — | 4.87 | 4.87 |
| v4-584 (无 thinking 训练) | 69% | 82% | 4.60 | 5.00 |
| **v5-580 thinking-on** ⭐ | **70%** | **92%** | **5.00** | **5.00** |
| v5-580 thinking-off | 68% | 86% | 5.00 | 4.87 |

注: open 5 分制, M2-32B 当 judge 有天花板效应 (高分聚集), 真实差距需配合 mcq 客观题判读.

## 推理使用

### 推荐: vLLM ≥ 0.19.1 + reasoning parser

```bash
pip install vllm>=0.19.1

vllm serve shdkahjkda/medical-v5-8b \
  --served-model-name medical-v5 \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.85 \
  --reasoning-parser qwen3 \
  --dtype bfloat16
```

### Python 直接调用

```python
from vllm import LLM, SamplingParams

llm = LLM(model="shdkahjkda/medical-v5-8b", dtype="bfloat16")
tokenizer = llm.get_tokenizer()

messages = [
    {"role": "user", "content": "风寒感冒和风热感冒怎么鉴别"}
]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True,   # 关键: True 让模型先 thinking 再答
)
out = llm.generate([prompt], SamplingParams(temperature=0.3, max_tokens=4096))
print(out[0].outputs[0].text)
```

### OpenAI 兼容 HTTP API

```python
import openai
client = openai.OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")
resp = client.chat.completions.create(
    model="medical-v5",
    messages=[{"role": "user", "content": "二陈汤的组成和功效"}],
    temperature=0.3,
    max_tokens=4096,
    extra_body={"chat_template_kwargs": {"enable_thinking": True}},
)
# vllm 0.19.1: thinking 段在 resp.choices[0].message.reasoning, final 在 .content
```

## 关键 caveat

1. **mcq + thinking 不兼容默认配置**: chat_template 标准 mcq prompt 期望模型直接吐字母, 但 `enable_thinking=True` 时模型会先吐 `<think>...</think>` 段. **mcq 用例必须把 max_tokens 拉到 ≥4096**, 且 parser 必须先剥 `<think>` 段再抓 ABCDE, 否则准确率暴跌 (实测 CMB 70% → 10%).
2. **多轮对话**回传 history 时 **不要带 reasoning 段**, 只回传 final content (Qwen3 官方建议, 否则 token 浪费 + 风格污染).
3. **判官选择**: 不要再用 M2-32B 当 judge 评本模型 — 会有"老师改学生"bias. 推荐 GPT-4 / Claude Opus / 人工抽样.

## License

- **模型权重**: Apache 2.0 (跟随 Qwen3-8B 底座)
- **训练数据**: 包含 Baichuan-M2-32B 蒸馏内容, 受 M2 商用条款约束, **仅限研究和教育用途**, 不可用于商业部署
- **代码**: Apache 2.0

## 配套代码

GitHub: https://github.com/pai-pixel/medical-v5 (private)

包含: chat 推理接口 (FastAPI + vllm) / 训练 launcher / 评估脚本.

## Disclaimer

本模型仅供研究使用. 输出 **不构成医疗建议**, 任何临床决策必须由执业医师审核. 涉及具体用药、剂量、急救处理请始终咨询专业医务人员或拨打急救电话.

## 项目状态

2026-06-21 完工. 后续视情况做 int4 量化部署到 RK3588 类边缘终端.

## Citation

```
@misc{medical-v5-2026,
  author = {pai-pixel},
  title = {medical-v5: Qwen3-8B SFT 中医西医兼通临床助手},
  year = {2026},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/shdkahjkda/medical-v5-8b}}
}
```
