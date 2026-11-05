---
library_name: transformers
tags:
- finance
- sentiment-analysis
- twitter
- turkish
- prediction
- transformers
- bert
license: mit
base_model:
- dbmdz/bert-base-turkish-128k-uncased
---

# ❤️ Prediction Sentiment Classifier

This model classifies the **sentiment of stock prediction phrases** from Turkish finance-related tweets.  
It’s used to assign a tone (e.g., **positive** or **negative**) to the predicted movement of a stock.

🧾 Example:
> `"will reach 80 TL soon"` → Positive  
> `"may fall to 25 TL next week"` → Negative

---

## 🧠 Model Details

- **Developed by:** damlakonur  
- **Model type:** `BERT` fine-tuned for `sequence classification`  
- **Language(s):** Turkish  
- **Finetuned from:** `bert-base-cased`  
- **License:** MIT  
- **Classes:** `LABEL_0` = Negative, `LABEL_1` = Positive

---

## 🚀 How to Use

```python
from transformers import pipeline

model = pipeline("text-classification", model="your-username/prediction-sentiment-bist30")

output = model("will reach 80 TL soon")
print(output)