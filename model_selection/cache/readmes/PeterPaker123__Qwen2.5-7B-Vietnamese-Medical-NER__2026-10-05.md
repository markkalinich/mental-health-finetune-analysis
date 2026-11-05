---
library_name: transformers
tags: [ner, medical, vietnamese, qwen, sft, text-extraction]
---

# Model Card for PeterPaker123/Qwen2.5-7B-Vietnamese-Medical-NER

<!-- Provide a quick summary of what the model is/does. -->
This model is a generative Large Language Model (based on the Qwen2.5-7B architecture) strictly fine-tuned for **Vietnamese Medical Named Entity Recognition (NER)**. It acts as a dynamic, prompt-driven extraction agent that can accurately identify and extract *any* medical, clinical, or demographic entities from Vietnamese texts based on the user's instructions, outputting the results in a highly structured JSON format.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->
This model transitions away from traditional token-classification BERT models by utilizing an LLM as an intelligent extraction agent. It reads Vietnamese medical texts (such as clinical notes, user questions, or news) and outputs structured JSON lists. 

The model was trained via **Supervised Fine-Tuning (SFT)** on a vast array of entity types across multiple datasets. By injecting the target entity schemas directly into the system prompts during SFT, the model learned the generalized skill of **dynamic extraction**—it extracts exactly what the prompt asks for, returning a perfectly formatted JSON schema rather than memorizing a hardcoded list of labels.

- **Developed by:** PeterPaker123
- **Model type:** Causal Language Model (Generative NER)
- **Language(s) (NLP):** Vietnamese (`vi`)
- **License:** Apache 2.0 (Derived from Qwen base models)
- **Finetuned from model:** `Qwen/Qwen2.5-7B-Instruct`

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
Unlike traditional NER models constrained to a fixed set of predefined classes, this model supports **dynamic, prompt-defined entity extraction**. It acts as an intelligent agent that extracts *any* entity type specified in the system prompt. 

Commonly targeted categories include (but are not limited to):
* **`SYMPTOM_AND_DISEASE`**: Symptoms, signs of illness, diseases, or medical conditions.
* **`MEDICAL_PROCEDURE`**: Medical procedures, surgeries, therapies, or diagnostic methods.
* **`DRUG`**: Names of medicines, drugs, vitamins, or supplements.
* **`BODY_PART / ANATOMY`**: Anatomical locations, organs, or body structures.
* **`DOSAGE & MEASUREMENT`**: Medical quantities, medication dosages, or frequencies.
* **`DEMOGRAPHICS`**: Patient-specific identifiers (e.g., Age, Gender, Occupation, Location).

**How it works:** You simply define the desired categories and their descriptions in the `system` prompt, and the model will strictly adhere to extracting only those requested types into the required JSON schema.

### Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
This model can be integrated into downstream healthcare applications such as:
- Medical chatbot prompt enrichment (RAG pipelines).
- Automated structuring of telehealth transcripts and clinical notes.
- Clinical knowledge graph construction.
- Epidemiological data mining and surveillance.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
- **Medical Diagnosis or Triage:** This model is strictly an extraction tool. It does not diagnose, prescribe, or provide medical advice.
- **General Conversation:** The model has been aggressively aligned to output JSON lists. It will perform poorly at standard conversational AI tasks.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
- **Clinical Disclaimer:** This model is an AI research tool and **must not** be used for automated medical diagnosis, treatment planning, or life-or-death triage without human oversight.
- **Language Limitation:** The model is exclusively trained for the Vietnamese language. 
- **Hallucination Residuals:** While fine-tuning significantly improves adherence to the text, Generative LLMs may occasionally alter the spelling of extracted text or hallucinate entities, especially if the input text is highly ambiguous or noisy.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. Extracted entities in a clinical setting must be validated by a human medical professional or a deterministic cross-checking system.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
import json
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "PeterPaker123/Qwen2.5-7B-Vietnamese-Medical-NER"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto")

prompt = [
  {
    "role": "system",
    "content": "You are a medical expert. Your task is to identify and extract medical entities from the given text.\nThe entity types to extract are:\n- SYMPTOM_AND_DISEASE: Symptoms, signs of illness, diseases, or medical conditions.\n- MEDICAL_PROCEDURE: Medical procedures, surgeries, therapies, or diagnostic methods.\n- DRUG: Names of medicines, drugs, vitamins, or supplements.\n- DEMOGRAPHICS: Age, gender, or patient ID.\n\nReturn the result as a JSON list containing dictionaries with \"entity\" and \"type\" keys. If no relevant entities are found, return an empty list []"
  },
  {
    "role": "user",
    "content": "Text: Bệnh nhân nam 45 tuổi nhập viện vì đau dữ dội vùng bụng dưới, được chỉ định siêu âm ổ bụng."
  }
]

inputs = tokenizer.apply_chat_template(prompt, return_tensors="pt", add_generation_prompt=True).to(model.device)
outputs = model.generate(inputs, max_new_tokens=256, temperature=0.0)

response = tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)
print(response)
# Expected Output: 
# [
#   {"entity": "nam", "type": "DEMOGRAPHICS"},
#   {"entity": "45 tuổi", "type": "DEMOGRAPHICS"},
#   {"entity": "đau dữ dội vùng bụng dưới", "type": "SYMPTOM_AND_DISEASE"}, 
#   {"entity": "siêu âm ổ bụng", "type": "MEDICAL_PROCEDURE"}
# ]
```

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->
This model was trained on a consolidated corpus derived from four premier Vietnamese medical datasets. 

Unlike models mapped to a fixed set of classes, **this model was Supervised Fine-Tuned (SFT) on ALL available entity types** across these datasets. This extensive exposure taught the model how to dynamically parse the system prompt and extract the requested target types accurately.

| Dataset Name | Domain / Source | Total Samples | Entities Used During SFT |
|---|---|---|---|
| **VietBioNER** | Tuberculosis (TB) clinical treatment | ~1,700 | Symptom & Disease, Diagnostic Procedure, Location, Date |
| **PhoNER_COVID19** | COVID-19 pandemic surveillance | ~10,000 | Symptom & Disease, Patient ID, Age, Gender, Location, Org |
| **ViMQ** | Healthcare dialogue systems | ~10,000 | Symptom, Disease, Drug, Procedure, Body Structure |
| **ViMedNER** | General Medical NER | ~10,000 | Symptom, Disease, Drug, Body Part, Procedure, Time |

*Data Split:* Standard Train/Validation splits were maintained to monitor formatting accuracy and exact match (F1) scores during SFT.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing 

- Prompts were formatted into a strict ChatML format using text-only templates.
- **Dynamic Prompt Injection:** During SFT, training samples were dynamically generated to include varying subsets of target entities in the system prompt. This taught the model to read instructions carefully and only extract what was requested, rather than hallucinating categories from memory.

#### Training Hyperparameters

- **Training regime:** `bf16` mixed precision
- **Supervised Fine-Tuning (SFT):** Full parameter fine-tuning, Max Sequence Length 4096, Batch Size 2, Gradient Accumulation 8, Learning Rate 2e-5, Cosine Scheduler. Full AdamW optimizer. 

## Technical Specifications

### Model Architecture and Objective

Qwen2.5-7B Architecture. Causal Language Modeling objective fine-tuned to act as an entity extraction classifier capable of dynamic zero-shot categorization.

#### Hardware

NVIDIA RTX PRO 6000 Blackwell

#### Software

- `transformers`
- `trl` (SFTTrainer)
- `torch` (with `sdpa` attention)

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

Please cite the dataset authors who made this consolidated training possible:

```bibtex
@inproceedings{vietbioner,
    title = "{A Named Entity Recognition Corpus for Vietnamese Biomedical Texts to Support Tuberculosis Treatment}",
    author = "Phan, Uyen and Nguyen, Phuong and Nguyen, Nhung",
    booktitle = "Proceedings of the 13th Language Resources and Evaluation Conference",
    year = "2022",
    publisher = "European Language Resources Association"
}

@inproceedings{PhoNER_COVID19,
    title = {{COVID-19 Named Entity Recognition for Vietnamese}},
    author = {Thinh Hung Truong and Mai Hoang Dao and Dat Quoc Nguyen},
    booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
    year = {2021}
}

@article{vimq2023,
  title={ViMQ: A Vietnamese Medical Question Dataset for Healthcare Dialogue System Development},
  author={Vu, Hieu M. and Phan, Long and Nguyen, Nhung and others},
  year={2023}
}

@article{10.4108/eetinis.v11i3.5221,
    author={Pham Van Duong and Tien-Dat Trinh and Minh-Tien Nguyen and Huy-The Vu and Minh Chuan Pham and Tran Manh Tuan and Le Hoang Son},
    title={ViMedNER: A Medical Named Entity Recognition Dataset for Vietnamese},
    journal={EAI Endorsed Transactions on Industrial Networks and Intelligent Systems},
    volume={11},
    number={4},
    publisher={EAI},
    year={2024},
    doi={10.4108/eetinis.v11i3.5221}
}
```

## Glossary

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

- **NER:** Named Entity Recognition
- **SFT:** Supervised Fine-Tuning
- **Dynamic Extraction:** The ability of an LLM to identify unseen or varying categorizations purely based on the instructions provided in the system prompt.