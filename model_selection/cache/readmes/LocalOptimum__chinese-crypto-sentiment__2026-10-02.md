---
language:
- zh
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- chinese
- finance
- crypto
- news
metrics:
- accuracy
- f1
model-index:
- name: Chinese Crypto Sentiment v11
  results:
  - task:
      type: text-classification
      name: Chinese crypto news sentiment classification
    dataset:
      name: Frozen Luna consensus reference (Chinese sources)
      type: private
    metrics:
    - type: accuracy
      value: 0.8385
      name: Accuracy
    - type: f1
      value: 0.7605
      name: Macro F1
---

# Chinese Crypto Sentiment v11

这是面向中文加密货币新闻的三分类情感模型，标签为 `positive`、`neutral` 和 `negative`。v11 使用事件级去重、固定标签映射、统一文本预处理和 256-token 输入，并通过独立的 Luna 多票协议参考进行锁模后测试。

## Version

- Release: `v11.0.0`
- Variant: `luna-13000-unweighted-s42`
- Base model: `LocalOptimum/chinese-crypto-sentiment`
- Base revision: `42a7f02d35bf5813731ec6e163ea979a3617bb36`
- Weight SHA256: `8278088c99535d8c44e1276fc195d503e29e3a28ec267c9903fceb3046d234e4`
- Release date: 2026-08-29

固定 `revision="v11.0.0"` 可避免 `main` 后续更新造成结果漂移。

## Label Contract

| ID | Label | 定义 |
| ---: | --- | --- |
| 0 | `positive` | 对加密市场或相关项目基本面有明确正向影响 |
| 1 | `neutral` | 事实方向不足、正负混合，或属于计划、预测、常规运营和单账户行为 |
| 2 | `negative` | 对加密市场或相关项目基本面有明确负向影响 |

模型配置已固化该映射。不得按其他标签顺序解释分类头输出。

## Training Snapshot

| Item | Value |
| --- | ---: |
| Database annotated sources | 10,000 |
| Database valid texts | 9,952 |
| Supplemental consensus sources | 3,000 |
| Supplemental deduplicated texts | 2,999 |
| Combined source examples | 12,951 |
| Usable rows after conflict isolation | 12,888 |
| Event groups | 12,641 |
| Conflicting event groups excluded | 30 |
| Training rows | 10,310 |
| Validation rows | 2,578 |

补充数据由 `gpt-5.6-luna` 两次盲判，并仅对分歧事件追加第三票。3,087/3,200 个候选来源达到共识门槛，从中按难例、标签、媒体和年份选择 3,000 个来源。训练集与开发参考、最终测试集的来源交集和 0.90 相似度事件交集均为 0。数据在训练完成后导入数据库，当前数据库规模为 13,000 条。

## Evaluation

### Frozen Chinese Protocol Reference

主发布指标只包含 BlockBeats、Foresight、Odaily 和 PANews。904 条事件来自锁模后建立的最终集合，未参与训练、早停、消融选择或随机种子选择。标签由 Luna 自适应两票/三票协议产生，表示固定操作协议，不主张是客观情感真值。

| Model | Accuracy | Macro F1 | Positive F1 | Neutral F1 | Negative F1 | ECE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| v10 unweighted | 0.8175 | 0.7390 | 0.6067 | 0.8753 | **0.7350** | 0.1399 |
| **v11.0.0** | **0.8385** | **0.7605** | **0.6844** | **0.8907** | 0.7064 | **0.0316** |

### All-Source Sensitivity Analysis

加入 70 条 CoinDesk 英文事件后，最终协议参考共有 974 条接受事件，覆盖率为 97.4%。v11 的 accuracy / macro F1 为 `0.8316 / 0.7451`，v10 为 `0.8039 / 0.7159`。配对比较中 v11 修正 67 个 v10 错误，反向退化 40 个，McNemar 精确检验 `p=0.0116`；accuracy 增量的 5,000 次 bootstrap 95% CI 为 `[0.0072, 0.0483]`，macro F1 增量 CI 为 `[-0.0006, 0.0586]`。

CoinDesk 英文切片的 macro F1 为 `0.4448`。该结果作为域外泛化限制公开保留，不计入中文模型的主发布门禁。

### Internal Grouped Validation

| Metric | Value |
| --- | ---: |
| Accuracy | 0.8592 |
| Macro F1 | 0.8055 |
| Positive F1 | 0.7273 |
| Neutral F1 | 0.9033 |
| Negative F1 | 0.7858 |

内部验证只用于训练早停；模型选择和正式结论以冻结协议参考为准。

## Usage

```python
from transformers import pipeline


classifier = pipeline(
    "text-classification",
    model="LocalOptimum/chinese-crypto-sentiment",
    revision="v11.0.0",
)

result = classifier(
    "比特币现货 ETF 获批并开始交易。",
    truncation=True,
    max_length=256,
)[0]
print(result)  # {'label': 'positive', 'score': ...}
```

训练和生产使用预处理版本 `2.0`：NFKC 规范化、HTML unescape、删除 HTML 标签、URL 和英文 `@handle`、合并空白，并移除常见媒体与日期前缀。直接使用原始文本仍可推理，但复现实验指标时应采用相同预处理。

## Training Configuration

| Parameter | Value |
| --- | --- |
| Architecture | BERT sequence classification |
| Epochs | 3 |
| Learning rate | `1e-5` |
| Train batch size | 16 |
| Precision | BF16 |
| Class weights | Disabled |
| Hard-case repetition | Disabled |
| Max length | 256 |
| Seed | 42 |
| Split unit | Near-duplicate event group |
| Best-model metric | Macro F1 |

## Intended Use

- 中文加密货币新闻的事件级情感分类
- 新闻聚合、舆情统计和候选信号生成
- 人工复核队列的辅助标注

模型输出不构成投资建议，不应脱离事件核验、来源检查和风险控制直接触发交易。

## Known Limitations

- 模型基础和正式评测范围为中文；CoinDesk 等英文输入属于域外数据，不承诺效果。
- 中文最终测试中 v11 的 negative F1 为 0.7064，低于 v10 的 0.7350，尽管总体 macro F1 更高。
- 三票协议均使用 Luna，同一模型家族的系统性偏好不会因重复投票消失。
- 最终测试集为单来源事件，尚未测量跨来源同事件预测一致率。
- 历史媒体和年份分布不完全独立，不能把年份切片差异直接解释为时间漂移。

`eval_report.json` 保存内部事件组验证结果，`split_manifest.json` 保存训练配置与切分清单，`release_metrics.json` 保存正式发布指标、范围和产物哈希。

## License

Apache-2.0。该模型是 `yiyanghkust/finbert-tone-chinese` 系列模型的继续微调版本。
