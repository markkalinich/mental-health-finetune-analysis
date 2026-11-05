---
license: cc-by-sa-4.0
language:
- en
base_model:
- google/flan-t5-large
library_name: transformers
tags:
- poetry
- meter 
- stress 
- flan-t5 
- lora 
- eighteenth-century-poetry
---

# KemiOm/poetry-combined-best

`KemiOm/poetry-combined-best` is a LoRA-adapted `google/flan-t5-large` model for English poetry generation with explicit structural constraints, especially **meter** and **rhyme**.  
This checkpoint represents the best-performing combined run from a multi-round fine-tuning workflow.

## Model Description

- **Model type:** Seq2seq language model flan-t5-large with LoRA adapters
- **Primary task:** Constraint-aware poetry generation
- **Focus constraints:** Stress/meter conformity and end-rhyme pattern adherence
- **Domain:** Predominantly eighteenth-century English poetic style plus preprocessing for modern compatibility where applicable

## Intended Uses

- Creative writing assistance for metrically constrained verse
- Research experiments in form-constrained generation
- Educational demos on meter, stress, and rhyme control in language models
- Rapid prototyping of poetry prompts requiring line-level formal structure

## Training Data

This model is fine-tuned on an English poetry corpus curated for line-level form analysis.

- **Genre emphasis:** Formal verse with strong metrical/rhyme signals
- **Data processing goals:**
  - normalize punctuation and line breaks
  - extract/encode stress and meter targets
  - mark rhyme targets from line-end tokens
- **Split strategy:** train/validation/test 

> Replace dataset references with exact public/private IDs and include any additional licensing notes for upstream poem sources.

## Preprocessing

The preprocessing pipeline includes:

1. text normalization (quotes, whitespace, punctuation variants),
2. line segmentation and stanza preservation,
3. stress pattern estimation (dictionary + heuristic fallback),
4. meter label assignment (iambic pentameter target strings),
5. rhyme label extraction and scheme encoding (AABB/ABAB/etc.),
6. prompt-target formatting for text-to-text training.

## Task Definition

`KemiOm/poetry-combined-best` performs **combined line-level structure evaluation** for poetry.

Given an input line, the model predicts a structured label string:

`stress:<pattern>|meter_type:<meter>|rhyme:<phones>|end:<0_or_1>|caesura:<index_or_->`

Where:

- `stress`: token-level stress sequence pattern
- `meter_type`: predicted metrical class (e.g., iambic pentameter)
- `rhyme`: phonetic rhyme representation of the line ending
- `end`: end-of-unit flag (`1` if line ends a unit, else `0`)
- `caesura`: caesura position or `-` if none

## Training Procedure

- **Base model:** `google/flan-t5-large`
- **Adaptation method:** LoRA
- **Framework:** Hugging Face `transformers` + PEFT
- **Objective:** Conditional generation under form constraints
- **Selection criterion:** Best combined validation performance on meter + rhyme objectives


Best combined run parameters (from `round2/combined/run_params.json`):
- **Base model:** `google/flan-t5-large`
- **Adaptation:** LoRA
- **LoRA rank (`r`):** `32`
- **LoRA alpha:** `64`
- **LoRA dropout:** `0.05`
- **LoRA target modules:** `q,k,v,o`
- **Epochs:** `5.0`
- **Learning rate:** `5e-05`
- **Weight decay:** `0.01`
- **Warmup ratio:** `0.1`
- **Train batch size (per device):** `8`
- **Gradient accumulation:** `2`
- **Effective batch size:** `16` per device group (multiply by number of GPUs if distributed)
- **Eval batch size (per device):** `4`
- **Max input length:** `384`
- **Max target length:** `128`
- **Eval/Save interval:** every `300` steps
- **Seed:** `42`
- **Precision flags:** `no_fp16=true`, `bf16=false`
- **Max steps:** `-1` (epoch-based)
- **Merge adapters after training:** `true`


## Example Use
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_id = "KemiOm/poetry-combined-best"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
prompt = "Tired Nature's sweet restorer, balmy Sleep!"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_new_tokens=180,
    do_sample=True,
    temperature=0.8,
    top_p=0.95
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
