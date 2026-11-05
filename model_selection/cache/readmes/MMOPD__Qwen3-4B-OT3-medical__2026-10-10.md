---
license: apache-2.0
base_model: MMOPD/Qwen3-4B-OT3-2ep
language:
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- qwen3
- medical
- reasoning
- thinking
- sft
- distillation
- mmopd
datasets:
- GBaker/MedQA-USMLE-4-options
---

# Qwen3-4B-OT3-medical (medical teacher, SFT)

`Qwen3-4B-OT3-medical` is the **medical domain teacher** of the MMOPD study: `MMOPD/Qwen3-4B-OT3-2ep` further fine-tuned
(supervised) on verified long-chain-of-thought answers that a much stronger model (Qwen3.6-35B-A3B, MedQA 94.6%) produced for
MedQA training questions. Only traces whose final answer matched the gold letter were kept (rejection sampling), at most 3
distinct traces per question. It raises MedQA from 69.8 to 80.7 while keeping the general Qwen3 thinking format.

## Training

|  |  |
|---|---|
| init | `MMOPD/Qwen3-4B-OT3-2ep` |
| data | 40,853 verified teacher traces on MedQA-USMLE training questions in 4-option (20,360) and 5-option (20,493) form (15,427 prompt variants), 8-gram decontaminated against the evaluation sets |
| trace teacher | Qwen3.6-35B-A3B, 8 samples per question at temperature 1.0, keep the correct ones (up to 3, shortest first), thinking part capped at 16k characters |
| recipe | SFT, 4 epochs, LR 1e-5 (5% warmup), max length 8,192, flatten packing, bf16 + ZeRO-2; final checkpoint (step 3,368) |

## Evaluation

Domain benchmarks (temperature 1.0, top-p 1.0, long generation budget; accuracy in %):

| Model | MedQA | MedXpertQA | PubMedQA | CaseHOLD | FinQA | TAT-QA (EM) |
|---|---|---|---|---|---|---|
| Qwen3-4B-OT3-medical (this) | 80.7 | 22.3 | 77.2 | 59.8 | 54.0 | – |
| Qwen3-4B-OT3-2ep (student init) | 69.8 | 13.7 | 75.2 | 63.2 | 58.3 | 24.4 |
PubMedQA = accuracy (macro-F1 57.4 vs 56.6 for the init).
General benchmarks (Qwen3 thinking preset: temperature 0.6, top-p 0.95, top-k 20; 32,768 max new tokens; AIME = avg@8, LiveCodeBench v6 / IFEval / IFBench = 1 sample; scores in %):

| Model | AIME24 | AIME25 | AIME26 | LiveCodeBench v6 | IFEval | IFBench |
|---|---|---|---|---|---|---|
| Qwen3-4B-OT3-medical (this) | 52.9 | 45.0 | 40.0 | 39.9 | 41.2 | 27.0 |
| Qwen3-4B-OT3-2ep (student init) | 66.3 | 56.3 | 58.3 | 51.7 | 51.0 | 27.7 |

## Notes

- Weights are stored in bfloat16. Apache-2.0.
- Domain scores are measured at temperature 1.0 because that is the sampling regime in which these models serve as
  distillation teachers; general benchmarks use the Qwen3 thinking preset.
- Part of the MMOPD model family together with `MMOPD/Qwen3-4B-OT3-{1ep,2ep}`, `MMOPD/Qwen3-1.7B-OT3-{1ep,2ep}` and the
  other domain teachers `MMOPD/Qwen3-4B-OT3-{medical,law,finance,if}`.

## How to use

The models keep the Qwen3 chat template and thinking format (`<think> ... </think>` before the answer). Use
`enable_thinking=True` and sampling (not greedy); the evaluations below used a 32k-token generation budget.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
repo = "MMOPD/Qwen3-4B-OT3-medical"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype="auto", device_map="auto")
messages = [{"role": "user", "content": "A 45-year-old man presents with sudden severe chest pain radiating to the back and a blood pressure difference between arms. What is the most likely diagnosis?"}]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
out = model.generate(**tok(text, return_tensors="pt").to(model.device), max_new_tokens=32768,
                     do_sample=True, temperature=0.6, top_p=0.95, top_k=20)
print(tok.decode(out[0], skip_special_tokens=True))
```

vLLM: `vllm serve MMOPD/Qwen3-4B-OT3-medical --max-model-len 40960` (the same sampling settings apply).
