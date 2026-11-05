---
library_name: transformers
tags:
- unsloth
---
# Qwen3 Highlights

Qwen3 is the latest generation of large language models in Qwen series, offering a comprehensive suite of dense and mixture-of-experts (MoE) models. Built upon extensive training, Qwen3 delivers groundbreaking advancements in reasoning, instruction-following, agent capabilities, and multilingual support, with the following key features:

- **Uniquely support of seamless switching between thinking mode** (for complex logical reasoning, math, and coding) and **non-thinking mode** (for efficient, general-purpose dialogue) **within single model**, ensuring optimal performance across various scenarios.
- **Significantly enhancement in its reasoning capabilities**, surpassing previous QwQ (in thinking mode) and Qwen2.5 instruct models (in non-thinking mode) on mathematics, code generation, and commonsense logical reasoning.
- **Superior human preference alignment**, excelling in creative writing, role-playing, multi-turn dialogues, and instruction following, to deliver a more natural, engaging, and immersive conversational experience.
- **Expertise in agent capabilities**, enabling precise integration with external tools in both thinking and unthinking modes and achieving leading performance among open-source models in complex agent-based tasks.
- **Support of 100+ languages and dialects** with strong capabilities for **multilingual instruction following** and **translation**.

## Model Overview

**Qwen3-32B** has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Number of Parameters: 32.8B
- Number of Paramaters (Non-Embedding): 31.2B
- Number of Layers: 64
- Number of Attention Heads (GQA): 64 for Q and 8 for KV
- Context Length: 32,768 natively and [131,072 tokens with YaRN](#processing-long-texts). 

For more details, including benchmark evaluation, hardware requirements, and inference performance, please refer to our [blog](https://qwenlm.github.io/blog/qwen3/), [GitHub](https://github.com/QwenLM/Qwen3), and [Documentation](https://qwen.readthedocs.io/en/latest/).

## Quickstart

The code of Qwen3 has been in the latest Hugging Face `transformers` and we advise you to use the latest version of `transformers`.

With `transformers<4.51.0`, you will encounter the following error:
```
KeyError: 'qwen3'
```

The following contains a code snippet illustrating how to use the model generate content based on given inputs. 
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model_name = "Konthee/Qwen3-mt-medical-ch-th"
# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
# prepare the model input
system_prompt ="""\
You are a professional Chinese-Thai medical translator.

**Input**
You will be given two items:
    Context — a short Chinese patient-doctor conversation.
    Source — one specific Chinese sentence from that conversation to translate.

**Task**
    Translate the Source sentence into Thai.

**Requirements**
    1. Preserve the sentence’s medical meaning, tone, and intent.
    2. Make the Thai sound natural and suitable for spoken dialogue between doctor and patient.
    3.Ensure the translation is accurate, clear, and easy to understand.

**Output**
    Provide only the final Thai translation. Do not include explanations, reasoning, or any additional text.
"""

user_prompt = """\
context : {}

source : {} 
"""
messages = [
    {"role": "user", "content": system_prompt}
    {"role": "user", "content": user_prompt.format(context,source)},  
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
    # rindex finding 151668 (</think>)
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0
thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")
print("thinking content:", thinking_content)
print("content:", content)
```

### Evaluation Results
Results retrieved from the **AI Benchmark 2025 MT Leaderboard** https://benchmark.ai.in.th/score/leaderboard/2025-mt

| Split   | BLEU score|
|---------|---------|
| public  | 48.78 | 
| private | 47.95 |

_Data sourced directly from the leaderboard metrics_ 

This model corresponds to team **220_อย่าคับ เจนมันเวิ่นเว้อป่าวว**, which secured **1st place** on both the public leaderboards in the **2025-QA** competition on round 1
## APA  
> AI Thailand Benchmark Programs. (2025). _2025-MT: Machine Translation Task_. Retrieved June 23, 2025, from https://benchmark.ai.in.th/task/detail/2025-mt  


### Authors
* Konthee Boonmeeprakob (konthee1995@gmail.com)
* Pitikorn Khlaisamniang (pitikorn32@gmail.com)
