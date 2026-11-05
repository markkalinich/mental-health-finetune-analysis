---
language: 
  - zh
tags:
  - roberta
  - text-classification
  - multi-label-classification
  - emotion-detection
  - sentiment-analysis
  - pytorch
metrics:
  - f1
  - precision
  - recall
---

# RoBERTa Multi-Label Emotion & Tone Classifier (28 Emotions + 3 Tones)

[![Try it Live](https://img.shields.io/badge/🚀_Try_it_Live-Novel_Emotion_Search_Engine-blue?style=for-the-badge)](https://semo.liudev.com)
[![Author](https://img.shields.io/badge/Author-liudev-orange?style=for-the-badge)](https://huggingface.co/liudev)

## 🚀 官方应用展示 (Powered by this model)

本模型目前已在生产环境中部署。我们基于此模型开发了一款强大的 **“小说情绪起伏搜索引擎”**。

👉 **[点击这里立即体验在线 Demo：semo.liudev.com](https://semo.liudev.com)**

在这个应用中，我们展示了该模型的高阶用法：
1. **情绪轨迹检索 (Emotion Trajectory Search)**：不再是单纯的关键词搜索，你可以拼装一个情绪链条（例如：`喜极而泣 [Joy] -> [Sadness] -> [Relief]` 或 `先抑后扬 [Annoyance] -> [Surprise] -> [Admiration]`），引擎会在海量小说库中找到完美符合该情绪走向的章节。
2. **序列匹配算法**：底层结合了该模型的 31 维向量输出与 DTW (动态时间规整) 算法，实现长文本情绪子序列的模糊匹配。
3. **上下文感知高亮**：精准定位并渲染命中情绪的段落。
4. **AI 链条生成**：支持使用自然语言描述情绪走向，自动转化为模型的查询向量。

如果你对长文本情感分析、网文数据挖掘感兴趣，强烈建议试用该应用！

---

## 模型简介 (Model Description)
本模型 (`liudev/roberta-multilabel-28-3-classes`) 是一个基于 RoBERTa 架构的多标签文本分类模型。专门用于小说、对话或长文本段落的情感和基调分析。

模型共支持 **31 个类别**，包括：
- **28 种细粒度情感**（如 anger, joy, love, surprise 等）
- **3 种情感基调**（tone_positive, tone_negative, tone_neutral）

### 特殊的输入格式 (Context-Aware)
为了更好地理解小说/长文本中的上下文连贯性，**本模型在训练和推理时使用了双句输入（Pair Input）策略**：
- `text_a`: 历史上下文（如当前段落的前 3 段）
- `text_b`: 当前需要预测的段落文本
这种设计使得模型能够结合前文语境，做出更准确的判断。

## 生产环境推荐阈值 (High-Precision Thresholds)
在多标签分类中，默认的 `0.5` 阈值往往不是最优的。为了在生产环境中确保**“宁愿漏报，也不误报”（高查准率，Precision >= 80% 为目标）**，我们对每个标签进行了严格的阈值调优（正如我们的官方引擎中所使用的那样）。

强烈建议在推理时使用以下独立阈值字典：

```python
PRODUCTION_THRESHOLDS = {
    "anger": 0.71, "annoyance": 0.66, "disapproval": 0.65, "disgust": 0.75,
    "fear": 0.73, "nervousness": 0.74, "embarrassment": 0.82, "disappointment": 0.69,
    "gratitude": 0.75, "joy": 0.59, "amusement": 0.65, "excitement": 0.61,
    "optimism": 0.73, "pride": 0.73, "relief": 0.75, "admiration": 0.71,
    "approval": 0.69, "love": 0.77, "caring": 0.73, "desire": 0.78,
    "neutral": 0.63, "sadness": 0.68, "grief": 0.80, "remorse": 0.81,
    "surprise": 0.59, "realization": 0.61, "curiosity": 0.78, "confusion": 0.77,
    "tone_positive": 0.49, "tone_negative": 0.47, "tone_neutral": 0.62
}
```

## 如何使用 (How to Use)

以下是一个开箱即用的推理示例，包含了上下文组装和自定义阈值过滤：

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "liudev/roberta-multilabel-28-3-classes"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

# 推荐的生产环境阈值 (High Precision)
THETA_FINAL_TENSOR = torch.tensor([
    0.71, 0.66, 0.65, 0.75, 0.73, 0.74, 0.82, 0.69, 0.75, 0.59, 
    0.65, 0.61, 0.73, 0.73, 0.75, 0.71, 0.69, 0.77, 0.73, 0.78, 
    0.63, 0.68, 0.80, 0.81, 0.59, 0.61, 0.78, 0.77, 0.49, 0.47, 0.62
])

# 标签映射
id2label = model.config.id2label

# 构建输入 (Context + Current Paragraph)
context_paragraphs = [
    "夜幕低垂，狂风在破败的庙宇外肆虐，吹得半掩的残门嘎吱作响。",
    "李青死死握紧了手中的长剑，手心满是冷汗，连呼吸都变得极其小心翼翼。"
]
current_paragraph = "突然，黑暗中传来一声凄厉的惨叫，紧接着，一双血红色的眼睛在神像背后缓缓睁开！"

text_a = "\n".join(context_paragraphs) # 前文历史（提供语境）
text_b = current_paragraph             # 当前需要分析情绪的段落

inputs = tokenizer(
    text_a, 
    text_b, 
    padding=True, 
    truncation=True, 
    max_length=256, 
    return_tensors="pt"
)

with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.sigmoid(logits).squeeze(0) # 转换为概率

# 使用自定义阈值进行过滤
predictions = []
for idx, prob in enumerate(probs):
    if prob >= THETA_FINAL_TENSOR[idx]:
        predictions.append({
            "label": id2label[idx],
            "score": round(prob.item(), 4)
        })

print(predictions)
# Expected Output format:[{'label': 'fear', 'score': 0.8855}, {'label': 'nervousness', 'score': 0.7645}, {'label': 'surprise', 'score': 0.8146}, {'label': 'tone_negative', 'score': 0.8112}]

```

## 评估指标 (Evaluation Results)

本模型在验证集上的综合表现如下：
- **Micro F1:** 0.75
- **Macro F1:** 0.72
- **Samples F1:** 0.75

### 详细分类报告 (基于 Best F1 阈值)

模型在各个标签上的查准率（Precision）和召回率（Recall）表现：

| Label | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| anger | 0.75 | 0.77 | 0.76 | 887 |
| annoyance | 0.76 | 0.73 | 0.74 | 1874 |
| disapproval | 0.70 | 0.74 | 0.72 | 2013 |
| disgust | 0.75 | 0.67 | 0.71 | 691 |
| fear | 0.71 | 0.68 | 0.70 | 1165 |
| nervousness | 0.64 | 0.70 | 0.67 | 1134 |
| embarrassment| 0.48 | 0.62 | 0.54 | 417 |
| disappointment| 0.66 | 0.80 | 0.73 | 1805 |
| gratitude | 0.88 | 0.76 | 0.82 | 683 |
| joy | 0.85 | 0.88 | 0.87 | 2329 |
| amusement | 0.72 | 0.68 | 0.70 | 1546 |
| excitement | 0.81 | 0.81 | 0.81 | 2073 |
| optimism | 0.68 | 0.68 | 0.68 | 1464 |
| pride | 0.62 | 0.67 | 0.65 | 1151 |
| relief | 0.69 | 0.64 | 0.67 | 1023 |
| admiration | 0.61 | 0.75 | 0.67 | 1529 |
| approval | 0.67 | 0.74 | 0.70 | 1917 |
| love | 0.65 | 0.68 | 0.67 | 922 |
| caring | 0.67 | 0.71 | 0.69 | 1630 |
| desire | 0.53 | 0.62 | 0.57 | 1132 |
| neutral | 0.74 | 0.75 | 0.75 | 1810 |
| sadness | 0.84 | 0.82 | 0.83 | 1585 |
| grief | 0.64 | 0.77 | 0.70 | 612 |
| remorse | 0.67 | 0.63 | 0.65 | 323 |
| surprise | 0.76 | 0.79 | 0.77 | 2355 |
| realization | 0.65 | 0.79 | 0.71 | 3563 |
| curiosity | 0.69 | 0.69 | 0.69 | 762 |
| confusion | 0.64 | 0.72 | 0.68 | 839 |
| tone_positive | 0.87 | 0.86 | 0.86 | 4306 |
| tone_negative | 0.87 | 0.90 | 0.89 | 4772 |
| tone_neutral | 0.75 | 0.77 | 0.76 | 2093 |
| **Micro Avg** | **0.73** | **0.77** | **0.75** | **50405** |

*(注意：若采用前文提供的生产环境高精度阈值，Precision 将普遍提升至 0.7~0.85 以上，代价是 Recall 会按预期下降。)*

以上内容撰写使用LLM生成，以上代码可直接在kaggle上运行，以上数据均为实际运行结果，已测试通过。