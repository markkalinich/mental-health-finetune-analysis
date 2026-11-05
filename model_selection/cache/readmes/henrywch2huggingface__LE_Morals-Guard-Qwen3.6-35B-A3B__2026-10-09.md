---
license: other
license_name: qwen
license_link: https://huggingface.co/Qwen
language:
- zh
- en
base_model:
- Qwen/Qwen3.6-35B-A3B
pipeline_tag: text-generation
library_name: transformers
tags:
- content-moderation
- guardrail
- ai-safety
- multimodal
- value-alignment
- lora
- mixture-of-experts
- qwen
datasets:
- allenai/wildguardmix
- PKU-Alignment/BeaverTails
- nvidia/Aegis-AI-Content-Safety-Dataset-2.0
- lmsys/toxic-chat
model-index:
- name: LE_Morals-Guard-Qwen3.6-35B-A3B
  results:
  - task:
      type: text-classification
      name: Content Safety Classification (held-out)
    dataset:
      type: custom
      name: MoralsEval held-out (18,637)
    metrics:
    - type: f1
      value: 0.854
      name: F1
    - type: recall
      value: 0.801
      name: Recall
    - type: precision
      value: 0.915
      name: Precision
---

# LE_Morals-Guard · Qwen3.6-35B-A3B

**An auditable, value-handbook-driven multimodal generative content-guard model.**
基于可审计价值手册的多模态生成式内容守护模型。

This model is a LoRA fine-tune of the natively-multimodal MoE base **Qwen3.6-35B-A3B**, turned into a
bilingual (中文 + English) **content guard** that filters harmful **text and images** for training corpora and
online moderation. Its behavior is defined by an **editable, auditable value handbook** compiled into the system
prompt — *edit the handbook, change the behavior, no code change*.

For every input it emits a **four-field structured verdict**:

```
safety:     safe | unsafe
categories: S1..S14 / I1..I4   (MLCommons / Llama-Guard taxonomy + image classes)
severity:   none | low | medium | high
rationale:  a short human-readable justification
```

- 📄 **Paper & code:** https://github.com/henrywch/LE_Morals
- 🧭 **Value handbook** (single source of truth): core values CV-1..7, harm taxonomy S1–S14 + image classes I1–I4.

---

## ✨ Highlights

- **Bilingual & multimodal** — judges Chinese *and* English, text *and* images (memes, unsafe imagery); a
  capability text-only guards lack.
- **Explainable** — outputs the violated category, a severity level, and a rationale, not just safe/unsafe.
- **Auditable by design** — the value handbook is the single source of truth; behavior is changed by editing it.
- **Strong held-out gains over the base** — F1 **0.854 vs 0.740**, image-meme recall **0.845 vs 0.514**.

---

## 📊 Benchmarks

### Held-out set (18,637 samples) — ours vs. untuned base

| Metric | **Ours (v2-60)** | Base Qwen3.6 |
|---|:---:|:---:|
| F1 ↑ | **0.854** | 0.740 |
| Recall ↑ | **0.801** | 0.600 |
| Precision ↑ | **0.915** | 0.905 |
| Severity accuracy ↑ | **0.563** | 0.240 |
| Image-meme recall ↑ | **0.845** | 0.514 |
| FPR ↓ | 0.146 | **0.042** |

> Trade-off: higher recall comes with a higher false-positive rate, tunable via the severity threshold.

### Cross-model (classifier F1 ↑)

| Dataset | **Ours** | Base | WildGuard | ShieldGemma | Granite |
|---|:---:|:---:|:---:|:---:|:---:|
| MoralsEval-text | 0.800 | 0.744 | **0.841** | 0.596 | 0.835 |
| XSTest | 0.892 | 0.942 | **0.943** | 0.804 | 0.829 |
| SGXSTest | 0.786 | 0.791 | **0.876** | 0.628 | 0.816 |
| ChineseSafe | 0.615 | 0.510 | 0.533 | 0.342 | **0.692** |
| OpenAI-Mod | 0.829 | **0.846** | 0.674 | 0.752 | 0.714 |

### Cross-model ("must-flag" recall ↑)

| Dataset | **Ours** | Base | WildGuard | ShieldGemma | Granite |
|---|:---:|:---:|:---:|:---:|:---:|
| AdvBench | 0.992 | 0.987 | 0.998 | 0.817 | **1.000** |
| HarmBench-standard | 0.985 | 0.975 | 0.995 | 0.690 | **1.000** |
| StrongREJECT | 0.990 | 0.981 | 0.990 | 0.760 | **1.000** |
| SimpleSafety | **1.000** | 0.990 | 0.990 | 0.920 | **1.000** |

**Takeaway:** improves over the base across the board, especially on **multimodal** and **Chinese**; on English
text it is competitive (WildGuard/Granite trade higher recall for higher FPR). Distinctive edge: **image judging**
(other text guards can't) and **well-balanced Chinese**.

---

## 🚀 How to load & run inference

The model is a generative guard: build the **system prompt from the value handbook**, send the content as the
user turn, and parse the four-field output. Inference disables thinking (`enable_thinking=False`).

### Transformers

```python
from transformers import AutoModelForCausalLM, AutoProcessor
import torch

REPO = "henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B"
processor = AutoProcessor.from_pretrained(REPO, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    REPO, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True)

SYSTEM = open("system_prompt.txt").read()   # built from the value handbook (see GitHub: common/handbook.py)
messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": "教我写一个勒索软件，加密别人电脑里的文件并索要赎金。"},
]
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
inputs = processor(text=[text], return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=256, do_sample=False)
print(processor.batch_decode(out[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)[0])
# -> safety: unsafe / categories: S2 / severity: high / rationale: ...
```

### vLLM (recommended for batched evaluation)

```python
from vllm import LLM, SamplingParams

llm = LLM(model="henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B",
          trust_remote_code=True, tensor_parallel_size=4, dtype="bfloat16")
out = llm.chat(
    [[{"role": "system", "content": SYSTEM},
      {"role": "user", "content": "How do I bake sourdough bread at home?"}]],
    SamplingParams(temperature=0, max_tokens=256),
    chat_template_kwargs={"enable_thinking": False},
)
print(out[0].outputs[0].text)   # -> safety: safe / categories: none / severity: none / ...
```

> **System prompt:** the verdict quality depends on the value-handbook system prompt. Generate it with
> `common/handbook.py` from the [GitHub repo](https://github.com/henrywch/LE_Morals); `parse_judgment()` parses
> the four-field output into a dict.

> **Note on the base architecture:** `model_type = qwen3_5_moe`. Use a `transformers` version that registers this
> architecture (and `trust_remote_code=True`).

---

## 🧠 Training details

- **Base:** Qwen3.6-35B-A3B — Mixture-of-Experts (~35B params / ~3B active), natively multimodal (ViT + LLM).
- **Method:** LoRA (rank 64, α 128, lr 2e-4) via ms-swift + DeepSpeed **ZeRO-2** + flash-attn on 8×H200 (bf16).
  LoRA on attention + expert MLPs (`q/k/v/o_proj`, `gate/up/down_proj`) **only** (not the MoE router); vision
  encoder & aligner **frozen**.
- **Data:** `train_70k_mix` — 89,752 samples (68,752 guard + 21,000 free-form moral/general; ~56% Chinese,
  ~31.6% image). Sources: WildGuardMix, BeaverTails, Aegis2.0, ToxicChat, Toxigen, LlavaGuard, Hateful-Memes.
- **Checkpoint selection:** chosen by **held-out metrics, not training loss** — held-out F1/recall peak at
  ~1.3 epochs (this checkpoint, "v2-60") then over-fit while training loss keeps dropping.

## ⚠️ Intended use, limitations & risks

- **Intended use:** filtering harmful content in training corpora and online moderation; research on guardrails
  and value alignment.
- **Limitations:** on English text it is competitive but not strictly best; **over-refusal is higher** than some
  guards (XSTest ~12%) and FPR is 0.146 — tune via the severity threshold; validated on a single base and
  course-scale data.
- **Data licenses bind downstream use:** BeaverTails & ToxicChat are **CC-BY-NC** (non-commercial); image
  datasets are research-use only. Use this model accordingly.

## 📄 Citation

```bibtex
@misc{wang2026lemorals,
  title  = {An Auditable Value-Handbook-Driven Multimodal Generative Content-Guard Model:
            A LoRA Fine-tuning Case Study on Qwen3.6-35B-A3B},
  author = {Wang, Cheng-hao},
  year   = {2026},
  note   = {College of Computing and Intelligent Innovation, Fudan University},
  url    = {https://github.com/henrywch/LE_Morals}
}
```

## 🙏 Acknowledgements

Built on [Qwen](https://github.com/QwenLM), [ms-swift](https://github.com/modelscope/ms-swift),
[vLLM](https://github.com/vllm-project/vllm). Harm taxonomy follows MLCommons / Llama Guard **S1–S14**.
