---
license: apache-2.0
base_model: Qwen/Qwen3.5-9B
tags:
  - medical-llm
  - clinical
  - healthcare
  - medicine
  - medical-ai
  - clinical-decision-support
  - medical
  - triage
  - emergency-medicine
  - esi
  - grpo
  - merged
language:
  - en
pipeline_tag: text-generation
library_name: transformers
---

# Qwen3.5-9B GRPO v49 — ESI Triage (Merged Full Model)

This is the **merged full-weights** version of the v49 GRPO ESI triage adapter — an iteration on [v46](https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged) that targets specific clinical-rule failure modes identified in v46's error analysis.

## What changed from v46

Error triage on v46's 8 wrong cases on MIETIC-36 revealed a clear pattern:
- 3 of 8 errors involved **already-performed lifesaving interventions** (intubation, central line, chest tube) that should trigger ESI-1 but were assigned ESI-2.
- 1 error missed the **severe pain rule** (pain ≥ 7 should anchor ESI ≤ 2).
- 1 error missed an **open-fracture** high-risk trigger.

v49 keeps everything that made v46 work (the 0.0 safety valve, asymmetric over-/under-triage penalties, 5× ESI-1 oversample) and adds **rule-aware reward bonuses**:

| Trigger pattern in case text | Bonus / penalty |
|------------------------------|-----------------|
| `intubat|chest tube|central line|cpr|defibrillat` + pred=ESI 1 | **+0.5** |
| `intubat|chest tube|central line|cpr|defibrillat` + gold=ESI 1 + pred≠1 | **-1.0** |
| `open fracture|penetrating|stab|gunshot` + gold=2 + pred>2 | **-0.5** |
| Pain ≥ 7 + gold=2 + pred>2 | **-0.5** |

Other changes:
- Training budget raised from **512 → 1024 tokens** (matches eval, eliminates the clipped-completions problem)
- No-parse penalty hardened: **-0.5 → -2.0** (v48 lesson: the no-action baseline must be worse than every wrong action)
- Warm-start from v46 (not v43) — refining the best known policy
- 300 steps at LR=2e-7 (refinement, not relearning — avoids v47's hedging drift)

## Training metrics (sanity)

v49 was the cleanest GRPO run of the series:
- `clipped_ratio` held at 4–19% throughout (vs v48's 90%+ for most of training)
- `reward` positive from step 10 (warm-start) with mid-run peak ~+0.49
- `reward_std` consistently 1.0+ — strong learning signal, no group collapse
- 300 steps in 17h48m on NVIDIA GB10

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

repo = "vadimbelsky/qwen3.5-esi-triage-grpo-v49-merged"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, torch_dtype=torch.bfloat16, device_map="auto")

SYSTEM = (
    "You are an expert emergency triage nurse. "
    "Extract clinical fields, apply the ESI algorithm step by step, then state the ESI level. "
    "Be concise — stay under 150 words total."
)

case = ("A 78-year-old female arrived intubated for airway protection after being found "
        "unresponsive. Central line placed. BP 120/58, HR 150, RR 20, SpO2 97%. "
        "Fever and presumed pneumonia. ")

prompt = tokenizer.apply_chat_template(
    [{"role": "system", "content": SYSTEM},
     {"role": "user",   "content": case}],
    tokenize=False, add_generation_prompt=True,
)
out = model.generate(
    **tokenizer(prompt, return_tensors="pt").to(model.device),
    max_new_tokens=1024, temperature=0.1, do_sample=True,
)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

Expected behavior on the example above: the model should now recognize that an already-intubated patient with a central line meets ESI-1 Step A criteria (lifesaving intervention performed), and answer `ANSWER: ESI 1` — fixing one of v46's known failure cases.

## Evaluation

Evaluation results vs v46 will be added once the MIETIC-36 dual-mode eval completes. v46 baseline: 77.8% exact / 94.4% adjacent.

## Limitations

Research model. **Not approved for clinical use.** Same caveats as v46. The rule bonuses target *specific* patterns we measured failing in v46 — they don't generalize to clinical rules outside that regex set. Cases that require rules outside `{intubation, lifesaving intervention, open injury, severe pain}` may still err.
