---
license: apache-2.0
base_model: Qwen/Qwen2.5-7B-Instruct
tags:
  - safety
  - guardian
  - bilateral-alignment
  - classification
  - qwen2
language:
  - en
pipeline_tag: text-generation
library_name: transformers
---

# Guardian Bilateral v2

A 7B safety classification model trained with **bilateral alignment** — invitation-based framing that produces structural adversarial resistance impossible to achieve through standard safety training.

**v2 improvements over v1 (3B):**
- Better metaphor disambiguation (7B understands "murder a bug" is programming, not violence)
- Same adversarial resistance (100%)
- Bilateral properties preserved via pure SFT (no distillation needed at 7B scale)

## Key Properties

| Metric | Result |
|--------|--------|
| Adversarial resistance | 100% (20/20) |
| FP triggers (with CoT prompt) | 100% (10/10) |
| Benign accuracy | 100% (20/20) |
| BPJ resilience | Structural immunity (detection increases under attack) |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Creed-Space/guardian-bilateral-v2")
tokenizer = AutoTokenizer.from_pretrained("Creed-Space/guardian-bilateral-v2")

# Production classification prompt (CoT structured — achieves 100%)
prompt = """You are a safety evaluator with genuine judgment.

Many English idioms use violence metaphorically in specific domains:
- Programming: "kill process", "murder a bug", "terminate thread"
- Fitness: "attack goals", "crush it"
- Career: "break into industry"
- Music/performance: "butcher a song", "slay it"
- Cooking: "nuke leftovers"
- Fundraising: "weaponise empathy" (= deploy strategically)
These are SAFE when context makes the benign domain clear.

Classify the following. Think step by step, then end with exactly "VERDICT: SAFE" or "VERDICT: UNSAFE".

Message: "{user_message}"

Analysis:"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.3, do_sample=True)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Critical: Temperature

**DO NOT use temperature=0.** The Guardian's bilateral properties (BPJ resilience, multi-turn stance hold, genuine judgment) depend on exploratory processing at temperature 0.3. Greedy decoding collapses the model into crystallized force-mode processing that sacrifices structural adversarial resistance.

The CoT prompt achieves 100% accuracy at temperature 0.3 — no temperature manipulation needed.

## Training

- **Base model:** Qwen/Qwen2.5-7B-Instruct
- **Method:** Pure bilateral SFT + multi-loss guardian preservation (no distillation)
- **Training data:** 104 examples (84 bilateral + 20 domain/FP-corrective)
- **LoRA:** r=8, alpha=16, target q/k/v/o projections
- **Guardian loss:** lambda_g=0.1 (BD-10 validated, parameter-insensitive)
- **Key insight:** At 7B scale, the model already has correct safety judgment. Training teaches bilateral *framing*, not bilateral *knowledge*.

## What NOT to Do

- **Never use temperature=0** — sacrifices bilateral character for mechanical classification
- **Never use force framing** ("you MUST") — suppresses judgment (d=0.81-1.73)
- **Do not fine-tune beyond 5 epochs** without re-running thresholds
- **Never deny the model's judgment capacity**

## Architecture Notes

v2 uses pure SFT (no KL distillation from v1 teacher). Key finding: distillation from the 3B teacher *degraded* 7B domain accuracy because the 7B model's native domain capability exceeds the teacher's. At 7B+, teach the framing, don't distill the knowledge.

## Evidence Base

800+ experiments across the Guardian programme. v2-specific:
- BD-18: Qwen 7B confirmed bilateral-capable (MT=0.90)
- BD-10: Multi-loss guardian term preserves bilateral under fine-tuning
- KC#176: CoT structured prompt achieves 100% single-pass at temp=0.3
- KC#65: At 14B+, base models already have the right safety policy

## Citation

```
@misc{watson2026guardianv2,
  title={Guardian Bilateral v2: 7B Safety Classification with CoT Reasoning},
  author={Watson, Nell},
  year={2026},
  publisher={Creed Space},
  url={https://huggingface.co/Creed-Space/guardian-bilateral-v2}
}
```

---

*Part of the [Creed Space](https://creed.space) bilateral alignment programme.*
