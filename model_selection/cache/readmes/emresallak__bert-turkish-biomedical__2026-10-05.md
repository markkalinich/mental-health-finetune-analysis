---
library_name: transformers
tags:
- bert
- turkish
- biomedical
- nlp
---

# Model Card for emresallak/bert-turkish-biomedical

## Model Description

This model is a Turkish biomedical BERT model fine-tuned for natural language processing tasks in the biomedical domain.

It is based on a pre-trained Turkish BERT model and adapted to better understand domain-specific terminology such as medical concepts, clinical language, and biomedical text.

- **Developed by:** emresallak  
- **Model type:** BERT  
- **Language(s):** Turkish  
- **License:** apache-2.0 (recommended, change if different)  
- **Finetuned from model:** dbmdz/bert-base-turkish-cased  

---

## Model Sources

- **Repository:** https://huggingface.co/emresallak/bert-turkish-biomedical  

---

## Uses

### Direct Use

This model can be used for Turkish biomedical NLP tasks such as:

- Text classification  
- Named entity recognition (NER)  
- Semantic understanding of medical text  

### Downstream Use

The model can be further fine-tuned for specific tasks like:

- Clinical text classification  
- Medical entity extraction  
- Question answering in the biomedical domain  

### Out-of-Scope Use

This model should **NOT** be used for:

- Medical diagnosis  
- Clinical decision-making  
- Any real-world healthcare application without expert validation  

---

## Bias, Risks, and Limitations

- The model inherits biases from the original training data  
- Biomedical datasets may contain incomplete or domain-specific biases  
- Performance may degrade on:
  - Non-biomedical Turkish text  
  - Informal language  
  - Out-of-distribution inputs  

### Recommendations

Users should:

- Validate outputs before real-world use  
- Avoid using the model in high-stakes scenarios  
- Perform task-specific fine-tuning when possible  

---

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("emresallak/bert-turkish-biomedical")
model = AutoModel.from_pretrained("emresallak/bert-turkish-biomedical")