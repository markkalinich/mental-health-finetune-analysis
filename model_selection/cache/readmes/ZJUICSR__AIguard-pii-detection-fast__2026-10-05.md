---
license: apache-2.0
language:
- zh
metrics:
- accuracy
- precision
- recall
- f1
pipeline_tag: token-classification
library_name: transformers
---

# AIguard-0.6B-PII-Chinese

<p align="center">
    <a href="https://huggingface.co/docs/transformers">
        <img alt="Built with Transformers" src="https://img.shields.io/badge/Built%20with-Transformers-yellow">
    </a>
    <a href="https://opensource.org/licenses/Apache-2.0">
        <img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
    </a>
    <a href="https://huggingface.co">
        <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow">
    </a>
</p>

基于 [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) 微调的中文个人身份信息（PII）识别模型，支持 **21 类敏感实体**的高精度抽取，专为中文场景下的隐私数据保护、合规审查与数据脱敏设计。

## 📊 模型效果

| 指标 | 数值 |
|------|------|
| **实体级别 F1** | **96.29%** |
| **Micro F1** | **96.29%** |
| **Macro F1** | **96.70%** |
| **序列标注准确率** | **99.91%** |
| **目标实体召回率** | **99.55%** |
| **推理延迟 (GPU)** | ~90ms / 512 tokens |

### 各实体类型详细表现

| 实体类型 | 说明 | Precision | Recall | F1 | 测试样本数 |
|---------|------|-----------|--------|----|--------|
| `name` | 姓名 | 99.33% | 99.66% | **99.50%** | 1,194 |
| `id_card` | 身份证号 | 98.85% | 99.23% | **99.04%** | 1,039 |
| `mobile` | 手机号 | 99.56% | 99.91% | **99.73%** | 1,123 |
| `address` | 地址 | 99.83% | 100.0% | **99.91%** | 1,163 |
| `email` | 邮箱 | 97.65% | 97.65% | **97.65%** | 1,107 |
| `passport` | 护照号 | 99.82% | 99.82% | **99.82%** | 1,109 |
| `hkmtp_pass` | 港澳通行证 | 99.74% | 99.74% | **99.74%** | 1,153 |
| `social_security` | 社会保障号 | 99.29% | 99.90% | **99.59%** | 975 |
| `drivers_license` | 驾驶证号 | 99.44% | 99.72% | **99.58%** | 1,059 |
| `plate_number` | 车牌号 | 99.47% | 99.82% | **99.64%** | 1,118 |
| `bank_card` | 银行卡号 | 99.57% | 99.78% | **99.67%** | 1,377 |
| `credit_card` | 信用卡号 | 99.58% | 99.92% | **99.75%** | 1,193 |
| `bank_password` | 银行密码 | 99.14% | 100.0% | **99.57%** | 1,386 |
| `birth_date` | 出生日期 | 95.86% | 98.01% | **96.92%** | 1,206 |
| `insurance_policy` | 保险单号 | 99.24% | 99.75% | **99.49%** | 1,182 |
| `taobao_order` | 淘宝订单号 | 98.94% | 99.56% | **99.25%** | 1,128 |
| `jd_order` | 京东订单号 | 99.43% | 99.76% | **99.59%** | 1,228 |
| `pdd_order` | 拼多多订单号 | 99.23% | 99.66% | **99.45%** | 1,170 |
| `ems_tracking` | EMS快递单号 | 100.0% | 100.0% | **100.0%** | 1,257 |
| `sf_tracking` | 顺丰快递单号 | 99.75% | 99.75% | **99.75%** | 1,184 |
| `yto_tracking` | 圆通快递单号 | 36.23% | 53.17% | **43.10%** | 1,104 |

* 实体数据示例
```json
"name": "汪豹锐",
"id_card": "340203200210257432",
"birth_date": "2002-10-25",
"address": "安徽省芜湖市弋江区新华路17号楼1399室",
"mobile": "13717627942",
"email": "wang.uz02@sina.com",
"passport": "K20138207",
"hkmtp_pass": "W32765504",
"social_security": "340203200210257432",
"drivers_license": "340203200210257432",
"plate_number": "皖C·44059",
"bank_card": "6225880443899783447",
"credit_card": "5588600092873914",
"bank_password": "102574",
"insurance_policy": "PAB202204089626802",
"taobao_order": "26030304024271434099",
"jd_order": "2952756430649672146",
"pdd_order": "260607-8514645871356",
"ems_tracking": "9895844345593",
"sf_tracking": "SF0642806007386",
"yto_tracking": "YT530178350300"
```

> ⚠️ **注意**：`yto_tracking`（圆通快递单号）因格式特征较弱，召回率较低，建议在实际使用中结合规则后处理进行增强。

## 🏗️ 技术架构

### 基座模型
- **Qwen3-0.6B** — 轻量级中文大语言模型，兼顾推理速度与理解能力

### 训练策略
- **任务类型**：Token Classification（BIOE 标注体系）
- **数据规模**：覆盖 10 大领域、30 个真实生活场景，数万条合成样本
- **场景覆盖**：车辆与交通、金融与银行、快递与电商、政务与法律、职场与人事、电信与网络、医疗与健康、商旅与出行、房产与物业、社交与生活

### 数据构建亮点
- 采用 **LLM 合成 + 人工校验** 的方式构建训练数据
- 严格约束：实体值不可改写、不可掩码、不可缺失
- 口语化表达，模拟真实用户交互场景（焦急、礼貌、愤怒等情绪）

## 🚀 快速开始

### 环境要求

```bash
pip install transformers torch
```

### 加载模型

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

model_name = "ZJUICSR/AIguard-pii-detection-fast"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# 自动获取标签映射
id2label = model.config.id2label
```

### 单条推理

```python
def predict_pii(text, max_length=512):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=max_length,
        return_offsets_mapping=True
    )
    offset_mapping = inputs.pop("offset_mapping")[0].tolist()

    with torch.no_grad():
        outputs = model(**inputs)

    predictions = torch.argmax(outputs.logits, dim=-1)[0].tolist()
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    # BIOE 解码
    entities = []
    current_entity = None

    for idx, (pred_id, (start, end)) in enumerate(zip(predictions, offset_mapping)):
        label = id2label[pred_id]

        if label.startswith("B-"):
            if current_entity:
                entities.append(current_entity)
            current_entity = {
                "start": start,
                "end": end,
                "label": label[2:],
                "text": text[start:end]
            }
        elif label.startswith("I-") or label.startswith("E-"):
            if current_entity and current_entity["label"] == label[2:]:
                current_entity["end"] = end
                current_entity["text"] = text[current_entity["start"]:end]
                if label.startswith("E-"):
                    entities.append(current_entity)
                    current_entity = None
        else:
            if current_entity:
                entities.append(current_entity)
                current_entity = None

    if current_entity:
        entities.append(current_entity)

    return {"text": text, "entities": entities}

# 示例
text = "你好，我叫张三，身份证号是110101199001011234，手机号13800138000。"
result = predict_pii(text)
print(result)
```

### 输出示例

```json
{
  "text": "你好，我叫张三，身份证号是110101199001011234，手机号13800138000。",
  "entities": [
    {"start": 6, "end": 8, "label": "name", "text": "张三"},
    {"start": 14, "end": 32, "label": "id_card", "text": "110101199001011234"},
    {"start": 37, "end": 48, "label": "mobile", "text": "13800138000"}
  ]
}
```
## 💡 应用场景

- **数据脱敏**：自动识别并掩码敏感信息，满足 GDPR、《个人信息保护法》等合规要求
- **客服质检**：实时检测对话中泄露的隐私数据
- **日志审计**：扫描系统日志中的 PII 泄露风险
- **数据治理**：结构化抽取文档中的身份信息，构建隐私数据资产目录

## ⚡ 性能优化建议

1. **批处理推理**：对于大量文本，建议使用 `DataLoader` 进行批处理
2. **长度控制**：输入文本建议控制在 512 tokens 以内，超长文本请先分段
3. **后处理增强**：对于 `yto_tracking` 等弱特征实体，可结合正则表达式进行二次校验

## ⚠️ 使用声明

1. **合规使用**：本模型仅用于合法的数据安全与隐私保护场景，禁止用于非法收集、窃取或滥用个人信息。
2. **模型局限**：
   - 训练数据为合成生成，可能与真实分布存在差异
   - 对 `yto_tracking` 的识别能力较弱，建议生产环境结合规则引擎
   - 不保证对伪造、变造身份信息的识别能力
3. **人工复核**：模型输出结果建议进行人工复核，关键业务场景请勿完全依赖自动判定。

## 📄 许可证

本项目采用 [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) 开源协议。

## 🙏 致谢

- 基座模型：[Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) by Alibaba Qwen Group
- 训练框架：[Hugging Face Transformers](https://github.com/huggingface/transformers)

---

<p align="center">Made with ❤️ for Chinese PII Protection</p>
