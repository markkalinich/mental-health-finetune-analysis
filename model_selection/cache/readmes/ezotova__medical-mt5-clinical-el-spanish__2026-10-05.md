---
license: cc-by-nc-4.0
language:
- es
base_model:
- HiTZ/Medical-mT5-large
pipeline_tag: text-generation
tags:
- medical
datasets:
- Biomedical-TeMU/CodiEsp_corpus
- DrBenchmark/E3C
- IIC/CT-EBM-SP
metrics:
- rouge
- bertscore
- bleu
- meteor
- accuracy
---


# medical-mt5-clinical-el-spanish

A generative model for **clinical entity linking** (ICD-10-CM/ES coding) in Spanish, fine-tuned from [HiTZ/Medical-mT5-large](https://huggingface.co/HiTZ/Medical-mT5-large) on Spanish clinical text corpora.

Given a clinical mention extracted from a medical document, the model generates the corresponding ICD-10 code in a sequence-to-sequence fashion. 

---

## Model Description

| Attribute | Details |
|---|---|
| **Architecture** | mT5-large (encoder-decoder) |
| **Base model** | [HiTZ/Medical-mT5-large](https://huggingface.co/HiTZ/Medical-mT5-large) |
| **Task** | Clinical entity linking / ICD-10 coding |
| **Language** | Spanish (`es`) |
| **Parameters** | ~1.2B |
| **Precision** | float32 |
| **License** | CC BY-NC 4.0 |

This model is part of a comparative study on generative approaches to clinical entity linking in Spanish. 
It is one of several fine-tuned variants explored in the associated paper.

---

## Intended Use

### Primary Use
- Automated ICD-10 code assignment from Spanish clinical text mentions
- Clinical NLP pipelines for Spanish electronic health records (EHRs)
- Research on generative entity linking in low-resource medical settings

### Out-of-Scope Use
- Non-clinical or general-domain text
- Languages other than Spanish
- Direct clinical decision-making without human expert oversight

---

## Training Data

The model was fine-tuned on three Spanish clinical NLP datasets:

| Dataset | Description |
|---|---|
| [Biomedical-TeMU/CodiEsp_corpus](https://huggingface.co/datasets/Biomedical-TeMU/CodiEsp_corpus) | CodiEsp shared task corpus — Spanish clinical cases annotated with ICD-10 codes (diagnoses and procedures) |
| [DrBenchmark/E3C](https://huggingface.co/datasets/DrBenchmark/E3C) | European clinical corpus with entity annotations across multiple languages, including Spanish |
| [IIC/CT-EBM-SP](https://huggingface.co/datasets/IIC/CT-EBM-SP) | Spanish clinical trial corpus annotated for biomedical entities |
| [Mantra GSC](https://huggingface.co/datasets/bigbio/mantra_gsc) | Medline abstract titles, drug labels, biomedical patent claims in Spanish |


## Evaluation

Performance is reported as mean ± standard deviation across three runs with different random seeds on the CodiEsp corpus.


| Split | Model | PLI | PLII |
|---|---|---|---|
| TEST | **Medical-mT5-C+M** | **70.46 ± 0.32** | **77.04 ± 0.35** |
| TEST UNSEEN | **Medical-mT5-C+M** | **42.46 ± 1.46** | **53.49 ± 1.34** |

The **TEST UNSEEN** split contains entity mentions whose surface forms were not seen during training, providing a stricter evaluation of generalization.

**C** refers to the context, which means that the training data was prepared as a concatenation of the entity mention and the sentence where it occurs. 

**+M** refers to Mapped corpus, which were created from the corpora annotated with UMLS CUIs but was mapped to ICD-10 automatically with [ClinIDMap](https://github.com/Vicomtech/ClinIDMap)

**PLI (Pipeline I)** — the model's generated text is compared against all ICD-10 code descriptions in the knowledge base using normalized string matching (diacritics removed, lowercased). A code is assigned when an exact match is found.

**PLII (Pipeline II)** — extends Pipeline I with semantic text similarity (STS). The generated text and all ICD-10 descriptions are embedded using multilingual SapBERT; the nearest neighbour in the vector space (L2 distance) determines the predicted code. This handles cases where the generated output is semantically close to the correct description but not an exact string match.


---

## How to Use

```python
from transformers import AutoConfig, MT5ForConditionalGeneration, AutoTokenizer

model_name = "ezotova/medical-mt5-clinical-el-spanish"
tokenizer = AutoTokenizer.from_pretrained(model_name)

config = AutoConfig.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name, config=config)

# Example: entity mention from a clinical note
def make_prompt(term, sentence):
    return f"Genera una definición para el término: {term} - en la frase: {sentence}"

term = "TC abdominal"
sentence = "La TC abdominal es normal."

prompt = make_prompt(term, sentence)

inputs = tokenizer(prompt, return_tensors="pt", padding=True)

outputs = model.generate(
    **inputs,
    max_new_tokens=128,
    num_beams=5,
    early_stopping=True
)

prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(prediction)

# Expected: tomografía computarizada (scanner tc) de abdomen [Code: BW20]

```

---

## Citation

```bibtex
@article{zotova2025clinical,
  title     = {Generative Models for Clinical Entity Linking in Spanish},
  author    = {Zotova, Elena and Cuadros, Montse and Rigau, German},
  journal   = {Preprint submitted to Elsevier: Available at SSRN 5976036},
  year      = {2026},
  doi       = {[DOI]}
}
```

---

## Ethical Considerations

- This model is intended **for research purposes only** and should not be used as a standalone clinical coding tool without expert review.
- Training data consists of de-identified or synthetic clinical text; however, users should exercise caution when applying the model to real patient data.
- Performance may vary across clinical specialties, document types, and ICD-10 coding guidelines versions.

---

## Acknowledgements

This work was carried out at [Vicomtech](https://www.vicomtech.org/) in collaboration with the [HiTZ Center](https://www.hitz.eus/) (UPV/EHU). 

The base model [HiTZ/Medical-mT5-large](https://huggingface.co/HiTZ/Medical-mT5-large) was developed at HiTZ/IXA and is gratefully acknowledged.
