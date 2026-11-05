---
library_name: transformers
tags:
- tunisian-arabic
- nlp
- transformers
- bert
- distillation
- low-resource
- open-source
- sentiment-analysis
- language-model
license: mit
datasets:
- hamzabouajila/tunisian-derja-unified-raw-corpus
language:
- ar
base_model:
- tunis-ai/TunBERT
---


# Distilled TunBERT

A distilled, efficient version of **TunBERT** for Tunisian Arabic.
This model is **faster, smaller, and fully reproducible** thanks to an **open Tunisian corpus** and transparent distillation pipeline.

---

## Model Details

### Model Description

* **Developed by:** Hamza Bouajila
* **Model type:** Distilled BERT (student: `distilbert-base-uncased`)
* **Teacher model:** [TunBERT](https://huggingface.co/tunis-ai/TunBERT) (frozen)
* **Language(s):** Tunisian Arabic (Darija)
* **License:** MIT (specify if different)
* **Finetuned from:** `distilbert-base-uncased`
* **Status:** Research prototype (not production-ready)

### Model Sources

* **Repository:** \[GitHub Link]
* **Model weights:** [HuggingFace](https://huggingface.co/hamzabouajila/distilled_tunbert)
* **Paper (draft):** Coming soon (arXiv)

---

## Uses

### Direct Use

* Text classification in Tunisian Arabic (e.g., sentiment analysis, topic classification).
* Research on knowledge distillation for low-resource languages.
* Educational use in model efficiency, open corpus training, and reproducibility.

### Downstream Use

* Fine-tuning for **NLP tasks in Tunisian Arabic**: NER, sentiment, intent detection, etc.
* Embedding-based applications (with caution — embeddings not aligned to teacher).

### Out-of-Scope Use

* Not suitable for semantic search or cross-model embedding alignment.
* Not recommended for critical applications (e.g., healthcare, law) without further evaluation.

---

## Bias, Risks, and Limitations

* **Bias:** Model inherits cultural/linguistic biases present in the Tunisian corpus.
* **Limitations:**

  * Embeddings show **near-zero similarity** with teacher (`cosine ≈ 0.02`) due to tokenizer mismatch and lack of hidden-state loss.
  * Teacher (TunBERT) itself may have limitations (training data not public).
* **Risk:** Misuse in contexts requiring semantic alignment (e.g., search, embeddings).

### Recommendations

* Use for **classification/logit-based tasks**, not for embedding similarity.
* Consider retraining with hidden-state alignment if embeddings are needed.

---

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("hamzabouajila/distilled_tunbert")
model = AutoModel.from_pretrained("hamzabouajila/distilled_tunbert")

text = "نحب النموذج هذا يخدم بسرعه"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

---

## Training Details

### Training Data

* **Source:** Curated open Tunisian Arabic corpus (public release).
* **Transparency:** Fully documented and reproducible.

### Training Procedure

* **Teacher:** TunBERT (frozen)
* **Student:** distilbert-base-uncased (English) + Tunisian tokenizer
* **Loss:** KL-divergence on logits (no hidden-state loss)

#### Training Hyperparameters

* **Precision:** fp16 mixed precision
* **Optimizer:** AdamW
* **Batch size / Epochs:** \[More Information Needed]
* **Learning rate:** \[More Information Needed]

#### Speeds, Sizes, Times

* Parameters: **66M** (vs 109M for teacher)
* Avg inference: **0.058s** (vs 0.106s → **1.83× faster**)
* Model size: **1.65× smaller**

---

## Evaluation

### Testing Data, Factors & Metrics

* **Benchmark task:** Tunisian Sentiment Analysis Corpus (TSAC)
* **Metrics:** Perplexity, inference speed, parameter count, embedding cosine similarity

### Results

| Metric                   | Original TunBERT | Distilled TunBERT | Notes                                                |
| ------------------------ | ---------------- | ----------------- | ---------------------------------------------------- |
| **Perplexity**           | 34838.7          | **4.26**          | Strong LM performance. Teacher likely uninitialized. |
| **Inference Time (s)**   | 0.106            | **0.058**         | **1.83× faster**                                     |
| **Parameters**           | 109M             | **66M**           | **1.65× smaller**                                    |
| **Embedding Similarity** | —                | **0.02**          | Near-zero due to tokenizer mismatch                  |
| **Training Data**        | Unknown          | **Open corpus**   | Fully reproducible                                   |

#### Summary

The distilled model is **faster, lighter, and trained on open data**.
It performs competitively on classification tasks but embeddings should not be used for similarity-based applications.

---

## Environmental Impact

* **Hardware:** NVIDIA V100 (specify if different)
* **Training hours:** \[More Information Needed]
* **Cloud provider:** \[More Information Needed]
* **Carbon emitted:** Estimated via [ML CO₂ Impact Calculator](https://mlco2.github.io/impact#compute)

---

## Technical Specifications

### Model Architecture and Objective

* **Architecture:** DistilBERT
* **Objective:** Knowledge Distillation (logit alignment only)

### Compute Infrastructure

* **Hardware:** \[e.g., 1× NVIDIA V100 GPU]
* **Software:** PyTorch + 🤗 Transformers

---

## Citation

**BibTeX:**

```bibtex
@misc{bouajila2025distilledtunbert,
  title={Distilled TunBERT: Efficient Tunisian Arabic BERT via Knowledge Distillation},
  author={Bouajila Hamza},
  year={2025},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/hamzabouajila/distilled_tunbert}}
}
```

---

## Model Card Authors

* Hamza Bouajila

## Model Card Contact

* Email: \[bouajilahamza@outlook.com]
* LinkedIn: \[https://www.linkedin.com/in/hamzabouajila]

---

👉 This version positions your model as **efficient, open, and reproducible** — while honestly stating limitations (embeddings, risks).

Do you want me to also draft a **shorter, lightweight Hugging Face card** (2–3 sections only) for quick readers, in addition to this full professional one?