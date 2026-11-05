---
library_name: transformers
pipeline_tag: text-classification
language:
- zh
tags:
- sentiment-analysis
- mario
- forum
- off-topic-detection
license: apache-2.0
model-index:
- name: pannnnnnn/4_labels
  results:
  - task:
      type: text-classification
      name: 4-way Sentiment + OT
    metrics:
    - type: accuracy
      value: 0.854
    - type: f1
      name: macro_f1
      value: 0.852
    - type: f1
      name: negative_f1
      value: 0.939
    - type: f1
      name: neutral_f1
      value: 0.774
    - type: f1
      name: positive_f1
      value: 0.804
    - type: f1
      name: ot_f1
      value: 0.891
---

# pannnnnnn/4_labels

## Model Summary
這是一個 **中文論壇評論四分類模型**，輸入遊戲討論文字後，輸出以下四類標籤之一：
- **0 = 負面**
- **1 = 中立**
- **2 = 正面**
- **3 = OT (Off-topic, 離題)**

模型專門應用於 **任天堂馬力歐系列遊戲**的社群評論（如 Dcard、Mobile01、PTT、巴哈姆特），研究目的是分析論壇情緒與股價走勢的關聯。

特色：
- **關鍵字白名單規則**：若文字（或任一分段）包含「奧德賽 / 3D世界 / 狂怒 / 創作家 / 馬創」，則強制視為非 OT。  
- **長文本切段**：對超過 512 token 的文字自動分段推論，最後取平均機率。  
- **一體化模型**：一次輸出四類，不需 Stage1 / Stage2。  

---

## Model Details
- **Developed by:** pannnnnnn  
- **Language(s):** zh-TW, zh-CN（主要為繁體中文）  
- **Model type:** Transformer (RoBERTa-zh base finetuned)  
- **License:** Research use (non-commercial)  
- **Finetuned from:** `hfl/chinese-roberta-wwm-ext`  

---

## Training Details

### Training Data
- 來源：台灣遊戲論壇（Dcard、Mobile01、PTT、巴哈姆特），自建爬蟲收集。  
- 清理：去掉網址、簽名檔、重複貼文；正規化全半形字；保留 emoji。  
- 人工標註：四類（負面、中立、正面、OT）。  

### Training Procedure
- Optimizer: AdamW  
- Loss: CrossEntropy (focal loss variant)  
- Batch size: 32  
- Epochs: 3  
- Mixed precision: fp16  

---

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data
- **切分方式**：依 `timestamp` 欄位排序後，以時間先後劃分資料集。  
- **分配比例**：最後 10% 的資料作為 **Test Set**；倒數前 15% 作為 **Validation Set**；其餘為 **Training Set**。  
- **目的**：模擬「訓練只能使用過去資料，測試用未來資料」，避免資訊洩漏 (data leakage)。  

#### Factors
- 不同子遊戲（如《奧德賽》《3D世界＋狂怒世界》《創作家》）在情緒分布上的差異。  
- 貼文長度（短文 vs 長文）對分類效果的影響。  

#### Metrics
- Accuracy  
- Macro-F1  
- Per-class F1  

### Results

| Label | Precision | Recall | F1   | Support |
|-------|-----------|--------|------|---------|
| neg   | 0.964     | 0.915  | 0.939| 59      |
| neu   | 0.789     | 0.759  | 0.774| 54      |
| pos   | 0.738     | 0.882  | 0.804| 51      |
| ot    | 0.930     | 0.855  | 0.891| 62      |
| **Accuracy** | – | – | **0.854** | 226 |
| **Macro avg** | 0.855 | 0.853 | 0.852 | – |
| **Weighted avg** | 0.862 | 0.854 | 0.856 | – |

---

## Uses

### Direct Use
- 輸入論壇貼文 / 留言，判斷其情緒或是否離題。  
- 適合研究用途（例如：情緒與股價關聯分析、論壇口碑追蹤）。  

### Downstream Use
- 可再微調到其他領域的四類情緒分類。  
- 可改成三類情緒（合併 OT 與中立）或二類情緒。  

### Out-of-Scope Use
- 不適用於醫療、法律、金融決策。  
- 不適合處理極短、缺乏上下文的片段。  

---

## Bias, Risks, Limitations
- **資料來源偏差**：主要來自遊戲論壇，不能泛用到所有中文語境。  
- **諷刺/雙關困難**：模型可能誤判反諷、梗文。  
- **跨遊戲混淆**：若評論同時提及其他遊戲，判斷可能不準。  

**建議**：搭配人工檢視與統計，避免單一模型輸出直接做高風險決策。  

---

## How to Use

```python
from transformers import pipeline

pipe = pipeline("text-classification",
                model="pannnnnnn/4_labels",
                truncation=True,
                top_k=None)

print(pipe("這代真的比奧德賽更好玩！"))
# [{'label': 'positive', 'score': 0.92}]
