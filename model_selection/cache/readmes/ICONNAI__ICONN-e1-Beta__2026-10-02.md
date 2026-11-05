---
library_name: transformers
tags:
- emotional-ai
- ICONN
- chatbot
- base
co2_eq_emissions:
  emissions: 3.37
  source: CodeCarbon
  training_type: pretraining
  geographical_location: US-West
  hardware_used: 18 x B200
pipeline_tag: text-generation
license: apache-2.0
---

<div align="center" style="line-height: 1;">

![ICONN AI Logo](https://i.postimg.cc/gJwHqh1D/svgviewer-png-output.png)


  <a href="https://huggingface.co/collections/ICONNAI/iconn-1-6851e8a88ed4eb66b4fd0132" target="_blank" style="margin: 2px;">
    <img alt="ICONN 1 Models" src="https://img.shields.io/badge/📦_ICONN_1_Models-HuggingFace-1CBEEF?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;" />
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

</div>

# ICONN e1: The new era of Open-Source AI

**GPU poor? Less than 3x A100s? A e1 Lite model is coming with just 22B parameters alongside a model for consumer CPUs with 14B and 7B parameters.**


-   **Emotional Context Awareness**  
    ICONN e1 interprets emotional cues and adjusts tone, vocabulary, and response style—offering a more human-like, emotionally reactive experience.
    
-   **ICONN Emotional Core (IEC) (Notice: Not available on Huggingface)**  
    Powered by millions of small AI agents, IEC gives ICONN its emotional personality, with billions of simulated emotional states and detections.
    
-   **Reasoning**  
    ICONN e1 is one of the most powerful reasoning open-source models, and most closed-source models in or out of Huggingface.






# What is in the ICONN i1 MoE?





## ICONN i1 MoE and Experts

ICONN e1, being a MoE just like it's base model ICONN 1, has multiple expert models. Keywords are taken from the user's input to choose which expert generates the output.

| Expert Chosen       | User Input                                                                                                                                                                                                                                                                     |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ICONN-e1            | `'Hi!'`                                                                                                                                                                                                                                                                         |
| ICONN-e1-Pro        | `Solve for m: m² − (2 + ∑₍ⱼ₌₁₎² j)·m + (1 + ∑₍ⱼ₌₁₎³ j² − 14) = 0.`                                                                                                                                                                        |
| ICONN-e1-Science    | `If a stable isotope of Ununoctium (Uuo, now Og) could be synthesized in bulk, what would be its most likely physical state at STP and why, considering relativistic effects?`                                                                                                |
| ICONN-e1-Code       | `Create a zero-dependency quantum-safe VM in Zig that compiles a domain-specific language into a fully homomorphic encrypted IR, supports hot-reloading WebAssembly modules, parallel scheduling via lock-free fibers, and performs live introspection through a headless OpenGL debug overlay.` |

**ICONN-e1:**  
ICONN's general-purpose reasoning model, designed for everyday tasks, logic, and conversation.

**ICONN-e1-Pro:**  
ICONN's advanced reasoning model, optimized for complex problem-solving in math, logic, and professional domains.

**ICONN-e1-Science:**  
ICONN's scientific expert model, trained on advanced science datasets to enhance precision in physics, chemistry, biology, and technical reasoning.

**ICONN-e1-Code:**  
ICONN's coding specialist, trained for programming, compiler theory, software architecture, and technical code generation across multiple languages.


# Usage
**First, make sure you have at least 4x Nvidia A100 or a single B100, and 120GB RAM and 120-192GB VRAM. Don't have this? Use our Lite model, coming soon.

> Run the code below to run ICONN i1:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

def run_iconn_chatbot(model_name="ICONNAI/ICONN-e1"):

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    device = 0 if torch.cuda.is_available() else -1
    
    chat_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=device,
        max_length=1624,
        do_sample=True,
        top_p=0.9,
        temperature=0.4,
        pad_token_id=tokenizer.eos_token_id
    )
    
    print(f"ICONN chatbot running with model: {model_name}. Type 'exit' to quit.")
    conversation_history = ""
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        conversation_history += f"User: {user_input}\nBot:"
        
        response = chat_pipeline(conversation_history, max_length=len(tokenizer.encode(conversation_history)) + 100)[0]['generated_text']
        
        bot_reply = response[len(conversation_history):].strip().split("\n")[0]
        
        print(f"Bot: {bot_reply}")
        
        conversation_history += f" {bot_reply}\n"

if __name__ == "__main__":
    run_iconn_chatbot()
```

## Cite Us

**If you use ICONN 1, please cite us as follows:**

```DoI

@misc{iconnai_2025,
	author       = { ICONNAI },
	title        = { ICONN-e1-Beta (Revision ca41146) },
	year         = 2025,
	url          = { https://huggingface.co/ICONNAI/ICONN-e1-Beta },
	doi          = { 10.57967/hf/5861 },
	publisher    = { Hugging Face }
}

```