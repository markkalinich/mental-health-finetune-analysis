---
base_model: google/medgemma-4b-it
library_name: transformers
model_name: clinical_sdtm
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# MODEL CARD

This model is a fine-tuned version of [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it).
It has been trained using [TRL](https://github.com/huggingface/trl).

The [ClinicalIntelligence/saama_gemma](https://huggingface.co/ClinicalIntelligence/saama_gemma) is a fine-tuned MedGemma model designed to transform unstructured clinical narratives—such as discharge notes—into structured, SDTM-aligned datasets (e.g., Adverse Events, Medical History, Procedures). Trained on an SME-curated dataset derived from MIMIC-III, the model treats clinical data extraction as a complex reasoning task, explicitly evaluating assertion, temporality, and causality to generate accurate, traceable JSON outputs. By learning regulatory semantics directly, it significantly outperforms base models in domain grounding and schema consistency. Users should note current limitations regarding context window constraints for lengthy notes, rare abbreviation handling, and the resolution of multi-domain entities.



## INSTALLATION
```
pip install -U transformers
```

## QUICK START
**NOTE** - Adjust the **max_new_tokens** parameter as needed, it is set to **16000** to generate complete think tokens and extracted entities.

```python
import re

from transformers import pipeline

prefix = """Extract SDTM domain entities from: """

unstructured_text = """
This previously healthy gentleman presented three days after swallowing a fishbone, reporting subsequent odynophagia, right-sided neck pain, and referred otalgia to the right ear. 
Extensive diagnostic imaging, including a soft-tissue neck X-ray, barium swallow, and CT of the neck, showed no evidence of a radiopaque foreign body or esophageal perforation. Furthermore, an ORL endoscopy and a follow-up EGD confirmed the absence of any foreign objects, though the EGD did identify a soft palate ulcer and an antral nodule.
Following these procedures, the patient was able to tolerate soft foods without further discomfort. It is highly probable that the fishbone caused localized mucosal micro-trauma before being naturally dislodged and passed through the gastrointestinal tract. 
The patient was discharged with a prescription for viscous lidocaine and ibuprofen 400mg as needed for pain, with a documented maximum daily limit of 1200mg."""

generator = pipeline(
    "text-generation", model="ClinicalIntelligence/saama_gemma", device="cuda"
)
output = generator(
    [{"role": "user", "content": prefix + unstructured_text}],
    return_full_text=False,
    max_new_tokens=16000,
)[0]
llm_output = output["generated_text"]


def extract_entities(text):
    """
    Extracts entities, domains, and justifications from the given text
    and returns them as a list of dictionaries.
    """
    # The regex pattern looks for:
    # 1. Content inside <think> and </think> tags
    # 2. Domain prefixed with ~ (ignoring whitespace/special characters like non-breaking spaces)
    # 3. Extracted entity prefixed with ~~ (up to the next <think> tag or end of string)
    pattern = r"(?s)<think>\s*(.*?)\s*</think>\s*~([A-Z0-9]+)\s*~~(.*?)(?=<think>|$)"

    # Find all matches in the text
    matches = re.findall(pattern, text)

    extracted_data = []

    for justification, domain, entity in matches:
        extracted_data.append(
            {
                "domain": domain.strip(),
                "extracted_entity": entity.strip(),
                "justification": justification.strip(),
            }
        )

    return extracted_data


extracted_entities_list = extract_entities(llm_output)

for extracted_entity in extracted_entities_list:
    print(extracted_entity)
```

## SAMPLE OUTPUT
```python
{'domain': 'AE', 'extracted_entity': 'swallowing a fishbone', 'justification': "This is an adverse event (AE) because it is an untoward medical occurrence that happened to the patient. The timing 'three days after' indicates it is a current event that precipitated the visit, not a pre-existing condition from the patient's medical history (MH)."}
{'domain': 'AE', 'extracted_entity': 'odynophagia', 'justification': 'This is an adverse event (AE) because it is a new symptom reported by the patient, occurring after the inciting event (swallowing the fishbone). It is an untoward medical occurrence and is temporally associated with the current visit, not a historical condition (MH).'}
{'domain': 'AE', 'extracted_entity': 'neck pain', 'justification': 'This is an adverse event (AE) because it is a new symptom reported by the patient, occurring after the inciting event. It is an untoward medical occurrence and is temporally associated with the current visit, not a historical condition (MH).'}
{'domain': 'AE', 'extracted_entity': 'otalgia', 'justification': 'This is an adverse event (AE) because it is a new symptom reported by the patient, occurring after the inciting event. It is an untoward medical occurrence and is temporally associated with the current visit, not a historical condition (MH).'}
{'domain': 'PR', 'extracted_entity': 'soft-tissue neck X-ray', 'justification': 'This is a procedure (PR) because it represents a diagnostic intervention performed on the patient to investigate their symptoms. It is an action taken, not an observation of a spontaneous event (AE) or a pre-existing condition (MH).'}
{'domain': 'PR', 'extracted_entity': 'barium swallow', 'justification': 'This is a procedure (PR) because it is a diagnostic intervention performed on the patient. It is an action taken, not an observation of a spontaneous event (AE) or a pre-existing condition (MH).'}
{'domain': 'PR', 'extracted_entity': 'CT of the neck', 'justification': 'This is a procedure (PR) because it is a diagnostic intervention performed on the patient. It is an action taken, not an observation of a spontaneous event (AE) or a pre-existing condition (MH).'}
{'domain': 'PR', 'extracted_entity': 'ORL endoscopy', 'justification': 'This is a procedure (PR) because it is a diagnostic intervention performed on the patient to evaluate the oropharynx. It is an action taken, not an observation of a spontaneous event (AE) or a pre-existing condition (MH).'}
{'domain': 'PR', 'extracted_entity': 'EGD', 'justification': 'This is a procedure (PR) because it is a diagnostic intervention (Esophagogastroduodenoscopy) performed on the patient. It is an action taken, not an observation of a spontaneous event (AE) or a pre-existing condition (MH).'}
{'domain': 'AE', 'extracted_entity': 'soft palate ulcer', 'justification': 'This is an adverse event (AE) because it is an untoward medical occurrence identified during the current visit. The timing is current, not historical (MH). It is not a planned observation like a physical exam (PE) or vital sign (VS), but a newly identified pathological condition.'}
{'domain': 'AE', 'extracted_entity': 'antral nodule', 'justification': 'This is an adverse event (AE) because it is an untoward medical occurrence identified during the current visit. The timing is current, not historical (MH). It is not a planned observation like a physical exam (PE) or vital sign (VS), but a newly identified pathological condition.'}
{'domain': 'AE', 'extracted_entity': 'localized mucosal micro-trauma', 'justification': "This is an adverse event (AE) because it is the pathological event diagnosed as the cause of the patient's symptoms. It is an untoward medical occurrence that happened to the patient, not a historical condition (MH)."}
{'domain': 'CM', 'extracted_entity': 'viscous lidocaine', 'justification': 'This is a concomitant medication (CM) because it is a therapeutic agent prescribed to the patient for a current condition (pain). It is not a historical medication (MH) and is not a procedural agent (AG).'}
{'domain': 'CM', 'extracted_entity': 'ibuprofen', 'justification': 'This is a concomitant medication (CM) because it is a therapeutic agent prescribed to the patient for a current condition (pain). It is not a historical medication (MH) and is not a procedural agent (AG).'}
{'domain': 'AE', 'extracted_entity': 'pain', 'justification': 'This is an adverse event (AE) because it is a symptom for which the patient is receiving treatment. The timing is current, not historical (MH).'}
{'domain': 'DS', 'extracted_entity': 'discharged', 'justification': "This entity describes the patient's disposition (DS) at the end of the encounter. It indicates the outcome of the visit and the patient's status relative to the clinical setting."}
{'domain': 'DM', 'extracted_entity': 'gentleman', 'justification': 'This entity describes the sex of the patient, which is a fundamental demographic characteristic. It is not a medical event, finding, or intervention, thus it belongs in the Demographics (DM) domain.'}
{'domain': 'DM', 'extracted_entity': 'previously healthy', 'justification': "This entity describes the patient's age, which is a fundamental demographic characteristic. It is not a medical event, finding, or intervention, thus it belongs in the Demographics (DM) domain."}
{'domain': 'DS', 'extracted_entity': 'discharged', 'justification': "This entity describes the patient's disposition (DS) at the end of the encounter. It indicates the outcome of the visit and the patient's status relative to the clinical setting."}
```

## TRAINING PROCEDURE
* Training Data Size: 6,500 samples (grouped by uid and formatted into complete user/assistant conversational threads)
* Number of Epochs: 5 (The model processed the entire dataset 5 times, totaling approximately 4,065 optimization steps)
* Effective Batch Size: 8 (Per-device batch size of 1 combined with 8 gradient accumulation steps)
* LoRA Rank ($r$ / Adapter Size): 16 (Provides a balance between capturing complex, domain-specific logic and maintaining a lightweight adapter)
* LoRA Alpha: 32LoRA Scaling Factor: 2.0 (Calculated as Alpha / Rank, providing a strong fine-tuning signal to enforce strict extraction formatting)
* Targeted Layers: All linear layers (target_modules="all-linear")
* Adapters were applied to attention modules as well as MLP blocks to maximize instructional compliance and mimic full fine-tuning
* Maximum Sequence Length: 12,000 tokens (Sufficient to handle extensive hospital course notes)
* Learning Rate: 2e-4Precision: bfloat16 with Flash Attention 2 and gradient checkpointing enabled for memory efficiency.

### FRAMEWORK VERSIONS

- TRL: 0.28.0
- Transformers: 5.2.0
- Pytorch: 2.10.0
- Datasets: 4.5.0
- Tokenizers: 0.22.2