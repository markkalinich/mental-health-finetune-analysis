---
license: apache-2.0
language:
- en
metrics:
- f1
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
library_name: transformers
---
# 🛡️ Content Moderation Model (DistilBERT Fine-Tuned)

##  Model Description
This model is based on **[DistilBERT](https://huggingface.co/distilbert-base-uncased)** and fine-tuned on the **Jigsaw Toxic Comment Classification dataset** for **multi-label content moderation**.  
It can detect multiple forms of toxic or harmful language in English comments, including:

- toxic  
- severe_toxic  
- obscene  
- threat  
- insult  
- identity_hate  
- safe (added when no toxic categories apply)  

DistilBERT is a smaller, faster version of BERT while retaining most of its performance, making it suitable for real-time moderation tasks.

---

## 🏷️ Intended Use
- Moderating **online communities** (forums, chat apps, social media).  
- Filtering **toxic comments** in user-generated text.  
- Educational and research purposes.  

⚠️ **Not for production without further evaluation.** Models may misclassify sarcasm, slang, or subtle harassment. Always use human moderators for critical cases.

---

## 📊 Training Details
- **Base model**: `distilbert-base-uncased`  
- **Dataset**: [Jigsaw Toxic Comment Classification](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)  
- **Task**: Multi-label classification (comments can have multiple labels).  
- **Labels**: toxic, severe_toxic, obscene, threat, insult, identity_hate, safe  
- **Hyperparameters**:  
  - Batch size: 16 (train), 32 (eval)  
  - Learning rate: 1e-5  
  - Epochs: 5  
  - Weight decay: 0.01  
- **Metric**: Macro-F1  

---

## 📈 Evaluation Results
Validation performance (held-out split):
- **Macro-F1 Score**: ~0.91  
- Training loss stabilized around ~0.14  
- Validation loss ~0.15  

✅ Strong at detecting direct insults and threats.  
⚠️ Struggles with **sarcasm or subtle negativity**.  

---

## 🚀 How to Use
```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="your-username/content-moderation-distilbert",
    tokenizer="your-username/content-moderation-distilbert",
    return_all_scores=True,
    function_to_apply="sigmoid"   # multi-label classification
)

texts = [
    "You are an amazing person and I respect you.",
    "I hate you, you are disgusting!",
    "I will not kill you tomorrow"
]

for t in texts:
    preds = classifier(t)
    print(f"\nInput: {t}")
    for label in preds[0]:
        print(f"{label['label']}: {label['score']:.3f}")