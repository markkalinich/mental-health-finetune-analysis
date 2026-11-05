---
library_name: transformers
tags:
- emotional-ai
- ICONN
- chatbot
- base
co2_eq_emissions:
  emissions: 0.34
  source: CodeCarbon
  training_type: pretraining
  geographical_location: US-West
  hardware_used: 9 x B200
pipeline_tag: text-generation
license: apache-2.0
---
<div align="center" style="line-height: 1;">

![ICONN AI Logo](https://i.postimg.cc/gJwHqh1D/svgviewer-png-output.png)


  <a href="https://huggingface.co/collections/ICONNAI/iconn-1-6851e8a88ed4eb66b4fd0132" target="_blank" style="margin: 2px;">
    <img alt="ICONN 1 Models" src="https://img.shields.io/badge/📦_ICONN_1_Models-HuggingFace-1CBEEF?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;" />
  </a>

  <a href="https://huggingface.co/spaces/ICONNAI/ICONN-Mini-Chat" target="_blank" style="margin: 2px;">
    <img alt="ICONN 1 Chat" src="https://img.shields.io/badge/💬_ICONN_1_Chat-Online-65C7F9?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;" />
  </a>

  <a href="https://huggingface.co/ICONNAI" target="_blank" style="margin: 2px;">
    <img alt="ICONN on Hugging Face" src="https://img.shields.io/badge/🤗_ICONN_on_HF-ICONNAI-A4BCF0?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;" />
  </a>

  <a href="https://opensource.org/license/apache-2-0" target="_blank" style="margin: 2px;">
    <img alt="License Apache 2.0" src="https://img.shields.io/badge/⚖️_License-Apache_2.0-5C63DA?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;" />
  </a>

  <a href="https://github.com/organizations/ICONN-AI/" target="_blank" style="margin: 2px;">
    <img alt="ICONN on GitHub" src="https://img.shields.io/badge/🐙_ICONN_on_GitHub-ICONN--AI-8C8CFF?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;" />
  </a>

  <a href="https://huggingface.co/ICONNAI" target="_blank" style="margin: 2px;">
    <img alt="Follow ICONNAI" src="https://img.shields.io/badge/⭐_Follow_ICONNAI-HuggingFace-A4BCF0?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;" />
  </a>

  <a href="https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/2932" target="_blank" style="margin: 2px;">
    <img alt="React to Vote" src="https://img.shields.io/badge/🗳️_Vote_for_us_as_Inference_Provider-React_👍-1CBEEF?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;" />
  </a>
  
</div>

## ICONN 1
Introducing **ICONN 1 Mini Beta**, a cutting-edge open-source AI model with just **7 billion parameters** — designed for natural, human-like language understanding and generation. Despite its compact size, it delivers powerful performance through efficient architecture and careful tuning. ICONN 1 Mini Beta represents the next step in accessible, conversational AI.

Developed entirely from scratch, ICONN-1-Mini-Beta is based on a new **ICONN** framework and comprises **7 billion parameters**.  

ICONN-1 is released in three distinct forms to serve different application needs:
-   **ICONN-1-Mini-Beta**(This model) is a small 7B model trained for a lightweight alternative to ICONN 1.
-   **ICONN-1** is  optimized for natural, emotionally resonant, and conversational interactions.
-   **ICONN-e1** is a specialized variant of the model fine-tuned for advanced reasoning, critical analysis, and complex problem-solving.

Together, these models represent a major leap forward in the evolution of AI systems—demonstrating not only deep reasoning but also a commitment to openness, accessibility, and human-aligned intelligence.



## Usage

To run **ICONN 1 Mini Beta**, you need:

- **Any hardware - CPU or GPU; Just make sure you have about 15GB storage space!**

> Run the code below to run ICONN 1 Mini Beta:

```python
import os

import torch

from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer

from threading import Thread

  

model_id = "ICONNAI/ICONN-1-Mini-Beta"

  

try:

model = AutoModelForCausalLM.from_pretrained(

model_id, torch_dtype=torch.float16, device_map="auto", trust_remote_code=True

)

tokenizer = AutoTokenizer.from_pretrained(model_id)

except Exception as e:

exit(f"Exiting due to model loading error: {e}")

  

def generate_response(

message:  str,

max_new_tokens:  int = 2048,

temperature:  float = 0.4,

top_p:  float = 0.9,

top_k:  int = 50,

repetition_penalty:  float = 1.2,

) -> str:

conversation = [{"role":  "user",  "content": message}]

  

try:

input_ids = tokenizer.apply_chat_template(

conversation, return_tensors="pt", enable_thinking=True

)

except Exception as e:

return  f"Error applying chat template: {e}"

  

input_ids = input_ids.to(model.device)

  

streamer = TextIteratorStreamer(tokenizer, timeout=20.0, skip_prompt=True, skip_special_tokens=True)

  

adjusted_top_k = int(max(1, top_k))

  

generate_kwargs = dict(

{"input_ids": input_ids},

streamer=streamer,

max_new_tokens=max_new_tokens,

do_sample=True,

top_p=top_p,

top_k=adjusted_top_k,

temperature=temperature,

num_beams=1,

repetition_penalty=repetition_penalty,

)

  

try:

t = Thread(target=model.generate, kwargs=generate_kwargs)

t.start()

except Exception as e:

return  f"Error starting generation thread: {e}"

  

outputs = []

for text in streamer:

outputs.append(text)

return  "".join(outputs)

  

if  __name__ == "__main__":

question = "Can you explain briefly to me what is the Python programming language?"

print(f"User Question: {question}")

  

response = generate_response(question)

print(f"Bot Response: {response}")
```

## Cite Us

**If you use ICONN 1, please cite us as follows:**

```DoI

@misc{iconnai_2025,
	author       = { ICONNAI },
	title        = { ICONN-1-Mini-Beta (Revision e29b435) },
	year         = 2025,
	url          = { https://huggingface.co/ICONNAI/ICONN-1-Mini-Beta },
	doi          = { 10.57967/hf/5860 },
	publisher    = { Hugging Face }
}

```