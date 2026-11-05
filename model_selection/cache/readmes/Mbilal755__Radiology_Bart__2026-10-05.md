---
language:
- en
metrics:
- rouge-l
tags:
- medical
- summarization
- clinical
- bart
- Radiology
- Radiology Reports
datasets:
- MIMIC-III
widget:
- >-
  post contrast axial sequence shows enhancing large neoplasm left parietal
  convexity causing significant amount edema mass effect study somewhat limited
  due patient motion similar enhancing lesion present inferior aspect right
  cerebellar hemisphere right temporal encephalomalacia noted mra brain shows
  patent flow anterior posterior circulation evidence aneurysm vascular
  malformation
- >-
  seen hypodensity involving right parietal temporal lobes right cerebellar
  hemisphere effacement sulci mild mass effect lateral ventricle hemorrhage new
  region territorial infarction basal cisterns patent mucosal thickening fluid
  within paranasal sinuses aerosolized secretions likely related intubation
  mastoid air cells middle ear cavities clear
- >-
  heart size normal mediastinal hilar contours unchanged widening superior
  mediastinum likely due combination mediastinal lipomatosis prominent thyroid
  findings unchanged compared prior ct aortic knob mildly calcified pulmonary
  vascularity engorged patchy linear opacities lung bases likely reflect
  atelectasis focal consolidation pleural effusion present multiple old
  rightsided rib fractures
inference:
  parameters:
    max_length: 350
---

# Radiology Report Summarization

This model summarizes radiology findings into accurate, informative impressions to improve radiologist-clinician communication.

## Model Highlights

- **Model name:** Radiology_Bart
- **Author:** [Muhammad Bilal](linkedin.com/in/muhammad-bilal-6155b41aa)
- **Model type:** Sequence-to-sequence model
- **Library:** PyTorch, Transformers
- **Language:** English

### Parent Model 
- **Repository:** [GanjinZero/biobart-v2-base](https://huggingface.co/GanjinZero/biobart-v2-base)
- **Paper:** [BioBART: Pretraining and Evaluation of A Biomedical Generative Language Model](https://arxiv.org/pdf/2204.03905.pdf)
 
This model is a version of pretrained BioBart-v2-base model further finetuned on 70,000 radiology reports to generate radiology impressions. It produces concise, coherent summaries while preserving key findings.

## Model Architecture

Radiology_Bart is built on the BioBart architecture, a sequence-to-sequence model which is pre-trained on biomedical-text-data[PubMed](https://pubmed.ncbi.nlm.nih.gov/). The encoder-decoder structure allows it to compress radiology findings into impression statements.

Key components:

- Encoder: Maps input text to contextualized vector representations
- Decoder: Generates output text token-by-token
- Attention: Aligns relevant encoder and decoder hidden states  

## Data

The model was trained on 70,000 deidentified radiology reports split into training (52,000), validation (8,000), and test (10,000) sets. The data covers diverse anatomical regions and imaging modalities (X-ray, CT, MRI).

## Training

- Optimization: AdamW 
- Batch size: 16
- Learning rate: 5.6e-5
- Epochs: 4

The model was trained to maximize the similarity between generated and reference impressions using ROUGE metrics.

## Performance

  **Evaluation Metrics** 
  
| ROUGE-1 score | ROUGE-2 score | ROUGE-L score | ROUGELSUM score |
|---------------|---------------|---------------|-----------------|
|   44.857      |    29.015     |     42.032    |    42.038       |

Demonstrating high overlap with human references.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Pipeline

# Sample findings 
findings = "There is a small lung nodule in the right upper lobe measuring 6 mm. The heart size is normal. No pleural effusion or pneumothorax."

# Load model & tokenizer
summarizer = pipeline("summarization", model="Mbilal755/Radiology_Bart")
tokenizer = AutoTokenizer.from_pretrained("Mbilal755/Radiology_Bart")

# Tokenize findings
inputs = tokenizer(findings, return_tensors="pt")

# Generate summary 
summary = summarizer(findings)[0]['summary_text']

# Print outputs
print(f"Findings: {findings}")
print(f"Summary: {summary}")
```

## Limitations

This model is designed solely for radiology report summarization. It should not be used for clinical decision-making or other NLP tasks.

## Check Demo
   [For Demo Click here](https://huggingface.co/spaces/Mbilal755/Rad_Summarizer)
## Model Card Contact
-  Name: Eng. Muhammad Bilal
- [Muhammad Bilal Linkedin](linkedin.com/in/muhammad-bilal-6155b41aa)
- [Muhammad Bilal GitHub](https://github.com/BILAL0099)
-