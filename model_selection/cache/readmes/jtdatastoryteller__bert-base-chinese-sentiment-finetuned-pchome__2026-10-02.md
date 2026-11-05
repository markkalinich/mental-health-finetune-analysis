---
language: zh
license: mit
pipeline_tag: text-classification
library_name: transformers
tags:
  - bert
  - app-reviews
  - sentiment-analysis
  - chinese
widget:
  - text: "這個商品真的很棒，我很喜歡！"
  - text: "物流速度太慢了，差評。"
---

# 中文情緒分類模型

本模型基於 `bert-base-chinese`，針對中文評論文本進行三類情緒分類的 Fine-tuning。

## 模型用途

輸入一段中文文本，模型會自動將其分類至以下三個類別之一：

| 類別 | 說明 |
|------|------|
| 正面 | 表達正向、滿意、讚揚的文本 |
| 負面 | 表達負向、不滿、批評的文本 |
| 中性 | 不帶明顯情緒傾向的文本 |

## 使用方式

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="jtdatastoryteller/bert-base-chinese-sentiment-finetuned-pchome"
)

result = classifier("這個 App 使用體驗很差！")
print(result)
# 輸出：[{'label': '負面', 'score': 0.95}]
```

## 訓練資料

- 資料集：Pchome App 評論情緒分類標註資料
- 樣本數：約 1,000 筆

## 訓練設定

- 基礎模型：bert-base-chinese
- 學習率：2e-5
- 批次大小：32
- 最大序列長度：128
- 損失函數：Focal Loss（gamma=2）
- 不平衡處理：Class Weight

## 注意事項

本模型以小規模資料集訓練，建議用於同領域的中文情緒分析場景。
若應用於其他領域，建議重新進行 Fine-tuning。
