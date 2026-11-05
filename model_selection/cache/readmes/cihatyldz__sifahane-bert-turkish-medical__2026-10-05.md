---
language:
  - tr
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - bert
  - turkish
  - medical
  - text-classification
  - healthcare
  - nlp
  - fine-tuned
  - clinical-nlp
datasets:
  - cihatyldz/sifahane-turkish-medical-complaints
base_model: dbmdz/bert-base-turkish-cased
model-index:
  - name: sifahane-bert-turkish-medical
    results:
      - task:
          type: text-classification
          name: Text Classification
        dataset:
          name: Sifahane Turkish Medical Complaints
          type: cihatyldz/sifahane-turkish-medical-complaints
        metrics:
          - type: accuracy
            value: 0.993
            name: Accuracy
          - type: f1
            value: 0.993
            name: F1 (macro)
---

# 🏥 Şifahane — Turkish Medical Text Classification (BERT)

A fine-tuned **Turkish BERT** model for classifying patient complaints into **12 medical departments** with high accuracy.

This model is part of the [Şifahane project](https://huggingface.co/spaces/cihatyldz/sifahane-turkish-medical), a dual-model medical triage demo comparing a fine-tuned BERT classifier against a zero-shot LLM.

## Model Overview

| Property | Value |
|---|---|
| **Base Model** | [`dbmdz/bert-base-turkish-cased`](https://huggingface.co/dbmdz/bert-base-turkish-cased) |
| **Language** | Turkish (tr) |
| **Task** | Multi-class Text Classification (12 classes) |
| **Parameters** | ~111M |
| **Inference Speed** | ~15–130 ms on CPU |
| **License** | Apache 2.0 |

## Intended Use

**Primary use case:** Classifying Turkish patient complaints into the appropriate medical department for triage routing.

**Input:** Free-text patient complaint in Turkish.  
**Output:** Predicted department label with confidence scores.

### Example

```
Input:  "Göğsümde şiddetli ağrı var, sol koluma yayılıyor, terleme eşlik ediyor."
Output: Kardiyoloji (98.7%)
```

## Supported Classes (12 Departments)

| # | Department | Description |
|---|---|---|
| 0 | **Dermatoloji** | Skin conditions (eczema, fungal infections, allergies) |
| 1 | **Endokrinoloji** | Hormonal/metabolic disorders (diabetes, thyroid) |
| 2 | **Gastroenteroloji** | Digestive system (gastritis, liver, IBS) |
| 3 | **Göğüs Hastalıkları** | Respiratory (asthma, COPD, pneumonia) |
| 4 | **Göz Hastalıkları** | Eye conditions (conjunctivitis, glaucoma) |
| 5 | **KBB** | Ear, nose, throat (sinusitis, otitis, tonsillitis) |
| 6 | **Kadın Doğum** | Obstetrics & gynecology |
| 7 | **Kardiyoloji** | Cardiovascular (hypertension, arrhythmia, coronary) |
| 8 | **Nöroloji** | Neurological (migraine, epilepsy, stroke, vertigo) |
| 9 | **Ortopedi** | Musculoskeletal (disc herniation, meniscus, fractures) |
| 10 | **Psikiyatri** | Mental health (depression, anxiety, sleep disorders) |
| 11 | **Üroloji** | Urological (UTI, kidney stones, prostate) |

## Quick Start

### With Transformers Pipeline

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="cihatyldz/sifahane-bert-turkish-medical",
    top_k=3,
)

result = classifier("Midemde şiddetli yanma var, 2 haftadır devam ediyor.")
print(result)
# [[{'label': 'Gastroenteroloji', 'score': 0.98}, ...]]
```

### Manual Inference

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "cihatyldz/sifahane-bert-turkish-medical"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

text = "Başımın sol tarafında zonklayıcı ağrı var, ışığa hassaslaştım."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)[0]

pred_id = probs.argmax().item()
label = model.config.id2label[pred_id]
confidence = probs[pred_id].item()

print(f"Department: {label} ({confidence:.1%})")
# Department: Nöroloji (97.2%)
```

## Training Details

### Dataset

- **Source:** [`cihatyldz/sifahane-turkish-medical-complaints`](https://huggingface.co/datasets/cihatyldz/sifahane-turkish-medical-complaints)
- **Size:** ~6,000 synthetic Turkish patient complaints
- **Generation Method:** Template-based synthesis with randomized clinical parameters (duration, intensity, symptoms, body location)
- **Coverage:** 12 departments × 36 conditions × 3 urgency levels
- **Split:** 80% train / 10% validation / 10% test (stratified)

### Training Configuration

| Hyperparameter | Value |
|---|---|
| Base model | `dbmdz/bert-base-turkish-cased` |
| Epochs | 4 |
| Batch size | 32 |
| Learning rate | 2e-5 |
| Weight decay | 0.01 |
| Warmup ratio | 0.1 |
| Max sequence length | 128 |
| Optimizer | AdamW |
| LR scheduler | Linear with warmup |
| FP16 | Enabled |
| Early stopping | Patience = 2 (metric: F1 macro) |

### Training Infrastructure

- **Hardware:** NVIDIA Tesla T4 (Google Colab)
- **Training time:** ~5–10 minutes
- **Framework:** Hugging Face Transformers + Trainer API

## Evaluation Results

Evaluated on the held-out test split (~600 examples):

| Metric | Score |
|---|---|
| **Accuracy** | ~99.3% |
| **F1 (macro)** | ~99.3% |
| **F1 (weighted)** | ~99.3% |

> **Note:** High scores reflect the synthetic nature of the training data with clear template patterns. Real-world clinical text would yield lower but still useful performance. The model demonstrates strong pattern recognition within its training distribution.

## Live Demo

Try the model in action at the **Şifahane Space**, where it runs side-by-side with a zero-shot LLM (Qwen2.5-7B):

🚀 **[Şifahane Demo](https://huggingface.co/spaces/cihatyldz/sifahane-turkish-medical)**

The demo compares two approaches:

| | BERT Classifier (this model) | LLM (Qwen2.5-7B) |
|---|---|---|
| **Speed** | ~15–130 ms (CPU) | ~1–3 s (Inference API) |
| **Approach** | Fine-tuned, single-task | Zero-shot, multi-task |
| **Flexibility** | Fixed categories | Open-ended |
| **Cost** | Free (CPU) | Free (HF Inference API) |

## Project Portfolio

This model is part of a Turkish NLP portfolio demonstrating three different AI architectures across three domains:

| Project | Domain | Architecture | Link |
|---|---|---|---|
| 🪙 **Akçe** | Banking | Fine-tuned LLM (Generative) | [Space](https://huggingface.co/spaces/cihatyldz/banka-gpt-turkce) |
| 🐪 **Kervan** | Logistics | RAG (Retrieval + Generative) | [Space](https://huggingface.co/spaces/cihatyldz/kervan-lojistik-rag) |
| 🏥 **Şifahane** | Healthcare | Dual-Model (Classifier vs LLM) | [Space](https://huggingface.co/spaces/cihatyldz/sifahane-turkish-medical) |

## Limitations & Ethical Considerations

- **Not a medical device:** This model is for research and educational purposes only. It should never be used for actual medical diagnosis or triage decisions.
- **Synthetic training data:** The model was trained on template-generated data, not real clinical records. Performance on real-world patient language may differ.
- **Turkish only:** The model is designed for Turkish text and will not perform well on other languages.
- **Fixed taxonomy:** The model only supports the 12 predefined departments. Complaints outside these categories may be misclassified.
- **No urgency assessment:** This model predicts department only. Urgency classification requires additional logic (see the Şifahane Space for a rule-based urgency module).

## Citation

```bibtex
@misc{yildiz2025sifahane,
  author       = {Cihat Yıldız},
  title        = {Şifahane: Turkish Medical Text Classification with Fine-tuned BERT},
  year         = {2025},
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/cihatyldz/sifahane-bert-turkish-medical}
}
```

## Contact

- **Developer:** Cihat Yıldız
- **Hugging Face:** [@cihatyldz](https://huggingface.co/cihatyldz)
- **Demo:** [Şifahane Space](https://huggingface.co/spaces/cihatyldz/sifahane-turkish-medical)
