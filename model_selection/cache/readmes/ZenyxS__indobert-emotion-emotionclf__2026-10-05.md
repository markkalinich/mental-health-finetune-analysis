---
library_name: transformers
license: apache-2.0
language:
- id
tags:
- emotion-classification
- indonesian
- bert
- student-research
- conversational-ai
- classification
---

# 🤖 IndoBERT Emotion Classifier

A fine-tuned IndoBERT model for **Indonesian-language emotion classification** in conversational or chatbot contexts.  
This model was developed as part of a research project on detecting **user satisfaction and emotional states** from short-text feedback and responses.

It classifies input text into one of five emotions:

- 😄 **Senang** — Happy / satisfied  
- 😐 **Netral** — Neutral / indifferent  
- 🤔 **Bingung** — Confused / unsure  
- 😤 **Frustrasi** — Frustrated / unsatisfied  
- 😡 **Marah** — Angry / annoyed

---

## 📌 Model Details

- **Model name:** `username/indobert-emotion-classifier`  <!-- replace `username` with your HF username -->
- **Developed by:** Fabian Prasetyo  
- **Institution:** SMKN 21 Jakarta  
- **Language:** Indonesian (`id`)  
- **License:** Apache 2.0  
- **Base model:** [indobenchmark/indobert-base-p1](https://huggingface.co/indobenchmark/indobert-base-p1)  
- **Task:** Emotion classification from short conversational text  
- **Number of classes:** 5  

---

## 🎯 Use Cases

### ✅ Direct Use
- Emotion recognition for Indonesian chatbot conversations.  
- Sentiment/feedback analysis for educational or customer service systems.  
- Emotion-aware dialogue systems and virtual assistants.

### 🔄 Downstream Use
- As a module in larger conversational AI systems.  
- As a feature extractor for satisfaction prediction or escalation pipelines.

### 🚫 Out-of-Scope Use
- ❌ Clinical or psychological diagnosis.  
- ❌ Text domains unrelated to conversation or short feedback (e.g., news articles, long essays).

---

## ⚠️ Bias, Risks, and Limitations

- The dataset consists of **student chatbot feedback** and may not generalize beyond similar conversational contexts.  
- Minority labels (`Frustrasi`, `Marah`) are underrepresented — this leads to **low recall** for those classes.  
- Heavy slang, code-switching (Indonesian-English), typos, and non-standard spelling can reduce model accuracy.  
- Use caution before applying in high-risk or safety-critical settings (no clinical/medical decisions, no legal decisions, etc.).

---

## 🚀 Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "username/indobert-emotion-classifier"  # replace 'username' with your HF username
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, return_all_scores=True)

text = "Apaan sih ini, nggak jelas banget!"
print(classifier(text))
✅ Example Output:

python
[
  {'label': 'Frustrasi', 'score': 0.3700},
  {'label': 'Bingung', 'score': 0.3357},
  {'label': 'Netral', 'score': 0.1256},
  {'label': 'Marah', 'score': 0.1058},
  {'label': 'Senang', 'score': 0.0629}
]
```

# 📊 IndoBERT Emotion Classifier

A fine-tuned IndoBERT model for classifying emotions in Indonesian short-chat responses.  
Developed as part of a student research project at **SMKN 21 Jakarta**.

---

## 📁 Dataset

- **Source**: 1,896 annotated chatbot responses  
- **Participants**: 237 students  
- **Label distribution**:
  - Netral: 1,018  
  - Bingung: 442  
  - Senang: 249  
  - Frustrasi: 98  
  - Marah: 89  

⚠️ **Note**: The dataset is imbalanced, particularly for *Frustrasi* and *Marah*. This strongly affects per-class performance.

---

## ⚙️ Training Procedure

- **Train/Test Split**: 80/20  
- **Epochs**: 3  
- **Optimizer**: AdamW  
- **Loss Function**: CrossEntropy with class weights  
- **Precision**: fp32  
- **Hardware**: NVIDIA T4 (~2 min/epoch)  
- **Framework**: 🤗 Transformers + PyTorch  

---

## 🧠 Model Architecture

- **Base Model**: IndoBERT (BERT-base, ~110M parameters)  
  - 12 layers, 768 hidden size, 12 attention heads  
- **Fine-tuning**: All layers (full fine-tune)  

---

## 📈 Evaluation Results

| Label      | Precision | Recall | F1  |
|------------|-----------|--------|-----|
| Senang     | 0.21      | 0.38   | 0.27 |
| Netral     | 0.54      | 0.26   | 0.35 |
| Bingung    | 0.35      | 0.56   | 0.43 |
| Frustrasi  | 0.04      | 0.04   | 0.04 |
| Marah      | 0.00      | 0.00   | 0.00 |

- **Overall Accuracy**: ~0.33  
- **Macro F1**: 0.22  

**Interpretation**:  
The model captures dominant intents (neutral, confused, positive) reasonably well, but struggles with rare classes (*Frustrasi*, *Marah*) due to dataset imbalance.

---

## 🧪 Example Predictions

```python
def predict(text, classifier):
    scores = classifier(text)[0]
    return sorted(scores, key=lambda x: x["score"], reverse=True)[0]

print(predict("Apaan sih ini, nggak jelas banget!"))
# → Frustrasi (0.37)

print(predict("Aku sangat senang jawabannya jelas sekali"))
# → Senang (0.42)

print(predict("Hah? Maksudnya gimana?"))
# → Bingung (0.37)
```

---


# 🧠 Technical Specifications  

**Architecture:** IndoBERT (BERT-base: 12 layers, 768 hidden, 12 heads, ~110M parameters)  
**Fine-tuning:** Full fine-tuning (all layers)  
**Training time:** ~2 minutes/epoch on NVIDIA T4 (reported)  
**Framework:** 🤗 Transformers + PyTorch  

---

# 🛠️ Recommendations (Actionable)  

### Class imbalance  
- Oversample minority classes.  
- Apply stronger augmentation (back-translation, synonym replacement).  
- Experiment with focal loss or class-balanced loss functions.  

### Preprocessing  
- Normalize slang and common typos.  
- Apply light text normalization:  
  - lowercasing  
  - repeated-character normalization  
  - token-level normalization for common chat abbreviations  

### Data collection  
- Collect more labeled samples for *Frustrasi* and *Marah*.  
- Use active learning to prioritize annotation of high-uncertainty samples.  

### Evaluation  
- Report confidence intervals (e.g., via bootstrap).  
- Provide confusion matrix and per-class metrics.  

### Deployment  
- Apply quantization (e.g., 8-bit) for reduced latency on edge devices.  
- Define fallback policy: escalate or request human review when *Frustrasi* or *Marah* prediction exceeds a threshold.  

---

# 📬 Contact  

**Author:** Fabian Prasetyo  
**Institution:** SMKN 21 Jakarta  
**Email:** fabianprasetyo133@gmail.com  

---

# 📚 Citation  

If you use this model, please cite it as:  

```bibtex
@misc{prasetyo2025indobert,
  title={IndoBERT Emotion Classifier},
  author={Fabian Prasetyo},
  institution={SMKN 21 Jakarta},
  year={2025},
  howpublished={\url{https://huggingface.co/username/indobert-emotion-classifier}}
}