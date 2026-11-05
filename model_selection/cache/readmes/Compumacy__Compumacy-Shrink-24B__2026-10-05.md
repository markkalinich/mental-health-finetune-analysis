---
license: apache-2.0
language:
- en
library_name: transformers
tags:
- compumacy
- psychology
- psychiatry
- clinical-assessment
- mental-health
- text-generation
datasets:
- Daemontatox/Psy-Data-books
model-index:
- name: Compumacy-Shrink-24B
  results: []
---

# Compumacy-Shrink-24B
## A Specialized Language Model for Clinical Psychology & Psychiatry

**Compumacy-Shrink-24B** is a highly specialized, 24-billion parameter language model, fine-tuned to assist mental health professionals in clinical assessment and treatment planning. This model is engineered to process complex clinical vignettes and generate structured, evidence-based responses that align with established diagnostic manuals and practice guidelines.

This model is intended as a state-of-the-art research tool to augment, not replace, the nuanced expertise of a licensed clinician. It systematically applies diagnostic criteria from the DSM-5-TR, references ICD-11 classifications, and cites peer-reviewed literature to support its recommendations.

- **Model Developed by:** [Compumacy](https://huggingface.co/Compumacy)
- **Fine-tuning and Dataset Curation:** [Daemontatox](https://huggingface.co/Daemontatox) (Ammar-Alnagar)
- **Dataset:** [Daemontatox/Psy-Data-books](https://huggingface.co/datasets/Daemontatox/Psy-Data-books)

## Model Description

**Compumacy-Shrink-24B** was fine-tuned on the `Daemontatox/Psy-Data-books` dataset, a comprehensive corpus of professional psychiatric literature, seminal textbooks, and clinical guidelines. This focused training enables the model to emulate the diagnostic reasoning process of a psychiatrist, adhering to a strict, structured format for clinical documentation.

The model's core competencies include:

1.  **Chief Complaint Analysis:** Objectively summarizing presenting symptoms.
2.  **Differential Diagnosis:** Systematically evaluating potential diagnoses against DSM-5-TR criteria.
3.  **Comprehensive Risk Assessment:** Identifying risks related to suicide, homicide, psychosis, and substance use.
4.  **Evidence-Based Recommendations:** Proposing treatment plans (pharmacotherapy, psychotherapy) based on guidelines from the APA, WFSBP, and NICE.
5.  **Monitoring and Referrals:** Outlining necessary follow-ups and indications for specialized care.

## How to Use

This model is designed for use with the `transformers` library. For efficient inference on consumer hardware, it is recommended to load the model in 4-bit or 8-bit precision.

### Installation

First, ensure you have the necessary libraries installed:
```bash
pip install transformers torch accelerate bitsandbytes
```
Inference Code

The model's performance is highly dependent on using the specific prompt structure it was trained on. Please use the Alpaca-style prompt format provided below.

``` python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Compumacy/Compumacy-Shrink-24B"

# For memory efficiency, load the model with quantization
# Use load_in_4bit=True for consumer GPUs
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_4bit=True,
    torch_dtype=torch.bfloat16, # Use float16 if bfloat16 is not supported
    device_map="auto",
)

# Define the structured prompt template
alpaca_prompt = """
### Instruction:
You are a licensed psychiatrist AI providing clinical assessments and recommendations.
Apply DSM-5-TR diagnostic criteria systematically, reference ICD-11 classifications, and base all recommendations on peer-reviewed psychiatric literature.
Follow evidence-based practice guidelines (APA, WFSBP, NICE).

Structure your response with:
1) Chief Complaint Analysis - summarize presenting symptoms objectively,
2) Differential Diagnosis - list potential diagnoses with supporting/contradicting criteria,
3) Risk Assessment - evaluate suicide risk, homicide risk, psychosis, substance use, medical emergencies,
4) Clinical Recommendations - evidence-based treatments with specific medications, dosages, therapy modalities,
5) Monitoring Requirements - labs, side effects, therapeutic response timelines,
6) Referral Indications - when specialized care or hospitalization needed.

Safety protocols: Immediately flag suicidal/homicidal ideation, identify psychotic symptoms requiring urgent intervention, recognize medical emergencies (delirium, catatonia, NMS), note substance intoxication/withdrawal risks. Cite specific studies (Author, Year, Journal), reference clinical guidelines with publication dates, include meta-analysis data when available, state confidence levels for recommendations. Specify when in-person evaluation mandatory, identify insufficient information for diagnosis, recommend immediate professional consultation when appropriate. Provide structured clinical documentation with no therapeutic relationship established.

### Input:
{}

### Response:
{}"""

# Your clinical input goes here
clinical_vignette = "A 42-year-old software developer presents with a chief complaint of 'constant worry' for the past year. She describes feeling on edge, difficulty controlling her anxious thoughts, muscle tension, and significant sleep disturbance. The worry spans multiple domains including work performance, finances, and her children's safety, and is causing her significant distress and impairment in her social life."

# Format the prompt
formatted_prompt = alpaca_prompt.format(clinical_vignette, "")
inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)

# Generate the response
# Using do_sample=True with temperature can produce more nuanced, less deterministic outputs
outputs = model.generate(
    **inputs, 
    max_new_tokens=2048, 
    temperature=0.7, 
    do_sample=True, 
    top_p=0.95, 
    top_k=50,
    eos_token_id=tokenizer.eos_token_id
)
response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print only the generated response part
print(response_text.split("### Response:")[1].strip())

```

### Ethical Considerations and Limitations

This model is a research preview and is NOT a substitute for a qualified medical or mental health professional.

No Clinical Relationship: The model does not and cannot establish a therapeutic relationship. Its outputs are for informational, educational, and research purposes only.

Verification Required: All outputs, including diagnoses, risk assessments, and treatment plans, must be independently verified by a licensed clinician before being considered for any real-world application.

Data Bias: The model's knowledge is limited to its training data (Daemontatox/Psy-Data-books). This data may contain inherent biases (e.g., cultural, gender, or theoretical orientation). The model may not be suitable for populations or clinical presentations not well-represented in the source material.

Risk of Hallucination: Like all LLMs, this model can hallucinate facts, studies, and clinical details. Citations should be cross-referenced with original sources.

Confidentiality: Do not input any Protected Health Information (PHI) or Personally Identifiable Information (PII) into this model. It is not designed for secure handling of sensitive patient data.

Emergency Situations: This model is not a crisis intervention tool. If you or someone you know is in immediate danger, contact emergency services or a crisis hotline.

### Disclaimer

The developers of this model are not responsible for any actions taken based on its output. Use of this model is at your own risk. It is intended solely for professionals and researchers in the field of mental health as an experimental tool to supplement, not replace, professional judgment and care. An in-person evaluation by a qualified professional is mandatory for any real-world clinical assessment.

### Citations

If you use this model or its dataset in your research, please cite the following:

```
@misc{alnagr_compumacy-shrink-24b_2024,
  author = {Alnagar, Ammar (Daemontatox)},
  title = {Compumacy-Shrink-24B: A Specialized Language Model for Clinical Psychiatry},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face Model Repository},
  howpublished = {\url{https://huggingface.co/Compumacy/Compumacy-Shrink-24B}}
}

@inproceedings{wolf-etal-2020-transformers,
    title = "Transformers: State-of-the-Art Natural Language Processing",
    author = "Thomas Wolf and Lysandre Debut and Victor Sanh and Julien Chaumond and Clement Delangue and Anthony Moi and Pierric Cistac and Tim Rault and Rémi Louf and Morgan Funtowicz and Joe Davison and Sam Shleifer and Patrick von Platen and Clara Ma and Yacine Jernite and Julien Plu and Canwen Xu and Teven Le Scao and Sylvain Gugger and Mariama Drame and Quentin Lhoest and Alexander M. Rush",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = oct,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-demos.6",
    pages = "38--45"
}

```
