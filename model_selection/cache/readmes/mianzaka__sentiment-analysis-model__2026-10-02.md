---
license: cc-by-nc-4.0
tags:
  - sentiment-analysis
  - text-classification
  - nlp
language:
  - en
---

# Amazon Reviews Sentiment Analysis Model

## Model Description
This model is a **sentiment analysis model** fine-tuned using **BertForSequenceClassification** on the **Amazon Reviews dataset**.
It classifies Amazon product reviews into sentiment categories: negative, neutral, or positive.
Intended for **research, educational, and non-commercial use only**.

---

## Base Model
* **bert-base-uncased**
* Architecture: Transformer (BERT)
* Head: Sequence Classification
---

## Intended Use

### ✅ Allowed Uses
* Academic research
* Educational projects
* Personal learning
* Non-commercial applications
* Experiments and benchmarking

### ❌ Prohibited Uses
* Commercial use
* Selling or reselling the model
* Paid APIs or SaaS products
* Monetized applications or services

Commercial use is **strictly prohibited** under the CC BY-NC 4.0 license.

---

## Training Data
Trained on the **Amazon Reviews dataset**:
* Language: English
* Domain: E-commerce product reviews
* Data type: Text reviews with sentiment labels

The original dataset creators retain all rights to the data. Users should consult the dataset’s original license for details.

---

## Training Procedure
* Model: BertForSequenceClassification
* Framework: Hugging Face Transformers
* Number of labels: 3
* Loss Function: Cross-entropy loss
* Training performed on GPU if available, otherwise CPU

### Label Mapping
| Label ID | Sentiment |
| -------- | --------- |
| 0        | Negative  |
| 1        | Neutral   |
| 2        | Positive  |

---

## Evaluation
Evaluated using a **multi-class classification report** with three categories:
* Negative
* Neutral
* Positive

Metrics include precision, recall, F1-score, and support (per class).
Performance may vary depending on product category and review style.

---

## Limitations and Bias
* Reflects biases in Amazon reviews
* May not perform well on non-product text
* Not suitable for non-English languages
* Predictions are subjective, not factual judgments
---

## Ethical Considerations
Analyze subjective content only; not for high-stakes decisions.

---

## How to Use
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "mianzaka/sentiment-analysis-model"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "The product quality is decent but delivery was slow."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)

predicted_label = torch.argmax(outputs.logits, dim=1).item()
label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
print("Predicted sentiment:", label_map[predicted_label])
```

---

## License
Released under **CC BY-NC 4.0**. Commercial use, resale, or monetization is prohibited.
Full license: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

---

## Citation
```bibtex
@misc{sentiment-analysis-model,
  author = {Mian Zaka},
  title  = {Amazon Reviews Sentiment Analysis Model},
  year   = {2026},
  publisher = {Hugging Face}
}
```

---

## Contact
For questions or feedback, contact the model author via Hugging Face.