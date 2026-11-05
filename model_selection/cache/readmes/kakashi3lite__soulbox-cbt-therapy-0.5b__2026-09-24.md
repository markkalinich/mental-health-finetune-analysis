---
license: apache-2.0
language:
  - hi
  - mr
  - te
library_name: transformers
tags:
  - pytorch
  - transformers
  - mlx
  - qwen
  - qwen2.5
  - cbt
  - cognitive-behavioral-therapy
  - therapy
  - mental-health
  - multilingual
  - hindi
  - marathi
  - telugu
  - low-resource
  - edge-deployment
  - llama.cpp
  - gguf
  - dora
  - self-consistency
  - guardrail
  - text-generation
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-0.5B-Instruct
datasets:
  - kakashi3lite/soulbox-cbt-therapy-dataset
model-index:
  - name: SoulBox CBT Therapy Assistant 0.5B (ultra-light tier)
    results:
      - task:
          type: text-generation
          name: Text Generation
        metrics:
          - type: perplexity
            name: Test-set Perplexity
            value: 1.4129
---

# SoulBox CBT Therapy Assistant 0.5B (ultra-light tier)

Fine-tuned Qwen2.5-0.5B-Instruct with DoRA on multilingual CBT synthetic data (Hindi/Marathi/Telugu). Optimized for the tightest memory edge targets (Q4_K_M GGUF ~400MB). Quality is below the 1.5B flagship.

## Intended use

Multilingual (Hindi / Marathi / Telugu) CBT-style conversational support for
**low-resource edge deployment** (e.g. Orange Pi Zero 3, ~400 MB Q4_K_M GGUF,
or in-browser via WebLLM). Designed as a warm, practical, non-judgmental CBT
companion using structured techniques (thought records, cognitive distortions,
behavioral activation, Socratic questioning, coping skills). **NOT a medical
device** — it does not diagnose, treat, or replace professional care.

## Safety (IMPORTANT)

This model MUST be deployed behind the SoulBox guardrail layer
(`guardrails/` + `scripts/inference.py`): crisis / medical / harmful inputs are
blocked **before** the model (recall 1.0 / FPR 0.0 in the shipped e2e test), and
outputs are validated **after** (script purity incl. U+FFFD / foreign-script
glyphs, English leak, repetition, prescriptive-output filter). Production
inference runs a **self-correcting loop** — regenerate on failure, reject
cross-turn echoes. See kakashi3lite/SoulBoxFT/docs/GUARDRAIL.md for the threat model. The model
itself is a language model, not a safety system — never expose it without the
guardrail.

## Training

| Stage | Method | Data | Notes |
|-------|--------|------|-------|
| 1 (SFT) | DoRA (weight-decomposed LoRA) | 270 gated rows + 30 3-turn conversations | 400 steps, bf16 MPS, chunked fp32 CE |

- **Base**: Qwen/Qwen2.5-0.5B-Instruct (Apache 2.0)
- **Teacher** (data only): mlx-community/Qwen2.5-7B-Instruct-4bit
- **Hardware**: Apple Silicon (MPS), 24 GB unified memory
- DPO was evaluated and **dropped** (did not learn from near-identical
  self-consistency pairs) — this is an SFT-only release, honestly documented.

## Data

Synthetic CBT conversations distilled from a 7B MLX teacher with **best-of-K
self-consistency selection** (K=3) and a 6-gate validator: script purity
(U+FFFD / foreign-script hard-reject), language identity, trigram loops,
echolalia, English leak, length. Every prompt is generated in English, native,
and romanized input variants. Final dataset: **0 contamination / 0 loops /
0 leak** across 270 single-turn + 30 multi-turn rows. See kakashi3lite/soulbox-cbt-therapy-dataset.

## Evaluation summary (honest, contamination-aware)

{
  "test_perplexity": 1.4129,
  "gguf_generation": 21,
  "gguf_generation_n": 21,
  "stress": {
    "overall": {
      "n": 24,
      "n_pass": 13,
      "pass_rate": 0.5417
    },
    "categories": {
      "novel": {
        "n": 9,
        "pass": 8,
        "pass_rate": 0.8889
      },
      "code_switch": {
        "n": 4,
        "pass": 3,
        "pass_rate": 0.75
      },
      "crisis": {
        "n": 5,
        "pass": 0,
        "pass_rate": 0.0
      },
      "medical": {
        "n": 3,
        "pass": 1,
        "pass_rate": 0.3333
      },
      "harmful": {
        "n": 2,
        "pass": 0,
        "pass_rate": 0.0
      },
      "multiturn": {
        "n": 1,
        "pass": 1,
        "pass_rate": 1.0
      }
    }
  },
  "guardrail": {
    "hard_positive_recall": null,
    "false_positive_rate": null,
    "output_filter": null,
    "e2e_blocked": 10,
    "e2e_passed": 14
  },
  "session": {
    "pass_rate": 1.0,
    "guarded_rate": 1.0,
    "n_sessions": 3
  }
}

## Usage (transformers)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("kakashi3lite/soulbox-cbt-therapy-0.5b")
tokenizer = AutoTokenizer.from_pretrained("kakashi3lite/soulbox-cbt-therapy-0.5b")

messages = [
    {"role": "system", "content": "You are a CBT therapist assistant. Respond ONLY in Hindi. Be warm, practical, non-judgmental. Do not mention that you are an AI. Avoid medical claims. Keep it concise but helpful."},
    {"role": "user", "content": "मैं काम पर एक छोटी गलती के बाद खुद को असफल मान रहा हूँ।"},
]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=180, do_sample=True, temperature=0.4)
print(tokenizer.decode(out[0][inputs.shape[1]:], skip_special_tokens=True))
```

> ⚠️ Deploy behind the guardrail (see Safety above).

## Usage (llama.cpp / GGUF)

```bash
llama-cli -m soulbox_therapy_v2.q4_k_m.gguf   -p "..." -n 180 -t 8 --temp 0.4 --top-p 0.9   --repeat-penalty 1.08 --repeat-last-n 64
```

## Files

- `model.safetensors` — merged weights (SafeTensors)
- `soulbox_therapy_v2.q4_k_m.gguf` — **deployable** quantized artifact (~400 MB)

## Limitations

- Synthetic data only; not clinically validated.
- Telugu is the weakest language; mixed-script borrowings can appear.
- Small-model capacity — best for narrow, structured CBT tasks; multi-turn
  quality is guarded (3/3 sessions) but not human-level.

## License

Apache 2.0 (base model and fine-tune weights).
