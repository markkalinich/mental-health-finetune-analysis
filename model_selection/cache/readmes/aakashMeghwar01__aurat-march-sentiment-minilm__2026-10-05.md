---
language:
- ur
tags:
- sentiment-analysis
- aurat-march
- urdu-news
- pakistan
- text-analytics
- computational-linguistics
- low-resource-nlp
license: apache-2.0
base_model: microsoft/Multilingual-MiniLM-L12-H384
model-index:
- name: aurat-march-sentiment-minilm
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    metrics:
    - type: accuracy
      value: 0.83
    - type: f1
      value: 0.83
      name: Weighted F1
datasets:
- aakashMeghwar01/aurat-march-processed-news
metrics:
- accuracy
- f1
pipeline_tag: sentence-similarity
---

# Aurat March Sentiment Analysis (Urdu & English)

Fine-tuned `microsoft/Multilingual-MiniLM-L12-H384` for three-class sentiment classification of Pakistani news coverage of the Aurat March feminist movement.

**Labels:** `Oppositional` · `Supportive` · `Neutral`

Developed as part of the Master's Thesis *"Compact Transformer-Based Sentiment Analysis of Aurat March Media Coverage in Urdu and English"* at HSE University, Nizhny Novgorod.

## Usage
```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="aakashMeghwar01/aurat-march-sentiment-minilm"
)

# English example
classifier("The Aurat March is an important movement for women's rights in Pakistan")
# → [{'label': 'Supportive', 'score': 0.87}]

# Urdu example
classifier("عورت مارچ کے نعرے اسلامی اقدار کے خلاف ہیں")
# → [{'label': 'Oppositional', 'score': 0.79}]
```

## Evaluation

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| Oppositional | 0.89 | 0.81 | 0.85 | 21 |
| Supportive | 0.83 | 0.88 | 0.86 | 17 |
| Neutral | 0.67 | 0.75 | 0.71 | 8 |
| **Weighted avg** | **0.83** | **0.83** | **0.83** | **46** |

## Training

- **Base model:** `microsoft/Multilingual-MiniLM-L12-H384`
- **Training corpus:** 470 annotated Urdu and English news articles (Aurat March coverage 2018–2023)
- **Class weighting:** WeightedTrainer with inverse-frequency weights to handle class imbalance
- **Epochs:** 10 · **Batch size:** 16 · **Learning rate:** 2e-5
- **Hardware:** Google Colab T4 GPU

## Labels

| ID | Label | Description |
|----|-------|-------------|
| 0 | Oppositional | Article frames the Aurat March negatively |
| 1 | Supportive | Article frames the Aurat March positively |
| 2 | Neutral | Procedural/balanced reporting |

## Citation
```
Meghwar, A. (2025). Compact Transformer-Based Sentiment Analysis of Aurat March 
Media Coverage in Urdu and English. MA Thesis, HSE University Nizhny Novgorod.
Model: https://huggingface.co/aakashMeghwar01/aurat-march-sentiment-minilm
```

## Contact

**Aakash Meghwar** · aakashmeghwar01@gmail.com · [LinkedIn](https://www.linkedin.com/in/aakashmeghwar/)
It utilizes a **Compact Transformer (MiniLM-L12-v2)** architecture, fine-tuned specifically to navigate the nuanced socio-political discourse of the Aurat March in Pakistan. The model is optimized for high performance on consumer-grade hardware (T4 GPUs), adhering to the "Green AI" philosophy of accessible NLP for low-resource languages.

## 🚀 About the Author
I am **Aakash Meghwar**, a Computational Linguist specializing in South Asian languages. 
* 🎓 **M.S. in Applied Linguistics & Text Analytics** (HSE, Russia - Graduating June 2026)
* 🎓 **B.S. in English Language & Literature** (NUML, Islamabad)
* 💡 **Founder:** [Text Tech Solutions](https://texttechsolutions.com)
* ✍️ **Published Researcher:** Author of *"Compact Transformer Models for Classical Urdu Poetry"* (Corporum Journal).

## 🤝 Open for Collaboration & PhD Opportunities
I am actively seeking **PhD opportunities** and **Research Collaborations** in the following areas:
* **Low-Resource NLP:** Developing efficient models for Sindhi, Urdu, and Siraiki.
* **Literary Informatics:** Computational stylistics and affective registers in classical poetry.
* **SindhiLM Evolution:** I am currently developing **SindhiLM-v2** (featuring an improved Sindhi-BPE tokenizer and knowledge distillation).

**Are you looking for a researcher to join your NLP lab or organization?** I am open to discussing projects involving Model Compression, Cross-Lingual Transfer, and South Asian Language Tech.

## 📩 Contact & Links
- **Email:** aakashmeghwar01@gmail.com
- **LinkedIn:** [Aakash Meghwar](https://www.linkedin.com/in/aakashmeghwar/)
- **Projects:** [SindhiLM](https://huggingface.co/aakashMeghwar01/SindhiLM) | [Urdu Poetry Research](https://github.com/aakashMeghwar01)


## How to use
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="aakashMeghwar01/aurat-march-sentiment-minilm")
# Example Urdu input
classifier("عورت مارچ خواتین کے حقوق کی ایک اہم تحریک ہے")