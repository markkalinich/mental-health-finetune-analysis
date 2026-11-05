---
base_model: arcee-ai/AFM-4.5B
library_name: transformers
pipeline_tag: text-generation
language:
- en
tags:
- medical
- instruction-tuned
- dpo
- grpo
- cot
- mergekit
- arcee-fusion
- openmed
license: apache-2.0
---

# AFM-4.5B-OpenMed

**Lightweight medical finetune on top of Arcee’s AFM-4.5B** for education and research use. Trained with a simple 3-stage recipe (SFT → DPO → GRPO-CoT) and finalized via **Arcee Fusion** weight merging (MergeKit).

More information about our **methodology** will be available in a forthcoming **blog post**.

All experiments were performed on **AMD MI300x** GPUs, with computing credits generously provided by [Hot AISLE](https://hotaisle.xyz/).

> ⚠️ **Medical safety**  
> This model is **not** a clinician. It can hallucinate and should **not** be used for diagnosis or treatment. Always involve qualified medical professionals.

---

## TL;DR

- **Base:** [`arcee-ai/AFM-4.5B`](https://huggingface.co/arcee-ai/AFM-4.5B) – Arcee’s 4.5B instruction model intended for cloud-to-edge deployment.
- **Training (high level):**
  1) **SFT** proprietary synthetic medical datasets + **tool-calling (search) traces**  
  2) **DPO** using **MedMCQA-derived** preferences (multiple-choice signal)
  3) **GRPO** for **chain-of-thought enrichment**, using **MedReason** verifiable rewards; short rationales encouraged, final answer checked.
  4) **Model merge:** **Arcee Fusion** (MergeKit) for selective, importance-aware parameter fusion.
- **Eval (EleutherAI harness; author’s settings, bs=64)**  
  - **MMLU:** **61.10** (vs **55.53** base)  
  - **MMLU-Pro:** **33.44** (vs **32.61** base) – harder 10-choice variant.  
  - **IFEVAL:** **63.55** (vs **63.67** base) – verifiable instruction following.
  
_Note:_ Arcee’s internal evals may use different harnesses; avoid cross-harness comparisons.

---

## What’s inside

### Specialization steps

1. **Domain SFT (medical + tools)**  
   Instruction-style synthetic medical Q&A + conversions; supervised **search/tool-use traces** to teach function-calling patterns compatible with chat templates.

2. **Preference alignment — DPO**  
   Uses **MedMCQA** correctness as a proxy preference signal to bias toward concise, clinically reasonable options.

3. **Reasoning enrichment — GRPO (CoT)**  
   **Group Relative Policy Optimization** without a critic; groups of sampled solutions are scored by **verifiable rewards** (answer correctness + light format checks). Trained with **MedReason** QA signal.

4. **Finalization — Arcee Fusion (MergeKit)**  
   **Selective** weight fusion to preserve gains while limiting over-averaging; configured via `merge_method: arcee_fusion`.

---

## Intended use & limitations

**Intended:** Medical SLM's **research**, tool-augmented retrieval demos.

**Out of scope:** Unsupervised patient care, generating prescriptions, and time-critical guideline decisions.

---

## Evaluation

> Author-run with the EleutherAI `lm-evaluation-harness`; seeds, prompts, and templates affect absolute scores.

| Benchmark | AFM-4.5B-OpenMed | AFM-4.5B (same harness) |
|---|---:|---:|
| **MMLU** | **61.10** | 55.53 |
| **MMLU-Pro** | **33.44** | 32.61 |
| **IFEVAL** | 63.55 | **63.67** |

- **MMLU-Pro** increases difficulty (10 options; more reasoning-heavy); small deltas are still meaningful.
- **IFEVAL** checks **verifiable** constraints (length, keyword counts, format, etc.).


| mmlu                  | AFM-4.5B-OpenMed | AFM-4.5B |
| :-------------------- | :--------------- | :------- |
| **other**             |                  |          |
| clinical_knowledge    | 67.55            | 65.66    |
| college_medicine      | 64.74            | 54.34    |
| professional_medicine | 63.97            | 59.56    |
| virology              | 49.4             | 48.19    |
| **stem**              |                  |          |
| anatomy               | 62.96            | 56.3     |
| college_biology       | 78.47            | 65.97    |
| college_chemistry     | 44.00            | 37.00    |
| high_school_biology   | 79.03            | 71.29    |
| high_school_chemistry | 53.2             | 43.84    |
| **groups**            |                  |          |
| humanities            | 56.13            | 50.46    |
| other                 | 68.97            | 63.47    |
| social sciences       | 73.25            | 68.61    |
| stem                  | 48.91            | 42.53    |


### Reproduce (example commands)

```bash
# MMLU classic
lm_eval --model hf \
  --model_args pretrained=openmed-community/AFM-4.5B-OpenMed,parallelize=True,dtype=bfloat16,trust_remote_code=True \
  --task mmlu \
  --batch_size=64 \
  --apply_chat_template \
  --output_path=results \
  --fewshot_as_multiturn 


# MMLU-Pro (10-choice)
lm_eval --model hf \
  --model_args pretrained=openmed-community/AFM-4.5B-OpenMed,parallelize=True,dtype=bfloat16,trust_remote_code=True \
  --tasks leaderboard_mmlu_pro  \
  --batch_size=64 \
  --apply_chat_template \
  --output_path=results \
  --fewshot_as_multiturn 

# IFEVAL (verifiable instruction following)
lm_eval --model hf \
  --model_args pretrained=openmed-community/AFM-4.5B-OpenMed,parallelize=True,dtype=bfloat16,trust_remote_code=True \
  --tasks leaderboard_ifeval \
  --batch_size=64 \
  --apply_chat_template \
  --output_path=results \
  --fewshot_as_multiturn

```

---

## Quickstart (Transformers)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "openmed-community/AFM-4.5B-OpenMed"
tok = AutoTokenizer.from_pretrained(model_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

messages = [
  {"role": "system", "content": "You are a careful medical assistant. Cite sources and warn this is not medical advice."},
  {"role": "user", "content": "Briefly: cellulitis vs erysipelas differences?"}
]
prompt = tok.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=256, do_sample=False)
print(tok.decode(out[0], skip_special_tokens=True))
```

## Data & training notes

* **SFT data:** Proprietary synthetic medical data + search traces.
* **DPO signal:** Preferences derived from **MedMCQA** multiple-choice correctness.
* **GRPO reward:** Answer-checking + format verifiers; **MedReason** used to shape faithful, short CoT.
* No known PHI; please open an issue if you spot any.

---

## Compatibility & licenses

* **Base model:** AFM-4.5B (Arcee). Refer to the base card/blog for architecture and usage details. License for AFM releases is **Apache 2.0**;
* **Merging:** MergeKit with **Arcee Fusion**; see repo/blog for configuration.

---

## Additional note

We also provide a **non-merged** [openmed-community/AFM-4.5B-OpenMed-RL-CoT](https://huggingface.co/openmed-community/AFM-4.5B-OpenMed-RL-CoT) checkpoint after step 3 (**GRPO**). In our harness, it shows **better CoT** behavior but a significant drop on **IFEVAL**. Consider it if you want maximum reasoning verbosity, then apply your own MergeKit recipe.