



---
language:
  - en
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen1.5-1.8B-Chat
tags:
  - emotions
  - vad
  - dialogue
  - multi-label
  - empathy
  - psychology
  - evaluation
datasets:
  - OpenDataLab/DailyDialog
  - goemotions
  - empathetic_dialogues
model-index:
  - name: Emoloom-2B
    results:
      - task:
          type: text-classification
          name: Multi-label Emotion + VAD (in-text JSON)
        dataset:
          name: Mixed (GoEmotions + Empathetic Dialogues)
          type: custom
        metrics:
          - type: macro_f1
            value: 0.350
          - type: macro_precision
            value: 0.500
          - type: macro_recall
            value: 0.269
          - type: vad_1_minus_rmse
            value: 0.942
          - type: parse_ok
            value: 1.000
      - task:
          type: zero-shot-eval
          name: Cross-corpus Quick Eval (DailyDialog)
        dataset:
          name: OpenDataLab/DailyDialog
          type: dialog
        metrics:
          - type: macro_f1
            value: 0.307
          - type: vad_1_minus_rmse
            value: 0.807
          - type: parse_ok
            value: 0.976
---

# Emoloom-2B

**Emoloom-2B** is a ~2B-parameter emotion understanding model that outputs **multi-label emotion categories** and **continuous VAD** (Valence, Arousal, Dominance) for dialogue utterances. It is fine-tuned from **Qwen/Qwen1.5-1.8B-Chat** with SFT on a curated mix of GoEmotions and Empathetic Dialogues, plus consistency constraints to keep JSON outputs robust and parsing-friendly.

> Output format (single line JSON):
> `{"labels": ["sad","anxious"], "vad": {"v": 0.42, "a": 0.31, "d": 0.28}, "rationale": "short evidence"}`

---

## ✨ Highlights

- **Dual signal**: multi-label categories + continuous VAD in \[0,1], two decimals.
- **Robust JSON**: training disables KV cache during generation for consistent formatting.
- **Long-tail focus**: sampling and weak-label cleanup reduce “mode collapse” onto majority classes.
- **Paper-ready figures**: bundled plotting code exports high-res bar/radar/CI-band PNGs.

---

## 📊 Results (dev & cross-corpus)

| Exp                        | Macro-F1 | Macro-P | Macro-R | VAD(1-RMSE) | ParseOK | n(dev) |
|---------------------------:|:--------:|:-------:|:-------:|:-----------:|:-------:|-------:|
| `sft_qwen_mix2080`         | **0.3500** | 0.5000 | 0.2693 | **0.9417**  | 1.000   | 3663   |
| `sft_qwen_mix5050`         | 0.3470   | 0.5000 | 0.2657 | 0.9337      | 1.000   | 3309   |
| `sft_qwen_mix8020`         | 0.3341   | 0.5000 | 0.2509 | 0.9135      | 1.000   | 2068   |
| `sft_qwen_mix2080_dd_quick` (DailyDialog, quick) | 0.3071 | 0.5000 | 0.2136 | 0.8066 | 0.976 | 6261 |

Notes:
- `ParseOK` = fraction of generations that are valid, one-line JSON.
- VAD score is reported as **1 − RMSE** (higher is better).

---

## 🧠 Model Details

- **Base**: `Qwen/Qwen1.5-1.8B-Chat`
- **Size**: ~1.8B params
- **Architecture**: causal decoder-only transformer
- **Precision**: BF16 training, eval in BF16/FP16/FP32 fallback
- **Tokenizer**: Qwen tokenizer (pad set to EOS if missing)

---

## 🧾 Training Data & Processing

- **Sources**: GoEmotions (multi-label), Empathetic Dialogues (dialogue empathy).
- **Mixing**: ratios explored (20:80, 50:50, 80:20); **20:80** gave the best trade-off.
- **QC**: remove toxic/unclear; enforce min VAD confidence; short rationale template.
- **Target JSON**: `{labels, vad:{v,a,d}, rationale}` with two-decimal VAD.

---

## ⚙️ Fine-tuning Setup (SFT)

- **Max length**: typically 1024–1536 tokens (adaptive truncation for stability)
- **Batch**: micro-batch 1, gradient accumulation up to 128 (OOM-safe)
- **LR**: ~1.2e-5 cosine decay, warmup ~3%
- **Stability**: gradient checkpointing; `use_cache=False` at train/eval

---

## ✅ Evaluation

- Prompts build a short **system** + **user** pair (context + utterance).
- Greedy decode, max_new_tokens ~196 (quick eval uses 48).
- Metrics:
  - Multi-label **Macro-F1 / P / R** on gold label space
  - VAD **1−RMSE** on \[v,a,d]
  - **ParseOK** for JSON validity

---

## 🚀 Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import json, torch

name = "Lixeeone/Emoloom-2B"
tok = AutoTokenizer.from_pretrained(name, trust_remote_code=True, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(name, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True)
if tok.pad_token_id is None:
    tok.pad_token = tok.eos_token
model.config.use_cache = False  # keep output format stable

context = "We argued last night but made up this morning."
utterance = "I’m still a bit shaken though."

sys = ("You are an empathetic assistant. Identify emotion labels (multi-label) "
       "and estimate VAD (Valence, Arousal, Dominance in [0,1]). Respond with STRICT one-line JSON only.")
usr = (
    "Task: Read the text and provide emotion labels and VAD with two decimals, plus a brief rationale (<=30 words).\n"
    "Return JSON ONLY, single line:\n"
    '{{"labels": [...], "vad": {{"v": 0.00, "a": 0.00, "d": 0.00}}, "rationale": "..."}}\n'
    f"Context: {context}\n"
    f'Text: "{utterance}"'
)

msgs = [{"role":"system","content":sys},{"role":"user","content":usr}]
prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
inp = tok(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    out = model.generate(**inp, max_new_tokens=128, do_sample=False, use_cache=False)
gen = tok.decode(out[0][inp["input_ids"].shape[1]:], skip_special_tokens=True)

pred = json.loads(gen)  # {"labels":[...], "vad":{"v":..,"a":..,"d":..}, "rationale": "..."}
print(pred)



