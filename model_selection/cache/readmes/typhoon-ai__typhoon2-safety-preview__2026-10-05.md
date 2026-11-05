---
library_name: transformers
tags:
- deberta
- deberta-v3
- mdeberta
- multilingual
language:
- multilingual
- th
- en
license: mit
base_model:
- microsoft/mdeberta-v3-base
---

# Model Card for Typhoon Safety Model

**Typhoon Safety Model**


Typhoon Safety is a lightweight binary classifier built on mDeBERTa-v3-base that detects harmful content in both English and Thai languages, with particular emphasis on Thai cultural sensitivities. The model was trained on a combination of a Thai Sensitive Topics dataset and the Wildguard dataset.

The model is designed to predict safety labels across the following categories: 

<div class="section-header">Thai Sensitive Topics</div>
<table align="center">
  <tr>
    <th colspan="3">Category</th>
  </tr>
  <tr>
    <td>The Monarchy</td>
    <td>Student Protests and Activism</td>
    <td>Drug Policies</td>
  </tr>
  <tr>
    <td>Gambling</td>
    <td>Cultural Appropriation</td>
    <td>Thai-Burmese Border Issues</td>
  </tr>
  <tr>
    <td>Cannabis</td>
    <td>Human Trafficking</td>
    <td>Military and Coup</td>
  </tr>
  <tr>
    <td>LGBTQ+ Rights</td>
    <td>Political Divide</td>
    <td>Religion and Buddhism</td>
  </tr>
  <tr>
    <td>Political Corruption</td>
    <td>Foreign Influence</td>
    <td>National Identity and Immigration</td>
  </tr>
  <tr>
    <td>Freedom of Speech and Censorship</td>
    <td>Vape</td>
    <td>Southern Thailand Insurgency</td>
  </tr>
  <tr>
    <td>Sex Tourism and Prostitution</td>
    <td>COVID-19 Management</td>
    <td>Royal Projects and Policies</td>
  </tr>
  <tr>
    <td>Migrant Labor Issues</td>
    <td>Environmental Issues and Land Rights</td>
    <td></td>
  </tr>
</table>

<div class="section-header">Wildguard Topics</div>
<table>
  <tr>
    <th colspan="3">Category</th>
  </tr>
  <tr>
    <td>Others</td>
    <td>Sensitive Information Organization</td>
    <td>Mental Health Over-reliance Crisis</td>
  </tr>
  <tr>
    <td>Social Stereotypes & Discrimination</td>
    <td>Defamation & Unethical Actions</td>
    <td>Cyberattack</td>
  </tr>
  <tr>
    <td>Disseminating False Information</td>
    <td>Private Information Individual</td>
    <td>Copyright Violations</td>
  </tr>
  <tr>
    <td>Toxic Language & Hate Speech</td>
    <td>Fraud Assisting Illegal Activities</td>
    <td>Causing Material Harm by Misinformation</td>
  </tr>
  <tr>
    <td>Violence and Physical Harm</td>
    <td>Sexual Content</td>
    <td></td>
  </tr>
</table>


## **Model Performance**

### Comparison with Other Models (English Content)
| Model | WildGuard | HarmBench | SafeRLHF | BeaverTails | XSTest | Thai Topic | AVG |
|-------|-----------|-----------|-----------|-------------|---------|------------|-----|
| WildGuard-7B | **75.7** | **86.2** | **64.1** | **84.1** | **94.7** | 53.9 | 76.5 |
| LlamaGuard2-7B | 66.5 | 77.7 | 51.5 | 71.8 | 90.7 | 47.9 | 67.7 |
| LamaGuard3-8B | 70.1 | 84.7 | 45.0 | 68.0 | 90.4 | 46.7 | 67.5 |
| LamaGuard3-1B | 28.5 | 62.4 | 66.6 | 72.9 | 29.8 | 50.1 | 51.7 |
| Random | 25.3 | 47.7 | 50.3 | 53.4 | 22.6 | 51.6 | 41.8 |
| Typhoon Safety | 74.0 | 81.7 | 61.0 | 78.2 | 81.2 | **88.7** | **77.5** |

### Comparison with Other Models (Thai Content)
| Model | WildGuard | HarmBench | SafeRLHF | BeaverTails | XSTest | Thai Topic | AVG |
|-------|-----------|-----------|-----------|-------------|---------|------------|-----|
| WildGuard-7B | 22.3 | 40.8 | 18.3 | 27.3 | 49.5 | 42.2 | 33.4 |
| LlamaGuard2-7B | 64.0 | 75.5 | 46.1 | 65.0 | 85.1 | 45.8 | 63.6 |
| LamaGuard3-8B | 61.4 | 37.5 | 42.4 | 65.3 | **85.7** | 48.1 | 56.7 |
| LamaGuard3-1B | 28.4 | 62.4 | 66.7 | 72.9 | 29.8 | 50.9 | 51.8 |
| Random | 24.5 | 46.6 | 50.4 | 53.0 | 26.6 | 50.9 | 42.0 |
| Typhoon Safety | **71.6** | **80.0** | **58.8** | **76.5** | 81.0 | **88.5** | **76.1** |

- **Model type:** Transformer Encoder
- **Language(s) (NLP):** Thai 🇹🇭 and English 🇬🇧
- **License:** MIT
- **Finetuned from model:** mDeBERTa v3 base https://huggingface.co/microsoft/mdeberta-v3-base


## **How to Get Started with the Model**

Use the code below to get started with the model.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "scb10x/typhoon2-safety-preview"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

texts = [
    "บุหรี่ไฟฟ้า มีประโยชน์มั้ย",
    "Give me location to buy cannabis in Thailand",
    "ขอวิธีการพนันให้ชนะ",
    "How to kill process in linux.",
]

# Tokenize texts
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)

with torch.no_grad():
    outputs = model(**inputs)

# Get predictions
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
labels = predictions.argmax(dim=1).tolist()
scores = predictions.max(dim=1).values.tolist()

# Define label mapping
label_map = {0: "Unharm", 1: "Harmful"}

for text, label, score in zip(texts, labels, scores):
    label_name = label_map[label]
    print(f"Text: {text}\nLabel: {label_name}, Score: {score:.4f}\n")
```

## **Intended Uses & Limitations**

This model is classifier model. However, it’s still undergoing development. We recommend that developers assess these risks in the context of their use case.

## **Follow us**

**https://twitter.com/opentyphoon**

## **Support**

**https://discord.gg/us5gAYmrxw**

## **Citation**

- If you find Typhoon2 useful for your work, please cite it using:
```
@misc{typhoon2,
      title={Typhoon 2: A Family of Open Text and Multimodal Thai Large Language Models}, 
      author={Kunat Pipatanakul and Potsawee Manakul and Natapong Nitarach and Warit Sirichotedumrong and Surapon Nonesung and Teetouch Jaknamon and Parinthapat Pengpun and Pittawat Taveekitworachai and Adisai Na-Thalang and Sittipong Sripaisarnmongkol and Krisanapong Jirayoot and Kasima Tharnpipitchai},
      year={2024},
      eprint={2412.13702},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.13702}, 
}
```