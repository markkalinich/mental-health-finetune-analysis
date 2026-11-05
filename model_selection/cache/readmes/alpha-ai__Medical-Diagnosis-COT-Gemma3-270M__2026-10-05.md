---
base_model: google/gemma-3-270m-it
tags:
- medical
- healthcare
- chain-of-thought
- cot
- reasoning
- sft
- lora
- unsloth
- gemma
- gemma-3
- long-context
- transformers
license: apache-2.0
language:
- en
pipeline_tag: text-generation
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
---

<div align="center">
<img src="https://huggingface.co/alpha-ai/Medical-Diagnosis-COT-Gemma3-270M/resolve/main/Medical-Diagnosis-COT-Gemma3-270M.png"
     alt="Model card" 
     style="width: 500px; height: auto; object-position: center top;">
</div>

# Medical-Diagnosis-COT-Gemma3-270M

**Alpha AI (www.alphaai.biz)** fine-tuned Gemma-3 270M for **medical question answering with explicit chain-of-thought (CoT)**. The model emits reasoning inside `<think> ... </think>` followed by a final answer, making it well-suited for research on verifiable medical reasoning and for internal tooling where transparent intermediate steps are desired.

> ⚠️**Not for clinical use.** This model is a research system, not a medical device. Do not use it for diagnosis or treatment decisions.

---

## TL;DR

* **Base**: `google/gemma-3-270m-it` (Gemma 3, 270M params). Access requires accepting Google’s Gemma license on Hugging Face. 
* **Data**: `FreedomIntelligence/medical-o1-reasoning-SFT` (`en` split; columns: `Question`, `Complex_CoT`, `Response`).
* **Training**: SFT with LoRA via Unsloth; assistant-only loss; sequences templated in Gemma-3 chat format.
* **Objective**: Produce `<think>…</think>` (reasoning) + final answer.

---

## Intended Use & Limitations

**Intended use**

* Research on medical reasoning, CoT interpretability, prompt engineering, dataset curation.
* Internal assistants that require visible reasoning traces (to be reviewed by humans).

**Out of scope / limitations**

* Not a substitute for clinician judgment; may hallucinate facts.
* No guarantee of guideline adherence (e.g., UpToDate/NICE/ACOG).
* Biases from synthetic/derived training data will propagate.

Dataset license is **Apache-2.0**; the base model is covered by **Google's Gemma license**, review these before use.

---

## Model Details

* **Model family**: Gemma 3 (270M).
* **Context window**: Gemma 3 supports up to **128K tokens** (practical context used during SFT was lower due to GPU limits). 
* **Architecture**: decoder-only causal LM (Gemma family).
* **Fine-tuning**: Parameter-Efficient Fine-Tuning (LoRA) using Unsloth.

---

## Data

**Source**: `FreedomIntelligence/medical-o1-reasoning-SFT` + Human annotated and filtered medical diagnosis data

* English subset (`en`): \~19.7k rows with fields **`Question`**, **`Complex_CoT`**, **`Response`**. Total dataset ≈ 90,120 rows across splits/languages. 
* Built for advanced medical reasoning; constructed with GPT-4o and a verifier on **verifiable medical problems**. See dataset card and paper.
* Human annotated data ~ 10k rows with similar fields.

**Preprocessing**

* Each row rendered to a chat conversation under the **Gemma-3** template.
* Assistant output concatenates `<think>{Complex_CoT}</think>\n{Response}`.
* Training objective masked to **assistant** tokens only (instruction masking).

---

## Prompt & Output Format

**Training prompt style (system + user + assistant):**

```text
System:
Below is an instruction that describes a task,
paired with an input that provides further context.

Write a response that appropriately completes the request.

Before answering, think carefully about the question and create a step-by-step
chain of thoughts to ensure a logical and accurate response.

### Instruction:

You are a medical expert with advanced knowledge in clinical reasoning,
diagnostics, and treatment planning.

Please answer the following medical question.

User:
### Question:

{question}

### Response:

Assistant:
<think>
{complex_cot}
</think>
{final_answer}
```

**Generation tip (serve-time):**
If you don’t want to expose CoT to end-users, post-process generated text to **strip the `<think> ... </think>` block** and only show the final answer.

Python snippet to strip CoT:

```python
import re
def strip_think(text: str) -> str:
    return re.sub(r"<think>.*?</think>\s*", "", text, flags=re.S|re.I).strip()
```

---

## Quick Start

### Transformers (merged weights)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "alphaaico/Medical-Diagnosis-COT-Gemma3-270M"
tok  = AutoTokenizer.from_pretrained(repo)
mdl  = AutoModelForCausalLM.from_pretrained(repo, device_map="auto")

prompt = """### Question:

A 65-year-old with exertional dyspnea and orthopnea presents with bilateral
pitting edema and raised JVP. What initial pharmacologic therapy is indicated?

### Response:
"""

from transformers import TextStreamer
streamer = TextStreamer(tok, skip_prompt=True, skip_special_tokens=True)

inputs = tok.apply_chat_template(
    [{"role":"system","content":"You are a careful medical reasoner."},
     {"role":"user","content":prompt}],
    tokenize=True, add_generation_prompt=True, return_tensors="pt"
).to(mdl.device)

out = mdl.generate(**inputs, max_new_tokens=256, temperature=1.0, top_p=0.95, top_k=64, streamer=streamer)
```

### PEFT LoRA (if this repo hosts LoRA adapters)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

base = "google/gemma-3-270m-it"   # requires accepting Gemma license on Hugging Face
repo = "alphaaico/Medical-Diagnosis-COT-Gemma3-270M"

tok = AutoTokenizer.from_pretrained(base)
base_mdl = AutoModelForCausalLM.from_pretrained(base, device_map="auto")
mdl = PeftModel.from_pretrained(base_mdl, repo)  # merges LoRA at runtime
mdl.eval()
```

> If you see a 403/404 on the base model, make sure you’ve accepted Google’s Gemma license in your Hugging Face account. 

---

## Training Procedure

* **Trainer**: TRL `SFTTrainer` (supervised finetuning). 
* **Library**: Unsloth for fast loading + LoRA. Example reference repo for Gemma-3-270M is available on Hugging Face. 

**Key hyperparameters (demo run that produced loss ≈ 3.3):**

* Steps: `max_steps=500` , ideall go beyond 1500 for better results.
* Optimizer: `adamw_8bit`, `weight_decay=0.01`, `lr_scheduler_type=linear`
* LR: `5e-5` (for longer runs, `2e-5` is often more stable)
* Batch: `per_device_train_batch_size=8`, `gradient_accumulation_steps=1`
* Warmup: `warmup_steps=5`
* Seed: `3407`
* Loss masking: **assistant-only** (user/system tokens ignored)

> Note: For very long CoT sequences on small GPUs (e.g., T4 16 GB), consider `per_device_train_batch_size=1` + gradient accumulation and a larger `max_seq_length`. Gemma 3 supports up to **128K** context, but practical fine-tuning length depends on memory. For smaller queries, everything fits well for this to be used on edge devices.

---

## Evaluation

* **Training loss**: \~**3.3** at step 500 (demo run). Further decreased to \~**2.3** with parameter tuning.
* **Format compliance**: qualitatively verified to produce `<think>…</think>` followed by an answer.
* **No formal clinical benchmarks** reported yet. Contributions welcome via the Discussions tab.

---

## Safety, Ethics, and Responsible Use

* Do not rely on outputs for patient care. Validate with authoritative sources and licensed professionals.
* Be mindful of dataset artifacts and synthetic reasoning patterns.
* Consider stripping CoT in user-facing apps to avoid over-trust in intermediate narratives.

---

## License & Attribution

* **Base model**: Google **Gemma 3** — access controlled under Google’s Gemma license on Hugging Face. 
* **Dataset**: `FreedomIntelligence/medical-o1-reasoning-SFT` — **Apache-2.0**. 
* **This fine-tune**: Derivative work under the base model’s license terms. Review and comply with both licenses before distribution or commercial use.

**Please cite the dataset if you use this model:**

```
@misc{chen2024huatuogpto1medicalcomplexreasoning,
  title={HuatuoGPT-o1, Towards Medical Complex Reasoning with LLMs},
  author={Junying Chen and Zhenyang Cai and Ke Ji and Xidong Wang and Wanlong Liu and Rongsheng Wang and Jianye Hou and Benyou Wang},
  year={2024},
  eprint={2412.18925},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2412.18925}
}
```

---

## Acknowledgements

* **Google** for releasing Gemma 3.
* **FreedomIntelligence** for `medical-o1-reasoning-SFT`.
* **Unsloth** for streamlined fine-tuning utilities for Gemma 3.

---

## Contact

Questions, issues, or contributions: open a Discussion on this repo.
For enterprise collaboration with **Alpha AI**, reach out via the organization profile on Hugging Face or find us on www.alphaai.biz.

---

### Appendix: Inference without CoT (server-side filter)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import re

repo = "alphaaico/Medical-Diagnosis-COT-Gemma3-270M"
tok  = AutoTokenizer.from_pretrained(repo)
mdl  = AutoModelForCausalLM.from_pretrained(repo, device_map="auto")

def strip_think(txt): return re.sub(r"<think>.*?</think>\s*", "", txt, flags=re.S|re.I).strip()

def ask(question):
    user = f"### Question:\n\n{question}\n\n### Response:"
    msgs = [
      {"role":"system","content":"You are a medical expert. Think step-by-step, then answer succinctly."},
      {"role":"user","content":user},
    ]
    prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    out = mdl.generate(**tok(prompt, return_tensors="pt").to(mdl.device), max_new_tokens=512, temperature=1.0, top_p=0.95, top_k=64)
    text = tok.decode(out[0], skip_special_tokens=True)
    return strip_think(text)

print(ask("Elderly patient with new ankle swelling on thiazolidinedione—likely cause?"))
```
