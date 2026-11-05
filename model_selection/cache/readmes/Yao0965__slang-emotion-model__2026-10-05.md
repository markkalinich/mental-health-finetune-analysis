---
language: zh
tags:
- sentiment-analysis
- emotion-classification
- slang
- traditional-chinese
license: apache-2.0
widget:
- text: "頂"
- text: "笑死"
- text: "QQ"
- text: "傻眼"
---

# 台灣網路俚語情緒分析模型

繁體中文網路俚語情緒分析模型，支援 8 種情緒分類。

## 情緒類別

- LABEL_0: 平淡語氣
- LABEL_1: 關切語調
- LABEL_2: 開心語調
- LABEL_3: 憤怒語調
- LABEL_4: 悲傷語調
- LABEL_5: 疑問語調
- LABEL_6: 驚奇語調
- LABEL_7: 厭惡語調

## 使用方式
```python
from transformers import pipeline

# 注意用戶名是 Yao0965
classifier = pipeline('text-classification', model='Yao0965/slang-emotion-model')
result = classifier('笑死')[0]
print(result)
```

## 範例

| 輸入 | 預測情緒 |
|------|---------|
| 頂 | 開心語調 |
| 雷 | 厭惡語調 |
| 笑死 | 開心語調 |
| QQ | 悲傷語調 |
