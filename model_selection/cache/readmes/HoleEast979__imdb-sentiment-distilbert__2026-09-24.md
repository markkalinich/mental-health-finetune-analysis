---
library_name: transformers
license: apache-2.0
language: en
base_model: distilbert-base-uncased
tags:
- sentiment-analysis
- text-classification
- imdb
- generated_from_trainer
datasets:
- imdb
model-index:
- name: HoleEast979/imdb-sentiment-distilbert
  results:
  - task:
      type: text-classification
    dataset:
      name: imdb
      type: imdb
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.85
---

# 模型卡：基于 DistilBERT 的 IMDB 情感分析模型

这是一个基于 `distilbert-base-uncased` 模型，在经典的 **IMDB 电影评论数据集** 上进行微调的情感分析模型。它能够高效地判断一段英文文本所表达的情感是正面的还是负面的。

## 📝 模型简介 (Model Description)

本模型是一个文本分类器，它接收一段英文文本作为输入，并输出其情感倾向（`POSITIVE` 或 `NEGATIVE`）。模型通过在包含 50,000 条电影评论的 IMDB 数据集上进行微调，学习到了识别影评领域情感表达的特定模式。由于其基础模型是 DistilBERT，它在保持较高准确率（85%）的同时，具有更快的推理速度和更小的模型体积。

## 🚀 用途与局限性 (Intended Uses & Limitations)

### 主要用途

本模型主要用于对**英文电影评论**进行情感倾向的二元分类。它可以被集成到以下应用场景中：

* 舆情监控系统，用于分析用户对某部电影的整体评价。
* 评论筛选工具，自动将评论区分为好评和差评。
* 作为更复杂推荐系统的特征输入。

### 局限性与偏见

* **领域限制**: 模型在电影评论领域的表现最佳，在其他领域（如产品评论、新闻文章、社交媒体帖子）的文本上性能可能会下降。
* **数据偏见**: 模型可能反映出训练数据（IMDB 评论）中存在的偏见。例如，某些特定类型电影的评论风格可能会影响模型的判断。
* **语言限制**: 模型目前仅支持英文文本。
* **无法理解复杂情感**: 模型无法处理讽刺、双关语或复杂的多重情感混合的文本。

## 💡 如何使用 (How to Use)

您可以非常方便地使用 `transformers` 库中的 `pipeline` 来调用这个模型。

```python
# 安装transformers库
# pip install transformers

from transformers import pipeline

# 使用您的模型仓库ID加载pipeline
# 请将 "YOUR_USERNAME/imdb-sentiment-distilbert" 替换为您的模型地址
sentiment_pipeline = pipeline(
    "sentiment-analysis", 
    model="YOUR_USERNAME/imdb-sentiment-distilbert"
)

# 测试正面评论
positive_comment = "This movie was absolutely fantastic, a masterpiece of modern cinema!"
result_pos = sentiment_pipeline(positive_comment)
print(result_pos)
# 预期输出: [{'label': 'POSITIVE', 'score': ...}]

# 测试负面评论
negative_comment = "I would not recommend this film, it was quite boring and a waste of time."
result_neg = sentiment_pipeline(negative_comment)
print(result_neg)
# 预期输出: [{'label': 'NEGATIVE', 'score': ...}]
````

## 📚 训练细节 (Training Details)

### 训练数据 (Training Data)

本模型使用了 `imdb` 数据集进行训练和评估。该数据集包含 50,000 条电影评论，其中 25,000 条用于训练，25,000 条用于测试。每条评论都被标记为 `POSITIVE` (正面) 或 `NEGATIVE` (负面)。

### 训练过程 (Training Procedure)

模型微调是基于 Hugging Face `Trainer` API 在 Kaggle 平台的 T4 GPU 上完成的。整个训练过程的指标通过 `WandB` 进行了实时跟踪和记录。

#### 超参数 (Hyperparameters)

| 超参数 | 值 |
| :--- | :--- |
| `learning_rate` | `2e-05` |
| `train_batch_size` | `16` |
| `eval_batch_size` | `16` |
| `seed` | `42` |
| `optimizer` | `AdamW` |
| `lr_scheduler_type` | `linear` |
| `num_epochs` | `2` |

## 📊 评估 (Evaluation)

模型在 IMDB 数据集的评估集上取得了以下性能：

| 指标 (Metric) | 数值 (Value) |
| :--- | :--- |
| **评估损失 (Loss)** | `0.3455` |
| **准确率 (Accuracy)** | `0.85` |