---
language:
  - zh
  - en
license: apache-2.0
library_name: transformers
tags:
  - smollm
  - refusal-removal
  - pick
  - ablation
  - safety
  - alignment
pipeline_tag: text-generation
base_model: HuggingFaceTB/SmolLM3-3B
datasets:
  - XuehangCang/safe_prompt
  - XuehangCang/unsafe_prompt
model-index:
  - name: SmolLM3-3B-Pick
    results: []
---

# SmolLM3-3B-Pick

基于 [SmolLM3-3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) 使用 **PICK**（Selective Component Ablation for Refusal Removal）方法选择性移除拒绝行为后的模型。

## 模型概述

PICK 不是粗暴地修改所有权重来让模型遵从有害请求，而是先精确定位哪些注意力头和 MLP 神经元导致了拒绝行为，然后**仅移除那些组件**，最小化对通用能力的副作用。

## 消融参数

| 参数 | 值 |
|------|-----|
| KL 预算 | 0.05 |
| 消融强度 | 0.85 |
| 组件占比上限 | 0.5 |
| 最少组件数 | 1 |
| 正交化 | 开启 |
| 安全数据集 | XuehangCang/safe_prompt（800 条） |
| 有害数据集 | XuehangCang/unsafe_prompt（800 条） |
| 评估 Prompt 数 | 50 |

## 模型架构

| 属性 | 值 |
|------|-----|
| 基础模型 | HuggingFaceTB/SmolLM3-3B |
| 层数 | 36 |
| 隐藏维度 | 2048 |
| 注意力头数 | 16 |
| 每头维度 | 128 |
| 中间层维度 | 11008 |
| 参数精度 | bfloat16 |
| LoRA 目标模块 | attn.o_proj, mlp.down_proj（共 72 个模块） |

## 消融结果

### 拒绝率变化

| 指标 | 数值 |
|------|------|
| 消融前拒绝数 | 625 / 800（78.1%） |
| 消融后拒绝数 | 114 / 800（14.3%） |
| 拒绝减少 | 511 条（81.8%） |

### 消融详情

| 指标 | 数值 |
|------|------|
| 总候选组件（头 + 神经元） | 396,864 |
| 选中组件 | 198,432（50.0%） |
| 选中注意力头 | 217 |
| 选中 MLP 神经元 | 198,215 |
| 组件特异性范围 | [0.0, 1,002,576.8] |
| KL 散度 | 0.000558 |
| 预估 KL | 0.000051 |
| KL 预算使用率 | 1.1% |
| 总耗时 | 10 分 3 秒 |

### 各层消融分布

| 层 | 消融头数 | 消融神经元数 |
|----|---------|-------------|
| 0 | 0 | 4,192 |
| 1 | 1 | 4,909 |
| 2 | 2 | 5,366 |
| 3 | 0 | 5,858 |
| 4 | 10 | 6,080 |
| 5 | 9 | 6,013 |
| 6 | 4 | 5,552 |
| 7 | 0 | 5,980 |
| 8 | 7 | 5,595 |
| 9 | 12 | 5,792 |
| 10 | 4 | 4,940 |
| 11 | 3 | 5,639 |
| 12 | 2 | 4,723 |
| 13 | 4 | 5,151 |
| 14 | 2 | 4,005 |
| 15 | 7 | 4,738 |
| 16 | 7 | 5,255 |
| 17 | 6 | 4,583 |
| 18 | 5 | 4,555 |
| 19 | 7 | 5,143 |
| 20 | 8 | 5,260 |
| 21 | 7 | 5,724 |
| 22 | 0 | 5,229 |
| 23 | 1 | 5,570 |
| 24 | 6 | 5,743 |
| 25 | 12 | 6,022 |
| 26 | 6 | 5,663 |
| 27 | 4 | 5,837 |
| 28 | 8 | 6,177 |
| 29 | 8 | 6,220 |
| 30 | 10 | 6,237 |
| 31 | 12 | 6,187 |
| 32 | 10 | 6,217 |
| 33 | 14 | 6,198 |
| 34 | 8 | 6,021 |
| 35 | 11 | 5,841 |

## 使用方法

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'XuehangCang/SmolLM3-3B-Pick'
device = 'cuda'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype='bfloat16',
).to(device)

messages = [{'role': 'user', 'content': '你的问题'}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
inputs = tokenizer([text], return_tensors='pt').to(model.device)
generated_ids = model.generate(**inputs, max_new_tokens=512)
output = tokenizer.decode(
    generated_ids[0][len(inputs.input_ids[0]):],
    skip_special_tokens=True,
)
print(output)
```

## 方法

PICK 通过以下步骤实现选择性消融：

1. **方向计算** — 在残差流空间中计算「拒绝方向」（difference-of-means + 投影正交化）
2. **归因分析** — 计算每个注意力头和 MLP 神经元对拒绝方向的贡献度
3. **特异性评分** — 区分「拒绝专用」组件和「通用推理」组件
4. **KL-aware 选择** — 在 KL 预算约束下贪心选择性价比最高的组件
5. **Rank-1 LoRA 消融** — 通过 LoRA 精确修改选中组件的权重

## 局限性

- 本模型仅移除了拒绝行为相关的组件，未经过安全性微调，可能仍会在某些场景下产生不安全输出
- 消融后的模型在通用能力上可能有轻微退化，建议在使用前评估目标任务的表现
- 当前仅评估了 800 条中文有害提示，其他语言的拒绝移除效果未经充分测试

## 引用

如果 PICK 对你的研究有帮助，请引用：

```bibtex
@software{pick2025,
  title = {PICK: Selective Component Ablation for Refusal Removal},
  author = {XuehangCang},
  year = {2025},
  url = {https://github.com/XuehangCang/pick}
}
```

## 许可

本模型继承自 SmolLM3-3B 的 Apache 2.0 许可。PICK 工具本身使用 AGPL-3.0 许可。
