---
language: ar
spaces:
- AymanElbery/arabic-medical-classifier-demo
tags:
- arabic
- medical
- text-classification
- healthcare
- arabertv2
license: apache-2.0
datasets:
- private
pipeline_tag: text-classification
widget:
- text: "ما هي أعراض ارتفاع ضغط الدم؟ [SEP] من أهم الأعراض الصداع والدوخة والنزيف الأنفي."
- text: "ما هو علاج فقر الدم؟ [SEP] يتم علاجه عن طريق تناول مكملات الحديد والأطعمة الغنية بالحديد."
- text: "ما هي أسباب مرض السكري؟ [SEP] بسبب نقص الإنسولين أو مقاومة الجسم له."
---

# Arabic Medical Classification Model (AraBERTv2)

This model classifies **Arabic medical questions and answers** into one of **89 medical categories** such as *Cardiology*, *Neurology*, *Endocrinology*, etc.

It is fine-tuned on a private dataset of **800,000 Arabic (question, answer, classification)** pairs to help in building Arabic healthcare QA systems, virtual assistants, and medical chatbots.

---

## Model Details

| Property | Value |
|-----------|--------|
| **Base model** | [aubmindlab/bert-base-arabertv2](https://huggingface.co/aubmindlab/bert-base-arabertv2) |
| **Language** | Arabic (Modern Standard Arabic + some dialect) |
| **Task** | Text Classification |
| **Number of classes** | 89 |
| **Training samples** | ~800,000 |
| **Evaluation metrics** | Accuracy, F1 Macro, F1 Weighted |
| **Hardware used** | 1 × NVIDIA GPU (CUDA 12.8) |
| **Framework** | Transformers + PyTorch |

---

## ⚙️ How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_id = "YourUsername/arabic-medical-classifier-arabertv2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

question = "ما هي أعراض ارتفاع ضغط الدم؟"
answer = "من أهم الأعراض الصداع والدوخة والنزيف الأنفي أحيانًا."
text = question + tokenizer.sep_token + answer

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
with torch.no_grad():
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)
    pred_id = torch.argmax(probs, dim=-1).item()

print("Predicted class:", model.config.id2label[pred_id])
print("Confidence:", probs[0][pred_id].item())
