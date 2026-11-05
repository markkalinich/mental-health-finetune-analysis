---
language:
- en
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- guardpoint
- valiant
- valiant-labs
- qwen
- qwen-3.5
- qwen-3.5-27b
- 27b
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
base_model: Qwen/Qwen3.5-27B
datasets:
- sequelbox/Superpotion-DeepSeek-V3.2-Speciale
license: apache-2.0
---


**[Support our open-source dataset and model releases!](https://huggingface.co/spaces/sequelbox/SupportOpenSource)**


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64f267a8a4f79a118e0fcc89/2jMQlAEy5KHCwYJNxxr27.jpeg)

Guardpoint: [gemma-4-12B](https://huggingface.co/ValiantLabs/gemma-4-12B-it-Guardpoint), [Qwen3-14B](https://huggingface.co/ValiantLabs/Qwen3-14B-Guardpoint), [gpt-oss-20b](https://huggingface.co/ValiantLabs/gpt-oss-20b-Guardpoint), [Qwen3.5-27B](https://huggingface.co/ValiantLabs/Qwen3.5-27B-Guardpoint), [Qwen3-32B](https://huggingface.co/ValiantLabs/Qwen3-32B-Guardpoint), [gpt-oss-120b](https://huggingface.co/ValiantLabs/gpt-oss-120b-Guardpoint)


Guardpoint is a medical reasoning specialist built on Qwen 3.5 27b.
- Finetuned on our high-difficulty [medical reasoning](https://huggingface.co/datasets/sequelbox/Superpotion-DeepSeek-V3.2-Speciale) data generated with [Deepseek V3.2 Speciale!](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Speciale)
- Structured medical reasoning: organized, informative responses for medical diagnosis, management, knowledge, and understanding!
- Cut token costs: organized, concise responses use less tokens for faster inference!
- Trained on a wide variety of medical disciplines, patient profiles, and question types!

## Prompting Guide
Guardpoint delivers structured medical responses using the [Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) prompt format.

Guardpoint is a reasoning finetune; **we recommend enable_thinking=True for all chats.**

Example inference script to get started:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "ValiantLabs/Qwen3.5-27B-Guardpoint"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "A 60-year-old undergoes a Total Knee Arthroplasty (TKA). Post-operatively, they complain of a clunking sensation and instability when descending stairs. On exam, they have excessive posterior translation of the tibia at 90 degrees of flexion. The TKA used a Cruciate Retaining (CR) implant. Diagnosis is PCL incompetence or rupture. Explain why a CR implant relies on a functional PCL for femoral rollback and how converting to a Posterior Stabilized (PS) implant resolves this biomechanical failure."
#prompt = "I have that tube in my chest for dialysis while my arm heals. The dressing came off in the shower and the tube got tugged a bit. It didn't come out, but now there's this red cuff thing showing that used to be inside the skin. It’s sticking out about an inch. Can I just push it back in and tape it?"
#prompt = "In the workup of a tumor of unknown primary, a biopsy shows a poorly differentiated carcinoma. The IHC profile is: CK7+, CK20+, CDX2+, TTF-1 negative, PAX8 negative. Based on this cytokeratin and transcription factor profile, where is the most likely primary site of the malignancy?"
#prompt = "I have bad arthritis in my lower back and hips. I saw a chiropractor who said my 'pelvis is twisted' and wants to do high-velocity adjustments. My rheumatologist said absolutely not because of my 'osteophytes'. Who is right? I just want to walk without stiffness."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

# parsing thinking content
try:
    # rindex finding 248069 (</think>)
    index = len(output_ids) - output_ids[::-1].index(248069)
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("thinking content:", thinking_content)
print("content:", content)
```


DISCLAIMER: Guardpoint is a medical reasoning finetune that is subject to the strengths and weaknesses of LLMs. A conversation with an LLM is not a substitute for a professional medical examination. Utilize Guardpoint responsibly.


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/63444f2687964b331809eb55/VCJ8Fmefd8cdVhXSSxJiD.jpeg)


Guardpoint is created by [Valiant Labs.](http://valiantlabs.ca/)

[Check out our HuggingFace page to see Shining Valiant, Esper, and all of our models!](https://huggingface.co/ValiantLabs)

We care about open source. For everyone to use.