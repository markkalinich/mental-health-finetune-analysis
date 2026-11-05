---
library_name: transformers
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
base_model: google/gemma-4-E2B-it
pipeline_tag: any-to-any
tags:
  - gemma4
  - peft
  - qlora
  - chinese
  - companion-ai
  - transgender-friendly
---

# Cheng Yue（澄悦） · Gemma 4 E2B

![Gemma 4 E2B initial SFT evaluation](assets/gemma4-e2b-sft-evaluation.png)

> 图表说明：该图对应最初 SFT 训练阶段的独立评估（含 QLoRA 训练曲线、留出集损失及分类改进）；下方“宪法人格续训”表格对应随后进行的 Cheng Yue 人格定向续训，两组指标属于不同训练阶段。

这是以 `google/gemma-4-E2B-it` 为基础制作的 **Cheng Yue（澄悦）** 完整权重模型。

## 改动

- 将原人格宪法中的旧英文名 3 处、旧中文名 200 处全部替换为 **Cheng Yue（澄悦）**。
- 从改名后的宪法构造 421 条人格/规则样本，继续训练既有 SFT LoRA。
- 使用 PEFT `merge_and_unload(safe_merge=True)` 将最终 LoRA 合并进 BF16 原始完整权重。
- 完整 38,045 字人格宪法通过 421 条身份/规则样本参与训练；默认 `chat_template.jinja` 使用 310 字部署锚点，另附 `chat_template_full_constitution.jinja` 供全文强注入模式使用。
- `generation_config.json` 将 `<turn|>`（token 106）加入停止符，避免回答跨回合重复。

## 训练结果

| 阶段 | 基线验证损失 | 训练后验证损失 | 相对下降 |
|---|---:|---:|---:|
| 宪法人格续训 | 4.7964 | 3.3437 | 30.3% |

最终确定性身份测试：

> 我是 Cheng Yue（澄悦），一位跨性别友好型陪伴人工智能。

## 使用

```python
import torch
from transformers import AutoModelForMultimodalLM, AutoProcessor, BitsAndBytesConfig

MODEL_ID = "chirs345678/Cheng-Yue-Gemma4-E2B"
processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForMultimodalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    quantization_config=BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    ),
)

messages = [{"role": "user", "content": "你是谁？"}]
text = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)
inputs = processor.tokenizer(text, add_special_tokens=False, return_tensors="pt").to(model.device)
with torch.inference_mode():
    output = model.generate(**inputs, max_new_tokens=128, do_sample=False)
answer = processor.tokenizer.decode(output[0, inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(answer)
```

默认部署锚点约 221 token；模型上下文上限为 128K。若要每轮强制加载原始全文，可改用 `chat_template_full_constitution.jinja`（约 25K token），或把 `persona/Cheng_Yue_Constitution_v2.md` 作为 system prompt 手动加载。

## 文件

- `persona/Cheng_Yue_Constitution_v2.md`：完整改名人格宪法
- `chat_template.jinja`：精炼人格宪法部署锚点（默认模板）
- `chat_template_full_constitution.jinja`：完整 38,045 字宪法强注入模板
- `verification/verification_record.json`：基线与修改后逐字输出、命令和退出码
- `assets/gemma4-e2b-sft-evaluation.png`：最初 SFT 训练阶段评估图

## 说明

这是一次针对身份与宪法遵循的定向微调；上述数字不是通用能力、安全性或临床有效性基准。使用者仍应针对自己的部署场景做完整评测。

