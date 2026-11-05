---
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- guardpoint
- valiant
- valiant-labs
- gpt
- gpt-oss
- gpt-oss-120b
- openai
- 120b
- reasoning
- science
- science-reasoning
- medicine
- internal-medicine
- clinical-diagnosis
- medical-understanding
- medical-reasoning
- medical-diagnosis
- medical-management
- problem-solving
- anatomy
- angiology
- bariatric
- cardiovascular
- dental
- dermatology
- endocrinology
- ENT
- hematology
- immunology
- infectious-disease
- musculoskeletal
- neurology
- obstetrics
- ophtamology
- oncology
- orthopedics
- pathology
- psychiatry
- pulmonology
- radiology
- surgery
- triage
- urology
- analytical
- data
- data-interpretation
- expert
- rationality
- conversational
- chat
- instruct
base_model: openai/gpt-oss-120b
datasets:
- sequelbox/Superpotion-DeepSeek-V3.2-Speciale
license: apache-2.0
---


**[Support our open-source dataset and model releases!](https://huggingface.co/spaces/sequelbox/SupportOpenSource)**


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64f267a8a4f79a118e0fcc89/2jMQlAEy5KHCwYJNxxr27.jpeg)

Guardpoint: [gemma-4-12B](https://huggingface.co/ValiantLabs/gemma-4-12B-it-Guardpoint), [Qwen3-14B](https://huggingface.co/ValiantLabs/Qwen3-14B-Guardpoint), [gpt-oss-20b](https://huggingface.co/ValiantLabs/gpt-oss-20b-Guardpoint), [Qwen3.5-27B](https://huggingface.co/ValiantLabs/Qwen3.5-27B-Guardpoint), [Qwen3-32B](https://huggingface.co/ValiantLabs/Qwen3-32B-Guardpoint), [gpt-oss-120b](https://huggingface.co/ValiantLabs/gpt-oss-120b-Guardpoint)


Guardpoint is a medical reasoning specialist built on gpt-oss.
- Finetuned on our high-difficulty [medical reasoning](https://huggingface.co/datasets/sequelbox/Superpotion-DeepSeek-V3.2-Speciale) data generated with [Deepseek V3.2 Speciale!](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Speciale)
- Structured medical reasoning: organized, informative responses for medical diagnosis, management, knowledge, and understanding!
- Cut token costs: organized, concise responses use less tokens for faster inference!
- Trained on a wide variety of medical disciplines, patient profiles, and question types!

## Prompting Guide
Guardpoint uses the [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) prompt format.

Guardpoint is a reasoning finetune; **reasoning level high is generally recommended.**

Example inference script provided by [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) to get started:

```python
from transformers import pipeline
import torch

model_id = "ValiantLabs/gpt-oss-120b-Guardpoint"

pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)

prompt = "A 60-year-old undergoes a Total Knee Arthroplasty (TKA). Post-operatively, they complain of a clunking sensation and instability when descending stairs. On exam, they have excessive posterior translation of the tibia at 90 degrees of flexion. The TKA used a Cruciate Retaining (CR) implant. Diagnosis is PCL incompetence or rupture. Explain why a CR implant relies on a functional PCL for femoral rollback and how converting to a Posterior Stabilized (PS) implant resolves this biomechanical failure."
#prompt = "I have that tube in my chest for dialysis while my arm heals. The dressing came off in the shower and the tube got tugged a bit. It didn't come out, but now there's this red cuff thing showing that used to be inside the skin. It’s sticking out about an inch. Can I just push it back in and tape it?"
#prompt = "In the workup of a tumor of unknown primary, a biopsy shows a poorly differentiated carcinoma. The IHC profile is: CK7+, CK20+, CDX2+, TTF-1 negative, PAX8 negative. Based on this cytokeratin and transcription factor profile, where is the most likely primary site of the malignancy?"
#prompt = "I have bad arthritis in my lower back and hips. I saw a chiropractor who said my 'pelvis is twisted' and wants to do high-velocity adjustments. My rheumatologist said absolutely not because of my 'osteophytes'. Who is right? I just want to walk without stiffness."

messages = [
    {"role": "user", "content": prompt},
]

outputs = pipe(
    messages,
    max_new_tokens=8000,
)
print(outputs[0]["generated_text"][-1])
```


DISCLAIMER: Guardpoint is a medical reasoning finetune that is subject to the strengths and weaknesses of LLMs. A conversation with an LLM is not a substitute for a professional medical examination. Utilize Guardpoint responsibly.


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/63444f2687964b331809eb55/VCJ8Fmefd8cdVhXSSxJiD.jpeg)


Guardpoint is created by [Valiant Labs.](http://valiantlabs.ca/)

[Check out our HuggingFace page to see Shining Valiant, Esper, and all of our models!](https://huggingface.co/ValiantLabs)

We care about open source. For everyone to use.
